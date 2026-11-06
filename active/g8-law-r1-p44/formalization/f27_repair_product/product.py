"""F27 bounded staged repair product. Declared finite graph; NOT Go semantics."""
from dataclasses import dataclass
from heapq import heappush, heappop
from math import inf

@dataclass(frozen=True)
class Edit:
    actor: str
    cost: int
    target: str

@dataclass
class Local:
    start: str
    goals: dict
    edges: dict
    rights: frozenset
    demands: frozenset

    def validate(self):
        if self.start not in self.goals or set(self.goals)!=set(self.edges):
            raise ValueError("incomplete graph")
        if any(not g <= self.demands for g in self.goals.values()):
            raise ValueError("undeclared goal")
        for es in self.edges.values():
            for e in es:
                if e.target not in self.goals or type(e.cost)!=int or e.cost<0:
                    raise ValueError("invalid edit")

def cost(g, word):
    g.validate()
    if not set(word)<=g.demands: raise ValueError("undeclared demand")
    pq=[(0,g.start,0)]
    best={(g.start,0):0}
    while pq:
        c,s,k=heappop(pq)
        if c!=best[s,k]: continue
        if k==len(word): return c
        required=set(word[:k])
        if set(word[:k+1])<=g.goals[s]:
            state=(s,k+1)
            if c<best.get(state,inf):
                best[state]=c;heappush(pq,(c,*state))
        for e in g.edges[s]:
            if e.actor in g.rights and required<=g.goals[e.target]:
                state=(e.target,k); nc=c+e.cost
                if nc<best.get(state,inf):
                    best[state]=nc;heappush(pq,(nc,*state))
    return inf

def combine(a,b):
    a.validate();b.validate()
    if a.demands&b.demands:raise ValueError("shared demand name")
    if any("@" in s for s in a.goals) or any("@" in s for s in b.goals):
        raise ValueError("reserved state separator")
    key=lambda x,y:x+"@"+y
    goals={key(x,y):a.goals[x]|b.goals[y] for x in a.goals for y in b.goals}
    edges={}
    for x in a.goals:
        for y in b.goals:
            edges[key(x,y)]=tuple(
                [Edit(e.actor,e.cost,key(e.target,y)) for e in a.edges[x] if e.actor in a.rights]
                +[Edit(e.actor,e.cost,key(x,e.target)) for e in b.edges[y] if e.actor in b.rights])
    return Local(key(a.start,b.start),goals,edges,a.rights|b.rights,a.demands|b.demands)

def separate(a,b,word):
    if not set(word)<=a.demands|b.demands:raise ValueError("undeclared demand")
    x=cost(a,tuple(d for d in word if d in a.demands))
    y=cost(b,tuple(d for d in word if d in b.demands))
    return x+y
