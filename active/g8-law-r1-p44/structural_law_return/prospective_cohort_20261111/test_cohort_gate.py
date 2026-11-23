import unittest
import itertools
from dataclasses import replace
from cohort_gate import Evidence, Grade, classify

class GateTests(unittest.TestCase):
    def test_missing_seal(self):
        self.assertEqual(classify(Evidence()), Grade.INVALID)
    def test_historical(self):
        self.assertEqual(classify(Evidence(historical_demand=True)), Grade.HISTORICAL)
    def test_protocol_only(self):
        self.assertEqual(classify(Evidence(prereg_hash="abc", prereg_time=10)), Grade.PROTOCOL)
    def test_bad_chronology(self):
        e=Evidence(prereg_hash="abc", prereg_time=20, reveal_time=10, manifest_hash_before_reveal=True, independent_demand_author=True)
        self.assertEqual(classify(e), Grade.INVALID)
    def test_no_independent_author(self):
        e=Evidence(prereg_hash="abc", prereg_time=10, reveal_time=20, manifest_hash_before_reveal=True)
        self.assertEqual(classify(e), Grade.INVALID)
    def test_reveal(self):
        e=Evidence(prereg_hash="abc", prereg_time=10, reveal_time=20, manifest_hash_before_reveal=True, independent_demand_author=True)
        self.assertEqual(classify(e), Grade.REVEALED)
    def test_execution_is_not_causality(self):
        e=Evidence(prereg_hash="abc", prereg_time=10, reveal_time=20, manifest_hash_before_reveal=True, independent_demand_author=True, matched_source_arms=True, equivalent_permissions=True, protected_old_contracts=True, executed_source_tests=True)
        self.assertEqual(classify(e), Grade.EXECUTED)
        self.assertEqual(classify(replace(e, actor_assignment_predeclared=True, observed_outcomes=True, baseline_same_information=True)), Grade.CAUSAL_CANDIDATE)
    def test_leakage_overrides(self):
        e=Evidence(prereg_hash="abc", prereg_time=10, reveal_time=20, manifest_hash_before_reveal=True, independent_demand_author=True, leakage_or_postselection=True)
        self.assertEqual(classify(e), Grade.INVALID)
    def test_exhaustive_512_critical_flag_combinations(self):
        names=("manifest_hash_before_reveal","independent_demand_author","matched_source_arms","equivalent_permissions","protected_old_contracts","executed_source_tests","actor_assignment_predeclared","observed_outcomes","baseline_same_information")
        for flags in itertools.product((False,True), repeat=len(names)):
            e=Evidence(prereg_hash="abc",prereg_time=10,reveal_time=20,**dict(zip(names,flags)))
            if classify(e)==Grade.CAUSAL_CANDIDATE:
                self.assertTrue(all(flags))

if __name__=="__main__":
    unittest.main()
