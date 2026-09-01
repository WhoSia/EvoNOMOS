#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

POLICIES = ("DIRECT", "INVERT")
ROUTES = ("node18", "node24")


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
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    rcerts = [json.loads(p.read_text()) for p in root.rglob("r_cert.json")]
    records = [json.loads(p.read_text()) for p in root.rglob("result.json")]
    result = {
        "stage": "DIP-70-WC2",
        "authority": "DIRECT_WORLD_CONTACT_ONLY_IF_RCERT_AND_ALL_FOUR_SCIENCE_CELLS_PASS",
        "status": "HOLD",
        "expected_cells": 4,
        "observed_cells": len(records),
        "transport_invariance": "UNRESOLVED",
        "route_pairs": {},
        "next": "MANDATORY_PI_RECOURT",
    }

    if len(rcerts) != 1:
        result["hold_reason"] = "RCERT_RECEIPT_COUNT_MISMATCH"
        result["observed_rcert_receipts"] = len(rcerts)
    elif rcerts[0].get("status") != "PASS":
        result["hold_reason"] = "RCERT_HOLD"
        result["r_cert"] = rcerts[0]
    elif len(records) != 4:
        result["hold_reason"] = "MISSING_REQUIRED_SCIENCE_CELL"
    else:
        by = {(r.get("policy"), r.get("route")): r for r in records}
        expected = {(p, q) for p in POLICIES for q in ROUTES}
        if set(by) != expected or len(by) != 4:
            result["hold_reason"] = "CELL_IDENTITY_MISMATCH"
        else:
            result["cells"] = {
                f"{p}-{q}": {
                    "status": by[(p, q)].get("status"),
                    "first_failure_stage": by[(p, q)].get("first_failure_stage"),
                    "V": by[(p, q)].get("V"),
                    "node_version": by[(p, q)].get("node_version"),
                    "phase0_production_hash": by[(p, q)].get("phase0_production_hash"),
                    "phase1_production_hash": by[(p, q)].get("phase1_production_hash"),
                    "base_oracle": by[(p, q)].get("base_oracle"),
                    "phase0_oracle": by[(p, q)].get("phase0_oracle"),
                    "phase1_oracle": by[(p, q)].get("phase1_oracle"),
                }
                for p in POLICIES for q in ROUTES
            }

            hash_drift = []
            for p in POLICIES:
                a, b = by[(p, "node18")], by[(p, "node24")]
                for field in ("phase0_production_hash", "phase1_production_hash"):
                    if a.get(field) != b.get(field):
                        hash_drift.append({
                            "policy": p,
                            "field": field,
                            "node18": a.get(field),
                            "node24": b.get(field),
                        })
            if hash_drift:
                result["hold_reason"] = "ROUTE_CHANGED_TREATMENT_BYTES"
                result["hash_drift"] = hash_drift
            elif any(by[(p, q)].get("status") != "PASS" for p in POLICIES for q in ROUTES):
                result["hold_reason"] = "AT_LEAST_ONE_REQUIRED_SCIENCE_CELL_HOLD"
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
                    by[(p, "node18")]["V"] == by[(p, "node24")]["V"]
                    for p in POLICIES
                )
                same_signature = (
                    result["route_pairs"]["node18"]["signature"]
                    == result["route_pairs"]["node24"]["signature"]
                )
                if same_policy_vectors and same_signature:
                    result["status"] = "PASS"
                    result["transport_invariance"] = "TRANSPORT_INVARIANT_LOCAL"
                    result["signature"] = result["route_pairs"]["node18"]["signature"]
                else:
                    result["hold_reason"] = "ROUTE_OUTCOME_DISAGREEMENT"
                    result["transport_invariance"] = "FALSIFIED_OR_UNRESOLVED"

    out.write_text(json.dumps(result, indent=2) + "\n")
    print("EVONOMOS_DIP70_WC2_AGGREGATE", json.dumps({
        "status": result.get("status"),
        "hold_reason": result.get("hold_reason"),
        "transport_invariance": result.get("transport_invariance"),
        "signature": result.get("signature"),
        "route_pairs": result.get("route_pairs"),
    }, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
