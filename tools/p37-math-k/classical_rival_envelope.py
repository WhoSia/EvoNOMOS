"""P37 Math-K negative-identification court over the EXISTING E4 source-tethered graph.

This deliberately reuses E4's previously tested researcher-authored finite
repair model.  Neither a new original-Go test nor all-source-patches theorem.
"""
from collections import defaultdict, Counter
from itertools import product
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
original = runpy.run_path(str(ROOT / "tools/p37-e4/model/capability_repair_graph.py"))
find = original["find"]
enabled = original["enabled"]
invariant = original["invariant"]
G, S = original["G"], original["S"]
RG, RD, RS = original["RG"], original["RD"], original["RS"]
start = (G, RG, True)
goal = (S, RS, False)


def classical_least_fixed_point(case):
    """Independent backwards EF fixpoint on the admitted owner-edit graph."""
    key_g, matching_store, bridge, expiry = case
    states = list(product((G, S), (RG, RD, RS), (True, False)))
    assert len(states) == 12
    reached = {goal} if invariant(goal, key_g, matching_store) else set()
    while True:
        previous = set(reached)
        for source in states:
            if invariant(source, key_g, matching_store) and any(
                target in previous
                for _, target in enabled(source, key_g, matching_store, bridge, expiry)
            ):
                reached.add(source)
        if reached == previous:
            return start in reached


def projections(case):
    key_g, store_s, bridge_b, expiry = case
    return {
        "source_and_present_only": (key_g,),
        "source_and_reader_capabilities": (key_g, store_s),
        "capabilities_and_bridge": (key_g, store_s, bridge_b),
        "full_classical_context": (key_g, store_s, bridge_b, expiry),
    }


def minimum_deterministic_errors(rows, name):
    """Best possible deterministic predictor using ONLY a named projection."""
    fibers = defaultdict(list)
    for case, actual in rows:
        fibers[projections(case)[name]].append(actual)
    return sum(min(v.count(False), v.count(True)) for v in fibers.values())


def run():
    rows = []
    for case in product((False, True), repeat=4):
        key_g, matching_store, bridge, expiry = case
        concrete_bfs = find(
            start, goal, key_g, matching_store,
            bridge=bridge, duty_expiry=expiry,
        )
        actual = concrete_bfs is not None
        full_classical = classical_least_fixed_point(case)
        conjunction = all(case)
        assert actual == full_classical == conjunction, (case, actual, full_classical)
        if actual:
            assert [label for label, _ in concrete_bfs] == [
                "B_authorized_dual_reader",
                "A_issuer_change",
                "EXTERNAL_expire_legacy_obligation",
                "B_remove_legacy_reader",
            ]
        rows.append((case, actual))
    assert len(rows) == 16 and sum(outcome for _, outcome in rows) == 1

    for negative in (
        (True, True, False, True),
        (True, True, True, False),
        (True, False, True, True),
    ):
        assert not dict(rows)[negative]
        assert dict(rows)[(True, True, True, True)]
        # SAME static original source, same present G observation, different
        # migration future because of excluded authority/handles/obligations.
        assert negative[0] is True

    error_counts = {
        name: minimum_deterministic_errors(rows, name)
        for name in projections((True, True, True, True))
    }
    assert error_counts == {
        "source_and_present_only": 1,
        "source_and_reader_capabilities": 1,
        "capabilities_and_bridge": 1,
        "full_classical_context": 0,
    }, error_counts

    print("P37_MATH_K_E4_REUSE_NO_NEW_GO_SOURCE_PASS")
    print("P37_MATH_K_FULL_CLASSICAL_MU_CALCULUS_EQUIVALENT_PASS cases=16 positives=1")
    print("P37_MATH_K_EXACT_BOUNDED_OWNER_OBLIGATION_CONJUNCTION_PASS")
    print("P37_MATH_K_PROJECTED_INFORMATION_INDETERMINACY_PASS min_errors=1,1,1,0")
    print("P37_MATH_K_STRONG_CLASSICAL_RIVAL_DIFFERENCE=0")
    print("P37_MATH_K_LAW_IDENTIFICATION_HOLD_NO_NEW_NATIVE_TRIAL")


if __name__ == "__main__":
    run()
