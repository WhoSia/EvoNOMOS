"""Subset oracle, witness validation, and interleaved cost/authority benchmark."""
import heapq
import json
import random
import statistics
import sys
import time
from repair_permissions import options
from repair_frontier import graph


def oracle(model, start, goal, candidates):
    names = sorted(set(candidates)-set(model['allowed_owners']))
    results = []
    for mask in range(1 << len(names)):
        extra = frozenset(n for i,n in enumerate(names) if mask & (1<<i))
        states, adj, _ = graph({**model, 'allowed_owners': model['allowed_owners']+sorted(extra)})
        q, d = [(0,start)], {start:0}
        while q:
            c,u = heapq.heappop(q)
            if d[u]!=c: continue
            if goal in states[u]['goals']:
                results.append((extra,c));break
            for v,w,_ in adj[u]:
                if c+w<d.get(v,float('inf')):
                    d[v]=c+w;heapq.heappush(q,(c+w,v))
    return {(s,c) for s,c in results if not any(t<=s and d<=c and (t,d)!=(s,c) for t,d in results)}


def checked(model, start, goal, names):
    rows=options(model,start,goal,names)
    result=set()
    for row in rows:
        u,c,extra=start,0,set()
        for i in row['edges']:
            a,b,o,w=model['edges'][i]
            assert a==u and model['states'][b]['safe']
            u,c=b,c+w
            if o not in model['allowed_owners']: extra.add(o)
        assert goal in model['states'][u]['goals'] and extra==set(row['additional_owners'])<=set(names) and c==row['cost']
        result.add((frozenset(extra),c))
    assert len(result)==len(rows)
    return result


def fixture(n,k,seed):
    rng=random.Random(seed);names=[f'o{i}' for i in range(k)]
    states={str(i):{'safe':i in (0,n-1) or rng.random()>.1,'goals':['g'] if i==n-1 else []} for i in range(n)}
    edges=[[str(rng.randrange(n)),str(rng.randrange(n)),rng.choice(['app']*2+names+['excluded']),rng.randint(1,12)] for _ in range(5*n)]
    return {'states':states,'allowed_owners':['app'],'edges':edges},names


def test():
    model={'states':{'s':{'safe':True,'goals':[]},'g':{'safe':True,'goals':['g']},'bad':{'safe':False,'goals':[]}},'allowed_owners':['app'],'edges':[['s','g','app',9],['s','g','a',4],['s','g','b',2],['s','bad','app',1],['bad','g','app',1],['s','g','excluded',1]]}
    assert checked(model,'s','g',['a','b'])=={(frozenset(),9),(frozenset({'a'}),4),(frozenset({'b'}),2)}
    assert checked(model,'g','g',['a'])=={(frozenset(),0)}
    assert checked(model,'s','missing',['a'])==set()
    for seed in range(160):
        m,names=fixture(4+seed%12,seed%5,seed)
        assert checked(m,'0','g',names)==oracle(m,'0','g',names)
    print('PASS 160 random graphs + 3 explicit boundary cases')


def bench():
    rng=random.Random(112)
    for n,k in ((64,2),(64,4),(128,6),(128,8)):
        m,names=fixture(n,k,112)
        fs={'subset':lambda:oracle(m,'0','g',names),'pareto':lambda:checked(m,'0','g',names)}
        expected=fs['subset']();assert fs['pareto']()==expected
        times={key:[] for key in fs}
        for _ in range(7):
            order=list(fs);rng.shuffle(order)
            for key in order:
                t=time.perf_counter_ns();got=fs[key]();dt=time.perf_counter_ns()-t
                assert got==expected;times[key].append(dt)
        print(json.dumps({'states':n,'candidate_owners':k,'edges':len(m['edges']),'options':len(expected),'raw_ns':times,'medians_ns':{key:statistics.median(vals) for key,vals in times.items()}}))


if __name__=='__main__':
    test()
    if '--bench' in sys.argv: bench()
