#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

REPO_URL = "https://github.com/Plimmerton-Labs/homebridge-ups-monitor.git"
BASE_SHA = "000e26da0b4c7c699e472207df447964960b8b11"
UI = "homebridge-ui/server.js"
CONSUMERS = {"lib/dashboardServer.js", UI}


def write_log(path: Path, cp):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"$ {' '.join(cp.args if isinstance(cp.args, list) else [str(cp.args)])}\n"
        f"returncode={cp.returncode}\n\nSTDOUT\n{cp.stdout or ''}\n\nSTDERR\n{cp.stderr or ''}\n"
    )


def run(cmd, cwd, log_path: Path, env=None):
    merged = os.environ.copy()
    if env:
        merged.update(env)
    cp = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, env=merged)
    write_log(log_path, cp)
    if cp.returncode != 0:
        raise RuntimeError(f"command failed ({cp.returncode}): {' '.join(cmd)}")
    return cp


def sha256(data: bytes):
    return hashlib.sha256(data).hexdigest()


def load_manifest(sealed: Path, policy: str, phase: str):
    return json.loads((sealed / policy / phase / "manifest.json").read_text())


def verify_and_apply(repo: Path, sealed: Path, policy: str, phase: str):
    manifest = load_manifest(sealed, policy, phase)
    if manifest["base_sha"] != BASE_SHA or manifest["policy"] != policy or manifest["phase"] != phase:
        raise RuntimeError("sealed manifest identity mismatch")
    combined = hashlib.sha256()
    for rel in manifest["changed_paths"]:
        src = sealed / policy / phase / "files" / rel
        data = src.read_bytes()
        if sha256(data) != manifest["file_sha256"][rel]:
            raise RuntimeError(f"sealed file hash mismatch before apply: {rel}")
        combined.update(rel.encode("utf-8"))
        combined.update(b"\0")
        combined.update(data)
        combined.update(b"\0")
        dest = repo / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    if combined.hexdigest() != manifest["production_hash"]:
        raise RuntimeError("sealed aggregate treatment hash mismatch")
    for rel in manifest["changed_paths"]:
        if sha256((repo / rel).read_bytes()) != manifest["file_sha256"][rel]:
            raise RuntimeError(f"route changed treatment bytes after apply: {rel}")
    return manifest


def production_stats(repo: Path):
    cp = subprocess.run(
        ["git", "diff", "--numstat", "HEAD", "--", "lib", UI],
        cwd=repo, text=True, capture_output=True, check=True,
    )
    files = []
    churn = 0
    for line in cp.stdout.splitlines():
        if not line.strip():
            continue
        add, delete, rel = line.split("\t", 2)
        if rel == UI or (rel.startswith("lib/") and rel.endswith(".js")):
            files.append(rel)
            if add == "-" or delete == "-":
                raise RuntimeError(f"binary production diff not measurable: {rel}")
            churn += int(add) + int(delete)
    return sorted(files), churn


def commit_phase0(repo: Path, paths):
    subprocess.run(["git", "config", "user.name", "EvoNOMOS WC2"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "evonomos-wc2@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "add", "--", *paths], cwd=repo, check=True)
    subprocess.run(["git", "commit", "--quiet", "-m", "evonomos wc2 sealed phase0"], cwd=repo, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--policy", choices=["DIRECT", "INVERT"], required=True)
    ap.add_argument("--route", choices=["node18", "node24"], required=True)
    ap.add_argument("--sealed", required=True)
    ap.add_argument("--evaluator", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    log_dir = out.parent / "logs"
    sealed = Path(args.sealed).resolve()
    evaluator = Path(args.evaluator).resolve()
    result = {
        "stage": "DIP-70-WC2",
        "policy": args.policy,
        "route": args.route,
        "base_sha": BASE_SHA,
        "status": "HOLD",
        "first_failure_stage": None,
        "V": None,
    }

    stage = "ROUTE_IDENTITY"
    try:
        node_version = subprocess.run(["node", "--version"], text=True, capture_output=True, check=True).stdout.strip()
        expected_major = args.route.removeprefix("node")
        if not node_version.startswith(f"v{expected_major}."):
            raise RuntimeError(f"route mismatch: expected Node{expected_major}, observed {node_version}")
        result["node_version"] = node_version

        r_cert = json.loads((sealed / "r_cert.json").read_text())
        if r_cert.get("status") != "PASS" or r_cert.get("scientific_oracle_opened") is not False:
            raise RuntimeError("science opened without clean R-CERT PASS")
        result["r_cert_status"] = "PASS"

        with tempfile.TemporaryDirectory(prefix="evonomos-wc2-science-") as td:
            repo = Path(td) / "repo"
            stage = "BASE_ACQUISITION"
            run(["git", "clone", "--quiet", REPO_URL, str(repo)], Path(td), log_dir / "00-clone.log")
            run(["git", "checkout", "--quiet", BASE_SHA], repo, log_dir / "01-checkout.log")
            observed = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, text=True, capture_output=True, check=True).stdout.strip()
            if observed != BASE_SHA:
                raise RuntimeError(f"base identity mismatch: {observed}")

            stage = "BASE_ORACLE"
            run(["npm", "ci", "--no-audit", "--no-fund"], repo, log_dir / "02-npm-ci.log")
            run(["npm", "run", "lint"], repo, log_dir / "03-base-lint.log")
            run(["npm", "test", "--", "--runInBand"], repo, log_dir / "04-base-test.log")
            result["base_oracle"] = "PASS"

            stage = "PHASE0_TREATMENT_HASH"
            m0 = verify_and_apply(repo, sealed, args.policy, "phase0")
            result["phase0_production_hash"] = m0["production_hash"]
            evaluator_dest = repo / "test" / "evonomos-wc2.test.js"
            evaluator_dest.write_bytes(evaluator.read_bytes())
            result["evaluator_sha256"] = sha256(evaluator.read_bytes())

            stage = "PHASE0_ORACLE"
            run(
                ["npx", "--no-install", "jest", "test/evonomos-wc2.test.js", "--runInBand"],
                repo, log_dir / "05-phase0-focused.log", env={"EVONOMOS_WC2_PHASE": "phase0"},
            )
            run(["npm", "run", "lint"], repo, log_dir / "06-phase0-lint.log", env={"EVONOMOS_WC2_PHASE": "phase0"})
            run(["npm", "test", "--", "--runInBand"], repo, log_dir / "07-phase0-test.log", env={"EVONOMOS_WC2_PHASE": "phase0"})
            f0_paths, c0 = production_stats(repo)
            if set(f0_paths) != set(m0["changed_paths"]):
                raise RuntimeError(f"phase0 measured path mismatch: {f0_paths} vs {m0['changed_paths']}")
            f0 = len(f0_paths)
            result["phase0_oracle"] = "PASS"
            commit_phase0(repo, m0["changed_paths"])

            stage = "PHASE1_TREATMENT_HASH"
            m1 = verify_and_apply(repo, sealed, args.policy, "phase1")
            result["phase1_production_hash"] = m1["production_hash"]

            stage = "PHASE1_ORACLE"
            run(
                ["npx", "--no-install", "jest", "test/evonomos-wc2.test.js", "--runInBand"],
                repo, log_dir / "08-phase1-focused.log", env={"EVONOMOS_WC2_PHASE": "phase1"},
            )
            run(["npm", "run", "lint"], repo, log_dir / "09-phase1-lint.log", env={"EVONOMOS_WC2_PHASE": "phase1"})
            run(["npm", "test", "--", "--runInBand"], repo, log_dir / "10-phase1-test.log", env={"EVONOMOS_WC2_PHASE": "phase1"})
            f1_paths, c1 = production_stats(repo)
            expected_delta = sorted(set(m1["changed_paths"]) - set(m0["changed_paths"]))
            if f1_paths != expected_delta:
                raise RuntimeError(f"phase1 measured path mismatch: {f1_paths} vs {expected_delta}")
            f1 = len(f1_paths)
            p1 = len(set(f1_paths) & CONSUMERS)
            result["phase1_oracle"] = "PASS"
            result["phase0_changed_paths"] = f0_paths
            result["phase1_changed_paths"] = f1_paths
            result["V"] = [f0, c0, f1, c1, p1]
            result["status"] = "PASS"
            result["first_failure_stage"] = None
    except Exception as exc:
        result["first_failure_stage"] = stage
        result["hold_reason"] = type(exc).__name__
        result["hold_detail"] = str(exc)

    out.write_text(json.dumps(result, indent=2) + "\n")
    print("EVONOMOS_DIP70_WC2_CELL", json.dumps({
        "policy": result["policy"],
        "route": result["route"],
        "status": result["status"],
        "first_failure_stage": result.get("first_failure_stage"),
        "V": result.get("V"),
    }, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
