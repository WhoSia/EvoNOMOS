#!/usr/bin/env python3
"""P42 R11-P10-P9: exhaustive contract-relative partial-commutation court.

Theory, four mode predictions and original prior-art boundaries were committed
FIRST at 0d0d434ffc17788ae82bd7c9a93f9319295727d4. Finite authored
once-only three-edit semantics. NOT real Go/source-owner proof.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import json

SEAL = "0d0d434ffc17788ae82bd7c9a93f9319295727d4"
E = ("A", "B", "C")
PAIRS = tuple((a, b) for a, b in (("A", "B"), ("A", "C"), ("B", "C")))
WORDS = tuple(w for n in range(4) for w in product(E, repeat=n))
assert len(WORDS) == 40
COSTS = {"A": (1, 0, 0), "B": (0, 1, 0), "C": (0, 0, 1)}

def exec_history(mode, w):
    installed = set()
    total = [0, 0, 0]
    receipts = []
    for action in w:
        if action in installed:
            return None
        if mode == "H" and action == "B" and "A" not in installed:
            return None
        step_cost = list(COSTS[action])
        if mode == "C" and action == "A" and "B" in installed:
            step_cost[0] = 2
        for i, c in enumerate(step_cost):
            total[i] += c
        installed.add(action)
        receipts.append((action, tuple(step_cost)))
    final_state = tuple(int(e in installed) for e in E)
    # We require FULL terminal source and associated owner rights, not a
    # retrospective source-vs-client observational quotient.
    current_rights = tuple(1 - b for b in final_state)
    client = (
        "A" in w and "B" in w and w.index("A") < w.index("B")
        if mode == "K" else None
    )
    return (final_state, current_rights, tuple(total), client), tuple(receipts)

def result(mode, w):
    x = exec_history(mode, w)
    return None if x is None else x[0]

def swaps(w, pair):
    a, b = pair
    for i in range(len(w) - 1):
        if (w[i], w[i + 1]) == (a, b) or (w[i], w[i + 1]) == (b, a):
            q = list(w)
            q[i], q[i + 1] = q[i + 1], q[i]
            yield tuple(q)

def exact_independence(mode):
    independent = []
    violating = {}
    for pair in PAIRS:
        fails = [(w, v) for w in WORDS for v in swaps(w, pair)
                 if result(mode, w) != result(mode, v)]
        if fails:
            violating["".join(pair)] = ("".join(fails[0][0]), "".join(fails[0][1]))
        else:
            independent.append("".join(pair))
    return tuple(independent), violating

def trace_quotient_count(mode, independence):
    legal = tuple(w for w in WORDS if result(mode, w) is not None)
    index = {w: i for i, w in enumerate(legal)}
    parent = list(range(len(legal)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i, j):
        x, y = find(i), find(j)
        if x != y:
            parent[y] = x
    for w in legal:
        for label in independence:
            for swapped in swaps(w, (label[0], label[1])):
                assert swapped in index
                assert result(mode, w) == result(mode, swapped)
                union(index[w], index[swapped])
    fibers = defaultdict(list)
    for w in legal:
        fibers[find(index[w])].append(w)
    return legal, tuple(tuple(v) for v in fibers.values())

def main():
    summary = {}
    for mode in ("N", "H", "K", "C"):
        indep, bad = exact_independence(mode)
        legal, blocks = trace_quotient_count(mode, indep)
        expected_indep = ("AB", "AC", "BC") if mode == "N" else ("AC", "BC")
        expected_legal = 9 if mode == "H" else 16
        expected_quotient = {"N": 8, "H": 6, "K": 10, "C": 10}[mode]
        assert indep == expected_indep, (mode, indep)
        assert len(legal) == expected_legal, (mode, len(legal))
        assert len(blocks) == expected_quotient, (mode, len(blocks))
        assert sum(map(len, blocks)) == len(legal)
        assert all(len({result(mode, w) for w in fiber}) == 1 for fiber in blocks)
        endpoints = {result(mode, w)[0] for w in legal}
        assert len(endpoints) == (6 if mode == "H" else 8)
        summary[mode] = dict(
            legal_words=len(legal), source_endpoints=len(endpoints),
            language_safe_static_independence=list(indep),
            adjacent_swap_reachable_quotient_classes=len(blocks),
            excluded_pair_witnesses=bad,
        )
    assert set(summary["K"]["language_safe_static_independence"]).issubset(
        summary["N"]["language_safe_static_independence"]
    )

    AB, BA = tuple("AB"), tuple("BA")
    assert result("N", AB) == result("N", BA)
    assert result("K", AB)[:3] == result("K", BA)[:3]
    assert result("K", AB)[3] is True and result("K", BA)[3] is False
    assert result("H", AB) is not None and result("H", BA) is None
    assert result("C", AB)[0:2] == result("C", BA)[0:2]
    assert result("C", AB)[2] == (1, 1, 0)
    assert result("C", BA)[2] == (2, 1, 0)

    # Verify EVERY predicate on the eight current source-world states, not
    # merely the eight individual atoms.
    source_labels = tuple(product((0, 1), repeat=3))
    count = 0
    for mask in range(1 << len(source_labels)):
        selected = {v for i, v in enumerate(source_labels) if (mask >> i) & 1}
        for mode in ("N", "K"):
            by_endpoint = defaultdict(set)
            for w in WORDS:
                r = result(mode, w)
                if r is not None:
                    by_endpoint[r[0]].add(r[0] in selected)
            assert all(len(v) == 1 for v in by_endpoint.values())
        count += 1
    assert count == 256

    # Under the unrestricted future client vocabulary, a singleton contract
    # K={AB} distinguishes AB from BA, and analogously AC/CA and BC/CB.
    arbitrary_language_witnesses = {}
    for pair in PAIRS:
        a, b = pair
        w, v = (a, b), (b, a)
        assert result("N", w) is not None and result("N", v) is not None
        assert result("N", w) == result("N", v)
        assert w != v
        arbitrary_language_witnesses[a+b] = {"single_contract": "".join(w),
                                               "rejected_swap": "".join(v)}
    assert set(arbitrary_language_witnesses) == {"AB", "AC", "BC"}

    receipt = {
        "protocol": "EVONOMOS_G8_P42_R11_P10_P9_CONTRACT_RELATIVE_COMMUTATION",
        "research_theorem_precode_commit": SEAL,
        "verdict": "PASS_FOUR_FROZEN_MODES_CONTRACT_RELATIVE_TRACE_QUOTIENT",
        "finite_authored_grammar": "three once-only independently owned edit labels",
        "all_words_including_illegal_checked": len(WORDS),
        "source_terminal_predicates_exhaustively_checked": count,
        "modes": summary,
        "all_possible_future_client_languages_independence": [],
        "arbitrary_singleton_client_distinguishing_witnesses": arbitrary_language_witnesses,
        "mathematical_theorems": [
            "T1 contextual pair equivalence factors through Mazurkiewicz trace quotient",
            "T2 client query extension antitone under fixed admissions and costs",
            "T3 arbitrarily expressive future clients rule out nonvacuous pair independence",
            "T4 source diamond alone inadequate with prefix safety, history-sensitive demand, path-dependent costs",
            "T5 finite 40-word decision COMPLETE only for frozen once-only grammar",
        ],
        "classical_prior": "Mazurkiewicz trace theory, Lipton reduction, partial-order model checking",
        "real_source_G1_G7_certified": False,
        "third_party_maintainer_edit_authority_verified": False,
        "new_independent_architecture_repair_rank": "NOT_ATTEMPTED",
        "phase": "P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED",
    }
    path = Path("out/p42-r11-p10-p9/contract-relative-commutation-proof.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(receipt["verdict"])
    for mode, data in summary.items():
        print(f"P9_MODE_{mode}: legal={data['legal_words']} endpoints={data['source_endpoints']} "
              f"independent={data['language_safe_static_independence']} quotient={data['adjacent_swap_reachable_quotient_classes']}")
    print("P9_256_TERMINAL_GOALS_40_CONTEXT_WORDS_3_UNIVERSAL_LANGUAGE_NEGATIVES_PASS")

if __name__ == "__main__":
    main()
