"""R82 provenance verdict: project variants are not go-chi/chi v5.1.0 bytes.

Run with the upstream source and a project checkout:
 python r82_upstream_fidelity_audit.py --upstream .../route_headers.go --root .../EvoNOMOS
Does NOT rerun a complete upstream module or establish an ATLAS advantage.
"""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

UPSTREAM_REF = 'go-chi/chi@v5.1.0:middleware/route_headers.go'
UPSTREAM_BLOB = '997bed569ad89aec1f30765bfc6e868a7f232b6d'
TEAM_FILES = {
    'original_live': ('arms/live/route_headers.go', 'ad9a2fbc0a30a39475f746068e74e2d3e6c93999'),
    'original_snapshot': ('arms/snapshot/route_headers.go', 'e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75'),
    'repaired_live': ('d8/live/route_headers.go', 'e481e73aa1d82497c25011b6468d7e8749c705f7'),
    'repaired_snapshot': ('d8/snapshot/route_headers.go', '66e88964508cedc38740913a7c00fbf5b6e6220a'),
}
R80_ZIP_SHA256 = '050a8c291e760c907700606a5d23b17e6e4204ef2b6b6d2b3c5439c41ac96a2c'


def blob(path):
    return subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()


def identical_git_blob(path, sha):
    got = blob(path)
    if got != sha:
        raise ValueError(f'wrong blob: {path} actual={got} expected={sha}')
    return path.read_bytes()


def analyze(upstream: Path, root: Path, zip_path=None):
    source = identical_git_blob(upstream, UPSTREAM_BLOB)
    source_lines = source.decode('utf-8').splitlines()
    rows = []
    for name, (rel, sha) in TEAM_FILES.items():
        variant = identical_git_blob(root / 'tools/p35-p7' / rel, sha)
        if variant == source or sha == UPSTREAM_BLOB:
            raise AssertionError('known team-derived source was unexpectedly upstream-identical')
        lines = variant.decode('utf-8').splitlines()
        edits = difflib.SequenceMatcher(None, source_lines, lines, autojunk=False).get_opcodes()
        rows.append({
            'arm': name, 'team_blob': sha, 'upstream_blob': UPSTREAM_BLOB,
            'byte_identical_to_upstream': False,
            'upstream_lines_affected': sum(j - i for kind, i, j, x, y in edits if kind != 'equal'),
            'team_lines_affected': sum(y - x for kind, i, j, x, y in edits if kind != 'equal'),
            'diff_algorithm': 'python.difflib.SequenceMatcher(autojunk=False)',
            'label': 'RESEARCH_DERIVATIVE_OF_CHI_NOT_CHI_V5_1_0',
        })
    result = {
        'upstream_ref': UPSTREAM_REF, 'upstream_git_blob': UPSTREAM_BLOB,
        'upstream_bytes_verified': True, 'team_blobs_verified': len(rows),
        'team_variants_upstream_identical': 0, 'rows': rows,
        'r80_r81_label': 'EXACT_TEAM_VARIANT_BYTES_IN_ISOLATED_GO_NOT_UPSTREAM_CHI',
        'full_upstream_module_tested': False,
        'attributed_novelty': 'NOT_ESTABLISHED',
        'external_claude_report': 'INDEPENDENT_PARTIAL_REPLICATION_AND_CRITIQUE',
        'decision': 'STOP_SEPARATE_ATLAS_NARROW_CONTRACT_RESEARCH_MERGE_INTO_STRONG_ADR',
    }
    if zip_path is not None:
        measured = hashlib.sha256(zip_path.read_bytes()).hexdigest()
        if measured != R80_ZIP_SHA256:
            raise ValueError(f'R80 ZIP SHA-256 mismatch: {measured}')
        result['r80_zip_sha256_verified'] = measured
    else:
        result['r80_zip_sha256_verified'] = 'NOT_CHECKED_IN_THIS_RUN'
    return result


def test(root: Path, upstream: Path, zip_path=None):
    actual = analyze(upstream, root, zip_path)
    assert actual['team_blobs_verified'] == 4
    assert all(not item['byte_identical_to_upstream'] for item in actual['rows'])
    assert actual['full_upstream_module_tested'] is False
    bad_copy = upstream.parent / 'modified_upstream_probe.go'
    bad_copy.write_bytes(upstream.read_bytes() + b'\n')
    try:
        try:
            analyze(bad_copy, root)
        except ValueError:
            pass
        else:
            raise AssertionError('modified upstream passed')
    finally:
        bad_copy.unlink(missing_ok=True)
    actual['negative_controls'] = 1
    actual['result'] = 'PASS_UPSTREAM_DERIVATIVE_PROVENANCE_GATE'
    return actual


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--upstream', type=Path, required=True)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--r80-zip', type=Path)
    args = parser.parse_args()
    print(json.dumps(test(args.root, args.upstream, args.r80_zip), indent=2))
