"""Inspect the archived ASE benchmark without executing archive members."""

import argparse
import ast
from collections import Counter
from hashlib import file_digest
import json
from pathlib import Path
from zipfile import ZipFile


ROOT = "AreWeSOLID/dataset/"
GROUND_TRUTH = ROOT + "groundtruth/"
PRINCIPLES = ("dip", "isp", "lsp", "ocp", "srp")
LANGUAGES = ("CSHARP", "JAVA", "KOTLIN", "PYTHON")
LEVELS = ("EASY", "HARD", "MODERATE")


def declared_methods(text):
    return {
        (node.name, member.name)
        for node in ast.parse(text).body
        if isinstance(node, ast.ClassDef)
        for member in node.body
        if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
        and not member.name.startswith("_")
    }


def inspect_ground_truth(archive, principle):
    path = GROUND_TRUTH + f"{principle}_violations.json"
    rows = json.loads(archive.read(path))["code_examples"]
    language_aliases = {"C#": "CSHARP"}
    groups = Counter(
        (language_aliases.get(row["language"], row["language"]), row["level"])
        for row in rows
    )
    expected = {(language, level): 4 for language in LANGUAGES for level in LEVELS}
    labels = Counter(row["violation"] for row in rows)
    if groups != expected or labels != {principle.upper(): 48}:
        raise ValueError(f"Unexpected ground-truth layout in {path}")
    return rows


def inspect_ocp(rows):
    fields = Counter(field for row in rows for field in row)
    methods = []
    for number, row in enumerate(rows, 1):
        if row["language"] != "PYTHON":
            continue
        removed = declared_methods(row["input"]) - declared_methods(row["output"])
        methods.append((number, sorted(".".join(pair) for pair in removed)))
    return {
        "fields": dict(sorted(fields.items())),
        "python_pair_count": len(methods),
        "python_rows_with_removed_declared_method": [
            number for number, removed in methods if removed
        ],
        "python_row_37_removed_declared_methods": dict(methods)[37],
    }


def audit(path):
    with path.open("rb") as source:
        sha256 = file_digest(source, "sha256").hexdigest()
    with ZipFile(path) as archive:
        by_principle = {
            key: inspect_ground_truth(archive, key)
            for key in PRINCIPLES
        }
        completion_prefix = ROOT + "completions/test/ocp--"
        completion_counts = {
            name: sum(1 for line in archive.read(name).splitlines() if line.strip())
            for name in archive.namelist()
            if name.startswith(completion_prefix) and name.endswith("/output_test.jsonl")
        }
        if len(completion_counts) != 16 or set(completion_counts.values()) != {48}:
            raise ValueError("Unexpected OCP completion inventory")
    return {
        "archive_sha256": sha256,
        "ground_truth_counts": {
            key.upper(): len(rows) for key, rows in by_principle.items()
        },
        "raw_c_sharp_labels": {
            key.upper(): sorted({row["language"] for row in rows} & {"C#", "CSHARP"})
            for key, rows in by_principle.items()
        },
        "ocp": inspect_ocp(by_principle["ocp"]),
        "ocp_completion_file_count": len(completion_counts),
        "ocp_completion_rows_per_file": 48,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    args = parser.parse_args()
    print(json.dumps(audit(args.archive), indent=2))


if __name__ == "__main__":
    main()
