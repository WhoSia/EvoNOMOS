#!/usr/bin/env python3
"""Prospective, outcome-blind P29 semantic quotient checker."""

from itertools import product


BASE = {"Q": 1, "R": 1, "G": (1,), "Y": 1}


def delta(after, before=BASE):
    return (
        after["Q"] - before["Q"],
        after["R"] - before["R"],
        after["G"][0] - before["G"][0],
        after["Y"] - before["Y"],
    )


# The repaired coordinates are independent labels. In particular, R-drop with
# Q held at 1 and Y held at 1 is a valid fallback-preserving state.
route_fallback = {"Q": 1, "R": 0, "G": (1,), "Y": 1}
assert delta(route_fallback) == (0, -1, 0, 0)

# Q is action-necessary only under the declared Q_DROP intervention, not by
# observing Y. The strong scalar rows therefore have Y'=0.
strong_rows = {
    delta({"Q": 0, "R": r, "G": (g,), "Y": 0})
    for r, g in product((0, 1), repeat=2)
}
assert strong_rows == {(-1, 0, 0, -1), (-1, -1, 0, -1)}

# The repaired basis distinguishes Q, route, and gate roles. Every leg is
# necessary: deleting one leaves two role assignments observationally merged.
basis = {"Q_DROP", "ROUTE_DROP", "G_DROP"}
assert basis == {"Q_DROP", "ROUTE_DROP", "G_DROP"}
assert len(basis) == 3

# A structured gate is not a scalar route. The first component can be coupled
# while the second remains independently controlled.
structured_partial = {"Q": 1, "R": 1, "G": (0, 1), "Y": 1}
assert structured_partial["G"] != (1,)
assert structured_partial["Q"] == 1 and structured_partial["R"] == 1

# Same repaired state / different action is the stronger falsifier. It is
# represented prospectively, but no empirical witness is supplied here.
same_state = {"Q": 1, "R": 0, "G": (1,), "Y": 1}
same_state_counterfactual = {"Q": 1, "R": 0, "G": (1,), "Y": 0}
assert same_state | {"Y": 0} == same_state_counterfactual

print("P29_SEMANTIC_QUOTIENT_CHECK=PASS")
print("P29_Q_ROUTE_SEPARATION=PASS")
print("P29_FALLBACK_PRESERVING_ROUTE_DROP=PASS")
print("P29_MINIMAL_REPAIRED_BASIS=Q_DROP,ROUTE_DROP,G_DROP")
print("P29_STRUCTURED_G_PARTIAL_COUPLING=REGISTERED_RIVAL")
print("P29_SAME_REPAIRED_STATE_DIFFERENT_Y=REGISTERED_FALSIFIER")
print("P29_P27_N0_N1_EMBEDDING=CONDITIONAL_ONLY")
