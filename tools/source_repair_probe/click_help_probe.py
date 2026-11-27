"""Retrospective Click #2832; source-derived defaults, bounded native CLI checks."""
import ast
import hashlib
import importlib.metadata as md
import inspect
import json
import textwrap
from pathlib import Path
from unittest.mock import patch

import click
from click import decorators as d
from click.testing import CliRunner

PINS = {'core.py':'e6305011adf3f7450fa1e9392147e52b8acf2b0c',
        'decorators.py':'bcf8906e7098a3cf82bdd87855c410e86f4f4279',
        'parser.py':'600b8436d7c1e833cb3c5efea898b42d15d920c0',
        'testing.py':'772b2159ccd95d29d8d940fc818d3bb1d2610cbf'}


def extract():
    assert md.version('click') == '8.1.8'
    root = Path(click.__file__).parent
    for name, sha in PINS.items():
        raw = (root/name).read_bytes()
        assert hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest() == sha
    tree = ast.parse((root/'decorators.py').read_text())
    helper = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'help_option')
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'HelpOption')
    init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == '__init__')
    calls = [n.value for n in init.body if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
             and ast.unparse(n.value.func) == 'kwargs.setdefault']
    defaults = {ast.literal_eval(n.args[0]):ast.unparse(n.args[1]) for n in calls}
    guard = next(n for n in init.body if isinstance(n, ast.If) and ast.unparse(n.test) == 'not param_decls')
    decls = ast.literal_eval(guard.body[0].value)
    assert list(defaults) == ['is_flag','expose_value','is_eager','help','callback']
    assert ast.unparse(helper.body[-1]) == 'return option(*param_decls, **kwargs)'
    assert ast.unparse(helper.body[-2]) == "kwargs.setdefault('cls', HelpOption)"
    assert decls == ('--help',)
    # Intentionally restricted expression evaluator: no eval or arbitrary AST execution.
    values = {}
    for key, expr in defaults.items():
        node = ast.parse(expr, mode='eval').body
        if isinstance(node, ast.Constant): values[key] = node.value
        elif isinstance(node, ast.Call) and ast.unparse(node.func) == '_' and len(node.args)==1:
            values[key] = d._(ast.literal_eval(node.args[0]))
        elif ast.unparse(node) == 'self.show_help': values[key] = d.HelpOption.show_help
        else: raise ValueError(f'unsupported default {key}: {expr}')
    return decls, values, {'helper_line':helper.lineno,'constructor_line':init.lineno,
                           'default_expressions':defaults,'fallback_declarations':decls}


DECLS, DEFAULTS, SOURCE = extract()
ORIGINAL = d.help_option


def restored_help_option(*param_decls, **kwargs):
    """Candidate wrapper at the source-level decorator boundary, not upstream patch."""
    cls = kwargs.get('cls', d.HelpOption)
    if cls is None or not issubclass(cls, d.HelpOption):
        param_decls = param_decls or DECLS
        for k, v in DEFAULTS.items(): kwargs.setdefault(k,v)
    return ORIGINAL(*param_decls, **kwargs)


CASES = [
    ('automatic','auto',(),('--help',),{}),
    ('ordinary_explicit','default',('-h','--help'),('--help',),{}),
    ('custom_long','custom',('-h','--help'),('--help',),{}),
    ('custom_short','custom',('-h','--help'),('-h',),{}),
    ('custom_short_only','custom',('-h',),('-h',),{}),
    ('custom_no_decls','custom',(),('--help',),{}),
    ('custom_no_args','custom',('-h','--help'),(),{}),
    ('custom_help_text','custom',('-h','--help'),('--help',),{'help':'Personal help text'}),
    ('custom_callback','custom',('-h','--help'),('--help',),{'callback':'MARK'}),
    ('custom_explicit_false','custom',('-h','--help'),('--help','x'),{'is_flag':False}),
    ('custom_eager_before_bad','custom',('-h','--help'),('--help','--bad'),{}),
    ('help_subclass','help_subclass',('-h','--help'),('--help',),{}),
]
MODES = ('native','app_explicit','app_inherit','boundary_wrapper')


def one(case, mode):
    name, kind, decls, argv, overrides = case
    events = []
    class Custom(click.HelpOption if mode=='app_inherit' else click.Option):
        pass
    class HelpSubclass(click.HelpOption):
        pass
    def mark(ctx, param, value):
        events.append('custom_callback')
    def command():
        events.append('command')
        click.echo('COMMAND')
    options = dict(overrides)
    if options.get('callback') == 'MARK': options['callback'] = mark
    if kind == 'custom': options['cls'] = Custom
    elif kind == 'help_subclass': options['cls'] = HelpSubclass
    f = restored_help_option if mode=='boundary_wrapper' else ORIGINAL
    try:
        if kind != 'auto':
            if mode=='app_explicit' and kind=='custom':
                decls = decls or DECLS
                for k,v in DEFAULTS.items(): options.setdefault(k,v)
            command = f(*decls,**options)(command)
        cmd = click.command(name='probe')(command)
        param = cmd.params[0] if cmd.params else None
        result = CliRunner().invoke(cmd,list(argv),catch_exceptions=True)
        return dict(case=name,mode=mode,exit=result.exit_code,output=result.output,events=events,
                    param_class=type(param).__name__ if param else None,
                    exact_custom_type=type(param) is Custom if kind=='custom' else None,
                    custom_base=Custom.__bases__[0].__name__ if kind=='custom' else None,
                    is_flag=getattr(param,'is_flag',None),is_eager=getattr(param,'is_eager',None),
                    expose_value=getattr(param,'expose_value',None),
                    exception=type(result.exception).__name__ if result.exception else None)
    except Exception as exc:
        return dict(case=name,mode=mode,construction_error=type(exc).__name__,message=str(exc),events=events)


def run():
    rows=[one(c,m) for c in CASES for m in MODES]
    by={(r['case'],r['mode']):r for r in rows}
    def obs(r): return tuple(r.get(k) for k in ('exit','output','events','construction_error','message'))
    # Application explicit mode is equal-information conventional workaround, not ground truth.
    mismatch=[n for n,*_ in CASES if obs(by[n,'app_explicit'])!=obs(by[n,'boundary_wrapper'])]
    preserved=[n for n,*_ in CASES if obs(by[n,'native'])==obs(by[n,'boundary_wrapper'])]
    required=['custom_long','custom_short','custom_short_only','custom_no_decls','custom_help_text']
    def accepted(r): return r.get('exit')==0 and 'Usage:' in r.get('output','') and not r['events']
    scores={m:sum(accepted(by[n,m]) for n in required) for m in MODES}
    return dict(source=SOURCE,rows=rows,reported_help_contract_scores=scores,
                required_cases=required,explicit_vs_wrapper_mismatch=mismatch,native_unchanged=preserved,
                scope='finite installed 8.1.8; wrapper is invoked at decorator boundary, no package source on-disk modified; not historical 8.1.7 execution')


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
