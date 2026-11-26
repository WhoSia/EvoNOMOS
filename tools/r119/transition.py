"""R119: replay single-file transitions on R118 source arms.
Usage: python transition.py /path/to/replayed-r118 /path/to/new-output-dir
Inputs must include original R118 source and run.jsonl from replay.py.
"""
from collections import deque
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

RUN_SHA = 'e80d34d96ba4762be0fa710908270382477e610c'
TEST_SHA = '70f54c94ff6ac219017f07470cc8ef61cf736121'


def blob(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def shortest(edges, start, goals, protect, deny=()):
    todo = deque([(start, [])])
    seen = {start}
    while todo:
        state, path = todo.popleft()
        if state in goals:
            return path
        for nxt, action, file in edges[state]:
            if nxt not in seen and protect(nxt) and action not in deny:
                seen.add(nxt)
                todo.append((nxt, path + [(action, file, sorted(nxt))]))
    return None


def main(root, out):
    assert blob((root / 'run.py').read_bytes()) == RUN_SHA
    assert blob((root / 'token_probe.go.txt').read_bytes()) == TEST_SHA
    spec = importlib.util.spec_from_file_location('r118', root / 'run.py')
    r118 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r118)
    for name, sha in r118.EXPECTED.items():
        assert blob((root / name).read_bytes()) == sha, name
    rows = [json.loads(line) for line in (root / 'run.jsonl').read_text().splitlines()]
    expected = {(r['arm'], frozenset(r['actions'])): r for r in rows if 'arm' in r}
    assert len(expected) == 12
    out.mkdir(parents=True, exist_ok=False)
    env = {**os.environ, 'GOTOOLCHAIN': 'local', 'GOPROXY': 'off', 'GOMAXPROCS': '2'}
    summary = {}
    for arm in ('independent', 'shared'):
        menu = ('type', 'charset') if arm == 'independent' else ('type', 'charset', 'global')
        states = [frozenset(c) for k in range(len(menu) + 1) for c in itertools.combinations(menu, k)]
        sources = {}
        for state in states:
            with tempfile.TemporaryDirectory() as tmp:
                p = Path(tmp)
                r118.stage(arm, tuple(sorted(state)), p)
                sources[state] = {x.name: x.read_bytes() for x in p.iterdir()}
        edges = {s: [] for s in states}
        observations = {}
        for s in states:
            for action in menu:
                nxt = s ^ {action}
                changed = [n for n in sources[s] if sources[s][n] != sources[nxt][n]]
                assert set(sources[s]) == set(sources[nxt]) and len(changed) == 1
                name = changed[0]
                assert name == {'type': 'content_type.go', 'charset': 'content_charset.go', 'global': 'content_media_parse.go'}[action]
                edit = ('remove ' if action in s else 'add ') + action
                label = arm + '_' + ('-'.join(sorted(s)) or 'base') + '__' + edit.replace(' ', '-')
                with tempfile.TemporaryDirectory() as tmp:
                    p = Path(tmp)
                    for fn, data in sources[s].items():
                        (p / fn).write_bytes(data)
                    (p / name).write_bytes(sources[nxt][name])
                    assert {x.name: x.read_bytes() for x in p.iterdir()} == sources[nxt]
                    proc = subprocess.run(['go', 'test', '-count=1', '-v', '.'], cwd=p, env=env,
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                    (out / (label + '.log')).write_text(proc.stdout)
                    proc.check_returncode()
                obs = {tuple(x.split()[1:4]): int(x.split()[4]) for x in proc.stdout.splitlines() if x.startswith('OBS ')}
                assert len(obs) == 16
                legacy = all(v == 204 for (m, t, c), v in obs.items() if t == 'application/json')
                tr = all(v == 415 for (m, t, c), v in obs.items() if m == 'type' and t != 'application/json')
                cr = all(v == 415 for (m, t, c), v in obs.items() if m == 'charset' and t != 'application/json')
                ca = all(v == 204 for (m, t, c), v in obs.items() if m == 'charset' and t != 'application/json')
                ref = expected[arm, nxt]
                assert legacy and (tr and cr) == ref['common'] and (tr and ca) == ref['divergent']
                assert tr == bool(nxt & {'type', 'global'})
                assert cr == bool(nxt & {'charset', 'global'})
                if nxt in observations:
                    assert observations[nxt] == (tr, cr, ca, obs)
                observations[nxt] = (tr, cr, ca, obs)
                edges[s].append((nxt, edit, name))
        common = {s for s, (tr, cr, ca, _) in observations.items() if tr and cr}
        divergent = {s for s, (tr, cr, ca, _) in observations.items() if tr and ca}
        protect = lambda s: observations[s][0]
        paths = { '+'.join(sorted(s)): shortest(edges, s, divergent, protect) for s in common }
        denied = { '+'.join(sorted(s)): shortest(edges, s, divergent, protect, ('remove global',)) for s in common }
        summary[arm] = {'edges': sum(map(len, edges.values())), 'common_to_divergent': paths,
                        'global_removal_denied': denied}
    i, s = summary['independent'], summary['shared']
    assert i['edges'] == 8 and s['edges'] == 24
    assert len(i['common_to_divergent']['charset+type']) == 1
    assert len(s['common_to_divergent']['charset+type']) == 1
    assert [x[0] for x in s['common_to_divergent']['global']] == ['add type', 'remove global']
    assert s['global_removal_denied']['global'] is None
    assert s['global_removal_denied']['charset+type'] is not None
    summary['base_common_then_divergent_units'] = {'independent': 2 + len(i['common_to_divergent']['charset+type']),
        'shared_global': 1 + len(s['common_to_divergent']['global']),
        'shared_local': 2 + len(s['common_to_divergent']['charset+type'])}
    assert set(summary['base_common_then_divergent_units'].values()) == {3}
    (out / 'result.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
