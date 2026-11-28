"""Construct only declared source substitutions; upstream package is untouched."""
from itertools import product
from types import ModuleType
from extract import extract, OPS

RAW,SITES,FIELDS,ALIASES=extract()
KEYS=tuple(sorted(SITES))
HOOK=b'    def _evo_rebuild(self, **kwargs):\n        return self.__class__(**kwargs)\n\n'
MARK=b'    def normalized(self):\n'
ALL=(1<<len(KEYS))-1

def materialize(mask,hook):
    lines=RAW.splitlines(keepends=True)
    for i,key in enumerate(KEYS):
        if mask&(1<<i):
            n=SITES[key]; assert n.lineno==n.end_lineno
            row=lines[n.lineno-1]; a,b=n.col_offset,n.end_col_offset
            assert row[a:b]==b'self.__class__'
            lines[n.lineno-1]=row[:a]+b'self._evo_rebuild'+row[b:]
    src=b''.join(lines)
    if hook:
        assert src.count(MARK)==1
        src=src.replace(MARK,HOOK+MARK,1)
    return src

def load(src):
    mod=ModuleType('dateutil._evo_constructor_factors')
    exec(compile(src,'<pinned-relativedelta>','exec'),mod.__dict__)
    return mod.relativedelta

def classes(B,override):
    class Compatible(B): pass
    class Optional(B):
        def __init__(self,*a,tag='DEFAULT',**kw):
            super().__init__(*a,**kw);self.tag=tag
    class Required(B):
        def __init__(self,*a,tag,**kw):
            super().__init__(*a,**kw);self.tag=tag
    if override:
        def rebuild(self,**kw): return type(self)(tag=self.tag,**kw)
        Optional._evo_rebuild=Required._evo_rebuild=rebuild
    return {'base':B,'compatible':Compatible,'optional':Optional,'required':Required}

def selected(mask,op):
    return op in OPS and bool(mask&(1<<KEYS.index(OPS[op])))

def worlds(): return product(range(ALL+1),(False,True),(False,True))
