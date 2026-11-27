"""Finite synthetic audit: joint repair feasibility, not a source experiment."""
from itertools import product, combinations
from collections import Counter
from pathlib import Path
import json


def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n - 1):
        yield p + ((n - 1,),)
        for j in range(len(p)):
            yield p[:j] + (p[j] + (n - 1,),) + p[j + 1:]


def intersection(menus, group):
    result = 7
    for i in group:
        result &= menus[i]
    return result


def min_partition(menus, ps, pairwise=False):
    def compatible(group):
        if pairwise:
            return all(menus[i] & menus[j] for i, j in combinations(group, 2))
        return bool(intersection(menus, group))
    return min(len(p) for p in ps if all(compatible(g) for g in p))


def min_cover(menus):
    # Independently enumerate action subsets; each world needs at least one.
    return min(mask.bit_count() for mask in range(1, 8) if all(mask & m for m in menus))


def main():
    rows = []
    for n in range(1, 5):
        ps = tuple(partitions(n))
        counts = Counter()
        witnesses = []
        for menus in product(range(1, 8), repeat=n):
            exact = min_partition(menus, ps)
            pair = min_partition(menus, ps, pairwise=True)
            cover = min_cover(menus)
            assert pair <= exact == cover
            counts[(pair, exact, cover)] += 1
            if pair < exact and len(witnesses) < 5:
                witnesses.append({'menus': menus, 'pair': pair, 'exact': exact})
        rows.append({'worlds': n, 'cases': 7**n, 'partition_count': len(ps),
                     'counts': [{'pair':p,'exact':e,'cover':c,'count':k} for (p,e,c),k in sorted(counts.items())],
                     'pairwise_failures': sum(k for (p,e,c),k in counts.items() if p<e),
                     'cover_failures': sum(k for (p,e,c),k in counts.items() if e!=c),
                     'witnesses': witnesses})
    witness = (3, 6, 5)
    assert min_partition(witness, tuple(partitions(3)), True) == 1
    assert min_cover(witness) == 2
    result = {'action_encoding': {'a':1,'b':2,'c':4}, 'rows': rows,
              'total':sum(r['cases'] for r in rows),
              'pairwise_failures':sum(r['pairwise_failures'] for r in rows),
              'cover_failures':sum(r['cover_failures'] for r in rows)}
    Path('result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
