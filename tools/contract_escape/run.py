"""Recheck a frozen shared parser with a local escape rival (bounded oracle)."""
import hashlib, importlib.util, json, os, subprocess, sys, tempfile, shutil, difflib
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def blob(b): return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()

def main(r118root,out):
    assert blob((r118root/'run.py').read_bytes())=='e80d34d96ba4762be0fa710908270382477e610c'
    assert blob((r118root/'token_probe.go.txt').read_bytes())=='70f54c94ff6ac219017f07470cc8ef61cf736121'
    spec=importlib.util.spec_from_file_location('r118',r118root/'run.py'); r118=importlib.util.module_from_spec(spec);spec.loader.exec_module(r118)
    for name,expected in r118.EXPECTED.items(): assert blob((r118root/name).read_bytes())==expected,name
    out.mkdir(parents=True,exist_ok=False)
    env={**os.environ,'GOTOOLCHAIN':'local','GOPROXY':'off','GOMAXPROCS':'2'}
    vectors={}; snapshots={}
    for name in ('independent','global','bypass','fallback'):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp); r118.stage('independent' if name=='independent' else 'shared',() if name=='independent' else ('global',),p)
            c=p/'content_charset.go'; orig=c.read_text()
            if name=='bypass':
                c.write_bytes((r118root/'independent/content_charset.go').read_bytes())
            if name=='fallback':
                s=orig.replace('import (\n','import (\n\t"mime"\n',1)
                old='\t_, ce, valid := parseCanonicalContentType(ce)\n\tif !valid { return false }'
                new='\traw := ce\n\t_, ce, valid := parseCanonicalContentType(raw)\n\tif !valid {\n\t\t_, params, err := mime.ParseMediaType(raw)\n\t\tif err != nil { return false }\n\t\tce = strings.ToLower(params["charset"])\n\t}'
                assert s.count(old)==1; c.write_text(s.replace(old,new))
            snapshots[name]={f.name:f.read_bytes() for f in p.glob('content_*.go')}
            if name in ('bypass','fallback'):
                changed=[k for k in snapshots['global'] if snapshots[name][k]!=snapshots['global'][k]]
                assert changed==['content_charset.go'],changed
                (out/(name+'.diff')).write_text(''.join(difflib.unified_diff(orig.splitlines(True),c.read_text().splitlines(True),fromfile='global/content_charset.go',tofile=name+'/content_charset.go')))
                (out/(name+'_charset.go.txt')).write_bytes(c.read_bytes())
            shutil.copyfile(ROOT/'probe.go.txt',p/'escape_test.go')
            r=subprocess.run(['go','test','-count=1','-v','.'],cwd=p,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (out/(name+'.log')).write_text(r.stdout);r.check_returncode()
            rows={tuple(map(int,x.split()[1:5])):tuple(map(int,x.split()[5:9])) for x in r.stdout.splitlines() if x.startswith('ESC ')}
            assert len(rows)==640
            vectors[name]=rows
    assert all(set(v)==set(vectors['global']) for v in vectors.values())
    results={}
    for name in ('global','bypass','fallback'):
        mismatch=[0]*4
        for k,got in vectors[name].items():
            a=vectors['global'][k][0];b=vectors['independent'][k][1];both=204 if a==b==204 else 415
            for i,(x,y) in enumerate(zip(got,(a,b,both,both))):mismatch[i]+=x!=y
        results[name]={'mismatch_type_charset_ab_ba':mismatch,'cases':640,'production_files_changed':0 if name=='global' else 1}
    assert results['global']['mismatch_type_charset_ab_ba'][1]>0
    for n in ('bypass','fallback'):assert results[n]['mismatch_type_charset_ab_ba']==[0]*4
    summary={'results':results,'source_blobs':{n:{k:blob(v) for k,v in m.items()} for n,m in snapshots.items()},'native_runs':4,'status_observations':4*640*4,'original_protected_cases':4*12,'original_token_observations':4*16}
    (out/'result.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n'); print(json.dumps(summary,indent=2,sort_keys=True))

if __name__=='__main__':main(Path(sys.argv[1]).resolve(),Path(sys.argv[2]).resolve())
