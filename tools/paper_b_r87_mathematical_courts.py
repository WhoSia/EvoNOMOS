"""R87 mathematical sanity checks for a contextual design-warrant atlas.

These are familiar mathematical constructions and counterexamples, NOT
new universal software principles, empirical outcomes, or proofs of novelty.
"""
from fractions import Fraction
from itertools import combinations, product
import json


def info_join(a, b):
    """Product-order supremum for support/defeat evidence bits."""
    return (max(a[0], b[0]), max(a[1], b[1]))


def info_meet(a, b):
    return (min(a[0], b[0]), min(a[1], b[1]))


def check_lattice():
    states = list(product((0, 1), repeat=2))
    for a, b, c in product(states, repeat=3):
        assert info_join(a, info_meet(a, b)) == a
        assert info_meet(a, info_join(a, b)) == a
        assert info_join(a, info_join(b, c)) == info_join(info_join(a, b), c)
        assert info_meet(a, info_meet(b, c)) == info_meet(info_meet(a, b), c)
    return len(states)**3


def local_global_counterexample():
    # Variables x,y,z; local charts U={x,y}, V={y,z}.
    # Independent binary assignments agree on intersection {y}.
    first = {"x": 0, "y": 0}
    second = {"y": 0, "z": 0}
    assert first["y"] == second["y"]
    combined = {**first, **second}
    # Cross-chart global requirement cannot be checked in either chart.
    global_requirement = combined["x"] != combined["z"]
    assert not global_requirement
    return {"overlap_consistent": True, "global_requirement_satisfied": global_requirement}


def robust_cost_boundary():
    # R60 researcher-defined toy: M = 4-2q, S = 1+5q.
    q = Fraction(3, 7)
    assert 4 - 2*q == 1 + 5*q
    interval = (Fraction(3, 10), Fraction(3, 5))
    assert interval[0] < q < interval[1]
    lower = interval[0]
    upper = interval[1]
    assert 4 - 2*lower > 1 + 5*lower
    assert 4 - 2*upper < 1 + 5*upper
    return {"cost_tie_probability": str(q), "uncertain_interval": list(map(str, interval)),
            "uniformly_cheaper_on_interval": False}


def minimum_rationale_cover():
    # Expository finite instance, not the complexity-theoretic reduction.
    obligations = {0, 1, 2}
    options = [({0, 1}, 2), ({1, 2}, 2), ({0, 2}, 2)]
    solutions = []
    for n in range(len(options)+1):
        for chosen in combinations(range(len(options)), n):
            covered = set().union(*(options[i][0] for i in chosen))
            if obligations <= covered:
                solutions.append((sum(options[i][1] for i in chosen), chosen))
    assert min(solutions)[0] == 4
    return {"minimal_toy_cost": min(solutions)[0], "known_problem": "WEIGHTED_SET_COVER"}


def test():
    return {"result": "PASS_FOUR_MATHEMATICAL_SANITY_CHECKS",
            "lattice_associative_absorption_cases": check_lattice(),
            "gluing_counterexample": local_global_counterexample(),
            "robust_design_tradeoff": robust_cost_boundary(),
            "minimum_rationale_cover": minimum_rationale_cover(),
            "independent_architecture_advantage": "NOT_TESTED",
            "new_complexity_theorem": False,
            "mathematics_status": "KNOWN_CONSTRUCTIONS_AND_EXPLICIT_COUNTEREXAMPLES"}


if __name__ == "__main__":
    print(json.dumps(test(), ensure_ascii=False, indent=2))
