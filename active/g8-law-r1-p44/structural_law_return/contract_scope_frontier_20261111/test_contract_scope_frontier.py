from fractions import Fraction as F
from itertools import product
import unittest
from contract_scope_frontier import Assumptions,NATIVE_BOUNDED_OPTIONS,evaluate

from pareto_proxy import pareto

class SourceAnchoredDecisionTests(unittest.TestCase):
    def test_native_source_pareto_vector_and_hard_contract(self):
        self.assertEqual(pareto(),["constructor","match_lower","route_both"])
        self.assertEqual(pareto(include_direct_risk=False),["constructor","match_lower"])
        self.assertEqual(pareto(keep_direct_as_hard=True),["route_both"])


    def test_native_bounded_option_inclusion(self):
        self.assertEqual(NATIVE_BOUNDED_OPTIONS["route_only"],frozenset({"constructor","route_both","match_lower"}))
        self.assertEqual(NATIVE_BOUNDED_OPTIONS["route_plus_direct"],frozenset({"route_both"}))
        self.assertTrue(NATIVE_BOUNDED_OPTIONS["route_plus_direct"]<=NATIVE_BOUNDED_OPTIONS["route_only"])
    def test_conditional_sign_reversal_is_not_measured_effect(self):
        x=Assumptions(F(1),F(2),F(4),F(1,10),F(2,5))
        o=evaluate(x)
        self.assertEqual(o["signed_shared_minus_local_loss_range"],["-3/5","3/5"])
        self.assertEqual(o["verdict"],"ABSTAIN_SENSITIVE_TO_UNMEASURED_CLIENT_SCOPE")
        self.assertTrue(o["assumed_values_not_measured"])
    def test_hard_contract_excludes_shared_even_when_penalty_looks_small(self):
        x=Assumptions(F(1),F(2),F(4),F(0),F(1,100))
        self.assertEqual(evaluate(x,True)["verdict"],"LOCAL_ONLY_HARD_CLIENT_CONTRACT")
    def test_known_no_protected_client_makes_shared_feasible(self):
        x=Assumptions(F(1),F(2),F(4),F(0),F(0))
        self.assertEqual(evaluate(x,True)["verdict"],"SHARED_ROBUSTLY_LOWER_EXPECTED_LOSS")
    def test_robust_sign_cases(self):
        x=Assumptions(F(1),F(2),F(4),F(3,10),F(2,5))
        self.assertEqual(evaluate(x)["verdict"],"LOCAL_ROBUSTLY_LOWER_EXPECTED_LOSS")
        y=Assumptions(F(1),F(2),F(4),F(0),F(1,5))
        self.assertEqual(evaluate(y)["verdict"],"SHARED_ROBUSTLY_LOWER_EXPECTED_LOSS")
    def test_1200_finite_cost_and_probability_parameter_cases(self):
        cases=0
        for c_s,c_l,h,lo,hi in product(range(4),range(4),range(5),range(5),range(5)):
            if lo>hi:continue
            x=Assumptions(F(c_s),F(c_l),F(h),F(lo,4),F(hi,4))
            o=evaluate(x)
            low,high=map(F,o["signed_shared_minus_local_loss_range"])
            self.assertEqual(low,F(c_s)+F(lo,4)*h-F(c_l))
            self.assertEqual(high,F(c_s)+F(hi,4)*h-F(c_l))
            self.assertLessEqual(low,high)
            if o["verdict"]=="LOCAL_ROBUSTLY_LOWER_EXPECTED_LOSS":self.assertGreater(low,0)
            if o["verdict"]=="SHARED_ROBUSTLY_LOWER_EXPECTED_LOSS":self.assertLess(high,0)
            cases+=1
        self.assertEqual(cases,1200)
    def test_invalid_assumptions_rejected(self):
        with self.assertRaises(ValueError):Assumptions(F(1),F(1),F(1),F(-1),F(0))
        with self.assertRaises(ValueError):Assumptions(F(1),F(1),F(-1),F(0),F(1))

if __name__=="__main__":unittest.main(verbosity=2)
