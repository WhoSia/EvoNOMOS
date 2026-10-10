#!/usr/bin/env python3
"""P41 P3 source test log -> five-principle classical-reduction witness ledger.
Manual classical labels are explanatory and NOT a prospective rival predictor.
"""
import json,sys,hashlib
from pathlib import Path
def main():
 if len(sys.argv)!=4: raise SystemExit("usage p3_reduction_audit.py manifest.json original_go.log output.json")
 path,log_path,out=map(Path,sys.argv[1:])
 doc=json.loads(path.read_text());log=log_path.read_text()
 assert doc["protocol"]=="EVONOMOS_P41_P3_FIVE_CLASSICAL_REDUCTION_COURT_V1"
 assert len(doc["cases"])==5
 assert len({c["id"] for c in doc["cases"]})==5
 assert {c["id"] for c in doc["cases"]}=={"SRP","OCP","LSP","ISP","DIP"}
 assert "FAIL" not in log and "P41_P3_" in log
 for c in doc["cases"]:
  marker=c["nativeToken"]
  assert len(marker)>25 and log.count(marker)==1,(c["id"],marker,log.count(marker))
  assert len(c["classical"])>18 and len(c["conditional"])>18
  assert len(c["lean"])>10
  if c["id"]=="OCP":
   assert log.count(c["counterexample"])==1
 assert doc["expectedNativeTokens"]==6
 receipt={
  "protocol":"P41_P3_SOURCE_GROUNDED_CLASSICAL_REDUCTION_AUDIT_V1",
  "manifest_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
  "native_go_log_sha256":hashlib.sha256(log_path.read_bytes()).hexdigest(),
  "original_echo_pin":doc["originalEcho"],
  "five_scoped_principles_verified":5,
  "six_source_verdict_markers_verified":6,
  "classical_explanatory_competitors":["frame","guarded update/context refinement","Liskov-Wing behavioral equivalence","interface projection","provider data refinement"],
  "independent_blind_classical_prediction_comparison":False,
  "historical_SOLID_reconstructed":False,
  "universal_A_F_independence_proved":False,
  "new_nonclassical_OO_law_proved":False,
  "cases":doc["cases"],
 }
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
 print("P41_P3_ORIGINAL_SOURCE_FIVE_CLASSICAL_REDUCTIONS_AND_SIX_MARKERS_AUDIT_PASS")
if __name__=="__main__": main()
