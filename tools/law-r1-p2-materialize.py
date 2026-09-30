#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess
from pathlib import Path

PROVIDERS=[("IssueTracker","issue_tracker"),("NetGSM","sms"),("Mutlucell","sms"),("Verimor","sms"),("IletiMerkezi","sms")]
SOURCE_SHA="398482d590daaac0d44e288c9be3bc6f6667f8b8"
EXPECTED_BASELINE=92

def run(*args,cwd=None): return subprocess.check_output(args,cwd=cwd,text=True).strip()
def write(path,text): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text,encoding="utf-8")
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def fname(name): return re.sub(r"(?<!^)(?=[A-Z])","-",name).lower()

def provider_js(name,kind):
    if kind=="issue_tracker":
        body='''        const status = heartbeatJSON && heartbeatJSON.status;
        const action = status === 0 ? "open" : status === 1 ? "close" : "test";
        return JSON.stringify({provider:this.name,transport:"issue_tracker",action,message:msg});'''
    else:
        body=f'''        return JSON.stringify({{provider:this.name,transport:"sms",endpoint:"{fname(name)}",message:msg}});'''
    return f'''class {name} {{
    name = "{name}";
    async send(notification,msg,monitorJSON=null,heartbeatJSON=null) {{
{body}
    }}
}}
module.exports = {name};
'''

def form_vue(name):
    return f'''<template>
  <div class="law-r1-p2-provider-form" data-provider="{name}">
    <input v-model="$parent.notification.lawR1P2Endpoint" type="text" />
  </div>
</template>
<script>
export default {{ name: "{name}LawR1P2Form" }};
</script>
'''

def census(root):
    server=(root/"server/notification.js").read_text(encoding="utf-8")
    front=(root/"src/components/notifications/index.js").read_text(encoding="utf-8")
    dialog=(root/"src/components/NotificationDialog.vue").read_text(encoding="utf-8")
    imports=len(re.findall(r'require\("\./notification-providers/',server))
    m=re.search(r'const list = \[(.*?)\n\s*\];',server,re.S)
    if not m: raise SystemExit("cannot locate backend provider list")
    instances=len(re.findall(r'\bnew\s+[A-Za-z0-9_]+\s*\(',m.group(1)))
    front_imports=len(re.findall(r'^import\s+',front,re.M))
    fm=re.search(r'const NotificationFormList = \{(.*?)\n\};',front,re.S)
    if not fm: raise SystemExit("cannot locate frontend form registry")
    forms=len(re.findall(r'^\s{4}["A-Za-z0-9_.-]+:',fm.group(1),re.M))
    return {"backend_provider_imports":imports,"backend_provider_instances":instances,"frontend_provider_imports":front_imports,"frontend_form_entries":forms,"dialog_bytes":len(dialog.encode())}

def validate(root):
    got=run("git","rev-parse","HEAD",cwd=root)
    if got!=SOURCE_SHA: raise SystemExit(f"wrong source head {got}")
    c=census(root)
    for k in ("backend_provider_imports","backend_provider_instances","frontend_provider_imports","frontend_form_entries"):
        if c[k]!=EXPECTED_BASELINE: raise SystemExit(f"baseline {k}={c[k]} expected {EXPECTED_BASELINE}")
    surfaces=[root/"server/notification.js",root/"src/components/notifications/index.js",root/"src/components/NotificationDialog.vue"]
    for n,_ in PROVIDERS:
        if any(n in p.read_text(encoding="utf-8") for p in surfaces): raise SystemExit(f"provider already present: {n}")
    return c

def copy_birth(source,dest):
    if dest.exists(): shutil.rmtree(dest)
    shutil.copytree(source,dest,symlinks=True,ignore=shutil.ignore_patterns(".git"))

def common_bytes(root):
    changed=[]
    for name,kind in PROVIDERS:
        p=root/f"server/notification-providers/{fname(name)}.js"; write(p,provider_js(name,kind)); changed.append(p)
        v=root/f"src/components/notifications/{name}.vue"; write(v,form_vue(name)); changed.append(v)
    return changed

def apply_dispersed(root):
    changed=common_bytes(root)
    server=root/"server/notification.js"; s=server.read_text(encoding="utf-8")
    anchor='const { commandExists } = require("./util-server");'
    imports="\n".join([f'const {n} = require("./notification-providers/{fname(n)}");' for n,_ in PROVIDERS])
    if anchor not in s: raise SystemExit("server import anchor missing")
    s=s.replace(anchor,imports+"\n"+anchor,1)
    marker="        const list = ["; members="\n".join([f"            new {n}()," for n,_ in PROVIDERS])
    if marker not in s: raise SystemExit("server list anchor missing")
    s=s.replace(marker,marker+"\n"+members,1); write(server,s); changed.append(server)

    idx=root/"src/components/notifications/index.js"; x=idx.read_text(encoding="utf-8")
    first='import Alerta from "./Alerta.vue";'; imports="\n".join([f'import {n} from "./{n}.vue";' for n,_ in PROVIDERS])
    x=x.replace(first,imports+"\n"+first,1)
    map_anchor="const NotificationFormList = {"; entries="\n".join([f"    {n}: {n}," for n,_ in PROVIDERS])
    x=x.replace(map_anchor,map_anchor+"\n"+entries,1); write(idx,x); changed.append(idx)

    dialog=root/"src/components/NotificationDialog.vue"; d=dialog.read_text(encoding="utf-8")
    other='            let other = {\n                GoogleSheets: "Google Sheets",'
    if other not in d: raise SystemExit("dialog other anchor missing")
    d=d.replace(other,other+'\n                IssueTracker: "Issue Tracker",',1)
    sms='            let smsServices = {'; sms_entries='\n'.join([f'                {n}: "{n}",' for n in ["NetGSM","Mutlucell","Verimor","IletiMerkezi"]])
    d=d.replace(sms,sms+"\n"+sms_entries,1); write(dialog,d); changed.append(dialog)
    return changed

def apply_dual(root):
    changed=common_bytes(root)
    breg=root/"server/notification-providers/law-r1-p2-membership-registry.js"
    text="\n".join([f'const {n} = require("./{fname(n)}");' for n,_ in PROVIDERS])
    text+="\n\nmodule.exports = ["+", ".join([f"new {n}()" for n,_ in PROVIDERS])+"];\n"; write(breg,text); changed.append(breg)

    server=root/"server/notification.js"; s=server.read_text(encoding="utf-8")
    anchor='const { commandExists } = require("./util-server");'
    s=s.replace(anchor,'const lawR1P2MembershipRegistry = require("./notification-providers/law-r1-p2-membership-registry");\n'+anchor,1)
    s=s.replace("        const list = [","        const list = [\n            ...lawR1P2MembershipRegistry,",1); write(server,s); changed.append(server)

    freg=root/"src/components/notifications/law-r1-p2-membership-registry.js"
    t="\n".join([f'import {n} from "./{n}.vue";' for n,_ in PROVIDERS])
    t+="\n\nexport const lawR1P2NotificationForms = {\n"+"\n".join([f"    {n}: {n}," for n,_ in PROVIDERS])+"\n};\n"
    t+='export const lawR1P2NotificationCategories = {\n    other: { IssueTracker: "Issue Tracker" },\n    smsServices: { NetGSM: "NetGSM", Mutlucell: "Mutlucell", Verimor: "Verimor", IletiMerkezi: "IletiMerkezi" }\n};\n'
    write(freg,t); changed.append(freg)

    idx=root/"src/components/notifications/index.js"; x=idx.read_text(encoding="utf-8")
    first='import Alerta from "./Alerta.vue";'
    x=x.replace(first,'import { lawR1P2NotificationForms } from "./law-r1-p2-membership-registry.js";\n'+first,1)
    x=x.replace("const NotificationFormList = {","const NotificationFormList = {\n    ...lawR1P2NotificationForms,",1); write(idx,x); changed.append(idx)

    dialog=root/"src/components/NotificationDialog.vue"; d=dialog.read_text(encoding="utf-8")
    d=d.replace("<script>",'<script>\nimport { lawR1P2NotificationCategories } from "./notifications/law-r1-p2-membership-registry.js";',1)
    marker="            // Sort by notification name alphabetically"
    merge='            other = { ...other, ...lawR1P2NotificationCategories.other };\n            smsServices = { ...smsServices, ...lawR1P2NotificationCategories.smsServices };\n\n'
    if marker not in d: raise SystemExit("dialog merge anchor missing")
    d=d.replace(marker,merge+marker,1); write(dialog,d); changed.append(dialog)
    return changed

def custody(root,files):
    return [{"path":str(p.relative_to(root)),"sha256":sha(p)} for p in sorted(set(files),key=lambda p:str(p))]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--source",required=True); ap.add_argument("--out",required=True); ap.add_argument("--receipt",required=True); a=ap.parse_args()
    src=Path(a.source).resolve(); out=Path(a.out).resolve(); base=census(src); validate(src)
    disp=out/"dispersed"; dual=out/"dual_registry"; copy_birth(src,disp); copy_birth(src,dual)
    dc=apply_dispersed(disp); rc=apply_dual(dual)
    identical=[]
    for name,_ in PROVIDERS:
        for rel in [f"server/notification-providers/{fname(name)}.js",f"src/components/notifications/{name}.vue"]:
            x=sha(disp/rel); y=sha(dual/rel)
            if x!=y: raise SystemExit(f"cross-arm byte mismatch {rel}")
            identical.append({"path":rel,"sha256":x})
    receipt={"schema_version":"law-r1-p2-materialization-v1","source_commit":SOURCE_SHA,"baseline_census":base,"arms":{"DISPERSED_MEMBERSHIP_EXTENSION":{"custody":custody(disp,dc)},"DUAL_RUNTIME_MEMBERSHIP_REGISTRY":{"custody":custody(dual,rc)}},"cross_arm_identical_provider_bytes":identical,"outcomes_firewall":"S/L/C/A/Q LOC churn scalar winner CLOSED"}
    Path(a.receipt).parent.mkdir(parents=True,exist_ok=True); Path(a.receipt).write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")

if __name__=="__main__": main()
