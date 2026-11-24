"""R104: full historical route_headers.go differential experiment.
Usage: python run.py path/to/live.go path/to/snapshot.go
Requires Go; exact historical Git blob hashes are mandatory.
No claim of upstream contract, authentic owner authority, or human cost.
"""
from pathlib import Path
import os
import subprocess
import tempfile
import itertools
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    'live': 'ad9a2fbc0a30a39475f746068e74e2d3e6c93999',
    'snapshot': 'e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75',
}
OPS = {
    'base': [],
    'constructor': [('func NewPattern(value string) Pattern {', 'func NewPattern(value string) Pattern {\n value = strings.ToLower(value)')],
    'route_both': [('NewPattern(match)', 'NewPattern(strings.ToLower(match))'), ('NewPattern(m)', 'NewPattern(strings.ToLower(m))')],
    'match_lower': [('func (p Pattern) Match(v string) bool {', 'func (p Pattern) Match(v string) bool {\n p.prefix = strings.ToLower(p.prefix)\n p.suffix = strings.ToLower(p.suffix)')],
}
MODES = ('direct', 'route', 'any', 'raw')


def blob_sha(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def main(paths):
    if len(paths) != 2:
        raise SystemExit(__doc__)
    sources = dict(zip(EXPECTED, (Path(p).read_bytes() for p in paths)))
    for arm, data in sources.items():
        assert blob_sha(data) == EXPECTED[arm], (arm, blob_sha(data), EXPECTED[arm])
        print('SOURCE', arm, blob_sha(data))
    results = {}
    for arm, data in sources.items():
        for op, changes in OPS.items():
            src = data.decode('utf-8')
            for old, new in changes:
                assert src.count(old) == 1, (arm, op, old)
                src = src.replace(old, new)
            with tempfile.TemporaryDirectory() as d:
                p = Path(d)
                (p / 'route.go').write_text(src, encoding='utf-8')
                (p / 'probe_test.go').write_bytes((ROOT / 'probe_test.go.txt').read_bytes())
                out = subprocess.check_output(['go', 'test', '-v', '-count=1', '.'], cwd=d, env={**os.environ, 'GO111MODULE': 'off'}, text=True, stderr=subprocess.STDOUT)
                obs = [line.split()[1:] for line in out.splitlines() if line.startswith('OBS ')]
                rows = {tuple(row[:3]): row[3] for row in obs}
                expected = {(mode, str(i), str(j)) for mode in MODES for i in range(8) for j in range(11)}
                assert len(obs) == len(rows) == 352 and set(rows) == expected
                results[arm, op] = rows
    for arm in sources:
        base = results[arm, 'base']
        for op in OPS:
            if op == 'base':
                continue
            r = results[arm, op]
            print('CHANGE', arm, op, {mode: sum(r[k] != base[k] for k in base if k[0] == mode) for mode in MODES})
        for a, b in itertools.combinations(('constructor', 'route_both', 'match_lower'), 2):
            x, y = results[arm, a], results[arm, b]
            print('DIFF', arm, a, b, {mode: sum(x[k] != y[k] for k in x if k[0] == mode) for mode in MODES})
        assert all(results[arm, 'route_both'][k] == base[k] for k in base if k[0] in ('direct', 'raw'))
        assert all(results[arm, 'route_both'][k] == results[arm, 'constructor'][k] == results[arm, 'match_lower'][k] for k in base if k[0] in ('route', 'any'))
        assert results[arm, 'constructor'] == results[arm, 'match_lower']
        assert any(results[arm, 'constructor'][k] != results[arm, 'route_both'][k] for k in base if k[0] == 'raw')
    for op in OPS:
        assert results['live', op] == results['snapshot', op]
    print('PASS', len(results), 'Go runs', sum(map(len, results.values())), 'observations')


if __name__ == '__main__':
    main(sys.argv[1:])
