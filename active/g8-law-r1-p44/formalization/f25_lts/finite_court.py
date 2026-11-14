"""A tiny finite complete labelled edit-LTS court. NOT Go-source soundness."""
from dataclasses import dataclass
from typing import Dict, Tuple

Label = Tuple[str, str, int]
Edge = Tuple[Label, str]

@dataclass(frozen=True)
class Graph:
    observation: Dict[str, str]
    transitions: Dict[str, Tuple[Edge, ...]]

    def validate(self):
        states = set(self.observation)
        if set(self.transitions) != states:
            raise ValueError("incomplete transition table")
        for edges in self.transitions.values():
            for ((actor, demand, cost), target) in edges:
                if not actor or not demand or not isinstance(cost, int) or cost < 0:
                    raise ValueError("invalid labelled edit")
                if target not in states:
                    raise ValueError("unknown target")

def largest_cost_labelled_bisimulation(a: Graph, b: Graph):
    """Greatest finite fixed point, matching exact actor/demand/cost and observer."""
    a.validate(); b.validate()
    relation = {(p,q) for p in a.observation for q in b.observation
                if a.observation[p] == b.observation[q]}
    while True:
        smaller=set()
        for p,q in relation:
            left,right=a.transitions[p],b.transitions[q]
            if all(any(label==olabel and (dest,odest) in relation
                       for olabel,odest in right) for label,dest in left) and all(
                   any(label==olabel and (odest,dest) in relation
                       for olabel,odest in left) for label,dest in right):
                smaller.add((p,q))
        if smaller==relation:
            return relation
        relation=smaller

def trace_language(graph: Graph, start: str, horizon: int):
    graph.validate()
    seen={(start,())}
    frontier=[(start,())]
    for _ in range(horizon):
        upcoming=[]
        for p,word in frontier:
            for label,dest in graph.transitions[p]:
                node=(dest,word+(label,))
                if node not in seen:
                    seen.add(node);upcoming.append(node)
        frontier=upcoming
    return {word for _,word in seen}

def shortest_repair(graph: Graph, start: str, actor: str, demand: str):
    """Demo min cost to first matching *edge*, NOT preserved sequential demand."""
    graph.validate()
    import heapq
    pq=[(0,start)];dist={start:0};best=None
    while pq:
        price,state=heapq.heappop(pq)
        if price!=dist[state]:continue
        for (edge_actor,edge_demand,edge_cost),target in graph.transitions[state]:
            next_price=price+edge_cost
            if edge_actor==actor and edge_demand==demand:
                best=next_price if best is None else min(best,next_price)
            if next_price<dist.get(target,float("inf")):
                dist[target]=next_price
                heapq.heappush(pq,(next_price,target))
    return best

def branch_countermodels():
    la=("maintainer","a",1);lb=("maintainer","b",1);lc=("maintainer","c",1)
    a=Graph({"s":"ok","branch":"ok","z":"ok"},
            {"s":((la,"branch"),),"branch":((lb,"z"),(lc,"z")),"z":()})
    b=Graph({"s":"ok","left":"ok","right":"ok","z":"ok"},
            {"s":((la,"left"),(la,"right")),"left":((lb,"z"),),
             "right":((lc,"z"),),"z":()})
    return a,b

def rights_countermodel():
    edge=(("owner","extend",1),"target")
    a=Graph({"s":"old_client_ok","target":"old_client_ok"},
            {"s":(edge,),"target":()})
    b=Graph({"s":"old_client_ok","target":"old_client_ok"},
            {"s":(),"target":()})
    return a,b
