"""Retrospective #1217 mechanism diagnostic, not an exact 1.3.3 reproduction."""
import hashlib
import importlib.metadata as md
import importlib.util
import io
import json
import tempfile
from pathlib import Path

from requests import Request
from requests.adapters import HTTPAdapter
from requests_cache.backends import FileCache, SQLiteCache
from urllib3.response import HTTPResponse

PINS = {
    'serializers/cattrs.py': 'a791cd690498ed1f3963255272fd7e402e84e1a1',
    'backends/filesystem.py': '12a4e67fd337794c2fba9d3054db89f6a9755460',
}
CASES = [
    ('undeclared_utf8', 'text/html', '<title>Café Zürich</title> naïve – 日本'.encode()),
    ('latin1', 'text/plain; charset=ISO-8859-1', b'caf\xe9'),
    ('utf8_declared', 'text/plain; charset=utf-8', 'Café 日本'.encode()),
    ('ascii_undeclared', 'text/plain', b'hello'),
    ('invalid_utf8', 'text/plain; charset=utf-8', b'a\xffb'),
    ('json_format', 'application/json', b'{"a":1, "b":2}\n'),
    ('binary', 'application/octet-stream', b'\x00\xff\x80'),
]


def blob(b):
    return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()


def response(content_type, body):
    req = Request('GET', 'http://example.invalid/probe').prepare()
    raw = HTTPResponse(body=io.BytesIO(body), status=200, preload_content=False,
                       headers={'Content-Type': content_type, 'Content-Length': str(len(body))})
    r = HTTPAdapter().build_response(req, raw)
    assert r.content == body
    return r


def run():
    assert md.version('requests') == '2.32.5'
    assert md.version('requests-cache') == '1.3.2'
    root = Path(importlib.util.find_spec('requests_cache').origin).parent
    for path, expected in PINS.items():
        assert blob((root/path).read_bytes()) == expected, path
    rows = []
    for name, ct, body in CASES:
        for mode in ('filesystem_default', 'filesystem_binary', 'sqlite_default'):
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp)/'cache'
                def open_cache():
                    if mode == 'sqlite_default': return SQLiteCache(str(path))
                    return FileCache(str(path), decode_content=(mode=='filesystem_default'))
                first = response(ct, body)
                before = (first.content, first.text, first.encoding, first.headers['Content-Type'], first.headers['Content-Length'])
                cache = open_cache()
                try: cache.save_response(first, cache_key='probe')
                finally: cache.close()
                cache = open_cache()
                try:
                    second = cache.get_response('probe')
                    assert second is not None
                    after = (second.content, second.text, second.encoding, second.headers['Content-Type'], second.headers['Content-Length'])
                    rows.append(dict(case=name, mode=mode, bytes_equal=before[0]==after[0],
                                     text_equal=before[1]==after[1], encoding_equal=before[2]==after[2],
                                     content_type_equal=before[3]==after[3], content_length_equal=before[4]==after[4],
                                     before_hex=before[0].hex(), after_hex=after[0].hex(),
                                     before_encoding=before[2], after_encoding=after[2]))
                finally: cache.close()
    summary = {mode: {field: sum(not r[field] for r in rows if r['mode']==mode)
                      for field in ('bytes_equal','text_equal','encoding_equal','content_type_equal','content_length_equal')}
               for mode in ('filesystem_default','filesystem_binary','sqlite_default')}
    return {'versions':{n:md.version(n) for n in ('requests','requests-cache','urllib3','attrs','cattrs')},
            'pins':PINS, 'rows':rows, 'mismatches':summary}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False))
