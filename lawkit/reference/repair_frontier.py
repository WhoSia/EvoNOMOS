"""Finite declared repair graph: exact integer costs, no inferred source or authority."""
import argparse
import heapq
import json
from pathlib import Path


def graph(model):
    states = model['states']
    if not isinstance(states, dict) or not states:
        raise ValueError('states must be a nonempty object')
    for name, state in states.items():
        if not isinstance(name, str) or not name or type(state['safe']) is not bool:
            raise ValueError('state name and Boolean safe required')
        if not isinstance(state['goals'], list) or not all(isinstance(g, str) for g in state['goals']):
            raise ValueError('goals must be strings')
    owners = model['allowed_owners']
    if not isinstance(owners, list) or not all(isinstance(o, str) for o in owners):
        raise ValueError('allowed_owners must be strings')
    if not isinstance(model['edges'], list):
        raise ValueError('edges must be a list')
    safe = {s for s in states if states[s]['safe']}
    forward = {s: [] for s in sorted(safe)}
    reverse = {s: [] for s in forward}
    for i, edge in enumerate(model['edges']):
        u, v, owner, cost = edge
        if not all(isinstance(x, str) for x in (u, v, owner)) or u not in states or v not in states:
            raise ValueError('unknown state or invalid owner')
        if type(cost) is not int or cost <= 0:
            raise ValueError('edge cost must be a positive integer')
        if u in safe and v in safe and owner in owners:
            forward[u].append((v, cost, i))
            reverse[v].append((u, cost, i))
    return states, forward, reverse


def frontier(parsed, goal):
    states, forward, reverse = parsed
    targets = {s for s in forward if goal in states[s]['goals']}
    dist = {s: 0 for s in targets}
    next_edge = {}
    queue = [(0, s) for s in targets]
    heapq.heapify(queue)
    while queue:
        d, v = heapq.heappop(queue)
        if d != dist[v]:
            continue
        for u, c, i in reverse[v]:
            if u not in dist or d+c < dist[u]:
                dist[u], next_edge[u] = d+c, i
                heapq.heappush(queue, (d+c, u))
    return {s: {'cost': dist.get(s), 'next_edge': next_edge.get(s)} for s in forward}


def verify(parsed, goal, result):
    states, forward, _ = parsed
    if set(result) != set(forward):
        raise ValueError('certificate state set differs')
    for u, row in result.items():
        d, i = row['cost'], row['next_edge']
        target = goal in states[u]['goals']
        if d is not None and (type(d) is not int or d < 0):
            raise ValueError('invalid distance')
        if target:
            if d != 0 or i is not None:
                raise ValueError('invalid goal certificate')
        elif d is None:
            if i is not None:
                raise ValueError('unreachable witness')
        elif type(i) is not int or d == 0 or not any(j == i and result[v]['cost'] is not None and d == c+result[v]['cost'] for v,c,j in forward[u]):
            raise ValueError('missing decreasing witness')
        for v,c,_ in forward[u]:
            dv = result[v]['cost']
            if dv is not None and (d is None or d > c+dv):
                raise ValueError('distance inequality failed')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', type=Path)
    parser.add_argument('goal')
    args = parser.parse_args()
    try:
        parsed = graph(json.loads(args.model.read_text(encoding='utf-8')))
        result = frontier(parsed, args.goal)
        verify(parsed, args.goal, result)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps({'goal': args.goal, 'scope': 'declared finite graph only', 'states': result}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
