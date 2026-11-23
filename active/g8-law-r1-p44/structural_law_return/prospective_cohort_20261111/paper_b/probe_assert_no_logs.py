"""Replay CPython's assertNoLogs addition on two pinned unittest snapshots.

Pass directories containing case.py, _log.py, util.py and result.py from
the parent and the commit. The historical modules run on the host Python
and use its logging module. This is a focused probe of the public methods.
"""

import argparse
from hashlib import sha1
import importlib
import json
import logging
from pathlib import Path
import sys
import tempfile
from types import ModuleType


COMMON = {
    "util.py": "050eaed0b3f58fb09d1797f81c19de44110c511e",
    "result.py": "111317b329a8521b5482a68d5f8962ba5772b6d9",
}
BEFORE = COMMON | {
    "case.py": "52eb7d05ed1431c38c7f151b5e0162265da58582",
    "_log.py": "94e7e758bd9a077d036afcc2abc6b6ab40c3689c",
}
AFTER = COMMON | {
    "case.py": "872f12112755e99dc53154bac166a93572dd95ae",
    "_log.py": "961c448a7fb356474f731a4a67a5c694553fb397",
}


def read_snapshot(path, expected):
    sources = {}
    for name, oid in expected.items():
        source = (path / name).read_bytes()
        blob = f"blob {len(source)}\0".encode("ascii") + source
        if sha1(blob).hexdigest() != oid:
            raise ValueError(f"{path / name} did not match Git blob {oid}")
        sources[name] = source
    return sources


def run_snapshot(name, sources):
    with tempfile.TemporaryDirectory() as tmp:
        for filename, contents in sources.items():
            (Path(tmp) / filename).write_bytes(contents)
        package = ModuleType(name)
        package.__path__ = [tmp]
        sys.modules[name] = package
        try:
            case = importlib.import_module(f"{name}.case")
            return probe(case.TestCase(), name)
        finally:
            for entry in tuple(sys.modules):
                if entry == name or entry.startswith(f"{name}."):
                    del sys.modules[entry]


def probe(case, name):
    parent = logging.getLogger(name)
    child = logging.getLogger(f"{name}.child")
    expected_output = [f"INFO:{name}.child:example"]
    old_handlers = [logging.NullHandler()]
    parent.handlers = old_handlers
    parent.propagate = False
    parent.setLevel(logging.WARNING)
    try:
        with case.assertLogs(parent, "INFO") as captured:
            child.info("example")
        with case.assertRaises(case.failureException):
            with case.assertLogs(parent, "INFO"):
                child.debug("below threshold")
        outcomes = {
            "legacy_records": [
                (rec.name, rec.levelno, rec.getMessage())
                for rec in getattr(captured, "records", ())
            ] == [(child.name, logging.INFO, "example")],
            "legacy_output": getattr(captured, "output", None) == expected_output,
            "legacy_fails_on_no_matching_log": True,
        }
        if hasattr(case, "assertNoLogs"):
            with case.assertNoLogs(parent, "INFO") as value:
                child.debug("below threshold")
            with case.assertRaises(case.failureException) as failure:
                with case.assertNoLogs(parent, "INFO"):
                    child.info("example")
            with case.assertRaisesRegex(RuntimeError, "sentinel"):
                with case.assertNoLogs(parent, "INFO"):
                    raise RuntimeError("sentinel")
            outcomes["new"] = {
                "passes_without_matching_logs": True,
                "yields_none": value is None,
                "reports_matching_child_log": expected_output[0] in str(failure.exception),
                "propagates_unexpected_exception": True,
            }
        else:
            outcomes["new"] = None
        outcomes["logger_restored"] = (
            parent.handlers == old_handlers
            and parent.level == logging.WARNING
            and parent.propagate is False
        )
        return outcomes
    finally:
        parent.handlers = []
        parent.setLevel(logging.NOTSET)
        parent.propagate = True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    args = parser.parse_args()
    before = read_snapshot(args.before, BEFORE)
    after = read_snapshot(args.after, AFTER)
    old_return = b"        return handler.watcher\n"
    if after["_log.py"].count(old_return) != 1:
        raise ValueError("Expected one historical watcher-return line")
    control = after | {"_log.py": after["_log.py"].replace(old_return, b"        return None\n")}
    baseline = run_snapshot("paper_b_parent", before)
    merged = run_snapshot("paper_b_merged", after)
    negative = run_snapshot("paper_b_control", control)
    for key in ("legacy_records", "legacy_output"):
        if not baseline[key] or not merged[key] or negative[key]:
            raise AssertionError(key)
    for outcomes in (baseline, merged, negative):
        if not outcomes["legacy_fails_on_no_matching_log"] or not outcomes["logger_restored"]:
            raise AssertionError(outcomes)
    if baseline["new"] is not None or not all(merged["new"].values()) or negative["new"] != merged["new"]:
        raise AssertionError("Unexpected feature evidence")
    print(json.dumps({"host": sys.version.split()[0], "baseline": baseline,
                      "merged": merged, "negative_control": negative}, indent=2))


if __name__ == "__main__":
    main()
