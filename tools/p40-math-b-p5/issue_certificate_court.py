#!/usr/bin/env python3
"""Machine check P40 P5 original Go holdout log against the prior immutable manifest.
The receipt is a verifiable experiment audit, NOT a semantic proof that Go itself
refines the Lean model. The declared abstentions never increase prediction scores.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

def main():
    if len(sys.argv) != 5:
        raise SystemExit("usage issue_certificate_court.py prereg.json ecosystem native.log receipt.json")
    manifest_path, ecology, log_path, result_path = map(str, sys.argv[1:])
    m = json.loads(Path(manifest_path).read_text())
    assert m["contract"] == "P40_MATH_B_P5_ISSUE_DERIVED_PREREG_V1"
    assert ecology in {"echo", "gin"}
    relevant = [row for row in m["cases"] if row["ecosystem"] == ecology]
    assert len(relevant) == 4
    log = Path(log_path).read_text()
    actual = re.findall(r"P40_P5_LOCKED_PREDICTION_PASS\s+([A-Z0-9-]+)", log)
    abstains = re.findall(r"P40_P5_ABSTAIN_OBSERVATION\s+id=([A-Z0-9-]+)", log)
    expected = [r["id"] for r in relevant if r["forecast"] != "ABSTAIN"]
    expected_abstains = [r["id"] for r in relevant if r["forecast"] == "ABSTAIN"]
    assert sorted(actual) == sorted(expected), (actual, expected)
    assert sorted(abstains) == sorted(expected_abstains), (abstains, expected_abstains)
    assert "P40_P5_FORECAST_FALSIFIED" not in log
    evidence = []
    for row in relevant:
        matches = [line for line in log.splitlines() if
                   "P40_P5_ABSTAIN_OBSERVATION id="+row["id"] in line or
                   "P40_P5_LOCKED_PREDICTION_PASS "+row["id"] in line]
        assert len(matches) == 1
        evidence.append({
            "id": row["id"],
            "source_issue": row["source"],
            "locked_forecast": row["forecast"],
            "verdict": "ABSTAIN_OBSERVED" if row["forecast"] == "ABSTAIN" else "LOCKED_PREDICTION_CONFIRMED",
            "native_go_log": matches[0].strip(),
        })
    receipt = {
        "protocol": "P40_P5_ISSUE_PREDICTION_CERTIFICATE_V1",
        "scope": "Four issue-derived native scenarios for one pinned Go implementation",
        "manifest_sha256": hashlib.sha256(Path(manifest_path).read_bytes()).hexdigest(),
        "native_log_sha256": hashlib.sha256(Path(log_path).read_bytes()).hexdigest(),
        "ecosystem": ecology,
        "certified_predicted": len(actual),
        "reported_abstentions": len(abstains),
        "cases": evidence,
        "warning": "Proof of test provenance and named native observations, NOT a Go-to-Lean simulation proof or prospective generalization to real PR fixes."
    }
    Path(result_path).write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print("P40_P5_MACHINE_ORIGINAL_GO_CERTIFICATE_PASS", ecology, len(actual), len(abstains))
if __name__ == "__main__":
    main()
