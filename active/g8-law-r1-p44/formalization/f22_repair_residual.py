"""Bounded illustrative repair-right-language countermodel, not Go source proof."""
from heapq import heappush, heappop
from math import inf

A = {"s": ("a","b"), "a": ("ab",), "b": ("ab",), "ab": ()}
B = {"s": ("a","b"), "a": (), "b": ()}
SAT = {"s": frozenset(), "a": frozenset({"a"}), "b": frozenset({"b"}), "ab": frozenset({"a","b"})}

def min_cost(graph, start, goals):
    queue, dist = [(0,start)], {start: 0}
    while queue:
        cost, state = heappop(queue)
        if cost != dist[state]: continue
        if goals <= SAT[state]: return cost
        for nxt in graph[state]:
            nc = cost+1
            if nc < dist.get(nxt,inf):
                dist[nxt]=nc
                heappush(queue,(nc,nxt))
    return inf

def staged(graph, demands):
    # Demand at stage k is enabled only after reaching a satisfying state;
    # previously accepted demands remain protected at every edit prefix.
    queue=[(0,"s",0)]
    dist={("s",0): 0}
    while queue:
        cost,state,k=heappop(queue)
        if cost != dist[state,k]: continue
        if k==len(demands):return cost
        required=frozenset(demands[:k])
        goal=frozenset(demands[:k+1])
        if goal <= SAT[state]:
            key=(state,k+1)
            if cost<dist.get(key,inf):
                dist[key]=cost
                heappush(queue,(cost,*key))
        for nxt in graph[state]:
            if required <= SAT[nxt]:
                key=(nxt,k)
                if cost+1 < dist.get(key,inf):
                    dist[key]=cost+1
                    heappush(queue,(cost+1,*key))
    return inf

if __name__ == "__main__":
    assert min_cost(A,"s",frozenset({"a"}))==1
    assert min_cost(B,"s",frozenset({"a"}))==1
    assert min_cost(A,"s",frozenset({"b"}))==1
    assert min_cost(B,"s",frozenset({"b"}))==1
    assert staged(A,["a","b"])==2
    assert staged(B,["a","b"])==inf
    assert staged(A,["b","a"])==2
    assert staged(B,["b","a"])==inf
    assert staged(A,["a"])==staged(B,["a"])==1
    assert staged(A,["b"])==staged(B,["b"])==1
    print("PASS 10 bounded checks: equal one-shot, unequal sequential residual")
