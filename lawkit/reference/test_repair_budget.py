"""Compare bounded A*, lifted Dijkstra and the exact maximal-subset baseline."""
from itertools import combinations
import heapq
import json
import platform
import random
import statistics
import sys
import time
from repair_budget import best
from repair_frontier import graph
from repair_permissions import options
from test_repair_permissions import fixture
from benchmark_permissions import stress


def cost(row):
    return None if row is None else row['cost']


def subset(model, start, goal, names, budget):
    names = sorted(set(names)-set(model['allowed_owners']))
    bits = {n:1<<i for i,n in enumerate(names)}
    states, adj, _ = graph({**model,'allowed_owners':model['allowed_owners']+names})
    adj = {u:[(v,c,i,bits.get(model['edges'][i][2],0)) for v,c,i in edges] for u,edges in adj.items()}
    answer = None
    for group in combinations(names,min(budget,len(names))):
        mask = sum(bits[n] for n in group)
        q,d,parent = [(0,start)],{start:0},{}
        while q:
            c,u = heapq.heappop(q)
            if d[u]!=c: continue
            if answer is not None and c>=answer['cost']: break
            if goal in states[u]['goals']:
                path=[]
                while u!=start:
                    u,i=parent[u];path.append(i)
                path.reverse()
                extra=sorted({model['edges'][i][2] for i in path}-set(model['allowed_owners']))
                answer={'cost':c,'additional_owners':extra,'edges':path}
                break
            for v,w,i,b in adj[u]:
                if b&mask==b and c+w<d.get(v,float('inf')):
                    d[v]=c+w;parent[v]=(u,i);heapq.heappush(q,(c+w,v))
    return answer


def checked(model,start,goal,names,budget,row):
    if row is None: return None
    u,c,used=start,0,set()
    for i in row['edges']:
        a,b,o,w=model['edges'][i]
        assert a==u and model['states'][b]['safe']
        u,c=b,c+w;used.add(o)
    used-=set(model['allowed_owners'])
    assert goal in model['states'][u]['goals'] and c==row['cost']
    assert used==set(row['additional_owners'])<=set(names) and len(used)<=budget
    return c


def test():
    queries=0
    for seed in range(180):
        m,names=fixture(4+seed%12,seed%6,seed)
        rows=options(m,'0','g',names)
        for b in range(len(names)+2):
            expected=min((r['cost'] for r in rows if len(r['additional_owners'])<=b),default=None)
            for row in (best(m,'0','g',names,b),best(m,'0','g',names,b,heuristic=False),subset(m,'0','g',names,b)):
                assert checked(m,'0','g',names,b,row)==expected
            queries+=1
    for k in (0,1,4,8):
        m,names=stress(k)
        for b in range(k+2):
            assert cost(best(m,'0','g',names,b))==2*k-min(k,b)
    m,names=stress(2)
    assert best(m,'0','absent',names,2) is None
    assert cost(best(m,'2','g',names,0))==0
    for invalid in (-1,True,1.5):
        try: best(m,'0','g',names,invalid)
        except ValueError: pass
        else: raise AssertionError('invalid budget accepted')
    print(f'PASS {queries} random budget queries across 180 graphs, 3 implementations; boundary checks PASS')


def bench():
    print(json.dumps({'python':platform.python_version(),'platform':platform.platform(),'repeats':7,'timing':'graph preparation, search, witness validation; no JSON IO'}))
    rng=random.Random(113)
    cases=[('random-128-8',fixture(128,8,112),b) for b in (0,2,4,8)]
    cases += [('antichain-12',stress(12),b) for b in (2,6,12)]
    for label,(m,names),b in cases:
        funcs={'subset':lambda:subset(m,'0','g',names,b),'dijkstra':lambda:best(m,'0','g',names,b,heuristic=False),'astar':lambda:best(m,'0','g',names,b)}
        expected=cost(funcs['subset']());times={k:[] for k in funcs}
        for _ in range(7):
            order=list(funcs);rng.shuffle(order)
            for k in order:
                t=time.perf_counter_ns();row=funcs[k]();got=checked(m,'0','g',names,b,row);elapsed=time.perf_counter_ns()-t
                assert got==expected;times[k].append(elapsed)
        print(json.dumps({'case':label,'budget':b,'cost':expected,'raw_ns':times,'median_ns':{k:statistics.median(v) for k,v in times.items()}}))


if __name__=='__main__':
    test()
    if '--bench' in sys.argv: bench()
