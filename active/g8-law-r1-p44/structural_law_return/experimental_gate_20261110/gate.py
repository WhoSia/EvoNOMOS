"""Audit real prospective source-architecture experiment eligibility.

This does NOT execute independent coding agents, infer causal treatment effects,
or verify that public issue search was globally exhaustive. A positive evidence
gate requires real external execution records rather than invented placeholders.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import argparse
import json


def instant(value: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError("missing timestamp")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamps must be timezone-aware")
    return parsed.astimezone(timezone.utc)


def audit(data: dict[str, Any]) -> dict[str, Any]:
    violations: list[str] = []
    observations: list[str] = []
    arms = data.get("architectures", [])
    issues = data.get("issues", [])
    observations.append("PUBLIC_ISSUE_SEARCH_NOT_A_CERTIFIED_GLOBAL_CENSUS")
    if len(arms) < 2:
        violations.append("NEED_TWO_ARCHITECTURE_TREATMENTS")
    if len({a.get("name") for a in arms}) != len(arms):
        violations.append("DUPLICATE_ARCHITECTURE_NAME")
    approved_initial_fixtures = {
        "tools/p35-p7/tests/p35_p7_common_test.go",
        "tools/p35-p7/tests/p35_p7_modes_test.go",
    }
    for arm in arms:
        if not arm.get("source_commit") or len(arm.get("source_commit", "")) != 40:
            violations.append("MISSING_OR_INVALID_ARM_SHA:" + str(arm.get("name")))
        if not arm.get("source_blob_sha") or len(arm.get("source_blob_sha", "")) != 40:
            violations.append("MISSING_ARCHITECTURE_SOURCE_BLOB:" + str(arm.get("name")))
        if not arm.get("source_file_path"):
            violations.append("MISSING_ARCHITECTURE_FILE_PATH:" + str(arm.get("name")))
        if not arm.get("old_contract_fixture"):
            violations.append("MISSING_PREEXISTING_CONTRACT:" + str(arm.get("name")))
        all_initial = [arm.get("old_contract_fixture")] + arm.get("other_initial_fixtures", [])
        if any(p not in approved_initial_fixtures for p in all_initial):
            violations.append("LATER_CONTRACT_CONTAMINATES_BASELINE:" + str(arm.get("name")))
    if not issues:
        violations.append("EMPTY_ISSUE_DENOMINATOR")
    if len({i.get("id") for i in issues}) != len(issues):
        violations.append("DUPLICATE_ISSUE_ID")
    seen = {i.get("id") for i in issues}
    selected = set(data.get("selected_issue_ids", []))
    if not selected.issubset(seen):
        violations.append("SELECTED_ISSUES_NOT_IN_CENSUS")
    for issue in issues:
        try:
            issued = instant(issue["created_at"])
            for arm in arms:
                if instant(arm["created_at"]) >= issued:
                    violations.append("ARM_NOT_PRIOR_TO_ISSUE:" + str(issue.get("id")))
        except (KeyError, ValueError, TypeError):
            violations.append("INVALID_CHRONOLOGY:" + str(issue.get("id")))
        if issue.get("category") not in {
            "existing_behavior_regression", "opt_in_new_feature",
            "documentation_or_support", "other",
        }:
            violations.append("UNDEFINED_DEMAND_CATEGORY:" + str(issue.get("id")))
        if issue.get("category") != "existing_behavior_regression" and issue.get("scored_repair_comparison"):
            violations.append("INELIGIBLE_DEMAND_MISCLASSIFIED_AS_REPAIR:" + str(issue.get("id")))
    if len(selected) != len(issues):
        observations.append("SELECTED_SUBSET_OF_CENSUS_ONLY")
    if data.get("outcomes_known_before_cohort_freeze", True):
        observations.append("RETROSPECTIVE_OUTCOME_LEAKAGE")
    if data.get("postfirst_run_protocol_amendment", False):
        observations.append("PROTOCOL_AMENDED_AFTER_FIRST_OUTCOME")
    agents = data.get("maintainer_executions", [])
    if len(agents) < 2:
        violations.append("INDEPENDENT_MAINTAINER_EXECUTIONS_ABSENT")
    for run in agents:
        mandatory = ("runner_id", "actor_id", "architecture",
                     "task_id", "source_commit", "policy",
                     "actual_patch_sha", "old_new_contract_result",
                     "tool_budget", "attempt_log_url")
        for field in mandatory:
            if not run.get(field):
                violations.append("MISSING_REAL_AGENT_EVIDENCE:" + field)
        if run.get("actor_kind") == "research_script":
            violations.append("SCRIPTED_PATCH_NOT_AN_INDEPENDENT_AGENT")
    if not data.get("equal_information_budget_verified", False):
        violations.append("EQUAL_INFORMATION_BUDGET_NOT_VERIFIED")
    if not data.get("independent_future_prediction", False):
        violations.append("PROSPECTIVE_FORECAST_NOT_VERIFIED")
    if not data.get("source_owner_rights_verified", False):
        violations.append("OWNER_RIGHTS_NOT_VERIFIED")
    return {
        "gate": "LAW_R2_HOLD" if violations else "READY_FOR_HUMAN_SCIENTIFIC_REVIEW",
        "checked_architecture_count": len(arms),
        "observed_issue_count": len(issues),
        "eligible_existing_regressions": sum(
            i.get("category") == "existing_behavior_regression" for i in issues
        ),
        "real_maintainer_run_count": len(agents),
        "blocking_conditions": sorted(set(violations)),
        "epistemic_caveats": sorted(set(observations)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = audit(data)
    encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    print(encoded, end="")
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")


if __name__ == "__main__":
    main()
