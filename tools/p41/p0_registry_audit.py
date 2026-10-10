#!/usr/bin/env python3
"""P41-P0 evidence type checker.

It validates epistemic types and source receipts already verified in P40,
not content truth or live permission. No automatic promotion from synthetic
to original native evidence is permitted.
"""
import hashlib
import json
import sys
from pathlib import Path

EXPECTED = {"A","B","C","D","E","F"}
NATIVE = {"A","B","D","E"}
SYNTHETIC = {"C","F"}
KNOWN_RECEIPTS = {
    "A": (38060623268,"3882266a3641a36fc2111b48cd597adab1c1ecea"),
    "B": (38052437653,"3882266a3641a36fc2111b48cd597adab1c1ecea"),
    "D": (38051358314,"3882266a3641a36fc2111b48cd597adab1c1ecea"),
    "E": (38047274495,"167e1e3bd039d060696b99c8da4e876ae04f42c1")
}
def main():
    if len(sys.argv)!=3:
        raise SystemExit("usage: p0_registry_audit.py input.json receipt.json")
    infile,outfile=map(Path,sys.argv[1:])
    data=json.loads(infile.read_text())
    assert data["protocol"]=="EVONOMOS_G8_LAW_R1_P41_P0_EVIDENCE_MATRIX_V1"
    assert data["status"]=="OPEN"
    definitions=data["definitions"]
    assert len(definitions)==6
    assert {r["code"] for r in definitions}==EXPECTED
    for r in definitions:
        key=r["code"]
        assert len(r["predicate"])>14 and len(r["observation"])>18
        assert len(r["missing"])>20
        if key in NATIVE:
            assert r["evidence_status"]=="NATIVE_BOUNDED"
            assert r["source"]["repo"]=="WhoSia/EvoNOMOS"
            assert (r["source"]["run_id"],r["source"]["original_upstream_commit"])==KNOWN_RECEIPTS[key]
        else:
            assert key in SYNTHETIC
            assert r["evidence_status"]=="SYNTHETIC_ONLY"
            assert r["source"] is None
    claims=["A-F independence","historical SOLID","new-law"]
    assert any("independence" in x for x in data["proof_debt"])
    assert any("HOLD" in x for x in data["proof_debt"])
    receipt={
        "protocol":"P41_P0_EPISTEMIC_TYPE_AUDIT_PASS",
        "input_sha256":hashlib.sha256(infile.read_bytes()).hexdigest(),
        "native_bounded_count":len(NATIVE),
        "synthetic_only_count":len(SYNTHETIC),
        "proven_six_axiom_independence":False,
        "source_Go_operational_semantics_proven":False,
        "full_historical_SOLID_derived":False,
        "law_R2_authorized":False
    }
    outfile.parent.mkdir(parents=True,exist_ok=True)
    outfile.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("P41_P0_PROVENANCE_BOUNDARY_AUDIT_PASS native=4 synthetic=2")
if __name__=="__main__":
    main()
