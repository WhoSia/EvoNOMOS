"""Offline native SQLite cache extension stress; self-generated payloads only."""
import importlib.util, importlib.metadata as md
import io, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path
from contextvars import ContextVar
import cache_carrier as cc
import provenance
import run

EXTRA_PINS={'serializers/pipeline.py':'9d1f7972fdf1726c671ff1830ea1f78e26486f4e','backends/base.py':'e980ae756b27a4da3a24fda9504b950508dde68d','backends/sqlite.py':'d4116fbd601fe85417905b7236d04a40e0772cc1','serializers/__init__.py':'b76202ea262682e6422063aae95361ad29056e4b','session.py':'8d9885b9513dfb3bffbf08ec247f691cee6c4b98'}
ARMS=('native','stage','backend','caller')
UNKNOWN=('unknown',None)
KEY='_evonomos_received_declaration_v1'
ATTR='_received_declaration'
ACTIVE=ContextVar('save_metadata',default=None)


def normalize(value):
    if isinstance(value,(tuple,list)) and len(value)==2:
        tag,text=value
        if tag=='declared' and isinstance(text,str): return (tag,text)
        if tag in ('absent','unknown') and text is None: return (tag,None)
    return UNKNOWN


def worker(arm, directory, migration=False):
    from requests import Request
    from requests.adapters import HTTPAdapter
    from requests.utils import _parse_content_type_header
    from requests_cache import CachedSession
    from requests_cache.backends.sqlite import SQLiteCache
    from requests_cache.serializers import pickle_serializer,json_serializer
    from requests_cache.serializers.pipeline import SerializerPipeline
    from urllib3.response import HTTPResponse

    class PreserveStage:
        def __init__(self,base): self.base=base
        def copy(self): return PreserveStage(self.base.copy())
        @property
        def decode_content(self): return self.base.decode_content
        @decode_content.setter
        def decode_content(self,value): self.base.decode_content=value
        def dumps(self,obj):
            data=self.base.dumps(obj)
            assert KEY not in data
            meta=ACTIVE.get()
            if meta is None: meta=normalize(getattr(obj,ATTR,None))
            data[KEY]=list(meta)
            return data
        def loads(self,data):
            data=dict(data);meta=normalize(data.pop(KEY,None))
            obj=self.base.loads(data);setattr(obj,ATTR,meta)
            return obj

    class PreserveCache(SQLiteCache):
        def save_response(self,response,*args,**kwargs):
            token=ACTIVE.set(normalize(getattr(response,ATTR,None)))
            try: return super().save_response(response,*args,**kwargs)
            finally: ACTIVE.reset(token)

    def serializer(name,mode=arm):
        base={'pickle':pickle_serializer,'json':json_serializer}[name]
        if mode=='native': return base
        return SerializerPipeline([PreserveStage(base.stages[0]),*base.stages[1:]],name='carrier-'+name,is_binary=base.is_binary)

    def open_session(path,name,mode=arm):
        cls=PreserveCache if mode in ('backend','caller') else SQLiteCache
        backend=cls(str(path),serializer=serializer(name,mode))
        session=CachedSession(backend=backend)
        assert session.cache is backend
        return session

    def fresh(raw):
        req=Request('GET','http://example.invalid/').prepare()
        r=HTTPAdapter().build_response(req,HTTPResponse(body=io.BytesIO(b'\xe0\xe9'),headers={'Content-Type':raw},status=200,preload_content=False,reason='OK'))
        assert r.content==b'\xe0\xe9'
        if arm=='caller':
            v=_parse_content_type_header(r.headers['Content-Type'])[1].get('charset')
            setattr(r,ATTR,('declared',v) if isinstance(v,str) else ('absent',None))
        r.headers['Content-Type']='text/plain; charset=utf-8';r.encoding='latin-1'
        return r

    if migration:
        assert arm=='caller'
        rows=[]
        for i,(raw,expected) in enumerate(cc.HISTORIES):
            for name in ('pickle','json'):
                for case in ('old_read_only','old_overwrite','legacy_upgrade'):
                    path=directory/f'{i}-{name}-{case}.sqlite'
                    old_writer=case=='legacy_upgrade'
                    with open_session(path,name,'native' if old_writer else 'caller') as s:
                        s.cache.save_response(fresh(raw),cache_key='probe')
                    with open_session(path,name,'caller' if old_writer else 'native') as s:
                        r=s.cache.get_response('probe');assert r is not None
                        interim=normalize(getattr(r,ATTR,None))
                        legacy_interim=(r.content,r.encoding,r.text)==(b'\xe0\xe9','latin-1','àé')
                        if case!='old_read_only': s.cache.save_response(r,cache_key='probe')
                    with open_session(path,name,'caller') as s:
                        r=s.cache.get_response('probe');assert r is not None
                        observed=normalize(getattr(r,ATTR,None))
                        want=expected if case=='old_read_only' else UNKNOWN
                        legacy=(r.content,r.encoding,r.text)==(b'\xe0\xe9','latin-1','àé')
                    rows.append(dict(header=raw,serializer=name,case=case,interim=interim,observed=observed,expected=want,passed=interim==UNKNOWN and observed==want,legacy=legacy and legacy_interim))
        assert all(r['passed'] and r['legacy'] for r in rows)
        print(json.dumps(rows));return

    rows=[]
    for i,(raw,expected) in enumerate(cc.HISTORIES):
        for name in ('pickle','json'):
            path=directory/f'{i}-{name}.sqlite';r=fresh(raw)
            assert normalize(getattr(r,ATTR,None))==expected
            for cycle in range(1,4):
                with open_session(path,name) as s: s.cache.save_response(r,cache_key='probe')
                with open_session(path,name) as s: c=s.cache.get_response('probe')
                assert c is not None and ACTIVE.get() is None
                observed=normalize(getattr(c,ATTR,None))
                rows.append(dict(header=raw,serializer=name,cycle=cycle,observed=observed,expected=expected,passed=observed==expected,legacy=(c.content,c.encoding,c.text)==(b'\xe0\xe9','latin-1','àé')))
                r=c
    # Exercise reset when actual storage serialization raises during save.
    cleanup=None
    if arm in ('backend','caller'):
        class FailingStage:
            def dumps(self,value):
                assert ACTIVE.get()==('declared','latin-1')
                raise RuntimeError('controlled storage failure')
            def loads(self,value): raise AssertionError('unexpected read')
        c=PreserveCache(str(directory/'failure.sqlite'),serializer=FailingStage())
        try:
            try: c.save_response(fresh(cc.HISTORIES[1][0]),cache_key='bad')
            except RuntimeError as e: assert str(e)=='controlled storage failure'
            else: raise AssertionError('expected failure')
            cleanup=ACTIVE.get() is None and c.get_response('bad') is None
            assert cleanup
        finally: c.close()
    print(json.dumps({'rows':rows,'exception_cleanup':cleanup}))


def main(out):
    assert md.version('requests')=='2.32.5' and md.version('requests-cache')=='1.3.2'
    req=Path(importlib.util.find_spec('requests').origin).parent
    cache=Path(importlib.util.find_spec('requests_cache').origin).parent
    for n,h in run.PINS.items(): assert run.blob((req/n).read_bytes())==h,n
    for n,h in {**cc.CACHE_PINS,**EXTRA_PINS}.items(): assert run.blob((cache/n).read_bytes())==h,n
    out.mkdir(parents=True,exist_ok=False);summary={}
    base={n:(req/n).read_text() for n in ('utils.py','models.py','adapters.py')}
    for arm in ARMS:
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp);shutil.copytree(req,tmp/'requests',ignore=shutil.ignore_patterns('__pycache__'))
            if arm!='caller':
                src=provenance.sources(base,'snapshot_serialized')
                src['models.py']=run.once(src['models.py'],'        return getattr(self, "_received_declaration", ("unknown", None))\n','        value = getattr(self, "_received_declaration", None)\n        return ("unknown", None) if value is None else value\n')
                for n,s in src.items(): (tmp/'requests'/n).write_text(s)
            directory=out/arm;directory.mkdir()
            env={**os.environ,'PYTHONPATH':str(tmp),'PYTHONDONTWRITEBYTECODE':'1'}
            result=json.loads(subprocess.check_output([sys.executable,str(Path(__file__).resolve()),'--worker',arm,str(directory.resolve())],cwd=tmp,env=env,text=True))
            (directory/'rows.json').write_text(json.dumps(result,indent=2)+'\n');rows=result['rows']
            summary[arm]={'request_blobs':{n:run.blob((tmp/'requests'/n).read_bytes()) for n in run.PINS},'n':len(rows),'success_by_cycle':{str(i):sum(r['passed'] for r in rows if r['cycle']==i) for i in range(1,4)},'legacy_failures':sum(not r['legacy'] for r in rows),'exception_cleanup':result['exception_cleanup']}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='--worker': worker(sys.argv[2],Path(sys.argv[3]))
    elif sys.argv[1]=='--migration':
        req=Path(importlib.util.find_spec('requests').origin).parent
        cache=Path(importlib.util.find_spec('requests_cache').origin).parent
        for n,h in run.PINS.items(): assert run.blob((req/n).read_bytes())==h,n
        for n,h in {**cc.CACHE_PINS,**EXTRA_PINS}.items(): assert run.blob((cache/n).read_bytes())==h,n
        path=Path(sys.argv[2]).resolve();path.mkdir(parents=True,exist_ok=False)
        worker('caller',path,True)
    else: main(Path(sys.argv[1]).resolve())
