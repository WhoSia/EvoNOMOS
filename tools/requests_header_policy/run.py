"""Offline, SHA-pinned Requests 2.32.5 dual-demand comparative intervention.
Usage: python run.py NEW_OUTPUT_DIR
Requires requests==2.32.5 (installed dependency) and its runtime dependencies.
No network; no upstream PR lookup or mutation. Analyst-authored finite oracle.
"""
import ast
import difflib
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

PINS = {"utils.py": "8ab55852cc2188c53f08462ec4319c97fa49f04b", "adapters.py": "670c92767c5420a21538688132ce1f4f45e45873", "models.py": "c4b25fa0790da44683dab185c89ac08b69fb7419", "structures.py": "188e13e4829591facb23ae0e2eda84b9807cb818"}
ARMS = ("local", "parser", "policy")
DEMANDS = ("case", "boundary")
TYPES = ("text/plain", "TEXT/PLAIN", "Text/Plain", "text/html", "TEXT/XML", "application/json", "APPLICATION/JSON", "application/JSON", "application/vnd.context+xml", "application/x-context", "application/jsonx", "APPLICATION/JSONX", "application/TEXT", "application/xml", "image/text", "textual/plain")
PARAMS = ("", "; charset=utf-8", "; CHARSET=latin-1", "; charset=\"UTF-8\"", "; foo=bar")


def blob(b):
    return hashlib.sha1(f"blob {len(b)}\0".encode() + b).hexdigest()


def once(s, old, new):
    assert s.count(old) == 1, old
    return s.replace(old, new, 1)


def treatment(original, arm, changes):
    s = original
    if arm == "policy":
        start = s.index('    if "text" in content_type:', s.index('def get_encoding_from_headers('))
        end = s.index('\n\ndef ', start)
        policy = s[start:end].rstrip('\n')
        s = s[:start] + '    return _classify_encoding(content_type)\n\n\ndef _classify_encoding(content_type):\n' + policy + '\n' + s[end:]
    if "case" in changes:
        if arm == "parser":
            s = once(s, '    return content_type, params_dict', '    return content_type.lower(), params_dict')
        elif arm == "local":
            s = once(s, '    if "text" in content_type:', '    content_type = content_type.lower()\n\n    if "text" in content_type:')
        else:
            s = once(s, 'def _classify_encoding(content_type):\n', 'def _classify_encoding(content_type):\n    content_type = content_type.lower()\n')
    if "boundary" in changes:
        s = once(s, '    if "text" in content_type:', '    if content_type.startswith("text/"):')
        s = once(s, '    if "application/json" in content_type:', '    if content_type == "application/json":')
    return s


def functions(s):
    return {n.name: ast.dump(n, include_attributes=False) for n in ast.parse(s).body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


def delta(old, new):
    if old == new:
        return {"files": 0, "changed_existing_functions": [], "added_functions": [], "inserted_lines": 0, "deleted_lines": 0}
    a, b = functions(old), functions(new)
    diff = list(difflib.ndiff(old.splitlines(), new.splitlines()))
    return {"files": 1, "changed_existing_functions": sorted(k for k in a.keys() & b.keys() if a[k] != b[k]), "added_functions": sorted(b.keys() - a.keys()), "inserted_lines": sum(x.startswith('+ ') for x in diff), "deleted_lines": sum(x.startswith('- ') for x in diff)}


def worker(changes):
    from types import SimpleNamespace
    from requests import Request
    from requests.adapters import HTTPAdapter
    from requests.structures import CaseInsensitiveDict
    from requests.utils import _parse_content_type_header, get_encoding_from_headers
    req = Request('GET', 'http://example.invalid/').prepare()
    adapter = HTTPAdapter()
    out = []
    for typ in TYPES + ("",):
        for params in PARAMS if typ else ("",):
            raw = typ + params
            # Independent explicit reference for the frozen finite corpus.
            token = typ.lower() if "case" in changes else typ
            explicit = {"; charset=utf-8": "utf-8", "; CHARSET=latin-1": "latin-1", "; charset=\"UTF-8\"": "UTF-8"}.get(params)
            text = token.startswith('text/') if "boundary" in changes else 'text' in token
            js = token == 'application/json' if "boundary" in changes else 'application/json' in token
            want = explicit if explicit is not None else ('ISO-8859-1' if text else ('utf-8' if js else None))
            headers = CaseInsensitiveDict({'Content-Type': raw}) if raw else CaseInsensitiveDict()
            actual = get_encoding_from_headers(headers)
            response = adapter.build_response(req, SimpleNamespace(status=200, headers=headers, reason='OK'))
            response._content = b'\xe0\xe9\xee\xf4\xfb'; response._content_consumed = True
            text_ok = True if want is None else response.text == response._content.decode(want, errors='replace')
            parsed = _parse_content_type_header(raw)
            out.append({'raw': raw, 'want': want, 'direct': actual, 'adapter': response.encoding, 'text_ok': text_ok, 'raw_token': parsed[0], 'params': parsed[1]})
    # Published v2.32.5 fixture cases: representative parser and all 3 encoding fixtures.
    fixtures = [("application/xml", ("application/xml", {})), ("application/json ; charset=utf-8", ("application/json", {"charset":"utf-8"})), ("application/json ; Charset=utf-8", ("application/json", {"charset":"utf-8"})), ("text/plain", ("text/plain", {})), ("application/json ; ; ", ("application/json", {}))]
    for q in ["boundary2='something_else'", 'boundary2="something_else"', "'boundary2=something_else'", '"boundary2=something_else"']:
        fixtures.append((f"multipart/form-data; boundary = something ; {q} ; no_equals ", ("multipart/form-data", {"boundary":"something", "boundary2":"something_else", "no_equals":True})))
    checks = [(_parse_content_type_header(raw) == want) for raw, want in fixtures]
    checks.extend(get_encoding_from_headers(CaseInsensitiveDict(h)) == want for h,want in [({},None), ({"content-type":"application/json; charset=utf-8"},"utf-8"), ({"content-type":"text/plain"},"ISO-8859-1")])
    print(json.dumps({"cases":out,"old_fixtures_pass":sum(checks),"old_fixtures_total":len(checks)}))


def main(out):
    assert importlib.metadata.version('requests') == '2.32.5'
    root = Path(importlib.util.find_spec('requests').origin).parent
    for n, sha in PINS.items():
        assert blob((root/n).read_bytes()) == sha, n
    original = (root/'utils.py').read_text()
    out.mkdir(parents=True, exist_ok=False)
    rows = {}
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        shutil.copytree(root, tmp/'requests', ignore=shutil.ignore_patterns('__pycache__'))
        env = {**os.environ, 'PYTHONPATH': str(tmp), 'PYTHONDONTWRITEBYTECODE': '1'}
        for arm in ARMS:
            for changes in ((), ('case',), ('boundary',), DEMANDS):
                s = treatment(original, arm, changes)
                label = arm + '_' + ('-'.join(changes) or 'base')
                (tmp/'requests/utils.py').write_text(s)
                result = subprocess.check_output([sys.executable, str(Path(__file__).resolve()), '--worker', *changes], cwd=tmp, env=env, text=True)
                data = json.loads(result)
                (out/(label+'.json')).write_text(result)
                (out/(label+'.diff')).write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='original/utils.py',tofile=label+'/utils.py')))
                cases = data['cases']
                row = {"cases":len(cases),"direct_mismatch":sum(x['direct']!=x['want'] for x in cases),"adapter_mismatch":sum(x['adapter']!=x['want'] for x in cases),"text_mismatch":sum(not x['text_ok'] for x in cases),"old_fixtures": [data['old_fixtures_pass'],data['old_fixtures_total']],"raw_token_mismatch":sum(x['raw_token']!=x['raw'].split(';')[0] for x in cases),"source_blob":blob(s.encode()),"cumulative_delta":delta(original,s)}
                rows[label] = row
        sequences={}
        for arm in ARMS:
            for first,second in (DEMANDS,DEMANDS[::-1]):
                states=[original,treatment(original,arm,()),treatment(original,arm,(first,)),treatment(original,arm,DEMANDS)]
                sequences[arm+'_'+first+'_'+second]=[delta(a,b) for a,b in zip(states,states[1:])]
    summary={"pins":PINS,"rows":rows,"sequences":sequences}
    (out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2,sort_keys=True))
    assert all(v['direct_mismatch']==v['adapter_mismatch']==v['text_mismatch']==0 and v['old_fixtures']==[12,12] for v in rows.values()), 'oracle mismatch retained'
    assert rows['local_case-boundary']['raw_token_mismatch']==rows['policy_case-boundary']['raw_token_mismatch']==0
    assert rows['parser_case-boundary']['raw_token_mismatch']>0


if __name__ == '__main__':
    if sys.argv[1] == '--worker': worker(tuple(sys.argv[2:]))
    else: main(Path(sys.argv[1]).resolve())
