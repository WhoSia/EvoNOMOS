"""Strong application-only shared mixin on untouched dateutil; no extra dependency."""
import json
from itertools import product
from extract import native
from worlds import ALL,materialize,load,classes,FIELDS
from observations import FIXTURES,OPERATIONS,observe,signature

METHODS=('normalized','__add__','__sub__','__neg__','__abs__','__mul__')
DELTA_OPS=tuple(o for o in OPERATIONS if o not in ('date_add','reverse_date_add'))

def app_classes(B,alias):
    def fields(x): return {k:getattr(x,k) for k in FIELDS}
    class Mixin: pass
    def wrapper(name):
        def invoke(self,*a):
            value=getattr(B(**fields(self)),name)(*a)
            return type(self)(tag=self.tag,**fields(value)) if isinstance(value,B) else value
        return invoke
    for name in METHODS:setattr(Mixin,name,wrapper(name))
    if alias:Mixin.__rmul__=Mixin.__mul__
    class Optional(Mixin,B):
        def __init__(self,*a,tag='DEFAULT',**kw):super().__init__(*a,**kw);self.tag=tag
    class Required(Mixin,B):
        def __init__(self,*a,tag,**kw):super().__init__(*a,**kw);self.tag=tag
    c=classes(B,False);c.update(optional=Optional,required=Required);return c

def main():
    original=native.relativedelta
    refs={(i,op):signature(f(original(**kw),original),original) for i,kw in enumerate(FIXTURES) for op,f in OPERATIONS.items()}
    hooked=load(materialize(ALL,True))
    rows=[]
    for arm,B,cs in [('source_hook',hooked,classes(hooked,True)),('app_no_alias',original,app_classes(original,False)),('app_alias',original,app_classes(original,True))]:
        bad=[];core=0
        for ctx,C in cs.items():
            for i,kw in enumerate(FIXTURES):
                for op in OPERATIONS:
                    row=observe(B,C,kw,op,ctx in ('optional','required'),refs[i,op]);core+=not row[0]
                    if not all(row[:3]):bad.append([ctx,i,op,row])
        pairs=0;losses=0;pair_core=0;C=cs['optional']
        for kw,a,b in product(FIXTURES,DELTA_OPS,DELTA_OPS):
            ref=OPERATIONS[b](OPERATIONS[a](B(**kw),B),B)
            out=[OPERATIONS[b](OPERATIONS[a](C(**kw,tag=t),B),B) for t in ('A','B')]
            pairs+=1;losses+=[x.tag for x in out]!=['A','B'];pair_core+=any(signature(x,B)!=signature(ref,B) for x in out)
        mixed=[]
        for field,a,b in [('day',10,20),('month',1,2),('year',2024,2025),('hour',3,8)]:
            x=B(**{field:a})+C(**{field:b},tag='KEEP');ref=B(**{field:a})+B(**{field:b})
            mixed.append({'field':field,'core':signature(x,B)==signature(ref,B),'subtype':type(x)is C,'tag':getattr(x,'tag',None)})
        rows.append({'arm':arm,'observations':88,'failures':bad,'core_mismatches_or_errors':core,'paired_histories':pairs,'history_losses':losses,'history_core_mismatches':pair_core,'base_left':mixed})
    for r in (rows[0],rows[2]):assert not r['failures'] and not r['history_losses'] and not r['history_core_mismatches']
    assert len(rows[1]['failures'])==4 and all(x[2]=='rmul' for x in rows[1]['failures'])
    assert all(all(x['core'] and not x['subtype'] and x['tag'] is None for x in r['base_left']) for r in rows)
    print(json.dumps({'rows':rows,'cost_scope':'Hook: seven upstream call sites + one upstream default hook, application override implementation, shared reuse possible. Mixin: zero upstream sites, one shared wrapper generator, six method bindings + one alias binding, two subclass attachment points. No equal labor claim.'},indent=2))

if __name__=='__main__':main()
