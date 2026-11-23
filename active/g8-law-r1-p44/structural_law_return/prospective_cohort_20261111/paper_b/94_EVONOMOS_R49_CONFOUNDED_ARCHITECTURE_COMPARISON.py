#!/usr/bin/env python3
"""Exact constructed Simpson reversal in observational architecture maintenance costs.

This is a causal-inference teaching fixture with invented strata and costs,
not an empirical evaluation, a new theorem or measured SOLID performance.
"""
from fractions import Fraction as F
import json

# Hard contract eligibility is a prerequisite, assumed satisfied by both designs.
# Stratified cost for maintenance episode: X is strictly cheaper within each regime.
COST = {"easy": {"B": F(2), "X": F(1)},
        "hard": {"B": F(12), "X": F(11)}}
# Nonrandom assignment: the 'better' X architecture was selected for hard work.
ASSIGNMENT = {"B": {"easy": F(9, 10), "hard": F(1, 10)},
              "X": {"easy": F(1, 10), "hard": F(9, 10)}}


def observed(architecture):
    return sum(ASSIGNMENT[architecture][w] * COST[w][architecture]
               for w in ("easy", "hard"))


def matched_cost(architecture):
    return (COST["easy"][architecture] + COST["hard"][architecture])/2


def main():
    assert COST["easy"]["X"] < COST["easy"]["B"]
    assert COST["hard"]["X"] < COST["hard"]["B"]
    assert observed("B") == 3 and observed("X") == 10
    assert matched_cost("B") == 7 and matched_cost("X") == 6
    out = {
        "invented_regime_costs": {k:{a:str(v) for a,v in x.items()} for k,x in COST.items()},
        "observed_nonrandom": {a: str(observed(a)) for a in ("B", "X")},
        "matched_equal_regime": {a: str(matched_cost(a)) for a in ("B", "X")},
        "observational_conclusion": "B looks cheaper (3 vs 10)",
        "matched_conclusion": "X is cheaper (6 vs 7)",
        "requires_real_world_testing": True,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
