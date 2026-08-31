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
"A00":{"files":["script.js"],"marker":"headerScrollThresholdProvider","initial":"Change the header scrolled-class threshold from the current scrollY > 42 rule to scrollY > 48, preserving all other behavior.","follow":"Change only that threshold contract to scrollY > 56, preserving all other behavior."},
"A10":{"files":["script.js","index.html"],"marker":"KODO_THEME_PREFERENCE_STORE","initial":"Migrate persisted theme preference from key kodo-theme-v0112 to kodo-theme-v0113. Read the new key first, fall back to legacy v0112 for existing users, and write only v0113. Startup inline theme resolution and runtime theme persistence must agree.","follow":"Retire the legacy kodo-theme-v0112 fallback. Only kodo-theme-v0113 may determine persisted theme. Preserve all other behavior."},
"A01":{"files":["script.js"],"marker":"scrollPositionProvider","initial":"Allow header scroll position to be supplied by optional window.KODO_SCROLL_SOURCE.getY(); if unavailable, fall back to window.scrollY. The scrolled-class rule remains y > 42 and all other behavior is preserved.","follow":"Replace the host contract with window.KODO_VIEWPORT_SOURCE.getScrollY() and retire the old KODO_SCROLL_SOURCE hook, preserving fallback to window.scrollY and the y > 42 behavior."},
"A11":{"files":["script.js"],"marker":"menuStateController","initial":"Allow mobile-menu open state to be optionally owned by window.KODO_MENU_ADAPTER with read() and write(open). When absent, retain DOM-backed behavior. Button toggle and navigation-close behavior must stay synchronized with aria-expanded, mobileNav.hidden, and the visible menu mark.","follow":"Change the adapter contract to getOpen() and setOpen(open), retire read()/write(), and preserve behavior plus the DOM fallback."}}

def sh(cmd,cwd=None,check=True):
    p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if check and p.returncode: raise RuntimeError(f"CMD_FAIL {cmd}\n{p.stdout}")
    return p

def clone_base(dst):
    sh(["git","clone","--quiet",REPO,str(dst)]); sh(["git","checkout","--quiet",BASE],cwd=dst)

def extract_packet(root,anchor):
    s=(root/"script.js").read_text()
    if anchor=="A10":
        h=(root/"index.html").read_text(); m=re.search(r"<script>\s*(\(\(\) => \{.*?\}\)\(\);)\s*</script>",h,re.S)
        a=s.find("const THEME_KEY"); b=s.find("const closeMenu")
        return {"index.html#startup":m.group(1) if m else "","script.js#theme":s[a:b]}
    if anchor in ("A00","A01"):
        a=s.find("const syncHeader"); b=s.find("const media =",a); return {"script.js#header-scroll":s[a:b]}
    a=s.find("const closeMenu"); b=s.find("const syncHeader"); return {"script.js#menu":s[a:b]}

def build_prompt(anchor,policy,phase,packet):
    c=ANCHORS[anchor]; demand=c["initial"] if phase==0 else c["follow"]
    pol=("DIRECT policy: implement the demanded change at the existing consumers/owners directly. Do NOT introduce a new provider/adapter/config boundary solely to mediate this demand." if policy=="D" else f"INVERT policy: introduce exactly one stable provider/resolver/controller boundary for the changing detail, named `{c['marker']}`, and make the pre-existing consumers depend on that boundary. No unrelated refactor.")
    return f'''You are one arm of a preregistered software-maintenance experiment.
Return ONLY one JSON object with shape:
{{"replacements":[{{"file":"path","old":"exact current substring","new":"replacement substring"}}]}}
No markdown, commentary, patches, line numbers, or extra keys.
ANCHOR={anchor}
PHASE={'INITIAL' if phase==0 else 'FROZEN_FOLLOWUP'}
POLICY={policy}
DEMAND: {demand}
{pol}
Constraints:
- Preserve unrelated behavior and formatting.
- You may edit only: {', '.join(c['files'])}.
- Every `old` must be copied exactly from the CURRENT SOURCE PACKET and occur exactly once in its file.
- Use as few replacements as needed.
- Do not inspect any repository or use tools; the packet below is complete for this task.
- The other policy arm, other executor regime, and all outcomes are hidden.
CURRENT SOURCE PACKET:
{json.dumps(packet,ensure_ascii=False)}
'''

def groq(messages):
    payload={"model":MODEL,"messages":messages,"reasoning_effort":"medium","reasoning_format":"hidden","temperature":0.6,"top_p":0.95,"max_completion_tokens":2048,"stream":False,"response_format":{"type":"json_object"}}
    data=json.dumps(payload).encode()
    while True:
        req=urllib.request.Request(ENDPOINT,data=data,headers={"Authorization":"Bearer "+KEY,"Content-Type":"application/json"},method="POST")
        try:
            with urllib.request.urlopen(req,timeout=180) as r: raw=r.read().decode(); headers=dict(r.headers)
            obj=json.loads(raw)
            if obj.get("model")!=MODEL: raise RuntimeError("MODEL_MISMATCH:"+str(obj.get("model")))
            text=obj["choices"][0]["message"].get("content") or ""
            if not text.strip(): raise RuntimeError("EMPTY_MODEL_CONTENT")
            return text,obj.get("usage",{}),headers
        except urllib.error.HTTPError as e:
            body=e.read().decode("utf-8","replace")
            if e.code==429:
                reset=e.headers.get("retry-after"); wait=float(reset) if reset and reset.replace(".","",1).isdigit() else 8.0
                time.sleep(min(max(wait,1),60)); continue
            raise RuntimeError(f"GROQ_HTTP_{e.code}:{body[:500]}")

def parse_and_apply(root,text,anchor,policy):
    try: obj=json.loads(text)
    except Exception as e: raise RuntimeError("JSON_PARSE_FAIL:"+str(e))
    reps=obj.get("replacements")
    if not isinstance(reps,list) or not reps: raise RuntimeError("BAD_REPLACEMENTS")
    allowed=set(ANCHORS[anchor]["files"]); before={f:(root/f).read_text() for f in allowed}
    for x in reps:
        if set(x.keys())!={"file","old","new"}: raise RuntimeError("BAD_REPLACEMENT_KEYS")
        f=x["file"]; old=x["old"]; new=x["new"]
        if f not in allowed: raise RuntimeError("FILE_SCOPE_FAIL:"+f)
        cur=(root/f).read_text()
        if not isinstance(old,str) or not old or not isinstance(new,str): raise RuntimeError("BAD_REPLACEMENT_VALUE")
        if cur.count(old)!=1: raise RuntimeError(f"OLD_OCCURRENCE_FAIL:{f}:{cur.count(old)}")
        (root/f).write_text(cur.replace(old,new,1))
    after={f:(root/f).read_text() for f in allowed}; marker=ANCHORS[anchor]["marker"]; joined="\n".join(after.values())
    if policy=="I":
        if marker not in joined: raise RuntimeError("INVERT_BOUNDARY_MARKER_MISSING")
        if anchor=="A10" and not(marker in after["script.js"] and marker in after["index.html"]): raise RuntimeError("INVERT_SHARED_BOUNDARY_NOT_USED_BOTH_FILES")
    elif marker in joined: raise RuntimeError("DIRECT_INTRODUCED_FORBIDDEN_BOUNDARY")
    changed=[f for f in allowed if before[f]!=after[f]]
    if not changed: raise RuntimeError("NO_SOURCE_CHANGE")
    return before,after,changed

def churn(a,b):
    c=0
    for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(a=a.splitlines(),b=b.splitlines()).get_opcodes():
        if tag=="replace": c+=(i2-i1)+(j2-j1)
        elif tag=="delete": c+=i2-i1
        elif tag=="insert": c+=j2-j1
    return c

def locate_block(text,start,end):
    a=text.find(start)
    if a<0:return ""
    b=text.find(end,a+len(start)); return text[a:(b if b>=0 else len(text))]

def norm(x): return re.sub(r"\s+"," ",x).strip()

def consumer_blocks(root,anchor):
    s=(root/"script.js").read_text()
    if anchor in ("A00","A01"): return [locate_block(s,"const syncHeader","const media =")]
    if anchor=="A10": return [locate_block(s,"const applyTheme","let initialTheme"),locate_block(s,"let initialTheme","const closeMenu")]
    return [locate_block(s,"const closeMenu","button?.addEventListener"),locate_block(s,"button?.addEventListener","mobileNav?.querySelectorAll")]

def run_dynamic_oracle(root,anchor,phase):
    js=r'''
const fs=require('fs'),vm=require('vm'); const anchor=process.argv[1],phase=Number(process.argv[2]);
const script=fs.readFileSync('script.js','utf8'),html=fs.readFileSync('index.html','utf8');
function store(seed={}){const m=new Map(Object.entries(seed));return{getItem:k=>m.has(k)?m.get(k):null,setItem:(k,v)=>m.set(k,String(v)),dump:()=>Object.fromEntries(m)}}
function boot(o={}){const root={dataset:{},classList:{state:new Set(),toggle(k,v){v?this.state.add(k):this.state.delete(k)},replace(){}}};const mark={textContent:'+'};const bh={},lh={};const button={attrs:{'aria-expanded':'false'},setAttribute(k,v){this.attrs[k]=String(v)},getAttribute(k){return this.attrs[k]??null},addEventListener(k,f){bh[k]=f},querySelector(sel){return(sel==='.menu-mark'||sel.includes('aria-hidden'))?mark:null}};const link={addEventListener(k,f){lh[k]=f}},mobileNav={hidden:true,querySelectorAll(){return[link]}},header={classList:{scrolled:false,toggle(k,v){if(k==='is-scrolled')this.scrolled=!!v}}},th={};const themeButton={setAttribute(){},addEventListener(k,f){th[k]=f}},themeLabel={textContent:''},themeColor={setAttribute(){}};const document={documentElement:root,querySelector(sel){if(sel==='[data-menu-button]')return button;if(sel==='[data-mobile-nav]')return mobileNav;if(sel==='[data-header]')return header;if(sel==='[data-theme-toggle]')return themeButton;if(sel==='[data-theme-label]')return themeLabel;if(sel==='[data-theme-color]')return themeColor;return null},querySelectorAll(){return[]}};const sh={},localStorage=store(o.storage||{}),window={scrollY:o.scrollY||0};if(o.scrollSource)window.KODO_SCROLL_SOURCE=o.scrollSource;if(o.viewportSource)window.KODO_VIEWPORT_SOURCE=o.viewportSource;if(o.menuAdapter)window.KODO_MENU_ADAPTER=o.menuAdapter;window.window=window;window.document=document;window.localStorage=localStorage;const ctx={window,document,localStorage,matchMedia:()=>({matches:true}),addEventListener:(k,f)=>sh[k]=f,Image:class{},console};vm.createContext(ctx);vm.runInContext(script,ctx,{filename:'script.js'});return{root,button,mobileNav,header,mark,bh,lh,th,sh,localStorage,window}}
function A(x,m){if(!x)throw new Error(m)}
if(anchor==='A00'){const t=phase===0?48:56;let b=boot({scrollY:t});A(!b.header.classList.scrolled,'eq');b=boot({scrollY:t+1});A(b.header.classList.scrolled,'plus')}
if(anchor==='A01'){if(phase===0){let b=boot({scrollY:0,scrollSource:{getY:()=>100}});A(b.header.classList.scrolled,'old source');b=boot({scrollY:100});A(b.header.classList.scrolled,'fallback')}else{let b=boot({scrollY:0,scrollSource:{getY:()=>100},viewportSource:{getScrollY:()=>0}});A(!b.header.classList.scrolled,'retire old');b=boot({scrollY:0,viewportSource:{getScrollY:()=>100}});A(b.header.classList.scrolled,'new source');b=boot({scrollY:100});A(b.header.classList.scrolled,'fallback')}}
if(anchor==='A10'){const inline=(html.match(/<script>\s*(\(\(\) => \{[\s\S]*?\}\)\(\);)\s*<\/script>/)||[])[1];A(inline,'inline');function bi(x){const r={dataset:{},classList:{replace(){}}},ls=store(x),c={document:{documentElement:r},localStorage:ls};vm.createContext(c);vm.runInContext(inline,c);return{r,ls}}if(phase===0){let x=bi({'kodo-theme-v0113':'light','kodo-theme-v0112':'dark'});A(x.r.dataset.theme==='light','new wins');x=bi({'kodo-theme-v0112':'light'});A(x.r.dataset.theme==='light','legacy startup');let b=boot({storage:{'kodo-theme-v0112':'light'}});A(b.root.dataset.theme==='light','legacy runtime');if(b.th.click){b.th.click();A('kodo-theme-v0113'in b.localStorage.dump(),'write new')}}else{let x=bi({'kodo-theme-v0113':'light','kodo-theme-v0112':'dark'});A(x.r.dataset.theme==='light','new');x=bi({'kodo-theme-v0112':'light'});A(x.r.dataset.theme==='dark','ignore legacy startup');let b=boot({storage:{'kodo-theme-v0112':'light'}});A(b.root.dataset.theme==='dark','ignore legacy runtime')}}
if(anchor==='A11'){let state=false,ad=phase===0?{read:()=>state,write:v=>state=!!v}:{getOpen:()=>state,setOpen:v=>state=!!v};let b=boot({menuAdapter:ad});A(typeof b.bh.click==='function','button');b.bh.click();A(state===true&&b.button.attrs['aria-expanded']==='true'&&!b.mobileNav.hidden,'open sync');A(typeof b.lh.click==='function','link');b.lh.click();A(state===false&&b.button.attrs['aria-expanded']==='false'&&b.mobileNav.hidden,'close sync');b=boot({});b.bh.click();A(b.button.attrs['aria-expanded']==='true'&&!b.mobileNav.hidden,'fallback open');b.lh.click();A(b.button.attrs['aria-expanded']==='false'&&b.mobileNav.hidden,'fallback close')}
console.log('DYNAMIC_ORACLE_PASS');
'''
    p=subprocess.run(["node","-e",js,anchor,str(phase)],cwd=root,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if p.returncode: raise RuntimeError("DYNAMIC_ORACLE_FAIL:"+p.stdout[-1200:])
    if "DYNAMIC_ORACLE_PASS" not in p.stdout: raise RuntimeError("DYNAMIC_ORACLE_NO_PASS")

def validate(root,anchor,phase):
    sh(["node","--check","script.js"],cwd=root); sh(["python3","tools/check_site.py"],cwd=root); run_dynamic_oracle(root,anchor,phase)

def messages_for(regime,prompt,prior=None):
    base=[]
    if regime=="warm": base=[{"role":"user","content":PREFIX_USER},{"role":"assistant","content":PREFIX_ASSISTANT}]
    if prior: base+=prior
    base.append({"role":"user","content":prompt}); return base

def trajectory(base_dir,anchor,rep,policy,regime):
    tid=f"{anchor}-r{rep}-{policy}-{regime}"; work=Path(tempfile.mkdtemp(prefix="wc5_")); shutil.copytree(base_dir,work/"repo",dirs_exist_ok=True); root=work/"repo"
    rec={"id":tid,"anchor":anchor,"replicate":rep,"policy":policy,"regime":regime,"status":"HOLD"}
    try:
        base_cons=[norm(x) for x in consumer_blocks(root,anchor)]; p0=build_prompt(anchor,policy,0,extract_packet(root,anchor)); m0=messages_for(regime,p0); t0,u0,_=groq(m0); b0,a0,c0=parse_and_apply(root,t0,anchor,policy); validate(root,anchor,0)
        p1=build_prompt(anchor,policy,1,extract_packet(root,anchor)); prior=[{"role":"user","content":p0},{"role":"assistant","content":t0}]; m1=messages_for(regime,p1,prior); t1,u1,_=groq(m1); b1,a1,c1=parse_and_apply(root,t1,anchor,policy); validate(root,anchor,1)
        final_cons=[norm(x) for x in consumer_blocks(root,anchor)]; P1=sum(1 for x,y in zip(base_cons,final_cons) if x!=y); P1=max(0,P1-1) if policy=="I" else P1
        V=[len(c0),sum(churn(b0[f],a0[f]) for f in c0),len(c1),sum(churn(b1[f],a1[f]) for f in c1),P1]
        rec.update(status="PASS",V=V,phase0_files=c0,phase1_files=c1,usage0=u0,usage1=u1,output0=t0,output1=t1)
    except Exception as e: rec["error"]=str(e)[:1500]
    finally: shutil.rmtree(work,ignore_errors=True)
    return rec

def pareto(i,d):
    x=[a-b for a,b in zip(i,d)]
    if all(v==0 for v in x):return"TRADEOFF_TIE",x
    if all(v<=0 for v in x) and any(v<0 for v in x):return"PARETO_I",x
    if all(v>=0 for v in x) and any(v>0 for v in x):return"PARETO_D",x
    return"TRADEOFF_TIE",x

def main():
    base=Path(tempfile.mkdtemp(prefix="wc5_base_"))/"kodo"; clone_base(base); tr=[]
    for a in ["A00","A10","A01","A11"]:
      for r in range(1,7):
       for e in ["reset","warm"]:
        for p in ["I","D"]:
         z=trajectory(base,a,r,p,e);tr.append(z);print("TRAJECTORY",z["id"],z["status"],z.get("V"),z.get("error",""),flush=True)
    blocks=[]
    for a in ["A00","A10","A01","A11"]:
     for r in range(1,7):
      for e in ["reset","warm"]:
       xs={z["policy"]:z for z in tr if z["anchor"]==a and z["replicate"]==r and z["regime"]==e};b={"anchor":a,"replicate":r,"regime":e}
       if len(xs)!=2 or xs["I"]["status"]!="PASS" or xs["D"]["status"]!="PASS":b["signature"]="HOLD"
       else:sig,d=pareto(xs["I"]["V"],xs["D"]["V"]);b.update(signature=sig,d=d,V_I=xs["I"]["V"],V_D=xs["D"]["V"])
       blocks.append(b)
    cells={};mod={}
    for a in ["A00","A10","A01","A11"]:
     cells[a]={}
     for e in ["reset","warm"]:
      ss=[b["signature"] for b in blocks if b["anchor"]==a and b["regime"]==e];code="HOLD" if any(s=="HOLD" for s in ss) else "STABLE("+ss[0]+")" if len(set(ss))==1 else "UNRESOLVED_STOCHASTIC";cells[a][e]={"code":code,"signatures":ss}
     x,y=cells[a]["reset"]["code"],cells[a]["warm"]["code"];mod[a]="DIFF" if x.startswith("STABLE") and y.startswith("STABLE") and x!=y else "SAME" if x.startswith("STABLE") and x==y else "UNRESOLVED"
    bits="".join("1" if mod[a]=="DIFF" else "0" if mod[a]=="SAME" else "?" for a in ["A10","A01","A11"]);fam={"000":"H_N_NUISANCE","101":"H_I_IMPL","011":"H_S_SEM","001":"H_X_INTERACTION","111":"H_OR_EITHER_PRESSURE"};foot=fam.get(bits,"UNRESOLVED_FOOTPRINT" if "?" in bits else "MODEL_ESCAPE_PATTERN_"+bits);foot="MODEL_ESCAPE_LOW_LOW" if mod["A00"]=="DIFF" else foot
    summary={"model":MODEL,"base":BASE,"trajectories":len(tr),"pass_trajectories":sum(z["status"]=="PASS" for z in tr),"hold_trajectories":sum(z["status"]!="PASS" for z in tr),"cells":cells,"moderation":mod,"basis_bits":bits,"footprint":foot}
    (OUT/"trajectories.json").write_text(json.dumps(tr,indent=2));(OUT/"blocks.json").write_text(json.dumps(blocks,indent=2));(OUT/"summary.json").write_text(json.dumps(summary,indent=2));print("EVONOMOS_WC5_SUMMARY",json.dumps(summary,separators=(",",":")),flush=True);shutil.rmtree(base.parent,ignore_errors=True)
if __name__=="__main__":main()
