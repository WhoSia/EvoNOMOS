from pathlib import Path
import subprocess, shutil

BASE='374155134a39439060fb84a535bc8051f4ef5dfe'
ROOT=Path('/tmp/dip71_f1x')
SUB=ROOT/'subject'
if ROOT.exists(): shutil.rmtree(ROOT)
ROOT.mkdir(parents=True)
subprocess.run(['git','clone','--quiet','https://github.com/picoduck/wollipog.git',str(SUB)],check=True)
subprocess.run(['git','-C',str(SUB),'checkout','--quiet',BASE],check=True)
head=subprocess.check_output(['git','-C',str(SUB),'rev-parse','HEAD'],text=True).strip()
assert head==BASE, (head,BASE)
print('EXACT_BASE='+head)
patterns=['Codex — Interactive','Codex Interactive','Interactive (Recommended)','Use Recommended','codex-app-server','Codex App Server']
for p in patterns:
    print('\n=== PATTERN:',p,'===')
    r=subprocess.run(['git','-C',str(SUB),'grep','-n','-F',p],text=True,capture_output=True)
    print(r.stdout if r.stdout else '(none)')
print('\n=== candidate TS/TSX files with codex-app-server ===')
r=subprocess.run(['git','-C',str(SUB),'grep','-l','-F','codex-app-server','--','*.ts','*.tsx'],text=True,capture_output=True)
print(r.stdout)
