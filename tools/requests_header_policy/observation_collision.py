"""Exact receive-history observation collisions in SHA-pinned Requests (offline)."""
import hashlib
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

HISTORIES = [('text/plain', ('absent', None)),
             ('text/plain; charset=latin-1', ('declared', 'latin-1')),
             ('text/plain; charset=utf-8', ('declared', 'utf-8'))]


def worker(arm):
    import pickle
    from types import SimpleNamespace
    from requests import Request, Response
    from requests.adapters import HTTPAdapter
    from requests.utils import _parse_content_type_header
    req = Request('GET', 'http://example.invalid/').prepare()
    adapter = HTTPAdapter()
    rows = []
    for raw, expected in HISTORIES + [(None, ('unknown', None))]:
        response = adapter.build_response(req, SimpleNamespace(status=200, headers={'Content-Type': raw or 'text/plain'}, reason='OK'))
        response._content = b'\xe0\xe9'; response._content_consumed = True
        if raw is None:
            state = response.__getstate__(); state.pop('_received_declaration', None)
            response = Response.__new__(Response); response.__setstate__(state)
            captured = ('unknown', None)
        else:
            value = _parse_content_type_header(response.headers['content-type'])[1].get('charset')
            captured = ('declared', value) if isinstance(value, str) else ('absent', None)
        assert captured == expected
        response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        response.encoding = 'utf-8'
        legacy = response.__getstate__(); legacy.pop('_received_declaration', None)
        legacy_obj = Response.__new__(Response); legacy_obj.__setstate__(legacy)
        # Compare actual complete legacy state bytes, not selected fields.
        for protocol in (4,5):
            old_bytes = pickle.dumps(legacy, protocol=protocol)
            legacy_response_bytes = pickle.dumps(legacy_obj, protocol=protocol)
            if arm == 'legacy':
                carrier = pickle.dumps(response, protocol=protocol)
                observed = None  # no receive-history observation API
            elif arm == 'sidecar':
                carrier = pickle.dumps((response,captured), protocol=protocol)
                _, observed = pickle.loads(carrier)
            else:
                carrier = pickle.dumps(response, protocol=protocol)
                observed = pickle.loads(carrier).received_declaration
            rows.append({'raw':raw,'expected':expected,'protocol':protocol,
                         'legacy_state_hex':old_bytes.hex(),
                         'legacy_response_hex':legacy_response_bytes.hex(),
                         'carrier_hex':carrier.hex(), 'observed':observed,
                         'text':response.text,'encoding':response.encoding})
    print(json.dumps(rows))


def main(out):
    root = Path(importlib.util.find_spec('requests').origin).parent
    for n,sha in run.PINS.items(): assert run.blob((root/n).read_bytes()) == sha,n
    base={n:(root/n).read_text() for n in ('utils.py','models.py','adapters.py')}
    out.mkdir(parents=True,exist_ok=False); summary={}; allrows={}
    for arm in ('legacy','sidecar','snapshot_normalized'):
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp); shutil.copytree(root,tmp/'requests',ignore=shutil.ignore_patterns('__pycache__'))
            src=provenance.sources(base,'snapshot_serialized' if arm=='snapshot_normalized' else 'sidecar')
            if arm=='snapshot_normalized':
                src['models.py']=run.once(src['models.py'],'        return getattr(self, "_received_declaration", ("unknown", None))\n','        value = getattr(self, "_received_declaration", None)\n        return ("unknown", None) if value is None else value\n')
            for n,s in src.items(): (tmp/'requests'/n).write_text(s)
            env={**os.environ,'PYTHONPATH':str(tmp),'PYTHONDONTWRITEBYTECODE':'1'}
            rows=json.loads(subprocess.check_output([sys.executable,str(Path(__file__).resolve()),'--worker',arm],cwd=tmp,env=env,text=True));allrows[arm]=rows
            (out/(arm+'.json')).write_text(json.dumps(rows,indent=2)+'\n')
            summary[arm]={}
            for protocol in (4,5):
                group=[r for r in rows if r['protocol']==protocol]
                def count(k):return len({r[k] for r in group})
                summary[arm][str(protocol)]={'histories':len(group),'distinct_expected':len({tuple(r['expected']) for r in group}),'legacy_state_classes':count('legacy_state_hex'),'legacy_response_classes':count('legacy_response_hex'),'carrier_classes':count('carrier_hex'),'semantic_mismatch':None if arm=='legacy' else sum(r['observed']!=r['expected'] for r in group),'text_classes':count('text'),'encoding_classes':count('encoding')}
    for protocol in ('4','5'):
        for arm in summary:
            assert summary[arm][protocol]['legacy_state_classes']==1
            assert summary[arm][protocol]['legacy_response_classes']==1
        assert summary['legacy'][protocol]['carrier_classes']==1
        for arm in ('sidecar','snapshot_normalized'):
            assert summary[arm][protocol]['carrier_classes']==4
            assert summary[arm][protocol]['semantic_mismatch']==0
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n'); print(json.dumps(summary,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='--worker': worker(sys.argv[2])
    else: main(Path(sys.argv[1]).resolve())
