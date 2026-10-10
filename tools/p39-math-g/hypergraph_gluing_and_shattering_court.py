"""P39 Math-G: triple-permission hypergraph restriction, exact shattering,
join-tree constructive gluing, and source-prefix invariant countermodels.

Synthetic mathematics: one-shot physically commuting edits, ternary
relative order sign, no source/owner rights inferred from original Go.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import factorial


def triples(n):
    return tuple(combinations(range(n), 3))


def parity(order, triple):
    position = {v: i for i, v in enumerate(order)}
    a, b, c = triple
    return ((position[a] > position[b])
            ^ (position[a] > position[c])
            ^ (position[b] > position[c]))


def gyo_alpha(hyperedges):
    edges = [frozenset(e) for e in hyperedges]
    while edges:
        old = frozenset(edges)
        count = Counter(v for e in edges for v in e)
        edges = [frozenset(v for v in e if count[v] > 1) for e in edges]
        edges = [e for e in edges if e]
        edges = [e for i, e in enumerate(edges)
                 if not any(e <= f and (e < f or i > j)
                            for j, f in enumerate(edges) if i != j)]
        if frozenset(edges) == old:
            return False
    return True


def independent_alpha(n, hyperedges):
    # Independent test: primal graph must be chordal AND every maximal
    # primal clique must be covered by a hyperedge (hypergraph conformality).
    adj = [set() for _ in range(n)]
    for e in hyperedges:
        for a, b in combinations(e, 2):
            adj[a].add(b)
            adj[b].add(a)

    def clique(vs):
        return all(b in adj[a] for a, b in combinations(vs, 2))

    all_cliques = [frozenset(vs)
                   for k in range(1, n + 1)
                   for vs in combinations(range(n), k) if clique(vs)]
    maximal = [c for c in all_cliques
               if not any(c < d for d in all_cliques)]
    conformal = all(
        len(c) == 1 or any(c <= set(e) for e in hyperedges)
        for c in maximal
    )
    chordal = any(
        all(clique(tuple(v for v in order[i + 1:] if v in adj[u]))
            for i, u in enumerate(order))
        for order in permutations(range(n))
    )
    return conformal and chordal


def join_tree(hyperedges):
    if not hyperedges:
        return {}
    edges = [set(e) for e in hyperedges]
    tree = {i: [] for i in range(len(edges))}
    visited = {0}
    while len(visited) < len(edges):
        _, a, b = max(
            (len(edges[i] & edges[j]), i, j)
            for i in visited
            for j in range(len(edges)) if j not in visited
        )
        tree[a].append(b)
        tree[b].append(a)
        visited.add(b)
    for v in set().union(*edges):
        members = {i for i, e in enumerate(edges) if v in e}
        reached = set()
        stack = [min(members)]
        while stack:
            i = stack.pop()
            if i in reached:
                continue
            reached.add(i)
            stack.extend(j for j in tree[i] if j in members and j not in reached)
        assert reached == members, (v, edges, tree)
    return tree


def merge_local(global_order, local):
    old = set(global_order)
    local_old = [v for v in local if v in old]
    current = list(global_order)
    block = []
    for v in local:
        if v in old:
            for x in block:
                current.insert(current.index(v), x)
            block = []
        else:
            block.append(v)
    if block:
        if local_old:
            k = current.index(local_old[-1]) + 1
            current[k:k] = block
        else:
            current.extend(block)
    assert [v for v in current if v in old] == global_order
    assert [v for v in current if v in set(local)] == list(local)
    return current


def construct_tree_witness(n, hyperedges, signs):
    if not hyperedges:
        return tuple(range(n))
    tree = join_tree(hyperedges)
    root = next(p for p in permutations(hyperedges[0])
                if parity(p, hyperedges[0]) == signs[0])
    order = list(root)
    processed = {0}
    def dfs(parent, node):
        nonlocal order
        previous = set(order)
        shared = previous & set(hyperedges[node])
        # Running-intersection condition says old vars shared here
        # occur in the parent scope.
        assert shared == set(hyperedges[parent]) & set(hyperedges[node])
        local = next(perm for perm in permutations(hyperedges[node])
                     if parity(perm, hyperedges[node]) == signs[node]
                     and tuple(x for x in perm if x in shared)
                     == tuple(x for x in order if x in shared))
        order = merge_local(order, local)
        processed.add(node)
        for child in tree[node]:
            if child != parent:
                dfs(node, child)
    for child in tree[0]:
        dfs(0, child)
    for v in range(n):
        if v not in order:
            order.append(v)
    assert len(set(order)) == n
    assert all(parity(order, t) == s for t, s in zip(hyperedges, signs))
    return tuple(order)


def exhaustive_restriction_court():
    for n, expected in (
        (3, (2, 0, 0)),
        (4, (11, 0, 5)),
        (5, (126, 40, 858)),
    ):
        ts = triples(n)
        reps = [(0,) + p for p in permutations(range(1, n))]
        rows = [tuple(int(parity(p, t)) for t in ts) for p in reps]
        counts = Counter()
        constructive = 0
        for mask in range(1 << len(ts)):
            indices = [i for i in range(len(ts)) if mask >> i & 1]
            H = tuple(ts[i] for i in indices)
            alpha = gyo_alpha(H)
            assert alpha == independent_alpha(n, H)
            realized = {tuple(row[i] for i in indices) for row in rows}
            all_realizable = len(realized) == (1 << len(H))
            assert not alpha or all_realizable, (H, realized)
            if alpha:
                for y in product((0, 1), repeat=len(H)):
                    construct_tree_witness(n, H, y)
                    constructive += 1
            counts[("alpha" if alpha else
                    "nonalpha_fully_independent" if all_realizable
                    else "nonalpha_restricted")] += 1
        result = tuple(counts[x] for x in (
            "alpha", "nonalpha_fully_independent", "nonalpha_restricted"))
        assert result == expected, (n, result)
        print(f"P39_G_HYPERGRAPH_CENSUS n={n} total={sum(result)} "
              f"alpha={result[0]} cyclic_shattered={result[1]} "
              f"cyclic_nonshattered={result[2]} "
              f"join_tree_witnesses={constructive} PASS")


def invariant_coupling_court():
    H = ((0, 1, 2), (0, 1, 3))
    P = ((0, 2), (1, 2), (0, 3), (1, 3))
    assert gyo_alpha(H)
    assert gyo_alpha(H + P)  # binary source guards lie in triple scopes
    accepted = [p for p in permutations(range(4))
                if all(p.index(a) < p.index(b) for a, b in P)]
    assert len(accepted) == 4
    profiles = {tuple(int(parity(p, t)) for t in H) for p in accepted}
    assert profiles == {(0, 0), (1, 1)}, profiles
    # Both owners can independently accept 0 and 1 under P,
    # but opposite owner requirements cannot be glued.
    assert all({x[i] for x in profiles} == {0, 1} for i in (0, 1))
    assert (0, 1) not in profiles
    assert (1, 0) not in profiles
    print("P39_G_COMBINED_ALPHA_PREFIX_INVARIANT_JOINT_FAILURE "
          "individual_signs=2_each joint_profiles=2_of_4 "
          "separator=(0,1)_opposite_order PASS")


def orientation_shattering_court():
    examples = {
        3: ((0, 1, 2),),
        4: ((0, 1, 2), (0, 1, 3)),
        5: ((0, 1, 2), (0, 1, 3), (0, 1, 4), (2, 3, 4)),
        6: ((0, 1, 2), (0, 1, 3), (0, 4, 5),
            (1, 4, 5), (2, 3, 4), (2, 3, 5)),
    }
    for n, H in examples.items():
        reps = [(0,) + p for p in permutations(range(1, n))]
        profiles = {
            tuple(int(parity(order, t)) for t in H): order
            for order in reps
        }
        assert len(profiles) == 2 ** len(H)
        # Cyclic orders (n-1)! bound ALL possible profiles.
        assert 2 ** len(H) <= factorial(n - 1) < 2 ** (len(H) + 1)
        for y in product((0, 1), repeat=len(H)):
            assert y in profiles
            assert all(int(parity(profiles[y], t)) == s
                       for t, s in zip(H, y))
        print(f"P39_G_SHATTER_CAPACITY n={n} "
              f"max_triplet_questions={len(H)} "
              f"profiles={len(profiles)} cyclic_order_cap={factorial(n-1)} "
              f"hypergraph_alpha={gyo_alpha(H)} PASS")


if __name__ == "__main__":
    exhaustive_restriction_court()
    invariant_coupling_court()
    orientation_shattering_court()
    print("P39_MATH_G_ALL_SYNTHETIC_THEORY_CHECKS_PASS_NO_ORIGINAL_GO")
