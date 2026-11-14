"""Check demand and protected-boundary controls for published OCP reference patches."""
import json

from ocp_case import BASE, check_cases


def run():
    cases = {
        (case["design"], case["demand"]): case for case in check_cases()
    }
    results = []
    for design, baseline in BASE.items():
        for demand in ("triangle", "label"):
            case = cases[design, demand]
            changed = set(case["changed_protected_paths"])
            for boundary, protected in (("all", set(baseline)), ("none", set())):
                results.append({
                    "design": design,
                    "demand": demand,
                    "boundary": boundary,
                    "protected_paths": sorted(protected),
                    "touched_protected_paths": sorted(changed & protected),
                    "reference_patch_preserves_boundary": not (changed & protected),
                })

    observed = {
        (row["design"], row["demand"], row["boundary"]):
            row["reference_patch_preserves_boundary"]
        for row in results
    }
    expected = {
        ("dispatch", "triangle", "all"): False,
        ("dispatch", "label", "all"): True,
        ("methods", "triangle", "all"): True,
        ("methods", "label", "all"): False,
    }
    expected.update({(design, demand, "none"): True for design, demand, _ in list(expected)})
    if observed != expected:
        raise AssertionError(f"Unexpected reference-patch verdicts: {observed}")
    return results


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
