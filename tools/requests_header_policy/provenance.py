"""Received-time declaration vs current header: actual Requests objects, offline.
Usage: python provenance.py NEW_OUTPUT_DIR (adjacent run.py from first experiment).
Only locally generated pickle data is loaded.
"""
import difflib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import run

ARMS = ('sidecar', 'live', 'snapshot_naive', 'snapshot_serialized')


def sources(base, arm):
    src = dict(base)
    src['utils.py'] = run.treatment(src['utils.py'], 'local', run.DEMANDS)
    if arm == 'sidecar':
        return src
    live = '''    def _current_declaration(self):
        from .utils import _parse_content_type_header
        raw = self.headers.get("content-type") or ""
        _, params = _parse_content_type_header(raw)
        value = params.get("charset")
        if isinstance(value, str):
            return ("declared", value.strip("'\\\""))
        return ("absent", None)

    @property
    def received_declaration(self):
'''
    accessor = '        return self._current_declaration()\n\n' if arm == 'live' else '        return getattr(self, "_received_declaration", ("unknown", None))\n\n'
    marker = '    def __getstate__(self):\n'
    # __getstate__ is unique in this pinned source.
    src['models.py'] = run.once(src['models.py'], marker, live + accessor + marker)
    if arm.startswith('snapshot'):
        src['adapters.py'] = run.once(src['adapters.py'], '        response.encoding = get_encoding_from_headers(response.headers)\n', '        response.encoding = get_encoding_from_headers(response.headers)\n        response._received_declaration = response._current_declaration()\n')
    if arm == 'snapshot_serialized':
        src['models.py'] = run.once(src['models.py'], '        "encoding",\n', '        "encoding",\n        "_received_declaration",\n')
    return src


def worker(arm):
    import pickle
    from types import SimpleNamespace
    from requests import Request, Response
    from requests.adapters import HTTPAdapter
    from requests.structures import CaseInsensitiveDict
    req = Request('GET', 'http://example.invalid/').prepare()
    adapter = HTTPAdapter()
    raw_cases = [('text/plain', ('absent',None)), ('TEXT/PLAIN', ('absent',None)), ('application/json', ('absent',None)), ('text/plain; charset=latin-1', ('declared','latin-1')), ('text/plain; charset="UTF-8"', ('declared','UTF-8')), ('application/xml; CHARSET=utf-8', ('declared','utf-8'))]
    rows=[]
    for raw, expected in raw_cases:
        for mutation in (None,'text/plain; charset=utf-8','application/json'):
            for override in (None,'utf-8'):
                h = {'Content-Type':raw}
                r=adapter.build_response(req, SimpleNamespace(status=200, headers=h, reason='OK'))
                r._content=b'\xe0\xe9\xee\xf4\xfb'; r._content_consumed=True
                # The caller baseline uses explicit capture at receive time; no source edits.
                from requests.utils import _parse_content_type_header
                val=_parse_content_type_header(r.headers['content-type'])[1].get('charset')
                sidecar=('declared',val) if isinstance(val,str) else ('absent',None)
                def observed(obj, side):
                    return side if arm=='sidecar' else obj.received_declaration
                before=observed(r,sidecar)
                if mutation is not None: r.headers['content-type']=mutation
                if override is not None: r.encoding=override
                after=observed(r,sidecar)
                # Test new state and loading old-format state, never untrusted pickle.
                if arm=='sidecar':
                    rr, ss=pickle.loads(pickle.dumps((r,sidecar)))
                else:
                    rr=pickle.loads(pickle.dumps(r));ss=None
                restored=observed(rr,ss)
                old=r.__getstate__(); old.pop('_received_declaration',None)
                oldobj=Response.__new__(Response);oldobj.__setstate__(old)
                old_seen=observed(oldobj,('unknown',None))
                rows.append({'key':[raw,mutation,override],'expected':expected,'before':before,'after':after,'restored':restored,'old':old_seen,'encoding':r.encoding,'text':r.text,'restored_encoding':rr.encoding,'restored_text':rr.text,'state_keys':sorted(r.__getstate__())})
    print(json.dumps(rows))


def main(out):
    root=Path(importlib.util.find_spec('requests').origin).parent
    for name,sha in run.PINS.items():assert run.blob((root/name).read_bytes())==sha,name
    base={n:(root/n).read_text() for n in ('utils.py','models.py','adapters.py')}
    out.mkdir(parents=True,exist_ok=False)
    allrows={}; costs={}
    for arm in ARMS:
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp);shutil.copytree(root,tmp/'requests',ignore=shutil.ignore_patterns('__pycache__'))
            src=sources(base,arm); foundation=sources(base,'sidecar')
            costs[arm]={n:run.delta(foundation[n],src[n]) for n in src if src[n]!=foundation[n]}
            for n,s in src.items():
                (tmp/'requests'/n).write_text(s)
                if s!=foundation[n]:
                    (out/(arm+'_'+n+'.diff')).write_text(''.join(difflib.unified_diff(foundation[n].splitlines(True),s.splitlines(True),fromfile=n,tofile=n)))
            env={**os.environ,'PYTHONPATH':str(tmp),'PYTHONDONTWRITEBYTECODE':'1'}
            r=subprocess.check_output([sys.executable,str(Path(__file__).resolve()),'--worker',arm],cwd=tmp,env=env,text=True)
            (out/(arm+'.json')).write_text(r);allrows[arm]=json.loads(r)
    summary={}
    ref={tuple(x['key']):x for x in allrows['sidecar']}
    for arm,rows in allrows.items():
        mismatch={k:sum(x[k]!=x['expected'] for x in rows) for k in ('before','after','restored')}
        mismatch['old_unknown']=sum(x['old']!=['unknown',None] for x in rows)
        mismatch['legacy']=sum(any(x[k]!=ref[tuple(x['key'])][k] for k in ('encoding','text','restored_encoding','restored_text')) for x in rows)
        summary[arm]={'cases':len(rows),'mismatch':mismatch,'production_costs':costs[arm],'state_keys':rows[0]['state_keys']}
    (out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n'); print(json.dumps(summary,indent=2,sort_keys=True))
    assert all(x['mismatch']['legacy']==0 for x in summary.values())
    assert not any(summary['sidecar']['mismatch'].values())
    assert not any(summary['snapshot_serialized']['mismatch'].values())
    assert summary['live']['mismatch']['after']>0 and summary['live']['mismatch']['old_unknown']>0
    assert summary['snapshot_naive']['mismatch']['restored']==36


if __name__=='__main__':
    if sys.argv[1]=='--worker':worker(sys.argv[2])
    else:main(Path(sys.argv[1]).resolve())
