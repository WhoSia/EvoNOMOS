"""P38-P0 prospective gate: conservative OFF by default.

This is a *manifest* checker, not an authenticated evidence oracle.
It cannot verify GitHub source claims or prevent hindsight unless an
external reviewer audits the immutable cutoff receipts.
No original Go source is compiled, modified, or tested here.
"""
import argparse
import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

CURRENT = Path(__file__).resolve().parents[2]
M = CURRENT / "tools/p38-p0/preseal-manifest.json"
KINDS = ("yes", "no", "abstain")
BUDGET_KEYS = ("evidence_bytes", "source_parse_nodes", "state_expansions",
               "cpu_milliseconds", "preprocess_milliseconds", "label_annotations")
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def parse_instant(t):
    if not isinstance(t, str):
        raise ValueError("not an ISO 8601 instant")
    dt = datetime.fromisoformat(t.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("naive timestamp")
    return dt.astimezone(timezone.utc)


def validate(data, allow_synthetic=False):
    issues = set()
    if data.get("project") != "EvoNOMOS" or data.get("stage") != "G8-LAW-R1-P38-P0":
        issues.add("BAD_STAGE")
    if data.get("status") != "PREOUTCOME":
        issues.add("NOT_PREOUTCOME")
    if data.get("contains_holdout_labels") is not False:
        issues.add("LABEL_VISIBILITY_UNKNOWN")
    if data.get("candidate_source_status") != "ORIGINAL_PINNED":
        issues.add("UNVERIFIED_SOURCE")
    if data.get("case_type") not in ("LIVE_PROSPECTIVE", "HISTORICAL_OUT_OF_TIME"):
        issues.add("BAD_TIME_SPLIT")
    if data.get("case_type") == "HISTORICAL_OUT_OF_TIME":
        # Temporal backtesting is scientifically valid when sealed, but
        # retrospective observation is not automatically a new prospective test.
        issues.add("NOT_LIVE_PROSPECTIVE")
    if data.get("synthetic") is not False and not allow_synthetic:
        issues.add("SYNTHETIC_NOT_WORLD_CONTACT")

    src = data.get("source") or {}
    if not isinstance(src, dict) or not all(
        HEX40.fullmatch(str(src.get(k, ""))) for k in
        ("upstream_sha", "downstream_sha")
    ):
        issues.add("MISSING_ORIGINAL_SOURCE_SHA")
    if not src.get("natural_dependency_source_anchor"):
        issues.add("MISSING_NATURAL_DEPENDENCY")
    if not src.get("actual_independent_maintainer_evidence"):
        issues.add("MISSING_REAL_OWNER_AUTHORITY")
    if not src.get("allowed_edit_grammar_evidence"):
        issues.add("MISSING_SOURCE_EDIT_GRAMMAR")
    if not src.get("checkpoint_invariant_evidence"):
        issues.add("MISSING_INVARIANT")
    if not src.get("prospective_demand_source_anchor"):
        issues.add("MISSING_FUTURE_DEMAND")
    try:
        cutoff = parse_instant(data["cutoff_at"])
        sealed = parse_instant(data["predictions_sealed_at"])
        if sealed < cutoff:
            issues.add("PREDICTION_BEFORE_SOURCE_CUTOFF")
        for e in src.get("evidence_ledger", []):
            observed = parse_instant(e["observed_at"])
            if observed > cutoff:
                issues.add("POST_CUTOFF_EVIDENCE")
            if not e.get("uri") or not e.get("sha256"):
                issues.add("MISSING_EVIDENCE_RECEIPT")
            elif not HEX64.fullmatch(str(e["sha256"])):
                issues.add("BAD_EVIDENCE_SHA")
        if not src.get("evidence_ledger"):
            issues.add("NO_EVIDENCE_LEDGER")
        outcome = data.get("outcome") or {}
        if outcome.get("visibility") != "UNSEEN" or outcome.get("actual_label") is not None:
            issues.add("OUTCOME_ALREADY_EXPOSED")
        if not outcome.get("oracle_contract"):
            issues.add("NO_OUTCOME_ORACLE")
    except (KeyError, ValueError, TypeError) as exc:
        issues.add("BAD_TEMPORAL_PROVENANCE")

    models = data.get("models") or {}
    if not isinstance(models, dict) or not all(k in models for k in ("H", "B")):
        issues.add("RIVAL_NOT_FROZEN")
    else:
        if models["H"].get("prediction") not in KINDS or models["B"].get("prediction") not in KINDS:
            issues.add("BAD_PREDICTION")
        elif models["H"]["prediction"] == models["B"]["prediction"]:
            issues.add("NO_PROSPECTIVE_DISCORDANCE")
        if models["H"].get("prediction") == "abstain" or models["B"].get("prediction") == "abstain":
            issues.add("ONLY_ABSTENTION_DIFFERENCE")
        for name in ("H", "B"):
            m = models[name]
            if not HEX64.fullmatch(str(m.get("frozen_model_digest", ""))):
                issues.add("NO_FROZEN_MODEL_RECEIPT")
            if not m.get("implementation") or not m.get("feature_construction_contract"):
                issues.add("MODEL_IMPLEMENTATION_UNSPECIFIED")
            if not m.get("semantic_target") or m.get("semantic_target") != data.get("semantic_target"):
                issues.add("UNEQUAL_PREDICTION_TARGET")
            counts = m.get("measured_costs") or {}
            if not all(isinstance(counts.get(k), int) and
                       not isinstance(counts.get(k), bool) and
                       counts[k] >= 0 for k in BUDGET_KEYS):
                issues.add("INCOMPLETE_MODEL_COSTS")
            else:
                limits = data.get("shared_limits") or {}
                if any(not isinstance(limits.get(k), int) or
                       isinstance(limits.get(k), bool) or limits[k] < 0
                       for k in BUDGET_KEYS):
                    issues.add("UNFROZEN_RESOURCE_BUDGETS")
                elif any(counts[k] > limits[k] for k in BUDGET_KEYS):
                    issues.add("BUDGET_VIOLATION")

    rival = data.get("rival_selection") or {}
    if not rival.get("selection_receipt") or not rival.get("prior_validation_cutoff"):
        issues.add("RIVAL_SELECTION_NOT_FROZEN")
    if rival.get("selected_strongest_implementable_rival") not in (
        "B_sem", "B_AG", "B_impact", "B_query", "B_value", "B_composite"
    ):
        issues.add("STRONG_RIVAL_MISSING")
    if not rival.get("same_evidence_access") or not rival.get("same_implementation_budget"):
        issues.add("UNEQUAL_ACCESS")
    # Claiming label-safe selection is self-attestation; reviewer must inspect.
    if not data.get("independent_evidence_audit_receipt"):
        issues.add("INDEPENDENT_AUDIT_MISSING")

    return sorted(issues)


def fixture():
    # Entirely synthetic deliberately non-admissible unit fixture.
    zero40 = "0" * 40
    one64 = "1" * 64
    return {
        "project": "EvoNOMOS", "stage": "G8-LAW-R1-P38-P0",
        "status": "PREOUTCOME", "contains_holdout_labels": False,
        "case_type": "LIVE_PROSPECTIVE", "synthetic": True,
        "candidate_source_status": "ORIGINAL_PINNED",
        "semantic_target": "source_repair_feasibility_under_restricted_grammar",
        "cutoff_at": "2026-01-01T00:00:00Z",
        "predictions_sealed_at": "2026-01-02T00:00:00Z",
        "source": {
            "upstream_sha": zero40, "downstream_sha": zero40,
            "natural_dependency_source_anchor": "EXAMPLE_DO_NOT_USE",
            "actual_independent_maintainer_evidence": "EXAMPLE_DO_NOT_USE",
            "allowed_edit_grammar_evidence": "EXAMPLE_DO_NOT_USE",
            "checkpoint_invariant_evidence": "EXAMPLE_DO_NOT_USE",
            "prospective_demand_source_anchor": "EXAMPLE_DO_NOT_USE",
            "evidence_ledger": [{
                "uri": "example://not-a-repository",
                "observed_at": "2026-01-01T00:00:00Z",
                "sha256": one64,
            }],
        },
        "outcome": {"visibility": "UNSEEN", "actual_label": None,
                    "oracle_contract": "EXAMPLE_ONLY"},
        "shared_limits": {k: 100 for k in BUDGET_KEYS},
        "models": {
            label: {
                "prediction": prediction,
                "frozen_model_digest": one64,
                "implementation": "EXAMPLE_ONLY",
                "feature_construction_contract": "EXAMPLE_ONLY",
                "semantic_target": "source_repair_feasibility_under_restricted_grammar",
                "measured_costs": {k: 1 for k in BUDGET_KEYS}
            } for label, prediction in (("H", "yes"), ("B", "no"))
        },
        "rival_selection": {
            "selection_receipt": "EXAMPLE_ONLY",
            "prior_validation_cutoff": "2026-01-01T00:00:00Z",
            "selected_strongest_implementable_rival": "B_composite",
            "same_evidence_access": True,
            "same_implementation_budget": True,
        },
        "independent_evidence_audit_receipt": "EXAMPLE_ONLY"
    }


def selftest():
    f = fixture()
    assert validate(f) == ["SYNTHETIC_NOT_WORLD_CONTACT"]
    assert validate(f, allow_synthetic=True) == []
    counter = 0

    def force(code, edit):
        nonlocal counter
        x = copy.deepcopy(f)
        edit(x)
        assert code in validate(x), (code, validate(x))
        counter += 1

    force("NO_PROSPECTIVE_DISCORDANCE",
          lambda x: x["models"]["B"].update(prediction="yes"))
    force("BUDGET_VIOLATION",
          lambda x: x["models"]["H"]["measured_costs"].update(cpu_milliseconds=101))
    force("POST_CUTOFF_EVIDENCE",
          lambda x: x["source"]["evidence_ledger"][0].update(
              observed_at="2026-01-01T00:00:01Z"))
    force("OUTCOME_ALREADY_EXPOSED",
          lambda x: x["outcome"].update(visibility="SEEN", actual_label="yes"))
    force("MISSING_REAL_OWNER_AUTHORITY",
          lambda x: x["source"].update(actual_independent_maintainer_evidence=""))
    force("UNEQUAL_ACCESS",
          lambda x: x["rival_selection"].update(same_evidence_access=False))
    force("ONLY_ABSTENTION_DIFFERENCE",
          lambda x: x["models"]["H"].update(prediction="abstain"))
    force("MISSING_ORIGINAL_SOURCE_SHA",
          lambda x: x["source"].update(upstream_sha="unfixed"))
    force("BAD_TEMPORAL_PROVENANCE",
          lambda x: x.update(cutoff_at="unparseable"))
    force("NO_OUTCOME_ORACLE",
          lambda x: x["outcome"].update(oracle_contract=""))
    force("STRONG_RIVAL_MISSING",
          lambda x: x["rival_selection"].update(
              selected_strongest_implementable_rival="static_strawman"))
    force("INCOMPLETE_MODEL_COSTS",
          lambda x: x["models"]["B"]["measured_costs"].pop("preprocess_milliseconds"))
    force("RIVAL_SELECTION_NOT_FROZEN",
          lambda x: x["rival_selection"].update(selection_receipt=""))
    assert counter == 13
    print("P38_P0_MANIFEST_GATE_NEGATIVE_CONTROL_PASS fixtures=13")
    print("P38_P0_SYNTHETIC_CAN_NEVER_ISSUE_NATIVE_AUTHORIZATION_PASS")
    data = json.loads(M.read_text())
    blocked = validate(data)
    assert "UNVERIFIED_SOURCE" in blocked
    assert "NO_PROSPECTIVE_DISCORDANCE" not in blocked or "RIVAL_NOT_FROZEN" in blocked
    assert len(blocked) > 0
    print("P38_P0_CANONICAL_OPEN_MANIFEST_GATE=CLOSED")
    print("P38_P0_CANONICAL_OPEN_MANIFEST_BLOCKERS=" + ",".join(blocked))
    print("P38_P3_EXTERNAL_GO_NATIVE_TRIAL_NOT_AUTHORIZED")
    print("P38_P0_STAGE_OPEN_P1_THEORY_ALLOWED_DIP49_IDENTIFICATION_HOLD")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--manifest", default=str(M))
    args = parser.parse_args()
    if args.selftest:
        selftest()
    else:
        d = json.loads(Path(args.manifest).read_text())
        blockers = validate(d)
        print(json.dumps({
            "status": "CLOSED" if blockers else "STATIC_PRESEAL_REVIEW_REQUIRED",
            "blockers": blockers,
            "warning": "A static pass NEVER proves independent evidence verification or grants native-Go authorization."
        }, indent=2, sort_keys=True))
