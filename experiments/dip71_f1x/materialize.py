from pathlib import Path
import subprocess, shutil, json, re

BASE='374155134a39439060fb84a535bc8051f4ef5dfe'
ROOT=Path('/tmp/dip71_f1x_exec')
OUT=Path('experiments/dip71_f1x/RESULT_SEAL.json')
REPO='https://github.com/picoduck/wollipog.git'
LEGACY='Codex — Interactive'
CANON='Codex App Server'

if ROOT.exists(): shutil.rmtree(ROOT)
ROOT.mkdir(parents=True)

def run(cmd,cwd=None,check=True):
    return subprocess.run(cmd,cwd=cwd,text=True,capture_output=True,check=check)

def clone(name):
    d=ROOT/name
    run(['git','clone','--quiet',REPO,str(d)])
    run(['git','checkout','--quiet',BASE],cwd=d)
    assert run(['git','rev-parse','HEAD'],cwd=d).stdout.strip()==BASE
    run(['git','config','user.name','EvoNOMOS'],cwd=d)
    run(['git','config','user.email','evonomos@example.invalid'],cwd=d)
    return d

def text(p): return p.read_text()
def write(p,s): p.write_text(s)
def repl(p,old,new,n=1):
    s=text(p)
    c=s.count(old)
    if c < n: raise RuntimeError(f'{p}: expected >= {n} occurrences of {old!r}, found {c}')
    write(p,s.replace(old,new,n))

def common_phase0(d):
    repl(d/'apps/web/src/components/NewSessionDialog.tsx','Use Recommended','Use Codex App Server')
    repl(d/'apps/web/src/components/NewSessionDialog.tsx','Codex App Server is recommended for new sessions.','Codex App Server supports interactive approvals and resumable conversations.')
    repl(d/'apps/control-plane/src/sessions.ts','Finding sessions with Codex Interactive','Finding sessions with Codex App Server')
    repl(d/'apps/web/src/components/AgentSessionDiscoveryDialog.tsx','Codex Interactive session discovery','Codex App Server session discovery')

def direct_phase0(d):
    common_phase0(d)
    repl(d/'apps/control-plane/src/archive-session-page.ts','? "Codex — Interactive"','? "Codex App Server"')
    repl(d/'apps/control-plane/src/db.ts',"WHEN session.driver='codex-app-server' THEN 'Codex — Interactive'", "WHEN session.driver='codex-app-server' THEN 'Codex App Server'")
    p=d/'apps/web/src/components/agent-options.ts'
    repl(p,'if (a.driver === "codex" || a.driver === "codex-app-server") return "Codex";', 'if (a.driver === "codex-app-server") return "Codex App Server";\n  if (a.driver === "codex") return "Codex";')
    repl(p,'if (a.driver === "codex-app-server") return `Interactive (Recommended)${wsl}`;', 'if (a.driver === "codex-app-server") return a.context?.kind === "wsl" ? `WSL: ${a.context.distro}` : "";')
    repl(p,'if (driver === "codex-app-server") return "Codex — Interactive";', 'if (driver === "codex-app-server") return "Codex App Server";')
    repl(d/'apps/web/src/onboarding.ts','name: "Codex — Interactive"','name: "Codex App Server"')

def invert_phase0(d):
    common_phase0(d)
    proto=d/'packages/protocol/src/index.ts'
    s=text(proto)
    marker='export type AgentDriverKind = "acp" | "claude-code" | "codex" | "codex-app-server";'
    if marker not in s: raise RuntimeError('protocol driver marker missing')
    provider='''export const CODEX_APP_SERVER_DISPLAY_NAME = "Codex App Server";\nexport function stableAgentDisplayName(driver: AgentDriverKind | null | undefined, name: string | null | undefined): string {\n  if (driver === "codex-app-server") return CODEX_APP_SERVER_DISPLAY_NAME;\n  return name ?? driver ?? "Agent";\n}\n'''
    write(proto,s.replace(marker,marker+'\n\n'+provider,1))
    p=d/'apps/control-plane/src/archive-session-page.ts'
    repl(p,'import type { SessionStatus, SessionView } from "@wollipog/protocol";', 'import { stableAgentDisplayName, type SessionStatus, type SessionView } from "@wollipog/protocol";')
    old='''  const agent = conductor\n    ? "Conductor (Wollipog)"\n    : session.driver === "codex-app-server"\n    ? "Codex — Interactive"\n    : session.driver === "codex"\n      ? "Codex — Non-Interactive (codex exec)"\n      : session.agentName ?? session.agentId ?? session.driver;'''
    new='''  const agent = conductor\n    ? "Conductor (Wollipog)"\n    : session.driver === "codex"\n      ? "Codex — Non-Interactive (codex exec)"\n      : stableAgentDisplayName(session.driver, session.agentName ?? session.agentId ?? session.driver);'''
    repl(p,old,new)
    p=d/'apps/control-plane/src/db.ts'
    s=text(p)
    first_import=s.find('\n')
    write(p,s[:first_import+1]+'import { CODEX_APP_SERVER_DISPLAY_NAME } from "@wollipog/protocol";\n'+s[first_import+1:])
    repl(p,"WHEN session.driver='codex-app-server' THEN 'Codex — Interactive'", "WHEN session.driver='codex-app-server' THEN '${CODEX_APP_SERVER_DISPLAY_NAME}'")
    p=d/'apps/web/src/components/agent-options.ts'
    repl(p,'import type { AgentDefinition } from "@wollipog/protocol";', 'import { stableAgentDisplayName, type AgentDefinition } from "@wollipog/protocol";')
    repl(p,'if (a.driver === "codex" || a.driver === "codex-app-server") return "Codex";', 'if (a.driver === "codex-app-server") return stableAgentDisplayName(a.driver, a.name);\n  if (a.driver === "codex") return "Codex";')
    repl(p,'if (a.driver === "codex-app-server") return `Interactive (Recommended)${wsl}`;', 'if (a.driver === "codex-app-server") return a.context?.kind === "wsl" ? `WSL: ${a.context.distro}` : "";')
    repl(p,'if (driver === "codex-app-server") return "Codex — Interactive";', 'if (driver === "codex-app-server") return stableAgentDisplayName(driver, agentName ?? agentId);')
    p=d/'apps/web/src/onboarding.ts'
    s=text(p); first=s.find('\n')
    write(p,s[:first+1]+'import { CODEX_APP_SERVER_DISPLAY_NAME } from "@wollipog/protocol";\n'+s[first+1:])
    repl(p,'name: "Codex — Interactive"','name: CODEX_APP_SERVER_DISPLAY_NAME')

def direct_phase1(d):
    p=d/'apps/control-plane/src/archive-session-page.ts'
    repl(p,'  const agent = conductor\n    ? "Conductor (Wollipog)"', '  const agent = conductor\n    ? "Conductor (Wollipog)"\n    : session.agentName === "Codex — Interactive"\n      ? "Codex App Server"')
    p=d/'apps/web/src/components/agent-options.ts'
    repl(p,'  if (driver === "codex-app-server") return "Codex App Server";', '  if (agentName === "Codex — Interactive") return "Codex App Server";\n  if (driver === "codex-app-server") return "Codex App Server";')

def invert_phase1(d):
    p=d/'packages/protocol/src/index.ts'
    repl(p,'  if (driver === "codex-app-server") return CODEX_APP_SERVER_DISPLAY_NAME;\n  return name ?? driver ?? "Agent";', '  if (driver === "codex-app-server" || name === "Codex — Interactive") return CODEX_APP_SERVER_DISPLAY_NAME;\n  return name ?? driver ?? "Agent";')

def production_files(d):
    r=run(['git','diff','--name-only',BASE],cwd=d).stdout.splitlines()
    return [x for x in r if not re.search(r'(^|/)(test|tests|e2e)(/|\.|$)',x)]

def measure(d,base_ref):
    files=production_files(d) if base_ref==BASE else run(['git','diff','--name-only',base_ref],cwd=d).stdout.splitlines()
    files=[x for x in files if not re.search(r'(^|/)(test|tests|e2e)(/|\.|$)',x)]
    run(['git','add','--']+files,cwd=d)
    num=run(['git','diff','--cached','--numstat',base_ref],cwd=d).stdout.strip().splitlines()
    churn=0; counted=[]
    for line in num:
        a,b,path=line.split('\t')
        if a=='-' or b=='-': raise RuntimeError('binary production diff')
        churn += int(a)+int(b); counted.append(path)
    return len(counted),churn,num

def oracle(d,phase,arm):
    prod='\n'.join(text(d/x) for x in production_files(d))
    forbidden=['Interactive (Recommended)','Use Recommended','Finding sessions with Codex Interactive','Codex Interactive session discovery']
    for f in forbidden:
        if f in prod: raise RuntimeError(f'{arm} {phase}: forbidden stale phrase remains {f}')
    # four independently-authored phase-0 seams must expose canonical app-server identity.
    checks={
      'archive': 'Codex App Server' in text(d/'apps/control-plane/src/archive-session-page.ts'),
      'db': ('Codex App Server' in text(d/'apps/control-plane/src/db.ts') or 'CODEX_APP_SERVER_DISPLAY_NAME' in text(d/'apps/control-plane/src/db.ts')),
      'picker-session': ('Codex App Server' in text(d/'apps/web/src/components/agent-options.ts') or 'stableAgentDisplayName' in text(d/'apps/web/src/components/agent-options.ts')),
      'onboarding': ('Codex App Server' in text(d/'apps/web/src/onboarding.ts') or 'CODEX_APP_SERVER_DISPLAY_NAME' in text(d/'apps/web/src/onboarding.ts')),
    }
    if not all(checks.values()): raise RuntimeError(f'{arm} {phase}: seam oracle {checks}')
    if phase==1:
        if arm=='DIRECT':
            if text(d/'apps/control-plane/src/archive-session-page.ts').count('session.agentName === "Codex — Interactive"')!=1: raise RuntimeError('direct legacy archive guard missing')
            if text(d/'apps/web/src/components/agent-options.ts').count('agentName === "Codex — Interactive"')!=1: raise RuntimeError('direct legacy session guard missing')
        else:
            ps=text(d/'packages/protocol/src/index.ts')
            if 'driver === "codex-app-server" || name === "Codex — Interactive"' not in ps: raise RuntimeError('invert provider legacy equivalence missing')
            if ps.count('name === "Codex — Interactive"')!=1: raise RuntimeError('invert legacy equivalence not single-owner')
    run(['git','diff','--check'],cwd=d)
    return True

def execute(name,p0,p1):
    d=clone(name.lower())
    p0(d); oracle(d,0,name)
    F0,C0,num0=measure(d,BASE)
    run(['git','commit','-m',f'{name} phase0'],cwd=d)
    phase0=run(['git','rev-parse','HEAD'],cwd=d).stdout.strip()
    p1(d); ok=oracle(d,1,name)
    F1,C1,num1=measure(d,phase0)
    run(['git','commit','-m',f'{name} phase1'],cwd=d)
    return {'V':[F0,C0,F1,C1,1 if ok else 0],'phase0_numstat':num0,'phase1_numstat':num1,'phase0_commit':phase0,'phase1_commit':run(['git','rev-parse','HEAD'],cwd=d).stdout.strip()}

D=execute('DIRECT',direct_phase0,direct_phase1)
I=execute('INVERT',invert_phase0,invert_phase1)
delta=[I['V'][i]-D['V'][i] for i in range(5)]
# Utility-free geometry over cost coordinates where lower is better and P1 where higher is better.
def dominates(a,b):
    return all(a[i]<=b[i] for i in range(4)) and a[4]>=b[4] and (any(a[i]<b[i] for i in range(4)) or a[4]>b[4])
if dominates(D['V'],I['V']): geom='PARETO_DIRECT'
elif dominates(I['V'],D['V']): geom='PARETO_INVERT'
else: geom='TRADEOFF'
seal={'stage':'EvoNOMOS Generation VI DIP-71-F1-X','subject':'picoduck/wollipog#294','exact_base':BASE,'phase1_morphism':'exact legacy generated label Codex — Interactive joins canonical Codex App Server equivalence class; custom names preserved','DIRECT':D,'INVERT':I,'d_I_minus_D':delta,'geometry':geom,'oracle':'PASS','authority':'first complete paired readout; mandatory PI re-Court; no prevalence/moderator law by itself'}
OUT.write_text(json.dumps(seal,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(seal,indent=2,ensure_ascii=False))
