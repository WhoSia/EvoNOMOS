#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--bundle", type=Path, required=True)
    ap.add_argument("--commit", required=True)
    ap.add_argument("--tree", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--build", choices=["PASS", "FAIL"], required=True)
    ap.add_argument("--oracle", choices=["PASS", "FAIL"], required=True)
    ap.add_argument("--reconstruction", choices=["PASS", "FAIL"], required=True)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    receipt = {
        "stage": "EvoNOMOS Generation VIII ORIGIN-R1-P10-P2",
        "arm": args.arm,
        "base": manifest["base"],
        "contract_digest": manifest["contract_digest"],
        "arm_commit": args.commit,
        "arm_tree": args.tree,
        "arm_bundle_file": args.bundle.name,
        "arm_bundle_sha256": sha256(args.bundle),
        "common_file_sha256": manifest["common_file_sha256"],
        "changed_paths": manifest["changed_paths"],
        "build": args.build,
        "shared_oracle": args.oracle,
        "reconstruction_verified": args.reconstruction == "PASS",
        "comparative_metrics_opened": False,
        "winner": None,
        "status": (
            "PASS"
            if args.build == args.oracle == args.reconstruction == "PASS"
            else "HOLD"
        ),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("RECEIPT_OK")

if __name__ == "__main__":
    main()
