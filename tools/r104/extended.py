"""R104-B: extend the native observation court to public HeaderRoute and aliasing.
Run beside run.py and extended_probe.go.txt with the same exact source inputs.
The goal/protection predicates and edit permissions are researcher-defined.
"""
from pathlib import Path
import os, subprocess, tempfile, sys
from run import EXPECTED, OPS, blob_sha

ROOT = Path(__file__).resolve().parent
NORMALIZE = '''func normalizedMatch(p Pattern, value string) bool {
 p.prefix = strings.ToLower(p.prefix)
 p.suffix = strings.ToLower(p.suffix)
 return p.Match(value)
}
'''
HANDLER_HELPER = '''func normalizedRouteMatch(r HeaderRoute, value string) bool {
 if len(r.MatchAny)>0 {
  for _, m := range r.MatchAny { if normalizedMatch(m, value) { return true } }
  return false
 }
 return normalizedMatch(r.MatchOne, value)
}
'''
CANDIDATES = {**OPS,
 'ismatch_lower': [('m.Match(value)', 'normalizedMatch(m, value)'), ('r.MatchOne.Match(value)', 'normalizedMatch(r.MatchOne, value)')],
 'handler_lower': [('matcher.IsMatch(value)', 'normalizedRouteMatch(matcher, value)')],
}
PROTECTED = ('direct','ismatch','ismatchany','after')
ROUTE = tuple(f'{m}{i}' for m in ('route','any','raw','rawany') for i in range(2))


def execute(data, op):
    src = data.decode('utf-8')
    for old, new in CANDIDATES[op]:
        assert src.count(old)==1,(op,old)
        src=src.replace(old,new)
    if op in ('ismatch_lower','handler_lower'):
        src+='\n'+NORMALIZE
    if op=='handler_lower':
        src+='\n'+HANDLER_HELPER
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)
        (p/'route.go').write_text(src,encoding='utf-8')
        (p/'probe_test.go').write_bytes((ROOT/'extended_probe.go.txt').read_bytes())
        out=subprocess.check_output(['go','test','-v','-count=1','.'],cwd=d,env={**os.environ,'GO111MODULE':'off'},text=True,stderr=subprocess.STDOUT)
    rows=[line.split()[1:] for line in out.splitlines() if line.startswith('OBS ')]
    obs={tuple(r[:3]):r[3] for r in rows}
    keys={(m,str(i),str(j)) for m in PROTECTED+ROUTE for i in range(8) for j in range(11)}
    assert len(rows)==len(obs)==len(keys) and set(obs)==keys
    return obs


def main(paths):
    if len(paths)!=2: raise SystemExit(__doc__)
    results={}
    for arm,path in zip(EXPECTED,paths):
        data=Path(path).read_bytes()
        assert blob_sha(data)==EXPECTED[arm]
        for op in CANDIDATES:
            results[arm,op]=execute(data,op)
        base=results[arm,'base']
        target=results[arm,'constructor'] # explicitly comparison target, not independent requirement
        accepted=[]
        for op in CANDIDATES:
            x=results[arm,op]
            protect=all(x[k]==base[k] for k in base if k[0] in PROTECTED)
            meet=all(x[k]==target[k] for k in target if k[0] in ROUTE)
            print(arm,op,'protect',protect,'target',meet)
            if protect and meet: accepted.append(op)
        assert accepted==['handler_lower'],accepted
        print('ACCEPTED',arm,accepted)
    for op in CANDIDATES:
        assert results['live',op]==results['snapshot',op]
    print('PASS',len(results),'Go runs',sum(map(len,results.values())),'observations')


if __name__=='__main__':
    main(sys.argv[1:])
