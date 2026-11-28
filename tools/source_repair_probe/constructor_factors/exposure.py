"""Aggregate actual operation histories by source-site coverage, not deployment frequencies."""
import json
from fractions import Fraction
from pathlib import Path
from collections import defaultdict
from worlds import KEYS,selected
from observations import OPERATIONS


def main():
    r=json.loads(Path(__file__).with_name('history_results.json').read_text())
    by=defaultdict(set);groups=defaultdict(list)
    for row in r['rows']:
        m=row['mask'];k=sum(selected(m,op) for op in OPERATIONS)
        expected=Fraction(k,9)**2
        assert Fraction(row['retained'],row['pairs'])==expected
        by[m.bit_count()].add(expected)
        groups[m.bit_count(),bool(m&(1<<KEYS.index('__mul__:0')))].append(expected)
    bands=[{'sites':n,'min':str(min(vals)),'max':str(max(vals))} for n,vals in sorted(by.items())]
    budget=[{'sites':n,'mul_site':hit,'worlds':len(vals),'retention':str(vals[0])} for (n,hit),vals in sorted(groups.items()) if n==3 and len(set(vals))==1]
    assert len(budget)==2
    print(json.dumps({'bands':bands,'budget_three':budget,'scope':'Uniform grid of nine delta-output operation labels; independent two-step draws. Not actual workload distribution.'},indent=2))

if __name__=='__main__':main()
