"""R106: compare frozen direction and interval against paired benchmark rounds."""
import json
import sys
from collections import defaultdict
from statistics import median

p = json.load(open(sys.argv[1]))
rows = defaultdict(dict)
for line in open(sys.argv[2]):
    if line.startswith('MIX '):
        _, rep, mode, key, _, ns, *rest = line.split()
        k = key.split('/')[1]
        assert k in p['predictions'] and mode in ('dup', 'compile')
        assert rep not in rows[k, mode]
        rows[k, mode][rep] = float(ns)
for k, prediction in p['predictions'].items():
    a, b = rows[k, 'dup'], rows[k, 'compile']
    assert set(a) == set(b) == set(map(str, range(5)))
    delta = median(b.values()) - median(a.values())
    paired = [b[r]-a[r] for r in a]
    actual = 'compile' if max(paired)<0 else 'dup' if min(paired)>0 else 'abstain'
    lo, hi = p['delta_bounds_ns'][k]
    print(json.dumps(dict(k=int(k), prediction=prediction, observed=actual,
        dup=median(a.values()), compile=median(b.values()), delta=delta,
        paired_range=[min(paired),max(paired)],
        directional_pass=None if prediction=='abstain' else actual==prediction,
        median_in_range=lo<=delta<=hi)))
