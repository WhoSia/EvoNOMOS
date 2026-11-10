"""Adversarial regressions against research eligibility self-inflation."""
import copy
import json
import unittest
from pathlib import Path

from gate import audit, instant

FIXTURE = Path(__file__).with_name("observed_cohort.json")


class EvidenceGateTests(unittest.TestCase):
    def setUp(self):
        self.actual = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_real_archive_is_hold(self):
        result = audit(self.actual)
        self.assertEqual(result["gate"], "LAW_R2_HOLD")
        self.assertEqual(result["observed_issue_count"], 2)
        self.assertEqual(result["eligible_existing_regressions"], 1)
        self.assertEqual(result["real_maintainer_run_count"], 0)
        self.assertIn("INDEPENDENT_MAINTAINER_EXECUTIONS_ABSENT", result["blocking_conditions"])
        self.assertIn("RETROSPECTIVE_OUTCOME_LEAKAGE", result["epistemic_caveats"])

    def test_source_arm_must_precede_issue(self):
        data = copy.deepcopy(self.actual)
        data["architectures"][1]["created_at"] = "2026-11-04T00:00:00Z"
        self.assertIn("ARM_NOT_PRIOR_TO_ISSUE:1247", audit(data)["blocking_conditions"])

    def test_late_contract_not_initial_contract(self):
        data = copy.deepcopy(self.actual)
        data["architectures"][0]["old_contract_fixture"] = ""
        self.assertTrue(any(s.startswith("MISSING_PREEXISTING_CONTRACT")
                            for s in audit(data)["blocking_conditions"]))

    def test_silent_discard_of_issue_is_not_full_cohort(self):
        data = copy.deepcopy(self.actual)
        data["selected_issue_ids"] = [1247]
        self.assertIn("SELECTED_SUBSET_OF_CENSUS_ONLY", audit(data)["epistemic_caveats"])

    def test_new_feature_cannot_be_scored_as_old_api_bug(self):
        data = copy.deepcopy(self.actual)
        data["issues"][0]["scored_repair_comparison"] = True
        self.assertIn("INELIGIBLE_DEMAND_MISCLASSIFIED_AS_REPAIR:1241",
                      audit(data)["blocking_conditions"])

    def test_no_fabricated_agent_results(self):
        data = copy.deepcopy(self.actual)
        data["maintainer_executions"] = [
            {"actor_kind": "research_script", "runner_id": "not-an-agent"},
            {"actor_kind": "research_script", "runner_id": "not-an-agent2"},
        ]
        blockers = audit(data)["blocking_conditions"]
        self.assertIn("SCRIPTED_PATCH_NOT_AN_INDEPENDENT_AGENT", blockers)
        self.assertIn("MISSING_REAL_AGENT_EVIDENCE:actual_patch_sha", blockers)

    def test_missing_unique_architecture_blob(self):
        data = copy.deepcopy(self.actual)
        data["architectures"][0]["source_blob_sha"] = ""
        self.assertIn("MISSING_ARCHITECTURE_SOURCE_BLOB:LIVE",
                      audit(data)["blocking_conditions"])

    def test_duplicated_or_added_issue_rejected(self):
        data = copy.deepcopy(self.actual)
        data["issues"].append(copy.deepcopy(data["issues"][0]))
        self.assertIn("DUPLICATE_ISSUE_ID", audit(data)["blocking_conditions"])
        data = copy.deepcopy(self.actual)
        data["selected_issue_ids"].append(9999)
        self.assertIn("SELECTED_ISSUES_NOT_IN_CENSUS", audit(data)["blocking_conditions"])

    def test_naive_time_rejected(self):
        with self.assertRaises(ValueError):
            instant("2026-10-09T10:00:00")

    def test_no_agent_but_other_gates_true_still_hold(self):
        data = copy.deepcopy(self.actual)
        data["equal_information_budget_verified"] = True
        data["independent_future_prediction"] = True
        data["source_owner_rights_verified"] = True
        self.assertEqual(audit(data)["gate"], "LAW_R2_HOLD")


if __name__ == "__main__":
    unittest.main(verbosity=2)
