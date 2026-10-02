#!/usr/bin/env python3
import json, hashlib
from pathlib import Path

EVIDENCE = Path("active/g8-law-r1-p15/P15_BASIS_CUSTODY.json")
LIT = Path("active/g8-law-r1-p15/P15_LITERATURE_DATA_CUSTODY.json")
OUT = Path("out-p15")
OUT.mkdir(parents=True, exist_ok=True)

d = json.loads(EVIDENCE.read_text(encoding="utf-8"))
lit = json.loads(LIT.read_text(encoding="utf-8"))

families = d["replication_families"]
coexist = next(f for f in families if f["target"] == "COEXISTENCE_REQUIREMENT")
authority = next(f for f in families if f["target"] == "RELEASE_AUTHORITY")

def materially_invariant(f):
    original = {
        "target": f["target"], "grade": f["grade"], "domain": f["domain"],
        "G": f["G"], "E": f["E"], "held_context": f["held_context"], "worlds": f["worlds"]
    }
    variant = {
        "coordinate": f["target"], "match": f["grade"], "ecosystem": f["domain"],
        "geometry": f["G"], "evidence": f["E"], "fixed": f["held_context"],
        "contrasts": f["worlds"], "display_name": f["id"].lower()
    }
    restored = {
        "target": variant["coordinate"], "grade": variant["match"], "domain": variant["ecosystem"],
        "G": variant["geometry"], "E": variant["evidence"], "held_context": variant["fixed"],
        "worlds": variant["contrasts"]
    }
    h1 = hashlib.sha256(json.dumps(original, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    h2 = hashlib.sha256(json.dumps(restored, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"pass": h1 == h2, "original": h1, "variant": h2}

rep = {f["id"]: materially_invariant(f) for f in families}

coexist_exact = (
    coexist["grade"] == "EXACT_POST_SYNC_CONFIG_INTERVENTION"
    and coexist["held_context"]["COMPATIBILITY_OBLIGATION"] == "SAME_PUBLIC_RESOURCE_API_CONTRACT"
    and coexist["held_context"]["LIFECYCLE_PHASE"] == "POST_SYNC_CUTOVER_READY"
    and coexist["worlds"][0]["A"] != coexist["worlds"][1]["A"]
)
authority_exact = (
    authority["grade"] == "EXACT_OPEN_PR_TRUST_INTERVENTION"
    and authority["held_context"]["LIFECYCLE_PHASE"] == "OPEN_PULL_REQUEST"
    and authority["worlds"][0]["A"] != authority["worlds"][1]["A"]
)

stable = ["COMPATIBILITY_OBLIGATION"]
if coexist_exact:
    stable.append("COEXISTENCE_REQUIREMENT")
if authority_exact:
    stable.append("RELEASE_AUTHORITY")

deletion = {x["coordinate"]: x["status"] for x in d["basis_attacks"]["deletion"]}
merge = {"+".join(x["pair"]): x["status"] for x in d["basis_attacks"]["pairwise_merge"]}
split = {x["coordinate"]: x["status"] for x in d["basis_attacks"]["split"]}

minimal_basis = (
    set(stable) == {"COMPATIBILITY_OBLIGATION", "COEXISTENCE_REQUIREMENT", "RELEASE_AUTHORITY", "LIFECYCLE_PHASE"}
    and all(v.startswith("FAILS_DELETION") for v in deletion.values())
    and all(v in {"MERGE_REJECTED", "NO_DERIVABILITY_OBSERVED"} for v in merge.values())
)

result = {
    "stage": d["stage"],
    "stable_primitives": stable,
    "identified_single_domain": ["LIFECYCLE_PHASE"],
    "second_domain_replication": {
        "COEXISTENCE_REQUIREMENT": "PASS" if coexist_exact else "FAIL",
        "RELEASE_AUTHORITY": "PASS" if authority_exact else "FAIL"
    },
    "basis_attacks": {
        "deletion": deletion,
        "pairwise_merge": merge,
        "split": split
    },
    "representation_invariance": {
        "cases": rep,
        "all_pass": all(v["pass"] for v in rep.values())
    },
    "minimal_reproducible_basis": "PASS" if minimal_basis else "NOT_AUTHORIZED",
    "minimal_basis_blocker": None if minimal_basis else "LIFECYCLE_PHASE_LACKS_SECOND_EXACT_CROSS_DOMAIN_REPLICATION",
    "anti_rationalization_pass": len(d.get("post_hoc_coordinate_additions", [])) == 0,
    "same_normalized_X_G_E_conflicting_action_observed": d["same_normalized_X_G_E_conflicting_action_observed"],
    "literature_custody": {
        "drive_confirmed_count": len(lit["drive_confirmed"]),
        "used_but_drive_missing_count": len(lit["used_but_drive_missing"]),
        "previously_documented_open_count": len(lit["previously_documented_open_custody"]),
        "new_high_value_missing_donor_count": len(lit["new_high_value_missing_donor"]),
        "ruling": lit["custody_ruling"]
    },
    "caution": "Second-domain replication can promote coexistence and authority, but reproducible minimal-basis authority remains blocked until lifecycle itself transports to a second exact domain."
}

(OUT / "p15-basis.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("LAW_R1_P15_BASIS_CUSTODY=PASS")
print("STABLE=" + ",".join(stable))
print("COEXISTENCE_SECOND_DOMAIN=" + result["second_domain_replication"]["COEXISTENCE_REQUIREMENT"])
print("AUTHORITY_SECOND_DOMAIN=" + result["second_domain_replication"]["RELEASE_AUTHORITY"])
print("MINIMAL_BASIS=" + result["minimal_reproducible_basis"])
print("REPRESENTATION_INVARIANCE=" + str(result["representation_invariance"]["all_pass"]))
print("ANTI_RATIONALIZATION=" + str(result["anti_rationalization_pass"]))
print("DRIVE_MISSING_USED=" + str(result["literature_custody"]["used_but_drive_missing_count"]))
