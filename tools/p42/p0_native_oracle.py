#!/usr/bin/env python3
"""P42 P0: certify native Go observations vs ancestor-frozen six-case hypotheses.
Comparator is a declared source-aware classical guarded rule model, not a
prospective independent predictor and not a new OO law."""
import re,json,hashlib,sys
from pathlib import Path
def classical_prediction(item):
 eco=item["ecosystem"];kind=item["intervention"]
 admitted= not (eco=="httprouter" and kind=="collision")
 if not admitted:
  return dict(source_admitted=False,old_frame="NOT_APPLICABLE",new_goal="REJECTED",handler_result="NOT_APPLICABLE")
 if kind=="collision":
  return dict(source_admitted=True,old_frame="VIOLATED",new_goal="REPLACES_OLD",handler_result="NEW")
 if kind=="provider":
  return dict(source_admitted=True,old_frame="VIOLATED",new_goal="DIVERTED",handler_result="PROVIDER")
 if kind=="separate_method":
  return dict(source_admitted=True,old_frame="PRESERVED",new_goal="POST_OWN_HANDLER",handler_result="OLD")
 return dict(source_admitted=True,old_frame="PRESERVED",new_goal="FULFILLED",handler_result="OLD")
def main():
 if len(sys.argv)!=5:raise SystemExit("usage p0_oracle.py frozen.json echo.log httprouter.log receipt.json")
 freeze_path,echo_path,ht_path,out=map(Path,sys.argv[1:])
 m=json.loads(freeze_path.read_text())
 assert m["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P0_FREEZE_V1"
 observed=[]
 for path,eco in [(echo_path,"Echo"),(ht_path,"httprouter")]:
  log=path.read_text()
  assert "\nFAIL\t" not in log and "\n--- FAIL:" not in log
  for line in log.splitlines():
   hit=re.search(r'P42_NATIVE_CASE\s+(\{[^\r\n]*\})',line)
   if hit:
    item=json.loads(hit.group(1))
    assert item["ecosystem"]==eco
    observed.append(item)
 assert len(observed)==6 and len({o["id"] for o in observed})==6
 actual={x["id"]:x for x in observed}
 hypoth={x["id"]:x for x in m["preregistrations"]}
 assert set(actual)==set(hypoth)
 fields=("source_admitted","old_frame","new_goal","handler_result")
 checks=[]
 for case_id in sorted(hypoth):
  truth=actual[case_id];expected=hypoth[case_id]
  assert truth["authority"]=="UNKNOWN"
  mismatch={f:(expected[f],truth[f]) for f in fields if expected[f]!=truth[f]}
  classical=classical_prediction(expected)
  classical_mismatch={f:(classical[f],truth[f]) for f in fields if classical[f]!=truth[f]}
  obs=truth["observation"]
  if truth["old_frame"]=="PRESERVED":
   assert (obs["status"],obs["body"],obs["contract_header"],obs["handler_id"],obs["invocations"]) == (200,"OLD","old","OLD",1)
  elif truth["old_frame"]=="VIOLATED":
   assert obs["status"]==200 and obs["handler_id"] in ("NEW","PROVIDER")
   assert obs["body"]!="OLD" and obs["contract_header"]!="old" and obs["invocations"]==0
  else:
   assert truth["source_admitted"] is False and obs["status"]==0
  checks.append(dict(id=case_id,frozen_prediction_pass=not bool(mismatch),classical_source_aware_pass=not bool(classical_mismatch),mismatch=mismatch,competing_model="KNOWN_PINNED_SOURCE_RULES"))
 assert all(x["frozen_prediction_pass"] for x in checks)
 assert all(x["classical_source_aware_pass"] for x in checks)
 receipt={
   "protocol":"P42_P0_FROZEN_NATIVE_TWO_ECOLOGY_SOURCE_AND_CLASSICAL_COURT_PASS",
   "frozen_manifest_sha256":hashlib.sha256(freeze_path.read_bytes()).hexdigest(),
   "echo_original_log_sha256":hashlib.sha256(echo_path.read_bytes()).hexdigest(),
   "httprouter_original_log_sha256":hashlib.sha256(ht_path.read_bytes()).hexdigest(),
   "cases_checked":6,
   "frozen_source_hypotheses_correct":6,
   "source_aware_classical_guarded_CSP_correct":6,
   "new_blind_issue_prediction":False,
   "independent_prospective_classical_comparator":False,
   "upstream_historical_change_rights":"UNKNOWN",
   "client_observer_set":"one declared GET /p42/old, five selected coordinates",
   "user_source_modified":False,
   "original_source_modified":False,
   "history_complete_governance":False,
   "cross_implementation_universal_law":False,
   "LAW_R2_authorized":False,
   "cases":checks
 }
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
 print("P42_P0_SIX_OF_SIX_FROZEN_ORIGINAL_GO_AND_CLASSICAL_COURT_PASS")
if __name__=="__main__":main()
