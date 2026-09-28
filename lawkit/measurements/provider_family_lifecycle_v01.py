#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
from typing import Any
ARMS=("WIDE_BOUNDARY_REUSE","CAPABILITY_SEGREGATED")
def git(repo:Path,args:list[str],check:bool=True):
    return subprocess.run(["git","-C",str(repo),*args],check=check,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
def changed(repo:Path,old:str,new:str,path:str)->bool:
    r=git(repo,["diff","--quiet",old,new,"--",path],False)
    if r.returncode not in (0,1): raise RuntimeError(r.stderr)
    return r.returncode==1
def eligible(path:str)->bool:
    if not path.startswith("packages/") or path.startswith("packages/trueforge-sdk/"): return False
    parts=path.split("/")
    if "test" in parts or "tests" in parts: return False
    if path.startswith("packages/trueforge/catalog/") and path.endswith((".yaml",".yml")): return True
    return "/src/" in path and path.endswith((".ts",".tsx"))
def churn(repo:Path,old:str,new:str):
    r=git(repo,["diff","--numstat",old,new]); total=0; rows=[]
    for line in r.stdout.splitlines():
        if not line.strip(): continue
        a,d,p=line.split("\t",2)
        if not eligible(p): continue
        if a=="-" or d=="-": raise RuntimeError("binary eligible path "+p)
        ai,di=int(a),int(d); total+=ai+di
        rows.append({"path":p,"additions":ai,"deletions":di})
    return total,rows
def cval(probe:dict[str,Any],phase:str)->int:
    p=probe[phase]; tools=p.get("tools",[]); f=p.get("fetch"); vis="web_fetch" in tools
    if f=="PASS" and vis: return 1
    if f=="HIDDEN" and not vis: return 0
    raise RuntimeError(f"invalid exposure {phase}: {f} {tools}")
def phase(repo,old,new,idx,q,probe,c):
    ss=[s["id"] for s in c["authority_sites"] if changed(repo,old,new,s["path"])]
    lv,lr=churn(repo,old,new)
    aa=[s["id"] for s in c["A"]["fixed_sites"] if changed(repo,old,new,s["path"])]
    dp=c["A"]["dynamic_provider_transport_auth"][f"phase{idx}"]
    if changed(repo,old,new,dp): aa.append("provider_transport_auth")
    return {"S":len(ss),"L":lv,"C":cval(probe,f"phase{idx}"),"A":len(aa),"Q":int(q),"S_sites":ss,"A_sites":aa,"L_rows":lr}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--constitution",required=True,type=Path); ap.add_argument("--input",required=True,type=Path); ap.add_argument("--out",required=True,type=Path)
    a=ap.parse_args(); c=json.loads(a.constitution.read_text()); i=json.loads(a.input.read_text()); base=i["base"]; outarms={}
    for arm in ARMS:
        x=i["arms"][arm]; repo=Path(x["repo"])
        if git(repo,["rev-parse","HEAD"]).stdout.strip()!=x["child_head"]: raise RuntimeError(arm+" child mismatch")
        p0=phase(repo,base,x["parent_head"],0,x["q0"],json.loads(Path(x["phase0_probe"]).read_text()),c)
        p1=phase(repo,x["parent_head"],x["child_head"],1,x["q1"],json.loads(Path(x["phase1_probe"]).read_text()),c)
        outarms[arm]={"phase0":p0,"phase1":p1,"vector":{"phase0":[p0[k] for k in ("S","L","C","A","Q")],"phase1":[p1[k] for k in ("S","L","C","A","Q")]}}
    out={"protocol":c["protocol"],"stage":c["stage"],"base":base,"arms":outarms,"scalarization":False,"winner":None}
    a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("SIMULTANEOUS_VECTOR_REVEAL=PASS")
    print(json.dumps({arm:outarms[arm]["vector"] for arm in ARMS},sort_keys=True))
if __name__=="__main__": main()
