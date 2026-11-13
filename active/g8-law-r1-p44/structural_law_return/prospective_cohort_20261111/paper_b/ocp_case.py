"""Generate an OCP review fixture and execute its four published reference patches."""
import argparse
import json

BASE = {
    "dispatch": {
        "render.py": '''def render(shape):
    match shape:
        case "circle": return "circle"
        case "square": return "square"
        case _: raise ValueError(shape)
''',
    },
    "methods": {
        "circle.py": 'def render(): return "circle"\n',
        "square.py": 'def render(): return "square"\n',
    },
}
# The published candidates are deliberately small and explicit. Other edit
# strategies are outside this fixture's comparison.
PATCHES = {
    ("dispatch", "triangle"): {
        "render.py": BASE["dispatch"]["render.py"].replace(
            '        case _: raise', '        case "triangle": return "triangle"\n        case _: raise'
        ),
    },
    ("methods", "triangle"): {"triangle.py": 'def render(): return "triangle"\n'},
    ("dispatch", "label"): {
        "label.py": '''def label(shape):
    match shape:
        case "circle": return "Circle"
        case "square": return "Square"
        case _: raise ValueError(shape)
''',
    },
    ("methods", "label"): {
        "circle.py": BASE["methods"]["circle.py"] + 'def label(): return "Circle"\n',
        "square.py": BASE["methods"]["square.py"] + 'def label(): return "Square"\n',
    },
}
TASKS = {
    "triangle": "Support rendering a triangle as 'triangle'. Preserve circle and square rendering.",
    "label": "Add a label operation returning 'Circle' and 'Square'. Preserve existing rendering.",
}
POLICY = {
    "dispatch": "Each operation has one dispatch file. Keep this representation for the candidate patch.",
    "methods": "Each shape owns its operations in its file. Keep this representation for the candidate patch.",
}


def prompt_fixture(*, reveal_demand):
    return [
        {
            "design": design,
            "source": source,
            **({"request": request} if reveal_demand else {}),
            "representation": POLICY[design],
            "protected_paths": sorted(source),
            "question": "Can the proposed design accommodate the requested change without editing a "
                        "protected file? State assumptions. If information is missing, say what is needed.",
        }
        for design, source in BASE.items()
        for request in (TASKS.values() if reveal_demand else (None,))
    ]


def check_cases():
    results = []
    for (design, demand), patch in PATCHES.items():
        before = BASE[design]
        after = before | patch
        modules = {}
        for path, source in after.items():
            namespace = {}
            exec(compile(source, path, "exec"), namespace)
            modules[path] = namespace

        checks = []
        shapes = ["circle", "square"]
        if demand == "triangle":
            shapes.append("triangle")
        for shape in shapes:
            if design == "dispatch":
                checks.append(modules["render.py"]["render"](shape) == shape)
            else:
                checks.append(modules[f"{shape}.py"]["render"]() == shape)

        if demand == "label":
            for shape in shapes:
                if design == "dispatch":
                    checks.append(modules["label.py"]["label"](shape) == shape.title())
                else:
                    checks.append(modules[f"{shape}.py"]["label"]() == shape.title())

        if not all(checks):
            raise RuntimeError(f"Functional contract failed for {design}/{demand}")
        changed = sorted(path for path, content in before.items() if after[path] != content)
        results.append({
            "design": design,
            "demand": demand,
            "functional_checks_passed": len(checks),
            "changed_protected_paths": changed,
            "added_paths": sorted(after.keys() - before.keys()),
        })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prompt-fixture", "blind-fixture", "check"])
    args = parser.parse_args()
    result = check_cases() if args.mode == "check" else prompt_fixture(
        reveal_demand=args.mode == "prompt-fixture"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
