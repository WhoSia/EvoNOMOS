"""P37-MATH-L finite information and computational-budget identifiability court.

Only reuses the existing E4 original-API-tethered RESEARCH-AUTHORED
source-repair model. Additional graph-oracle worlds are wholly synthetic.
No new original Go source test. No newly identified beyond-classical law.
"""
from fractions import Fraction
from itertools import product, permutations
from functools import lru_cache
from pathlib import Path
import runpy

BITS = ("matching_scs_store", "authorized_B_dual_reader", "external_legacy_expiry")
WORLDS = tuple(product((False, True), repeat=3))


def e4_truth():
    """Outcomes come from the existing source-tethered E4 restricted repair graph."""
    root = Path(__file__).resolve().parents[2]
    e4 = runpy.run_path(str(root / "tools/p37-e4/model/capability_repair_graph.py"))
    start = (e4["G"], e4["RG"], True)
    goal = (e4["S"], e4["RS"], False)
    outcomes = {}
    for x in WORLDS:
        store, bridge, expiry = x
        actual = e4["find"](
            start, goal, True, store, bridge=bridge, duty_expiry=expiry
        ) is not None
        assert actual == all(x), x
        outcomes[x] = actual
    assert sum(outcomes.values()) == 1
    return outcomes


def remaining(observed):
    return tuple(x for x in WORLDS if all(x[j] == v for j, v in observed))


def certificate(observed, outcomes):
    answers = {outcomes[x] for x in remaining(observed)}
    return next(iter(answers)) if len(answers) == 1 else None


def minimax_depth(outcomes):
    """Strongest exact classical adaptive tree, under identical bit-query oracle."""
    @lru_cache(None)
    def depth(observed):
        if certificate(observed, outcomes) is not None:
            return 0
        unused = [i for i in range(3) if i not in dict(observed)]
        return 1 + min(
            max(
                depth(tuple(sorted(observed + ((i, v),))))
                for v in (False, True)
            )
            for i in unused
        )
    return depth(())


def judge(world, budget, order, outcomes):
    """Judge sees only queried bits, never directly receives the entire world."""
    observed = ()
    queries = 0
    for i in order[:budget]:
        if certificate(observed, outcomes) is not None:
            break
        observed = tuple(sorted(observed + ((i, world[i]),)))
        queries += 1
    return certificate(observed, outcomes), queries


def weighted_expected_cost(order, probabilities, costs):
    """Independent synthetic probabilities, arbitrary accounting units."""
    expected = Fraction(0)
    for world in WORLDS:
        weight = Fraction(1)
        for i, value in enumerate(world):
            weight *= probabilities[i] if value else 1 - probabilities[i]
        expense = 0
        for i in order:
            expense += costs[i]
            if not world[i]:
                break
        expected += weight * expense
    return expected


def graph_oracle_adversary():
    """Budget-B graph probes cannot distinguish B-prefix-identical worlds.

    Only the just-discovered node handle may be queried. The (B+1)-th
    expansion differs: one graph reaches a goal, the other dead-ends.
    These are synthetic graphs, not genuine Go edit graphs.
    """
    checked = 0
    for budget in range(9):
        def successor(node, has_goal):
            if node < budget:
                return node + 1
            if node == budget:
                return "GOAL" if has_goal else None
            return None

        for has_goal in (False, True):
            node = 0
            transcript = []
            for _ in range(budget):
                assert node != "GOAL"
                nxt = successor(node, has_goal)
                transcript.append((node, nxt))
                node = nxt
            assert transcript == [(i, i + 1) for i in range(budget)]
            assert successor(node, has_goal) == (
                "GOAL" if has_goal else None
            )
            checked += 1
    assert checked == 18
    return checked


def run():
    outcomes = e4_truth()
    assert minimax_depth(outcomes) == 3
    assert sum(outcomes.values()) == 1

    examined = 0
    for order in permutations(range(3)):
        for budget in range(4):
            unknown = 0
            for world in WORLDS:
                value, queries = judge(world, budget, order, outcomes)
                assert queries <= budget
                if value is None:
                    unknown += 1
                else:
                    assert value == outcomes[world]
                examined += 1
            assert unknown == (
                2 ** (3 - budget) if budget < 3 else 0
            ), (order, budget, unknown)
    assert examined == 6 * 4 * 8 == 192

    # All-positive world must be undecidable at every smaller budget.
    # Uniform 0-1 error lower bound for any budget <3 is 1/8,
    # achieved by the classic always-negative classifier.
    for budget in (0, 1, 2):
        assert judge((True, True, True), budget, (0, 1, 2), outcomes)[0] is None
    assert judge((True, True, True), 3, (0, 1, 2), outcomes)[0] is True
    assert sum(not v for v in outcomes.values()) == 7

    # Synthetic p/c are not measured probabilities or deployment cost.
    p = (Fraction(3, 4), Fraction(1, 2), Fraction(1, 4))
    c = (4, 1, 2)
    candidates = {
        order: weighted_expected_cost(order, p, c)
        for order in permutations(range(3))
    }
    best = min(candidates, key=candidates.get)
    assert best == (1, 2, 0) and candidates[best] == Fraction(5, 2)
    assert candidates[(0, 1, 2)] == Fraction(11, 2)
    assert all(value >= candidates[best] for value in candidates.values())

    # This order is also the classical optimal stochastic AND test order.
    classical_order = tuple(sorted(
        range(3),
        key=lambda i: Fraction(c[i], 1) / (1 - p[i]),
    ))
    assert classical_order == best

    graph_cases = graph_oracle_adversary()
    print("P37_MATH_L_ORIGINAL_E4_REUSE_VALID_START_8_CONTEXTS_PASS")
    print("P37_MATH_L_INFORMATION_ORACLE_MINIMAX_DEPTH=3")
    print("P37_MATH_L_UNIFORM_CERTIFYING_QUERY_AUDIT_PASS worlds=192")
    print("P37_MATH_L_BUDGET_2_SELECTIVE_ABSTENTION=2_OF_8")
    print("P37_MATH_L_BUDGET_LT_3_HARD_CLASSIFIER_MIN_ERRORS=1_OF_8")
    print("P37_MATH_L_CLASSICAL_COST_OPTIMAL_ORDER=bridge,expiry,store expected=5/2 naive=11/2")
    print(f"P37_MATH_L_SYNTHETIC_GRAPH_ORACLE_DEPTH_OBSTRUCTION_PASS cases={graph_cases}")
    print("P37_MATH_L_EVO_VS_STRONG_CLASSICAL_PREDICTION_DIFFERENCE=0")
    print("P37_MATH_L_NO_NEW_NATIVE_GO_EXPERIMENT_LAW_IDENTIFICATION_HOLD")


if __name__ == "__main__":
    run()
