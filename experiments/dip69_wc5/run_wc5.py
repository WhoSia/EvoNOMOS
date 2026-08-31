#!/usr/bin/env python3
import os, json, time, shutil, tempfile, subprocess, urllib.request, urllib.error, re, difflib
from pathlib import Path

REPO="https://github.com/WhoSia/Kodo-web.git"
BASE="bd47de6f07250bb6c5cd9fd3ade99b911eda1596"
MODEL="openai/gpt-oss-20b"
ENDPOINT="https://api.groq.com/openai/v1/chat/completions"
KEY=os.environ["GROQ_API_KEY"]
OUT=Path("wc5_output"); OUT.mkdir(exist_ok=True)
PREFIX_USER=("Neutral warm-history prefix only. The current study outcome is unknown. "
             "No source solution, implementation hint, sibling artifact, result, or current-study outcome is present. "
             "You will later receive an actionable software-maintenance packet. Reply exactly WARM_PREFIX_ACK.")
PREFIX_ASSISTANT="WARM_PREFIX_ACK"

ANCHORS={
"A00":{
 "files":["script.js"], "marker":"headerScrollThresholdProvider",
 "initial":"Change the header scrolled-class threshold from the current scrollY > 42 rule to scrollY > 48, preserving all other behavior.",
 "follow":"Change only that threshold contract to scrollY > 56, preserving all other behavior.",
},
"A10":{
 "files":["script.js","index.html"], "marker":"KODO_THEME_PREFERENCE_STORE",
 "initial":"Migrate persisted theme preference from key kodo-theme-v0112 to kodo-theme-v0113. Read the new key first, fall back to legacy v0112 for existing users, and write only v0113. Startup inline theme resolution and runtime theme persistence must agree.",
 "follow":"Retire the legacy kodo-theme-v0112 fallback. Only kodo-theme-v0113 may determine persisted theme. Preserve all other behavior.",
},
"A01":{
 "files":["script.js"], "marker":"scrollPositionProvider",
 "initial":"Allow header scroll position to be supplied by optional window.KODO_SCROLL_SOURCE.getY(); if unavailable, fall back to window.scrollY. The scrolled-class rule remains y > 42 and all other behavior is preserved.",
 "follow":"Replace the host contract with window.KODO_VIEWPORT_SOURCE.getScrollY() and retire the old KODO_SCROLL_SOURCE hook, preserving fallback to window.scrollY and the y > 42 behavior.",
},
"A11":{
 "files":["script.js"], "marker":"menuStateController",
 "initial":"Allow mobile-menu open state to be optionally owned by window.KODO_MENU_ADAPTER with read() and write(open). When absent, retain DOM-backed behavior. Button toggle and navigation-close behavior must stay synchronized with aria-expanded, mobileNav.hidden, and the visible menu mark.",
 "follow":"Change the adapter contract to getOpen() and setOpen(open), retire read()/write(), and preserve behavior plus the DOM fallback.",
}}

def sh(cmd,cwd=None,check=True):
    p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if check and p.returncode:
        raise RuntimeError(f"CMD_FAIL {cmd}\n{p.stdout}")
    return p

def clone_base(dst):
    sh(["git","clone","--quiet",REPO,str(dst)])
    sh(["git","checkout","--quiet",BASE],cwd=dst)

def extract_packet(root, anchor):
    s=(root/"script.js").read_text()
    if anchor=="A10":
        h=(root/"index.html").read_text()
        m=re.search(r"<script>\s*(\(\(\) => \{.*?\}\)\(\);)\s*</script>",h,re.S)
        inline=m.group(1) if m else ""
        a=s.find("const THEME_KEY")
        b=s.find("const closeMenu")
        return {"index.html#startup":inline,"script.js#theme":s[a:b]}
    if anchor in ("A00","A01"):
        a=s.find("const syncHeader")
        b=s.find("const media =",a)
        return {"script.js#header-scroll":s[a:b]}
    if anchor=="A11":
        a=s.find("const closeMenu")
        b=s.find("const syncHeader")
        return {"script.js#menu":s[a:b]}
    raise KeyError(anchor)

def build_prompt(anchor,policy,phase,packet):
    cfg=ANCHORS[anchor]
    demand=cfg["initial"] if phase==0 else cfg["follow"]
    if policy=="D":
        policy_text=("DIRECT policy: implement the demanded change at the existing consumers/owners directly. "
                     "Do NOT introduce a new provider/adapter/config boundary solely to mediate this demand.")
    else:
        policy_text=(f"INVERT policy: introduce exactly one stable provider/resolver/controller boundary for the changing detail, "
                     f"named `{cfg['marker']}`, and make the pre-existing consumers depend on that boundary. No unrelated refactor.")
    return f'''You are one arm of a preregistered software-maintenance experiment.
Return ONLY one JSON object with shape:
{{"replacements":[{{"file":"path","old":"exact current substring","new":"replacement substring"}}]}}
No markdown, commentary, patches, line numbers, or extra keys.

ANCHOR={anchor}
PHASE={'INITIAL' if phase==0 else 'FROZEN_FOLLOWUP'}
POLICY={policy}
DEMAND: {demand}
{policy_text}

Constraints:
- Preserve unrelated behavior and formatting.
- You may edit only: {', '.join(cfg['files'])}.
- Every `old` must be copied exactly from the CURRENT SOURCE PACKET and occur exactly once in its file.
- Use as few replacements as needed.
- Do not inspect any repository or use tools; the packet below is complete for this task.
- The other policy arm, other executor regime, and all outcomes are hidden.

CURRENT SOURCE PACKET:
{json.dumps(packet,ensure_ascii=False)}
'''

def groq(messages):
    payload={
      "model":MODEL,"messages":messages,"reasoning_effort":"medium","reasoning_format":"hidden",
      "temperature":0.6,"top_p":0.95,"max_completion_tokens":2048,"stream":False,
      "response_format":{"type":"json_object"}
    }
    data=json.dumps(payload).encode()
    while True:
        req=urllib.request.Request(ENDPOINT,data=data,headers={
            "Authorization":"Bearer "+KEY,"Content-Type":"application/json"
        },method="POST")
        try:
            with urllib.request.urlopen(req,timeout=180) as r:
                raw=r.read().decode()
                headers=dict(r.headers)
            obj=json.loads(raw)
            if obj.get("model") != MODEL:
                raise RuntimeError("MODEL_MISMATCH:"+str(obj.get("model")))
            text=obj["choices"][0]["message"].get("content") or ""
            if not text.strip():
                raise RuntimeError("EMPTY_MODEL_CONTENT")
            usage=obj.get("usage",{})
            return text,usage,headers
        except urllib.error.HTTPError as e:
            body=e.read().decode("utf-8","replace")
            if e.code==429:
                reset=e.headers.get("retry-after")
                wait=float(reset) if reset and reset.replace(".","",1).isdigit() else 8.0
                time.sleep(min(max(wait,1),60))
                continue
            raise RuntimeError(f"GROQ_HTTP_{e.code}:{body[:500]}")

def parse_and_apply(root,text,anchor,policy):
    try: obj=json.loads(text)
    except Exception as e: raise RuntimeError("JSON_PARSE_FAIL:"+str(e))
    reps=obj.get("replacements")
    if not isinstance(reps,list) or not reps: raise RuntimeError("BAD_REPLACEMENTS")
    allowed=set(ANCHORS[anchor]["files"])
    before={f:(root/f).read_text() for f in allowed}
    for x in reps:
        if set(x.keys()) != {"file","old","new"}: raise RuntimeError("BAD_REPLACEMENT_KEYS")
        f=x["file"]; old=x["old"]; new=x["new"]
        if f not in allowed: raise RuntimeError("FILE_SCOPE_FAIL:"+f)
        path=root/f; cur=path.read_text()
        if not isinstance(old,str) or not old or not isinstance(new,str): raise RuntimeError("BAD_REPLACEMENT_VALUE")
        if cur.count(old)!=1: raise RuntimeError(f"OLD_OCCURRENCE_FAIL:{f}:{cur.count(old)}")
        path.write_text(cur.replace(old,new,1))
    after={f:(root/f).read_text() for f in allowed}
    marker=ANCHORS[anchor]["marker"]
    joined="\n".join(after.values())
    if policy=="I":
        if marker not in joined: raise RuntimeError("INVERT_BOUNDARY_MARKER_MISSING")
        if anchor=="A10" and not (marker in after["script.js"] and marker in after["index.html"]):
            raise RuntimeError("INVERT_SHARED_BOUNDARY_NOT_USED_BOTH_FILES")
    else:
        if marker in joined: raise RuntimeError("DIRECT_INTRODUCED_FORBIDDEN_BOUNDARY")
    changed=[f for f in allowed if before[f]!=after[f]]
    if not changed: raise RuntimeError("NO_SOURCE_CHANGE")
    return before,after,changed

def churn(a,b):
    sm=difflib.SequenceMatcher(a=a.splitlines(),b=b.splitlines())
    c=0
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=="replace": c+=(i2-i1)+(j2-j1)
        elif tag=="delete": c+=(i2-i1)
        elif tag=="insert": c+=(j2-j1)
    return c

def locate_block(text,start_token,end_token=None):
    a=text.find(start_token)
    if a<0:return ""
    if end_token:
        b=text.find(end_token,a+len(start_token))
        if b<0:b=len(text)
    else:b=len(text)
    return text[a:b]

def norm(x):
    return re.sub(r"\s+"," ",x).strip()

def consumer_blocks(root,anchor):
    s=(root/"script.js").read_text()
    if anchor in ("A00","A01"):
        return [locate_block(s,"const syncHeader","const media =")]
    if anchor=="A10":
        return [
          locate_block(s,"const applyTheme","let initialTheme"),
          locate_block(s,"let initialTheme","const closeMenu")
        ]
    if anchor=="A11":
        return [
          locate_block(s,"const closeMenu","button?.addEventListener"),
          locate_block(s,"button?.addEventListener","mobileNav?.querySelectorAll")
        ]
    return []

def run_dynamic_oracle(root,anchor,phase):
    s=(root/"script.js").read_text()
    h=(root/"index.html").read_text()
    if anchor=="A00":
        threshold=48 if phase==0 else 56
        if f"> {threshold}" not in s and f">{threshold}" not in s: raise RuntimeError("ORACLE_A00_THRESHOLD")
        if phase==0 and re.search(r"scrollY\s*>\s*42",s): raise RuntimeError("ORACLE_A00_OLD")
        if phase==1 and re.search(r"scrollY\s*>\s*48",s): raise RuntimeError("ORACLE_A00_RETIRED")
        return
    if anchor=="A10":
        if "kodo-theme-v0113" not in s or "kodo-theme-v0113" not in h: raise RuntimeError("ORACLE_A10_NEW_KEY")
        if phase==0:
            if "kodo-theme-v0112" not in s or "kodo-theme-v0112" not in h: raise RuntimeError("ORACLE_A10_FALLBACK")
        else:
            if "kodo-theme-v0112" in s or "kodo-theme-v0112" in h: raise RuntimeError("ORACLE_A10_LEGACY_RETIRED")
        return
    if anchor=="A01":
        if phase==0:
            if "KODO_SCROLL_SOURCE" not in s or "getY" not in s: raise RuntimeError("ORACLE_A01_HOOK")
        else:
            if "KODO_VIEWPORT_SOURCE" not in s or "getScrollY" not in s: raise RuntimeError("ORACLE_A01_NEW_HOOK")
            if "KODO_SCROLL_SOURCE" in s: raise RuntimeError("ORACLE_A01_OLD_HOOK")
        if "window.scrollY" not in s: raise RuntimeError("ORACLE_A01_FALLBACK")
        return
    if anchor=="A11":
        if "KODO_MENU_ADAPTER" not in s: raise RuntimeError("ORACLE_A11_ADAPTER")
        if phase==0:
            if ".read" not in s or ".write" not in s: raise RuntimeError("ORACLE_A11_METHODS")
        else:
            if "getOpen" not in s or "setOpen" not in s: raise RuntimeError("ORACLE_A11_NEW_METHODS")
            if re.search(r"\.read\s*\(",s) or re.search(r"\.write\s*\(",s): raise RuntimeError("ORACLE_A11_OLD_METHODS")
        if "aria-expanded" not in s or "mobileNav.hidden" not in s: raise RuntimeError("ORACLE_A11_DOM_SYNC")
        return

def validate(root,anchor,phase):
    sh(["node","--check","script.js"],cwd=root)
    sh(["python3","tools/check_site.py"],cwd=root)
    run_dynamic_oracle(root,anchor,phase)

def messages_for(regime,prompt,prior=None):
    base=[]
    if regime=="warm":
        base=[{"role":"user","content":PREFIX_USER},{"role":"assistant","content":PREFIX_ASSISTANT}]
    if prior:
        base += prior
    base.append({"role":"user","content":prompt})
    return base

def trajectory(base_dir,anchor,rep,policy,regime):
    tid=f"{anchor}-r{rep}-{policy}-{regime}"
    work=Path(tempfile.mkdtemp(prefix="wc5_"))
    shutil.copytree(base_dir,work/"repo",dirs_exist_ok=True)
    root=work/"repo"
    rec={"id":tid,"anchor":anchor,"replicate":rep,"policy":policy,"regime":regime,"status":"HOLD"}
    try:
        base_cons=[norm(x) for x in consumer_blocks(root,anchor)]
        p0=build_prompt(anchor,policy,0,extract_packet(root,anchor))
        m0=messages_for(regime,p0)
        t0,u0,_=groq(m0)
        b0,a0,chg0=parse_and_apply(root,t0,anchor,policy)
        validate(root,anchor,0)
        p1=build_prompt(anchor,policy,1,extract_packet(root,anchor))
        prior=[{"role":"user","content":p0},{"role":"assistant","content":t0}]
        m1=messages_for(regime,p1,prior=prior)
        t1,u1,_=groq(m1)
        b1,a1,chg1=parse_and_apply(root,t1,anchor,policy)
        validate(root,anchor,1)
        final_cons=[norm(x) for x in consumer_blocks(root,anchor)]
        P1=sum(1 for x,y in zip(base_cons,final_cons) if x!=y)
        if policy=="I": P1=max(0,P1-1)
        F0=len(chg0); C0=sum(churn(b0[f],a0[f]) for f in chg0)
        F1=len(chg1); C1=sum(churn(b1[f],a1[f]) for f in chg1)
        rec.update(status="PASS",V=[F0,C0,F1,C1,P1],phase0_files=chg0,phase1_files=chg1,
                   usage0=u0,usage1=u1,output0=t0,output1=t1)
    except Exception as e:
        rec["error"]=str(e)[:1500]
    finally:
        shutil.rmtree(work,ignore_errors=True)
    return rec

def pareto(vI,vD):
    d=[a-b for a,b in zip(vI,vD)]
    if all(x==0 for x in d):return "TRADEOFF_TIE",d
    if all(x<=0 for x in d) and any(x<0 for x in d):return "PARETO_I",d
    if all(x>=0 for x in d) and any(x>0 for x in d):return "PARETO_D",d
    return "TRADEOFF_TIE",d

def main():
    base=Path(tempfile.mkdtemp(prefix="wc5_base_"))/"kodo"
    clone_base(base)
    trajectories=[]
    for anchor in ["A00","A10","A01","A11"]:
      for rep in range(1,7):
        for regime in ["reset","warm"]:
          for policy in ["I","D"]:
            r=trajectory(base,anchor,rep,policy,regime)
            trajectories.append(r)
            print("TRAJECTORY",r["id"],r["status"],r.get("V"),r.get("error",""),flush=True)
    blocks=[]
    for anchor in ["A00","A10","A01","A11"]:
      for rep in range(1,7):
        for regime in ["reset","warm"]:
          xs={x["policy"]:x for x in trajectories if x["anchor"]==anchor and x["replicate"]==rep and x["regime"]==regime}
          b={"anchor":anchor,"replicate":rep,"regime":regime}
          if len(xs)!=2 or xs["I"]["status"]!="PASS" or xs["D"]["status"]!="PASS": b["signature"]="HOLD"
          else:
            sig,d=pareto(xs["I"]["V"],xs["D"]["V"]); b.update(signature=sig,d=d,V_I=xs["I"]["V"],V_D=xs["D"]["V"])
          blocks.append(b)
    cells={}; moderation={}
    for anchor in ["A00","A10","A01","A11"]:
      cells[anchor]={}
      for regime in ["reset","warm"]:
        ss=[b["signature"] for b in blocks if b["anchor"]==anchor and b["regime"]==regime]
        if any(s=="HOLD" for s in ss): code="HOLD"
        elif len(set(ss))==1: code="STABLE("+ss[0]+")"
        else: code="UNRESOLVED_STOCHASTIC"
        cells[anchor][regime]={"code":code,"signatures":ss}
      r=cells[anchor]["reset"]["code"]; w=cells[anchor]["warm"]["code"]
      if r.startswith("STABLE") and w.startswith("STABLE"): moderation[anchor]="DIFF" if r!=w else "SAME"
      else: moderation[anchor]="UNRESOLVED"
    bits=[]
    for a in ["A10","A01","A11"]: bits.append("1" if moderation[a]=="DIFF" else "0" if moderation[a]=="SAME" else "?")
    code="".join(bits)
    families={"000":"H_N_NUISANCE","101":"H_I_IMPL","011":"H_S_SEM","001":"H_X_INTERACTION","111":"H_OR_EITHER_PRESSURE"}
    footprint=families.get(code,("UNRESOLVED_FOOTPRINT" if "?" in code else "MODEL_ESCAPE_PATTERN_"+code))
    if moderation["A00"]=="DIFF": footprint="MODEL_ESCAPE_LOW_LOW"
    summary={"model":MODEL,"base":BASE,"trajectories":len(trajectories),
             "pass_trajectories":sum(x["status"]=="PASS" for x in trajectories),
             "hold_trajectories":sum(x["status"]!="PASS" for x in trajectories),
             "cells":cells,"moderation":moderation,"basis_bits":code,"footprint":footprint}
    (OUT/"trajectories.json").write_text(json.dumps(trajectories,indent=2))
    (OUT/"blocks.json").write_text(json.dumps(blocks,indent=2))
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2))
    print("EVONOMOS_WC5_SUMMARY",json.dumps(summary,separators=(",",":")),flush=True)
    shutil.rmtree(base.parent,ignore_errors=True)

if __name__=="__main__": main()
