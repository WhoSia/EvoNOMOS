"""Exhaust native worlds; predict observer outcomes before seeing individual probes."""
import json
from extract import native, PIN
from worlds import ALL,KEYS,materialize,load,classes,selected,worlds
from observations import FIXTURES,OPERATIONS,signature,observe


def predict(mask,H,T,ctx,op):
    tagged=ctx in ('optional','required')
    delta=op not in ('date_add','reverse_date_add')
    hit=selected(mask,op)
    if not delta: return True,True,True,None
    if hit and not H and not (T and tagged): return False,False,False,'AttributeError'
    keep=tagged and hit and T
    if ctx=='required' and not keep: return False,False,False,'TypeError'
    return True,True,not tagged or keep,None


def main():
    original=native.relativedelta
    refs={(i,op):signature(f(original(**kw),original),original) for i,kw in enumerate(FIXTURES) for op,f in OPERATIONS.items()}
    rows=[]
    for mask,H,T in worlds():
        B=load(materialize(mask,H));cs=classes(B,T)
        protected=failures=mismatches=0
        for ctx,C in cs.items():
            for i,kw in enumerate(FIXTURES):
                for op in OPERATIONS:
                    actual=observe(B,C,kw,op,ctx in ('optional','required'),refs[i,op])
                    pred=predict(mask,H,T,ctx,op)
                    mismatches+=actual!=pred
                    good=all(actual[:3])
                    failures+=not good
                    if ctx in ('base','compatible'): protected+=not good
        rows.append({'mask':mask,'H':H,'T':T,'protected_failures':protected,'contract_failures':failures,'prediction_mismatches':mismatches})
    safe=[(r['mask'],r['H'],r['T']) for r in rows if not r['protected_failures']]
    admitted=[(r['mask'],r['H'],r['T']) for r in rows if not r['contract_failures']]
    csp_safe=[(m,h,t) for m,h,t in worlds() if not m or h]
    csp_admitted=[(m,h,t) for m,h,t in worlds() if m==ALL and h and t]
    result={'pin':PIN,'keys':KEYS,'worlds':len(rows),'observations':len(rows)*len(FIXTURES)*len(OPERATIONS)*4,'mismatches':sum(r['prediction_mismatches'] for r in rows),'safe_count':len(safe),'admitted':admitted,'classical_match':safe==csp_safe and admitted==csp_admitted,'rows':rows}
    print(json.dumps(result,indent=2))
    assert result['mismatches']==0 and result['classical_match']

if __name__=='__main__':main()
