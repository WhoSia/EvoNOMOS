"""Offline R81 reproducer: byte-verified D8 Go benchmark, NOT human effort.

Execute from a full EvoNOMOS main checkout:
    python tools/p35-p7/r81_cost_replay.py --out r81_replay.json

Requires Go 1.23+ and git. Runtime cost is environment-dependent and the
posthoc lifecycle bench must never be reported as preregistered confirmatory.
"""
import argparse
from collections import defaultdict
import json
import os
from pathlib import Path
import re
import statistics
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'tools' / 'p35-p7'
GO_FILES = {
    'live': ('d8/live/route_headers.go', 'e481e73aa1d82497c25011b6468d7e8749c705f7'),
    'snapshot': ('d8/snapshot/route_headers.go', '66e88964508cedc38740913a7c00fbf5b6e6220a'),
}
TEST_FILES = {
    'p35_p7_common_test.go': '81f8123d6e24eb92c1ce9529f170be36191dd1c1',
    'p35_p7_d8_same_requirement_test.go': 'ed13ceb8f78ccc923f58ea12584a366cd3080d37',
    'r80_temporal_contract_test.go': 'fe9ea93df2a80e6fee2d8ed437b56f062fa6ce17',
    'r81_cost_tradeoff_test.go': 'ca9e0a07bf69f169ef15f16ac8b19dd7f1fd7ddb',
    'r81_lifecycle_exploratory_test.go': 'a66816f5eace1e673e4d83ab06f6d786e7113bb2',
}
PATTERN = re.compile(r'^(BenchmarkR81\S+)-\d+\s+\d+\s+([\d.]+) ns/op\s+(\d+) B/op\s+(\d+) allocs/op$', re.M)


def check_blob(path, expected):
    if not path.is_file():
        raise ValueError(f'missing evidence file: {path}')
    actual = subprocess.run(['git', 'hash-object', str(path)], check=True,
                            text=True, capture_output=True).stdout.strip()
    if actual != expected:
        raise ValueError(f'blob mismatch for {path}: {actual} != {expected}')
    return path.read_bytes()


def invoke(cwd, args, *, temporal=None):
    env = dict(os.environ, GOPROXY='off', GOTOOLCHAIN='local')
    if temporal is not None:
        env['R80_EXPECT'] = temporal
    proc = subprocess.run(args, cwd=cwd, env=env, check=False,
                          text=True, capture_output=True, timeout=120)
    if proc.returncode:
        raise RuntimeError(f'Go command failed {args}: {proc.stdout}\n{proc.stderr}')
    return proc.stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path)
    parser.add_argument('--rounds', type=int, default=5)
    args = parser.parse_args()
    if not 1 <= args.rounds <= 20:
        raise ValueError('1 <= rounds <= 20')
    source = {k: check_blob(BASE / p, sha) for k, (p, sha) in GO_FILES.items()}
    tests = {n: check_blob(BASE / 'tests' / n, sha) for n, sha in TEST_FILES.items()}
    observations = []
    with tempfile.TemporaryDirectory(prefix='evonomos-r81-') as tmp:
        roots = {}
        for arm in GO_FILES:
            folder = Path(tmp) / arm
            folder.mkdir()
            roots[arm] = folder
            (folder / 'route_headers.go').write_bytes(source[arm])
            (folder / 'go.mod').write_text('module example.org/r81-' + arm + '\n\ngo 1.23\n')
            for filename, content in tests.items():
                (folder / filename).write_bytes(content)
            invoke(folder, ['go', 'test', '-race', '-count=1',
                            '-run', 'TestP35P7|TestR80', './...'],
                   temporal='after' if arm == 'live' else 'downstream')
        for i in range(args.rounds):
            order = ('live', 'snapshot') if i % 2 == 0 else ('snapshot', 'live')
            for arm in order:
                stdout = invoke(roots[arm], ['go', 'test', '-run', '^$',
                                          '-bench', '^BenchmarkR81',
                                          '-benchtime=200ms', '-count=1',
                                          '-benchmem', './...'])
                parsed = PATTERN.findall(stdout)
                if len(parsed) != 6:
                    raise AssertionError(f'expected 6 benchmark outputs, observed {len(parsed)}: {stdout}')
                for name, ns, bytes_, allocations in parsed:
                    observations.append(dict(round=i+1, arm=arm, benchmark=name,
                                             ns_per_op=float(ns), bytes_per_op=int(bytes_),
                                             allocs_per_op=int(allocations)))
    grouped = defaultdict(list)
    for row in observations:
        grouped[(row['arm'], row['benchmark'])].append(row['ns_per_op'])
    summary = [dict(arm=k[0], benchmark=k[1], n=len(v),
                    median_ns=statistics.median(v), min_ns=min(v), max_ns=max(v))
               for k, v in sorted(grouped.items())]
    result = dict(scope='ISOLATED_SOURCE_NATIVE_GOLANG',
                  all_source_blobs_verified=True,
                  native_race_regression='PASS_SEQUENTIAL_TESTS',
                  preregistered_benchmarks=('BenchmarkR81SteadyLookup',
                                            'BenchmarkR81ConstructHandler'),
                  exploratory_posthoc_benchmark='BenchmarkR81Lifecycle',
                  human_maintainability='NOT_MEASURED',
                  external_replication='NOT_PERFORMED',
                  scientific_novelty='NOT_ESTABLISHED',
                  rounds=args.rounds, summary=summary, raw=observations)
    result_json = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.out:
        args.out.write_text(result_json)
    else:
        print(result_json)
    return result


if __name__ == '__main__':
    main()
