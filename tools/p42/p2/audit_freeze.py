#!/usr/bin/env python3
"""P42-P2: validate source/test preregistration, not post-hoc client oracle."""
import hashlib,json,sys
from pathlib import Path
def main():
 if len(sys.argv)!=3:raise SystemExit("usage: freeze.py manifest receipt")
 p,out=map(Path,sys.argv[1:])
 d=json.loads(p.read_text())
 assert d["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P2_PRE_NATIVE_BEHAVIOR_FREEZE_V1"
 assert d["status"]=="FROZEN_BEFORE_P42_P2_NATIVE_GO_TESTS"
 assert d["context"]["pre_sha"]=="5440f99719cc8de4be2ae6abfc8f275302791730"
 assert d["context"]["post_sha"]=="f085ffbe8f99de165bd920746920000ab56bd6bc"
 assert d["context"]["source_code_read_only"] is True
 a=d["frozen_predictions"]
 assert len(a)==5 and len({x["case"] for x in a})==5
 assert {(x["case"],x["before_http_status"],x["after_http_status"]) for x in a}=={
  ("health",200,200),("bare",200,404),("inline",200,200),("other",200,404),("masked-inline",200,200)}
 assert len(d["fixture"]["observer_columns"])>=9
 assert d["tcs_scope"]["source_to_lean_simulation_proven"] is False
 assert d["classical_reference_model"]["predicted_novel_superiority"] is False
 assert d["tcs_scope"]["historical_authority"]=="UNKNOWN; no claim PR was illegitimate"
 v={"status":"P42_P2_FIVE_CONTEXT_PRE_NATIVE_OBSERVER_FREEZE_PASS","sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"contexts":len(a),"historical_original_source_pins":2,"blind_new_issue":False,"source_to_lean_bridge":False,"historical_authority_authenticated":False,"LAW_R2":False}
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(v,indent=2)+"\n")
 print(v["status"])
if __name__=="__main__":main()
