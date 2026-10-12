#!/usr/bin/env python3
"""Independent P42-R2 witness court: finite minimax set cover and S/L/C/A/Q surface.
Reads the separately CI-certified original Go log and finite verdict artifact.
This is an independent algorithm, not new mathematical priority.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import hashlib,json,re,subprocess,sys

def parse_logs(path):
 rows=defaultdict(dict)
 for line in path.read_text().splitlines():
  m=re.search(r'P42_R2_OBS\s+(\{[^\r\n]*\})',line)
  if m:
   r=json.loads(m.group(1)); key=r["id"]
   if key in rows[r["revision"]]:raise AssertionError("duplicate trace")
   rows[r["revision"]][key]=r
 return rows

def obs(r,level):
 common=("registration_panicked","request_panicked","panic_class","status","body","header")
 fine=("handler_id","template","param_names","param_values","bound_name","handler_calls")
 return tuple(json.dumps(r.get(k),sort_keys=True) for k in common+(fine if level=="FULL" else ()))

def group(rows,versions,contexts,level):
 by=defaultdict(list)
 for revision in versions:
  fingerprint=tuple(obs(rows[revision][c],level) for c in contexts)
  by[fingerprint].append(revision)
 return sorted(tuple(sorted(x)) for x in by.values())

def exact_independent(rows,versions,contexts,level):
 all_classes=group(rows,versions,contexts,level)
 tested=0
 for size in range(len(contexts)+1):
  candidates=[]
  for suite in combinations(contexts,size):
   tested+=1
   if group(rows,versions,suite,level)==all_classes:
    candidates.append(suite)
  if candidates:return candidates,tested
 raise AssertionError("full frozen suite itself failed to partition")

def change_geometry(root,programs):
 out=[]
 for former,later in zip(programs[:10],programs[1:11]):
  proc=subprocess.run(["git","-C",str(root),"diff","--numstat",former["sha"],later["sha"]],capture_output=True,text=True,check=True)
  changes=[]
  for row in proc.stdout.splitlines():
   a,d,path=row.split("\t",2)
   if not(a.isdigit() and d.isdigit()):raise ValueError("binary source diff requires separate scope")
   changes.append({"path":path,"lines_added":int(a),"lines_deleted":int(d),"is_test_file":path.endswith("_test.go")})
  source=[c for c in changes if not c["is_test_file"]]
  test=[c for c in changes if c["is_test_file"]]
  out.append({
   "from":former["id"],"to":later["id"],
   "actual_source_sha":later["sha"],
   "source_files_touched":[c["path"] for c in source],
   "test_files_touched":[c["path"] for c in test],
   "S_implementation_files_touched":len(source),
   "L_implementation_line_edits":sum(c["lines_added"]+c["lines_deleted"] for c in source),
   "test_line_edits":sum(c["lines_added"]+c["lines_deleted"] for c in test),
   "method":"actual original git diff --numstat; NOT person-hours / difficulty / architecture-independent cost"
  })
 return out

def main():
 if len(sys.argv)!=7:raise SystemExit("usage verify.py manifest errata go.log court.json original-git-checkout receipt.json")
 manifestp,erratap,logp,sourcep,root,out=map(Path,sys.argv[1:])
 manifest=json.loads(manifestp.read_text());errata=json.loads(erratap.read_text());claimed=json.loads(sourcep.read_text())
 assert claimed["protocol"]=="P42_R2_VERIFIED_REAL_SOURCE_SUBCOHORT_16_CONTEXT_PARTITION_COURT"
 assert errata["protocol"]=="P42_P2_R2_POST_FREEZE_SOURCE_LOCATOR_ERRATUM_V1"
 programs=[dict(x) for x in manifest["actual_programs"]]
 assert programs[3]["sha"]==errata["frozen_transcription"]
 programs[3]["sha"]=errata["corrected_original_commit"]
 assert len(programs)==12
 rows=parse_logs(logp)
 versions=[x["id"] for x in programs]
 ctx=[x["id"] for x in manifest["contexts"]]
 assert set(rows)==set(versions)
 assert all(set(rows[v])==set(ctx) for v in versions)
 independent={}
 for kind in ("HTTP","FULL"):
  suites,nchecked=exact_independent(rows,versions,ctx,kind)
  classes=group(rows,versions,ctx,kind)
  expected=[tuple(x) for x in claimed["all_tied_minimal_suites"][kind]]
  assert set(suites)==set(expected),(kind,suites,expected)
  assert len(classes)==claimed[kind.lower()+"_number_of_observation_classes"]
  independent[kind]={
    "classes":classes,"minimum":len(suites[0]),
    "all_minimal_suite_count":len(suites),
    "subsets_exhaustively_checked":nchecked,
    "minimum_suites":suites
  }
 demand=claimed["demand_vectors"]
 assert demand["PRE"]["legacy_bare_reachable"]
 assert not demand["PRE"]["new_inline_verb_correct_binding"]
 assert not demand["MERGED"]["legacy_bare_reachable"]
 assert demand["MERGED"]["new_inline_verb_correct_binding"]
 assert any(set(x)=={"PRE","MERGED"} for x in claimed["source_revision_pairs_demand_incomparable"])
 geometry=change_geometry(root,programs)
 assert len(geometry)==10
 assert all(g["S_implementation_files_touched"]>=0 for g in geometry)
 record={
  "protocol":"P42_R2_INDEPENDENT_12_ACTUAL_SOURCE_PARETO_AND_MINIMUM_CERTIFICATE_PASS",
  "verified_source_sha256":hashlib.sha256(sourcep.read_bytes()).hexdigest(),
  "log_sha256":hashlib.sha256(logp.read_bytes()).hexdigest(),
  "original_pr_source_locator_fixed_after_freeze":True,
  "twelve_original_code_states":True,
  "independent_hitting_set_and_partition":independent,
  "PRE_to_MERGED_old_vs_new_requirement_preference_reversal":True,
  "architecture_level_superiority_or_sign_reversal":False,
  "architecture_geometry_s_l_coordinates":geometry,
  "C_client_binding_obligations":"measured selected request semantics; not complete interface conformance cost",
  "A_authority":"UNKNOWN, no historical edit entitlement inferred",
  "Q_selected_client_semantics":"192 actual original Go trace outcomes, not all requirements",
  "S_L_C_A_Q_scalar_winner":None,
  "total_demand_incomparable_pairs":len(claimed["source_revision_pairs_demand_incomparable"]),
  "full_echo_language_semantics_proved":False,
  "global_new_TCS_result_proved":False,
  "LAW_R2_authorized":False
 }
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n")
 print("P42_R2_INDEPENDENT_12_ORIGINAL_COMMITS_SOURCE_GEOMETRY_MINIMUM_PARETO_PASS")
 print(json.dumps({x:{"classes":len(independent[x]["classes"]),"minimum_contexts":independent[x]["minimum"],"number_of_minimal_suites":independent[x]["all_minimal_suite_count"],"tested_subsets":independent[x]["subsets_exhaustively_checked"],"classes_members":independent[x]["classes"]} for x in ("HTTP","FULL")},ensure_ascii=False))
 print("ACTUAL_PRE_MERGED_DEMAND_SIGN_REVERSAL",demand["PRE"],demand["MERGED"])
 print("ACTUAL_SOURCE_STAGE_S_L",[(x["to"],x["S_implementation_files_touched"],x["L_implementation_line_edits"],x["test_line_edits"]) for x in geometry])
if __name__=="__main__":main()
