"""R114: native bounded Context observations; exact two upstream blobs plus authored alternatives."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from observed_repair import blob, compile_model

ROOT=Path(__file__).resolve().parent
BASE='82220730e99d94f776de4471d71d7ebf40e889c9'
MERGED='fe79a7421b7c7dd2a513814b2afd568c0ccd3091'
CLIENT='''package client
import "example.org/chi"
func Capture(x *chi.Context) *chi.Context {
 if c,ok:=any(x).(interface{Clone() *chi.Context});ok{return c.Clone()}
 return nil
}
'''
LOCAL='''package client
import ("example.org/chi";"slices")
func Capture(x *chi.Context) *chi.Context {
 y:=&chi.Context{RoutePath:x.RoutePath,RouteMethod:x.RouteMethod}
 y.URLParams.Keys=slices.Clone(x.URLParams.Keys)
 y.URLParams.Values=slices.Clone(x.URLParams.Values)
 y.RoutePatterns=slices.Clone(x.RoutePatterns)
 return y
}
'''
EXPECTED={'base':[True,False,False],'local':[True,True,False],
          'shallow':[True,False,False],'merged':[True,True,True]}
KEYS=['legacy','public_snapshot','native_private']


def main(base,merged,out):
    base,merged=base.read_bytes(),merged.read_bytes()
    if blob(base)!=BASE or blob(merged)!=MERGED:
        raise ValueError('upstream blob mismatch')
    out.mkdir(parents=True,exist_ok=True)
    source={'base':(base,CLIENT),'local':(base,LOCAL),
            'shallow':(base+b'\nfunc (x *Context) Clone() *Context { y := *x; return &y }\n',CLIENT),
            'merged':(merged,CLIENT)}
    spec={'protected':['legacy'],'goals':{'public':['public_snapshot'],
           'full':['public_snapshot','native_private']},'allowed_owners':['app'],
          'path_owners':{'context.go':'upstream','client/capture.go':'app'},
          'transitions':[['base','local'],['base','shallow'],['base','merged'],['shallow','merged']],
          'snapshots':{}}
    for name,(context,client) in source.items():
        row={'files':{},'observations':{}}
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);(p/'client').mkdir()
            (p/'go.mod').write_text('module example.org/chi\n\ngo 1.23\n')
            (p/'shim.go').write_text('package chi\ntype Routes interface{}\ntype methodTyp uint\n')
            for logical,data in [('context.go',context),('client/capture.go',client.encode())]:
                (p/logical).write_bytes(data)
                f=name+'_'+logical.replace('/','_');(out/f).write_bytes(data)
                row['files'][logical]={'file':f,'blob':blob(data)}
            (p/'probe_test.go').write_bytes((ROOT/'probe.go.txt').read_bytes())
            (p/'client/probe_test.go').write_bytes((ROOT/'client_probe.go.txt').read_bytes())
            env={**os.environ,'GOTOOLCHAIN':'local','GOPROXY':'off','GOMAXPROCS':'2'}
            r=subprocess.run(['go','test','-race','-v','-count=1','./...'],cwd=p,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (out/(name+'.log')).write_text(r.stdout);print(name,r.stdout,flush=True);r.check_returncode()
            for line in r.stdout.splitlines():
                if line.startswith('OBS '):
                    _,key,value=line.split()
                    if key in row['observations'] or value not in ('true','false'):raise ValueError('invalid observation')
                    row['observations'][key]=value=='true'
            assert [row['observations'][k] for k in KEYS]==EXPECTED[name],row
        spec['snapshots'][name]=row
    (out/'manifest.json').write_text(json.dumps(spec,indent=2)+'\n')
    model=compile_model(spec,out)
    (out/'model.json').write_text(json.dumps(model,indent=2)+'\n')
    print(json.dumps(model,indent=2))


if __name__=='__main__':
    main(*(Path(a) for a in sys.argv[1:]))
