#!/usr/bin/env python3
"""Prospectively frozen second-demand incremental Go source edit comparison."""
import difflib, hashlib, json, pathlib, subprocess, sys
root=pathlib.Path(__file__).resolve().parents[2]
ast_bin=pathlib.Path(sys.argv[1]).resolve()
def syms(p):
 return json.loads(subprocess.check_output([str(ast_bin),str(p)],text=True))
out={"d4_preseal":"5d31ade7711e382450e62083a4dc831a31e665fe","d5_preoutcome_preseal":"880cdc6660374d7b7e34f186f6c5e10d0aa93920","before_d5_arm_commit":"0045c078e8e09b1a2c108a912af19c7fc8b23a18","incremental":{},"prospective_predictions":{"independent":{"changed_files":2,"changed_existing_functions":["AllowContentType","contentEncoding"]},"shared":{"changed_files":1,"changed_existing_functions":["parseCanonicalContentType"]}}}
for arm in ("independent","shared"):
 before=root/"tools"/"p35-p4"/"arms"/arm
 after=root/"tools"/"p35-p4b"/"arms"/arm
 changed_files=[];changed_functions=[];added=removed=0
 for p in sorted(after.glob("*.go")):
  old=before/p.name
  a=old.read_text().splitlines(True) if old.exists() else []
  b=p.read_text().splitlines(True)
  df=list(difflib.unified_diff(a,b))
  if df:changed_files.append(p.name)
  added+=sum(x.startswith("+") and not x.startswith("+++") for x in df)
  removed+=sum(x.startswith("-") and not x.startswith("---") for x in df)
  o=syms(old) if old.exists() else {};n=syms(p)
  changed_functions += [k.removeprefix("func:") for k in n if k.startswith("func:") and k in o and n[k]!=o[k]]
 actual={"changed_files":len(changed_files),"production_file_names":changed_files,"changed_existing_functions":sorted(changed_functions),"count_changed_existing_functions":len(changed_functions),"lines_added":added,"lines_removed":removed}
 expected=out["prospective_predictions"][arm]
 assert actual["changed_files"]==expected["changed_files"],(arm,actual,expected)
 assert actual["changed_existing_functions"]==expected["changed_existing_functions"],(arm,actual,expected)
 out["incremental"][arm]=actual
out["comparison"]={"D4_initial_changed_files":{"independent":2,"shared":3},"D5_incremental_changed_files":{"independent":2,"shared":1},"D4_plus_D5_change_site_visits":{"independent":4,"shared":4},"sign_reversal_in_incremental_edit_count":True,"overall_lifecycle_winner":"NOT_IDENTIFIED","B0plus_and_Parnas_B2_explain":True,"B1_history_support":"INSUFFICIENT","new_universal_design_law":False}
print(json.dumps(out,ensure_ascii=False,indent=2))
