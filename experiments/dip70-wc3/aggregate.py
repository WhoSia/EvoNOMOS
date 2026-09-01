#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def signature(d: list[int]) -> str:
    if all(x == 0 for x in d):
        return "EXACT_TIE"
    if all(x <= 0 for x in d) and any(x < 0 for x in d):
        return "PARETO_INVERT"
    if all(x >= 0 for x in d) and any(x > 0 for x in d):
        return "PARETO_DIRECT"
    return "TRADEOFF"


def stable_projection(r: dict) -> dict:
    return {
        "status": r.get("status"),
        "exact_base": r.get("exact_base"),
        "lancedb": r.get("lancedb"),
        "baseline": r.get("baseline"),
        "phases": r.get("phases"),
        "V": r.get("V"),
        "measurement": r.get("measurement"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--receipts-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    root = Path(args.receipts_dir)
    out = Path(args.out)
    receipts = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(root.glob("science-*.json"))]
    result: dict = {"status": "AGGREGATE_HOLD", "receipt_count": len(receipts)}
    if len(receipts) != 4:
        result["error"] = "EXPECTED_FOUR_SCIENCE_RECEIPTS"
    else:
        keyed = {(r["policy"], r["python"].rsplit(".", 1)[0]): r for r in receipts}
        expected_keys = {("DIRECT", "3.12"), ("DIRECT", "3.13"), ("INVERT", "3.12"), ("INVERT", "3.13")}
        if set(keyed) != expected_keys:
            result["error"] = f"SCIENCE_KEY_MISMATCH:{sorted(keyed)}"
        elif any(r.get("status") != "SCIENCE_PASS" for r in receipts):
            result["error"] = "AT_LEAST_ONE_SCIENCE_HOLD"
            result["holds"] = [r for r in receipts if r.get("status") != "SCIENCE_PASS"]
        else:
            route_checks = {}
            for policy in ("DIRECT", "INVERT"):
                a = keyed[(policy, "3.12")]
                b = keyed[(policy, "3.13")]
                pa = stable_projection(a)
                pb = stable_projection(b)
                same = pa == pb
                route_checks[policy] = {
                    "same_scientific_projection": same,
                    "python_3_12_receipt": a["receipt_sha256"],
                    "python_3_13_receipt": b["receipt_sha256"],
                    "V": a["V"],
                    "phase0_treatment_sha256": a["phases"]["phase0"]["treatment_sha256"],
                    "phase1_treatment_sha256": a["phases"]["phase1"]["treatment_sha256"],
                }
            if not all(v["same_scientific_projection"] for v in route_checks.values()):
                result["error"] = "ROUTE_PROJECTION_DIFFERENCE"
                result["route_checks"] = route_checks
            else:
                vd = route_checks["DIRECT"]["V"]
                vi = route_checks["INVERT"]["V"]
                d = [i - x for i, x in zip(vi, vd, strict=True)]
                sig = signature(d)
                result = {
                    "status": "AGGREGATE_PASS",
                    "transport_adjudication": "TRANSPORT_INVARIANT_LOCAL",
                    "route_family": "CPython 3.12 vs 3.13 / Ubuntu 24.04 / LanceDB exact workflow pin",
                    "DIRECT_V": vd,
                    "INVERT_V": vi,
                    "d_INVERT_minus_DIRECT": d,
                    "pareto_signature": sig,
                    "route_checks": route_checks,
                    "scientific_receipts": [r["receipt_sha256"] for r in receipts],
                }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["aggregate_sha256"] = hashlib.sha256(payload).hexdigest()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
