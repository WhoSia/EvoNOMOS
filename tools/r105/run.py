"""R105 native differential/benchmark; python run.py live.go snapshot.go [--profile]."""
import hashlib
import os
from pathlib import Path
import random
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
SHAS = {'live':'ad9a2fbc0a30a39475f746068e74e2d3e6c93999','snapshot':'e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75'}
LOWER = '''func lowerPattern(p Pattern) Pattern {
 p.prefix = strings.ToLower(p.prefix)
 p.suffix = strings.ToLower(p.suffix)
 return p
}
func normalizedMatch(p Pattern, value string) bool { return lowerPattern(p).Match(value) }
'''
DUP = '''func normalizedRouteMatch(r HeaderRoute, value string) bool {
 if len(r.MatchAny)>0 {
  for _, m := range r.MatchAny { if normalizedMatch(m, value) { return true } }
  return false
 }
 return normalizedMatch(r.MatchOne, value)
}
'''


def replace(s, old, new):
    assert s.count(old) == 1, old
    return s.replace(old, new)


def patch(s, mode):
    if mode == 'dup':
        return replace(s, 'matcher.IsMatch(value)', 'normalizedRouteMatch(matcher, value)') + '\n' + LOWER + DUP
    if mode == 'shared':
        s = replace(s, 'matcher.IsMatch(value)', 'matcher.matchWith(value, normalizedMatch)')
        s = replace(s, 'func (r HeaderRoute) IsMatch(value string) bool {', 'func (r HeaderRoute) IsMatch(value string) bool { return r.matchWith(value, Pattern.Match) }\nfunc (r HeaderRoute) matchWith(value string, match func(Pattern,string)bool) bool {')
        s = replace(s, 'm.Match(value)', 'match(m,value)')
        return replace(s, 'r.MatchOne.Match(value)', 'match(r.MatchOne,value)') + '\n' + LOWER
    if mode == 'compile':
        s = replace(s, 'copyMatchers[i].MatchAny = append([]Pattern(nil), m.MatchAny...)', 'copyMatchers[i].MatchAny = append([]Pattern(nil), m.MatchAny...)\n copyMatchers[i].MatchOne = lowerPattern(m.MatchOne)\n for j,p := range copyMatchers[i].MatchAny { copyMatchers[i].MatchAny[j] = lowerPattern(p) }')
        return s + '\n' + LOWER.split('func normalizedMatch')[0]
    raise ValueError(mode)


def main(paths):
    sources = {}
    for arm, path in zip(SHAS, paths, strict=True):
        data = Path(path).read_bytes()
        assert hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()==SHAS[arm]
        sources[arm] = data.decode()
    env = {**os.environ,'GO111MODULE':'off','GOMAXPROCS':'1'}
    def run(cmd, cwd, arm):
        return subprocess.run(cmd,cwd=cwd,env={**env,'EVO_ARM':arm},text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=True).stdout
    with tempfile.TemporaryDirectory() as d:
        root=Path(d); binaries={}
        def build(arm, mode, source):
            p=root/f'{arm}-{mode}';p.mkdir()
            (p/'route.go').write_text(patch(source,mode))
            (p/'probe_test.go').write_bytes((ROOT/'probe_test.go.txt').read_bytes())
            run(['go','test','-c','-o','probe'],p,arm)
            return p
        for arm in sources:
            p=build(arm,'dup',sources[arm]);binaries[arm,'dup']=p
            print('TEST',arm,'dup',run(['./probe','-test.v'],p,arm),flush=True)
        p=binaries['snapshot','dup']
        print('BASE PROFILE',run(['./probe','-test.run=^$','-test.bench=^BenchmarkServeMiss64$','-test.benchtime=500ms','-test.cpuprofile=cpu.out'],p,'snapshot'),flush=True)
        print(run(['go','tool','pprof','-top','-cum','-nodecount=10','probe','cpu.out'],p,'snapshot'),flush=True)
        for arm in sources:
            for mode in ('shared','compile') if arm=='snapshot' else ('shared',):
                p=build(arm,mode,sources[arm]);binaries[arm,mode]=p
                print('TEST',arm,mode,run(['./probe','-test.v'],p,arm),flush=True)
        # Freeze a LIVE registry using the SNAPSHOT construction: intentional negative control.
        p=build('live','compile',sources['snapshot'])
        bad=subprocess.run(['./probe','-test.run=TestMutation','-test.v'],cwd=p,env={**env,'EVO_ARM':'live'},text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        assert bad.returncode!=0 and 'slice visibility' in bad.stdout,bad.stdout
        print('EXPECTED_NEGATIVE',bad.stdout,flush=True)
        rng=random.Random(105)
        for rep in range(5):
            order=list(binaries);rng.shuffle(order)
            for arm,mode in order:
                p=binaries[arm,mode]
                out=run(['./probe','-test.run=^$','-test.bench=Benchmark','-test.benchtime=100ms','-test.benchmem'],p,arm)
                for line in out.splitlines():
                    if line.startswith('Benchmark'):print('BENCH',rep,arm,mode,line,flush=True)

if __name__=='__main__':main(sys.argv[1:])
