"""Compare the archived OCP reference sources with saved completion inputs."""

import argparse
import json
from pathlib import Path
from zipfile import ZipFile

from audit_are_we_solid import ROOT, inspect_ground_truth


REFERENCE_SIDES = ("input", "output")
EXAMPLE_RUN = "ocp--codellama70b-temp0-latest--example"
EXAMPLE_ROW_ID = 12


def audit_alignment(path):
    with ZipFile(path) as archive:
        references = inspect_ground_truth(archive, "ocp")
        raw = {side: {record[side] for record in references} for side in REFERENCE_SIDES}
        trimmed = {side: {code.strip() for code in raw[side]} for side in REFERENCE_SIDES}
        matches = {}
        example = None
        for name in sorted(archive.namelist()):
            if not (name.startswith(ROOT + "completions/test/ocp--")
                    and name.endswith("/output_test.jsonl")):
                continue
            for line_number, line in enumerate(archive.read(name).splitlines(), start=1):
                if not line.strip():
                    continue
                row = json.loads(line)
                counts = matches.setdefault(row["strategy"], {
                    "saved_records": 0,
                    "exact": dict.fromkeys(REFERENCE_SIDES, 0),
                    "outer_whitespace_trimmed": dict.fromkeys(REFERENCE_SIDES, 0),
                })
                counts["saved_records"] += 1
                code = row["input"]
                for side in REFERENCE_SIDES:
                    counts["exact"][side] += code in raw[side]
                    counts["outer_whitespace_trimmed"][side] += code.strip() in trimmed[side]
                if Path(name).parent.name == EXAMPLE_RUN and row["id"] == EXAMPLE_ROW_ID:
                    if example is not None or row["language"] != "PYTHON":
                        raise ValueError("Unexpected record at the Python EXAMPLE locator")
                    example = {"member": name, "line": line_number, "id": row["id"]}
        if example is None:
            raise ValueError("Python EXAMPLE record was not found")
    return {"reference_pair_count": len(references), "by_strategy": matches,
            "saved_prompt_locator": example}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    args = parser.parse_args()
    print(json.dumps(audit_alignment(args.archive), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
