"""Prefix safety over source snapshots, not a live deployment or migration."""
from collections import deque
from itertools import combinations
import importlib.util
import json
from pathlib import Path
from source_factors import pinned,extract
from factor_worlds import WORLDS,materialize,predict,expected
from factor_native import observe
from factor_run import normalized

START=(True,False,'raw')
GOAL=(True,True,'normalized')
LABELS=('capture','whitelist','accessor')

def protected(case,cycle): return case[2]!='adapter' or cycle==0

def graph(safe,rights):
    return {w:[v for v in safe if (diff:=[i for i in range(3) if w[i]!=v[i]]) and len(diff)==1 and diff[0] in rights] for w in safe}

def paths(edges,start,goal):
    queue=deque([(start,)])
    shortest=None; found=[]
    while queue:
        p=queue.popleft()
        if shortest is not None and len(p)>shortest: break
        if p[-1]==goal:
            shortest=len(p);found.append(p);continue
        queue.extend(p+(v,) for v in edges.get(p[-1],[]) if v not in p)
    return found

def main():
    root=Path(importlib.util.find_spec('requests').origin).parent
    base=pinned(root);ref=observe(root,base)
    native=[];model=[];goal=[];world_rows=[]
    for world in WORLDS:
        src=materialize(base,world);factors=extract(src);rows=observe(root,src)
        np=mp=all_bad=legacy=0
        for row,old in zip(rows,ref,strict=True):
            case,cycle,value,*legacy_values=row;assert row[:2]==old[:2]
            n=normalized(value)!=expected(case);m=predict(factors,case,cycle)!=expected(case)
            np+=protected(case,cycle) and n;mp+=protected(case,cycle) and m
            all_bad+=n;legacy+=legacy_values!=old[3:]
        assert legacy==0
        if not np: native.append(world)
        if not mp: model.append(world)
        if not all_bad: goal.append(world)
        world_rows.append({'world':world,'protected_failures':np,'model_protected_failures':mp})
    assert native==model and goal==[GOAL]
    scenarios=[]
    for k in range(4):
        for rights in combinations(range(3),k):
            a=paths(graph(native,rights),START,GOAL);b=paths(graph(model,rights),START,GOAL)
            assert a==b
            scenarios.append({'rights':[LABELS[i] for i in rights],'distance':len(a[0])-1 if a else None,'shortest_orders':len(a),'paths':a})
    assert paths(graph(native,range(3)),START,GOAL)==[(START,(True,False,'normalized'),GOAL)]
    assert not paths(graph(native,(1,)),START,GOAL)
    assert not paths(graph(native,(2,)),START,GOAL)
    print(json.dumps({'safe_worlds':native,'goal_worlds':goal,'world_rows':world_rows,'scenarios':scenarios,'scope':'snapshot safety; no actual cross-version migration; null distance means unreachable in declared grammar'},indent=2))

if __name__=='__main__': main()
