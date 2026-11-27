"""Cross-library schema repair, exact-version offline compatibility experiment."""
import importlib.util, json, os, pickle, shutil, subprocess, sys, tempfile
from pathlib import Path
import cache_carrier as cc
import provenance
import run


def worker(schema, phase, data_dir):
    import io
    from requests import Request
    from requests.adapters import HTTPAdapter
    from requests_cache.models.response import CachedResponse
    from requests_cache.serializers import pickle_serializer, json_serializer, dict_serializer
    from urllib3.response import HTTPResponse
    req=Request('GET','http://example.invalid/').prepare()
    pipelines={'pickle':pickle_serializer,'json':json_serializer,'dict':dict_serializer}
    rows=[]
    for i,(raw,expected) in enumerate(cc.HISTORIES):
        for name,p in pipelines.items():
            if phase=='write':
                r=HTTPAdapter().build_response(req,HTTPResponse(body=io.BytesIO(b'\xe0\xe9'),headers={'Content-Type':raw},status=200,preload_content=False,reason='OK'))
                assert r.content==b'\xe0\xe9' and r.received_declaration==expected
                r.headers['Content-Type']='text/plain; charset=utf-8';r.encoding='latin-1'
                c=CachedResponse.from_response(r)
                assert c.received_declaration==expected
                # Keep native payload in its own envelope solely to transport types to reader process.
                payload=p.dumps(c)
                with (data_dir/f'{schema}-{i}-{name}.pkl').open('wb') as f: pickle.dump(payload,f)
                for cycle in range(1,4):
                    try:
                        c=CachedResponse.from_response(c)
                        c=p.loads(p.dumps(c))
                        rows.append({'header':raw,'pipeline':name,'cycle':cycle,'observed':c.received_declaration,'expected':expected,'pass':c.received_declaration==expected,'legacy_pass':(c.content,c.encoding,c.text)==(b'\xe0\xe9','latin-1','àé'),'error':None})
                    except Exception as e:
                        rows.append({'header':raw,'pipeline':name,'cycle':cycle,'error':type(e).__name__+': '+str(e),'pass':False,'legacy_pass':False});break
            else:
                for writer in ('old','extended'):
                    try:
                        with (data_dir/f'{writer}-{i}-{name}.pkl').open('rb') as f: payload=pickle.load(f)
                        c=p.loads(payload)
                        want=expected if writer=='extended' and schema=='extended' else ('unknown',None)
                        rows.append({'header':raw,'pipeline':name,'writer':writer,'reader':schema,'observed':c.received_declaration,'expected':want,'pass':c.received_declaration==want,'legacy_pass':(c.content,c.encoding,c.text)==(b'\xe0\xe9','latin-1','àé'),'error':None})
                    except Exception as e:
                        rows.append({'header':raw,'pipeline':name,'writer':writer,'reader':schema,'error':type(e).__name__+': '+str(e),'pass':False,'legacy_pass':False})
    print(json.dumps(rows))


def main(out):
    req=Path(importlib.util.find_spec('requests').origin).parent
    cache=Path(importlib.util.find_spec('requests_cache').origin).parent
    for n,h in run.PINS.items(): assert run.blob((req/n).read_bytes())==h,n
    for n,h in cc.CACHE_PINS.items(): assert run.blob((cache/n).read_bytes())==h,n
    out.mkdir(parents=True,exist_ok=False); data=out/'payloads';data.mkdir()
    base={n:(req/n).read_text() for n in ('utils.py','models.py','adapters.py')}
    results={}; blobs={}
    with tempfile.TemporaryDirectory() as tmp:
        tmp=Path(tmp)
        for schema in ('old','extended'):
            p=tmp/schema;p.mkdir()
            shutil.copytree(req,p/'requests',ignore=shutil.ignore_patterns('__pycache__'))
            shutil.copytree(cache,p/'requests_cache',ignore=shutil.ignore_patterns('__pycache__'))
            src=provenance.sources(base,'snapshot_serialized')
            src['models.py']=run.once(src['models.py'],'        return getattr(self, "_received_declaration", ("unknown", None))\n','        value = getattr(self, "_received_declaration", None)\n        return ("unknown", None) if value is None else value\n')
            for n,s in src.items(): (p/'requests'/n).write_text(s)
            cp=p/'requests_cache/models/response.py';original=cp.read_text()
            if schema=='extended':
                s=run.once(original,'from typing import TYPE_CHECKING, Dict, List, Optional, Union','from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union')
                s=run.once(s,'    _content: bytes = field(default=None)\n','    _received_declaration: Optional[Tuple[str, Optional[str]]] = field(default=None)\n    _content: bytes = field(default=None)\n')
                cp.write_text(s)
            blobs[schema]=run.blob(cp.read_bytes())
        for phase in ('write','read'):
            for schema in ('old','extended'):
                env={**os.environ,'PYTHONPATH':str(tmp/schema),'PYTHONDONTWRITEBYTECODE':'1'}
                rows=json.loads(subprocess.check_output([sys.executable,str(Path(__file__).resolve()),'--worker',schema,phase,str(data.resolve())],cwd=tmp/schema,env=env,text=True))
                (out/f'{phase}-{schema}.json').write_text(json.dumps(rows,indent=2)+'\n')
                key=phase+'-'+schema
                results[key]={'n':len(rows),'mismatch':sum(not x['pass'] for x in rows),'legacy_mismatch':sum(not x['legacy_pass'] for x in rows),'errors':sum(x['error'] is not None for x in rows)}
                if phase=='read':
                    results[key]['by_writer']={w:{'n':len(g),'mismatch':sum(not x['pass'] for x in g),'legacy_mismatch':sum(not x['legacy_pass'] for x in g),'errors':sum(x['error'] is not None for x in g)} for w in ('old','extended') if (g:=[x for x in rows if x['writer']==w])}
    result={'cache_response_blobs':blobs,'results':results,'scope':'synthetic inputs, two pinned packages; proposed field not upstream; old-schema payloads generated locally; no real ACL, labor or full test suite'}
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps(result,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='--worker': worker(sys.argv[2],sys.argv[3],Path(sys.argv[4]))
    else: main(Path(sys.argv[1]).resolve())
