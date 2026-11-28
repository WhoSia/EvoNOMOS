"""Native operations and independent original-value observer."""
from datetime import date, timedelta
from worlds import FIELDS

FIXTURES=({'days':1.5,'hours':2,'day':20},{'days':-3,'minutes':-45,'month':2})
OPERATIONS={
    'normalize':lambda x,B:x.normalized(),
    'add_delta':lambda x,B:x+B(days=2,day=17),
    'add_timedelta':lambda x,B:x+timedelta(hours=30),
    'sub_delta':lambda x,B:x-B(days=2,day=17),
    'neg':lambda x,B:-x,
    'abs':lambda x,B:abs(x),
    'mul':lambda x,B:x*2,
    'rmul':lambda x,B:2*x,
    'div':lambda x,B:x/2,
    'date_add':lambda x,B:x+date(2024,1,31),
    'reverse_date_add':lambda x,B:date(2024,1,31)+x,
}

def signature(x,B):
    if isinstance(x,B): return ('delta',tuple(repr(getattr(x,k)) for k in FIELDS))
    if isinstance(x,date): return (type(x).__name__,x.isoformat())
    raise AssertionError(type(x))

def observe(B,C,kw,op,tagged,ref):
    x=C(**kw,**({'tag':'KEEP'} if tagged else {}))
    try:
        y=OPERATIONS[op](x,B)
    except (TypeError,AttributeError) as exc:
        return False,False,False,type(exc).__name__
    delta=ref[0]=='delta'
    return signature(y,B)==ref, (type(y) is C if delta else True), (not tagged or not delta or getattr(y,'tag',None)=='KEEP'),None
