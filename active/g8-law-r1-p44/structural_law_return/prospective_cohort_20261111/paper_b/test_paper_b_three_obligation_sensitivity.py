import unittest
from paper_b_three_obligation_sensitivity import (
  compatible, verdict, statistics, all_disclosures, countermodels,
  project_original_two_facts,
)

class ThreeObligationSensitivity(unittest.TestCase):
    def test_exact_twenty_seven_disclosures(self):
        self.assertEqual(len(all_disclosures()),27)
        self.assertEqual(statistics(),{"ACCEPT":1,"REJECT":19,"HOLD":7})

    def test_eight_possible_complete_worlds(self):
        self.assertEqual(len(compatible((None,None,None))),8)

    def test_absent_all_obligations_accepted(self):
        self.assertEqual(verdict((False,False,False)),"ACCEPT")

    def test_any_positive_obligation_rejects(self):
        for index in range(3):
            v=[None]*3
            v[index]=True
            self.assertEqual(verdict(tuple(v)),"REJECT")

    def test_seven_hold_states_have_opposing_countermodels(self):
        seen=0
        for evidence in all_disclosures():
            pair=countermodels(evidence)
            if verdict(evidence)=="HOLD":
                seen+=1
                self.assertIsNotNone(pair)
                self.assertIn(pair[0],compatible(evidence))
                self.assertIn(pair[1],compatible(evidence))
                self.assertNotEqual(pair[0],pair[1])
            else:
                self.assertIsNone(pair)
        self.assertEqual(seen,7)

    def test_unknown_new_fact_blocks_previous_approval(self):
        self.assertEqual(verdict((False,False,None)),"HOLD")
        self.assertEqual(verdict((False,False,False)),"ACCEPT")
        self.assertEqual(verdict((False,False,True)),"REJECT")

    def test_original_2_factor_recovered_when_third_false(self):
        grid=project_original_two_facts()
        self.assertEqual(len(grid),9)
        counts={v:sum(x[2]==v for x in grid) for v in ("ACCEPT","REJECT","HOLD")}
        self.assertEqual(counts,{"ACCEPT":1,"REJECT":5,"HOLD":3})

    def test_invalid_evidence_fail_closed(self):
        for bad in ((None,None),("unknown",False,None),(0,False,None)):
            with self.assertRaises(ValueError):
                compatible(bad)

if __name__=="__main__":
    unittest.main()
