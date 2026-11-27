"""Compare real file-boundary candidate with the earlier in-process wrapper."""
import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import click

HERE = Path(__file__).resolve().parent
ORIGINAL = Path(click.__file__).parent
SOURCE = (ORIGINAL/'decorators.py').read_text()
NEEDLE = '    kwargs.setdefault("cls", HelpOption)\n    return option(*param_decls, **kwargs)\n'
assert SOURCE.count(NEEDLE) == 1
# Reuse the source-derived expressions, substituting the static callback receiver.
source = json.loads((HERE/'result.json').read_text())['source']
lines = ['    cls = kwargs.get("cls", HelpOption)',
         '    if cls is None or not issubclass(cls, HelpOption):',
         '        if not param_decls:',
         '            param_decls = '+repr(tuple(source['fallback_declarations']))]
for k,expr in source['default_expressions'].items():
    if expr == 'self.show_help': expr = 'HelpOption.show_help'
    lines.append(f'        kwargs.setdefault({k!r}, {expr})')
PATCHED = SOURCE.replace(NEEDLE,'\n'.join(lines)+'\n'+NEEDLE)
# Exact 8.1.7 algorithm reconstructed from tag (body, no original docstring).
OLD_BODY = '''    def callback(ctx, param, value):
        if not value or ctx.resilient_parsing:
            return
        echo(ctx.get_help(), color=ctx.color)
        ctx.exit()

    if not param_decls:
        param_decls = ("--help",)

    kwargs.setdefault("is_flag", True)
    kwargs.setdefault("expose_value", False)
    kwargs.setdefault("is_eager", True)
    kwargs.setdefault("help", _("Show this message and exit."))
    kwargs["callback"] = callback
    return option(*param_decls, **kwargs)
'''
OLD_TRANSPLANT = SOURCE.replace(NEEDLE,OLD_BODY)
# Child script uses public API only; no monkeypatching or source-dependent oracle.
CHILD = '''import click,json,sys
from click.testing import CliRunner
cases=json.loads(sys.argv[1]); rows=[]
for name,kind,decls,argv,opts0 in cases:
    events=[]
    class Custom(click.Option): pass
    class HelpSubclass(click.HelpOption): pass
    def mark(ctx,param,value): events.append('custom_callback')
    def command(): events.append('command'); click.echo('COMMAND')
    opts=dict(opts0)
    if opts.get('callback')=='MARK': opts['callback']=mark
    if kind=='custom': opts['cls']=Custom
    elif kind=='help_subclass': opts['cls']=HelpSubclass
    try:
        if kind!='auto': command=click.help_option(*decls,**opts)(command)
        cmd=click.command(name='probe')(command)
        param=cmd.params[0] if cmd.params else None
        result=CliRunner().invoke(cmd,argv,catch_exceptions=True)
        rows.append(dict(case=name,exit=result.exit_code,output=result.output,events=events,
                         exact_custom_type=type(param) is Custom if kind=='custom' else None,
                         exception=type(result.exception).__name__ if result.exception else None))
    except Exception as e:
        rows.append(dict(case=name,construction_error=type(e).__name__,message=str(e),events=events))
print(json.dumps(dict(imported=click.__file__,rows=rows)))
'''
# Extract literal fixture list without importing earlier runner against changed package.
tree=ast.parse((HERE/'click_help_probe.py').read_text())
cases=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CASES' for t in n.targets)))
result={}
for mode,code in [('native',SOURCE),('patched',PATCHED),('old_body_transplant',OLD_TRANSPLANT)]:
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp); shutil.copytree(ORIGINAL,root/'click',ignore=shutil.ignore_patterns('__pycache__'))
        (root/'click'/'decorators.py').write_text(code)
        env={**os.environ,'PYTHONPATH':str(root),'PYTHONDONTWRITEBYTECODE':'1'}
        p=subprocess.run([sys.executable,'-c',CHILD,json.dumps(cases)],cwd=root,env=env,capture_output=True,text=True,check=True)
        r=json.loads(p.stdout);assert Path(r['imported']).parent==root/'click'
        result[mode]={'decorators_sha256':hashlib.sha256(code.encode()).hexdigest(),'rows':r['rows']}
old=result['old_body_transplant']['rows'];new=result['patched']['rows']
fields=('exit','output','events','construction_error','message')
result['old_transplant_vs_patched']=[a['case'] for a,b in zip(old,new) if any(a.get(k)!=b.get(k) for k in fields)]
result['original_vs_patched']=[a['case'] for a,b in zip(result['native']['rows'],new) if any(a.get(k)!=b.get(k) for k in fields)]
result['scope']='fresh subprocess per arm, 8.1.8 package copy, no production edits, old body algorithm transplant not 8.1.7 release execution'
print(json.dumps(result,indent=2))
