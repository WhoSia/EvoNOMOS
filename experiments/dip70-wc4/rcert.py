#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

EXPECTED_BASE = "57fc8f74366170b55ec5473d764336c75a08f169"
TARGET = Path("scripts/video_intel.py")
HELPER = Path("scripts/index_update_policy.py")
POLICIES = ("DIRECT", "INVERT")
PHASES = (0, 1)


def run(cmd: list[str], *, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, check=check, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def aggregate_hash(items: dict[str, str]) -> str:
    h = hashlib.sha256()
    for key in sorted(items):
        h.update(key.encode())
        h.update(b"\0")
        h.update(items[key].encode())
        h.update(b"\n")
    return h.hexdigest()


def changed_paths(work: Path) -> list[str]:
    out = run(["git", "status", "--porcelain=v1", "--untracked-files=all"], cwd=work).stdout
    paths: list[str] = []
    for line in out.splitlines():
        if not line.strip():
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path)
    return sorted(paths)


def production_paths(policy: str) -> list[str]:
    return [str(TARGET)] if policy == "DIRECT" else [str(TARGET), str(HELPER)]


def overlay_snapshot(base: Path, snapshot: Path, work: Path) -> None:
    shutil.copytree(base, work, symlinks=True)
    for src in snapshot.rglob("*"):
        if not src.is_file():
            continue
        rel = src.relative_to(snapshot)
        dst = work / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def validate_snapshot(work: Path, policy: str, phase: int) -> dict:
    expected = sorted(production_paths(policy))
    observed = changed_paths(work)
    if observed != expected:
        raise RuntimeError(f"RCERT_HOLD:SCOPE:{policy}:phase{phase}:expected={expected}:observed={observed}")

    files = [work / p for p in expected]
    run([sys.executable, "-m", "py_compile", *[str(p) for p in files]], cwd=work)
    run(["ruff", "check", *expected], cwd=work)
    run(["git", "diff", "--check"], cwd=work)

    main = (work / TARGET).read_text(encoding="utf-8")
    helper = (work / HELPER).read_text(encoding="utf-8") if (work / HELPER).exists() else ""

    if policy == "DIRECT":
        if (work / HELPER).exists() or "IndexUpdatePolicy" in main or "index_update.commit" in main:
            raise RuntimeError(f"RCERT_HOLD:TOPOLOGY:DIRECT:phase{phase}")
        if "# DIRECT: scoped/full mutation policy remains inline in build_search_index." not in main:
            raise RuntimeError(f"RCERT_HOLD:TOPOLOGY:DIRECT_MARKER:phase{phase}")
    else:
        required = ("from index_update_policy import IndexUpdatePolicy", "index_update.pre_embed()", "index_update.commit(all_records)")
        if not (work / HELPER).exists() or any(marker not in main for marker in required):
            raise RuntimeError(f"RCERT_HOLD:TOPOLOGY:INVERT:phase{phase}")
        if "class IndexUpdatePolicy:" not in helper:
            raise RuntimeError(f"RCERT_HOLD:TOPOLOGY:INVERT_PROVIDER:phase{phase}")

    if phase == 0:
        combined = main + "\n" + helper
        forbidden = ["Scoped index requires an existing full index"]
        forbidden.append("_lancedb_quote_literal" if policy == "DIRECT" else "quote_lancedb_literal")
        if any(marker in combined for marker in forbidden):
            raise RuntimeError(f"RCERT_HOLD:PHASE_LEAK:{policy}:phase0")
    else:
        combined = main + "\n" + helper
        if "Scoped index requires an existing full index" not in combined:
            raise RuntimeError(f"RCERT_HOLD:PHASE1_MISSING_TABLE_GUARD:{policy}")
        quote_marker = "_lancedb_quote_literal" if policy == "DIRECT" else "quote_lancedb_literal"
        if quote_marker not in combined:
            raise RuntimeError(f"RCERT_HOLD:PHASE1_QUOTE_RULE:{policy}")
        if policy == "DIRECT":
            if "where_clauses.append(f\"channel = {_lancedb_quote_literal(channel_filter)}\")" not in main:
                raise RuntimeError("RCERT_HOLD:DIRECT_HYBRID_QUOTE")
        else:
            if "where_clauses.append(f\"channel = {quote_lancedb_literal(channel_filter)}\")" not in main:
                raise RuntimeError("RCERT_HOLD:INVERT_HYBRID_QUOTE")

    hashes = {p: sha256(work / p) for p in expected}
    return {"changed_production_paths": observed, "file_sha256": hashes, "treatment_sha256": aggregate_hash(hashes)}


def numstat_pair(old: Path | None, new: Path | None) -> tuple[int, int]:
    old_arg = str(old) if old is not None and old.exists() else os.devnull
    new_arg = str(new) if new is not None and new.exists() else os.devnull
    proc = run(["git", "diff", "--no-index", "--numstat", "--", old_arg, new_arg], check=False)
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"RCERT_HOLD:NUMSTAT:{proc.stdout}")
    adds = dels = 0
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        a, d, *_ = line.split("\t")
        if a == "-" or d == "-":
            raise RuntimeError("RCERT_HOLD:BINARY_PRODUCTION_FILE")
        adds += int(a)
        dels += int(d)
    return adds, dels


def diff_vector(base: Path, p0: Path, p1: Path, policy: str) -> dict:
    all_paths = sorted(set(production_paths(policy)))
    initial_touched: list[str] = []
    follow_touched: list[str] = []
    c0 = c1 = 0
    detail: dict[str, dict] = {}
    for rel in all_paths:
        b = base / rel
        a = p0 / rel
        z = p1 / rel
        a0, d0 = numstat_pair(b if b.exists() else None, a if a.exists() else None)
        a1, d1 = numstat_pair(a if a.exists() else None, z if z.exists() else None)
        if a0 + d0:
            initial_touched.append(rel)
            c0 += a0 + d0
        if a1 + d1:
            follow_touched.append(rel)
            c1 += a1 + d1
        detail[rel] = {"initial": {"add": a0, "del": d0}, "followup": {"add": a1, "del": d1}}

    provider_locus = {str(HELPER)} if policy == "INVERT" else set()
    preexisting_consumers = {str(TARGET)}
    p1_consumers = sorted((set(follow_touched) & preexisting_consumers) - provider_locus)
    vector = [len(initial_touched), c0, len(follow_touched), c1, len(p1_consumers)]
    return {
        "V": vector,
        "initial_paths": initial_touched,
        "followup_paths": follow_touched,
        "p1_consumer_loci": p1_consumers,
        "numstat": detail,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-dir", required=True)
    ap.add_argument("--materializer", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    base = Path(args.base_dir).resolve()
    materializer = Path(args.materializer).resolve()
    out = Path(args.out).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    head = run(["git", "rev-parse", "HEAD"], cwd=base).stdout.strip()
    if head != EXPECTED_BASE:
        raise RuntimeError(f"RCERT_HOLD:BASE_IDENTITY:{head}")
    if changed_paths(base):
        raise RuntimeError("RCERT_HOLD:BASE_NOT_CLEAN")

    treatments = out / "treatments"
    run([sys.executable, str(materializer), "--base-dir", str(base), "--out", str(treatments)])

    receipts: dict[str, dict] = {}
    work_root = out / "work"
    for policy in POLICIES:
        receipts[policy] = {}
        for phase in PHASES:
            snap = treatments / policy / f"phase{phase}"
            work = work_root / policy / f"phase{phase}"
            overlay_snapshot(base, snap, work)
            receipts[policy][f"phase{phase}"] = validate_snapshot(work, policy, phase)
        receipts[policy]["measurement"] = diff_vector(
            base,
            treatments / policy / "phase0",
            treatments / policy / "phase1",
            policy,
        )

    manifest = {
        "status": "RCERT_PASS_PREOUTCOME",
        "scientific_oracle_opened": False,
        "exact_base": head,
        "cert_python": sys.version.split()[0],
        "policies": receipts,
    }
    seal_payload = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    manifest["rcert_manifest_sha256"] = hashlib.sha256(seal_payload).hexdigest()
    (out / "RCERT.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    shutil.rmtree(work_root)
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "RCERT_HOLD", "scientific_oracle_opened": False, "error": str(exc)}, sort_keys=True))
        raise
