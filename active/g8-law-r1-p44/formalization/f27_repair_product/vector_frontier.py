"""Bounded vector-cost path frontier for a finite declared edit graph."""
from collections import deque
from dataclasses import dataclass
@dataclass(frozen=True)
class Move:
    actor:str
    prices:tuple
    dest:str

def attainable(start, goals, edges, rights, demands, word, caps):
    if not caps or any(v<0 for v in caps) or not set(word)<=demands:
        raise ValueError("bad declarations")
    if set(goals)!=set(edges) or start not in goals:
        raise ValueError("incomplete graph")
    queue=deque([(start,0,(0,)*len(caps))])
    seen=set(queue);out=set()
    while queue:
        s,k,c=queue.popleft()
        if k==len(word):
            out.add(c);continue
        nxt=[]
        if set(word[:k+1])<=goals[s]:
            nxt.append((s,k+1,c))
        for e in edges[s]:
            if e.actor not in rights:continue
            if e.dest not in goals or len(e.prices)!=len(caps) or any(v<0 for v in e.prices):
                raise ValueError("invalid vector edge")
            if not set(word[:k])<=goals[e.dest]:continue
            price=tuple(x+y for x,y in zip(c,e.prices))
            if all(x<=lim for x,lim in zip(price,caps)):
                nxt.append((e.dest,k,price))
        for v in nxt:
            if v not in seen:seen.add(v);queue.append(v)
    return out

def pareto(costs):
    return frozenset(c for c in costs if not any(
        d!=c and all(x<=y for x,y in zip(d,c)) for d in costs))
