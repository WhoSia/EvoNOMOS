"""R80 offline exact-Git-blob source-native P35/D8 replay.

Run in a WhoSia/EvoNOMOS checkout:
    python tools/p35-p7/r80_exact_source_replay.py

Replays isolated router packages, not the complete upstream Chi module.
Expected D8 failure in an original arm is evidence, not a D8 success.
"""
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
BASE = Path("tools/p35-p7")
SOURCES = {
    "original_live": ("arms/live/route_headers.go", "ad9a2fbc0a30a39475f746068e74e2d3e6c93999", "after", False),
    "original_snapshot": ("arms/snapshot/route_headers.go", "e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75", "downstream", False),
    "repaired_live": ("d8/live/route_headers.go", "e481e73aa1d82497c25011b6468d7e8749c705f7", "after", True),
    "repaired_snapshot": ("d8/snapshot/route_headers.go", "66e88964508cedc38740913a7c00fbf5b6e6220a", "downstream", True),
}
TESTS = {
    "p35_p7_common_test.go": "81f8123d6e24eb92c1ce9529f170be36191dd1c1",
    "p35_p7_d8_same_requirement_test.go": "ed13ceb8f78ccc923f58ea12584a366cd3080d37",
    "r80_temporal_contract_test.go": "fe9ea93df2a80e6fee2d8ed437b56f062fa6ce17",
}
SUITES = (
    ("D0", "TestP35P7EmptyRouterExactlyOnce|TestP35P7StableHeaderOrderAndFallback|TestP35P7RouteAny"),
    ("D8", "TestP35P7D8IdenticalNewDemand"),
    ("TEMPORAL", "TestR80TemporalAfterConstruction"),
)
FAILURES = (
    "TestP35P7D8IdenticalNewDemand/later-exact-over-earlier-wildcard",
    "TestP35P7D8IdenticalNewDemand/route-any-exact-pattern-matches",
)


def git_blob(source: Path) -> str:
    result = subprocess.run(["git", "hash-object", str(source)], check=True, capture_output=True, text=True)
    return result.stdout.strip()


def verified(path: Path, wanted: str) -> bytes:
    if not path.is_file():
        raise ValueError(f"missing file {path}")
    got = git_blob(path)
    if got != wanted:
        raise ValueError(f"Git blob mismatch {path}: expected {wanted}, found {got}")
    return path.read_bytes()


def run() -> dict:
    go = subprocess.run(["go", "version"], capture_output=True, text=True, check=True).stdout.strip()
    source_bytes = {key: verified(ROOT / BASE / info[0], info[1]) for key, info in SOURCES.items()}
    test_bytes = {name: verified(ROOT / BASE / "tests" / name, sha) for name, sha in TESTS.items()}
    rows = []
    with tempfile.TemporaryDirectory(prefix="evonomos-r80-") as folder:
        for key, (_path, _sha, expected_temporal, repaired) in SOURCES.items():
            mod = Path(folder) / key
            mod.mkdir()
            (mod / "go.mod").write_text(f"module example.org/evonomos-r80-{key}\n\ngo 1.23\n")
            (mod / "route_headers.go").write_bytes(source_bytes[key])
            for name, data in test_bytes.items():
                (mod / name).write_bytes(data)
            for label, pat in SUITES:
                env = dict(os.environ, GOPROXY="off", GOTOOLCHAIN="local", R80_EXPECT=expected_temporal)
                proc = subprocess.run(["go", "test", "-race", "-count=1", "-run", pat, "-v", "./..."],
                                      cwd=mod, env=env, capture_output=True, text=True, timeout=120)
                observed = "PASS" if proc.returncode == 0 else "FAIL"
                expected = "FAIL" if label == "D8" and not repaired else "PASS"
                actual_subfails = tuple(line.split("--- FAIL: ", 1)[-1].split(" (", 1)[0]
                                        for line in proc.stdout.splitlines() if line.startswith("    --- FAIL:"))
                if observed != expected:
                    raise AssertionError(f"unexpected {key} {label}: {observed}, stdout {proc.stdout}, stderr {proc.stderr}")
                if observed == "FAIL" and set(actual_subfails) != set(FAILURES):
                    raise AssertionError(f"unexpected D8 failure signature: {actual_subfails}")
                if "WARNING: DATA RACE" in proc.stdout + proc.stderr:
                    raise AssertionError("Go race detector reported a race")
                rows.append({"arm": key, "test": label, "observed": observed,
                             "expected": expected, "failed_cases": list(actual_subfails)})
    return {"go": go, "source_integrity": "SEVEN_GIT_BLOBS_EXACT", "scope": "ISOLATED_ROUTER_NOT_FULL_CHI",
            "tests": len(rows), "expected_match": all(x["observed"] == x["expected"] for x in rows),
            "novel_architecture_winner": "NOT_IDENTIFIED", "human_repair_cost": "NOT_MEASURED", "rows": rows}


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
