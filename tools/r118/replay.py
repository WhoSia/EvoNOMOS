"""Rehydrate R118's immutable historical inputs and replay in a new directory.

Usage (full Git clone, Python >=3.10, local Go >=1.23):
    python tools/r118/replay.py /path/to/new-evidence-directory

No network, checkout, branch change, or modification of original run.py.
"""
import hashlib
from pathlib import Path
import subprocess
import sys

HIST = "4a619db738e6bba36edbd47379e4e183419afb28"
R118 = "4c70f31afbe1f1e2e238b5f539d0fdefc71d8f9c"
REPO = Path(__file__).resolve().parents[2]
ARM_PREFIX = "tools/p35-p4/arms/"
PATCH = "active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/matched_contract/shared-empty-type.patch"
PINS = {
    "independent/content_charset.go": (HIST, ARM_PREFIX + "independent/content_charset.go", "7ecb4a2d5e91d7ef775f824e64f2210bf360e5f2"),
    "independent/content_type.go": (HIST, ARM_PREFIX + "independent/content_type.go", "8751cb40ca041b8f56bc1c6b9260db0a28434ee6"),
    "shared/content_charset.go": (HIST, ARM_PREFIX + "shared/content_charset.go", "53d6ef557bc890cb8727d552e7ab16dc46143a88"),
    "shared/content_type.go": (HIST, ARM_PREFIX + "shared/content_type.go", "d1fad4adce7225e674c1c035636ef53bb9a27e4c"),
    "shared/content_media_parse.go": (HIST, ARM_PREFIX + "shared/content_media_parse.go", "1144b1fd275994fde766a331a9995cafc2ed0eb9"),
    "shared-empty-type.patch": (HIST, PATCH, "206c455379d5bf772421c1dc165cee4448f62664"),
    "run.py": (R118, "tools/r118/run.py", "e80d34d96ba4762be0fa710908270382477e610c"),
    "token_probe.go.txt": (R118, "tools/r118/token_probe.go.txt", "70f54c94ff6ac219017f07470cc8ef61cf736121"),
}


def blob_sha(data):
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    out = Path(sys.argv[1]).resolve()
    # Verify all bytes before creating any destination files.
    recovered = {}
    for dest, (ref, path, expected) in PINS.items():
        data = subprocess.check_output(
            ["git", "-C", str(REPO), "show", f"{ref}:{path}"]
        )
        actual = blob_sha(data)
        if actual != expected:
            raise RuntimeError(f"{dest}: {actual} != {expected}")
        recovered[dest] = data
    out.mkdir(parents=True, exist_ok=False)
    for dest, data in recovered.items():
        p = out / dest
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    with (out / "run.jsonl").open("wb") as receipt:
        result = subprocess.run(
            [sys.executable, str(out / "run.py")],
            cwd=out, stdout=receipt, check=False,
        )
    sys.stdout.write((out / "run.jsonl").read_text())
    result.check_returncode()


if __name__ == "__main__":
    main()
