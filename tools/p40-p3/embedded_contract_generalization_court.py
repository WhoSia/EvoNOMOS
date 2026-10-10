"""P40-P3: 9-context guarded three-architecture theorem, original embedding rights.

Original Go compiler witnesses from embedded_promotion_collision_court.py:
original Composite{Fast; Other} calling Other.Next fails after adding Fast.Next.
With wrapped FastAdapter, source Fast is not modified and old Composite survives.
Owner rights are explicitly synthetic, not actual maintainer approvals.
"""
from collections import Counter, deque
from itertools import product

ARCHES = ("coupled", "direct", "versioned_adapter")


def safe(arch, legacy_protected, embedded_old_client, t, x, f):
    if embedded_old_client and x and arch != "versioned_adapter":
        return False
    if arch == "coupled" and t and (not x or legacy_protected):
        return False
    if f and not (t and x):
        return False
    return True


def reachable(arch, ctx):
    p, f, m, w, L, q, t_first, atomic, e = ctx
    allow_x = w if arch == "versioned_adapter" else m
    visited = {(0, 0, 0)}
    queue = deque(visited)
    while queue:
        t, x, F = queue.popleft()
        if (t, x, F) == (1, 1, 1) and not (q and arch == "versioned_adapter"):
            return True
        nxt = []
        if p and not t:
            nxt.append((1, x, F))
        if allow_x and not x and (t or not t_first):
            nxt.append((t, 1, F))
        if f and not F:
            nxt.append((t, x, 1))
        # Atomic source edit still needs contract and concrete-edit permission.
        if atomic and p and allow_x and not t and not x and not F:
            nxt.append((1, 1, 0))
        for state in nxt:
            if state not in visited and safe(arch, L, e, *state):
                visited.add(state)
                queue.append(state)
    return False


def theorem(arch, ctx):
    p, f, m, w, L, q, t_first, atomic, e = ctx
    if arch == "coupled":
        return bool(p and f and m and not L and not e and (not t_first or atomic))
    if arch == "direct":
        return bool(p and f and m and not e)
    return bool(p and f and w and not q)


def main():
    counts = Counter()
    feasible = 0
    for ctx in product((False, True), repeat=9):
        result = []
        for arch in ARCHES:
            observed = reachable(arch, ctx)
            calculated = theorem(arch, ctx)
            assert observed == calculated, (arch, ctx, observed, calculated)
            feasible += observed
            result.append(observed)
        counts[tuple(result)] += 1
    assert sum(counts.values()) == 512 and feasible == 76, (counts, feasible)
    assert dict(counts) == {
        (False, False, False): 456,
        (False, False, True): 24,
        (False, True, False): 15,
        (False, True, True): 5,
        (True, True, False): 9,
        (True, True, True): 3,
    }, counts
    for profile in sorted(counts):
        print(f"P40_P3_EMBEDDING_512_CONTEXTS profile={tuple(int(x) for x in profile)} count={counts[profile]}")
    print("P40_P3_EMBEDDING_1536_BFS_EQUALS_NECESSARY_SUFFICIENT_FORMULA PASS")
    cases = {
        "direct_wrapper_baseline": ((1,1,1,1,1,0,0,0,0), (0,1,1)),
        "same_rights_embedding_wrapper_only": ((1,1,1,1,1,0,0,0,1), (0,0,1)),
        "embedding_plus_nominal_no_solution": ((1,1,1,1,1,1,0,0,1), (0,0,0)),
        "fast_edit_forbidden_wrapper_only": ((1,1,0,1,1,0,0,0,0), (0,0,1)),
        "wrapper_forbidden_direct_only": ((1,1,1,0,1,0,0,0,0), (0,1,0)),
    }
    for label, (bits, goal) in cases.items():
        got = tuple(int(reachable(a, tuple(bool(v) for v in bits))) for a in ARCHES)
        assert got == goal, (label, got, goal)
        print(f"P40_P3_EMBEDDING_CONTEXT_REVERSAL {label} C_D_W={got} PASS")
    print("P40_P3_EMBEDDING_OLD_CLIENT_SOURCE_GLUING_OBSTRUCTION_CLASSICAL_PASS")


if __name__ == "__main__":
    main()
