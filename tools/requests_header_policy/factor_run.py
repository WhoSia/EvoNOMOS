"""AST predictions vs native execution; exact equal-information finite CSP oracle."""
import importlib.util
import json
from pathlib import Path
from source_factors import pinned,extract
from factor_worlds import WORLDS,CASES,materialize,predict,expected,cost
from factor_native import observe

def normalized(value): return tuple(value) if isinstance(value,list) else value

def main():
    root=Path(importlib.util.find_spec('requests').origin).parent
    base=pinned(root); ref=observe(root,base)
    results=[]; predicted=[]; native=[]
    for world in WORLDS:
        src=materialize(base,world);factors=extract(src)
        assert factors==world,(world,factors)
        rows=observe(root,src)
        assert len(rows)==len(ref)==len(CASES)*4
        mismatch=bad_native=bad_model=legacy=0
        for row,old in zip(rows,ref):
            case,cycle,value,*legacy_values=row
            assert row[:2]==old[:2]
            v=normalized(value);p=predict(factors,case,cycle);target=expected(case)
            mismatch+=v!=p;bad_native+=v!=target;bad_model+=p!=target
            legacy+=legacy_values!=old[3:]
        if bad_model==0: predicted.append(world)
        if bad_native==0 and legacy==0: native.append(world)
        results.append({'world':world,'cost':cost(world),'rows':len(rows),'prediction_mismatches':mismatch,'native_contract_failures':bad_native,'model_contract_failures':bad_model,'legacy_mismatches':legacy})
    # Independent classical conjunction over explicit finite edit variables.
    csp=[w for w in WORLDS if w[0] and w[1] and w[2]=='normalized']
    result={'worlds':len(WORLDS),'observations':sum(r['rows'] for r in results),'prediction_mismatches':sum(r['prediction_mismatches'] for r in results),'legacy_mismatches':sum(r['legacy_mismatches'] for r in results),'factor_admitted':predicted,'native_admitted':native,'classical_csp_admitted':csp,'minimum_site_cost':min(map(cost,native),default=None),'rows':results}
    print(json.dumps(result,indent=2))
    assert predicted==native==csp and result['prediction_mismatches']==result['legacy_mismatches']==0

if __name__=='__main__': main()
