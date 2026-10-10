"""P39-MATH-C: synthetic monotone source-edit minimal-obstruction court.

No native Go or third-party tests. Every edit added once; a state is a
subset of named edit events. Exhaustive only in the declared finite models.
"""
from itertools import permutations, combinations


def internal_prefixes(order):
    value = 0
    for event in order[:-1]:
        value |= 1 << event
        yield value


def blocks_all(n, forbidden):
    return all(
        any(s in forbidden for s in internal_prefixes(order))
        for order in permutations(range(n))
    )


def directed_cube_min_cut():
    result = []
    for n in (2, 3, 4):
        vertices = range(1, (1 << n) - 1)
        checked = 0
        for k in range(n):
            for cut in combinations(vertices, k):
                assert not blocks_all(n, set(cut)), (n, cut)
                checked += 1
        minimum_cuts = []
        for cut in combinations(vertices, n):
            if blocks_all(n, set(cut)):
                minimum_cuts.append(cut)
            checked += 1
        assert tuple(1 << x for x in range(n)) in minimum_cuts
        result.append((n, len(minimum_cuts), checked))
        print(f"P39_MATH_C_HYPERCUBE_MIN_CUT n={n} cut_size={n} minimal_cuts={len(minimum_cuts)} checked={checked}")
    assert result == [(2, 1, 4), (3, 2, 42), (4, 2, 1471)], result


def owner_order_cut():
    # Two initially admissible owner edits a,b, then c requires both.
    # All states are safe except the shared prerequisite checkpoint {a,b}.
    ideals = {0, 1, 2, 3, 7}
    valid_orders = [
        order for order in permutations(range(3))
        if all(prefix in ideals for prefix in internal_prefixes(order))
    ]
    assert valid_orders == [(0, 1, 2), (1, 0, 2)]
    assert all(3 in set(internal_prefixes(order)) for order in valid_orders)
    assert not (3 in {0, 1, 2, 7})
    print("P39_MATH_C_OWNER_PRECEDENCE_CUT_COLLAPSE cut_size=1 legal_orders=2")


def accessible(family, n):
    return all(
        x == 0 or any(
            x & (1 << i) and (x ^ (1 << i)) in family
            for i in range(n)
        )
        for x in family
    )


def union_closed(family):
    return all((x | y) in family for x in family for y in family)


def extension(family, n, x, y):
    target = x | y
    seen = {x}
    stack = [x]
    while stack:
        state = stack.pop()
        if state == target:
            return True
        for bit in range(n):
            nxt = state | (1 << bit)
            if (
                nxt != state and nxt in family
                and nxt & target == nxt and nxt not in seen
            ):
                stack.append(nxt)
                seen.add(nxt)
    return False


def robust_union_extension(family, n):
    return all(
        extension(family, n, x, y)
        for x in family for y in family
    )


def antimatroid_theorem_court():
    for n, expected_accessible, expected_anti in (
        (2, 7, 6), (3, 82, 35)
    ):
        count = 0
        anti = 0
        nonempty = tuple(range(1, 1 << n))
        for mask in range(1 << len(nonempty)):
            family = {0} | {
                state for i, state in enumerate(nonempty)
                if mask & (1 << i)
            }
            if not accessible(family, n):
                continue
            count += 1
            union = union_closed(family)
            assert robust_union_extension(family, n) == union
            anti += union
        assert (count, anti) == (expected_accessible, expected_anti)
        print(f"P39_MATH_C_ANTIMATROID_CLASSICAL_EQUIV n={n} accessible={count} antimatroids={anti}")

    # Future repair survives some edit orders but not all admissible first edits.
    family = {0, 1, 2, 4, 3, 7}
    assert accessible(family, 3) and not union_closed(family)
    assert extension(family, 3, 0, 7)
    assert not extension(family, 3, 4, 7)
    print("P39_MATH_C_SAFE_FIRST_EDIT_CAN_STRAND_EXISTING_FUTURE_GOAL")

    no_access = {0, 3}
    assert union_closed(no_access) and not accessible(no_access, 2)
    assert not extension(no_access, 2, 0, 3)
    print("P39_MATH_C_ACCESSIBILITY_IS_NECESSARY")


if __name__ == "__main__":
    directed_cube_min_cut()
    owner_order_cut()
    antimatroid_theorem_court()
    print("P39_MATH_C_FINITE_COURT_PASS_CLASSICAL_MENGER_POSET_ANTIMATROID_CSP")
    print("P39_MATH_C_NO_NEW_GO_OR_NOVEL_THEOREM_ASSERTION_DIP49_HOLD")
