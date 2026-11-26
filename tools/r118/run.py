"""R118: exact historical P35-P4 arms, authored bounded MIME-token demand."""
import hashlib
import itertools
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
EXPECTED = {
 'independent/content_charset.go':'7ecb4a2d5e91d7ef775f824e64f2210bf360e5f2',
 'independent/content_type.go':'8751cb40ca041b8f56bc1c6b9260db0a28434ee6',
 'shared/content_charset.go':'53d6ef557bc890cb8727d552e7ab16dc46143a88',
 'shared/content_type.go':'d1fad4adce7225e674c1c035636ef53bb9a27e4c',
 'shared/content_media_parse.go':'1144b1fd275994fde766a331a9995cafc2ed0eb9',
 'shared-empty-type.patch':'206c455379d5bf772421c1dc165cee4448f62664',
}


def replace(path, old, new):
    text = path.read_text()
    assert text.count(old) == 1, (path, old)
    path.write_text(text.replace(old, new))


def stage(arm, actions, directory):
    for src in (ROOT/arm).glob('*.go'):
        shutil.copyfile(src, directory/src.name)
    t = directory/'content_type.go'
    c = directory/'content_charset.go'
    if arm == 'shared':
        subprocess.run(['git','apply','-p2',str(ROOT/'shared-empty-type.patch')], cwd=directory, check=True)
    if 'type' in actions:
        old = 'parseErr == nil && ok' if arm == 'independent' else 'valid && ok'
        replace(t, old, old+' && strings.Contains(s, "/")')
    if 'charset' in actions:
        if arm == 'independent':
            replace(c, '_, params, err := mime.ParseMediaType(ce)', 'media, params, err := mime.ParseMediaType(ce)')
            replace(c, 'if err != nil { return false }', 'if err != nil || !strings.Contains(media, "/") { return false }')
        else:
            replace(c, '_, ce, valid := parseCanonicalContentType(ce)', 'media, ce, valid := parseCanonicalContentType(ce)')
            replace(c, 'if !valid { return false }', 'if !valid || (media != "" && !strings.Contains(media, "/")) { return false }')
    if 'global' in actions:
        replace(directory/'content_media_parse.go', 'if err != nil { return "", "", false }', 'if err != nil || !strings.Contains(media, "/") { return "", "", false }')
    shutil.copyfile(ROOT/'token_probe.go.txt', directory/'token_test.go')
    (directory/'go.mod').write_text('module example.org/r118\n\ngo 1.23\n')


def main():
    for name, want in EXPECTED.items():
        data = (ROOT/name).read_bytes()
        got = hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        assert got == want, (name,got)
    rows=[]
    env={**os.environ,'GOTOOLCHAIN':'local','GOPROXY':'off','GOMAXPROCS':'2'}
    for arm in ('independent','shared'):
        menu=('type','charset') if arm=='independent' else ('type','charset','global')
        for k in range(len(menu)+1):
            for actions in itertools.combinations(menu,k):
                with tempfile.TemporaryDirectory() as tmp:
                    directory=Path(tmp)
                    stage(arm,actions,directory)
                    r=subprocess.run(['go','test','-count=1','-v','.'],cwd=directory,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                    label=arm+'_'+('_'.join(actions) or 'base')
                    (ROOT/(label+'.log')).write_text(r.stdout)
                    r.check_returncode()
                    obs={tuple(l.split()[1:4]):int(l.split()[4]) for l in r.stdout.splitlines() if l.startswith('OBS ')}
                    assert len(obs)==16
                    legacy=all(v==204 for (m,t,c),v in obs.items() if t=='application/json')
                    type_reject=all(v==415 for (m,t,c),v in obs.items() if m=='type' and t!='application/json')
                    charset_reject=all(v==415 for (m,t,c),v in obs.items() if m=='charset' and t!='application/json')
                    charset_accept=all(v==204 for (m,t,c),v in obs.items() if m=='charset' and t!='application/json')
                    assert legacy
                    if not actions: assert all(v==204 for v in obs.values())
                    row={'arm':arm,'actions':actions,'common':legacy and type_reject and charset_reject,'divergent':legacy and type_reject and charset_accept,'protected_cases':12,'new_observations':16}
                    rows.append(row);print(json.dumps(row),flush=True)
    minima={a:{g:min(len(r['actions']) for r in rows if r['arm']==a and r[g]) for g in ('common','divergent')} for a in ('independent','shared')}
    assert minima=={'independent':{'common':2,'divergent':1},'shared':{'common':1,'divergent':1}}
    assert not next(r for r in rows if r['arm']=='shared' and r['actions']==('global',))['divergent']
    print(json.dumps({'minima':minima,'variants':len(rows)}))


if __name__=='__main__':main()
