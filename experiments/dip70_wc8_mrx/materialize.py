#!/usr/bin/env python3
import json, os, pathlib, re, shutil, subprocess, sys, tempfile

BASE='7a54e7b4303eb55ed87ecc12dee06c5a6dabd38c'
REPO='https://github.com/glacayo/simple-rms-theme.git'
OUT=pathlib.Path(__file__).with_name('RESULT_SEAL.json')
CSS='''/* EvoNOMOS invariant palette bridge for issue #29 */\n:root {\n  --rms-color-primary: #0f172a;\n  --rms-color-accent: #2563eb;\n  --rms-color-accent-2: #f59e0b;\n  --rms-color-surface: #ffffff;\n}\nbody { color: var(--rms-color-primary); }\n.btn { background-color: var(--rms-color-accent); }\n.footer-v2 { background-color: var(--rms-color-primary); color: var(--rms-color-surface); }\n.star-rating { color: var(--rms-color-accent-2); }\n'''
DEFAULTS={
 'company_palette_color_1':'#0f172a',
 'company_palette_color_2':'#2563eb',
 'company_palette_color_3':'#f59e0b',
 'company_palette_color_4':'#ffffff',
}
TOKENS={
 'company_palette_color_1':'--rms-color-primary',
 'company_palette_color_2':'--rms-color-accent',
 'company_palette_color_3':'--rms-color-accent-2',
 'company_palette_color_4':'--rms-color-surface',
}

def run(cmd,cwd=None,check=True):
    p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if check and p.returncode:
        raise RuntimeError(f"command failed {cmd}:\n{p.stdout}")
    return p

def clone_subject(root):
    d=root/'subject'
    run(['git','clone','--quiet',REPO,str(d)])
    run(['git','checkout','--quiet',BASE],d)
    got=run(['git','rev-parse','HEAD'],d).stdout.strip()
    if got != BASE: raise RuntimeError(f'base mismatch {got}')
    run(['git','config','user.email','evonomos@example.invalid'],d)
    run(['git','config','user.name','EvoNOMOS'],d)
    return d

def php_block(arm, phase1=False):
    if arm=='INVERT':
        body='''\n/** EvoNOMOS WC8-MR semantic palette sanitizer. */\nfunction rms_evonomos_palette_sanitize(string $raw, string $fallback): string {\n    $value = strtolower(trim($raw));\n'''
        if phase1:
            body += '''    if (preg_match('/^#[0-9a-f]{3}$/', $value)) {\n        return '#' . $value[1] . $value[1] . $value[2] . $value[2] . $value[3] . $value[3];\n    }\n'''
        body += '''    return preg_match('/^#[0-9a-f]{6}$/', $value) ? $value : $fallback;\n}\n'''
        calls=[f"rms_evonomos_palette_sanitize((string) rms_get_option('{f}', '{d}'), '{d}')" for f,d in DEFAULTS.items()]
    else:
        chunks=[]; calls=[]
        for i,(f,d) in enumerate(DEFAULTS.items(),1):
            fn=f'rms_evonomos_palette_slot_{i}'
            c=f'''\n/** EvoNOMOS WC8-MR slot-local palette predicate {i}. */\nfunction {fn}(string $raw): string {{\n    $value = strtolower(trim($raw));\n'''
            if phase1:
                c += f'''    if (preg_match('/^#[0-9a-f]{{3}}$/', $value)) {{\n        return '#' . $value[1] . $value[1] . $value[2] . $value[2] . $value[3] . $value[3];\n    }}\n'''
            c += f'''    return preg_match('/^#[0-9a-f]{{6}}$/', $value) ? $value : '{d}';\n}}\n'''
            chunks.append(c); calls.append(f"{fn}((string) rms_get_option('{f}', '{d}'))")
        body=''.join(chunks)
    vals='\n'.join([f"        '{field}' => {call}," for field,call in zip(DEFAULTS,calls)])
    emits='\n'.join([f"        '{TOKENS[field]}' => $values['{field}']," for field in DEFAULTS])
    body += f'''\nfunction rms_evonomos_palette_values(): array {{\n    return [\n{vals}\n    ];\n}}\n\nfunction rms_evonomos_palette_css(): string {{\n    $values = rms_evonomos_palette_values();\n    $tokens = [\n{emits}\n    ];\n    $parts = [];\n    foreach ($tokens as $name => $value) {{\n        $parts[] = $name . ':' . $value;\n    }}\n    return ':root{{' . implode(';', $parts) . ';}}';\n}}\n\nfunction rms_evonomos_enqueue_palette_bridge(): void {{\n    if (function_exists('wp_enqueue_style')) {{\n        wp_enqueue_style('rms-palette', get_template_directory_uri() . '/assets/css/rms-palette.css', [], null);\n    }}\n    if (function_exists('wp_add_inline_style')) {{\n        wp_add_inline_style('rms-palette', rms_evonomos_palette_css());\n    }}\n}}\nif (function_exists('add_action')) {{\n    add_action('wp_enqueue_scripts', 'rms_evonomos_enqueue_palette_bridge');\n}}\n'''
    return body

def install(subject,arm,phase1=False):
    p=subject/'inc/acf-theme-options.php'
    base=run(['git','show',f'{BASE}:inc/acf-theme-options.php'],subject).stdout
    p.write_text(base+php_block(arm,phase1),encoding='utf-8')
    css=subject/'assets/css/rms-palette.css'; css.parent.mkdir(parents=True,exist_ok=True); css.write_text(CSS,encoding='utf-8')

def oracle(subject,phase1=False):
    cases=[
      ({'company_palette_color_1':'#112233','company_palette_color_2':'#AABBCC','company_palette_color_3':'bad','company_palette_color_4':''}, ['#112233','#aabbcc','#f59e0b','#ffffff']),
      ({'company_palette_color_1':'<script>','company_palette_color_2':'#123456','company_palette_color_3':'#abcdef','company_palette_color_4':'#010203'}, ['#0f172a','#123456','#abcdef','#010203']),
    ]
    if phase1:
      cases.append(({'company_palette_color_1':'#abc','company_palette_color_2':'#0F8','company_palette_color_3':'#123456','company_palette_color_4':'#fff'}, ['#aabbcc','#00ff88','#123456','#ffffff']))
    php='''<?php\n$GLOBALS["opts"]=[];\nfunction add_action($a,$b){} function add_filter($a,$b){} function __($s,$d=null){return $s;}\nfunction acf_add_options_page($x){} function acf_add_local_field_group($x){}\nfunction get_field($n,$scope=null){return $GLOBALS["opts"][$n] ?? null;}\nfunction sanitize_key($s){return preg_replace('/[^a-z0-9_\\-]/','',strtolower($s));}\nfunction get_template_directory(){return __DIR__;} function get_template_directory_uri(){return 'https://example.invalid/theme';}\nfunction wp_enqueue_style(...$x){} function wp_add_inline_style(...$x){}\nrequire __DIR__ . '/inc/acf-theme-options.php';\n'''
    for opts,expected in cases:
        php += '$GLOBALS["opts"]=' + json.dumps(opts).replace(': ', '=>').replace('{','[').replace('}',']') + ';\n'
        # json->php conversion above leaves quoted keys/value and commas, valid array syntax after colons replaced
        php += '$v=rms_evonomos_palette_values();\n'
        for field,exp in zip(DEFAULTS,expected):
            php += f"if ($v['{field}'] !== '{exp}') {{ fwrite(STDERR, 'FAIL {field} got=' . $v['{field}'] . PHP_EOL); exit(31); }}\n"
        php += '$css=rms_evonomos_palette_css(); if (strpos($css,"<script>")!==false) exit(32);\n'
    php += "if (!is_readable(__DIR__ . '/assets/css/rms-palette.css')) exit(33); echo \"ORACLE_PASS\\n\";\n"
    # safer direct construction of PHP arrays
    def arr(o): return '['+','.join([json.dumps(k)+'=>'+json.dumps(v) for k,v in o.items()])+']'
    php='''<?php\n$GLOBALS["opts"]=[];\nfunction add_action($a,$b){} function add_filter($a,$b){} function __($s,$d=null){return $s;}\nfunction acf_add_options_page($x){} function acf_add_local_field_group($x){}\nfunction get_field($n,$scope=null){return $GLOBALS["opts"][$n] ?? null;}\nfunction sanitize_key($s){return preg_replace('/[^a-z0-9_\\-]/','',strtolower($s));}\nfunction get_template_directory(){return __DIR__;} function get_template_directory_uri(){return 'https://example.invalid/theme';}\nfunction wp_enqueue_style(...$x){} function wp_add_inline_style(...$x){}\nrequire __DIR__ . '/inc/acf-theme-options.php';\n'''
    for opts,expected in cases:
        php += '$GLOBALS["opts"]='+arr(opts)+';\n$v=rms_evonomos_palette_values();\n'
        for field,exp in zip(DEFAULTS,expected):
            php += f"if ($v['{field}'] !== '{exp}') {{ fwrite(STDERR, 'FAIL {field} got=' . $v['{field}'] . PHP_EOL); exit(31); }}\n"
        php += '$css=rms_evonomos_palette_css(); if (strpos($css,"<script>")!==false) exit(32);\n'
    php += "if (!is_readable(__DIR__ . '/assets/css/rms-palette.css')) exit(33); echo \"ORACLE_PASS\\n\";\n"
    f=subject/'evonomos_oracle.php'; f.write_text(php,encoding='utf-8')
    lint=run(['php','-l','inc/acf-theme-options.php'],subject)
    test=run(['php','evonomos_oracle.php'],subject,check=False)
    f.unlink()
    return test.returncode==0, lint.stdout+test.stdout

def stage_measure(subject):
    run(['git','add','inc/acf-theme-options.php','assets/css/rms-palette.css'],subject)
    lines=run(['git','diff','--cached','--numstat'],subject).stdout.strip().splitlines()
    C=0
    for line in lines:
        a,d,_=line.split('\t',2); C += int(a)+int(d)
    return len(lines),C,lines

def arm_run(root,arm):
    subject=clone_subject(root/arm.lower())
    install(subject,arm,False)
    ok0,log0=oracle(subject,False)
    F0,C0,n0=stage_measure(subject)
    if not ok0: return {'phase0_pass':False,'log':log0,'V':None}
    run(['git','commit','-m',f'evonomos wc8 {arm} phase0'],subject)
    sha0=run(['git','rev-parse','HEAD'],subject).stdout.strip()
    install(subject,arm,True)
    ok1,log1=oracle(subject,True)
    F1,C1,n1=stage_measure(subject)
    return {'F0':F0,'C0':C0,'F1':F1,'C1':C1,'P1':1 if ok1 else 0,'V':[F0,C0,F1,C1,1 if ok1 else 0],
            'phase0_pass':ok0,'phase1_pass':ok1,'phase0_sha':sha0,'numstat0':n0,'numstat1':n1,'log_tail':(log0+log1)[-3000:]}

def classify(d,i):
    dv=[i['V'][k]-d['V'][k] for k in range(5)]
    # lower is better on F/C; P1 must match for scientific comparison
    if not d['phase1_pass'] or not i['phase1_pass']: return 'FUNCTIONAL_HOLD',dv
    if all(x>=0 for x in dv[:4]) and any(x>0 for x in dv[:4]): return 'PARETO_DIRECT',dv
    if all(x<=0 for x in dv[:4]) and any(x<0 for x in dv[:4]): return 'PARETO_INVERT',dv
    return 'TRADEOFF',dv

def main():
    with tempfile.TemporaryDirectory() as td:
        root=pathlib.Path(td)
        d=arm_run(root,'DIRECT'); i=arm_run(root,'INVERT')
    cls,dv=classify(d,i)
    seal={'issue':'glacayo/simple-rms-theme#29','base':BASE,
          'morphism':'MR-1: E0=#RRGGBB; Phase1 adds semantically equivalent #RGB expanded to #RRGGBB',
          'phase1_followup':'accept #RGB as one equivalent representation class while preserving all #RRGGBB behavior',
          'arms':{'DIRECT':d,'INVERT':i},'d_I_minus_D':dv,'classification':cls}
    OUT.write_text(json.dumps(seal,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(seal,indent=2))
    if cls=='FUNCTIONAL_HOLD': sys.exit(2)
if __name__=='__main__': main()
