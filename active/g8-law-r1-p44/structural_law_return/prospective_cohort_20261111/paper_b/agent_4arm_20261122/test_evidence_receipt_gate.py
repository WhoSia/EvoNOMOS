import copy
import unittest
from evidence_receipt_gate import ARMS, errors_for_receipt, manuscript_metrics, study_errors

def receipt(arm="NONE",invocation="fixture-1"):
    return {
        "trial_id":"synthetic-test-only", "study_kind":"synthetic_test",
        "task_id":"illustrative-unassigned", "model_id":"no-model",
        "source_commit":"a"*40, "task_spec_sha256":"b"*64,
        "tool_budget_id":"no-execution", "arm":arm,
        "invocation_id":invocation, "fresh_context":True,
        "run_status":"abstained", "code_patch_sha256":None,
        "patch_files":[], "explanation":"No actual agent was invoked. SOLID.",
        "go_results":{"baseline_pass":None,"new_requirement_pass":None,"race_pass":None},
        "contract_review":{"verdict":"UNRESOLVED","reviewer_id":"synthetic-placeholder","evidence_refs":[]},
    }

class EvidenceReceiptGate(unittest.TestCase):
    def test_one_synthetic_record(self):
        self.assertEqual(errors_for_receipt(receipt()),[])

    def test_four_arm_fixture_never_empirical(self):
        rows=[receipt(arm,f"fake-{i}") for i,arm in enumerate(ARMS)]
        m=manuscript_metrics(rows)
        self.assertEqual(m["observed_agent_invocations"],0)
        self.assertEqual(m["synthetic_receipts_excluded"],4)
        self.assertEqual(m["principle_mentions_in_observed_explanations"],0)
        self.assertEqual(m["agent_effect_estimate"],"NOT_IDENTIFIED")

    def test_missing_critical_requirement(self):
        x=receipt()
        del x["task_spec_sha256"]
        self.assertIn("missing:task_spec_sha256",errors_for_receipt(x))

    def test_wrong_patch_digest(self):
        x=receipt();x["code_patch_sha256"]="invalid"
        self.assertIn("code_patch_sha256",errors_for_receipt(x))

    def test_fake_complete_without_patch(self):
        x=receipt();x["run_status"]="completed"
        self.assertIn("completed_missing_patch",errors_for_receipt(x))

    def test_bad_evidence_for_decisive_review(self):
        x=receipt();x["contract_review"]["verdict"]="ADMISSIBLE"
        self.assertIn("decisive_review_without_evidence",errors_for_receipt(x))

    def test_same_invocation_in_two_arms_is_contamination(self):
        self.assertIn("record_1:reused_invocation_id",
                      study_errors([receipt("NONE","same"),receipt("HARD_SOLID","same")]))

    def test_different_task_specs_across_arms_is_confounded(self):
        a=receipt("NONE","one")
        z=receipt("HARD_SOLID","two")
        z["task_spec_sha256"]="c"*64
        self.assertIn("record_1:treatment_information_confounded",study_errors([a,z]))

    def test_different_tool_budgets_across_arms_is_confounded(self):
        a=receipt("NONE","one")
        z=receipt("SCOPED_SOLID","two")
        z["tool_budget_id"]="better_tools"
        self.assertIn("record_1:treatment_information_confounded",study_errors([a,z]))

    def test_json_boolean_zero_is_not_valid_go_result(self):
        x=receipt();x["go_results"]["baseline_pass"]=0
        self.assertIn("go_results_type",errors_for_receipt(x))

    def test_synthetic_invalid_record_never_aggregates(self):
        x=receipt();x["fresh_context"]=False
        with self.assertRaises(ValueError):
            manuscript_metrics([x])

    def test_an_observed_record_not_claimed_as_randomized_effect(self):
        x=receipt()
        x["study_kind"]="observed"
        x["run_status"]="completed"
        x["code_patch_sha256"]="c"*64
        x["patch_files"]=["handler.go"]
        x["go_results"]["baseline_pass"]=True
        result=manuscript_metrics([x])
        self.assertEqual(result["observed_agent_invocations"],1)
        self.assertEqual(result["agent_effect_estimate"],"NOT_IDENTIFIED")

if __name__=="__main__":
    unittest.main()
