"""R84 LIRA/JEV evidence ledger audit.

The 0..1 entries are explicitly subjective research-director assessments,
NOT measured probabilities, posterior confidence, empirical effect sizes or
independent peer ratings. Validate internal consistency and veto unsupported
scientific promotions without averaging across hard gates.

Usage: python tools/r84_lira_jev_audit.py [--ledger path]
"""
import argparse
import json
import math
from pathlib import Path

WEIGHTS = {"D": .30, "I": .20, "R": .20, "F": .20, "S": .10}
CLAIM_AXES = tuple(WEIGHTS) + ("E", "C", "G", "L", "N", "K", "X", "Q")
TASK_AXES = ("L", "V", "B", "N", "K", "X", "Q")
HARD_GATES = {
    "C07": ("C", .20),  # no human-review experiment
    "C08": ("C", .20),  # separate ATLAS novelty unsupported
    "C10": ("C", .20),  # no causal effect data
}


def bounded(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError(f"invalid {name}: {value!r}")


def verify(data):
    claims = data["claims"]
    tasks = data["tasks"]
    if len(claims) != 10 or len(tasks) != 8:
        raise ValueError("unexpected ledger size")
    if len({r["id"] for r in claims}) != len(claims):
        raise ValueError("duplicate claim")
    if len({r["id"] for r in tasks}) != len(tasks):
        raise ValueError("duplicate task")
    for row in claims:
        for name in CLAIM_AXES:
            bounded(row[name], row["id"] + "." + name)
        expected = round(sum(weight * row[key] for key, weight in WEIGHTS.items()), 3)
        if abs(expected - row["E"]) > 0.00001:
            raise ValueError(f"JEV E formula mismatch: {row['id']}: {row['E']} != {expected}")
        for field in ("claim", "source", "counter", "stop"):
            if not str(row.get(field, "")).strip():
                raise ValueError(f"missing provenance or defeater: {row['id']}.{field}")
    for row in tasks:
        for name in TASK_AXES:
            bounded(row[name], row["id"] + "." + name)
        for field in ("task", "condition", "stop"):
            if not str(row.get(field, "")).strip():
                raise ValueError(f"missing task evidence: {row['id']}.{field}")
    for claim_id, (axis, maximum) in HARD_GATES.items():
        row = next((r for r in claims if r["id"] == claim_id), None)
        if row is None or row[axis] > maximum:
            raise ValueError(f"unsupported claim promoted: {claim_id}.{axis}")
    atlas = next(row for row in tasks if row["id"] == "T08")
    if atlas["L"] != 0:
        raise ValueError("separate ATLAS work resumed without a new gate")
    if not data["meta"].get("no_compensation"):
        raise ValueError("missing noncompensatory gating")
    return {"result": "PASS_SUBJECTIVE_SCORE_LEDGER_INTEGRITY",
            "claims": len(claims), "tasks": len(tasks),
            "E_rule": WEIGHTS, "hard_gates": list(HARD_GATES),
            "assertion": "THIS_VALIDATES_LEDGER_STRUCTURE_NOT_SCIENTIFIC_TRUTH"}


def ranking(tasks, scenario):
    """Scenario probes for unstable prioritization. Non-empirical utility scores."""
    ranks = []
    for t in tasks:
        if t["id"] == "T08":
            continue
        if scenario == "default":
            val = t["L"]
        elif scenario == "information_first":
            val = .20*t["L"] + .65*t["V"] + .15*t["X"]
        elif scenario == "low_cost":
            val = .25*t["L"] + .30*t["V"] + .45*(1-t["B"])
        elif scenario == "causal_first":
            val = .20*t["L"] + .20*t["V"] + .60*t["X"]
        else:
            raise ValueError("invalid scenario")
        ranks.append((t["id"], round(val, 4)))
    return sorted(ranks, key=lambda r: (-r[1], r[0]))


def negative_tests(data):
    from copy import deepcopy
    mutations = [
        lambda x: x["claims"][0].update(E=0.123),
        lambda x: x["claims"][0].update(C=1.12),
        lambda x: x["claims"][0].update(D=float("nan")),
        lambda x: x["claims"][0].update(source=""),
        lambda x: x["claims"][0].update(id=x["claims"][1]["id"]),
        lambda x: x["tasks"][-1].update(L=.50),
        lambda x: next(r for r in x["claims"] if r["id"] == "C07").update(C=.90),
        lambda x: x["tasks"][0].update(B=-1),
        lambda x: x["meta"].update(no_compensation=[]),
    ]
    for i, mutate in enumerate(mutations):
        copy = deepcopy(data)
        mutate(copy)
        try:
            verify(copy)
        except (ValueError, KeyError, TypeError):
            continue
        raise AssertionError(f"mutation {i} was erroneously accepted")
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, default=Path(__file__).resolve().parents[1]
                        / "research/R84_LIRA_JEV_multiaxis_scores.json")
    args = parser.parse_args()
    ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    result = verify(ledger)
    result["negative_controls"] = negative_tests(ledger)
    result["priority_sensitivity"] = {name: ranking(ledger["tasks"], name)
                                      for name in ("default", "information_first", "low_cost", "causal_first")}
    result["claim_scores"] = [{"id":r["id"], "E":r["E"], "C":r["C"], "G":r["G"],
                               "L":r["L"], "N":r["N"], "K":r["K"], "X":r["X"], "Q":r["Q"]}
                              for r in ledger["claims"]]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
