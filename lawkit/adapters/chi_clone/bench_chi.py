"""Benchmark common public observations, not full-capability equivalence."""
import json
import os
from pathlib import Path
import random
import subprocess
import tempfile
import sys
from statistics import median
from observed_repair import blob, compile_model

ROOT=Path(__file__).resolve().parent

def main(root):
    spec=json.loads((root/'manifest.json').read_text())
    compile_model(spec,root)
    env={**os.environ,'GOTOOLCHAIN':'local','GOPROXY':'off','GOMAXPROCS':'1'}
    with tempfile.TemporaryDirectory() as d:
        bins={};times={}
        for name in ('local','merged'):
            p=Path(d)/name;p.mkdir();(p/'client').mkdir()
            (p/'go.mod').write_text('module example.org/chi\n\ngo 1.23\n')
            (p/'shim.go').write_text('package chi\ntype Routes interface{}\ntype methodTyp uint\n')
            for path,f in spec['snapshots'][name]['files'].items():
                (p/path).write_bytes((root/f['file']).read_bytes())
            (p/'client/bench_test.go').write_bytes((ROOT/'bench_probe.go.txt').read_bytes())
            subprocess.run(['go','test','-c','-o','probe','./client'],cwd=p,env=env,check=True)
            bins[name]=p
        rng=random.Random(114)
        for rep in range(7):
            order=list(bins);rng.shuffle(order)
            for name in order:
                s=subprocess.check_output(['./probe','-test.run=^$','-test.bench=BenchmarkCapture','-test.benchtime=60ms','-test.benchmem'],cwd=bins[name],env=env,text=True)
                for line in s.splitlines():
                    if line.startswith('BenchmarkCapture/'):
                        print(rep,name,line,flush=True)
                        f=line.split();key=(name,f[0].split('/')[1]);times.setdefault(key,[]).append(float(f[2]))
        for (name,n),v in sorted(times.items()):
            assert len(v)==7
            print(json.dumps({'mode':name,'n':n,'median_ns':median(v),'raw_ns':v}))

if __name__=='__main__':main(Path(sys.argv[1]))
