"""Pareto repair paths over cost and explicitly hypothetical additional owner permissions."""
import argparse
import heapq
import json
from pathlib import Path
from repair_frontier import graph


def insert(labels, mask, cost, path):
    if any(m & mask == m and c <= cost for m, (c, _) in labels.items()):
        return False
    for m in list(labels):
        if m & mask == mask and labels[m][0] >= cost:
            del labels[m]
    labels[mask] = cost, path
    return True


def options(model, start, goal, candidates):
    graph(model)  # validate the original envelope before adding hypothetical rights
    if not isinstance(candidates, list) or not all(isinstance(x, str) for x in candidates):
        raise ValueError('candidates must be a list of owner strings')
    names = sorted(set(candidates) - set(model['allowed_owners']))
    bits = {name: 1 << i for i, name in enumerate(names)}
    states, forward, _ = graph({**model, 'allowed_owners': model['allowed_owners'] + names})
    if start not in forward:
        raise ValueError('start must be a declared safe state')
    labels = {s: {} for s in forward}
    labels[start][0] = (0, ())
    queue, targets = [(0, start, 0)], {}
    while queue:
        cost, u, mask = heapq.heappop(queue)
        row = labels[u].get(mask)
        if row is None or row[0] != cost:
            continue
        if goal in states[u]['goals']:
            insert(targets, mask, cost, row[1])
            continue
        for v, c, i in forward[u]:
            new = mask | bits.get(model['edges'][i][2], 0)
            if insert(labels[v], new, cost+c, row[1]+(i,)):
                heapq.heappush(queue, (cost+c, v, new))
    return [{'additional_owners': [n for n in names if m & bits[n]], 'cost': c, 'edges': list(p)}
            for m, (c, p) in sorted(targets.items(), key=lambda x: (x[1][0], x[0]))]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('model', type=Path)
    p.add_argument('start')
    p.add_argument('goal')
    p.add_argument('--candidate-owner', action='append', default=[])
    a = p.parse_args()
    try:
        result = options(json.loads(a.model.read_text(encoding='utf-8')), a.start, a.goal, a.candidate_owner)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        p.error(str(exc))
    print(json.dumps({'scope': 'declared finite graph; hypothetical rights, not actual approval', 'options': result}, indent=2))


if __name__ == '__main__':
    main()
