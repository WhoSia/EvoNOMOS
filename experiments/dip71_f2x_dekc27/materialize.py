#!/usr/bin/env python3
import json, pathlib, subprocess, tempfile, textwrap, shutil

BASE='cdfcddb12f6248d881fd6789c905bae30058ecdd'
REPO='https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture.git'
OUT=pathlib.Path(__file__).with_name('RESULT_SEAL.json')


def run(cmd,cwd=None,check=True):
    p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if check and p.returncode:
        raise RuntimeError(f"command failed {cmd}:\n{p.stdout}")
    return p


def replace_once(path,old,new):
    s=path.read_text(encoding='utf-8')
    if s.count(old)!=1:
        raise RuntimeError(f'expected exactly one patch site in {path}: {old!r}, got {s.count(old)}')
    path.write_text(s.replace(old,new,1),encoding='utf-8')


def clone_subject(root):
    root.mkdir(parents=True,exist_ok=True)
    d=root/'subject'
    run(['git','clone','--quiet',REPO,str(d)])
    run(['git','checkout','--quiet',BASE],d)
    got=run(['git','rev-parse','HEAD'],d).stdout.strip()
    if got!=BASE: raise RuntimeError(f'base mismatch {got}')
    run(['git','config','user.email','evonomos@example.invalid'],d)
    run(['git','config','user.name','EvoNOMOS'],d)
    return d


def phase0(subject,arm):
    grade=subject/'scripts/dekc_grade.py'
    if arm=='DIRECT':
        replace_once(grade,'\ndef _clamp(x: float) -> float:\n',
            '\ndef _safe_description(value) -> str:\n    return value if isinstance(value, str) else ""\n\n\ndef _clamp(x: float) -> float:\n')
        fn='_safe_description'
    else:
        common=subject/'scripts/dekc_common.py'
        with common.open('a',encoding='utf-8') as f:
            f.write('\n\ndef safe_text(value) -> str:\n    """Canonical tolerant text boundary for mixed-bundle scalar fields."""\n    return value if isinstance(value, str) else ""\n')
        replace_once(grade,'    append_log,\n','    append_log,\n    safe_text,\n')
        fn='safe_text'
    replace_once(grade,'        blob = (fm.get("description") or "") + "\\n" + (body or "")\n',
        f'        blob = {fn}(fm.get("description")) + "\\n" + (body or "")\n')
    replace_once(grade,'        desc = (fm.get("description") or body or "").strip().lower()\n',
        f'        desc = ({fn}(fm.get("description")) or body or "").strip().lower()\n')


def phase1(subject,arm):
    business=subject/'scripts/dekc_business.py'
    index=subject/'scripts/dekc_index.py'
    if arm=='DIRECT':
        replace_once(business,'\ndef infer_definition(title: str, fm: dict, body: str) -> str:\n',
            '\ndef _safe_description(value) -> str:\n    return value if isinstance(value, str) else ""\n\n\ndef infer_definition(title: str, fm: dict, body: str) -> str:\n')
        bfn='_safe_description'
        replace_once(index,'\ndef tokenize(text: str) -> list[str]:\n',
            '\ndef _safe_description(value) -> str:\n    return value if isinstance(value, str) else ""\n\n\ndef tokenize(text: str) -> list[str]:\n')
        ifn='_safe_description'
    else:
        replace_once(business,'from dekc_common import list_concepts, parse_frontmatter, resolve_knowledge_root, slugify  # noqa: E402\n',
            'from dekc_common import list_concepts, parse_frontmatter, resolve_knowledge_root, safe_text, slugify  # noqa: E402\n')
        bfn='safe_text'
        replace_once(index,'from dekc_common import list_concepts, resolve_knowledge_root  # noqa: E402\n',
            'from dekc_common import list_concepts, resolve_knowledge_root, safe_text  # noqa: E402\n')
        ifn='safe_text'
    replace_once(business,'    desc = (fm.get("description") or "").strip()\n',
        f'    desc = {bfn}(fm.get("description")).strip()\n')
    replace_once(index,'        text = f"{fm.get(\'title\',\'\')} {fm.get(\'description\',\'\')} {fm.get(\'type\',\'\')} {\' \'.join(fm.get(\'tags\') or [])} {body}"\n',
        f'        text = f"{{fm.get(\'title\',\'\')}} {{{ifn}(fm.get(\'description\'))}} {{fm.get(\'type\',\'\')}} {{\' \'.join(fm.get(\'tags\') or [])}} {{body}}"\n')
    replace_once(index,'            "description": fm.get("description") or "",\n',
        f'            "description": {ifn}(fm.get("description")),\n')


def oracle(subject,phase):
    code=textwrap.dedent('''
        import json, pathlib, sys, tempfile
        root=pathlib.Path(__file__).resolve().parent
        sys.path.insert(0,str(root/'scripts'))
        import dekc_grade
        td=tempfile.TemporaryDirectory(); bundle=pathlib.Path(td.name)/'knowledge'; bundle.mkdir()
        path=bundle/'tables'/'x.md'; path.parent.mkdir(parents=True); path.write_text('fixture')
        fm={'type':'Table','title':'X','description':{'nested':'value'},'layer':'bronze','tags':[]}
        dekc_grade.list_concepts=lambda b:[(path,fm,'body text long enough for evidence traceability')]
        dekc_grade.build_graph=lambda b:{}
        dekc_grade.doctor=lambda b:{'concept_count':1,'edge_count':0,'validation_ok':True,'orphan_technical':[],'glossary_terms':0,'business_coverage':0.0,'index_built':False,'errors':[]}
        result=dekc_grade.grade_bundle(bundle)
        assert isinstance(result,dict) and 'score' in result
    ''')
    if phase==1:
        code += textwrap.dedent('''
            import dekc_business, dekc_index
            got=dekc_business.infer_definition('X',{'description':{'nested':'value'}},'Fallback prose line')
            assert got=='Fallback prose line', got
            ipath=bundle/'tables'/'y.md'; ipath.write_text('fixture')
            ifm={'type':'Table','title':'Y','description':{'secret_semantic_token':'SHOULD_NOT_INDEX'},'tags':[]}
            dekc_index.list_concepts=lambda b:[(ipath,ifm,'ordinary body')]
            dekc_index.build_graph=lambda b:{}
            manifest=dekc_index.build_index(bundle)
            inv=json.loads((bundle/'.index/inventory.json').read_text())
            assert inv[0]['description']=='', inv
            assert 'secret_semantic_token' not in json.dumps(inv).lower()
        ''')
    code += "print('ORACLE_PASS')\n"
    f=subject/'evonomos_oracle.py'; f.write_text(code,encoding='utf-8')
    p=run(['python3',str(f)],subject,check=False)
    f.unlink()
    return p.returncode==0,p.stdout


def measure(subject,files):
    run(['git','add',*files],subject)
    raw=run(['git','diff','--cached','--numstat'],subject).stdout.strip()
    rows=[x for x in raw.splitlines() if x.strip()]
    c=0
    for row in rows:
        a,d,_=row.split('\t',2); c+=int(a)+int(d)
    return len(rows),c,rows


def arm_run(root,arm):
    s=clone_subject(root/arm.lower())
    phase0(s,arm)
    ok0,log0=oracle(s,0)
    run(['python3','-m','py_compile','scripts/dekc_grade.py'] + (['scripts/dekc_common.py'] if arm=='INVERT' else []),s)
    f0=['scripts/dekc_grade.py'] + (['scripts/dekc_common.py'] if arm=='INVERT' else [])
    F0,C0,n0=measure(s,f0)
    if not ok0:
        return {'phase0_pass':False,'log':log0,'V':None}
    run(['git','commit','-m',f'evonomos DIP71 F2-X {arm} phase0'],s)
    phase1(s,arm)
    ok1,log1=oracle(s,1)
    run(['python3','-m','py_compile','scripts/dekc_business.py','scripts/dekc_index.py'],s)
    F1,C1,n1=measure(s,['scripts/dekc_business.py','scripts/dekc_index.py'])
    diffcheck=run(['git','diff','--cached','--check'],s,check=False)
    ok1=ok1 and diffcheck.returncode==0
    return {'F0':F0,'C0':C0,'F1':F1,'C1':C1,'P1':1 if ok1 else 0,
            'V':[F0,C0,F1,C1,1 if ok1 else 0], 'phase0_pass':ok0,'phase1_pass':ok1,
            'numstat0':n0,'numstat1':n1,'log_tail':(log0+log1+diffcheck.stdout)[-3000:]}


def classify(d,i):
    if not d.get('V') or not i.get('V') or not d['phase1_pass'] or not i['phase1_pass']:
        return 'FUNCTIONAL_HOLD',None
    dv=[i['V'][k]-d['V'][k] for k in range(5)]
    if all(x>=0 for x in dv[:4]) and any(x>0 for x in dv[:4]): return 'PARETO_DIRECT',dv
    if all(x<=0 for x in dv[:4]) and any(x<0 for x in dv[:4]): return 'PARETO_INVERT',dv
    return 'TRADEOFF',dv


def main():
    with tempfile.TemporaryDirectory() as td:
        root=pathlib.Path(td)
        d=arm_run(root,'DIRECT'); i=arm_run(root,'INVERT')
    cls,dv=classify(d,i)
    seal={'issue':'SpillwaveSolutions/data-engineering-knowledge-capture#27','base':BASE,
          'context_cell':{'D0':'LOW','Dplus':'HIGH'},
          'phase0':'grade-only tolerant description boundary; non-string/None becomes empty text',
          'phase1':'same policy propagated to dekc_business infer_definition and dekc_index build_index',
          'arms':{'DIRECT':d,'INVERT':i},'d_I_minus_D':dv,'classification':cls}
    OUT.write_text(json.dumps(seal,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(seal,indent=2))
    if cls=='FUNCTIONAL_HOLD': raise SystemExit(2)

if __name__=='__main__': main()
