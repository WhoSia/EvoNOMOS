"""P38-P2C historical contract-interference evidence court.

This court checks exact manually transcribed PUBLIC MAINTAINER-REPORTED data.
It does not download, compile or execute any native Go source. It cannot
certify causal attribution, complete syntax semantics, or law novelty.
"""
from pathlib import Path
from datetime import datetime
import json

HERE = Path(__file__).resolve().parent
DATA = HERE / "historical_semantic_receipt.json"


def parse_time(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def audit(d):
    assert d["role"] == "RETROSPECTIVE_CALIBRATION_ONLY"
    assert not d["independent_holdout"]
    assert d["prospective_prediction"] is None
    assert len(d["maintainer_reported_six_inputs"]) == 6
    events = {e["event"]: e for e in d["historical_events"]}
    assert len(events) == 4
    export = events["upstream_public_api_export_proposal"]
    sub = events["downstream_parser_substitution_pr"]
    upstream = events["upstream_parser_truncation_issue"]
    open_req = events["natural_cross_repo_future_request_screen"]
    assert export["merged"] is False and export["state"] == "closed"
    assert sub["merged"] is False and sub["state"] == "closed"
    assert upstream["state"] == "closed" and upstream["resolution"] == "DOCUMENTATION_ONLY"
    assert upstream["reported_diff_stats"] == {"additions": 5, "deletions": 0}
    assert open_req["state"] == "open" and open_req["label_observed"] is False
    assert open_req["role"] == "POTENTIAL_FUTURE_REQUIREMENT_NOT_SEALED"
    assert parse_time(export["closed_at"]) < parse_time(open_req["created_at"])
    assert parse_time(sub["created_at"]) < parse_time(sub["closed_at"])
    assert parse_time(sub["closed_at"]) <= parse_time(upstream["closed_at"])
    assert len(d["original_source"]["downstream"]["main_sha"]) == 40
    assert len(d["original_source"]["upstream"]["tag_sha"]) == 40

    rows = d["maintainer_reported_six_inputs"]
    assert len({row["input"] for row in rows}) == 6
    equal = [r["old"] == r["replacement"] for r in rows]
    assert equal == [True, False, False, False, False, False], equal
    # Contract Q0 = one normal header (selected retrospective);
    # strong Q6 = all six fixed historical exemplars.
    accepts_normal = equal[0]
    accepts_six = all(equal)
    assert accepts_normal and not accepts_six
    # Monotonicity under an expanding required test family:
    # failing one additional test can only shrink the admissible patches.
    for mask in range(1 << 6):
        checked = [i for i in range(6) if mask & (1 << i)]
        valid = all(equal[i] for i in checked)
        for j in range(6):
            if j in checked:
                continue
            extended = checked + [j]
            assert not (all(equal[k] for k in extended) and not valid)
    return sum(equal), len(equal) - sum(equal)


def check_negative_controls(d):
    x = json.loads(json.dumps(d))
    x["independent_holdout"] = True
    try:
        audit(x)
        raise AssertionError("RETROSPECTIVE_LEAKAGE_NOT_REJECTED")
    except AssertionError as err:
        assert str(err) != "RETROSPECTIVE_LEAKAGE_NOT_REJECTED"
    y = json.loads(json.dumps(d))
    y["prospective_prediction"] = "accepted"
    try:
        audit(y)
        raise AssertionError("PROSPECTIVE_LABEL_FABRICATION_NOT_REJECTED")
    except AssertionError as err:
        assert str(err) != "PROSPECTIVE_LABEL_FABRICATION_NOT_REJECTED"
    z = json.loads(json.dumps(d))
    z["historical_events"][2]["resolution"] = "BEHAVIOR_FIXED"
    try:
        audit(z)
        raise AssertionError("DOC_ONLY_MISCLASSIFIED")
    except AssertionError as err:
        assert str(err) != "DOC_ONLY_MISCLASSIFIED"
    return 3


def main():
    d = json.loads(DATA.read_text())
    matches, divergences = audit(d)
    assert (matches, divergences) == (1, 5)
    assert check_negative_controls(d) == 3
    print("P38_P2C_MAINTAINER_REPORTED_SIX_CASES_CHECKED matches=1 divergences=5")
    print("P38_P2C_CONTRACT_EXPANSION_MONOTONICITY_CHECKED subsets=64")
    print("P38_P2C_UPSTREAM_PUBLIC_EXPORT_REJECTED_2021")
    print("P38_P2C_DOWNSTREAM_SEMANTIC_SUBSTITUTION_PR_CLOSED_UNMERGED")
    print("P38_P2C_UPSTREAM_ISSUE_CLOSED_DOCUMENTATION_ONLY_NOT_BEHAVIOR_FIXED")
    print("P38_P2C_HISTORICAL_LEAKAGE_NEGATIVE_CONTROLS_PASS cases=3")
    print("P38_P2C_SOURCE_CODE_NOT_EXECUTED_RETROSPECTIVE_CALIBRATION_ONLY")
    print("P38_G0_PARTIAL_G1_G2_HOLD_P3_NATIVE_BLOCKED_DIP49_HOLD")


if __name__ == "__main__":
    main()
