"""Benchmark the previously tested candidates, not end-to-end HTTP latency."""
import hashlib, importlib.util, json, os, re, shutil, statistics, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def blob(b): return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()

def main(r118root,evidence,out):
    spec=importlib.util.spec_from_file_location('r118',r118root/'run.py');r118=importlib.util.module_from_spec(spec);spec.loader.exec_module(r118)
    for name,expected in r118.EXPECTED.items():assert blob((r118root/name).read_bytes())==expected,name
    assert blob((r118root/'run.py').read_bytes())=='e80d34d96ba4762be0fa710908270382477e610c'
    out.mkdir(parents=True,exist_ok=False)
    env={**os.environ,'GOTOOLCHAIN':'local','GOPROXY':'off','GOMAXPROCS':'2'}
    results={}
    for name in ('bypass','fallback'):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);r118.stage('shared',('global',),p)
            shutil.copyfile(evidence/(name+'_charset.go.txt'),p/'content_charset.go')
            assert blob((p/'content_charset.go').read_bytes())=={'bypass':'7ecb4a2d5e91d7ef775f824e64f2210bf360e5f2','fallback':'cb98dc9abc188d17699260e72c57025f5ca49261'}[name]
            assert blob((p/'content_media_parse.go').read_bytes())=='d98e83b024d48a38dd50279a4330ecc43019c214'
            assert blob((p/'content_type.go').read_bytes())=='38291a21754805ad0c6b8510dbcf3935a4029f6e'
            shutil.copyfile(ROOT/'bench.go.txt',p/'bench_test.go')
            r=subprocess.run(['go','test','-run','^$','-bench','^BenchmarkEscape$','-benchmem','-benchtime=100ms','-count=5','.'],cwd=p,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (out/(name+'.log')).write_text(r.stdout);r.check_returncode()
            rows={}
            for line in r.stdout.splitlines():
                m=re.match(r'BenchmarkEscape/(\w+)-\d+\s+\d+\s+([\d.]+) ns/op\s+(\d+) B/op\s+(\d+) allocs/op',line)
                if m:rows.setdefault(m[1],[]).append(tuple(map(float,m.groups()[1:])))
            assert set(rows)=={'slash','token','malformed','empty'} and all(len(v)==5 for v in rows.values())
            results[name]={k:{'ns_median':statistics.median(x[0] for x in v),'ns_range':[min(x[0] for x in v),max(x[0] for x in v)],'bytes_median':statistics.median(x[1] for x in v),'allocs_median':statistics.median(x[2] for x in v)} for k,v in rows.items()}
    (out/'result.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n');print(json.dumps(results,indent=2,sort_keys=True))

if __name__=='__main__':main(*(Path(x).resolve() for x in sys.argv[1:]))
