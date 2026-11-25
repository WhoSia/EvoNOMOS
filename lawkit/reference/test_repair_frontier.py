"""Independent Bellman-Ford oracle and end-to-end batch benchmark."""
import argparse
import heapq
import json
import platform
import random
import statistics
import time
import unittest
from copy import deepcopy
from pathlib import Path

from repair_frontier import graph, frontier, verify


def oracle(model, goal):
    safe = {s for s, row in model['states'].items() if row['safe']}
    d = {s: 0 if goal in model['states'][s]['goals'] else float('inf') for s in safe}
    for _ in range(len(safe)):
        old = d.copy()
        for u, v, owner, c in model['edges']:
            if u in safe and v in safe and owner in model['allowed_owners']:
                d[u] = min(d[u], c+old[v])
        if d == old:
            break
    return {s: None if x == float('inf') else x for s,x in d.items()}


def repeated_forward(parsed, goal):
    states, forward, _ = parsed
    targets = {s for s in forward if goal in states[s]['goals']}
    result = {}
    for start in forward:
        d, queue = {start: 0}, [(0, start)]
        result[start] = None
        while queue:
            cost, u = heapq.heappop(queue)
            if cost != d[u]:
                continue
            if u in targets:
                result[start] = cost
                break
            for v,c,_ in forward[u]:
                alt = cost+c
                if v not in d or alt < d[v]:
                    d[v] = alt
                    heapq.heappush(queue,(alt,v))
    return result


def random_model(n, seed):
    rng = random.Random(seed)
    names = [str(i) for i in range(n)]
    return {'states': {s: {'safe': rng.random() > .08, 'goals': ['g'] if rng.random() < .12 else []} for s in names},
            'allowed_owners': ['app'],
            'edges': [[rng.choice(names),rng.choice(names),rng.choice(['app','app','outside']),rng.randint(1,9)] for _ in range(5*n)]}


def chi_graph():
    # Recorded P42 finite grammar, not execution of Chi source.
    states, edges = {}, []
    for z in range(3):
        for t in range(32):
            u = str(t+32*z)
            states[u] = {'safe': True, 'goals': [g for g,yes in [('CD',t&12==12),('EC',bool(t&4) and z==1),('FD',bool(t&8) and z==2)] if yes]}
            for bit in range(5):
                if not t & (1<<bit):
                    edges.append([u,str((t|(1<<bit))+32*z),'app',1])
            if z==0:
                edges.extend([[u,str(t+32),'app',1],[u,str(t+64),'app',1]])
    return {'states':states,'allowed_owners':['app'],'edges':edges}


class Checks(unittest.TestCase):
    def test_examples(self):
        model = json.loads((Path(__file__).parent.parent/'fixtures/repair_frontier_example.json').read_text())
        p = graph(model)
        r = frontier(p,'feature')
        self.assertEqual(r['start']['cost'],5)
        self.assertIsNone(r['blocked']['cost'])
        self.assertNotIn('broken',r)
        self.assertTrue(verify(p,'feature',r))
        for s,change in [('start',{'cost':1,'next_edge':2}),('local',{'cost':None,'next_edge':None}),('done',{'cost':1,'next_edge':None})]:
            bad=deepcopy(r);bad[s]=change
            with self.assertRaises(ValueError):verify(p,'feature',bad)
        model['edges'][0][3]=0
        with self.assertRaises(ValueError):graph(model)

    def test_random(self):
        checks=0
        for seed in range(300):
            model=random_model(2+seed%19,seed)
            p=graph(model);r=frontier(p,'g')
            self.assertTrue(verify(p,'g',r))
            self.assertEqual({s:v['cost'] for s,v in r.items()},oracle(model,'g'))
            checks+=len(r)
        print('random graphs=300 safe-state checks='+str(checks))

    def test_chi(self):
        p=graph(chi_graph())
        for goal in ('CD','EC','FD','EF'):
            r=frontier(p,goal);self.assertTrue(verify(p,goal,r))
            for s,row in r.items():
                t,z=int(s)%32,int(s)//32
                want={'CD':int(not t&4)+int(not t&8),'EC':None if z==2 else int(not t&4)+int(z==0),'FD':None if z==1 else int(not t&8)+int(z==0),'EF':None}[goal]
                self.assertEqual(row['cost'],want)
        print('historical graph states=96 goal checks=384 (no native Chi run)')


def benchmark():
    print(json.dumps({'python':platform.python_version(),'platform':platform.platform(),'repeats':7,'timing':'parse/filter once per call; baseline costs only, candidate costs+witness+verify; no JSON IO'}))
    rng=random.Random(111)
    rare = random_model(512,111)
    for state in rare['states'].values():
        state['goals'] = []
    next(state for state in rare['states'].values() if state['safe'])['goals'] = ['g']
    cases = [('P42',chi_graph(),'EC')]+[(str(n),random_model(n,111),'g') for n in (128,512,2048)]
    cases += [('rare-512',rare,'g'),('absent-512',rare,'absent')]
    for label,model,goal in cases:
        def baseline():return repeated_forward(graph(model),goal)
        def candidate():
            p=graph(model);r=frontier(p,goal);verify(p,goal,r);return {s:v['cost'] for s,v in r.items()}
        expected=baseline();assert candidate()==expected
        times={'baseline':[],'candidate':[]}
        for _ in range(7):
            pairs=[('baseline',baseline),('candidate',candidate)];rng.shuffle(pairs)
            for name,fn in pairs:
                start=time.perf_counter_ns();got=fn();elapsed=time.perf_counter_ns()-start
                assert got==expected;times[name].append(elapsed)
        print(json.dumps({'case':label,'states':len(model['states']),'safe_states':len(expected),'edges':len(model['edges']),'raw_ns':times,'median_ns':{k:statistics.median(v) for k,v in times.items()}}))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--bench',action='store_true');args=parser.parse_args()
    if args.bench:benchmark()
    else:unittest.main(argv=[__file__],verbosity=2)
