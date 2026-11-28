"""Narrow source extraction for a pinned relativedelta constructor grammar."""
import ast
import hashlib
import importlib.metadata
from pathlib import Path
import dateutil.relativedelta as native

PIN='cd323a549e0f182541ebcde2d2ea1adfbbd9701e'
OPS={'normalize':'normalized:0','add_delta':'__add__:0','add_timedelta':'__add__:1','sub_delta':'__sub__:0','neg':'__neg__:0','abs':'__abs__:0','mul':'__mul__:0','rmul':'__mul__:0','div':'__mul__:0'}

def blob(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()

def extract():
    raw=Path(native.__file__).read_bytes()
    assert importlib.metadata.version('python-dateutil')=='2.9.0.post0'
    assert blob(raw)==PIN
    tree=ast.parse(raw)
    cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='relativedelta')
    methods={n.name:n for n in cls.body if isinstance(n,ast.FunctionDef)}
    sites={}; fields=set()
    for name,fn in methods.items():
        calls=sorted((n for n in ast.walk(fn) if isinstance(n,ast.Call) and ast.unparse(n.func)=='self.__class__'),key=lambda n:(n.lineno,n.col_offset))
        for i,n in enumerate(calls):
            sites[f'{name}:{i}']=n.func
            fields.add(tuple(k.arg for k in n.keywords))
    aliases={ast.unparse(t):ast.unparse(n.value) for n in cls.body if isinstance(n,ast.Assign) for t in n.targets}
    assert aliases['__rmul__']=='__mul__' and aliases['__truediv__']=='__div__'
    assert ast.unparse(methods['__div__'].body[-1])=='return self.__mul__(reciprocal)'
    assert ast.unparse(methods['__radd__'].body[-1])=='return self.__add__(other)'
    add=methods['__add__']
    assert ast.unparse(add.body[0].test)=='isinstance(other, relativedelta)'
    assert ast.unparse(add.body[1].test)=='isinstance(other, datetime.timedelta)'
    assert len(sites)==7 and set(sites)==set(OPS.values()) and len(fields)==1
    return raw,sites,next(iter(fields)),aliases
