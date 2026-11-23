"""Replay researcher-defined P35 tests against authentic go-chi/chi v5.1.0.

Research contract failures are NOT certification of an upstream defect,
a full Chi module regression, or a demonstrated ATLAS advantage.
"""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

UPSTREAM_BLOB = '997bed569ad89aec1f30765bfc6e868a7f232b6d'
TESTS = {
    'p35_p7_common_test.go': '81f8123d6e24eb92c1ce9529f170be36191dd1c1',
    'p35_p7_d8_same_requirement_test.go': 'ed13ceb8f78ccc923f58ea12584a366cd3080d37',
}


def checked(path: Path, expected: str) -> bytes:
    actual = subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()
    if actual != expected:
        raise ValueError(f'source provenance mismatch: {path}, got {actual}, wanted {expected}')
    return path.read_bytes()


def test(upstream: Path, root: Path):
    data = checked(upstream, UPSTREAM_BLOB)
    checks = {filename: checked(root / 'tools/p35-p7/tests' / filename, sha)
              for filename, sha in TESTS.items()}
    with tempfile.TemporaryDirectory(prefix='r82-authentic-upstream-') as d:
        target = Path(d)
        (target / 'go.mod').write_text('module example.org/authentic-chi-r82\n\ngo 1.23\n')
        (target / 'route_headers.go').write_bytes(data)
        for name, value in checks.items():
            (target / name).write_bytes(value)
        env = dict(os.environ, GOPROXY='off', GOTOOLCHAIN='local')
        command = ['go', 'test', '-race', '-count=1', '-v', './...']
        p = subprocess.run(command, cwd=target, env=env, capture_output=True, text=True, timeout=120)
        if p.returncode not in (0, 1):
            raise RuntimeError('Go did not complete normally: ' + p.stderr)
        logs = p.stdout + '\n' + p.stderr
        fails = re.findall(r'^--- FAIL: ([^ ]+)', logs, re.M)
        fails += re.findall(r'^    --- FAIL: ([^ ]+)', logs, re.M)
        if 'TestP35P7EmptyRouterExactlyOnce' not in fails:
            raise AssertionError('expected exact-once observation absent; investigate source/toolchain')
        if 'P35P7_D0_EMPTY_ROUTE_FAILURE exactly-once expected 1, got 2' not in logs:
            raise AssertionError('expected empty-router observation differs')
        if 'WARNING: DATA RACE' in logs:
            raise AssertionError('unexpected race detector result')
        return {
            'result': 'PASS_AUTHENTIC_UPSTREAM_DIAGNOSTIC_EXPECTED_FAILURES',
            'upstream_blob_verified': UPSTREAM_BLOB,
            'research_tests_blobs_verified': TESTS,
            'isolated_package': True,
            'whole_chi_module_tested': False,
            'test_requirement_authority': 'RESEARCH_TEAM_NOT_CHI_MAINTAINERS',
            'upstream_defect_confirmed': False,
            'command': command,
            'go_exit_code': p.returncode,
            'failed_cases': fails,
            'raw_log': logs,
            'interpretation': 'Observed under researcher-authored requirements; header order is not promised by upstream',
        }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--upstream', type=Path, required=True)
    ap.add_argument('--root', type=Path, required=True)
    ap.add_argument('--out', type=Path)
    args = ap.parse_args()
    r = test(args.upstream, args.root)
    text = json.dumps(r, indent=2, ensure_ascii=False) + '\n'
    if args.out:
        args.out.write_text(text)
    else:
        print(text)
