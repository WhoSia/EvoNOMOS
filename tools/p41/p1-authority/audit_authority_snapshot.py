#!/usr/bin/env python3
"""Validate a previously authenticated GitHub role snapshot's *epistemic scope*.
This offline audit cannot itself reauthenticate the historical observation.
"""
import json,sys,hashlib
from pathlib import Path
def main():
    if len(sys.argv)!=3:raise SystemExit("usage: audit_authority_snapshot.py input.json out.json")
    path,out=map(Path,sys.argv[1:])
    data=json.loads(path.read_text())
    assert data["protocol"]=="P41_P1_C_GITHUB_AUTHORITY_EVIDENCE_SNAPSHOT_V1"
    assert data["observed_local_date"]=="2026-10-11"
    assert data["independent_source_status"]=="AUTHENTICATED_PLATFORM_OPERATIONAL_SNAPSHOT_ONLY"
    assert data["general_p41_C_axiom_status"]=="UNPROVED"
    assert data["verification"][0]["observed_permission"]=="admin"
    assert data["verification"][1]["observed_authenticated_permissions"]["admin"] is True
    assert data["verification"][2]["observed_review_states"]==["COMMENTED","COMMENTED"]
    assert len(data["claim_not_granted"])>=5
    assert any("historical" in s for s in data["claim_not_granted"])
    assert any("institutional" in s for s in data["claim_not_granted"])
    receipt={
      "protocol":"P41_P1_PERMISSION_SNAPSHOT_TYPE_AUDIT_V1",
      "input_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
      "platform_permission_observed":"admin",
      "connector_observation_independently_reauthenticated_by_CI":False,
      "version_indexed_historical_permission_proved":False,
      "normative_institutional_legitimacy_proved":False,
      "general_A_F_independence_proved":False
    }
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("P41_P1_AUTHENTICATED_PLATFORM_SNAPSHOT_WITH_LIMITS_TYPECHECK_PASS")
if __name__=="__main__":main()
