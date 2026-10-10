#!/usr/bin/env python3
"""P40 P4 preregistered, intentionally scoped admission rule checker.

Go AST witness extraction confirms the predeclared source mechanics. These
hypothesis rules are source-informed human abstractions, NOT automatically
inferred executable semantics or a full source correctness proof.
"""
import json
import hashlib
import sys
from pathlib import Path

def forecast(row):
    a, b = row["edits"]
    eco = row["ecosystem"]
    if eco == "chi":
        return ("reject" if a["pattern"] == b["pattern"]
                or ("/pros/{" in a["pattern"] and "/pros/{" in b["pattern"])
                else "accept")
    if eco == "httprouter":
        same_method = a["method"] == b["method"]
        duplicate = a["pattern"] == b["pattern"]
        wildcard_static = ((":tenant" in a["pattern"] and "/pros/public/" in b["pattern"])
                           or (":tenant" in b["pattern"] and "/pros/public/" in a["pattern"]))
        return "reject" if same_method and (duplicate or wildcard_static) else "accept"
    if eco == "echo":
        # Limited closed grammar: wildcard/static distinct GET paths, literal
        # branches, per-method differences and default duplicate overwrite.
        return "accept"
    raise ValueError("unknown ecosystem " + eco)

def main():
    if len(sys.argv) != 4:
        raise SystemExit("usage: ast_forecast_gate.py prereg.json ast.json out.json")
    prereg_path, ast_path, out_path = map(Path, sys.argv[1:])
    prereg = json.loads(prereg_path.read_text())
    ast = json.loads(ast_path.read_text())
    assert prereg["contract"] == "P40_MATH_B_P4_PREREG_V1"
    assert ast["protocol"] == "P40_P4_AST_SIGNAL_RECEIPT_V1"
    claims = ast["claims"]
    assert len(claims) == 12 and all(x["Found"] for x in claims)
    actual = {eco: set() for eco in ("chi", "httprouter", "echo")}
    for cl in claims:
        assert cl["Line"] > 0
        assert cl["File"].endswith(".go")
        actual[cl["Source"]].add(cl["Needle"])
    needed = {
        "chi": {"findPattern", "subr.tree == mx.tree", "mALL", "mx.handler != nil"},
        "httprouter": {"r.trees[method]", "conflicts with existing wildcard", "a handle is already registered"},
        "echo": {"allowOverwritingRoute", "addStaticChild", "paramChild", "anyChild",
                 "AllowOverwritingRoute: true"},
    }
    assert all(actual[e] == expected for e, expected in needed.items())
    seen = set()
    output = []
    for case in prereg["cases"]:
        id_ = case["id"]
        assert id_ not in seen
        seen.add(id_)
        assert len(case["edits"]) == 2
        for edit in case["edits"]:
            assert set(edit) == {"method", "pattern", "probe", "response"}
            assert edit["pattern"].startswith("/pros/")
            assert edit["method"] in {"GET", "POST"}
        predicted = forecast(case)
        if case["forecast"] != predicted:
            raise AssertionError(f"FORECAST DRIFT {id_}: locked {case['forecast']} predicted {predicted}")
        output.append({"id": id_, "ecosystem": case["ecosystem"], "locked": predicted})
    assert len(seen) == 16
    receipt = {
        "protocol": "P40_P4_LOCKED_FORECAST_GATE_V1",
        "prereg_sha256": hashlib.sha256(prereg_path.read_bytes()).hexdigest(),
        "ast_sha256": hashlib.sha256(ast_path.read_bytes()).hexdigest(),
        "counts": {"total": len(output), "accept": sum(x["locked"] == "accept" for x in output),
                   "reject": sum(x["locked"] == "reject" for x in output)},
        "cases": output,
        "novelty_limit": "AST signatures certify narrow source anchors. Manually stated bounded rules are not derived solely from AST and not a full correctness proof.",
    }
    out_path.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print("P40_P4_PREREG_AST_ANCHORED_FORECASTS_LOCKED", receipt["counts"])
if __name__ == "__main__":
    main()
