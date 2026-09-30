#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, urllib.request
from pathlib import Path

UPTIME = [
    ("Plivo","62a2d01d3f2eb6df47e1c987b7819bead6a91e2e"),
    ("Ooredoo","8854e00a9283bdd81f3353c3fe55626dbee79c69"),
    ("SMSGateway","a808c63fe93b7ce1f835f3c51ae25e3bf567e930"),
    ("AmootSMS","e4821321e559c887b14e37d9979e604b221a8945"),
    ("Indigo","e62702d868a0b072c6e1870e5278762319637f04"),
]
HA = [
    ("my_pv","87da2fb0da59e36b38bc5cb45b538a925a4bc569"),
    ("greencell","d63bb480409fc6b9068ed03bda6f2e87b36a36a5"),
]

def get_json(url:str):
    req=urllib.request.Request(url,headers={
        "Accept":"application/vnd.github+json",
        "User-Agent":"EvoNOMOS-LAW-R1-P4",
        "X-GitHub-Api-Version":"2022-11-28",
    })
    token=os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization",f"Bearer {token}")
    with urllib.request.urlopen(req,timeout=60) as r:
        return json.load(r)

def raw(url:str)->bytes:
    req=urllib.request.Request(url,headers={"User-Agent":"EvoNOMOS-LAW-R1-P4"})
    with urllib.request.urlopen(req,timeout=60) as r:
        return r.read()

def added_lines(patch:str)->list[str]:
    return [line[1:] for line in patch.splitlines() if line.startswith("+") and not line.startswith("+++")]

def uptime_commit(name,sha):
    j=get_json(f"https://api.github.com/repos/louislam/uptime-kuma/commits/{sha}")
    files={f["filename"]:f for f in j.get("files",[])}
    required=[
      "server/notification.js",
      "src/components/notifications/index.js",
      "src/components/NotificationDialog.vue",
    ]
    if any(x not in files for x in required):
        raise RuntimeError(f"{name}: missing membership surface")
    s=files["server/notification.js"].get("patch","")
    i=files["src/components/notifications/index.js"].get("patch","")
    d=files["src/components/NotificationDialog.vue"].get("patch","")
    sa=added_lines(s); ia=added_lines(i); da=added_lines(d)
    sites={
      "backend_provider_import": any("notification-providers/" in x and "require(" in x for x in sa),
      "backend_provider_instance_registry": any(re.search(r"new\s+[A-Za-z0-9_]+\(\)",x) for x in sa),
      "frontend_provider_import": any(x.strip().startswith("import ") and "./" in x for x in ia),
      "frontend_form_registry": any(re.search(r":\s*[A-Za-z0-9_]+,?$",x.strip()) for x in ia if not x.strip().startswith("import ")),
      "ui_category_registry": any(":" in x for x in da),
    }
    provider_files=[f for f in files if f.startswith("server/notification-providers/") and f.endswith(".js")]
    form_files=[f for f in files if f.startswith("src/components/notifications/") and f.endswith(".vue")]
    if len(provider_files)!=1 or len(form_files)!=1:
        raise RuntimeError(f"{name}: expected one provider/form file, got {provider_files} {form_files}")
    provider=provider_files[0]; form=form_files[0]
    return {
      "name":name,"sha":sha,"parent":j["parents"][0]["sha"],
      "message":j["commit"]["message"].splitlines()[0],
      "llm_coauthored":"anthropic.com" in j["commit"]["message"].lower() or "claude" in j["commit"]["message"].lower(),
      "membership_sites":sites,
      "S_observed":sum(sites.values()),
      "provider_file":provider,
      "provider_blob":files[provider]["sha"],
      "form_file":form,
      "form_blob":files[form]["sha"],
      "has_upstream_provider_test":any(f.startswith("test/backend-test/notification-providers/") for f in files),
      "eligible_product_churn":sum(
        f.get("additions",0)+f.get("deletions",0)
        for p,f in files.items()
        if p in required or p==provider or p==form
      )
    }

def ha_commit(name,sha):
    j=get_json(f"https://api.github.com/repos/home-assistant/core/commits/{sha}")
    files=[f["filename"] for f in j.get("files",[])]
    prefix=f"homeassistant/components/{name}/"
    local=[p for p in files if p.startswith(prefix)]
    generated=[p for p in files if p.startswith("homeassistant/generated/")]
    tests=[p for p in files if p.startswith(f"tests/components/{name}/")]
    other=[p for p in files if p not in local and p not in generated and p not in tests]
    manifest=f"{prefix}manifest.json"
    central_runtime_candidates=[
      p for p in other
      if p.startswith("homeassistant/") and p not in ("CODEOWNERS",)
    ]
    # requirements_all.txt and CODEOWNERS are dependency/governance surfaces, not runtime membership.
    nonruntime_allowed=set(["CODEOWNERS","requirements_all.txt"])
    unexpected_other=[p for p in other if p not in nonruntime_allowed]
    return {
      "name":name,"sha":sha,"parent":j["parents"][0]["sha"],
      "message":j["commit"]["message"].splitlines()[0],
      "manifest_added":manifest in files,
      "local_component_file_count":len(local),
      "generated_index_files":generated,
      "nonruntime_global_files":[p for p in other if p in nonruntime_allowed],
      "unexpected_handwritten_global_files":unexpected_other,
      "central_runtime_candidates":central_runtime_candidates,
      "boundary_classification":"PREEXISTING_COMPONENT_MANIFEST_BOUNDARY_SUFFICIENT"
        if manifest in files and not unexpected_other and not central_runtime_candidates
        else "BOUNDARY_NOT_ESTABLISHED",
      "cil_action":"ABSTAIN"
        if manifest in files and not unexpected_other and not central_runtime_candidates
        else "REVIEW"
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",required=True,type=Path)
    ap.add_argument("--indigo-dir",required=True,type=Path)
    a=ap.parse_args()

    uptime=[uptime_commit(n,s) for n,s in UPTIME]
    for x in uptime:
        if x["S_observed"]!=5:
            raise RuntimeError(f"Uptime merge did not realize five-site path: {x}")
    indigo=next(x for x in uptime if x["name"]=="Indigo")
    if not indigo["has_upstream_provider_test"]:
        raise RuntimeError("Indigo upstream behavioral test absent")

    idir=a.indigo_dir
    idir.mkdir(parents=True,exist_ok=True)
    downloads=[
      (indigo["provider_file"],"indigo.js"),
      (indigo["form_file"],"Indigo.vue"),
      ("test/backend-test/notification-providers/test-indigo.js","upstream-test-indigo.js")
    ]
    for rel,name in downloads:
        data=raw(f"https://raw.githubusercontent.com/louislam/uptime-kuma/{indigo['sha']}/{rel}")
        (idir/name).write_bytes(data)

    ha=[ha_commit(n,s) for n,s in HA]
    for x in ha:
        if x["cil_action"]!="ABSTAIN":
            raise RuntimeError(f"Home Assistant abstention boundary not established: {x}")

    out={
      "schema_version":"law-r1-p4-world-contact-v1",
      "uptime_kuma":{
        "merge_census":uptime,
        "all_five_site_path":True,
        "real_implementation_target":"Indigo",
        "real_implementation_provider_blob":indigo["provider_blob"],
        "real_implementation_form_blob":indigo["form_blob"],
        "llm_mediated_witness":{
          "present":indigo["llm_coauthored"],
          "authority":"DESCRIPTIVE_WITNESS_ONLY__NO_CAUSATION"
        }
      },
      "home_assistant":{
        "worlds":ha,
        "all_abstain":all(x["cil_action"]=="ABSTAIN" for x in ha),
        "support_domain_boundary":"PREEXISTING_BOUNDARY_COLLAPSES_MEMBERSHIP_SURFACE_DIFFERENCE"
      },
      "verdict":"PASS_WORLD_CONTACT_CENSUS"
    }
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("LAW_R1_P4_WORLD_CONTACT=PASS")

if __name__=="__main__":
    main()
