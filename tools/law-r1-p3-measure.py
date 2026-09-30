#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, subprocess
from pathlib import Path

ARMS={
  "DISPERSED_MEMBERSHIP_EXTENSION":"dispersed",
  "DUAL_RUNTIME_MEMBERSHIP_REGISTRY":"dual"
}
PHASE_PROVIDERS={
  "phase0":["IssueTracker"],
  "phase1":["NetGSM","Mutlucell","Verimor","IletiMerkezi"]
}

def text(path:Path)->str:
    return path.read_text(encoding="utf-8") if path.exists() else ""

def eligible(rel:str)->bool:
    if rel=="server/notification.js": return True
    if rel.startswith("server/notification-providers/") and rel.endswith(".js"): return True
    if rel=="src/components/NotificationDialog.vue": return True
    if rel.startswith("src/components/notifications/") and rel.endswith((".js",".vue")): return True
    return False

def normalize_path(raw:str)->str|None:
    raw=raw.replace("\\","/")
    for marker in ("server/","src/"):
        i=raw.rfind(marker)
        if i>=0:
            return raw[i:]
    return None

def churn(old:Path,new:Path):
    p=subprocess.run(
      ["git","diff","--no-index","--no-renames","--numstat",str(old),str(new)],
      text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE
    )
    if p.returncode not in (0,1): raise RuntimeError(p.stderr)
    total=0; rows=[]
    for line in p.stdout.splitlines():
        if not line.strip(): continue
        parts=line.split("\t",2)
        if len(parts)!=3: continue
        a,d,raw=parts
        rel=normalize_path(raw)
        if rel is None or not eligible(rel): continue
        if a=="-" or d=="-": raise RuntimeError("binary eligible path "+raw)
        ai,di=int(a),int(d)
        total+=ai+di
        rows.append({"path":rel,"additions":ai,"deletions":di})
    rows.sort(key=lambda x:x["path"])
    return total,rows

def new_decl(old:str,new:str,patterns:list[str],providers:list[str])->bool:
    for provider in providers:
        for pattern in patterns:
            before=pattern.format(provider=provider) in old
            after=pattern.format(provider=provider) in new
            if after and not before: return True
    return False

def s_sites(arm:str,old:Path,new:Path,providers:list[str]):
    sites=[]
    if arm=="DISPERSED_MEMBERSHIP_EXTENSION":
        os=text(old/"server/notification.js"); ns=text(new/"server/notification.js")
        oi=text(old/"src/components/notifications/index.js"); ni=text(new/"src/components/notifications/index.js")
        od=text(old/"src/components/NotificationDialog.vue"); nd=text(new/"src/components/NotificationDialog.vue")
        tests=[
          ("backend_provider_import",os,ns,['const {provider} = require("./notification-providers/']),
          ("backend_provider_instance_registry",os,ns,["new {provider}()"]),
          ("frontend_provider_import",oi,ni,["import {provider} from"]),
          ("frontend_form_registry",oi,ni,["{provider}: {provider}"]),
          ("ui_category_registry",od,nd,["{provider}:"])
        ]
        for sid,a,b,pats in tests:
            if new_decl(a,b,pats,providers): sites.append(sid)
    else:
        ob=text(old/"server/notification-providers/law-r1-p2-membership-registry.js")
        nb=text(new/"server/notification-providers/law-r1-p2-membership-registry.js")
        of=text(old/"src/components/notifications/law-r1-p2-membership-registry.js")
        nf=text(new/"src/components/notifications/law-r1-p2-membership-registry.js")
        if new_decl(ob,nb,["const {provider} = require(","new {provider}()"],providers):
            sites.append("backend_membership_registry")
        if new_decl(of,nf,["import {provider} from","{provider}: {provider}","{provider}:"],providers):
            sites.append("frontend_membership_registry")
    return sites

def a_sites(arm:str,old:Path,new:Path):
    if arm=="DISPERSED_MEMBERSHIP_EXTENSION":
        # Status-quo path has no new shared boundary machinery.
        return []
    checks=[
      ("server_registry_hook","server/notification.js","lawR1P2MembershipRegistry"),
      ("frontend_form_registry_hook","src/components/notifications/index.js","lawR1P2NotificationForms"),
      ("ui_category_registry_hook","src/components/NotificationDialog.vue","lawR1P2NotificationCategories")
    ]
    out=[]
    for sid,rel,needle in checks:
        before=needle in text(old/rel); after=needle in text(new/rel)
        if after and not before: out.append(sid)
    return out

def contract_c(source:Path):
    p=source/"server/notification-providers/notification-provider.js"
    s=text(p)
    mandatory=[]
    if 'throw new Error("Have to override Notification.send(...)")' in s:
        mandatory.append("send")
    # No other mandatory override marker is accepted silently.
    markers=re.findall(r'Have to override Notification\.([A-Za-z0-9_]+)',s)
    unique=sorted(set(markers))
    if unique!=["send"] or mandatory!=["send"]:
        raise RuntimeError(f"unexpected mandatory provider contract: markers={unique}")
    return {"mandatory_runtime_capabilities":["send"],"demand_required_capabilities":["send"],"extraneous_count":0}

def phase_measure(arm:str,old:Path,new:Path,phase:str,q:int,c:int):
    providers=PHASE_PROVIDERS[phase]
    ss=s_sites(arm,old,new,providers)
    aa=a_sites(arm,old,new)
    lv,rows=churn(old,new)
    return {
      "S":len(ss),"L":lv,"C":c,"A":len(aa),"Q":q,
      "S_sites":ss,"A_sites":aa,"L_rows":rows
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--snapshots",required=True,type=Path)
    ap.add_argument("--source",required=True,type=Path)
    ap.add_argument("--q",required=True,type=Path)
    ap.add_argument("--constitution",required=True,type=Path)
    ap.add_argument("--out",required=True,type=Path)
    a=ap.parse_args()
    q=json.loads(a.q.read_text())
    constitution=json.loads(a.constitution.read_text())
    if q["verdict"]!="PASS_BOUNDED_Q" or q["q0"]!=1 or q["q1"]!=1:
        raise RuntimeError("Q gate not satisfied")
    contract=contract_c(a.source)
    c=contract["extraneous_count"]
    arms={}
    for arm,slug in ARMS.items():
        root=a.snapshots/slug
        p0=phase_measure(arm,root/"birth",root/"phase0","phase0",q["q0"],c)
        p1=phase_measure(arm,root/"phase0",root/"phase1","phase1",q["q1"],c)
        arms[arm]={
          "phase0":p0,
          "phase1":p1,
          "vector":{
            "phase0":[p0[k] for k in ("S","L","C","A","Q")],
            "phase1":[p1[k] for k in ("S","L","C","A","Q")]
          }
        }
    out={
      "protocol":constitution["protocol"],
      "stage":constitution["stage"],
      "source_commit":"398482d590daaac0d44e288c9be3bc6f6667f8b8",
      "oracle_strength":{
        "scope":q["oracle_scope"],
        "production_external_api_authority":q["production_external_api_authority"]
      },
      "contract_analysis":contract,
      "arms":arms,
      "scalarization":False,
      "winner":None
    }
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("LAW_R1_P3_SIMULTANEOUS_VECTOR_REVEAL=PASS")
    print(json.dumps({k:v["vector"] for k,v in arms.items()},sort_keys=True))

if __name__=="__main__": main()
