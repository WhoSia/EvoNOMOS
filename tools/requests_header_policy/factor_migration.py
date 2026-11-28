"""Cross-source migration of self-produced local Response artifacts only."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from source_factors import pinned
from factor_worlds import materialize

WORLDS=((True,False,'raw'),(True,False,'normalized'),(True,True,'normalized'))
HEADERS=('text/plain; charset=latin-1','text/plain; charset=utf-8')
TARGET=[['declared','latin-1'],['declared','utf-8']]
UNKNOWN=['unknown',None]

def worker(mode,folder):
    import pickle
    from types import SimpleNamespace
    from requests import Request
    from requests.adapters import HTTPAdapter
    folder=Path(folder)
    result=[]
    if mode=='write':
        req=Request('GET','http://example.invalid/').prepare()
        for i,header in enumerate(HEADERS):
            r=HTTPAdapter().build_response(req,SimpleNamespace(status=200,headers={'Content-Type':header},reason='OK'))
            r._content=b'\xe0\xe9';r._content_consumed=True
            r.headers['Content-Type']='application/xml; charset=UTF-16';r.encoding='latin-1'
            data=pickle.dumps(r,protocol=4);(folder/str(i)).write_bytes(data)
            result.append({'declaration':r.received_declaration,'encoding':r.encoding,'text':r.text,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
    elif mode=='read':
        for i in range(len(HEADERS)):
            r=pickle.loads((folder/str(i)).read_bytes())
            result.append({'declaration':r.received_declaration,'encoding':r.encoding,'text':r.text})
    else: raise ValueError(mode)
    print(json.dumps(result,ensure_ascii=True))

def invoke(root,src,mode,folder):
    with tempfile.TemporaryDirectory() as d:
        d=Path(d);shutil.copytree(root,d/'requests',ignore=shutil.ignore_patterns('__pycache__'))
        for name,s in src.items(): (d/'requests'/name).write_text(s)
        env={**os.environ,'PYTHONPATH':str(d),'PYTHONDONTWRITEBYTECODE':'1'}
        return json.loads(subprocess.check_output([sys.executable,str(Path(__file__).resolve()),mode,str(folder)],cwd=d,env=env,text=True))

def main():
    root=Path(importlib.util.find_spec('requests').origin).parent
    base=pinned(root);destination=materialize(base,WORLDS[-1]);rows=[]
    for w in WORLDS:
        with tempfile.TemporaryDirectory() as folder:
            folder=Path(folder);before=invoke(root,materialize(base,w),'write',folder)
            equal=(folder/'0').read_bytes()==(folder/'1').read_bytes()
            after=invoke(root,destination,'read',folder)
            assert [x['declaration'] for x in before]==TARGET
            assert [x['declaration'] for x in after]==(TARGET if w[1] else [UNKNOWN,UNKNOWN])
            assert equal == (not w[1])
            assert all((a['encoding'],a['text'])==(b['encoding'],b['text']) for a,b in zip(before,after,strict=True))
            rows.append({'source':w,'destination':WORLDS[-1],'artifacts_equal':equal,'before':before,'after':after})
    print(json.dumps({'rows':rows,'scope':'two authored inputs, locally generated protocol 4 pickle artifacts; actual cross-source decode; no upstream deployment'},indent=2))

if __name__=='__main__':
    if len(sys.argv)==1: main()
    elif len(sys.argv)==3: worker(sys.argv[1],sys.argv[2])
    else: raise SystemExit('invalid arguments')
