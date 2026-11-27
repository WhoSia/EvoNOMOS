"""Loopback-only historical #1217 session-path check."""
import json
import tempfile
from collections import Counter
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from requests_cache import CachedSession
from cache_byte_probe import CASES, run as direct_run


def run():
    direct = direct_run()
    bodies = {name: (ct, body) for name, ct, body in CASES}
    hits = Counter()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            name = self.path.split('/')[-1]
            ct, body = bodies[name]
            hits[self.path] += 1
            self.send_response(200)
            self.send_header('Content-Type', ct)
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    rows = []
    try:
        for name, _, body in CASES:
            for mode in ('filesystem_default', 'filesystem_binary', 'sqlite_default'):
                with tempfile.TemporaryDirectory() as tmp:
                    path = Path(tmp)/'cache'
                    route = f'/{mode}/{name}'
                    url = f'http://127.0.0.1:{server.server_port}{route}'
                    kw = {'backend': 'sqlite' if mode=='sqlite_default' else 'filesystem'}
                    if mode=='filesystem_binary': kw['decode_content'] = False
                    def request():
                        with CachedSession(str(path), **kw) as session:
                            session.trust_env = False
                            r = session.get(url, timeout=3)
                            return (r.from_cache, r.content, r.text, r.encoding,
                                    r.headers['Content-Type'], r.headers['Content-Length'])
                    a = request()
                    b = request()
                    assert not a[0] and b[0] and a[1] == body and hits[route] == 1
                    row = dict(case=name, mode=mode, server_hits=hits[route], cache_hit=b[0])
                    for i, field in enumerate(('bytes_equal','text_equal','encoding_equal','content_type_equal','content_length_equal'),1):
                        row[field] = a[i]==b[i]
                    rows.append(row)
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    fields = ('bytes_equal','text_equal','encoding_equal','content_type_equal','content_length_equal')
    lookup = {(r['case'],r['mode']):r for r in direct['rows']}
    mismatch = sum(r[f]!=lookup[r['case'],r['mode']][f] for r in rows for f in fields)
    return {'rows':rows,'direct_session_observable_mismatches':mismatch,
            'requests_per_pair':1, 'actual_cache_hits':sum(r['cache_hit'] for r in rows),
            'version_receipt':direct['versions']}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
