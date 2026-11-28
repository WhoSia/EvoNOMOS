"""Reject unsupported extraction patterns; test known boundary counterexamples."""
import importlib.util
from pathlib import Path
from source_factors import pinned,extract
from factor_worlds import materialize,predict,expected,UNKNOWN,MISSING

def rejected(src):
    try: extract(src)
    except ValueError: return
    raise AssertionError('unsupported mutation accepted')

def main():
    base=pinned(Path(importlib.util.find_spec('requests').origin).parent)
    src=materialize(base,(True,True,'normalized'))
    for name,old,new in [
        ('models.py','getattr(self, attr, None)','getattr(self, attr, 0)'),
        ('models.py','for name, value in state.items():','for name, value in reversed(list(state.items())):'),
        ('adapters.py','        response._received_declaration = response._current_declaration()','        if False:\n            response._received_declaration = response._current_declaration()'),
        ('models.py','return ("unknown", None) if value is None else value','return value')]:
        assert old in src[name]
        bad=dict(src);bad[name]=bad[name].replace(old,new,1);rejected(bad)
    known=('text/plain; charset=latin-1','text/plain','adapter')
    old=('text/plain; charset=latin-1','text/plain','legacy')
    assert predict((True,False,'normalized'),known,0)==expected(known)
    assert predict((True,False,'normalized'),known,1)==UNKNOWN
    assert predict((True,True,'raw'),old,0)==UNKNOWN
    assert predict((True,True,'raw'),old,1) is None
    assert predict((True,True,'absent'),known,0)==MISSING
    print('4 unsupported AST patterns rejected; 5 boundary assertions passed')

if __name__=='__main__': main()
