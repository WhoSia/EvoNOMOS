"""Bounded historical intake audit. Never certify prospective independence."""
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def audit(scope, search, metadata):
    errors = []
    repos = scope['population']
    receipts = search['receipts']
    if Counter(x['repo'] for x in receipts) != Counter(repos):
        errors.append('repository receipt coverage mismatch')
    expected = {}
    cap = scope['cap_per_repository']
    panels = {}
    for p in receipts:
        repo = p['repo']
        if 'error' in p:
            errors.append(f'{repo}: search unavailable')
            continue
        rows = p['rows']
        if p['returned'] != len(rows) or len(rows) > cap:
            errors.append(f'{repo}: count mismatch')
        panels[repo] = {'returned': len(rows), 'at_cap': len(rows) >= cap,
                        'coverage': 'UNKNOWN'}
        for x in rows:
            key = (repo, x['number'])
            if key in expected:
                errors.append(f'{key}: duplicate search result')
            expected[key] = x
    records = metadata['records']
    actual = Counter((x['repository'], x['number']) for x in records)
    if actual != Counter({k: 1 for k in expected}):
        errors.append('metadata coverage or uniqueness mismatch')
    dates = (datetime(2026, 11, 1, tzinfo=timezone.utc),
             datetime(2026, 11, 28, tzinfo=timezone.utc))
    exposure = set(scope['known_exposed'])
    author_counts = Counter()
    classifications = []
    for x in records:
        k = (x['repository'], x['number'])
        ident = f'{k[0]}#{k[1]}'
        status = 'RETROSPECTIVE_KNOWN_EXPOSED' if ident in exposure else 'RETROSPECTIVE_METADATA_ONLY'
        if 'error' in x:
            errors.append(f'{ident}: metadata unavailable')
            continue
        old = expected.get(k, {})
        if x.get('title') != old.get('title') or x.get('url') != old.get('url'):
            errors.append(f'{ident}: search/metadata identity mismatch')
        if x.get('is_pull_request') is not False:
            errors.append(f'{ident}: not verified as issue')
        try:
            dt = datetime.fromisoformat(x['created_at'].replace('Z', '+00:00'))
            if not dates[0] <= dt < dates[1]:
                errors.append(f'{ident}: outside window')
        except (KeyError, TypeError, ValueError):
            errors.append(f'{ident}: invalid date')
        if not x.get('author'):
            errors.append(f'{ident}: author missing')
        else:
            author_counts[x['author']] += 1
        classifications.append({'id': ident, 'status': status, 'independence': 'UNVERIFIED'})
    return {'status': 'FAIL' if errors else 'PASS_METADATA_CONSISTENCY_ONLY',
            'errors': errors, 'repositories': panels, 'records': len(records),
            'repositories_with_hits': sum(p['returned'] > 0 for p in panels.values()),
            'unique_author_logins': len(author_counts),
            'repeated_author_logins': {k: v for k, v in author_counts.items() if v > 1},
            'classifications': classifications, 'prospective_admitted': 0,
            'independent_demand_clusters': None, 'statistical_effective_n': None}


def main(root):
    s, q, m = (json.loads((root / name).read_text()) for name in
               ('rehearsal_scope.json', 'rehearsal_search_receipt.json', 'rehearsal_metadata.json'))
    result = audit(s, q, m)
    print(json.dumps(result, indent=2))
    return bool(result['errors'])


if __name__ == '__main__':
    sys.exit(main(Path(sys.argv[1])))
