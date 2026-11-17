"""Check whether additive rendering reaches a client's original import."""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from ocp_case import BASE


DISPATCH_ADAPTER = """from render import render as _render


def render(kind, *, bracketed=False):
    value = _render(kind)
    return f"[{value}]" if bracketed else value
"""
SHAPE_ADAPTER = """from circle import render as render_circle
from square import render as render_square


def render(kind, *, bracketed=False):
    renderers = {"circle": render_circle, "square": render_square}
    if kind not in renderers:
        raise ValueError(kind)
    value = renderers[kind]()
    return f"[{value}]" if bracketed else value
"""
PLUGIN = """def decorate(value):
    return f"[{value}]"
"""
CLIENT = """from importlib import import_module
import sys

layout, entry, expected = sys.argv[1:]
kinds = ("circle", "square")


def original(kind):
    if layout == "dispatch":
        return import_module("render").render, (kind,)
    return import_module(kind).render, ()


def client(kind):
    if entry == "additional":
        return import_module("render_adapter").render, (kind,)
    return original(kind)


for kind in kinds:
    old, old_args = original(kind)
    call, args = client(kind)
    assert old(*old_args) == kind
    assert call(*args) == kind
    if expected == "works":
        assert call(*args, bracketed=True) == f"[{kind}]"
        assert call(*args, bracketed=False) == kind
    else:
        try:
            call(*args, bracketed=True)
        except TypeError as error:
            if expected != "no_keyword" or "bracketed" not in str(error):
                raise
        except ModuleNotFoundError as error:
            if expected != "no_plugin" or error.name != "render_style":
                raise
        else:
            raise AssertionError(f"Expected {expected} for {kind}")
    assert old(*old_args) == kind

if layout == "dispatch":
    for use_style in (False, True) if expected == "works" else (False,):
        try:
            function, _ = client("unsupported")
            options = {"bracketed": True} if use_style else {}
            function("unsupported", **options)
        except ValueError as error:
            assert error.args == ("unsupported",)
        else:
            raise AssertionError("Expected ValueError for unsupported shape")
"""


def wrap_originals(before, layout, *, hook):
    signature = "kind" if layout == "dispatch" else ""
    local_arguments = f"{signature}, " if signature else ""
    if hook:
        decoration = '    if bracketed:\n        from render_style import decorate\n        return decorate(value)\n    return value\n'
    else:
        decoration = '    return f"[{value}]" if bracketed else value\n'
    return {
        name: source.replace("def render(", "def _render(", 1)
        + f"\n\ndef render({local_arguments}*, bracketed=False):\n"
        + f"    value = _render({signature})\n"
        + decoration
        for name, source in before.items()
    }


def exercise(sources, layout, entry, outcome):
    with TemporaryDirectory() as work:
        for name, source in sources.items():
            Path(work, name).write_bytes(source.encode("utf-8"))
        subprocess.run(
            [sys.executable, "-B", "-E", "-c", CLIENT, layout, entry, outcome],
            cwd=work,
            check=True,
        )
        return {name: Path(work, name).read_bytes() for name in sources}


def run():
    results = []
    for layout, plain in BASE.items():
        hook = wrap_originals(plain, layout, hook=True)
        adapter = {"render_adapter.py": DISPATCH_ADAPTER if layout == "dispatch" else SHAPE_ADAPTER}
        # Both negative controls use the identical caller that is used for a passing direct route.
        exercise(plain | adapter, layout, "original", "no_keyword")
        exercise(hook, layout, "original", "no_plugin")

        candidates = (
            ("additional_entry", plain, adapter, "additional", 0),
            ("original_entry", plain, wrap_originals(plain, layout, hook=False), "original", len(plain)),
            ("original_entry_with_hook", hook, {"render_style.py": PLUGIN}, "original", 0),
        )
        for scenario, baseline, patch, entry, count in candidates:
            actual = exercise(baseline | patch, layout, entry, "works")
            changed = sorted(name for name, source in baseline.items()
                             if actual[name] != source.encode("utf-8"))
            added = sorted(actual.keys() - baseline.keys())
            assert len(changed) == count, (layout, scenario, changed)
            assert len(added) == (0 if scenario == "original_entry" else 1), (layout, scenario, added)
            results.append({
                "layout": layout,
                "scenario": scenario,
                "changed_existing_files": changed,
                "added_files": added,
            })
    return results


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
