"""Native offline observations, isolated patched package per candidate."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from factor_worlds import CASES,MISSING

def worker():
    import pickle
    from types import SimpleNamespace
    from requests import Request, Response
    from requests.adapters import HTTPAdapter
    from requests.structures import CaseInsensitiveDict
    req=Request('GET','http://example.invalid/').prepare()
    rows=[]
    for case in CASES:
        raw,mutated,origin=case
        if origin=='direct':
            r=Response();r.headers=CaseInsensitiveDict({'Content-Type':raw});r.encoding='latin-1'
        else:
            r=HTTPAdapter().build_response(req,SimpleNamespace(status=200,headers={'Content-Type':raw},reason='OK'))
        r._content=b'\xe0\xe9';r._content_consumed=True
        if origin=='legacy':
            old=r.__getstate__();old.pop('_received_declaration',None)
            r=Response.__new__(Response);r.__setstate__(old)
        r.headers['Content-Type']=mutated
        r.encoding='latin-1'
        for cycle in range(4):
            rows.append([case,cycle,getattr(r,'received_declaration',MISSING),r.encoding,r.text])
            if cycle<3: r=pickle.loads(pickle.dumps(r))
    print(json.dumps(rows))

def observe(root,src):
    with tempfile.TemporaryDirectory() as d:
        d=Path(d);shutil.copytree(root,d/'requests',ignore=shutil.ignore_patterns('__pycache__'))
        for name,s in src.items(): (d/'requests'/name).write_text(s)
        env={**os.environ,'PYTHONPATH':str(d),'PYTHONDONTWRITEBYTECODE':'1'}
        return json.loads(subprocess.check_output([sys.executable,str(Path(__file__).resolve())],cwd=d,env=env,text=True))

if __name__=='__main__': worker()
