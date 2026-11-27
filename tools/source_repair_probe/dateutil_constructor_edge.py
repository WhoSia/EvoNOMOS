import json
from pathlib import Path
from probe import NATIVE, classes, FIXTURES, signature, fields
B=NATIVE.relativedelta
rows=[]
for arm in ('native','adapter','adapter_reflected'):
    cs=classes(B,arm!='native')
    if arm=='adapter_reflected':
        for k in ('optional','required'):
            cs[k].__rmul__=cs[k].__mul__
    for ctx,C in cs.items():
        def make(kw):return C(**kw,**({'tag':'KEEP'} if ctx in ('optional','required') else {}))
        for i,kw in enumerate(FIXTURES):
            base=signature(2*B(**kw),B); r=dict(arm=arm,context=ctx,operation='reflected_mul',fixture=i)
            try:
                x=2*make(kw);r.update(equal=signature(x,B)==base,exact_class=type(x)is C,tag=getattr(x,'tag',None))
            except Exception as e:r.update(error=type(e).__name__,equal=False,exact_class=False)
            rows.append(r)
        for field,v1,v2 in [('day',10,20),('month',1,2),('hour',3,8),('year',2024,2025)]:
            a,b={field:v1},{field:v2}
            for order in ('base_left','sub_left'):
                base=B(**a)+B(**b);r=dict(arm=arm,context=ctx,operation=order,field=field,expected=getattr(base,field))
                try:
                    x=B(**a)+make(b) if order=='base_left' else make(a)+B(**b)
                    r.update(equal=signature(x,B)==signature(base,B),actual=getattr(x,field),exact_class=type(x)is C,tag=getattr(x,'tag',None))
                except Exception as e:r.update(error=type(e).__name__,equal=False,exact_class=False)
                rows.append(r)
summary={}
for a in ('native','adapter','adapter_reflected'):
    summary[a]={}
    for c in ('base','compatible','optional','required'):
        summary[a][c]={}
        for op in ('reflected_mul','base_left','sub_left'):
            rs=[r for r in rows if r['arm']==a and r['context']==c and r['operation']==op]
            summary[a][c][op]={'n':len(rs),'equal':sum(r['equal'] for r in rs),'exact_class':sum(r['exact_class'] for r in rs),'tag_preserved':sum(r.get('tag')=='KEEP' for r in rs),'errors':sum('error'in r for r in rs)}
Path(__file__).with_name('edge_result.json').write_text(json.dumps({'summary':summary,'rows':rows},indent=2)+'\n');print(json.dumps(summary,indent=2))
