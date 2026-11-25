"""Run R107/R108 with the exact historical buffers.go; not the full grpc module."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    'buffers.go': '975ceb71853da3445d1cba07053ab0b3484773fe',
    'order_test.go': '2d4f5690861ef655f88348189d81131092c8494e',
    'concurrent_test.go': 'd2cbd179a00cfa7f0d96032ac18854d9762e11af',
}

def checked(name, source):
    data = source.read_bytes()
    sha = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
    if sha != EXPECTED[name]:
        raise ValueError(f'{name}: {sha} != {EXPECTED[name]}')
    print('EXACT', name, sha, flush=True)
    return data


def main(source):
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        mem = root / 'mem'
        mem.mkdir()
        (root / 'go.mod').write_text('module google.golang.org/grpc\n\ngo 1.23\n')
        for name, path in [('buffers.go', source), ('order_test.go', ROOT.parent / 'r107/order_test.go.txt'), ('concurrent_test.go', ROOT / 'concurrent_test.go.txt')]:
            (mem / name).write_bytes(checked(name, path))
        # Only the observed interface, not grpc's actual pool implementations.
        (mem / 'pool_contract.go').write_text('package mem\ntype BufferPool interface { Get(int) *[]byte; Put(*[]byte) }\n')
        env = {**os.environ, 'GOMAXPROCS': '4', 'GOTOOLCHAIN': 'local', 'GOPROXY': 'off'}
        subprocess.run(['go', 'test', '-race', '-v', '-count=3', './mem'], cwd=root, env=env, check=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python run.py path/to/exact/buffers.go')
    main(Path(sys.argv[1]))
