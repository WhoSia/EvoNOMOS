"""Fail-closed evidence classification; does not simulate actual maintainer action."""
import unittest
from dataclasses import replace
from f38_candidate_gate import Candidate, Gate, HISTORICAL_TRIAGE, classify


class ProspectiveCandidateGateTests(unittest.TestCase):
    def setUp(self):
        self.ready = Candidate(
            external_url="https://github.com/example/other/issues/1",
            source_author_independent=True,
            selected_without_arm_cost_inspection=True,
            edit_locus_app_owned=True,
            declared_old_contract=True,
            equivalent_edit_rights=True,
            forecast_presealed=True,
            original_source_test_executed=False,
            source_verdict_independently_checked=False,
        )

    def test_three_fetched_issues_are_not_f38_results(self):
        for c in HISTORICAL_TRIAGE.values():
            self.assertEqual(classify(c), Gate.SHARED_UPSTREAM_OUT_OF_SCOPE)
            self.assertFalse(c.original_source_test_executed)

    def test_invalid_issue_url_fails_closed(self):
        self.assertEqual(classify(replace(self.ready, external_url="file:///tmp/test")),
                         Gate.INSUFFICIENT_PROVENANCE)

    def test_nonindependent_author_fails_closed(self):
        self.assertEqual(classify(replace(self.ready, source_author_independent=False)),
                         Gate.INSUFFICIENT_PROVENANCE)

    def test_nonblind_app_task_stays_exploratory(self):
        self.assertEqual(classify(replace(self.ready,
                         selected_without_arm_cost_inspection=False)),
                         Gate.NONBLIND_EXPLORATORY)

    def test_unknown_old_contract_blocks_execution_claim(self):
        self.assertEqual(classify(replace(self.ready, declared_old_contract=False)),
                         Gate.CONTRACT_OR_RIGHTS_UNVERIFIED)

    def test_rights_mismatch_blocks_execution_claim(self):
        self.assertEqual(classify(replace(self.ready, equivalent_edit_rights=False)),
                         Gate.CONTRACT_OR_RIGHTS_UNVERIFIED)

    def test_missing_source_forecast_preseal(self):
        self.assertEqual(classify(replace(self.ready, forecast_presealed=False)),
                         Gate.UNSEALED_FORECAST)

    def test_ready_candidate_is_not_an_executed_trial(self):
        self.assertEqual(classify(self.ready), Gate.NOT_EXECUTED)

    def test_successful_execution_needs_independent_adjudication(self):
        self.assertEqual(classify(replace(self.ready,
                         original_source_test_executed=True,
                         source_verdict_independently_checked=True)),
                         Gate.EXECUTED_EVIDENCE_OPEN)

    def test_verified_flag_cannot_replace_execution(self):
        self.assertEqual(classify(replace(self.ready,
                         source_verdict_independently_checked=True)),
                         Gate.NOT_EXECUTED)


if __name__ == "__main__":
    unittest.main()
