"""Exhaustive observation masking on the pinned R114 archive; independent path oracle."""
import copy
import hashlib
import io
import json
import sys
from collections import Counter
from pathlib import Path
from zipfile import ZipFile
from observed_bounds import receipt, bounds

SHA='852cf2d6115f747a30b329c21dafa054343d06ade8a6fd47c6ae0bcec895e220'
INF=float('inf')


def cost(option):
    return INF if option is None else option['cost']


def oracle(spec, model, goal, budget):
    def safe(s):return all(spec['snapshots'][s]['observations'][n] for n in spec['protected'])
    def target(s):return all(spec['snapshots'][s]['observations'][n] for n in spec['goals'][goal])
    def visit(u,seen,extra,c):
        if not safe(u):return INF
        if target(u):return c
        result=INF
        for a,v,o,w in model['edges']:
            if a!=u or v in seen or o not in ('app','upstream'):continue
            owners=extra|({o} if o!='app' else set())
            if len(owners)<=budget:result=min(result,visit(v,seen|{v},owners,c+w))
        return result
    return visit('base',{'base'},set(),0)


def mutate(data, name, change, refresh):
    with ZipFile(io.BytesIO(data)) as z:
        files={n:z.read(n) for n in z.namelist()}
    files[name]=change(files[name])
    if refresh:
        manifest=json.loads(files['evidence_manifest.json'])
        manifest['files'][name]=hashlib.sha256(files[name]).hexdigest()
        files['evidence_manifest.json']=json.dumps(manifest).encode()
    out=io.BytesIO()
    with ZipFile(out,'w') as z:
        for n,v in files.items():z.writestr(n,v)
    return out.getvalue()


def main(path):
    data=path.read_bytes();spec,model=receipt(data,SHA)
    def rejects(d,sha):
        try:receipt(d,sha)
        except ValueError:return
        raise AssertionError('bad receipt accepted')
    rejects(data,'0'*64)
    changed=mutate(data,'results/local.log',lambda d:d.replace(b'public_snapshot true',b'public_snapshot false'),False)
    rejects(changed,SHA);rejects(changed,hashlib.sha256(changed).hexdigest())
    changed=mutate(data,'results/local.log',lambda d:d.replace(b'public_snapshot true',b'public_snapshot false'),True)
    rejects(changed,hashlib.sha256(changed).hexdigest())
    changed=mutate(data,'results/model.json',lambda d:d.replace(b'"safe": true',b'"safe": false',1),True)
    rejects(changed,hashlib.sha256(changed).hexdigest())
    print('PASS 5 receipt rejection controls')
    keys=[(s,n) for s,r in spec['snapshots'].items() for n in r['observations']]
    original=sum(1<<i for i,(s,n) in enumerate(keys) if spec['snapshots'][s]['observations'][n])
    queries=[(g,b) for g in spec['goals'] for b in (0,1)]
    complete=copy.deepcopy(spec);partial=copy.deepcopy(spec);values=[]
    for assignment in range(1<<len(keys)):
        for i,(s,n) in enumerate(keys):complete['snapshots'][s]['observations'][n]=bool(assignment&(1<<i))
        values.append(tuple(oracle(complete,model,g,b) for g,b in queries))
    counts=Counter();by_hidden=Counter();checks=0;completions=0
    for hidden in range(1<<len(keys)):
        fixed=original&~hidden
        for i,(s,n) in enumerate(keys):partial['snapshots'][s]['observations'][n]=None if hidden&(1<<i) else bool(fixed&(1<<i))
        lows=[INF]*len(queries);highs=[-1]*len(queries);sub=hidden
        while True:
            for j,c in enumerate(values[fixed|sub]):lows[j]=min(lows[j],c);highs[j]=max(highs[j],c)
            completions+=1
            if sub==0:break
            sub=(sub-1)&hidden
        for j,(g,b) in enumerate(queries):
            r=bounds(partial,model,'base',g,['upstream'],b)
            assert (cost(r['optimistic']),cost(r['pessimistic']))==(lows[j],highs[j])
            assert r['exact_cost']==(lows[j]==highs[j])
            counts[g,b]+=r['exact_cost'];by_hidden[hidden.bit_count()]+=r['exact_cost'];checks+=1
    assert completions==3**len(keys)
    print(json.dumps({'observations':len(keys),'masks':1<<len(keys),'completions':completions,'bound_queries':checks,'exact_by_query':{f'{g}/{b}':counts[g,b] for g,b in queries},'exact_by_hidden':dict(sorted(by_hidden.items()))},sort_keys=True))
    for row in partial['snapshots'].values():row['observations']={k:False for k in row['observations']}
    for budget in (-1,True,1.5):
        try:bounds(partial,model,'base','full',['upstream'],budget)
        except ValueError:pass
        else:raise AssertionError('invalid budget accepted')
    print('PASS invalid budget even at unsafe start')


if __name__=='__main__':main(Path(sys.argv[1]))
