"""Exploratory, post-hoc control expansion. Only unmodified Click executes here."""
import concurrent.futures, hashlib, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path
import click
from cia_probe import universe, predictions, changes, stats
ROOT = Path(__file__).resolve().parent
CASES = [('invalid_option','default',('-h','--help'),('--bad',),{}),
         ('missing_value','value_option',('-h','--help'),('--value',),{}),
         ('value_help','value_option',('-h','--help'),('--help',),{}),
         ('value_present','value_option',('-h','--help'),('--value','x'),{})]

def main():
    source = Path(click.__file__).parent
    base_result = json.loads((ROOT/'cia_result.json').read_text())
    for p,h in base_result['pins'].items():
        raw=(source/p).read_bytes();assert hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()==h
    traces=json.loads((ROOT/'cia_traces.json').read_text())
    U=universe(source)
    suite=set.union(*(predictions(x)[1] for x in traces['base'].values())) & U
    original= (ROOT/'cia_probe.py').read_text()
    needle="        if kind!='auto': command=click.help_option(*decls,**opts)(command)"
    assert original.count(needle)==1
    instrumented=original.replace(needle,"        if kind=='value_option': command=click.option('--value',expose_value=False)(command)\n"+needle)
    s=time.perf_counter()
    with tempfile.TemporaryDirectory() as td:
        root=Path(td);shutil.copytree(source,root/'click',ignore=shutil.ignore_patterns('__pycache__'))
        runner=root/'runner.py';runner.write_text(instrumented)
        env={**os.environ,'PYTHONPATH':str(root),'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0','LC_ALL':'C.UTF-8'}
        def invoke(c):
            q=subprocess.run([sys.executable,str(runner),'--child',json.dumps(c)],cwd=root,env=env,capture_output=True,text=True,check=True,timeout=20)
            return json.loads(q.stdout)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            rows=list(pool.map(invoke,CASES+CASES))
    controls={r['case']:r for r in rows[:4]};rep={r['case']:r for r in rows[4:]}
    unstable={n:sorted(changes(r,rep[n])) for n,r in controls.items()}
    assert all(not v for v in unstable.values())
    assert all(controls[n]['outcome']==rep[n]['outcome'] for n in controls)
    added=(set.union(*(predictions(r)[1] for r in controls.values()))&U)-suite
    enlarged=suite|added
    result={'baseline_named':len(suite),'expanded_named':len(enlarged),'added':sorted(added),'control_outcomes':{n:r['outcome'] for n,r in controls.items()},'unstable':unstable,'seconds':time.perf_counter()-s,'reports':{}}
    for m,v in base_result['reports'].items():
        actual=set(v['suite_actual']);result['reports'][m]={'original':stats(suite,actual),'expanded':stats(enlarged,actual),'remaining_miss':sorted(actual-enlarged),'added_tp':sorted(added&actual),'added_fp':sorted(added-actual)}
    (ROOT/'cia_controls_traces.json').write_text(json.dumps({'controls':controls,'repeat':rep},separators=(',',':'))+'\n')
    (ROOT/'cia_controls_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
