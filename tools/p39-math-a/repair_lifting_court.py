"""P39 Math-A: finite structural theorems and counterexamples.

Source-edge transition systems and option sets here are SYNTHETIC MATH.
No native Go, no third-party source test and no beyond-classical law claim.
"""
from itertools import product

S = ("a", "b", "g")
T = ("u", "v")
P = {"a": "u", "b": "u", "g": "v"}


def edges(nodes, bitmap):
    possible = list(product(nodes, repeat=2))
    return {(x, y) for i, (x, y) in enumerate(possible)
            if bitmap & (1 << i)}


def may(nodes, graph, goal):
    reached = {goal}
    while True:
        new = reached | {x for x, y in graph if y in reached}
        if new == reached:
            return reached
        reached = new


def forth(src, dst):
    return all((P[x], P[y]) in dst for x, y in src)


def back(src, dst):
    return all(
        any((x, y) in src and P[y] == v for y in S)
        for x in S for u, v in dst if P[x] == u
    )


def lifting_court():
    checked = 0
    p_morphisms = 0
    current_equivalent_future_different = 0
    for smask in range(1 << (len(S)**2)):
        src = edges(S, smask)
        concrete = may(S, src, "g")
        if ("a" in concrete) != ("b" in concrete):
            current_equivalent_future_different += 1
        for tmask in range(1 << (len(T)**2)):
            dst = edges(T, tmask)
            abstract = may(T, dst, "v")
            if forth(src, dst) and back(src, dst):
                p_morphisms += 1
                assert all(
                    (x in concrete) == (P[x] in abstract) for x in S
                ), (smask, tmask)
            checked += 1
    assert checked == 8192
    assert p_morphisms == 160
    assert current_equivalent_future_different == 128

    # a and b implement exactly the same OLD operational observation,
    # but differ under external authorized SOURCE edits.
    witness = {("a", "g")}
    assert "a" in may(S, witness, "g")
    assert "b" not in may(S, witness, "g")
    return checked, p_morphisms, current_equivalent_future_different


def owner_option_court():
    universe = (0, 1, 2)
    all_sets = [
        {v for v in universe if mask & (1 << v)}
        for mask in range(1, 8)
    ]
    bad = [
        (a, b, c)
        for a, b, c in product(all_sets, repeat=3)
        if (a & b) and (a & c) and (b & c) and not (a & b & c)
    ]
    assert len(bad) == 6
    assert any(
        a == {0, 1} and b == {1, 2} and c == {0, 2}
        for a, b, c in bad
    )

    # Connected subtrees of the path 0--1--2.
    intervals = [
        {0}, {1}, {2}, {0, 1}, {1, 2}, {0, 1, 2}
    ]
    for a, b, c in product(intervals, repeat=3):
        if (a & b) and (a & c) and (b & c):
            assert a & b & c
    return len(bad), len(intervals) ** 3


def main():
    cases, p_morphisms, different = lifting_court()
    bad, connected_checks = owner_option_court()
    print(f"P39_MATH_A_SOURCE_ABSTRACT_GRAPH_PAIRS={cases}")
    print(f"P39_MATH_A_CLASSICAL_P_MORPHISM_FUTURE_LIFT_PASS cases={p_morphisms}")
    print(f"P39_MATH_A_LSP_OLD_EQ_FUTURE_MAY_DIFF_PASS source_graphs={different}")
    print(f"P39_MATH_A_OWNER_PAIRWISE_NOT_GLOBAL_PASS triples={bad}")
    print(f"P39_MATH_A_CONNECTED_TREE_HELLY_PASS triples={connected_checks}")
    print("P39_MATH_A_NO_ORIGINAL_GO_CLASSICAL_TRANSPORT_DIP49_HOLD")


if __name__ == "__main__":
    main()
