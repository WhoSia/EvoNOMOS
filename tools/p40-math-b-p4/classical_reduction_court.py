#!/usr/bin/env python3
"""Independent baseline encodings on the frozen, externally Go-verified P40-P4 case court.

This script scores against preregistered outcome labels ONLY AFTER source-heldout
Actions #38051063271 independently verified all 16. It does not replace that
original-source runtime and uses a deliberately selected closed grammar.
"""
import json
from collections import Counter
from pathlib import Path

CASES = Path(__file__).with_name("preregistered_predictions.json")
run_id = "38051063271"
reference = json.loads(CASES.read_text())
assert reference["contract"] == "P40_MATH_B_P4_PREREG_V1"
cases = reference["cases"]
assert len(cases) == 16

def naive_local_only(case):
    return "accept"    # independent edits both locally pass

def literal_duplicate_only(case):
    a, b = case["edits"]
    return "reject" if a["method"] == b["method"] and a["pattern"] == b["pattern"] else "accept"

def classical_implementation_csp(case):
    # A classical source-aware CSP model on exactly the admitted grammar;
    # source-anchored rule, NOT a new category-theoretic law.
    a, b = case["edits"]
    eco = case["ecosystem"]
    if eco == "chi":
        occupied_mount_pattern = (a["pattern"] == b["pattern"]
            or ("/pros/{" in a["pattern"] and "/pros/{" in b["pattern"]))
        return "reject" if occupied_mount_pattern else "accept"
    if eco == "httprouter":
        overlap = (a["pattern"] == b["pattern"]
            or ((":tenant" in a["pattern"] and "/pros/public/" in b["pattern"])
                or (":tenant" in b["pattern"] and "/pros/public/" in a["pattern"])))
        return "reject" if (a["method"] == b["method"] and overlap) else "accept"
    if eco == "echo":
        # Separate static/parameter trie children and default duplicate overwrite.
        return "accept"
    raise ValueError(eco)

variants = {
    "local_acceptance_only": naive_local_only,
    "literal_duplicate_source_only": literal_duplicate_only,
    "classical_source_aware_csp": classical_implementation_csp,
}
scores = {}
for name, predict in variants.items():
    bad = []
    per_ecology = {}
    for row in cases:
        correct = predict(row) == row["forecast"]
        per_ecology.setdefault(row["ecosystem"], [0, 0])
        per_ecology[row["ecosystem"]][1] += 1
        per_ecology[row["ecosystem"]][0] += int(correct)
        if not correct:
            bad.append(row["id"])
    scores[name] = {
        "correct": len(cases)-len(bad), "total": len(cases),
        "misclassified": bad, "by_ecology": per_ecology
    }
assert scores["local_acceptance_only"]["correct"] == 10
assert scores["literal_duplicate_source_only"]["correct"] == 11
assert scores["classical_source_aware_csp"]["correct"] == 16
result = {
    "contract":"P40_P4_CLASSICAL_REDUCTION_V1",
    "externally_verified_native_run":run_id,
    "important_limit":"Scores use locked labels independently corroborated by a separate original-Go Action. The CSP result is an encoding of the same implementation rules, not an independent discovery or generalization.",
    "historical_solid_axioms_independence":"NOT_PROVED",
    "scores":scores,
    "locked_distribution":dict(Counter(c["forecast"] for c in cases))
}
out=Path(__file__).with_name("classical_reduction_receipt.json")
out.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
print("P40_P4_CLASSICAL_CSP_COLLAPSE_AND_WEAK_ABLATIONS_PASS",[(k,v["correct"]) for k,v in scores.items()])
