"""Compile explicit snapshot evidence into a finite LawKit graph, not source inference."""
import argparse
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path, PurePosixPath


def blob(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def read(root, path):
    p = PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError('invalid relative source path')
    f = (root / p).resolve(strict=True)
    if not f.is_relative_to(root.resolve()):
        raise ValueError('source escapes evidence root')
    return f.read_bytes()


def line_cost(a, b):
    return sum(i2-i1+j2-j1 for op,i1,i2,j1,j2 in SequenceMatcher(
        None, a.splitlines(keepends=True), b.splitlines(keepends=True), autojunk=False).get_opcodes() if op!='equal')


def compile_model(spec, root):
    protected, goals = spec['protected'], spec['goals']
    names = set(protected) | {x for requirements in goals.values() for x in requirements}
    if not protected or not goals or any(not r for r in goals.values()):
        raise ValueError('nonempty protected observations and goals required')
    states, files = {}, {}
    for name, row in spec['snapshots'].items():
        actual = {p: read(root, f['file']) for p,f in row['files'].items()}
        if {p:blob(d) for p,d in actual.items()} != {p:f['blob'] for p,f in row['files'].items()}:
            raise ValueError('source blob mismatch: '+name)
        obs = row['observations']
        if not names <= obs.keys() or any(type(obs[n]) is not bool for n in names):
            raise ValueError('missing or non-Boolean observation: '+name)
        files[name] = actual
        states[name] = {'safe':all(obs[n] for n in protected),
                        'goals':[g for g, req in goals.items() if all(obs[n] for n in req)]}
    edges, evidence = [], []
    for u,v in spec['transitions']:
        a,b = files[u],files[v]
        changed = sorted(p for p in a.keys()|b.keys() if a.get(p)!=b.get(p))
        owners = {spec['path_owners'][p] for p in changed}
        if len(owners)!=1:
            raise ValueError('transition must change files assigned to exactly one owner')
        costs = {p:line_cost(a.get(p,b''),b.get(p,b'')) for p in changed}
        total = sum(costs.values())
        if total<=0:
            raise ValueError('zero line edit cost')
        edges.append([u,v,owners.pop(),total])
        evidence.append({'edge':len(edges)-1,'changed_files':costs})
    return {'states':states,'allowed_owners':spec['allowed_owners'],'edges':edges,
            'evidence':evidence,'scope':'verified source bytes; supplied finite observations, declared transitions and hypothetical ownership; line edits are not labor'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('manifest', type=Path)
    a = p.parse_args()
    try:
        print(json.dumps(compile_model(json.loads(a.manifest.read_text()),a.manifest.parent),indent=2))
    except (ValueError,KeyError,TypeError,OSError) as exc:
        p.error(str(exc))


if __name__=='__main__':
    main()
