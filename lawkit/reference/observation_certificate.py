"""Enumerate minimal sufficient observation sets for the bounded Chi example."""
from itertools import combinations
import json
from pathlib import Path
import sys
from observed_bounds import bounds, receipt
from test_observed_bounds import SHA


def main(path):
    spec,model=receipt(path.read_bytes(),SHA)
    keys=[(s,n) for s,row in spec['snapshots'].items() for n in row['observations']]
    original=[spec['snapshots'][s]['observations'][n] for s,n in keys]
    queries=[(g,b) for g in spec['goals'] for b in (0,1)]
    minimal={q:[] for q in queries+[('joint',0)]}
    for k in range(len(keys)+1):
        for ids in combinations(range(len(keys)),k):
            known=set(ids)
            for i,(s,n) in enumerate(keys):
                spec['snapshots'][s]['observations'][n]=original[i] if i in known else None
            flags=[bounds(spec,model,'base',g,['upstream'],b)['exact_cost'] for g,b in queries]
            for q,flag in zip(queries+[('joint',0)],flags+[all(flags)]):
                if flag and not any(old<=known for old in minimal[q]):
                    minimal[q].append(known)
    expected=[(1,4),(1,5),(2,2),(4,7),(1,9)]
    assert [(len(v),min(map(len,v))) for v in minimal.values()]==expected
    for (g,b),sets in minimal.items():
        print(json.dumps({'query':g,'budget':b,'minimum_size':min(map(len,sets)),
            'certificates':[[f'{keys[i][0]}:{keys[i][1]}' for i in sorted(s)] for s in sets]}))


if __name__=='__main__':main(Path(sys.argv[1]))
