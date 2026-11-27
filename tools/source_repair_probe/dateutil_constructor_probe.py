import ast, hashlib, importlib, importlib.util, importlib.metadata, json, sys, tempfile
from pathlib import Path
from datetime import date, datetime, timedelta
import operator
PIN='cd323a549e0f182541ebcde2d2ea1adfbbd9701e'
NATIVE=importlib.import_module('dateutil.relativedelta')
SRC=Path(NATIVE.__file__).read_bytes()
assert importlib.metadata.version('python-dateutil')=='2.9.0.post0'
assert hashlib.sha1(b'blob '+str(len(SRC)).encode()+b'\0'+SRC).hexdigest()==PIN
TREE=ast.parse(SRC)
CLS=next(x for x in TREE.body if isinstance(x,ast.ClassDef) and x.name=='relativedelta')
SITES=[(f.name,n.lineno,tuple(k.arg for k in n.keywords)) for f in CLS.body if isinstance(f,ast.FunctionDef) for n in ast.walk(f) if isinstance(n,ast.Call) and ast.unparse(n.func)=='self.__class__']
assert len(SITES)==7 and len({s[2] for s in SITES})==1
FIELDS=SITES[0][2]
assert SRC.count(b'self.__class__(')==7
REVERSE=SRC.replace(b'self.__class__(',b'relativedelta(')
FIXTURES=[{'days':1.5,'hours':2},{'months':1,'day':31},{'days':-3,'minutes':-45},{'years':1,'leapdays':1,'weekday':None}]
OPS={'add_delta':lambda x,b:x+b(days=2),'add_timedelta':lambda x,b:x+timedelta(hours=30),'sub_delta':lambda x,b:x-b(days=2),'neg':lambda x,b:-x,'abs':lambda x,b:abs(x),'mul':lambda x,b:x*2,'div':lambda x,b:x/2,'normalized':lambda x,b:x.normalized(),'date_add':lambda x,b:x+date(2024,1,31),'reverse_date_add':lambda x,b:date(2024,1,31)+x}

def fields(x): return {k:getattr(x,k) for k in FIELDS}
def signature(x,B):
    if isinstance(x,B):return ['delta', {k:repr(v) for k,v in fields(x).items()}]
    if isinstance(x,date):return [type(x).__name__,x.isoformat()]
    return [type(x).__name__,repr(x)]
def classes(B,adapter=False):
    class Compatible(B):pass
    class OptionalTag(B):
        def __init__(self,*args,tag='DEFAULT',**kw):super().__init__(*args,**kw);self.tag=tag
    class RequiredTag(B):
        def __init__(self,*args,tag,**kw):super().__init__(*args,**kw);self.tag=tag
    # Explicit constructor adapter, restricted to these two classes, not arbitrary subclasses.
    def method(name):
        def invoke(self,*args):
            raw=B(**fields(self))
            result=getattr(raw,name)(*args)
            if isinstance(result,B):return type(self)(tag=self.tag,**fields(result))
            return result
        return invoke
    if adapter:
        for C in (OptionalTag,RequiredTag):
            for n in ('__add__','__radd__','__sub__','__neg__','__abs__','__mul__','__truediv__','normalized'):
                setattr(C,n,method(n))
    return {'base':B,'compatible':Compatible,'optional':OptionalTag,'required':RequiredTag}

def main():
    rows=[]
    with tempfile.TemporaryDirectory() as t:
        p=Path(t)/'relativedelta.py';p.write_bytes(REVERSE)
        spec=importlib.util.spec_from_file_location('dateutil._evo_reverse',p);rev=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rev;spec.loader.exec_module(rev)
        for arm,B,adapter in [('native',NATIVE.relativedelta,False),('reverse',rev.relativedelta,False),('app_adapter',NATIVE.relativedelta,True)]:
            for context,C in classes(B,adapter).items():
                for f,kw in enumerate(FIXTURES):
                    for op,func in OPS.items():
                        b=func(B(**kw),B); base=signature(b,B)
                        x=C(**kw,**({'tag':'KEEP'} if context in ('optional','required') else {})); delta=isinstance(b,B)
                        r={'arm':arm,'context':context,'fixture':f,'op':op,'delta_output':delta,'base':base}
                        try:
                            y=func(x,B);r.update(signature=signature(y,B),value_equal=signature(y,B)==base,exact_class=type(y) is C if delta else type(y) is type(b),tag_preserved=getattr(y,'tag',None)=='KEEP' if delta and context in ('optional','required') else None)
                        except Exception as e:r.update(error=type(e).__name__,message=str(e),value_equal=False,exact_class=False,tag_preserved=False if delta and context in ('optional','required') else None)
                        rows.append(r)
    # A common base oracle across variants, not only within each variant.
    bases={(r['fixture'],r['op']):r['signature'] for r in rows if r['arm']=='native' and r['context']=='base'}
    assert all(r.get('signature')==bases[r['fixture'],r['op']] for r in rows if r['context']=='base')
    summaries={}
    for arm in ('native','reverse','app_adapter'):
        summaries[arm]={}
        for context in ('base','compatible','optional','required'):
            rs=[r for r in rows if r['arm']==arm and r['context']==context];ds=[r for r in rs if r['delta_output']];ts=[r for r in ds if r['tag_preserved'] is not None]
            summaries[arm][context]={'n':len(rs),'delta_n':len(ds),'value_equal':sum(r['value_equal'] for r in rs),'delta_exact_class':sum(r['exact_class'] for r in ds),'tag_n':len(ts),'tag_preserved':sum(r['tag_preserved'] for r in ts),'errors':sum('error' in r for r in rs),'date_equal':sum(r['value_equal'] for r in rs if not r['delta_output'])}
    result={'source_blob':PIN,'source_sites':SITES,'reverse_sha256':hashlib.sha256(REVERSE).hexdigest(),'summary':summaries,'rows':rows,'scope':'Current pinned dateutil source, seven-site reverse mutant, explicit narrow application adapter; historical issue exposed; finite researcher-authored tag contract; no independent outcomes.'}
    Path(__file__).with_name('result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(summaries,indent=2))
if __name__=='__main__':main()
