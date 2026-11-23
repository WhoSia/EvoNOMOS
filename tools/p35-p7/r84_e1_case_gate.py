"""E1 metadata screening only; cannot verify human independence."""
from dataclasses import dataclass, replace
from datetime import datetime
import json

EXPOSED = {"https://github.com/go-chi/chi/pull/1045",
           "https://github.com/go-chi/chi/commit/05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723"}

@dataclass(frozen=True)
class Candidate:
    repository: str
    episode_url: str
    base_sha: str
    selector_id: str
    selected_at: str
    evidence_cutoff_at: str
    external_authorship: bool
    outcome_previously_viewed: bool
    research_authored_requirement: bool
    selection_receipt_url: str
    status: str = "CANDIDATE_UNADJUDICATED"

    def validate(self):
        if self.episode_url in EXPOSED or self.outcome_previously_viewed:
            raise ValueError("outcome-exposed example")
        if not self.external_authorship or self.research_authored_requirement:
            raise ValueError("researcher-designed source")
        if self.status != "CANDIDATE_UNADJUDICATED":
            raise ValueError("cannot self-certify as held-out")
        if not self.repository or not self.selector_id.strip():
            raise ValueError("missing provenance")
        if not self.episode_url.startswith("https://github.com/"):
            raise ValueError("missing episode URL")
        if not self.selection_receipt_url.startswith("https://"):
            raise ValueError("no selection audit")
        if len(self.base_sha) != 40 or any(c not in "0123456789abcdef" for c in self.base_sha):
            raise ValueError("invalid blob identifier")
        try:
            a = datetime.fromisoformat(self.selected_at.replace("Z", "+00:00"))
            b = datetime.fromisoformat(self.evidence_cutoff_at.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError("invalid timestamp") from exc
        if a.tzinfo is None or b.tzinfo is None or b > a:
            raise ValueError("temporal evidence boundary invalid")
        return "METADATA_CHECKED_NOT_INDEPENDENTLY_VERIFIED"


def intake(items):
    if not items:
        return {"status":"E1_NOT_EXECUTED", "real_cases":0}
    if len({x.episode_url for x in items}) != len(items):
        raise ValueError("duplicate source case")
    for x in items:
        x.validate()
    return {"status":"METADATA_ONLY_NO_BLIND_GOLD", "independence_verified":False}


def test():
    c=Candidate("example/repo","https://github.com/example/repo/pull/999",
                "a"*40,"independent-example","2026-11-23T12:00:00Z",
                "2026-11-23T10:00:00Z",True,False,False,
                "https://example.org/selection")
    assert c.validate() == "METADATA_CHECKED_NOT_INDEPENDENTLY_VERIFIED"
    mutants=[
        replace(c,episode_url="https://github.com/go-chi/chi/pull/1045"),
        replace(c,outcome_previously_viewed=True),
        replace(c,external_authorship=False),
        replace(c,research_authored_requirement=True),
        replace(c,status="BLINDED_GOLD_ACCEPTED"),
        replace(c,evidence_cutoff_at="2026-11-24T00:00:00Z"),
        replace(c,base_sha="bad"),
        replace(c,selection_receipt_url=""),
    ]
    for item in mutants:
        try: item.validate()
        except ValueError: continue
        raise AssertionError("bad case was accepted")
    try: intake([c,c])
    except ValueError: pass
    else: raise AssertionError("duplicate case accepted")
    assert intake([])["status"] == "E1_NOT_EXECUTED"
    return {"result":"PASS_METADATA_GATES","negative_controls":9,
            "synthetic_positive_only":True,"actual_external_cases":0,
            "human_gold":"NOT_COLLECTED","independence":"NOT_VERIFIED"}

if __name__=="__main__":
    print(json.dumps(test(),sort_keys=True))
