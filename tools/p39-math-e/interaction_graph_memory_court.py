"""P39-MATH-E: exact graph-to-source-future-rights memory court.

Mathematical synthetic source edit model only:
- graph vertices: one-shot commuting source modifications
- graph edges: *only* order-sensitive future owner authorization queries
- all source edit permutations legal and yield identical complete source
- distinguishability uses every edge-specific future query, not one aggregate.

Independent algorithms:
(1) orientation masks induced by all edit permutations,
(2) topological-sort acyclicity over all 2^m edge directions,
(3) Whitney spanning-subgraph sum for (-1)^n * chromatic(-1).
Finite verification ≠ native Go evidence, formal proof assistant or novel law.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial


def universe(n):
    return tuple(combinations(range(n), 2))


def graph_edges(n, mask):
    return tuple(e for i, e in enumerate(universe(n)) if mask & (1 << i))


def from_edit_orders(n, edges):
    masks = set()
    for order in permutations(range(n)):
        rank = {v: i for i, v in enumerate(order)}
        masks.add(sum((1 << k) for k, (u, v) in enumerate(edges)
                      if rank[u] < rank[v]))
    return len(masks)


def orientation_is_acyclic(n, edges, orientation):
    indeg = [0] * n
    outgoing = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if not (orientation & (1 << i)):
            u, v = v, u
        outgoing[u].append(v)
        indeg[v] += 1
    q = [i for i in range(n) if indeg[i] == 0]
    count = 0
    while q:
        u = q.pop()
        count += 1
        for v in outgoing[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return count == n


def from_independent_orientations(n, edges):
    return sum(orientation_is_acyclic(n, edges, mask)
               for mask in range(1 << len(edges)))


def stanley_via_whitney(n, edges):
    # chi_G(t) = sum_{A subset E} (-1)^|A| t^{components(V,A)}
    # signed value (-1)^n chi_G(-1).
    result = 0
    for mask in range(1 << len(edges)):
        parent = list(range(n))

        def root(a):
            while parent[a] != a:
                a = parent[a]
            return a

        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                parent[root(u)] = root(v)
        components = len({root(v) for v in range(n)})
        result += (-1) ** (n + mask.bit_count() + components)
    return result


def chordal_earlier_clique_factor(n, edges):
    ed = {tuple(sorted(x)) for x in edges}
    for order in permutations(range(n)):
        previous = []
        prod = 1
        valid = True
        for v in order:
            earlier = [u for u in previous if tuple(sorted((u, v))) in ed]
            if any(tuple(sorted((x, y))) not in ed
                   for x, y in combinations(earlier, 2)):
                valid = False
                break
            prod *= 1 + len(earlier)
            previous.append(v)
        if valid:
            return prod
    return None


def exact_small_graph_court():
    total = 0
    chordal = 0
    by_order = Counter()
    chordal_order = Counter()
    for n in range(1, 6):
        for mask in range(1 << len(universe(n))):
            edges = graph_edges(n, mask)
            a = from_edit_orders(n, edges)
            b = from_independent_orientations(n, edges)
            c = stanley_via_whitney(n, edges)
            assert a == b == c, (n, mask, edges, a, b, c)
            d = chordal_earlier_clique_factor(n, edges)
            if d is not None:
                assert d == a, (n, mask, a, d)
                chordal += 1
                chordal_order[n] += 1
            by_order[n] += 1
            total += 1
        print(
            f"P39_MATH_E_ALL_SIMPLE_GRAPHS n={n} "
            f"verified={by_order[n]} chordal={chordal_order[n]} "
            "permutation=orientation=chromatic PASS"
        )
    assert total == 1099
    assert chordal == 894
    print("P39_MATH_E_TOTAL_GRAPHS=1099_CHORDAL_GRAPHS=894_PASS")


def graph_families():
    for n in range(1, 9):
        families = {
            "path_tree": tuple((i, i + 1) for i in range(n - 1)),
            "complete": tuple(combinations(range(n), 2)),
            "matching": tuple((2 * i, 2 * i + 1) for i in range(n // 2)),
        }
        if n >= 3:
            families["cycle"] = (
                tuple((i, i + 1) for i in range(n - 1))
                + ((0, n - 1),)
            )
        for name, edges in families.items():
            v = from_edit_orders(n, edges)
            expected = {
                "path_tree": 2 ** (n - 1),
                "complete": factorial(n),
                "matching": 2 ** (n // 2),
                "cycle": 2 ** n - 2,
            }[name]
            assert v == expected
            mem = (v - 1).bit_length()
            if n in (4, 5, 8):
                print(
                    f"P39_MATH_E_FAMILY n={n} type={name} "
                    f"rights_residuals={v} min_extra_bits={mem} PASS"
                )

    # Equal numbers of edits (vertices) and interaction edges do not
    # determine the rounded optimal memory:
    dense_one = ((0,1),(0,2),(0,3),(0,4),(1,2),(1,3))
    dense_two = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
    assert len(dense_one) == len(dense_two) == 6
    assert from_edit_orders(5, dense_one) == 36
    assert from_edit_orders(5, dense_two) == 24
    assert (36-1).bit_length() == 6
    assert (24-1).bit_length() == 5
    print("P39_MATH_E_SAME_N_M_DIFFERENT_MIN_MEMORY n=5 m=6 bits=6_vs_5 PASS")
    print("P39_MATH_E_FOREST_TREEWIDTH1_HAS_UNBOUNDED_LINEAR_MEMORY n_minus_1")


if __name__ == "__main__":
    exact_small_graph_court()
    graph_families()
    print("P39_MATH_E_STANLEY1973_LINIAL1986_CLASSICAL_NOVELTY_HOLD")
    print("P39_MATH_E_NO_ORIGINAL_GO_NO_HOSTED_CI_CLAIM")
