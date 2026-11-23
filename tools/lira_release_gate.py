"""R76 manuscript release policy: explicit, non-compensatory evidence gates.

The model is deliberately NOT a scoring system for paper quality. All claims
in this gate are author-declared; external-review and empirical-test fields can
be set true only after independently recorded evidence is supplied.
Run: python tools/lira_release_gate.py
"""
from dataclasses import dataclass, replace
from typing import Mapping
import json


REQUIRED = (
    "primary_source_audit",
    "reference_completeness",
    "complete_bilingual_manuscript",
    "semantic_alignment_review",
    "independent_truth_adjudication",
    "source_native_reproduction",
    "fair_strong_baseline",
    "human_review_accuracy",
    "human_work_cost",
    "external_review_clearance",
)


@dataclass(frozen=True)
class EvidenceGate:
    passed: bool
    source_id: str | None

    def __post_init__(self):
        if self.passed and (not self.source_id or not self.source_id.strip()):
            raise ValueError("passing a gate requires an evidence ID")
        if not self.passed and self.source_id is not None:
            raise ValueError("failed/pending gate must not imply supportive evidence")


def audit_release(evidence: Mapping[str, EvidenceGate]) -> dict:
    if set(evidence) != set(REQUIRED):
        raise ValueError("wrong number or names of manuscript gates")
    if any(not isinstance(value, EvidenceGate) for value in evidence.values()):
        raise ValueError("untyped evidence record")
    missing = sorted(key for key, rec in evidence.items() if not rec.passed)
    return {
        "release": "HOLD" if missing else "ELIGIBLE_FOR_INDEPENDENT_REVIEW_NOT_ACCEPTED",
        "reasons": missing,
        "number_pending": len(missing),
        "noncompensatory": True,
        "reviewer_acceptance": "NOT_INFERRED",
    }


# Evidence from real user-visible artifacts and test records is still subject to
# verification. The following does NOT claim either source originality or
# independent referee approval.
V50_WORKING = {
    "primary_source_audit": EvidenceGate(False, None),
    "reference_completeness": EvidenceGate(False, None),
    "complete_bilingual_manuscript": EvidenceGate(False, None),
    "semantic_alignment_review": EvidenceGate(False, None),
    "independent_truth_adjudication": EvidenceGate(False, None),
    "source_native_reproduction": EvidenceGate(False, None),
    "fair_strong_baseline": EvidenceGate(False, None),
    "human_review_accuracy": EvidenceGate(False, None),
    "human_work_cost": EvidenceGate(False, None),
    "external_review_clearance": EvidenceGate(False, None),
}


def test():
    status = audit_release(V50_WORKING)
    assert status["release"] == "HOLD" and status["number_pending"] == 10
    assert status["noncompensatory"] is True
    for name in REQUIRED:
        assert name in status["reasons"]
    # An average over high-scoring prose cannot override the release veto.
    almost = dict(V50_WORKING)
    for name in REQUIRED:
        almost[name] = EvidenceGate(True, "synthetic-evidence-" + name)
    almost["external_review_clearance"] = EvidenceGate(False, None)
    assert audit_release(almost)["release"] == "HOLD"
    assert audit_release({key: EvidenceGate(True, key) for key in REQUIRED})["release"] == (
        "ELIGIBLE_FOR_INDEPENDENT_REVIEW_NOT_ACCEPTED"
    )
    # Fail closed, including wrongly setting a gate with no source.
    for bad in (
        lambda: EvidenceGate(True, None),
        lambda: EvidenceGate(False, "some-evidence"),
        lambda: audit_release({}),
        lambda: audit_release({**V50_WORKING, "paper_score": EvidenceGate(True, "self")}),
        lambda: audit_release({**V50_WORKING, "fair_strong_baseline": True}),
    ):
        try:
            bad()
        except ValueError:
            continue
        raise AssertionError("malformed gate passed validation")
    return {
        "status": status,
        "negative_controls": 5,
        "all_green_synthetic_only": "NOT_AN_ACCEPTANCE_CLAIM",
        "result": "PASS_MANUSCRIPT_GATES",
    }


if __name__ == "__main__":
    print(json.dumps(test(), ensure_ascii=False, sort_keys=True))
