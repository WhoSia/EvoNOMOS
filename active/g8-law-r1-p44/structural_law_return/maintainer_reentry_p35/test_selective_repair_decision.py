import unittest
from fractions import Fraction
from selective_repair_decision import (
 Counts,Penalties,P35_B0_B1,P35_B2,verdict,loss_original_always_alert,
 loss_never_alert,break_even_false_alert_to_miss_ratio)

class SourceAggregateDecisionAudit(unittest.TestCase):
    def test_exact_report_counts(self):
        self.assertEqual(P35_B0_B1.positives+P35_B0_B1.negatives,47)
        self.assertEqual(P35_B0_B1.top1_hits,9)
        self.assertEqual(P35_B2.top1_hits,8)
        self.assertEqual(P35_B0_B1.false_alerts,34)
    def test_false_alert_price_reverses_p35_ranking(self):
        p=Penalties(Fraction(1),Fraction(1),Fraction(0))
        self.assertEqual(loss_original_always_alert(P35_B0_B1,p),38)
        self.assertEqual(loss_never_alert(P35_B0_B1,p),13)
        self.assertEqual(verdict(p),"ABSTAIN")
    def test_cheap_review_makes_original_alert_rule_preferable(self):
        p=Penalties(Fraction(1,10),Fraction(1),Fraction(1))
        self.assertEqual(loss_original_always_alert(P35_B0_B1,p),Fraction(114,10))
        self.assertEqual(loss_never_alert(P35_B0_B1,p),13)
        self.assertEqual(verdict(p),"ALERT")
    def test_boundaries(self):
        self.assertEqual(break_even_false_alert_to_miss_ratio(P35_B0_B1),Fraction(9,34))
        self.assertEqual(break_even_false_alert_to_miss_ratio(P35_B0_B1,Fraction(1)),Fraction(5,34))
        p=Penalties(Fraction(5,34),Fraction(1),Fraction(1))
        self.assertEqual(verdict(p),"TIE")
    def test_different_classical_rival(self):
        self.assertEqual(break_even_false_alert_to_miss_ratio(P35_B2,Fraction(1)),Fraction(3,34))
    def test_zero_cost_or_wrong_inputs(self):
        self.assertEqual(verdict(Penalties(Fraction(0),Fraction(0),Fraction(0))),"TIE")
        with self.assertRaises(AssertionError):
            Counts(0,1,2,0).validate()

if __name__=="__main__":unittest.main(verbosity=2)
