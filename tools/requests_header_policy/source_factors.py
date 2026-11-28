"""Narrow AST extraction; unsupported source patterns fail closed."""
import ast
from pathlib import Path
import hashlib

FIELD = '_received_declaration'
PINS = {'models.py':'c4b25fa0790da44683dab185c89ac08b69fb7419','adapters.py':'670c92767c5420a21538688132ce1f4f45e45873','utils.py':'8ab55852cc2188c53f08462ec4319c97fa49f04b','structures.py':'188e13e4829591facb23ae0e2eda84b9807cb818'}
ACCESSORS = {'absent':'', 'live':'return self._current_declaration()', 'raw':'return getattr(self, "_received_declaration", ("unknown", None))', 'normalized':'value = getattr(self, "_received_declaration", None)\nreturn ("unknown", None) if value is None else value'}

def blob(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()

def pinned(root):
    for name, sha in PINS.items():
        if blob((root/name).read_bytes()) != sha:
            raise ValueError('source pin mismatch: '+name)
    return {name:(root/name).read_text() for name in ('models.py','adapters.py')}

def class_node(source,name):
    return next(n for n in ast.parse(source).body if isinstance(n,ast.ClassDef) and n.name==name)

def body_key(nodes):
    return tuple(ast.dump(n,include_attributes=False) for n in nodes)

def extract(src):
    response=class_node(src['models.py'],'Response')
    adapter=class_node(src['adapters.py'],'HTTPAdapter')
    methods={n.name:n for n in response.body if isinstance(n,ast.FunctionDef)}
    attrs=next(n.value for n in response.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='__attrs__' for t in n.targets))
    attrs=ast.literal_eval(attrs)
    returns=[n for n in ast.walk(methods['__getstate__']) if isinstance(n,ast.Return)]
    if body_key(returns)!=body_key(ast.parse('return {attr: getattr(self, attr, None) for attr in self.__attrs__}').body):
        raise ValueError('unsupported getstate')
    loops=[n for n in methods['__setstate__'].body if isinstance(n,ast.For)]
    if body_key(loops)!=body_key(ast.parse('for name, value in state.items():\n    setattr(self, name, value)').body):
        raise ValueError('unsupported setstate')
    build=next(n for n in adapter.body if isinstance(n,ast.FunctionDef) and n.name=='build_response')
    captures=[n for n in ast.walk(build) if isinstance(n,ast.Assign) and any(ast.unparse(t)=='response.'+FIELD for t in n.targets)]
    if captures and (any(n not in build.body for n in captures) or body_key(captures)!=body_key(ast.parse('response._received_declaration = response._current_declaration()').body)):
        raise ValueError('unsupported capture')
    method=methods.get('received_declaration')
    mode='absent'
    if method:
        if [ast.unparse(d) for d in method.decorator_list]!=['property']:
            raise ValueError('not property')
        mode=next((k for k,v in ACCESSORS.items() if v and body_key(method.body)==body_key(ast.parse(v).body)),None)
        if mode is None: raise ValueError('unsupported accessor')
    return bool(captures), FIELD in attrs, mode
