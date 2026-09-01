#!/usr/bin/env python3
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

REPO_URL = "https://github.com/Plimmerton-Labs/homebridge-ups-monitor.git"
BASE_SHA = "000e26da0b4c7c699e472207df447964960b8b11"
DASH = "lib/dashboardServer.js"
UI = "homebridge-ui/server.js"
STORE = "lib/telemetryStore.js"
PRODUCTION = (DASH, UI, STORE)

DASH_OLD = """      const points = telemetryStore.readHistory(this._storagePath, upsName);\n      return points.length ? points[points.length - 1] : null;\n"""
UI_OLD = """      const points = telemetryStore.readHistory(dataDir, upsName);\n      return points.length ? points[points.length - 1] : null;\n"""

DIRECT_SCAN_DASH = """      const points = telemetryStore.readHistory(this._storagePath, upsName);\n      for (let i = points.length - 1; i >= 0; i -= 1) {\n        const point = points[i];\n        if (point && [point.inV, point.outV, point.bat, point.load, point.runtime]\n          .some(value => value !== null && value !== undefined)) {\n          return point;\n        }\n      }\n      return null;\n"""
DIRECT_SCAN_UI = """      const points = telemetryStore.readHistory(dataDir, upsName);\n      for (let i = points.length - 1; i >= 0; i -= 1) {\n        const point = points[i];\n        if (point && [point.inV, point.outV, point.bat, point.load, point.runtime]\n          .some(value => value !== null && value !== undefined)) {\n          return point;\n        }\n      }\n      return null;\n"""
INVERT_DASH = """      const points = telemetryStore.readHistory(this._storagePath, upsName);\n      return telemetryStore.findLastUsableTelemetryPoint(points);\n"""
INVERT_UI = """      const points = telemetryStore.readHistory(dataDir, upsName);\n      return telemetryStore.findLastUsableTelemetryPoint(points);\n"""

READ_HISTORY_BLOCK = """function readHistory(dataDir, upsName) {\n  const histFile = path.join(dataDir, `ups-history-${upsName}.json`);\n  const buf      = new RingBuffer(histFile, READER_CAPACITY, { adopt: true });\n  return buf.read();\n}\n"""
HELPER = """

/**
 * Select the newest telemetry point containing at least one meaningful value.
 * Timestamp-only or all-null legacy samples are not usable; numeric zero is.
 * @param {Array<object>} points oldest -> newest
 * @returns {object|null}
 */
function findLastUsableTelemetryPoint(points = []) {
  if (!Array.isArray(points)) return null;
  for (let i = points.length - 1; i >= 0; i -= 1) {
    const point = points[i];
    if (point && [point.inV, point.outV, point.bat, point.load, point.runtime]
      .some(value => value !== null && value !== undefined)) {
      return point;
    }
  }
  return null;
}
"""
EXPORT_OLD = """  readHistory,\n  buildHistoryCsv,\n"""
EXPORT_NEW = """  readHistory,\n  findLastUsableTelemetryPoint,\n  buildHistoryCsv,\n"""

EXPECTED = {
    ("DIRECT", "phase0"): {DASH},
    ("DIRECT", "phase1"): {DASH, UI},
    ("INVERT", "phase0"): {DASH, STORE},
    ("INVERT", "phase1"): {DASH, UI, STORE},
}


def run(cmd, cwd=None, check=True):
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, check=check)


def replace_once(path: Path, old: str, new: str):
    text = path.read_text()
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected exactly one replacement in {path}: found {count}")
    path.write_text(text.replace(old, new, 1))


def add_provider(root: Path):
    path = root / STORE
    text = path.read_text()
    if text.count(READ_HISTORY_BLOCK) != 1:
        raise RuntimeError("readHistory anchor not unique")
    text = text.replace(READ_HISTORY_BLOCK, READ_HISTORY_BLOCK + HELPER, 1)
    if text.count(EXPORT_OLD) != 1:
        raise RuntimeError("telemetryStore export anchor not unique")
    text = text.replace(EXPORT_OLD, EXPORT_NEW, 1)
    path.write_text(text)


def materialize(root: Path, policy: str, phase: str):
    if policy == "DIRECT":
        replace_once(root / DASH, DASH_OLD, DIRECT_SCAN_DASH)
        if phase == "phase1":
            replace_once(root / UI, UI_OLD, DIRECT_SCAN_UI)
    elif policy == "INVERT":
        add_provider(root)
        replace_once(root / DASH, DASH_OLD, INVERT_DASH)
        if phase == "phase1":
            replace_once(root / UI, UI_OLD, INVERT_UI)
    else:
        raise ValueError(policy)


def changed_paths(root: Path):
    out = run(["git", "diff", "--name-only", BASE_SHA, "--"], cwd=root).stdout
    return {line.strip() for line in out.splitlines() if line.strip()}


def certify_state(root: Path, policy: str, phase: str):
    changed = changed_paths(root)
    expected = EXPECTED[(policy, phase)]
    if changed != expected:
        raise RuntimeError(f"scope mismatch {policy}/{phase}: {sorted(changed)} != {sorted(expected)}")
    run(["git", "diff", "--check", BASE_SHA, "--"], cwd=root)
    for rel in sorted(changed):
        if not rel.endswith(".js"):
            raise RuntimeError(f"unexpected non-JS treatment path: {rel}")
        run(["node", "--check", rel], cwd=root)

    dash = (root / DASH).read_text()
    ui = (root / UI).read_text()
    store = (root / STORE).read_text()

    if policy == "DIRECT":
        if "findLastUsableTelemetryPoint" in store or "findLastUsableTelemetryPoint" in dash or "findLastUsableTelemetryPoint" in ui:
            raise RuntimeError("DIRECT introduced/consumed shared semantic provider")
        if DIRECT_SCAN_DASH.strip() not in dash:
            raise RuntimeError("DIRECT standalone inline scan missing")
        if phase == "phase0":
            if UI_OLD.strip() not in ui:
                raise RuntimeError("DIRECT phase0 opened frozen UI consumer early")
        else:
            if DIRECT_SCAN_UI.strip() not in ui:
                raise RuntimeError("DIRECT phase1 UI inline scan missing")
    else:
        if store.count("function findLastUsableTelemetryPoint") != 1:
            raise RuntimeError("INVERT provider function count is not one")
        if store.count("  findLastUsableTelemetryPoint,") != 1:
            raise RuntimeError("INVERT provider export count is not one")
        if INVERT_DASH.strip() not in dash:
            raise RuntimeError("INVERT standalone consumer is not provider-bound")
        if DIRECT_SCAN_DASH.strip() in dash or DIRECT_SCAN_UI.strip() in ui:
            raise RuntimeError("INVERT duplicated inline scan in a transport consumer")
        if phase == "phase0":
            if UI_OLD.strip() not in ui:
                raise RuntimeError("INVERT phase0 opened frozen UI consumer early")
        else:
            if INVERT_UI.strip() not in ui:
                raise RuntimeError("INVERT phase1 UI consumer is not provider-bound")
    return changed


def sha256_bytes(data: bytes):
    return hashlib.sha256(data).hexdigest()


def seal_state(root: Path, out: Path, policy: str, phase: str, changed):
    state_out = out / policy / phase
    files_out = state_out / "files"
    files_out.mkdir(parents=True, exist_ok=True)
    file_hashes = {}
    combined = hashlib.sha256()
    for rel in sorted(changed):
        data = (root / rel).read_bytes()
        dest = files_out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        digest = sha256_bytes(data)
        file_hashes[rel] = digest
        combined.update(rel.encode("utf-8"))
        combined.update(b"\0")
        combined.update(data)
        combined.update(b"\0")
    manifest = {
        "policy": policy,
        "phase": phase,
        "base_sha": BASE_SHA,
        "changed_paths": sorted(changed),
        "file_sha256": file_hashes,
        "production_hash": combined.hexdigest(),
        "sealed_after_r_cert": True,
    }
    (state_out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


def compare_phase_order(states, policy):
    p0, p1 = states[(policy, "phase0")], states[(policy, "phase1")]
    changed = set()
    for rel in PRODUCTION:
        if (p0 / rel).read_bytes() != (p1 / rel).read_bytes():
            changed.add(rel)
    if changed != {UI}:
        raise RuntimeError(f"phase-order mismatch {policy}: phase1 delta={sorted(changed)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    receipt = {
        "stage": "DIP-70-WC2",
        "authority": "CI-0.11R-016",
        "base_sha": BASE_SHA,
        "status": "HOLD",
        "scientific_oracle_opened": False,
        "treatments": {},
    }
    try:
        node_version = run(["node", "--version"]).stdout.strip()
        if not node_version.startswith("v22."):
            raise RuntimeError(f"R-CERT requires Node22, observed {node_version}")
        with tempfile.TemporaryDirectory(prefix="evonomos-wc2-") as td:
            td = Path(td)
            base = td / "base"
            run(["git", "clone", "--quiet", REPO_URL, str(base)])
            run(["git", "checkout", "--quiet", BASE_SHA], cwd=base)
            observed = run(["git", "rev-parse", "HEAD"], cwd=base).stdout.strip()
            if observed != BASE_SHA:
                raise RuntimeError(f"base identity mismatch: {observed}")

            states = {}
            changed_sets = {}
            for policy in ("DIRECT", "INVERT"):
                for phase in ("phase0", "phase1"):
                    root = td / f"{policy.lower()}-{phase}"
                    run(["git", "worktree", "add", "--quiet", "--detach", str(root), BASE_SHA], cwd=base)
                    materialize(root, policy, phase)
                    changed_sets[(policy, phase)] = certify_state(root, policy, phase)
                    states[(policy, phase)] = root

            for policy in ("DIRECT", "INVERT"):
                compare_phase_order(states, policy)

            for policy in ("DIRECT", "INVERT"):
                receipt["treatments"][policy] = {}
                for phase in ("phase0", "phase1"):
                    manifest = seal_state(states[(policy, phase)], out, policy, phase, changed_sets[(policy, phase)])
                    receipt["treatments"][policy][phase] = {
                        "changed_paths": manifest["changed_paths"],
                        "production_hash": manifest["production_hash"],
                    }
            receipt["status"] = "PASS"
            receipt["r_cert_node"] = node_version
            receipt["checks"] = [
                "exact_base",
                "allowed_paths",
                "node_check_all_changed_production_js",
                "git_diff_check",
                "policy_topology",
                "phase_order",
                "hash_seal_after_certification",
            ]
    except Exception as exc:
        receipt["hold_reason"] = type(exc).__name__
        receipt["hold_detail"] = str(exc)
    (out / "r_cert.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("EVONOMOS_DIP70_WC2_RCERT", json.dumps({
        "status": receipt["status"],
        "hold_reason": receipt.get("hold_reason"),
        "scientific_oracle_opened": receipt["scientific_oracle_opened"],
    }, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()
