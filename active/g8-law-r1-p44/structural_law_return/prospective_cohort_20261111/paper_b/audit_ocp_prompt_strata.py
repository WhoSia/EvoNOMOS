"""Recount archived OCP prompts without extracting or running ZIP contents."""
import argparse
import ast
from collections import Counter, defaultdict
from hashlib import file_digest
import json
import re
from zipfile import ZipFile

ROOT = "AreWeSOLID/dataset/"


def audit(archive_path):
    with open(archive_path, "rb") as f:
        sha = file_digest(f, "sha256").hexdigest()
    with ZipFile(archive_path) as z:
        references = json.loads(z.read(ROOT + "groundtruth/ocp_violations.json"))["code_examples"]
        entries = []
        for filename in sorted(z.namelist()):
            if not (filename.startswith(ROOT + "completions/test/ocp--")
                    and filename.endswith("/output_test.jsonl")):
                continue
            for line in z.read(filename).splitlines():
                if line.strip():
                    row = json.loads(line)
                    source, prompt = row["input"], row["prompt"]
                    if not source or prompt.count(source) != 1:
                        raise ValueError("Could not isolate submitted code")
                    row["masked"] = prompt.replace(source, "<SUBMITTED-CODE>", 1)
                    entries.append(row)
    counts = Counter(row["input"] for row in entries)
    by_triple = defaultdict(set)
    by_strategy = defaultdict(set)
    for row in entries:
        key = (row["strategy"], row["language"], row["model"])
        by_triple[key].add(row["masked"])
        by_strategy[row["strategy"]].add(row["masked"])

    def strip_all(s):
        return re.sub(r"\s+", "", s)

    def ast_canon(s):
        try:
            return ast.dump(ast.parse(s), include_attributes=False)
        except (SyntaxError, IndentationError):
            return None

    normalizers = {"raw": lambda s: s, "outer_trim": str.strip,
                   "remove_whitespace": strip_all}
    align = {}
    for title, normalize in normalizers.items():
        reference_texts = {normalize(pair[k]) for pair in references for k in ("input", "output")}
        align[title] = sum(normalize(row["input"]) in reference_texts for row in entries)
    py_ref = {ast_canon(pair[k]) for pair in references if pair["language"] == "PYTHON"
              for k in ("input", "output")}
    py_ref.discard(None)
    py_rows = [row for row in entries if row["language"] == "PYTHON"]
    align["python_ast_dump"] = sum(ast_canon(row["input"]) in py_ref for row in py_rows)
    return {
        "sha256": sha,
        "reference_pairs": len(references),
        "saved_records": len(entries),
        "unique_submitted_sources": len(counts),
        "repeat_count_distribution": dict(sorted(Counter(counts.values()).items())),
        "unique_masked_scaffolds": len({row["masked"] for row in entries}),
        "scaffolds_per_strategy": {k: len(v) for k, v in sorted(by_strategy.items())},
        "strategy_language_model_triples": len(by_triple),
        "triples_with_nonconstant_scaffolds": sum(len(v) != 1 for v in by_triple.values()),
        "reference_alignment": align,
        "python_saved_records": len(py_rows),
        "python_ref_ast_sources": len(py_ref),
    }


if __name__ == "__main__":
    cli = argparse.ArgumentParser()
    cli.add_argument("archive")
    print(json.dumps(audit(cli.parse_args().archive), indent=2, ensure_ascii=False))
