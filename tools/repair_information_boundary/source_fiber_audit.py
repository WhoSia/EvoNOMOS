import json, sys, zipfile, hashlib
from collections import defaultdict, Counter
from itertools import combinations
from pathlib import Path


def audit(rows):
    groups = defaultdict(list)
    for key, obs, menu, signature in rows:
        groups[obs].append((key, menu))
    fibers = []
    for obs, members in sorted(groups.items(), key=lambda x: str(x[0])):
        menus = [m for _, m in members]
        nonempty = all(menus)
        pair = nonempty and all(a & b for a,b in combinations(menus,2))
        common = set.intersection(*menus)
        fibers.append(dict(observation=obs, worlds=len(members), menus=sorted({tuple(sorted(m)) for m in menus}), empty_worlds=sum(not m for m in menus), common=sorted(common), helly_gap=bool(pair and not common)))
    return dict(scenarios=len(rows), behavior_signatures=len({r[3] for r in rows}), fibers=len(fibers), empty_menu_fibers=sum(f['empty_worlds']>0 for f in fibers), helly_gaps=sum(f['helly_gap'] for f in fibers), detail=fibers, independent_demands=None, statistical_effective_n=None)


def main(root):
    p = lambda n: root / ('EvoNOMOS_'+n+'_evidence.zip')
    paths = {n:p(n) for n in ('contract_escape','requests_contract_lifecycle','R114')}
    with zipfile.ZipFile(paths['contract_escape']) as z:
        def load(arm):
            rows = {}
            for line in z.read('results/'+arm+'.log').decode().splitlines():
                if line.startswith('ESC '):
                    v = tuple(map(int,line.split()[1:])); assert len(v)==8 and v[:4] not in rows
                    rows[v[:4]]=v[4:]
            assert len(rows)==640
            return rows
        arms = ('global','bypass','fallback'); data={a:load(a) for a in (*arms,'independent')}
        assert all(set(x)==set(data['independent']) for x in data.values())
        rows = [(k,data['global'][k],{a for a in arms if data[a][k]==want},tuple(data[a][k] for a in (*arms,'independent'))) for k,want in data['independent'].items()]
        escape=audit(rows); escape['status_observations']=640*4*4
        hybrid_rows=[]
        for k in data['independent']:
            a,b=data['global'][k][0],data['independent'][k][1]
            both=204 if a==b==204 else 415
            want=(a,b,both,both)
            hybrid_rows.append((k,data['global'][k],{c for c in arms if data[c][k]==want},(want,*(data[c][k] for c in arms))))
        hybrid=audit(hybrid_rows)
        assert all(not f['empty_worlds'] for f in hybrid['detail'])
    with zipfile.ZipFile(paths['requests_contract_lifecycle']) as z:
        def load(arm,stage):
            data=json.loads(z.read('out/'+arm+'_'+stage+'.json'))['cases']
            d={r['raw']:r for r in data}; assert len(d)==len(data)==81
            return d
        base=load('local','base'); arms=('local','parser','policy'); data={a:load(a,'case-boundary') for a in arms}
        assert all(set(x)==set(base) for x in data.values())
        def freeze(x): return json.dumps(x,sort_keys=True)
        def sig(r): return (r['direct'],r['adapter'],r['raw_token'],freeze(r['params']))
        rows=[]
        for k,b in base.items():
            want=data['local'][k]['want']; target=(want,want,b['raw_token'],freeze(b['params']))
            rows.append((k,(b['direct'],b['adapter']),{a for a in arms if sig(data[a][k])==target},(sig(b),target,*(sig(data[a][k]) for a in arms))))
        requests=audit(rows)
    with zipfile.ZipFile(paths['R114']) as z:
        d=json.loads(z.read('results/model.json'))
        rows=[]
        for g in ('public','full'):
            m={a for a,v in d['states'].items() if v['safe'] and g in v['goals']}
            rows.append((g,(True,),m,tuple(sorted(m))))
        clone=audit(rows)
        clone['rights_note']='All observed candidate snapshots; hypothetical app-only authority excludes merged and yields empty full menu, not a Helly gap.'
    result={'scope':'Retrospective observed candidate menus only; no statistical n_eff estimate or independent new demand; fibers depend on explicitly chosen observer.', 'sha256':{n:hashlib.sha256(p.read_bytes()).hexdigest() for n,p in paths.items()}, 'chi_escape_full_reference':escape,'chi_escape_original_hybrid':hybrid,'requests':requests,'chi_clone':clone}
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':main(Path(sys.argv[1]))
