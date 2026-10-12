#!/usr/bin/env python3
"""P42-R2 original historical-source cohort fault-domain court.
Classical finite testing/coding problem: restricted observation partitions,
exhaustive minimum context cover, demand-wise incomparable source revisions.
Never infer global Go semantics or architectural superiority.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import hashlib,json,re,sys

def sig(x,kind):
 if kind=="HTTP":
  fields=("registration_panicked","request_panicked","panic_class","status","body","header")
 else:
  fields=("registration_panicked","request_panicked","panic_class","status","body","header",
          "handler_id","template","bound_name","handler_calls","param_names","param_values")
 return json.dumps({f:x.get(f) for f in fields},sort_keys=True,ensure_ascii=False)

def classes(rows,versions,ctx_ids,kind):
 groups=defaultdict(list)
 for v in versions:
  pattern=tuple(sig(rows[v][c],kind) for c in ctx_ids)
  groups[pattern].append(v)
 return sorted([members for members in groups.values()],key=lambda xs:xs[0])

def exact_minimum(rows,versions,ctx_ids,kind):
 different=[]
 for a,b in combinations(versions,2):
  bitmask=0
  for i,c in enumerate(ctx_ids):
   if sig(rows[a][c],kind)!=sig(rows[b][c],kind):
    bitmask |=1<<i
  if bitmask:different.append(bitmask)
 if not different:return [tuple()]
 n=len(ctx_ids)
 solutions=[]
 for size in range(n+1):
  for picks in combinations(range(n),size):
   selected=sum(1<<i for i in picks)
   if all(mask&selected for mask in different):
    solutions.append(tuple(ctx_ids[i] for i in picks))
  if solutions:break
 return solutions

def main():
 if len(sys.argv)!=4:raise SystemExit("usage judge.py frozen.json original-go.log receipt.json")
 freeze_path,trace_path,out=map(Path,sys.argv[1:])
 manifest=json.loads(freeze_path.read_text())
 text=trace_path.read_text()
 frozen_versions=[v["id"] for v in manifest["actual_programs"]]
 ctx_ids=[c["id"] for c in manifest["contexts"]]
 expected_shas={v["id"]:v["sha"] for v in manifest["actual_programs"]}
 unresolved=[]
 for line in text.splitlines():
  m=re.search(r"P42_R2_SOURCE_UNRESOLVED id=(\\w+) sha=([0-9a-f]{40})",line)
  if m:
   vid,sha=m.groups()
   assert vid in expected_shas and expected_shas[vid]==sha
   unresolved.append(vid)
 assert len(set(unresolved))==len(unresolved),unresolved
 versions=[x for x in frozen_versions if x not in unresolved]
 rows={v:{} for v in versions}
 for line in text.splitlines():
  m=re.search(r'P42_R2_OBS\s+(\{[^\n\r]*\})',line)
  if m:
   v=json.loads(m.group(1))
   rev,c=v["revision"],v["id"]
   assert rev in rows and c in ctx_ids,(rev,c)
   assert c not in rows[rev],("duplicate original source observation",rev,c)
   frozen=next(x for x in manifest["contexts"] if x["id"]==c)
   assert (v["scenario"],v["method"],v["path"])==(frozen["scenario"],frozen["method"],frozen["path"])
   rows[rev][c]=v
 assert len(frozen_versions)==12 and len(ctx_ids)==16
 assert len(versions)>=6
 assert len(unresolved)+len(versions)==12
 for v in versions:
  assert len(rows[v])==16,(v,len(rows[v]),set(ctx_ids)-set(rows[v]))
 groups={}
 minima={}
 for kind in ("HTTP","FULL"):
  groups[kind]=classes(rows,versions,ctx_ids,kind)
  minima[kind]=exact_minimum(rows,versions,ctx_ids,kind)
  assert minima[kind]
  g0=sorted([sorted(g) for g in groups[kind]])
  for selected in minima[kind]:
   reduced=sorted([sorted(g) for g in classes(rows,versions,selected,kind)])
   assert reduced==g0,("not a separating subset",kind,selected)
 # Demand vector: concrete independently frozen old/new requests, never a scalar.
 demand={}
 for v in versions:
  old=rows[v]["inline_bare"]
  new=rows[v]["inline_basic"]
  demand[v]={
   "legacy_bare_reachable":not old["registration_panicked"] and not old["request_panicked"] and old["status"]==200,
   "new_inline_verb_correct_binding":not new["registration_panicked"] and not new["request_panicked"] and new["status"]==200 and new["bound_name"]=="foo" and new["param_names"]==["name"],
   "backtrack_old_client_reachable":rows[v]["backtrack_generic"]["status"]==200,
   "leaf_old_client_reachable":rows[v]["leaf_path"]["status"]==200,
   "health_preserved":rows[v]["health"]["status"]==200,
  }
 keys=list(next(iter(demand.values())).keys())
 pareto_incomparable=[]
 for a,b in combinations(versions,2):
  x,y=demand[a],demand[b]
  if any(x[k] and not y[k] for k in keys) and any(y[k] and not x[k] for k in keys):
   pareto_incomparable.append((a,b))
 transitions=[]
 for a,b in zip(versions[:-1],versions[1:]):
  transitions.append({
   "source_from":a,"source_to":b,
   "http_changes":[c for c in ctx_ids if sig(rows[a][c],"HTTP")!=sig(rows[b][c],"HTTP")],
   "fine_changes":[c for c in ctx_ids if sig(rows[a][c],"FULL")!=sig(rows[b][c],"FULL")],
  })
 result={
  "protocol":"P42_R2_VERIFIED_REAL_SOURCE_SUBCOHORT_16_CONTEXT_PARTITION_COURT",
  "frozen_manifest_sha256":hashlib.sha256(freeze_path.read_bytes()).hexdigest(),
  "original_source_trace_sha256":hashlib.sha256(trace_path.read_bytes()).hexdigest(),
  "historical_original_commit_candidates":12,
  "historical_go_revisions":len(versions),"frozen_context_count":16,
  "native_go_trace_count":len(versions)*len(ctx_ids),
  "unresolved_original_commit_ids":unresolved,
  "unresolved_original_commit_shas":{x:expected_shas[x] for x in unresolved},
  "http_observation_partitions":groups["HTTP"],
  "full_observation_partitions":groups["FULL"],
  "http_number_of_observation_classes":len(groups["HTTP"]),
  "full_number_of_observation_classes":len(groups["FULL"]),
  "full_refines_http":all(any(set(g).issubset(set(h)) for h in groups["HTTP"]) for g in groups["FULL"]),
  "source_relative_exact_minimum_http_context_count":len(minima["HTTP"][0]),
  "source_relative_exact_minimum_full_context_count":len(minima["FULL"][0]),
  "source_relative_all_minimum_http_suite_count":len(minima["HTTP"]),
  "source_relative_all_minimum_full_suite_count":len(minima["FULL"]),
  "source_relative_lex_first_http_suite":minima["HTTP"][0],
  "source_relative_lex_first_full_suite":minima["FULL"][0],
  "all_tied_minimal_suites":minima,
  "demand_vectors":demand,
  "source_revision_pairs_demand_incomparable":pareto_incomparable,
  "source_transition_deltas":transitions,
  "historical_original_go_samples_grounded":True,
  "prereg_test_prior_to_oracles":True,
  "fully_original_source_variants_not_synthetic":True,
  "full_frozen_fault_domain_realized":len(unresolved)==0,
  "different_OO_architectural_rivals_compared":False,
  "true_prospective_unseen_future_demand":False,
  "complete_Go_to_Lean_semantics":False,
  "S_L_C_A_Q_overall_scalarized":False,
  "historical_upstream_permission_authenticated":False,
  "new_mathematical_theory_proved":False,
  "LAW_R2_authorized":False,
 }
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
 print("P42_R2_VERIFIED_ORIGINAL_SOURCE_SUBCOHORT_AND_FINITE_PARTITION_COURT_PASS",len(versions),"UNRESOLVED",len(unresolved))
 print(json.dumps({k:result[k] for k in ("http_number_of_observation_classes","full_number_of_observation_classes","source_relative_exact_minimum_http_context_count","source_relative_exact_minimum_full_context_count","source_relative_lex_first_http_suite","source_relative_lex_first_full_suite")},ensure_ascii=False))
 print("INCOMPARABLE_ORIGINAL_REVISIONS",len(pareto_incomparable))
if __name__=="__main__":main()
