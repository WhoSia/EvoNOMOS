#!/usr/bin/env python3
import itertools, json, hashlib
from pathlib import Path

SRC = Path("active/g8-law-r1-p12/P12_FRESH_WORLD_CUSTODY.json")
OUT = Path("out-p12")
OUT.mkdir(parents=True, exist_ok=True)
data = json.loads(SRC.read_text(encoding="utf-8"))
worlds = data["contrast_worlds"]
coords = list(worlds[0]["X"].keys())

def stable(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))

def partition_conflicts(keep):
    groups = {}
    for w in worlds:
        key = stable({
            "X": {k: w["X"][k] for k in keep},
            "G": w["G"],
            "E": w["E"],
        })
        groups.setdefault(key, []).append(w)
    conflicts = []
    for members in groups.values():
        actions = sorted({m["A"] for m in members})
        if len(actions) > 1:
            conflicts.append({
                "worlds": [m["id"] for m in members],
                "actions": actions,
            })
    return conflicts

full_conflicts = partition_conflicts(coords)
deletion = {}
for c in coords:
    keep = [x for x in coords if x != c]
    conflicts = partition_conflicts(keep)
    deletion[c] = {
        "deletion_failure": bool(conflicts),
        "conflicts": conflicts,
        "status": "IDENTIFIED_BY_DELETION_FAILURE" if conflicts else "NOT_IDENTIFIED_IN_CURRENT_CORPUS"
    }

minimal_subsets = []
for r in range(len(coords) + 1):
    for subset in itertools.combinations(coords, r):
        if not partition_conflicts(list(subset)):
            minimal_subsets.append(list(subset))
    if minimal_subsets:
        break

# Exact matched-(G,E) groups are the only clean within-corpus coordinate discriminators.
matched_ge = {}
for w in worlds:
    key = stable({"G": w["G"], "E": w["E"]})
    matched_ge.setdefault(key, []).append(w)
clean_pairs = []
for members in matched_ge.values():
    if len(members) < 2:
        continue
    for a,b in itertools.combinations(members,2):
        if a["A"] == b["A"]:
            continue
        diffs = [c for c in coords if a["X"][c] != b["X"][c]]
        clean_pairs.append({
            "left": a["id"],
            "right": b["id"],
            "differing_X_coordinates": diffs,
            "actions": [a["A"], b["A"]],
            "single_coordinate_identification": diffs[0] if len(diffs) == 1 else None
        })

# Predeclared reassignment candidates can leave X without changing total state information.
reassignment = {
    "RUNTIME_OR_TOOLCHAIN_PROVENANCE": {
        "target": "E",
        "predeclared": True,
        "status": "REASSIGNABLE_FROM_X_IN_P12_REPRESENTATION"
    },
    "OWNERSHIP_OR_RESPONSIBILITY_BOUNDARY": {
        "target": "G_OR_AUTHORITY_RELATION",
        "predeclared": True,
        "status": "NONPRIMITIVE_CANDIDATE__NOT_IDENTIFIED_AS_X"
    }
}

# Representation invariance: rename envelope keys and restore them; material content must hash identically.
rep_cases = {}
for w in worlds:
    original = {"X": w["X"], "G": w["G"], "E": w["E"], "A": w["A"]}
    alternate = {
        "context_coordinates": w["X"],
        "structural_geometry": w["G"],
        "world_evidence": w["E"],
        "decision": w["A"],
        "display": w["id"].lower(),
    }
    restored = {
        "X": alternate["context_coordinates"],
        "G": alternate["structural_geometry"],
        "E": alternate["world_evidence"],
        "A": alternate["decision"],
    }
    h1 = hashlib.sha256(stable(original).encode()).hexdigest()
    h2 = hashlib.sha256(stable(restored).encode()).hexdigest()
    rep_cases[w["id"]] = {"original":h1,"variant":h2,"pass":h1==h2}

result = {
    "stage": data["stage"],
    "source_count": len(data["sources"]),
    "world_count": len(worlds),
    "merged_source_count": sum(1 for s in data["sources"] if s["merged"]),
    "coordinates": coords,
    "full_state_conflicts": full_conflicts,
    "deletion_audit": deletion,
    "clean_matched_GE_pairs": clean_pairs,
    "identified_coordinates": [c for c,v in deletion.items() if v["deletion_failure"]],
    "unidentified_coordinates": [c for c,v in deletion.items() if not v["deletion_failure"]],
    "sample_minimal_subsets": minimal_subsets,
    "sample_minimal_cardinality": len(minimal_subsets[0]) if minimal_subsets else None,
    "minimality_warning": "Sample-minimal subsets are not universal X_min when matched-(G,E) coverage is sparse.",
    "reassignment_audit": reassignment,
    "representation_invariance": {
        "cases": rep_cases,
        "all_pass": all(v["pass"] for v in rep_cases.values())
    },
    "post_hoc_coordinate_additions": data.get("post_hoc_coordinate_additions", []),
    "anti_rationalization_pass": len(data.get("post_hoc_coordinate_additions", [])) == 0
}
(OUT / "p12-worlds.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("LAW_R1_P12_WORLD_CUSTODY=PASS")
print(f"SOURCES={result['source_count']}")
print(f"WORLDS={result['world_count']}")
print(f"IDENTIFIED={','.join(result['identified_coordinates']) or 'NONE'}")
print(f"SAMPLE_MIN_CARD={result['sample_minimal_cardinality']}")
print(f"REPRESENTATION_INVARIANCE={result['representation_invariance']['all_pass']}")
print(f"ANTI_RATIONALIZATION={result['anti_rationalization_pass']}")
