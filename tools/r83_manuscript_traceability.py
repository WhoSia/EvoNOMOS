"""R83 paper evidence consistency check, not a novelty or publication gate.

Verify that a narrow manuscript cites the official upstream Git blobs
separately from team variants and explicitly limits its empirical claims.
Requires checkout of WhoSia/EvoNOMOS main.
"""
from pathlib import Path
import argparse
import json

HASHES = {
    "official_old": "997bed569ad89aec1f30765bfc6e868a7f232b6d",
    "official_fixed": "1c3334d35fc2b592f1ff01c03213e4779ddde338",
    "team_live": "ad9a2fbc0a30a39475f746068e74e2d3e6c93999",
    "team_snapshot": "e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75",
    "team_d8_live": "e481e73aa1d82497c25011b6468d7e8749c705f7",
    "team_d8_snapshot": "66e88964508cedc38740913a7c00fbf5b6e6220a",
}
PRIMARY_LINKS = (
    "https://github.com/go-chi/chi/blob/v5.1.0/middleware/route_headers.go",
    "https://github.com/go-chi/chi/commit/05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723",
    "https://github.com/go-chi/chi/blob/v5.2.5/middleware/route_headers.go",
    "https://doi.org/10.1145/2491509.2491515",
)
MANDATORY_SCOPE = (
    "팀 파생", "업스트림", "독립", "미수행", "ATLAS", "강한 ADR",
    "외부", "기록 비용", "일반화", "D8", "음성 결과",
)


def check(text: str) -> dict:
    missing_hashes = [label for label, blob in HASHES.items() if blob not in text]
    missing_links = [u for u in PRIMARY_LINKS if u not in text]
    missing_scope = [phrase for phrase in MANDATORY_SCOPE if phrase not in text]
    if missing_hashes or missing_links or missing_scope:
        raise ValueError({"hashes": missing_hashes,
                          "urls": missing_links, "qualifiers": missing_scope})
    if HASHES["official_old"] in (HASHES["team_live"], HASHES["team_snapshot"]):
        raise AssertionError("upstream and team variants collapsed")
    return {
        "source_checks": len(HASHES),
        "primary_links": len(PRIMARY_LINKS),
        "scope_qualifiers": len(MANDATORY_SCOPE),
        "scientific_validity_tested": False,
        "external_human_review": False,
        "result": "PASS_MANUSCRIPT_TRACEABILITY_ONLY",
    }


def test(text: str) -> dict:
    state = check(text)
    negative = [
        text.replace(HASHES["official_old"], "UNVERIFIED"),
        text.replace(PRIMARY_LINKS[1], "MISSING_EXTERNAL_COMMIT"),
        text.replace("미수행", "NOT_PERFORMED_PLACEHOLDER"),
    ]
    for candidate in negative:
        try:
            check(candidate)
        except ValueError:
            pass
        else:
            raise AssertionError("provenance mutation passed")
    return state | {"negative_controls": len(negative)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / "papers/R83_contract_provenance_reproducibility_draft_ko.md")
    args = parser.parse_args()
    print(json.dumps(test(args.paper.read_text(encoding="utf-8")),
                     ensure_ascii=False, sort_keys=True))
