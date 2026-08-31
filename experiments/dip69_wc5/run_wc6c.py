#!/usr/bin/env python3
import json,time,tempfile,subprocess,shutil,re
from collections import Counter,defaultdict
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).parent))
import run_wc5 as m

OUT=Path("wc6c_output")
OUT.mkdir(exist_ok=True)
MODES=("STRICT_JSON","PROMPT_JSON")
ANCHORS=("A00","A10","A01","A11")
POLICIES=("I","D")
REGIMES=("reset","warm")


def groq_curl(messages,mode):
    payload={
        "model":m.MODEL,
        "messages":messages,
        "reasoning_effort":"medium",
        "reasoning_format":"hidden",
        "temperature":0.6,
        "top_p":0.95,
        "max_completion_tokens":2048,
        "stream":False,
    }
    if mode=="STRICT_JSON":
        payload["response_format"]={"type":"json_object"}
    elif mode!="PROMPT_JSON":
        raise RuntimeError("UNKNOWN_MODE:"+mode)

    while True:
        td=Path(tempfile.mkdtemp(prefix="wc6c_curl_"))
        req=td/"request.json"; resp=td/"response.json"; hdr=td/"headers.txt"
        req.write_text(json.dumps(payload,ensure_ascii=False))
        p=subprocess.run([
            "curl","-sS","-D",str(hdr),"-o",str(resp),"-w","%{http_code}",m.ENDPOINT,
            "-H",f"Authorization: Bearer {m.KEY}","-H","Content-Type: application/json",
            "--data-binary",f"@{req}"
        ],text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        code=p.stdout.strip()
        body=resp.read_text() if resp.exists() else p.stderr
        headers=hdr.read_text() if hdr.exists() else ""
        shutil.rmtree(td,ignore_errors=True)
        if code=="429":
            mm=re.search(r"(?im)^retry-after:\s*([0-9.]+)",headers)
            wait=float(mm.group(1)) if mm else 8.0
            time.sleep(min(max(wait,1),60))
            continue
        if code!="200":
            if code=="400" and "json_validate_failed" in body:
                raise RuntimeError("PROVIDER_JSON_VALIDATE_FAIL:"+body[:700])
            raise RuntimeError(f"GROQ_CURL_HTTP_{code}:{body[:700]}")
        obj=json.loads(body)
        if obj.get("model")!=m.MODEL:
            raise RuntimeError("MODEL_MISMATCH:"+str(obj.get("model")))
        text=obj["choices"][0]["message"].get("content") or ""
        if not text.strip():
            raise RuntimeError("EMPTY_MODEL_CONTENT")
        return text,obj.get("usage",{})


def error_class(err):
    s=str(err)
    prefixes=(
        "PROVIDER_JSON_VALIDATE_FAIL","GROQ_CURL_HTTP_","MODEL_MISMATCH","EMPTY_MODEL_CONTENT",
        "JSON_PARSE_FAIL","BAD_REPLACEMENTS","BAD_REPLACEMENT_KEYS","BAD_REPLACEMENT_VALUE",
        "FILE_SCOPE_FAIL","OLD_OCCURRENCE_FAIL","INVERT_BOUNDARY_MARKER_MISSING",
        "INVERT_SHARED_BOUNDARY_NOT_USED_BOTH_FILES","DIRECT_INTRODUCED_FORBIDDEN_BOUNDARY",
        "NO_SOURCE_CHANGE","CMD_FAIL","DYNAMIC_ORACLE_FAIL","DYNAMIC_ORACLE_NO_PASS"
    )
    for p in prefixes:
        if s.startswith(p):
            if p=="GROQ_CURL_HTTP_":
                return s.split(":",1)[0]
            return p
    return "OTHER_FAIL"


def one(base_dir,anchor,policy,regime,mode):
    identity=f"{anchor}-r1-{policy}-{regime}"
    cid=f"{identity}-{mode}"
    work=Path(tempfile.mkdtemp(prefix="wc6c_"))
    shutil.copytree(base_dir,work/"repo",dirs_exist_ok=True)
    root=work/"repo"
    rec={
        "id":cid,"identity":identity,"anchor":anchor,"replicate":1,
        "policy":policy,"regime":regime,"mode":mode,"phase":0,
        "status":"HOLD","stage":"INIT"
    }
    try:
        packet=m.extract_packet(root,anchor)
        prompt=m.build_prompt(anchor,policy,0,packet)
        messages=m.messages_for(regime,prompt)
        rec["stage"]="SERVE"
        text,usage=groq_curl(messages,mode)
        rec.update(served=True,model=m.MODEL,usage=usage,output=text)
        rec["stage"]="PARSE_APPLY"
        before,after,changed=m.parse_and_apply(root,text,anchor,policy)
        rec.update(changed_files=changed)
        rec["stage"]="VALIDATE"
        m.validate(root,anchor,0)
        rec.update(status="PASS",stage="PASS",error_class=None)
    except Exception as e:
        rec.update(error=str(e)[:1800],error_class=error_class(e))
    finally:
        shutil.rmtree(work,ignore_errors=True)
    return rec


def main():
    td=Path(tempfile.mkdtemp(prefix="wc6c_base_"))
    base=td/"base"
    m.clone_base(base)
    records=[]
    try:
        # Frozen identity order. Each identity is independently re-instantiated from the exact base.
        for anchor in ANCHORS:
            for policy in POLICIES:
                for regime in REGIMES:
                    for mode in MODES:
                        rec=one(base,anchor,policy,regime,mode)
                        records.append(rec)
                        print("WC6C",rec["id"],rec["status"],rec.get("error_class"),flush=True)
    finally:
        shutil.rmtree(td,ignore_errors=True)

    with (OUT/"results.jsonl").open("w") as f:
        for r in records:
            f.write(json.dumps(r,ensure_ascii=False)+"\n")

    by_mode={}
    for mode in MODES:
        rs=[r for r in records if r["mode"]==mode]
        by_mode[mode]={
            "n":len(rs),
            "pass":sum(r["status"]=="PASS" for r in rs),
            "hold":sum(r["status"]!="PASS" for r in rs),
            "error_classes":dict(Counter(r.get("error_class") or "PASS" for r in rs))
        }

    paired=[]
    lookup={(r["identity"],r["mode"]):r for r in records}
    for anchor in ANCHORS:
        for policy in POLICIES:
            for regime in REGIMES:
                identity=f"{anchor}-r1-{policy}-{regime}"
                a=lookup[(identity,"STRICT_JSON")]; b=lookup[(identity,"PROMPT_JSON")]
                paired.append({
                    "identity":identity,
                    "strict_status":a["status"],"strict_error":a.get("error_class"),
                    "prompt_status":b["status"],"prompt_error":b.get("error_class"),
                    "pass_switch":f"{a['status']}->{b['status']}"
                })

    switch_counts=Counter(x["pass_switch"] for x in paired)
    summary={
        "authority":"ZERO_CORE_MEASUREMENT_CALIBRATION_ONLY",
        "model":m.MODEL,"base":m.BASE,
        "identities":16,"calls":32,"phase":0,
        "modes":by_mode,
        "paired_switches":dict(switch_counts),
        "core_inference":"PROHIBITED",
        "next":"MANDATORY_PI_RECOURT"
    }
    (OUT/"paired.json").write_text(json.dumps(paired,ensure_ascii=False,indent=2))
    (OUT/"summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    print("EVONOMOS_WC6C_SUMMARY",json.dumps(summary,separators=(",",":")),flush=True)

if __name__=="__main__":
    main()
