"""Finite synthetic R99: joint repair/transfer messages under public observations.
Four worlds, two repair IDs, two disjoint strict participation intervals.
Bit 2*r+s denotes an admissible (repair r, transfer-sign s) action.
No empirical costs or source-native claim.
"""
from itertools import product
from collections import Counter

N = 4
INF = 5
MASKS = tuple(a | b for a in (0,1,2) for b in (0,4,8))

def partitions(n):
    def extend(labels):
        if len(labels) == n:
            yield tuple(sum(1 << i for i,x in enumerate(labels) if x == j)
                        for j in range(max(labels)+1))
        else:
            for j in range(max(labels)+2):
                yield from extend(labels+[j])
    yield from extend([0])

def common(worlds, cell):
    ans = 15
    for i,mask in enumerate(worlds):
        if cell >> i & 1:
            ans &= mask
    return ans

def minimum_menu(cells):
    # Exhaustive menu search; empty feasible cell yields INF.
    return min((m.bit_count() for m in range(1,16)
                if all(m & cell for cell in cells)), default=INF)

def oracle(cells):
    # Independent direct enumeration of deterministic cell-to-action policies.
    return min((len(set(p)) for p in product(*[
        tuple(i for i in range(4) if mask >> i & 1) for mask in cells])), default=INF)

def transfer_only(mask):
    return (mask & 3) | (mask >> 2)

def transfer_relaxation(cells):
    return min((m.bit_count() for m in range(1,4)
                if all(m & cell for cell in cells)), default=INF)

def refines(fine, coarse):
    return all(any(f & c == f for c in coarse) for f in fine)

def main():
    ps = tuple(partitions(N))
    assert len(ps) == 15
    pairs = [(i,j) for i,f in enumerate(ps) for j,c in enumerate(ps) if refines(f,c)]
    counts = Counter()
    for worlds in product(MASKS, repeat=N):
        answers = []
        for p in ps:
            cells = tuple(common(worlds,c) for c in p)
            v = minimum_menu(cells)
            assert v == oracle(cells)
            counts['oracle_checks'] += 1
            # Optimistic relaxation: project each world's repair IDs away first.
            projected = tuple(common(tuple(map(transfer_only,worlds)),c) & 3 for c in p)
            lower = transfer_relaxation(projected)
            assert lower <= v
            counts['strict_projection_gaps'] += lower < v
            counts['false_feasible'] += lower < INF and v == INF
            answers.append(v)
        for i,j in pairs:
            assert answers[i] <= answers[j]
            counts['refinement_checks'] += 1
    # Same transfer works, but no common repair can be selected under coarse observation.
    assert minimum_menu((common((1,4),(1|2)),)) == INF
    assert transfer_relaxation((1,)) == 1
    # With full disclosure the two different repairs require two joint messages.
    assert minimum_menu((1,4)) == 2
    print(dict(world_assignments=len(MASKS)**N, partitions=len(ps), **counts))

if __name__ == '__main__':
    main()
