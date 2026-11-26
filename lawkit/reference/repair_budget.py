"""Minimum-cost repair with a budget on distinct hypothetical additional owners."""
import argparse
import heapq
import json
from pathlib import Path
from repair_frontier import graph, frontier


def best(model, start, goal, candidates, budget, *, heuristic=True):
    graph(model)
    if not isinstance(candidates, list) or not all(isinstance(x, str) for x in candidates):
        raise ValueError('candidates must be a list of owner strings')
    if type(budget) is not int or budget < 0:
        raise ValueError('budget must be a nonnegative integer')
    names = sorted(set(candidates) - set(model['allowed_owners']))
    bits = {name: 1 << i for i, name in enumerate(names)}
    parsed = graph({**model, 'allowed_owners': model['allowed_owners'] + names})
    states, forward, _ = parsed
    if start not in forward:
        raise ValueError('start must be a declared safe state')
    # Relax only the additional-owner budget; retain safety and owner availability.
    h = {u:r['cost'] for u,r in frontier(parsed, goal).items()} if heuristic else dict.fromkeys(forward, 0)
    if h[start] is None:
        return None
    initial = (start, 0)
    distance, parent = {initial: 0}, {}
    queue = [(h[start], 0, start, 0)]
    while queue:
        _, neg_cost, u, mask = heapq.heappop(queue)
        cost = -neg_cost
        key = (u, mask)
        if distance[key] != cost:
            continue
        if goal in states[u]['goals']:
            path = []
            while key != initial:
                key, i = parent[key]
                path.append(i)
            return {'cost': cost, 'additional_owners': [n for n in names if mask & bits[n]], 'edges': path[::-1]}
        for v, c, i in forward[u]:
            new = mask | bits.get(model['edges'][i][2], 0)
            if new.bit_count() > budget or h[v] is None:
                continue
            nxt, alt = (v, new), cost+c
            if alt < distance.get(nxt, float('inf')):
                distance[nxt], parent[nxt] = alt, (key, i)
                heapq.heappush(queue, (alt+h[v], -alt, v, new))
    return None


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('model', type=Path)
    p.add_argument('start')
    p.add_argument('goal')
    p.add_argument('--candidate-owner', action='append', default=[])
    p.add_argument('--max-additional-owners', type=int, required=True)
    a = p.parse_args()
    try:
        result = best(json.loads(a.model.read_text(encoding='utf-8')), a.start, a.goal, a.candidate_owner, a.max_additional_owners)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        p.error(str(exc))
    print(json.dumps({'scope': 'declared finite graph; hypothetical rights only', 'option': result}, indent=2))


if __name__ == '__main__':
    main()
