"""Pinned Requests and requests-cache native boundary stress; no network."""
import importlib.metadata as md
import importlib.util
import io, json, os, pickle, shutil, subprocess, sys, tempfile
from pathlib import Path
import provenance
import run

CACHE_PINS = {'models/response.py':'57b7ce20c57f18c28471cdbcc50af4a0046cf39e','models/raw_response.py':'e895e551ecf44854043038427d92b612565c244d','serializers/cattrs.py':'a791cd690498ed1f3963255272fd7e402e84e1a1','serializers/preconf.py':'523599c639a20ba7b7c113502d7c06a77ac23efe'}
HISTORIES = [('text/plain',('absent',None)),('text/plain; charset=latin-1',('declared','latin-1')),('text/plain; charset=utf-8',('declared','utf-8'))]


def worker(arm):
    from types import SimpleNamespace
    from requests import Request, Response
    from requests.adapters import HTTPAdapter
    from requests.utils import _parse_content_type_header
    from requests_cache.models.response import OriginalResponse, CachedResponse
    from requests_cache.serializers import pickle_serializer, json_serializer, dict_serializer
    from urllib3.response import HTTPResponse
    req = Request('GET','http://example.invalid/').prepare()
    adapter = HTTPAdapter()
    def fresh(raw):
        r=adapter.build_response(req,HTTPResponse(body=io.BytesIO(b'\xe0\xe9'),headers={'Content-Type':raw},status=200,preload_content=False,reason='OK'))
        assert r.content==b'\xe0\xe9'
        _,params=_parse_content_type_header(r.headers['Content-Type'])
        value=params.get('charset')
        captured=('declared',value) if isinstance(value,str) else ('absent',None)
        r.headers['Content-Type']='text/plain; charset=utf-8'
        r.encoding='latin-1'
        return r,captured
    def carry_object(c,meta):
        if arm=='sidecar':
            return pickle.loads(pickle.dumps((c,meta)))
        return pickle.loads(pickle.dumps(c)),None
    def carry_pipeline(pipeline,c,meta):
        payload=pipeline.dumps(c)
        if arm=='sidecar':
            payload,meta=pickle.loads(pickle.dumps((payload,meta)))
        return pipeline.loads(payload),meta
    rows=[]
    for raw,expected in HISTORIES:
        paths = {
            'wrap':lambda r,m: (OriginalResponse.wrap_response(r,SimpleNamespace(skip_write=True,expires=None,cache_key=None)),m),
            'cache_conversion':lambda r,m: (CachedResponse.from_response(r),m),
            'cache_evolve':lambda r,m: (CachedResponse.from_response(CachedResponse.from_response(r)),m),
            'direct_pickle':lambda r,m: carry_object(CachedResponse.from_response(r),m),
            'cache_pickle_pipeline':lambda r,m: carry_pipeline(pickle_serializer,CachedResponse.from_response(r),m),
            'cache_json_pipeline':lambda r,m: carry_pipeline(json_serializer,CachedResponse.from_response(r),m),
            'cache_dict_pipeline':lambda r,m: carry_pipeline(dict_serializer,CachedResponse.from_response(r),m),
        }
        for name,fn in paths.items():
            r,captured=fresh(raw); legacy=(r.content,r.encoding,r.text)
            assert captured==expected
            if arm=='snapshot': assert r.received_declaration==expected
            # Sidecar travels alongside the object/pipeline payload; native pipeline
            # still consumes its original format. Envelope is an additional protocol.
            c,meta=fn(r,captured if arm=='sidecar' else None)
            observed=c.received_declaration if arm=='snapshot' else meta
            rows.append({'header':raw,'boundary':name,'expected':expected,'observed':observed,'pass':observed==expected,'legacy_pass':(c.content,c.encoding,c.text)==legacy,'class':type(c).__name__,'same_identity':c is r,'stored_attribute':hasattr(c,'_received_declaration')})
    print(json.dumps(rows))


def main(out):
    assert md.version('requests')=='2.32.5' and md.version('requests-cache')=='1.3.2'
    root=Path(importlib.util.find_spec('requests').origin).parent
    cache=Path(importlib.util.find_spec('requests_cache').origin).parent
    for n,h in run.PINS.items(): assert run.blob((root/n).read_bytes())==h,n
    for n,h in CACHE_PINS.items(): assert run.blob((cache/n).read_bytes())==h,n
    base={n:(root/n).read_text() for n in ('utils.py','models.py','adapters.py')}
    out.mkdir(parents=True,exist_ok=False); summary={}
    for arm in ('sidecar','snapshot'):
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp); shutil.copytree(root,tmp/'requests',ignore=shutil.ignore_patterns('__pycache__'))
            src=provenance.sources(base,'snapshot_serialized' if arm=='snapshot' else 'sidecar')
            if arm=='snapshot':
                src['models.py']=run.once(src['models.py'],'        return getattr(self, "_received_declaration", ("unknown", None))\n','        value = getattr(self, "_received_declaration", None)\n        return ("unknown", None) if value is None else value\n')
            for n,s in src.items(): (tmp/'requests'/n).write_text(s)
            env={**os.environ,'PYTHONPATH':str(tmp),'PYTHONDONTWRITEBYTECODE':'1'}
            rows=json.loads(subprocess.check_output([sys.executable,str(Path(__file__).resolve()),'--worker',arm],cwd=tmp,env=env,text=True))
            (out/(arm+'.json')).write_text(json.dumps(rows,indent=2)+'\n')
            summary[arm]={'source_blobs':{n:run.blob(s.encode()) for n,s in src.items()},'boundaries':{k:{'cases':len(g),'mismatch':sum(not x['pass'] for x in g),'legacy_mismatch':sum(not x['legacy_pass'] for x in g),'stored_attr_count':sum(x['stored_attribute'] for x in g)} for k in sorted({r['boundary'] for r in rows}) if (g:=[r for r in rows if r['boundary']==k])}}
    result={'versions':{n:md.version(n) for n in ('requests','requests-cache','urllib3','attrs','cattrs')},'cache_pins':CACHE_PINS,'results':summary,'scope':'synthetic inputs on pinned real package paths; separate sidecar envelope, not equivalent API or cost; no external requests or full suite'}
    (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='--worker': worker(sys.argv[2])
    else: main(Path(sys.argv[1]).resolve())
