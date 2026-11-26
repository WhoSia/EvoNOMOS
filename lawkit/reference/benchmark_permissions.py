"""Single-parse subset baseline versus certified path options, repeated interleaved runs."""
import heapq
import json
import platform
import random
import statistics
import time
from repair_frontier import graph
from repair_permissions import options
from test_repair_permissions import checked, fixture, oracle, test


def cached_oracle(model, start, goal, candidates):
    names = sorted(set(candidates)-set(model['allowed_owners']))
    bits = {name:1<<i for i,name in enumerate(names)}
    states, adj, _ = graph({**model,'allowed_owners':model['allowed_owners']+names})
    adj = {u:[(v,c,bits.get(model['edges'][i][2],0)) for v,c,i in edges] for u,edges in adj.items()}
    rows=[]
    for mask in range(1<<len(names)):
        q,d=[(0,start)],{start:0}
        while q:
            c,u=heapq.heappop(q)
            if d[u]!=c:continue
            if goal in states[u]['goals']:
                rows.append((mask,c));break
            for v,w,b in adj[u]:
                if b&mask==b and c+w<d.get(v,float('inf')):
                    d[v]=c+w;heapq.heappush(q,(c+w,v))
    return {(frozenset(n for n in names if mask&bits[n]),c) for mask,c in rows
            if not any(m&mask==m and d<=c and (m,d)!=(mask,c) for m,d in rows)}


def stress(k):
    # At each stage one can pay a high cost or use a distinct additional owner.
    # Every subset is nondominated: each extra owner saves one unit.
    names=[f'o{i}' for i in range(k)]
    states={str(i):{'safe':True,'goals':['g'] if i==k else []} for i in range(k+1)}
    edges=[]
    for i,n in enumerate(names):edges.extend([[str(i),str(i+1),'app',2],[str(i),str(i+1),n,1]])
    return {'states':states,'allowed_owners':['app'],'edges':edges},names


def main():
    test()
    for seed in range(80):
        m,names=fixture(4+seed%12,seed%5,seed)
        assert cached_oracle(m,'0','g',names)==oracle(m,'0','g',names)==checked(m,'0','g',names)
    print('PASS 80 cached-oracle cross-checks')
    print(json.dumps({'python':platform.python_version(),'platform':platform.platform(),'repeats':7,'timing':'both include graph preparation, pareto includes path witness validation, no IO'}))
    rng=random.Random(112)
    cases=[(f'random-{n}-{k}',fixture(n,k,112)) for n,k in ((64,2),(64,4),(128,6),(128,8))]
    cases += [(f'antichain-{k}',stress(k)) for k in (4,8)]
    for label,(m,names) in cases:
        expected=oracle(m,'0','g',names)
        if label.startswith('antichain'):assert len(expected)==1<<len(names)
        fs={'cached_subset':lambda:cached_oracle(m,'0','g',names),'pareto':lambda:checked(m,'0','g',names)}
        times={key:[] for key in fs}
        for _ in range(7):
            order=list(fs);rng.shuffle(order)
            for key in order:
                t=time.perf_counter_ns();got=fs[key]();dt=time.perf_counter_ns()-t
                assert got==expected;times[key].append(dt)
        record = {'case':label,'states':len(m['states']),'owners':len(names)}
        record.update(options=len(expected), raw_ns=times)
        record['median_ns'] = {key:statistics.median(v) for key,v in times.items()}
        print(json.dumps(record))


if __name__=='__main__':
    main()
