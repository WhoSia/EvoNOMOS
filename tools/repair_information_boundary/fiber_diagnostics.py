"""Retrospective diagnostics; projection counts are not statistical effective n."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json, sys, zipfile, hashlib

KEYS = ('header','body','type_allowlist','charset_allowlist')
ARMS = ('independent','global','bypass','fallback')
OUTPUTS = ('type','charset','ab','ba')


def subsets(items):
    return [s for k in range(len(items)+1) for s in combinations(items,k)]


def determinants(rows, i):
    valid = []
    for axes in subsets(range(4)):
        if any(set(a) <= set(axes) for a,_ in valid):
            continue
        lookup = {}
        for key, vec in rows.items():
            k = tuple(key[j] for j in axes)
            if k in lookup and lookup[k] != vec[i]:
                break
            lookup[k] = vec[i]
        else:
            valid.append((axes,len(lookup)))
    return [{'axes':[KEYS[j] for j in a],'projected_keys':n} for a,n in valid]


def classify(menus):
    unique = {frozenset(m) for m in menus}
    common = set.intersection(*(set(m) for m in unique))
    if common: status = 'UNIVERSAL_WITHIN_FIBER'
    elif not all(unique): status = 'EMPTY_MENU'
    elif len(unique) < 3: status = 'TRIVIAL_FEWER_THAN_THREE'
    elif not all(a & b for a,b in combinations(unique,2)): status = 'PAIRWISE_FAILURE'
    else: status = 'HELLY_GAP'
    return status,sorted(common)


def main(root, audit_file):
    archive = root/'EvoNOMOS_contract_escape_evidence.zip'
    assert hashlib.sha256(archive.read_bytes()).hexdigest()=='5a4a52127a415b84ea77c4634bae8e947804e6a063d8a786732ccbd6816261d8'
    by_arm = {}
    with zipfile.ZipFile(archive) as z:
        for arm in ARMS:
            rows={}
            for line in z.read('results/'+arm+'.log').decode().splitlines():
                if line.startswith('ESC '):
                    x=tuple(map(int,line.split()[1:])); assert len(x)==8 and x[:4] not in rows
                    rows[x[:4]]=x[4:]
            assert len(rows)==640
            by_arm[arm]={'raw_checks':4*len(rows),'outcome_vectors':len(set(rows.values())), 'minimal_determinants':{name:determinants(rows,i) for i,name in enumerate(OUTPUTS)},'conjunction_violations':sum(v[2:]!=(204,204) if v[:2]==(204,204) else v[2:]!=(415,415) for v in rows.values())}
    source=json.loads(audit_file.read_text()); groups={}
    for name in ('chi_escape_original_hybrid','chi_escape_full_reference','requests','chi_clone'):
        fs=source[name]['detail']; alphabet=sorted({a for f in fs for m in f['menus'] for a in m}); allmenus=[set(m) for f in fs for m in f['menus']]; universal=sorted(set.intersection(*allmenus)); mask_results=[]
        for mask in subsets(alphabet):
            fs_status=[classify([set(m)&set(mask) for m in f['menus']])[0] for f in fs]
            mask_results.append({'allowed':mask,'statuses':dict(Counter(fs_status))})
        groups[name]={'alphabet':alphabet,'universal_candidate_exists':bool(universal),'universal_candidates':universal,'unrestricted_status':mask_results[-1]['statuses'],'hypothetical_uniform_masks':mask_results,'total_helly_gaps_across_masks':sum(x['statuses'].get('HELLY_GAP',0) for x in mask_results)}
    print(json.dumps({'factorization':by_arm,'fiber_diagnostics':groups,'scope':'finite corpus only; no statistical n_eff or real ACL evidence'},indent=2))

if __name__=='__main__': main(Path(sys.argv[1]),Path(sys.argv[2]))
