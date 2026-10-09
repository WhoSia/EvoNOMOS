"""P37-MATH-J: finite checks of classical contextual kernel criteria.
Synthetic three-state source-edit graphs; not an upstream software experiment.
"""
STATES = range(3)
EDGES = [(i, j) for i in STATES for j in STATES if i != j]


def may(mask: int, accepting: set[int], start: int) -> bool:
    reachable = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        if node in accepting:
            return True
        for k, (u, v) in enumerate(EDGES):
            if (mask & (1 << k)) and u == node and v not in reachable:
                reachable.add(v)
                stack.append(v)
    return False


def signature(mask: int, accepting: set[int]) -> tuple[bool, ...]:
    return tuple(may(mask, accepting, s) for s in STATES)


def blocks(sig: tuple[bool, ...]) -> frozenset[frozenset[int]]:
    return frozenset(
        frozenset(i for i, v in enumerate(sig) if v == z) for z in set(sig)
    )


def refines(fine: frozenset, coarse: frozenset) -> bool:
    return all(any(a <= b for b in coarse) for a in fine)


def contextual_criteria() -> None:
    # Single local query: a,b indistinguishable; c distinguished.
    local = blocks((False, False, True))
    same = blocks((False, False, True))
    erase = blocks((False, False, False))
    split = blocks((False, True, True))
    # Equal kernels => sufficient AND minimal in this context.
    assert refines(local, same) and local == same
    # Local remains sufficient but needlessly distinguishes c.
    assert refines(local, erase) and local != erase
    # Context distinguishes a,b that local quotient merged.
    assert not refines(local, split)
    # Joint context family needs all three states distinguished.
    joint = frozenset(frozenset({i}) for i in STATES)
    assert all(refines(joint, p) for p in (same, split))
    assert not refines(local, joint)


def authority_expansion_exhaustive() -> tuple[int, int]:
    cases = noncomparable = 0
    full = (1 << len(EDGES)) - 1
    for base in range(1 << len(EDGES)):
        unavailable = full ^ base
        extra = unavailable
        while True:
            expanded = base | extra
            for accept_mask in range(1 << len(STATES)):
                accepts = {i for i in STATES if accept_mask & (1 << i)}
                before = signature(base, accepts)
                after = signature(expanded, accepts)
                # With I and accepting set fixed, adding edges cannot lose May.
                assert all(not a or b for a, b in zip(before, after))
                p, q = blocks(before), blocks(after)
                if not refines(p, q) and not refines(q, p):
                    noncomparable += 1
                cases += 1
            if extra == 0:
                break
            extra = (extra - 1) & unavailable
    # 3^6 pairs Γ0 ⊆ Γ1, times 2^3 demand-acceptance subsets.
    assert cases == 5832, cases
    assert noncomparable == 162, noncomparable

    # Explicit witness: Γ0 empty; Γ1 admits edit 0→2; demand accepts 2.
    edge_idx = EDGES.index((0, 2))
    assert signature(0, {2}) == (False, False, True)
    assert signature(1 << edge_idx, {2}) == (True, False, True)
    p = blocks(signature(0, {2}))
    q = blocks(signature(1 << edge_idx, {2}))
    assert not refines(p, q) and not refines(q, p)
    return cases, noncomparable


if __name__ == "__main__":
    contextual_criteria()
    count, incomparable = authority_expansion_exhaustive()
    print("P37_MATH_J_CONTEXTUAL_SUFFICIENCY_MINIMALITY_DISTINCT_PASS")
    print(f"P37_MATH_J_AUTHORITY_INCLUSION_REACHABILITY_MONOTONE_PASS cases={count}")
    print(f"P37_MATH_J_AUTHORITY_PARTITION_INCOMPARABILITY_PASS cases={incomparable}")
    print("CLASSICAL_KERNEL_CONTINUATION_AND_REACHABILITY_THEORY__NO_NEW_LAW")
