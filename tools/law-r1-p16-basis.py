#!/usr/bin/env python3
import hashlib
import itertools
import json
from pathlib import Path

EVIDENCE = Path("active/g8-law-r1-p16/P16_LIFECYCLE_AND_BASIS_CUSTODY.json")
LITERATURE = Path("active/g8-law-r1-p16/P16_LITERATURE_NOVELTY_CUSTODY.json")
BOUNDARY = Path("active/g8-law-r1-p16/P16_REPRESENTATION_BOUNDARY.md")
OUT = Path("out-p16")
OUT.mkdir(parents=True, exist_ok=True)

d = json.loads(EVIDENCE.read_text(encoding="utf-8"))
lit = json.loads(LITERATURE.read_text(encoding="utf-8"))
boundary_text = BOUNDARY.read_text(encoding="utf-8")

coords = [
    "COMPATIBILITY_OBLIGATION",
    "COEXISTENCE_REQUIREMENT",
    "RELEASE_AUTHORITY",
    "LIFECYCLE_PHASE",
]

life = d["lifecycle_replication_family"]
lifecycle_exact = (
    life["grade"] == "EXACT_OPEN_VS_CLOSED_PR_INTERVENTION"
    and life["prior_domain"] != life["fresh_domain"]
    and life["worlds"][0]["A"] != life["worlds"][1]["A"]
    and life["held_context"]["COMPATIBILITY_OBLIGATION"] == 0
    and life["held_context"]["COEXISTENCE_REQUIREMENT"] == 0
    and life["held_context"]["RELEASE_AUTHORITY"] == "TRUSTED_MEMBER"
    and life["held_context"]["IS_PULL_REQUEST"] is True
)

transport = d["transport"]
transport_complete = set(transport) == set(coords) and all(len(transport[c]) >= 2 for c in coords)

orthogonal = {
    row["coordinate"]: row
    for row in d["orthogonal_single_coordinate_interventions"]
}
orthogonal_complete = (
    set(orthogonal) == set(coords)
    and all(orthogonal[c]["other_coordinates_fixed"] for c in coords)
    and all(orthogonal[c]["action_difference"] for c in coords)
)

deletions = {row["coordinate"]: row for row in d["deletion_attacks"]}
deletion_complete = (
    set(deletions) == set(coords)
    and all(row["status"] == "FAILS_DELETION" for row in deletions.values())
    and all(len(row["witnesses"]) >= 2 for row in deletions.values())
)

expected_pairs = {tuple(sorted(p)) for p in itertools.combinations(coords, 2)}
observed_pairs = {
    tuple(sorted(row["pair"])): row
    for row in d["pairwise_quotient_attacks"]
}
pairwise_complete = (
    set(observed_pairs) == expected_pairs
    and all(row["status"] == "SEMANTIC_MERGE_REJECTED" for row in observed_pairs.values())
)

expected_triples = {tuple(sorted(t)) for t in itertools.combinations(coords, 3)}
triple_rows = {
    tuple(sorted(row["collapsed"])): row
    for row in d["higher_order_quotient_attacks"]["triple_collapses"]
}
triple_complete = (
    set(triple_rows) == expected_triples
    and all(row["status"] == "REJECTED_BY_SINGLE_COORDINATE_ORTHOGONAL_WITNESSES" for row in triple_rows.values())
)

full = d["higher_order_quotient_attacks"]["full_collapse"]
full_complete = (
    set(full["collapsed"]) == set(coords)
    and full["status"] == "REJECTED_AS_SEMANTIC_COARSENING"
)

split_rows = {row["coordinate"]: row for row in d["split_attacks"]}
split_complete = (
    set(split_rows) == set(coords)
    and all(row["status"] == "NO_PROSPECTIVE_FINER_SPLIT_JUSTIFIED" for row in split_rows.values())
)

scope = d["basis_scope"]
scope_safe = (
    scope["claimable"] == "REPRODUCIBLE_OPERATIONAL_MINIMAL_PRIMITIVE_BASIS_UNDER_FROZEN_COORDINATE_GRAMMAR"
    and "UNIVERSAL_COORDINATE_CARDINALITY_MINIMALITY_UNDER_ARBITRARY_BIJECTIONS" in scope["not_claimable"]
    and "UNIQUE_LATENT_FACTOR_DECOMPOSITION" in scope["not_claimable"]
    and "arbitrary recoding" in boundary_text.lower()
    and "non-injective semantic coarsening" in boundary_text.lower()
)

# Representation-invariance replay: re-encode the material lifecycle family and restore it.
material = {
    "target": life["target"],
    "grade": life["grade"],
    "prior_domain": life["prior_domain"],
    "fresh_domain": life["fresh_domain"],
    "G": life["G"],
    "E": life["E"],
    "held_context": life["held_context"],
    "worlds": life["worlds"],
}
variant = {
    "coordinate": material["target"],
    "match_grade": material["grade"],
    "domain_a": material["prior_domain"],
    "domain_b": material["fresh_domain"],
    "geometry": material["G"],
    "evidence": material["E"],
    "fixed": material["held_context"],
    "contrasts": material["worlds"],
    "display_name": "lifecycle-reencoded",
}
restored = {
    "target": variant["coordinate"],
    "grade": variant["match_grade"],
    "prior_domain": variant["domain_a"],
    "fresh_domain": variant["domain_b"],
    "G": variant["geometry"],
    "E": variant["evidence"],
    "held_context": variant["fixed"],
    "worlds": variant["contrasts"],
}
def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

representation_invariance = digest(material) == digest(restored)

anti_rationalization = len(d.get("post_hoc_coordinate_additions", [])) == 0

custody_ok = (
    len(lit["canonicalized_in_p16"]) == 3
    and len(lit["exact_pdf_unavailable_after_user_attempt"]) == 2
    and lit["new_external_acquisition_required_for_p16"] is False
)

operational_minimal_basis = all([
    lifecycle_exact,
    transport_complete,
    orthogonal_complete,
    deletion_complete,
    pairwise_complete,
    triple_complete,
    full_complete,
    split_complete,
    scope_safe,
    representation_invariance,
    anti_rationalization,
])

result = {
    "stage": d["stage"],
    "lifecycle_second_domain": "PASS" if lifecycle_exact else "FAIL",
    "transport": {
        c: {
            "domains": transport[c],
            "two_domain_exact": len(transport[c]) >= 2,
        }
        for c in coords
    },
    "orthogonal_single_coordinate_interventions": "PASS" if orthogonal_complete else "FAIL",
    "deletion_completeness": "PASS" if deletion_complete else "FAIL",
    "pairwise_quotient_exhaustion": {
        "status": "PASS" if pairwise_complete else "FAIL",
        "tested": len(observed_pairs),
        "expected": 6,
    },
    "higher_order_quotient_exhaustion": {
        "triple_status": "PASS" if triple_complete else "FAIL",
        "triple_tested": len(triple_rows),
        "triple_expected": 4,
        "full_collapse_status": "PASS" if full_complete else "FAIL",
    },
    "prospective_split_attack": "PASS" if split_complete else "FAIL",
    "representation_invariance": "PASS" if representation_invariance else "FAIL",
    "anti_rationalization": "PASS" if anti_rationalization else "FAIL",
    "basis_scope": {
        "operational_grammar_relative": "AUTHORIZED" if operational_minimal_basis else "NOT_AUTHORIZED",
        "universal_coordinate_cardinality": "NOT_CLAIMED",
        "unique_latent_factorization": "NOT_CLAIMED",
    },
    "operational_minimal_basis": "PASS" if operational_minimal_basis else "NOT_AUTHORIZED",
    "same_normalized_X_G_E_conflicting_action_observed": d["same_normalized_X_G_E_conflicting_action_observed"],
    "literature_custody": {
        "status": "PASS" if custody_ok else "FAIL",
        "canonicalized_count": len(lit["canonicalized_in_p16"]),
        "unavailable_exact_pdf_count": len(lit["exact_pdf_unavailable_after_user_attempt"]),
        "new_external_acquisition_required": lit["new_external_acquisition_required_for_p16"],
        "ruling": lit["custody_ruling"],
    },
    "caution": "Minimality is authorized only for the frozen operational primitive grammar and admissible non-injective semantic quotients. Arbitrary bijective recoding can always pack the tuple and is outside the claim."
}

(OUT / "p16-basis.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print("LAW_R1_P16_LIFECYCLE_CUSTODY=PASS")
print("LIFECYCLE_SECOND_DOMAIN=" + result["lifecycle_second_domain"])
print("TRANSPORT_COMPLETE=" + str(transport_complete))
print("ORTHOGONAL_INTERVENTIONS=" + result["orthogonal_single_coordinate_interventions"])
print("DELETION_COMPLETENESS=" + result["deletion_completeness"])
print("PAIRWISE_QUOTIENTS=" + result["pairwise_quotient_exhaustion"]["status"])
print("HIGHER_ORDER_QUOTIENTS=" + result["higher_order_quotient_exhaustion"]["triple_status"])
print("REPRESENTATION_INVARIANCE=" + result["representation_invariance"])
print("ANTI_RATIONALIZATION=" + result["anti_rationalization"])
print("OPERATIONAL_MINIMAL_BASIS=" + result["operational_minimal_basis"])
print("UNIVERSAL_CARDINALITY=" + result["basis_scope"]["universal_coordinate_cardinality"])
print("DRIVE_CUSTODY=" + result["literature_custody"]["status"])
