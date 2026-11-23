"""Execute Paper B's batch rendering candidates under two ownership rules."""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from ocp_case import BASE


OPERATION_BATCH = '''from render import render


def render_many(kinds):
    return [f"[{render(kind)}]" for kind in kinds]
'''

SHAPE_BATCH = '''import circle
import square


def render_many(kinds):
    renderers = {"circle": circle.render, "square": square.render}
    results = []
    for kind in kinds:
        if kind not in renderers:
            raise ValueError(kind)
        results.append(f"[{renderers[kind]()}]")
    return results
'''

OWNED_SHAPE_BATCH = '''import circle
import square


def render_many(kinds):
    renderers = {"circle": circle.render_batch_item, "square": square.render_batch_item}
    results = []
    for kind in kinds:
        if kind not in renderers:
            raise ValueError(kind)
        results.append(renderers[kind]())
    return results
'''

OWNED_ITEM = '''

def render_batch_item():
    return f"[{render()}]"
'''

CHECKS = '''import sys
from unittest.mock import patch

from batch import render_many

layout, rule = sys.argv[1:]
assert render_many(["square", "circle", "square"]) == ["[square]", "[circle]", "[square]"]
assert render_many([]) == []
try:
    render_many(["circle", "unsupported"])
except ValueError as error:
    assert error.args == ("unsupported",)
else:
    raise AssertionError("An unsupported shape must raise ValueError")

if layout == "dispatch":
    from render import render
    assert (render("circle"), render("square")) == ("circle", "square")
    with patch("batch.render", return_value="legacy"):
        assert render_many(["circle"]) == ["[legacy]"]
else:
    import circle
    import square
    assert (circle.render(), square.render()) == ("circle", "square")
    if rule == "layout_ownership":
        with patch("circle.render_batch_item", return_value="circle-owned"), \
             patch("square.render_batch_item", return_value="square-owned"):
            assert render_many(["square", "circle"]) == ["square-owned", "circle-owned"]
    else:
        with patch("circle.render", return_value="legacy"):
            assert render_many(["circle"]) == ["[legacy]"]
'''


def run():
    shape_sources = BASE["methods"]
    owned = {name: source + OWNED_ITEM for name, source in shape_sources.items()}
    operation_patch = {"batch.py": OPERATION_BATCH}
    candidates = (
        ("dispatch", "layout_ownership", operation_patch, 0),
        ("methods", "layout_ownership", owned | {"batch.py": OWNED_SHAPE_BATCH}, 2),
        ("dispatch", "shared_adapter", operation_patch, 0),
        ("methods", "shared_adapter", {"batch.py": SHAPE_BATCH}, 0),
    )
    rows = []
    for layout, rule, patch, predicted_existing in candidates:
        before = BASE[layout]
        after = before | patch
        with TemporaryDirectory() as directory:
            for name, source in after.items():
                Path(directory, name).write_bytes(source.encode("utf-8"))
            subprocess.run([sys.executable, "-B", "-c", CHECKS, layout, rule],
                           cwd=directory, check=True)
            changed = sorted(name for name, source in before.items()
                             if Path(directory, name).read_bytes() != source.encode("utf-8"))
            added = sorted(p.name for p in Path(directory).glob("*.py") if p.name not in before)
        rows.append({
            "layout": layout,
            "placement_rule": rule,
            "changed_existing_files": changed,
            "added_files": added,
            "matches_prediction": len(changed) == predicted_existing and added == ["batch.py"],
        })
    return rows


if __name__ == "__main__":
    results = run()
    print(json.dumps(results, indent=2))
    if not all(row["matches_prediction"] for row in results):
        raise SystemExit(1)
