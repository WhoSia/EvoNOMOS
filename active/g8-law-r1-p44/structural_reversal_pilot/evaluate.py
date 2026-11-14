"""Reproduce a bounded synthetic architecture intervention study.
This script does not authenticate real maintainer authority or estimate human effort.
"""
from pathlib import Path
import difflib
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def file_metrics(baseline: Path, candidate: Path):
    files = sorted({p.name for p in baseline.glob('*.go') if not p.name.endswith('_test.go')} |
                   {p.name for p in candidate.glob('*.go') if not p.name.endswith('_test.go')})
    altered = []
    added = removed = 0
    for name in files:
        old = (baseline / name).read_text().splitlines() if (baseline / name).exists() else []
        new = (candidate / name).read_text().splitlines() if (candidate / name).exists() else []
        delta = list(difflib.ndiff(old, new))
        add = sum(s.startswith('+ ') for s in delta)
        delete = sum(s.startswith('- ') for s in delta)
        if add or delete:
            altered.append(name)
            added += add
            removed += delete
    return altered, added, removed


def main():
    manifest = json.loads((ROOT / 'variants.json').read_text())
    results = []
    for v in manifest:
        candidate = ROOT / 'snapshots' / v['name']
        baseline = ROOT / 'snapshots' / (v['architecture'] + '_base_nomode')
        changed, added, removed = file_metrics(baseline, candidate)
        checks = {}
        for args in (['go', 'test', '-count=1', './...'], ['go', 'vet', './...'],
                     ['go', 'test', '-race', '-count=1', './...']):
            cp = subprocess.run(args, cwd=candidate, text=True, capture_output=True, timeout=90)
            checks[' '.join(args)] = {
                'exit_code': cp.returncode,
                'output': (cp.stdout + '\n' + cp.stderr).strip()[-1000:]
            }
        results.append({**v, 'changed_files': changed, 'added_source_lines': added,
                        'removed_source_lines': removed,
                        'source_loc': sum(len(p.read_text().splitlines())
                                          for p in candidate.glob('*.go')
                                          if not p.name.endswith('_test.go')),
                        'checks': checks})
    (ROOT / 'results_reproducible.json').write_text(json.dumps(results, indent=2) + '\n')
    failed = [(x['name'], cmd) for x in results for cmd, item in x['checks'].items()
              if item['exit_code'] != 0]
    for x in results:
        print(x['name'], 'changed_files=', len(x['changed_files']),
              'source_line_churn=', x['added_source_lines']+x['removed_source_lines'],
              'all_pass=', all(item['exit_code']==0 for item in x['checks'].values()))
    if failed:
        print('FAIL:', failed, file=sys.stderr)
        return 1
    print('PASS:', len(results), 'snapshots; ', len(results)*3, 'Go commands')
    return 0


if __name__ == '__main__':
    sys.exit(main())
