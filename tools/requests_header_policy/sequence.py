"""Apply each edit to current source, then run the frozen finite oracle."""
import ast
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


def step(s, arm, demand):
    if demand == 'boundary':
        s=run.once(s,'    if "text" in content_type:', '    if content_type.startswith("text/"):')
        return run.once(s,'    if "application/json" in content_type:', '    if content_type == "application/json":')
    if arm == 'parser':
        return run.once(s,'    return content_type, params_dict','    return content_type.lower(), params_dict')
    if arm == 'policy':
        return run.once(s,'def _classify_encoding(content_type):\n','def _classify_encoding(content_type):\n    content_type = content_type.lower()\n')
    anchor = '    if "text" in content_type:' if '    if "text" in content_type:' in s else '    if content_type.startswith("text/"):'
    return run.once(s,anchor,'    content_type = content_type.lower()\n\n'+anchor)


def functions(s):
    result={}
    def visit(body,prefix=''):
        for node in body:
            if isinstance(node,ast.ClassDef): visit(node.body,prefix+node.name+'.')
            elif isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
                result[prefix+node.name]=ast.dump(node,include_attributes=False)
    visit(ast.parse(s).body)
    return result


def method_delta(a,b):
    a,b=functions(a),functions(b)
    return {'changed':sorted(k for k in a.keys()&b.keys() if a[k]!=b[k]),'added':sorted(b.keys()-a.keys()),'removed':sorted(a.keys()-b.keys())}


def main(out):
    root=Path(importlib.util.find_spec('requests').origin).parent
    for n,sha in run.PINS.items(): assert run.blob((root/n).read_bytes())==sha,n
    original=(root/'utils.py').read_text(); out.mkdir(parents=True,exist_ok=False)
    rows=[]
    for arm in run.ARMS:
        for order in (run.DEMANDS,run.DEMANDS[::-1]):
            with tempfile.TemporaryDirectory() as tmp:
                tmp=Path(tmp); shutil.copytree(root,tmp/'requests',ignore=shutil.ignore_patterns('__pycache__'))
                env={**os.environ,'PYTHONPATH':str(tmp),'PYTHONDONTWRITEBYTECODE':'1'}
                target=tmp/'requests/utils.py'; target.write_text(run.treatment(original,arm,()))
                applied=[]; visits=int(arm=='policy')
                for demand in order:
                    old=target.read_text(); new=step(old,arm,demand); target.write_text(new); applied.append(demand); visits+=int(old!=new)
                    assert new==run.treatment(original,arm,tuple(applied))
                    d=json.loads(subprocess.check_output([sys.executable,str(Path(run.__file__).resolve()),'--worker',*applied],cwd=tmp,env=env,text=True))
                    cases=d['cases']; fail=sum(x['direct']!=x['want'] or x['adapter']!=x['want'] or not x['text_ok'] for x in cases)
                    raw_fail=sum(x['raw_token']!=x['raw'].split(';')[0] for x in cases)
                    rows.append({'arm':arm,'order':order,'applied':applied.copy(),'cases':len(cases),'fail':fail,'fixtures':[d['old_fixtures_pass'],d['old_fixtures_total']],'raw_fail':raw_fail,'file_visits':visits,'edit':method_delta(old,new),'sha':run.blob(new.encode())})
    base={n:(root/n).read_text() for n in ('utils.py','models.py','adapters.py')}; ref=provenance.sources(base,'sidecar')
    methods={a:{n:method_delta(ref[n],v) for n,v in provenance.sources(base,a).items() if ref[n]!=v} for a in provenance.ARMS}
    (out/'summary.json').write_text(json.dumps({'rows':rows,'provenance_methods':methods},indent=2)+'\n')
    assert len(rows)==12 and all(r['fail']==0 and r['fixtures']==[12,12] for r in rows)
    assert all(r['raw_fail']==(35 if r['arm']=='parser' and 'case' in r['applied'] else 0) for r in rows)
    print(json.dumps({'steps':len(rows),'cases':sum(r['cases'] for r in rows),'fixture_checks':sum(r['fixtures'][1] for r in rows),'finals':[r for r in rows if len(r['applied'])==2],'provenance_methods':methods},indent=2))


if __name__=='__main__':main(Path(sys.argv[1]).resolve())
