#!/usr/bin/env python3
"""P35-P4 source audit, with pre-demand fixed chi/v5.1.0 and rival sets."""
import difflib, hashlib, json, pathlib, subprocess, sys
root=pathlib.Path(__file__).resolve().parents[2]
origin=pathlib.Path(sys.argv[1]).resolve()
ast_bin=pathlib.Path(sys.argv[2]).resolve()
result={"baseline_commit":"67be7d9cafdaeb4e04e887ff78d09e030ee43b00","preseal_commit":"5d31ade7711e382450e62083a4dc831a31e665fe","arms":{},"rivals":{}}
def fp(p):
 return json.loads(subprocess.check_output([str(ast_bin),str(p)],text=True))
for arm in ["independent","shared"]:
 world=root/"tools"/"p35-p4"/"arms"/arm
 edit=[];add=rem=0;funcs=[];created=[]
 for p in sorted(world.glob("*.go")):
  pre=origin/p.name
  a=pre.read_text().splitlines(True) if pre.exists() else []
  b=p.read_text().splitlines(True)
  delta=list(difflib.unified_diff(a,b))
  if delta: edit.append(p.name)
  add+=sum(l.startswith("+") and not l.startswith("+++") for l in delta)
  rem+=sum(l.startswith("-") and not l.startswith("---") for l in delta)
  now=fp(p);old=fp(pre) if pre.exists() else {}
  funcs+= [k.removeprefix("func:") for k in now if k.startswith("func:") and k in old and old[k]!=now[k]]
  created+= [k.removeprefix("func:") for k in now if k.startswith("func:") and k not in old]
 assert sorted(funcs)==["AllowContentType","contentEncoding"],(arm,funcs)
 result["arms"][arm]={"changed_files":edit,"changed_file_count":len(edit),"changed_existing_functions":sorted(funcs),"new_functions":sorted(created),"source_lines_added":add,"source_lines_removed":rem,"sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(world.glob("*.go"))}}
observed=set(result["arms"]["independent"]["changed_existing_functions"])
for name,candidates in [("B0plus_static_impact",["ContentCharset","contentEncoding","AllowContentType"]),("B2_Parnas_information_hiding",["contentEncoding","AllowContentType"])]:
 c=set(candidates);result["rivals"][name]={"candidates":sorted(c),"precision":len(c&observed)/len(c),"recall":len(c&observed)/len(observed),"prediction":"PRESEALED_CONDITIONAL"}
result["rivals"]["B1_cochange"]={"charset_production_commits":1,"type_production_commits":5,"verified_joint_production_commits":0,"status":"INSUFFICIENT_HISTORY_TO_PREDICT_PAIR","prospective_metric":None}
result["limits"]={"full_CSDG_executed":False,"developer_time_measured":False,"future_change_value_measured":False,"new_predictive_law_proven":False}
print(json.dumps(result,ensure_ascii=False,indent=2))
