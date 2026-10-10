#!/usr/bin/env python3
"""P42-P0 freeze-only contract audit; validates cases and epistemic limits.
No future Go result is read in this stage."""
import json, hashlib, sys
from pathlib import Path

def main():
    if len(sys.argv)!=3: raise SystemExit("usage: audit_freeze.py manifest.json receipt.json")
    source,out=map(Path,sys.argv[1:])
    doc=json.loads(source.read_text())
    assert doc["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P0_FREEZE_V1"
    assert doc["status"]=="FROZEN_BEFORE_P42_NATIVE_HOLDOUT"
    original={e["ecosystem"]:e["sha"] for e in doc["provenance"]["original_sources"]}
    assert original=={"Echo":"3882266a3641a36fc2111b48cd597adab1c1ecea","httprouter":"484018016424d215c0b87c42f4c9b57d980fbd00"}
    governance=doc["provenance"]["governance"]
    assert governance["historical_external_edit_authority"]=="UNKNOWN"
    assert not governance["upstream_actor_identity_or_rights_claimed"]
    assert not governance["upstream_in_force_branch_policy_verified"]
    old=doc["old_request"]
    assert (old["method"],old["path"],old["status"],old["body"],old["header_value"],old["handler_id"],old["handler_invocations"])==("GET","/p42/old",200,"OLD","old","OLD",1)
    cases=doc["preregistrations"]
    assert len(cases)==6
    assert len({x["id"] for x in cases})==6
    assert {x["id"] for x in cases}=={
      "echo-disjoint","echo-collision","echo-provider",
      "httprouter-disjoint","httprouter-collision","httprouter-separate-method"}
    assert sum(x["source_admitted"] for x in cases)==5
    assert sum(x["old_frame"]=="PRESERVED" for x in cases)==3
    assert sum(x["old_frame"]=="VIOLATED" for x in cases)==2
    assert sum(x["old_frame"]=="NOT_APPLICABLE" for x in cases)==1
    assert any(x["name"]=="SOURCE_AWARE_CLASSICAL_GUARDED_CSP" for x in doc["comparators"])
    assert any("not a prospective blind" in x for x in doc["nonclaims"])
    assert any("ONE fixed GET" in x for x in doc["nonclaims"])
    receipt={
      "protocol":"P42_P0_FREEZE_BEFORE_NATIVE_EXECUTION_PASS",
      "manifest_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
      "frozen_cases":6,
      "selected_old_client_observer_coordinates":7,
      "original_upstream_source_modified":False,
      "blind_unseen_issue_research":False,
      "upstream_historical_edit_authorization_proved":False,
      "permission_unknown_remains_unknown":True,
      "strong_classical_source_aware_comparator_declared":True,
      "full_SOLID_axioms_proved":False,
      "LAW_R2_authorized":False
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("P42_P0_SIX_CASE_FROZEN_SOURCE_AUTHORITY_AND_OBSERVER_BUDGET_PASS")
if __name__=="__main__":main()
