#!/usr/bin/env python3
"""P33 historical source-grounded support dominance test.

Non-exhaustive two-policy candidate family; not a new prospective H win.
"""
import argparse, hashlib, json
from pathlib import Path

ARMS={"DISPERSED_MEMBERSHIP_EXTENSION":"dispersed",
      "DUAL_RUNTIME_MEMBERSHIP_REGISTRY":"dual"}
BASE=("server/notification.js",
      "src/components/notifications/index.js",
      "src/components/NotificationDialog.vue")
ROOTS=("server/notification-providers", "src/components/notifications")

def eligible(rel):
    return rel in BASE or any(
        rel.startswith(pre+"/") and rel.endswith((".js",".vue"))
        for pre in ROOTS
    )

def inventory(root):
    paths=set(BASE)
    for pre in ROOTS:
        d=root/pre
        if d.exists():
            paths.update(str(p.relative_to(root)) for p in d.rglob("*") if p.is_file())
    return {p:hashlib.sha256((root/p).read_bytes()).hexdigest()
            for p in sorted(paths) if eligible(p) and (root/p).is_file()}

def changes(old,new):
    a,b=inventory(old),inventory(new)
    return sorted(k for k in set(a)|set(b) if a.get(k)!=b.get(k))

def verify(snapshots,p3_seal):
    p3=json.loads(p3_seal.read_text())
    assert p3["canonical_run"]==36670337111
    assert p3["oracle_strength"]["established"]=="BOUNDED_NO_NETWORK"
    supp={}
    for arm,slug in ARMS.items():
        root=snapshots/slug
        supp[arm]={"first":changes(root/"birth",root/"phase0"),
                   "follow":changes(root/"phase0",root/"phase1")}
    d=set(supp["DISPERSED_MEMBERSHIP_EXTENSION"]["first"])
    r=set(supp["DUAL_RUNTIME_MEMBERSHIP_REGISTRY"]["first"])
    assert d<r, f"birth support not strict subset: left_only={d-r} right_only={r-d}"
    expected={
        "server/notification-providers/law-r1-p2-membership-registry.js",
        "src/components/notifications/law-r1-p2-membership-registry.js"
    }
    assert r-d==expected, f"unexpected extra files: {r-d}"
    left=p3["vectors"]["DISPERSED_MEMBERSHIP_EXTENSION"]
    right=p3["vectors"]["DUAL_RUNTIME_MEMBERSHIP_REGISTRY"]
    assert left["phase0"]==[5,22,0,0,1]
    assert right["phase0"]==[2,36,0,3,1]
    assert left["phase1"]==[5,80,0,0,1]
    assert right["phase1"]==[2,75,0,0,1]
    assert right["phase1"][1] < left["phase1"][1]
    return {
        "schema":"P33_PINNED_REPAIR_OPTION_SUPPORT_GEOMETRY_V1",
        "frozen_source_birth":p3["source"].get("commit") if "source" in p3 else
            "398482d590daaac0d44e288c9be3bc6f6667f8b8",
        "predecessor_canonical_run":p3["canonical_run"],
        "candidate_family_scope":"TWO_PRESEALED_IMPL_POLICIES_ONLY__NOT_ALL_POSSIBLE_REPAIRS",
        "evidence_class":"HISTORICAL_RECONSTITUTION_NOT_FRESH_OUTCOME",
        "changed_file_supports":supp,
        "first_disperse_support_strict_subset_dual":True,
        "first_disperse_support_count":len(d),
        "first_dual_support_count":len(r),
        "first_dual_extra_files":sorted(r-d),
        "first_S_disperse_dual":[5,2],
        "first_L_disperse_dual":[22,36],
        "follow_S_disperse_dual":[5,2],
        "follow_L_disperse_dual":[80,75],
        "invalid_dominance_inference":
          "Initial subset dominance over touched files cannot imply future lifecycle cost dominance; a source-compatible superset intervention can change the future cost function.",
        "not_claimed":[
          "general repair set enumeration",
          "minimality among all admissible repairs",
          "out-of-sample prediction",
          "B0+/B1/B2 defeated",
          "unrestricted production API equivalence",
          "new formal theorem"
        ],
        "verdict":"HISTORICAL_SOURCE_GROUNDED_COUNTEREXAMPLE_TO_NAIVE_PRUNING__LAW_R2_HOLD"
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--snapshots",type=Path,required=True)
    p.add_argument("--p3-seal",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    out=verify(args.snapshots,args.p3_seal)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("P33_SOURCE_SUPPORT_PRUNING_NEGATIVE_CONTROL=PASS")

if __name__=="__main__":main()
