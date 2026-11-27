"""Test-bounded PI/EAS adaptation, not full statement-level DEA or new law."""
import concurrent.futures
import ast, collections, hashlib, json, os, pathlib, shutil, subprocess, sys, tempfile, time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SEED='decorators.py:help_option'

def child():
    import click
    from click.testing import CliRunner
    root=Path(click.__file__).resolve().parent
    assert root == Path.cwd()/'click'
    name,kind,decls,argv,opts0=json.loads(sys.argv[2]); events=[]; trace=[]; ret=collections.defaultdict(list)
    class Custom(click.Option): pass
    class HelpSubclass(click.HelpOption): pass
    def mark(ctx,param,value): events.append('custom_callback')
    def command(): events.append('command'); click.echo('COMMAND')
    opts=dict(opts0)
    if opts.get('callback')=='MARK': opts['callback']=mark
    if kind=='custom': opts['cls']=Custom
    elif kind=='help_subclass': opts['cls']=HelpSubclass
    prefix=str(root)+os.sep
    def key(f):
        filename=f.f_code.co_filename
        if filename.startswith(prefix): return filename[len(prefix):]+':'+f.f_code.co_qualname
    def signature(v):
        # Never inspect arbitrary objects or repr; nonprimitive values deliberately opaque.
        if type(v) in (type(None),bool,int,float,str): return ['scalar',type(v).__name__,v]
        if type(v) in (tuple,list) and len(v)<=64 and all(type(x) in (type(None),bool,int,float,str) for x in v): return ['sequence',type(v).__name__,list(v)]
        return ['opaque',type(v).__module__,type(v).__qualname__]
    def profile(frame,event,arg):
        if event not in ('call','return'): return
        k=key(frame)
        if k:
            if event=='call': trace.append(['enter',k])
            else:
                ret[k].append(signature(arg))
        if event=='return' and frame.f_back is not None:
            p=key(frame.f_back)
            if p: trace.append(['resume',p])
    sys.setprofile(profile)
    try:
        if kind!='auto': command=click.help_option(*decls,**opts)(command)
        cmd=click.command(name='probe')(command)
        r=CliRunner().invoke(cmd,argv,catch_exceptions=True)
        outcome=dict(exit=r.exit_code,output=r.output,events=events,exception=type(r.exception).__name__ if r.exception else None)
    except Exception as e: outcome=dict(construction_error=type(e).__name__,message=str(e),events=events)
    finally: sys.setprofile(None)
    print(json.dumps(dict(case=name,trace=trace,returns=dict(ret),outcome=outcome),sort_keys=True))

def universe(source):
    # Method identity ignores line shifts, nested function identities included.
    out=set()
    for p in source.rglob('*.py'):
        def walk(node,qual=''):
            for n in ast.iter_child_nodes(node):
                if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
                    q=qual+n.name; out.add(str(p.relative_to(source))+':'+q); walk(n,q+'.<locals>.')
                elif isinstance(n,ast.ClassDef): walk(n,qual+n.name+'.')
                else: walk(n,qual)
        walk(ast.parse(p.read_text()))
    return out

def predictions(run):
    t=run['trace']; coverage={k for e,k in t if e=='enter'}
    starts=[i for i,(e,k) in enumerate(t) if e=='enter' and k==SEED]
    eas={k for e,k in t[starts[0]:]} if starts else set()
    return coverage,eas

def stats(pred,actual):
    tp=len(pred&actual);fp=len(pred-actual);fn=len(actual-pred)
    return dict(tp=tp,fp=fp,fn=fn,precision=tp/(tp+fp) if tp+fp else None,recall=tp/(tp+fn) if tp+fn else None,f1=2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else None)

def changes(a,b):
    ca=collections.Counter(k for e,k in a['trace'] if e=='enter'); cb=collections.Counter(k for e,k in b['trace'] if e=='enter')
    return {k for k in ca.keys()|cb.keys()|a['returns'].keys()|b['returns'].keys() if ca[k]!=cb[k] or a['returns'].get(k)!=b['returns'].get(k)}

def main():
    import click, importlib.metadata as md
    assert md.version('click')=='8.1.8'
    src=Path(click.__file__).parent
    pins={'core.py':'e6305011adf3f7450fa1e9392147e52b8acf2b0c','decorators.py':'bcf8906e7098a3cf82bdd87855c410e86f4f4279','parser.py':'600b8436d7c1e833cb3c5efea898b42d15d920c0','testing.py':'772b2159ccd95d29d8d940fc818d3bb1d2610cbf'}
    for p,h in pins.items():
        raw=(src/p).read_bytes(); assert hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()==h
    # Extract only the source construction section of the earlier runner, not its test execution.
    prior=(ROOT/'isolated_patch.py').read_text(); section=prior[prior.index('HERE ='):prior.index('# Child script')]
    ns=dict(__file__=str(ROOT/'isolated_patch.py'),Path=Path,click=click,json=json)
    exec(compile(section,'prior-local-research-runner','exec'),ns)
    variants={'base':ns['SOURCE'],'repeat':ns['SOURCE'],'patched':ns['PATCHED'],'old_transplant':ns['OLD_TRANSPLANT']}
    cases=ast.literal_eval(next(n.value for n in ast.parse((ROOT/'click_help_probe.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CASES' for t in n.targets)))
    U=universe(src); runs={}; runtime={}
    for mode,code in variants.items():
        start=time.perf_counter(); rows={}
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);shutil.copytree(src,root/'click',ignore=shutil.ignore_patterns('__pycache__'));(root/'click'/'decorators.py').write_text(code)
            env={**os.environ,'PYTHONPATH':str(root),'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0','LC_ALL':'C.UTF-8'}
            def invoke(c):
                p=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--child',json.dumps(c)],cwd=root,env=env,capture_output=True,text=True,check=True,timeout=20)
                return json.loads(p.stdout)
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
                for r in pool.map(invoke,cases): rows[r['case']]=r
        runs[mode]=rows;runtime[mode]=time.perf_counter()-start
        print(mode, runtime[mode], len(rows),flush=True)
        (ROOT/'cia_partial.json').write_text(json.dumps(runs,separators=(',',':'))+'\n')
    base=runs['base'];repeat=runs['repeat']
    unstable={n:changes(base[n],repeat[n]) for n in base}; assert all(base[n]['outcome']==repeat[n]['outcome'] for n in base)
    # Scope is fixed preexisting named functions/methods. Comprehensions/module bodies and new functions are reported separately.
    suite_cov=set.union(*(predictions(r)[0] for r in base.values()));suite_eas=set.union(*(predictions(r)[1] for r in base.values()))
    reports={}
    for mode in ['patched','old_transplant']:
        rows=[]; union_actual=set(); union_unstable=set.union(*unstable.values()); changed_out=[]
        for n,a in base.items():
            b=runs[mode][n]; diff=changes(a,b); eligible=U-unstable[n]; actual=diff&eligible;union_actual|=actual
            coverage,eas=predictions(a)
            if a['outcome']!=b['outcome']: changed_out.append(n)
            rows.append(dict(case=n,actual=sorted(actual),outside_named_universe=sorted(diff-U),unstable=sorted(unstable[n]),metrics={k:stats(v&eligible,actual) for k,v in {'coverage':coverage,'eas':eas,'suite_coverage':suite_cov,'suite_eas':suite_eas}.items()}))
        eligible=U-union_unstable;union_actual&=eligible
        reports[mode]=dict(rows=rows,changed_cli_cases=changed_out,suite_actual=sorted(union_actual),suite_metrics={k:stats(v&eligible,union_actual) for k,v in {'coverage':suite_cov,'eas':suite_eas,'all_named':U}.items()})
    result=dict(pins=pins,universe_size=len(U),suite_coverage_count=len(suite_cov&U),suite_eas_count=len(suite_eas&U),unstable={n:sorted(v) for n,v in unstable.items()},runtime_seconds=runtime,reports=reports,scope='preexisting AST-named methods only; profile call counts and ordered return signatures, no statement values; outside universe reported; baseline repeated; 12 historical cases; no independent outcome')
    (ROOT/'cia_traces.json').write_text(json.dumps(runs,ensure_ascii=False,separators=(',',':'))+'\n');(ROOT/'cia_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='reports'},indent=2));print(json.dumps({m:{k:v for k,v in r.items() if k!='rows' and k!='suite_actual'} for m,r in reports.items()},indent=2))
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='--child':child()
    else:main()
