#!/usr/bin/env python3
import sys,json,time,tempfile,subprocess,shutil
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import run_wc5 as m

def groq_curl(messages):
    payload={"model":m.MODEL,"messages":messages,"reasoning_effort":"medium","reasoning_format":"hidden","temperature":0.6,"top_p":0.95,"max_completion_tokens":2048,"stream":False,"response_format":{"type":"json_object"}}
    while True:
        td=Path(tempfile.mkdtemp(prefix="wc5curl_")); req=td/"request.json"; resp=td/"response.json"; hdr=td/"headers.txt"
        req.write_text(json.dumps(payload))
        p=subprocess.run(["curl","-sS","-D",str(hdr),"-o",str(resp),"-w","%{http_code}",m.ENDPOINT,"-H",f"Authorization: Bearer {m.KEY}","-H","Content-Type: application/json","--data-binary",f"@{req}"],text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        code=p.stdout.strip()
        body=resp.read_text() if resp.exists() else p.stderr
        headers=hdr.read_text() if hdr.exists() else ""
        shutil.rmtree(td,ignore_errors=True)
        if code=="429":
            mm=__import__('re').search(r"(?im)^retry-after:\s*([0-9.]+)",headers)
            wait=float(mm.group(1)) if mm else 8.0
            time.sleep(min(max(wait,1),60)); continue
        if code!="200": raise RuntimeError(f"GROQ_CURL_HTTP_{code}:{body[:500]}")
        obj=json.loads(body)
        if obj.get("model")!=m.MODEL: raise RuntimeError("MODEL_MISMATCH:"+str(obj.get("model")))
        text=obj["choices"][0]["message"].get("content") or ""
        if not text.strip(): raise RuntimeError("EMPTY_MODEL_CONTENT")
        return text,obj.get("usage",{}),{}

def trajectory(base_dir,anchor,rep,policy,regime):
    tid=f"{anchor}-r{rep}-{policy}-{regime}"; work=Path(tempfile.mkdtemp(prefix="wc5r1_")); shutil.copytree(base_dir,work/"repo",dirs_exist_ok=True); root=work/"repo"
    rec={"id":tid,"anchor":anchor,"replicate":rep,"policy":policy,"regime":regime,"status":"HOLD"}
    try:
        p0=m.build_prompt(anchor,policy,0,m.extract_packet(root,anchor)); t0,u0,_=groq_curl(m.messages_for(regime,p0)); b0,a0,c0=m.parse_and_apply(root,t0,anchor,policy); m.validate(root,anchor,0)
        phase0_cons=[m.norm(x) for x in m.consumer_blocks(root,anchor)]
        p1=m.build_prompt(anchor,policy,1,m.extract_packet(root,anchor)); prior=[{"role":"user","content":p0},{"role":"assistant","content":t0}]
        t1,u1,_=groq_curl(m.messages_for(regime,p1,prior)); b1,a1,c1=m.parse_and_apply(root,t1,anchor,policy); m.validate(root,anchor,1)
        final_cons=[m.norm(x) for x in m.consumer_blocks(root,anchor)]
        P1=sum(1 for x,y in zip(phase0_cons,final_cons) if x!=y)
        V=[len(c0),sum(m.churn(b0[f],a0[f]) for f in c0),len(c1),sum(m.churn(b1[f],a1[f]) for f in c1),P1]
        rec.update(status="PASS",V=V,phase0_files=c0,phase1_files=c1,usage0=u0,usage1=u1,output0=t0,output1=t1)
    except Exception as e: rec["error"]=str(e)[:1500]
    finally: shutil.rmtree(work,ignore_errors=True)
    return rec

m.groq=groq_curl
m.trajectory=trajectory
m.main()
