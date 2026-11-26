"""Decision-focused testing on the pinned R114 graph. All costs hypothetical."""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys
from zipfile import ZipFile

SHA = '852cf2d6115f747a30b329c21dafa054343d06ade8a6fd47c6ae0bcec895e220'


def load(path):
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == SHA
    with ZipFile(path) as z:
        spec = json.loads(z.read('results/manifest.json'))
        model = json.loads(z.read('results/model.json'))
    keys = [(s, k) for s, r in spec['snapshots'].items()
            for k in r['observations'] if k != 'legacy']
    assert len(keys) == 8
    actual = sum(1 << i for i, (s, k) in enumerate(keys)
                 if spec['snapshots'][s]['observations'][k])
    tests = []
    for s in spec['snapshots']:
        p = 1 << keys.index((s, 'public_snapshot'))
        n = 1 << keys.index((s, 'native_private'))
        tests.extend([(s+':public', p, 2), (s+':internal', n, 2), (s+':whole', p|n, 3)])
    return spec, model, keys, actual, tests


def evaluate(spec, model, keys, actual, tests, goal, budget, defer):
    worlds = list(range(1 << len(keys)))
    universe = (1 << len(worlds)) - 1
    actions = [('defer', defer, universe)]
    # All legacy predicates assumed true. Enumerate simple paths under fixed rights.
    def visit(u, seen, extra, cost, path):
        required = sum(1 << keys.index((u, k)) for k in spec['goals'][goal])
        feasible = sum(1 << w for w in worlds if w & required == required)
        actions.append((tuple(path), cost, feasible))
        for i, (a, v, owner, c) in enumerate(model['edges']):
            if a != u or v in seen or owner not in ('app', 'upstream'):
                continue
            used = extra | ({owner} if owner != 'app' else set())
            if len(used) <= budget:
                visit(v, seen|{v}, used, cost+c, path+[i])
    visit('base', {'base'}, set(), 0, [])
    perfect = [min(c for _, c, m in actions if m & (1 << w)) for w in worlds]
    groups = {}
    for w, c in enumerate(perfect):
        groups[c] = groups.get(c, 0) | (1 << w)
    parts = []
    for _, mask, _ in tests:
        p = {}
        for w in worlds:
            p[w&mask] = p.get(w&mask, 0) | (1 << w)
        parts.append(tuple(p.values()))

    @lru_cache(None)
    def opt(s, identify):
        n = s.bit_count()
        options = []
        for i, (_, c, m) in enumerate(actions):
            if s & ~m == 0 and (not identify or s & ~groups.get(c, 0) == 0):
                options.append((n*c, 0, 0, i))  # total, testing, action/test kind, id
        for i, (_, _, fee) in enumerate(tests):
            children = [t for m in parts[i] if (t := s&m)]
            if len(children) > 1:
                sub = [opt(t, identify) for t in children]
                options.append((n*fee+sum(r[0] for r in sub), n*fee+sum(r[1] for r in sub), 1, i))
        return min(options)

    def replay(identify):
        total = testing = 0
        actual_result = None
        for w in worlds:
            s, fee, trace = universe, 0, []
            while True:
                _, _, kind, i = opt(s, identify)
                if kind == 0:
                    name, c, m = actions[i]
                    assert s & ~m == 0 and m & (1 << w)
                    if identify:
                        assert c == perfect[w]
                    total += fee+c
                    testing += fee
                    if w == actual:
                        actual_result = {'tests': trace, 'action': name, 'test_cost': fee, 'repair_or_defer': c}
                    break
                name, _, price = tests[i]
                trace.append(name)
                fee += price
                nxt = next(s & m for m in parts[i] if m & (1 << w))
                assert nxt != s
                s = nxt
        assert (total, testing) == opt(universe, identify)[:2]
        return {'total': total, 'testing': testing, 'actual': actual_result}
    joint, identify = replay(False), replay(True)
    no_test = min(c for _, c, m in actions if m == universe)*len(worlds)
    assert joint['total'] <= min(identify['total'], no_test)
    assert identify['total'] - identify['testing'] == sum(perfect)
    opt.cache_clear()
    return {'goal':goal,'budget':budget,'defer':defer,'worlds':len(worlds),
            'joint':joint,'identify':identify,'no_test':no_test,'perfect':sum(perfect)}


def main(path):
    args = load(path)
    count=0
    for goal in ('public','full'):
        for defer in (12,40,80):
            a,b = [evaluate(*args,goal,budget,defer) for budget in (0,1)]
            assert b['joint']['total'] <= a['joint']['total']
            for row in (a,b):
                print(json.dumps(row,sort_keys=True));count+=2*row['worlds']
    print('PASS policy-world replays',count)


if __name__ == '__main__':
    main(Path(sys.argv[1]))
