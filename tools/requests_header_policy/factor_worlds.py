"""Finite source-edit grammar; no upstream mutation."""
from itertools import product
from source_factors import ACCESSORS

WORLDS=list(product((False,True),(False,True),ACCESSORS))
RAW=('text/plain','text/plain; charset=latin-1','application/json; charset=utf-8')
MUTATED=('application/xml; charset=UTF-16','text/plain')
ORIGINS=('adapter','direct','legacy')
CASES=list(product(RAW,MUTATED,ORIGINS))
UNKNOWN=('unknown',None)
MISSING=('missing',None)
DECLARATIONS={'text/plain':('absent',None),'text/plain; charset=latin-1':('declared','latin-1'),'application/json; charset=utf-8':('declared','utf-8'),'application/xml; charset=UTF-16':('declared','UTF-16')}
HELPER='''    def _current_declaration(self):
        from .utils import _parse_content_type_header
        raw = self.headers.get("content-type") or ""
        _, params = _parse_content_type_header(raw)
        value = params.get("charset")
        if isinstance(value, str):
            return ("declared", value.strip("'\\\""))
        return ("absent", None)

'''

def once(source,old,new):
    if source.count(old)!=1: raise ValueError('nonunique patch anchor: '+old)
    return source.replace(old,new,1)

def materialize(base,world):
    capture,whitelist,mode=world
    src=dict(base)
    if capture or mode=='live':
        marker='    def __getstate__(self):\n'
        src['models.py']=once(src['models.py'],marker,HELPER+marker)
    if mode!='absent':
        marker='    def __getstate__(self):\n'
        prop='    @property\n    def received_declaration(self):\n'+''.join('        '+line+'\n' for line in ACCESSORS[mode].splitlines())+'\n'
        src['models.py']=once(src['models.py'],marker,prop+marker)
    if capture:
        marker='        response.encoding = get_encoding_from_headers(response.headers)\n'
        src['adapters.py']=once(src['adapters.py'],marker,marker+'        response._received_declaration = response._current_declaration()\n')
    if whitelist:
        marker='        "encoding",\n'
        src['models.py']=once(src['models.py'],marker,marker+'        "_received_declaration",\n')
    return src

def expected(case):
    raw,_,origin=case
    return DECLARATIONS[raw] if origin=='adapter' else UNKNOWN

def predict(factors,case,cycle):
    capture,whitelist,mode=factors
    raw,mutated,origin=case
    present=capture and origin=='adapter'
    value=DECLARATIONS[raw] if present else None
    if cycle:
        present=whitelist
        if not whitelist: value=None
    if mode=='absent': return MISSING
    if mode=='live': return DECLARATIONS[mutated]
    if mode=='normalized': return UNKNOWN if value is None else value
    return value if present else UNKNOWN

def cost(world):
    c,w,m=world
    return int(c)+int(w)+int(m!='absent')
