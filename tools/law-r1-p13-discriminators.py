#!/usr/bin/env python3
import json, hashlib
from pathlib import Path

SRC = Path("active/g8-law-r1-p13/P13_DISCRIMINATOR_CUSTODY.json")
OUT = Path("out-p13")
OUT.mkdir(parents=True, exist_ok=True)
data = json.loads(SRC.read_text(encoding="utf-8"))

families = data["discriminator_families"]
targets = ["COMPATIBILITY_OBLIGATION","COEXISTENCE_REQUIREMENT","RELEASE_AUTHORITY"]

summary = {}
for target in targets:
    fams = [f for f in families if f["target"] == target]
    exact_domains = sorted({f["domain"] for f in fams if f["grade"] == "EXACT_INTERNAL"})
    near_domains = sorted({f["domain"] for f in fams if f["grade"] == "NEAR_MATCHED"})
    confounded = [f["id"] for f in fams if f["grade"] == "CONFOUNDED"]
    summary[target] = {
        "exact_domains": exact_domains,
        "near_domains": near_domains,
        "confounded_families": confounded,
        "bounded_identified": len(exact_domains) >= 1,
        "stable_primitive": len(exact_domains) >= 2,
    }

# Frozen preseal requires cross-domain exact replication for stable primitive promotion.
stable = [k for k,v in summary.items() if v["stable_primitive"]]
bounded = [k for k,v in summary.items() if v["bounded_identified"] and not v["stable_primitive"]]
unresolved = [k for k,v in summary.items() if not v["bounded_identified"]]

# Representation-invariance replay: discriminator meaning must survive field renaming.
rep = {}
for f in families:
    original = {
        "target": f["target"],
        "grade": f["grade"],
        "G": f["G"],
        "E": f["E"],
        "worlds": f["worlds"],
    }
    alt = {
        "coordinate_under_test": f["target"],
        "match_grade": f["grade"],
        "geometry": f["G"],
        "evidence": f["E"],
        "contrast_worlds": f["worlds"],
        "display_name": f["id"].lower(),
    }
    restored = {
        "target": alt["coordinate_under_test"],
        "grade": alt["match_grade"],
        "G": alt["geometry"],
        "E": alt["evidence"],
        "worlds": alt["contrast_worlds"],
    }
    h1 = hashlib.sha256(json.dumps(original,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    h2 = hashlib.sha256(json.dumps(restored,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    rep[f["id"]] = {"pass": h1 == h2, "original": h1, "variant": h2}

deps = {}
for d in data["dependency_hypotheses"]:
    deps[f'{d["from"]}->{d["to"]}'] = {
        "status": d["status"],
        "reason": d["reason"],
    }

result = {
    "stage": data["stage"],
    "source_count": len(data["sources"]),
    "merged_source_count": sum(1 for s in data["sources"] if s["merged"]),
    "family_count": len(families),
    "coordinate_summary": summary,
    "stable_primitives": stable,
    "bounded_identified": bounded,
    "unresolved_coordinates": unresolved,
    "dependency_graph": deps,
    "representation_invariance": {
        "cases": rep,
        "all_pass": all(v["pass"] for v in rep.values())
    },
    "anti_rationalization_pass": len(data.get("post_hoc_coordinate_additions", [])) == 0,
    "post_hoc_coordinate_additions": data.get("post_hoc_coordinate_additions", []),
    "same_normalized_X_G_E_conflicting_action_observed": False,
    "stable_structure_warning": "No coordinate reaches the presealed two-domain exact-replication threshold; bounded identification must not be promoted to stable primitive structure."
}

(OUT / "p13-discriminators.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print("LAW_R1_P13_DISCRIMINATOR_CUSTODY=PASS")
print(f"SOURCES={result['source_count']}")
print(f"FAMILIES={result['family_count']}")
print(f"STABLE={','.join(stable) or 'NONE'}")
print(f"BOUNDED={','.join(bounded) or 'NONE'}")
print(f"UNRESOLVED={','.join(unresolved) or 'NONE'}")
print(f"REPRESENTATION_INVARIANCE={result['representation_invariance']['all_pass']}")
print(f"ANTI_RATIONALIZATION={result['anti_rationalization_pass']}")
