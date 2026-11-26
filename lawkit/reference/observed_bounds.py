"""Check pinned R114-format receipts and bound repair cost under hidden observations."""
import argparse
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile
from repair_budget import best


def states(spec, unknown):
    def check(obs, names):
        return all(unknown if obs[n] is None else obs[n] for n in names)
    return {s: {'safe':check(row['observations'],spec['protected']),
                'goals':[g for g,ns in spec['goals'].items() if check(row['observations'],ns)]}
            for s,row in spec['snapshots'].items()}


def receipt(data, expected_sha):
    if hashlib.sha256(data).hexdigest()!=expected_sha:
        raise ValueError('archive digest mismatch')
    with ZipFile(io.BytesIO(data)) as z:
        names=z.namelist()
        if len(names)!=len(set(names)):
            raise ValueError('duplicate archive entry')
        hashes=json.loads(z.read('evidence_manifest.json'))['files']
        if set(names)!=set(hashes)|{'evidence_manifest.json'}:
            raise ValueError('archive inventory mismatch')
        for name,digest in hashes.items():
            if hashlib.sha256(z.read(name)).hexdigest()!=digest:
                raise ValueError('entry digest mismatch: '+name)
        spec=json.loads(z.read('results/manifest.json'))
        model=json.loads(z.read('results/model.json'))
        required=set(spec['protected'])|{n for ns in spec['goals'].values() for n in ns}
        for s,row in spec['snapshots'].items():
            obs={}
            for line in z.read(f'results/{s}.log').decode().splitlines():
                if line.startswith('OBS '):
                    _,key,value=line.split()
                    if key in obs or value not in ('true','false'):
                        raise ValueError('invalid observation log')
                    obs[key]=value=='true'
            declared=row['observations']
            if not required<=obs.keys() or any(type(v) is not bool for v in declared.values()) or obs!=declared:
                raise ValueError('log/manifest observation mismatch: '+s)
        if states(spec,False)!=model['states'] or spec['allowed_owners']!=model['allowed_owners'] or spec['transitions']!=[e[:2] for e in model['edges']]:
            raise ValueError('manifest/model mismatch')
    return spec,model


def bounds(spec, model, start, goal, candidates, budget):
    if type(budget) is not int or budget < 0:
        raise ValueError('budget must be a nonnegative integer')
    if not isinstance(candidates,list) or not all(isinstance(x,str) for x in candidates):
        raise ValueError('candidates must be owner strings')
    for row in spec['snapshots'].values():
        if any(v is not None and type(v) is not bool for v in row['observations'].values()):
            raise ValueError('observations must be Boolean or null')
    if start not in spec['snapshots'] or goal not in spec['goals']:
        raise ValueError('unknown start or goal')
    def solve(value):
        m={**model,'states':states(spec,value)}
        return best(m,start,goal,candidates,budget) if m['states'][start]['safe'] else None
    low,high=solve(True),solve(False)
    return {'optimistic':low,'pessimistic':high,
            'exact_cost':(None if low is None else low['cost'])==(None if high is None else high['cost']),
            'scope':'fixed declared graph; independent Boolean completions; null option means no path'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive',type=Path);p.add_argument('sha256');p.add_argument('start');p.add_argument('goal')
    p.add_argument('--candidate-owner',action='append',default=[])
    p.add_argument('--max-additional-owners',type=int,required=True)
    p.add_argument('--hide',action='append',default=[],metavar='STATE:OBS')
    a=p.parse_args()
    try:
        spec,model=receipt(a.archive.read_bytes(),a.sha256)
        for key in a.hide:
            s,o=key.split(':',1)
            if o not in spec['snapshots'][s]['observations']:
                raise ValueError('unknown observation: '+key)
            spec['snapshots'][s]['observations'][o]=None
        result=bounds(spec,model,a.start,a.goal,a.candidate_owner,a.max_additional_owners)
    except (ValueError,KeyError,TypeError,OSError) as exc:
        p.error(str(exc))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
