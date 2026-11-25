"""R105-C: held-out lifecycle check of R105-A component-time predictions.
Run: python lifecycle.py snapshot.go
Only same-snapshot, same-contract dup vs compile. No length optimization.
"""
import hashlib
import os
from pathlib import Path
import random
import subprocess
import sys
import tempfile
from run import ROOT, SHAS, patch

BENCH = '''
func BenchmarkLifecycle(b *testing.B){
 for _,c:=range []struct{name string;n int;value string;code int}{
  {"none",0,"no-match",204}, {"miss1",1,"no-match",204}, {"miss2",2,"no-match",204}, {"miss8",8,"no-match",204},
  {"hit16",16,"mixed-pattern-with-uppercase-yes-suffix",201}, {"hit32",32,"mixed-pattern-with-uppercase-yes-suffix",201},
  {"hit64",64,"mixed-pattern-with-uppercase-yes-suffix",201}, {"hit128",128,"mixed-pattern-with-uppercase-yes-suffix",201}, {"hit256",256,"mixed-pattern-with-uppercase-yes-suffix",201},
 } {b.Run(c.name,func(b *testing.B){
  hr:=registry();q:=httptest.NewRequest("GET","/",nil);q.Header.Set("X-Test",c.value);w:=&sink{}
  b.ReportAllocs();b.ResetTimer();for i:=0;i<b.N;i++{h:=hr.Handler(next);for j:=0;j<c.n;j++{h.ServeHTTP(w,q)};built=h}
  if c.n>0&&w.code!=c.code{b.Fatal(w.code)}
 })}
}
'''
# Fixed from A component medians/ranges BEFORE this lifecycle run.
PREDICT = {'none':'dup','miss1':'abstain','miss2':'compile','miss8':'compile','hit16':'dup','hit32':'dup','hit64':'abstain','hit128':'compile','hit256':'compile'}


def main(path):
    data=Path(path).read_bytes()
    assert hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()==SHAS['snapshot']
    env={**os.environ,'GO111MODULE':'off','GOMAXPROCS':'1','EVO_ARM':'snapshot'}
    def run(cmd,p):
        r=subprocess.run(cmd,cwd=p,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if r.returncode:print(r.stdout,flush=True);r.check_returncode()
        return r.stdout
    print('PRESET',PREDICT,flush=True)
    with tempfile.TemporaryDirectory() as d:
        modes=('dup','compile');bins={}
        for mode in modes:
            p=Path(d)/mode;p.mkdir();bins[mode]=p
            (p/'route.go').write_text(patch(data.decode(),mode))
            (p/'probe_test.go').write_text((ROOT/'probe_test.go.txt').read_text()+BENCH)
            run(['go','test','-c','-o','probe'],p)
            print('TEST',mode,run(['./probe','-test.v'],p),flush=True)
        rng=random.Random(1053)
        for rep in range(5):
            order=list(modes);rng.shuffle(order)
            for mode in order:
                out=run(['./probe','-test.run=^$','-test.bench=^BenchmarkLifecycle$','-test.benchtime=80ms','-test.benchmem'],bins[mode])
                for line in out.splitlines():
                    if line.startswith('BenchmarkLifecycle/'):print('LIFE',rep,mode,line,flush=True)

if __name__=='__main__':main(sys.argv[1])
