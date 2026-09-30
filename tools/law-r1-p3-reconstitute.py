#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, shutil
from pathlib import Path

ALL=[("IssueTracker","issue_tracker"),("NetGSM","sms"),("Mutlucell","sms"),("Verimor","sms"),("IletiMerkezi","sms")]
P0=[ALL[0]]
P1=ALL[1:]
EXPECTED_P2_MATERIALIZER_BLOB="6ce9dc792419bf51a2884508168babf78ad7b4ba"
EXPECTED_P2_ORACLE_BLOB="cf12e3d9617c021de86a736c706bc84c06aad9d9"
EXPECTED_P2_FIXTURE_BLOB="3183dd0cd7c8e2de0caea8bffbdd2bce0dc22b54"

def sha256(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_p2(path:Path):
    spec=importlib.util.spec_from_file_location("p2_materializer",path)
    if spec is None or spec.loader is None: raise RuntimeError("cannot load P2 materializer")
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

def materialize(mod,src:Path,dst:Path,arm:str,providers):
    mod.PROVIDERS=list(providers)
    mod.copy_birth(src,dst)
    if arm=="DISPERSED_MEMBERSHIP_EXTENSION": changed=mod.apply_dispersed(dst)
    elif arm=="DUAL_RUNTIME_MEMBERSHIP_REGISTRY": changed=mod.apply_dual(dst)
    else: raise RuntimeError(arm)
    return changed

def relevant_files(root:Path):
    out=[]
    exact={
      "server/notification.js",
      "src/components/NotificationDialog.vue",
      "src/components/notifications/index.js",
      "src/components/notifications/law-r1-p2-membership-registry.js",
      "server/notification-providers/law-r1-p2-membership-registry.js"
    }
    for p in root.rglob("*"):
        if not p.is_file(): continue
        rel=str(p.relative_to(root))
        if rel in exact or rel.startswith("server/notification-providers/") or rel.startswith("src/components/notifications/"):
            out.append(rel)
    return sorted(out)

def tree_receipt(root:Path):
    return [{"path":rel,"sha256":sha256(root/rel)} for rel in relevant_files(root)]

def compare(a:Path,b:Path):
    aa={x["path"]:x["sha256"] for x in tree_receipt(a)}
    bb={x["path"]:x["sha256"] for x in tree_receipt(b)}
    if aa!=bb:
        miss=sorted(set(aa)^set(bb))
        changed=sorted(k for k in set(aa)&set(bb) if aa[k]!=bb[k])
        raise RuntimeError(f"sealed treatment drift missing={miss[:10]} changed={changed[:10]}")
    return len(aa)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",required=True,type=Path)
    ap.add_argument("--repo-root",required=True,type=Path)
    ap.add_argument("--out",required=True,type=Path)
    ap.add_argument("--receipt",required=True,type=Path)
    a=ap.parse_args()

    mod=load_p2(a.repo_root/"tools/law-r1-p2-materialize.py")
    mod.PROVIDERS=list(ALL)
    baseline=mod.validate(a.source.resolve())

    if a.out.exists(): shutil.rmtree(a.out)
    a.out.mkdir(parents=True)

    arms={}
    for arm,slug in [("DISPERSED_MEMBERSHIP_EXTENSION","dispersed"),("DUAL_RUNTIME_MEMBERSHIP_REGISTRY","dual")]:
        birth=a.out/slug/"birth"
        phase0=a.out/slug/"phase0"
        phase1=a.out/slug/"phase1"
        sealed=a.out/slug/"sealed_final"
        mod.copy_birth(a.source.resolve(),birth)
        materialize(mod,a.source.resolve(),phase0,arm,P0)
        materialize(mod,a.source.resolve(),phase1,arm,ALL)
        materialize(mod,a.source.resolve(),sealed,arm,ALL)
        identity_count=compare(phase1,sealed)
        arms[arm]={
          "slug":slug,
          "birth":"birth",
          "phase0":"phase0",
          "phase1":"phase1",
          "sealed_identity_file_count":identity_count,
          "phase0_tree":tree_receipt(phase0),
          "phase1_tree":tree_receipt(phase1)
        }

    receipt={
      "schema_version":"law-r1-p3-reconstitution-v1",
      "source_commit":"398482d590daaac0d44e288c9be3bc6f6667f8b8",
      "p2_canonical_head":"0c40eac7a825780f7907a311cf670421f6aea13b",
      "expected_p2_git_blobs":{
        "materializer":EXPECTED_P2_MATERIALIZER_BLOB,
        "oracle":EXPECTED_P2_ORACLE_BLOB,
        "fixture":EXPECTED_P2_FIXTURE_BLOB
      },
      "baseline_census":baseline,
      "phase0_providers":[x[0] for x in P0],
      "phase1_incremental_providers":[x[0] for x in P1],
      "arms":arms,
      "verdict":"PASS_SEALED_PHASE_RECONSTITUTION"
    }
    a.receipt.parent.mkdir(parents=True,exist_ok=True)
    a.receipt.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("LAW_R1_P3_SEALED_RECONSTITUTION=PASS")

if __name__=="__main__": main()
