"""Independent read-only audit of the archived AreWeSOLID OCP JSON/JSONL.

Python 3.11+. Treats all submitted code as untrusted data: NEVER executes it.
Checks source digest, sample clustering, template masking, reference alignment,
and Python comment/docstring prevalence. Emits a JSON report.
"""
import argparse
import ast
import collections
import hashlib
import io
import json
import re
import tokenize
import zipfile

EXPECTED_SHA = 'd2cfbe50dd12d189c0ee2b561a842757fa7483251df9025b602c498b753f0353'
REFERENCE = 'AreWeSOLID/dataset/groundtruth/ocp_violations.json'
PREFIX = 'AreWeSOLID/dataset/completions/test/ocp--'


def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as source:
        for piece in iter(lambda: source.read(1024 * 1024), b''):
            h.update(piece)
    return h.hexdigest()


def key_ast(source):
    return ast.dump(ast.parse(source), include_attributes=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', help='Path to the exact AreWeSOLID.zip')
    parser.add_argument('--allow-different-sha', action='store_true')
    args = parser.parse_args()
    digest = hash_file(args.archive)
    if digest != EXPECTED_SHA and not args.allow_different_sha:
        raise ValueError('Archive SHA-256 mismatch: ' + digest)

    with zipfile.ZipFile(args.archive) as archive:
        names = sorted(n for n in archive.namelist()
                       if n.startswith(PREFIX) and n.endswith('/output_test.jsonl'))
        reference = json.loads(archive.read(REFERENCE))['code_examples']
        rows = []
        per_file = {}
        for name in names:
            entries = [json.loads(line) for line in archive.read(name).decode('utf-8').splitlines()
                       if line.strip()]
            per_file[name] = len(entries)
            rows.extend(entries)

    if not rows:
        raise ValueError('No OCP JSONL records found')
    masks = []
    occurrences = collections.Counter()
    groups = collections.defaultdict(list)
    for row in rows:
        occurrence = row['prompt'].count(row['input'])
        occurrences[occurrence] += 1
        if occurrence != 1:
            raise ValueError(f"Invalid masking input count for id {row['id']}: {occurrence}")
        masked = row['prompt'].replace(row['input'], '<SUBMITTED_CODE>')
        masks.append(masked)
        groups[(row['model'], row['strategy'], row['language'])].append((row['input'], masked))

    reference_sides = [code for pair in reference for code in (pair['input'], pair['output'])]
    unique_submissions = set(row['input'] for row in rows)
    exact = set(reference_sides)
    trim = {s.strip() for s in reference_sides}
    no_whitespace = {re.sub(r'\s+', '', s) for s in reference_sides}
    py_source = set(row['input'] for row in rows if row['language'] == 'PYTHON')
    py_refs = [side for pair in reference if pair['language'].upper() == 'PYTHON'
               for side in (pair['input'], pair['output'])]
    ast_errors = []
    ref_ast = set()
    for source in py_refs:
        try:
            ref_ast.add(key_ast(source))
        except (SyntaxError, ValueError) as error:
            ast_errors.append('reference: ' + str(error))
    submitted_ast_matches = 0
    comment_sources = 0
    docstring_sources = 0
    comment_lines = 0
    for source in py_source:
        try:
            submitted_ast_matches += key_ast(source) in ref_ast
            tree = ast.parse(source)
            if any(ast.get_docstring(node) for node in ast.walk(tree)
                   if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))):
                docstring_sources += 1
        except (SyntaxError, ValueError) as error:
            ast_errors.append('submitted: ' + str(error))
        try:
            comments = [t for t in tokenize.generate_tokens(io.StringIO(source).readline)
                        if t.type == tokenize.COMMENT]
            comment_sources += bool(comments)
            comment_lines += len(comments)
        except tokenize.TokenError as error:
            ast_errors.append('tokenize: ' + str(error))

    by_strategy = collections.defaultdict(set)
    for row, masked in zip(rows, masks):
        by_strategy[row['strategy']].add(masked)
    report = {
        'sha256': digest,
        'saved_jsonl_files': len(names),
        'records': len(rows),
        'unique_submitted_source_strings': len(unique_submissions),
        'unique_saved_record_ids': len(set(row['id'] for row in rows)),
        'reference_pairs': len(reference),
        'rows_per_file': dict(collections.Counter(per_file.values())),
        'prompt_input_occurrences': dict(occurrences),
        'distinct_masked_prompt_templates': len(set(masks)),
        'templates_per_strategy': {k: len(v) for k, v in sorted(by_strategy.items())},
        'model_strategy_language_groups': len(groups),
        'rows_per_group': dict(collections.Counter(len(v) for v in groups.values())),
        'distinct_inputs_per_group': dict(collections.Counter(len({code for code, _ in v}) for v in groups.values())),
        'templates_per_group': dict(collections.Counter(len({masked for _, masked in v}) for v in groups.values())),
        'reference_text_matches': {
            'exact_unique_submissions': sum(s in exact for s in unique_submissions),
            'strip_unique_submissions': sum(s.strip() in trim for s in unique_submissions),
            'all_whitespace_removed_unique_submissions': sum(re.sub(r'\s+', '', s) in no_whitespace for s in unique_submissions),
        },
        'python_only': {
            'unique_submitted_sources': len(py_source),
            'saved_rows': sum(row['language'] == 'PYTHON' for row in rows),
            'unique_source_ast_matches_with_reference_sides': submitted_ast_matches,
            'unique_sources_with_comment_tokens': comment_sources,
            'comment_tokens_across_unique_sources': comment_lines,
            'unique_sources_with_docstrings': docstring_sources,
            'parse_errors': ast_errors,
        },
        'limits': [
            'Text/AST mismatch does not establish semantic difference or provenance.',
            'Code comment prevalence does not establish whether a protected contract was stated.',
            'Saved rows are repeated code submissions, not independent reviewer decisions.',
            'Archive code was read as data and never executed.',
        ],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
