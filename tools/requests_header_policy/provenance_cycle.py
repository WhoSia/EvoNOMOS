"""Check repeated serialization of legacy and new Response objects (offline)."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import provenance
import run


def worker():
    import pickle
    from types import SimpleNamespace
    from requests import Request, Response
    from requests.adapters import HTTPAdapter
    req = Request('GET', 'http://example.invalid/').prepare()
    adapter = HTTPAdapter()
    rows = []
    for raw, expected in [('text/plain', ('absent', None)), ('text/plain; charset=latin-1', ('declared', 'latin-1'))]:
        for kind in ('known', 'legacy', 'direct'):
            r = adapter.build_response(req, SimpleNamespace(status=200, headers={'Content-Type':raw}, reason='OK'))
            r._content = b'\xe0\xe9'; r._content_consumed = True
            r.headers['Content-Type'] = 'application/json; charset=utf-8'
            r.encoding = 'latin-1'
            if kind == 'legacy':
                state = r.__getstate__(); state.pop('_received_declaration', None)
                r = Response.__new__(Response); r.__setstate__(state)
            elif kind == 'direct':
                r = Response(); r._content = b'\xe0\xe9'; r._content_consumed = True; r.encoding = 'latin-1'
            target = expected if kind == 'known' else ('unknown', None)
            legacy = (r.encoding, r.text)
            for cycle in range(4):
                rows.append({'raw':raw,'kind':kind,'cycle':cycle,'expected':target,'observed':r.received_declaration,'pass':r.received_declaration == target,'legacy_pass':(r.encoding,r.text)==legacy})
                r = pickle.loads(pickle.dumps(r))
    print(json.dumps(rows))


def main(out):
    root=Path(importlib.util.find_spec('requests').origin).parent
    for name,sha in run.PINS.items(): assert run.blob((root/name).read_bytes()) == sha, name
    base={n:(root/n).read_text() for n in ('utils.py','models.py','adapters.py')}
    out.mkdir(parents=True,exist_ok=False)
    summary={}
    for arm in ('snapshot_serialized','snapshot_normalized'):
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp); shutil.copytree(root,tmp/'requests',ignore=shutil.ignore_patterns('__pycache__'))
            src=provenance.sources(base,'snapshot_serialized')
            if arm == 'snapshot_normalized':
                src['models.py']=run.once(src['models.py'],'        return getattr(self, "_received_declaration", ("unknown", None))\n','        value = getattr(self, "_received_declaration", None)\n        return ("unknown", None) if value is None else value\n')
            for name,s in src.items(): (tmp/'requests'/name).write_text(s)
            env={**os.environ,'PYTHONPATH':str(tmp),'PYTHONDONTWRITEBYTECODE':'1'}
            rows=json.loads(subprocess.check_output([sys.executable,str(Path(__file__).resolve()),'--worker'],cwd=tmp,env=env,text=True))
            (out/(arm+'.json')).write_text(json.dumps(rows,indent=2)+'\n')
            summary[arm]={'cases':len(rows),'mismatch':sum(not x['pass'] for x in rows),'legacy_mismatch':sum(not x['legacy_pass'] for x in rows),'by_kind':{k:sum(not x['pass'] for x in rows if x['kind']==k) for k in ('known','legacy','direct')}}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n'); print(json.dumps(summary,indent=2))
    assert summary['snapshot_serialized']['mismatch']==12
    assert summary['snapshot_normalized']['mismatch']==0
    assert all(x['legacy_mismatch']==0 for x in summary.values())


if __name__=='__main__':
    if sys.argv[1]=='--worker': worker()
    else: main(Path(sys.argv[1]).resolve())
