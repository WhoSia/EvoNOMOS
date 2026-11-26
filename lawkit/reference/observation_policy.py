"""Exact finite test policies and greedy cross-class cutting (uniform worlds)."""
from functools import lru_cache
import json
from pathlib import Path
import sys
from observed_bounds import receipt
from test_observed_bounds import SHA, oracle


def partition(mask, worlds):
    groups = {}
    for i, w in enumerate(worlds):
        k = w & mask
        groups[k] = groups.get(k, 0) | 1 << i
    return tuple(groups.values())


def solve(worlds, labels, tests, actual):
    # Each test: (name, revealed bitmask, positive integer cost).
    if not worlds or len(set(worlds)) != len(worlds) or len(labels) != len(worlds) or actual not in worlds:
        raise ValueError('invalid worlds or labels')
    if any(mask <= 0 or type(c) is not int or c <= 0 for _, mask, c in tests):
        raise ValueError('invalid test')
    all_worlds = (1 << len(worlds)) - 1
    classes = {}
    for i, label in enumerate(labels):
        classes[label] = classes.get(label, 0) | 1 << i
    parts = [partition(mask, worlds) for _, mask, _ in tests]

    @lru_cache(None)
    def counts(w):
        return tuple(n for m in classes.values() if (n := (m & w).bit_count()))

    def children(w, i):
        return tuple(x for m in parts[i] if (x := m & w))

    def impurity(w):
        n = w.bit_count()
        return (n*n - sum(k*k for k in counts(w))) // 2

    @lru_cache(None)
    def optimal(w, worst):
        if len(counts(w)) == 1:
            return 0, 0, -1
        n = w.bit_count()
        options = []
        for i, (_, _, c) in enumerate(tests):
            cs = children(w, i)
            if len(cs) == 1:
                continue
            results = [optimal(v, worst) for v in cs]
            total = c*n + sum(r[0] for r in results)
            maximum = c + max(r[1] for r in results)
            options.append((total, maximum, i))
        if not options:
            raise ValueError('tests cannot distinguish target classes')
        return min(options, key=lambda r:(r[1],r[0],r[2]) if worst else r)

    @lru_cache(None)
    def greedy(w):
        if len(counts(w)) == 1:
            return -1
        n = w.bit_count()
        scores = []
        for i, (_, _, c) in enumerate(tests):
            cs = children(w,i)
            if len(cs) > 1:
                # Uniform conditional expected cut of cross-class pairs / cost.
                score = (n*impurity(w)-sum(v.bit_count()*impurity(v) for v in cs))/(n*c)
                scores.append((score,-i))
        if not scores:
            raise ValueError('tests cannot distinguish target classes')
        return -max(scores)[1]

    def replay(choose):
        costs=[]; actual_path=[]
        for j,world in enumerate(worlds):
            w=all_worlds;c=0;path=[]
            while len(counts(w))>1:
                i=choose(w,c);name,_,fee=tests[i]
                nxt=next(v for v in children(w,i) if v & (1<<j))
                assert nxt!=w
                w=nxt;c+=fee;path.append(name)
            assert w & (1<<j) and w & ~classes[labels[j]]==0
            costs.append(c)
            if world==actual: actual_path=path
        return {'total':sum(costs),'worst':max(costs),'actual_cost':costs[worlds.index(actual)],'actual_tests':actual_path}

    # Exact fixed panel: its union of observations must separate every class.
    panels={0:(0,())}
    for i,(_,mask,c) in enumerate(tests):
        for seen,(cost,ids) in list(panels.items()):
            new=seen|mask;candidate=(cost+c,ids+(i,))
            if new not in panels or candidate<panels[new]:panels[new]=candidate
    def sufficient(mask):
        seen={}
        for w,label in zip(worlds,labels):
            x=w&mask
            if x in seen and seen[x]!=label:return False
            seen[x]=label
        return True
    fixed=min((cost,ids) for mask,(cost,ids) in panels.items() if sufficient(mask))
    result={'worlds':len(worlds),'classes':len(classes),'fixed_cost':fixed[0],
            'fixed_tests':[tests[i][0] for i in fixed[1]]}
    for name,choose in [('expected',lambda w,c:optimal(w,False)[2]),('minimax',lambda w,c:optimal(w,True)[2]),('greedy',lambda w,c:greedy(w))]:
        result[name]=replay(choose)
    for name,worst in [('expected',False),('minimax',True)]:
        assert optimal(all_worlds,worst)[:2]==(result[name]['total'],result[name]['worst'])
    assert result['expected']['total']<=result['greedy']['total']
    assert result['minimax']['worst']<=result['greedy']['worst']
    assert result['minimax']['worst']<=fixed[0]
    # Exact expected cost subject to a hard per-world budget, not a weighted-sum proxy.
    @lru_cache(None)
    def capped(w, remaining):
        if len(counts(w)) == 1:
            return 0, -1
        if remaining < optimal(w, True)[1]:
            return float('inf'), -1
        n = w.bit_count()
        options = []
        for i, (_, _, c) in enumerate(tests):
            cs = children(w, i)
            if len(cs) > 1 and c <= remaining:
                total = c*n + sum(capped(v, remaining-c)[0] for v in cs)
                options.append((total, i))
        return min(options, default=(float('inf'), -1))

    result['capped'] = []
    if len(tests) > 8:
        for cap in range(result['minimax']['worst'], result['expected']['worst']+1):
            total, first = capped(all_worlds, cap)
            assert result['expected']['total'] <= total <= result['minimax']['total']
            verified=replay(lambda w,c:capped(w,cap-c)[1])
            assert verified['total']==total and verified['worst']<=cap
            result['capped'].append({'cap':cap,**verified})
        assert result['capped'][-1]['total']==result['expected']['total']
        assert all(a['total']>=b['total'] for a,b in zip(result['capped'],result['capped'][1:]))
    capped.cache_clear()
    result['dp_cache']=optimal.cache_info().currsize
    optimal.cache_clear();counts.cache_clear();greedy.cache_clear()
    return result


def main(path):
    spec,model=receipt(path.read_bytes(),SHA)
    keys=[(s,n) for s,row in spec['snapshots'].items() for n in row['observations']]
    actual=sum(1<<i for i,(s,n) in enumerate(keys) if spec['snapshots'][s]['observations'][n])
    worlds=list(range(1<<len(keys)));labels=[]
    for w in worlds:
        for i,(s,n) in enumerate(keys):spec['snapshots'][s]['observations'][n]=bool(w&(1<<i))
        labels.append(tuple(oracle(spec,model,g,b) for g in spec['goals'] for b in (0,1)))
    whole=[];split=[]
    for s in spec['snapshots']:
        public=1<<keys.index((s,'public_snapshot'))
        internal=(1<<keys.index((s,'legacy')))|(1<<keys.index((s,'native_private')))
        whole.append((s+':whole',public|internal,3))
        split.extend([(s+':public',public,2),(s+':internal',internal,2)])
    for name,tests in [('whole',whole),('split',split),('combined',whole+split)]:
        print(json.dumps({'menu':name,**solve(worlds,labels,tests,actual)}),flush=True)
    # Restricted hypothetical world family: legacy holds everywhere.
    ids=[i for i,(s,n) in enumerate(keys) if n=='legacy'];mask=sum(1<<i for i in ids)
    restricted=[w for w in worlds if w&mask==mask]
    print(json.dumps({'menu':'combined_legacy_true',**solve(restricted,[labels[w] for w in restricted],whole+split,actual)}),flush=True)


if __name__=='__main__':main(Path(sys.argv[1]))
