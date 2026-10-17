#!/usr/bin/env python3
"""P42 R11-P10-P8: finite history monitor vs source-only endpoint factorization.

The four proof obligations and predicted finite/infinite witnesses were sealed
BEFORE this checker at commit 235c32e0a25f85905a3273a8fc73550450602574.
All states/permissions are authored mathematics, not verified third-party source.
Classical Myhill-Nerode derivatives and DFA/source products are acknowledged.
"""
from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from pathlib import Path

PRESEAL = "235c32e0a25f85905a3273a8fc73550450602574"
E = ("A", "B")
COST = {"A": (1, 0), "B": (0, 1)}


@dataclass(frozen=True, order=True)
class Source:
    a: int = 0
    b: int = 0

    @property
    def rights(self):
        return (1 - self.a, 1 - self.b)


def edit(s: Source, e: str):
    if e == "A" and not s.a:
        return Source(1, s.b), ("event-A", COST[e])
    if e == "B" and not s.b:
        return Source(s.a, 1), ("event-B", COST[e])
    return None


def run(h):
    s = Source()
    receipts = []
    for e in h:
        step = edit(s, e)
        if step is None:
            return None
        s, receipt = step
        receipts.append(receipt)
    return s, tuple(receipts)


def feasible_histories():
    words = ((),) + tuple((e,) for e in E) + tuple(itertools.product(E, repeat=2))
    return tuple(w for w in words if run(w) is not None)


# DFA for the new client history predicate: exact completed word AB.
DFA = {
    "start": {"A": "seen-A", "B": "dead"},
    "seen-A": {"A": "dead", "B": "accept"},
    "accept": {"A": "dead", "B": "dead"},
    "dead": {"A": "dead", "B": "dead"},
}


def monitor(h, initial="start"):
    q = initial
    for e in h:
        q = DFA[q][e]
    return q


def policy_bruteforce(h):
    return h == ("A", "B")


def completed_receipts(h):
    out = run(h)
    assert out is not None
    s, receipts = out
    cost = tuple(sum(r[1][i] for r in receipts) for i in range(2))
    return {"source": (s.a, s.b), "rights": s.rights, "total_cost": cost}


def suffix_costs(h, goal):
    """Source terminal goal; remaining cost only, not historical total cost."""
    r = run(h)
    assert r is not None
    initial, _ = r
    costs = set()
    for v in ((), ("A",), ("B",), ("A", "B"), ("B", "A")):
        s = initial
        receipts = []
        for e in v:
            step = edit(s, e)
            if step is None:
                break
            s, rec = step
            receipts.append(rec)
        else:
            if (s.a, s.b) in goal:
                costs.add(tuple(sum(x[1][i] for x in receipts) for i in range(2)))
    return frozenset(costs)


def balanced_policy(h: str) -> bool:
    n = len(h) // 2
    return len(h) % 2 == 0 and h == "a" * n + "b" * n


def main():
    feasible = feasible_histories()
    assert feasible == ((), ("A",), ("B",), ("A", "B"), ("B", "A")), feasible
    source_states = {run(h)[0] for h in feasible}
    source_monitor_states = {(run(h)[0], monitor(h)) for h in feasible}
    assert len(source_states) == 4
    assert len(source_monitor_states) == 5
    assert monitor(("A", "B")) == "accept"
    assert monitor(("B", "A")) == "dead"

    AB, BA = ("A", "B"), ("B", "A")
    assert completed_receipts(AB) == completed_receipts(BA)
    assert completed_receipts(AB) == {
        "source": (1, 1), "rights": (0, 0), "total_cost": (1, 1)
    }
    assert policy_bruteforce(AB) and not policy_bruteforce(BA)

    # 16 source-terminal future goal sets have identical legal suffix-relative
    # remaining cost frontiers from AB and BA, independently of past order.
    goals_checked = 0
    outputs = ((0, 0), (0, 1), (1, 0), (1, 1))
    for mask in range(16):
        goal = frozenset(v for i, v in enumerate(outputs) if mask & (1 << i))
        assert suffix_costs(AB, goal) == suffix_costs(BA, goal)
        goals_checked += 1

    # Independent direct concatenation vs finite DFA monitor.
    derivative_pairs = 0
    for h in feasible:
        for v in ((), ("A",), ("B",), ("A", "B"), ("B", "A")):
            target = run(h + v)
            brute = target is not None and policy_bruteforce(h + v)
            via_monitor = target is not None and monitor(v, monitor(h)) == "accept"
            assert brute == via_monitor, (h, v, brute, via_monitor)
            derivative_pairs += 1

    # Tests 13 distinct prefixes; the unbounded theorem is a PAPER PROOF,
    # not extrapolation from these 156 finite comparisons.
    comparisons = 0
    for n, m in itertools.product(range(13), repeat=2):
        suffix = "b" * n
        assert balanced_policy("a" * n + suffix)
        assert balanced_policy("a" * m + suffix) == (n == m)
        if n != m:
            comparisons += 1
    assert comparisons == 156

    receipt = {
        "protocol": "EVONOMOS_P42_R11_P10_P8_HISTORY_RESIDUAL_FACTORING",
        "precode_theory_sha": PRESEAL,
        "verdict": "PASS_AUTHORED_FINITE_PAST_MONITOR_AND_NONREGULAR_RESIDUAL_WITNESSES",
        "finite_source_worlds": len(source_states),
        "source_plus_past_monitor_reachable_worlds": len(source_monitor_states),
        "independent_policy_derivative_agreements": derivative_pairs,
        "all_terminal_reach_goal_subsets_checked": goals_checked,
        "same_source_rights_total_cost_AB_BA": True,
        "past_order_contract_distinguishes_AB_BA": True,
        "nonregular_policy": "a^n b^n (n >= 0)",
        "distinct_prefix_n_range_tested": [0, 12],
        "pairwise_distinguishing_ordered_prefixes": comparisons,
        "infinite_no_finite_monitor": "MATHEMATICAL_PAPER_PROOF_NOT_INFERRED_FROM_FINITE_TESTS",
        "original_go_source_G1_G7_certified": False,
        "independent_architecture_repair_prediction": "NOT_ATTEMPTED",
        "phase": "P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED",
    }
    target = Path("out/p42-r11-p10-p8/history-residual-monitor-court.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(receipt["verdict"])
    print("P8_SOURCE_4_HISTORY_PRODUCT_5_REACH_16_PAST_ORDER_SPLIT_PASS")
    print(f"P8_NONREGULAR_BALANCED_RESIDUAL_DISTINCTIONS_{comparisons}_AND_PROOF_PRESEALED_PASS")


if __name__ == "__main__":
    main()
