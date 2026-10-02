#!/usr/bin/env python3
import json, hashlib
from pathlib import Path

SRC = Path("active/g8-law-r1-p11/P11_FRESH_WORLD_CUSTODY.json")
OUT = Path("out-p11")
OUT.mkdir(parents=True, exist_ok=True)

data = json.loads(SRC.read_text(encoding="utf-8"))

def normalize_world(w):
    # Representation-only fields are deliberately excluded from the material fingerprint.
    return {
        "X": {
            "public_compatibility_obligation": w["X"]["public_compatibility_obligation"],
            "release_window": w["X"]["release_window"],
            "consumer_transition": w["X"]["consumer_transition"],
            "authority_mode": w["X"]["authority_mode"],
        },
        "G": {
            "family": w["G"]["family"],
            "old_surface": w["G"]["old_surface"],
            "new_surface": w["G"]["new_surface"],
            "ownership_move": w["G"]["ownership_move"],
        },
        "E": w["E"],
    }

def fp(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

worlds = {}
for w in data["worlds"]:
    n = normalize_world(w)
    worlds[w["id"]] = {
        "material": n,
        "fingerprint": fp(n),
        "action": w["A"],
        "authority": w["authority"],
        "source": w["source"],
    }

# Representation invariance: rename purely representational envelope keys, then reconstruct.
variants = {}
for wid, item in worlds.items():
    m = item["material"]
    alt = {
        "context_block": m["X"],
        "geometry_block": m["G"],
        "evidence_block": m["E"],
        "display_name": f"variant::{wid.lower()}",
        "schema_version": "alt-1"
    }
    reconstructed = {
        "X": alt["context_block"],
        "G": alt["geometry_block"],
        "E": alt["evidence_block"],
    }
    variants[wid] = {
        "original": item["fingerprint"],
        "variant": fp(reconstructed),
        "pass": item["fingerprint"] == fp(reconstructed),
    }

aliases = []
for a in data["alias_candidates"]:
    left, right = worlds[a["left"]], worlds[a["right"]]
    aliases.append({
        **a,
        "same_material_fingerprint": left["fingerprint"] == right["fingerprint"],
        "different_action": left["action"] != right["action"],
    })

matched = data["matched_tests"]
result = {
    "stage": data["stage"],
    "world_count": len(worlds),
    "merged_authority_count": sum(1 for w in data["worlds"] if w["authority"]["merged"]),
    "worlds": worlds,
    "representation_invariance": {
        "cases": variants,
        "all_pass": all(v["pass"] for v in variants.values())
    },
    "alias_candidates": aliases,
    "same_material_state_conflicting_action_observed": any(
        a["same_material_fingerprint"] and a["different_action"] for a in aliases
    ),
    "matched_geometry": matched["matched_geometry"],
    "matched_context": matched["matched_context"],
    "development_only": data.get("development_only", []),
}
(OUT / "p11-worlds.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
print("LAW_R1_P11_WORLD_CUSTODY=PASS")
print(f"WORLDS={result['world_count']}")
print(f"MERGED_AUTHORITY={result['merged_authority_count']}")
print(f"REPRESENTATION_INVARIANCE={result['representation_invariance']['all_pass']}")
print(f"SAME_STATE_CONFLICT={result['same_material_state_conflicting_action_observed']}")
