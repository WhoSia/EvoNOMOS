#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

POLICIES = ("DIRECT", "INVERT")
ROUTES = ("node22", "node24")


def pareto(d):
    if all(x == 0 for x in d):
        return "EXACT_TIE"
    if all(x <= 0 for x in d) and any(x < 0 for x in d):
        return "PARETO_I"
    if all(x >= 0 for x in d) and any(x > 0 for x in d):
        return "PARETO_D"
    if any(x < 0 for x in d) and any(x > 0 for x in d):
        return "TRADEOFF"
    return "HOLD"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    root = Path(args.root)
    records = []
    for p in root.rglob("result.json"):
        records.append(json.loads(p.read_text()))

    result = {
        "stage": "DIP-70-WC1",
        "expected_cells": 4,
        "observed_cells": len(records),
        "authority": "DIRECT_WORLD_CONTACT_IF_ALL_FOUR_ADMISSIBLE",
        "status": "HOLD",
        "route_pairs": {},
        "transport_invariance": "UNRESOLVED",
        "next": "MANDATORY_PI_RECOURT",
    }
    if len(records) != 4:
        result["hold_reason"] = "MISSING_CELL_ARTIFACT"
    else:
        by = {(r["policy"], r["route"]): r for r in records}
        missing = [(p, q) for p in POLICIES for q in ROUTES if (p, q) not in by]
        if missing:
            result["hold_reason"] = "CELL_IDENTITY_MISMATCH"
            result["missing"] = missing
        else:
            result["cells"] = {
                f"{p}-{q}": {
                    "status": by[(p, q)].get("status"),
                    "first_failure_stage": by[(p, q)].get("first_failure_stage"),
                    "V": by[(p, q)].get("V"),
                    "node_version": by[(p, q)].get("node_version"),
                    "initial_production_hash": by[(p, q)].get("initial_production_hash"),
                    "followup_production_hash": by[(p, q)].get("followup_production_hash"),
                }
                for p in POLICIES for q in ROUTES
            }
            # Route is allowed to execute/evaluate only; treatment bytes must be identical.
            hash_drift = []
            for p in POLICIES:
                a, b = by[(p, "node22")], by[(p, "node24")]
                for field in ("initial_production_hash", "followup_production_hash"):
                    if a.get(field) != b.get(field):
                        hash_drift.append({"policy": p, "field": field, "node22": a.get(field), "node24": b.get(field)})
            if hash_drift:
                result["hold_reason"] = "ROUTE_CHANGED_TREATMENT_BYTES"
                result["hash_drift"] = hash_drift
            elif any(by[(p, q)].get("status") != "PASS" for p in POLICIES for q in ROUTES):
                result["hold_reason"] = "AT_LEAST_ONE_REQUIRED_CELL_HOLD"
            else:
                for q in ROUTES:
                    vi = by[("INVERT", q)]["V"]
                    vd = by[("DIRECT", q)]["V"]
                    d = [i - d0 for i, d0 in zip(vi, vd)]
                    result["route_pairs"][q] = {
                        "V_INVERT": vi,
                        "V_DIRECT": vd,
                        "d": d,
                        "signature": pareto(d),
                    }
                same_policy_vectors = all(
                    by[(p, "node22")]["V"] == by[(p, "node24")]["V"] for p in POLICIES
                )
                same_signature = result["route_pairs"]["node22"]["signature"] == result["route_pairs"]["node24"]["signature"]
                if same_policy_vectors and same_signature:
                    result["transport_invariance"] = "TRANSPORT_INVARIANT_LOCAL"
                    result["status"] = "PASS"
                    result["signature"] = result["route_pairs"]["node22"]["signature"]
                else:
                    result["hold_reason"] = "ROUTE_OUTCOME_DISAGREEMENT"
                    result["transport_invariance"] = "FALSIFIED_OR_UNRESOLVED"

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print("EVONOMOS_DIP70_WC1_AGGREGATE", json.dumps({
        "status": result.get("status"),
        "hold_reason": result.get("hold_reason"),
        "transport_invariance": result.get("transport_invariance"),
        "signature": result.get("signature"),
        "route_pairs": result.get("route_pairs"),
    }, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
