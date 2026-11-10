from fractions import Fraction as F
from itertools import product
import unittest
from decision_conflict import (
    certificate, exact_regret, optimize_signals, restic_worlds,
    triple_conflict_worlds, argmin, validate,
)

class DecisionBoundaryTests(unittest.TestCase):
    def test_restic_avoidable_decision_loss(self):
        c=certificate(restic_worlds())
        self.assertEqual(c["exact"],"27/100")
        self.assertEqual(c["hypergraph_lower_bound"],"27/100")
        self.assertEqual(c["minimal_conflicts"],[[["prepaid","metered"]]])

    def test_context_revealed_removes_gap(self):
        rows=[dict(r,signal=r["id"]) for r in restic_worlds()]
        self.assertEqual(exact_regret(rows),F())

    def test_three_way_conflict_no_pairwise_conflict(self):
        rows=triple_conflict_worlds()
        for i in range(3):
            for j in range(i+1,3):
                self.assertTrue(argmin(rows[i]) & argmin(rows[j]))
        c=certificate(rows)
        self.assertEqual(c["minimal_conflicts"],[[["a","b","c"]]])
        self.assertEqual(c["exact"],"1/3")
        self.assertEqual(c["hypergraph_lower_bound"],"1/3")

    def test_exhaustively_sound_two_by_two_and_three_by_three(self):
        for n,k,r in [(2,2,3),(3,3,2)]:
            for values in product(range(r),repeat=n*k):
                rows=[{"id":str(i),"signal":"same","losses":values[i*k:(i+1)*k],"p":F(1,n)}
                      for i in range(n)]
                c=certificate(rows)
                self.assertLessEqual(F(c["hypergraph_lower_bound"]),F(c["exact"]))

    def test_costed_information_changes_optimal_interface(self):
        rows=restic_worlds()
        features={"contract":{"prepaid":"prepaid","metered":"metered"}}
        self.assertEqual(optimize_signals(rows,features,{"contract":"0.10"})["features"],["contract"])
        self.assertEqual(optimize_signals(rows,features,{"contract":"0.10"})["total"],"1/10")
        self.assertEqual(optimize_signals(rows,features,{"contract":"0.40"})["features"],[])
        self.assertEqual(optimize_signals(rows,features,{"contract":"0.40"})["total"],"27/100")

    def test_actual_authorized_observation_boundary(self):
        rows=restic_worlds()
        features={"contract":{"prepaid":"p","metered":"m"}}
        result=optimize_signals(rows,features,{"contract":"0.01"},authorized=[])
        self.assertEqual(result["features"],[])
        self.assertEqual(result["regret"],"27/100")

    def test_information_interaction_xor(self):
        rows=[{"id":str(i),"signal":"same",
               "losses":(0,1) if (i//2)^(i%2) else (1,0),"p":"1/4"}
              for i in range(4)]
        features={"x":{str(i):i//2 for i in range(4)},
                  "y":{str(i):i%2 for i in range(4)}}
        full=optimize_signals(rows,features,{"x":0,"y":0})
        self.assertEqual(full["features"],["x","y"])
        for name in ("x","y"):
            restricted=optimize_signals(rows,features,{"x":0,"y":0},authorized=[name])
            self.assertEqual(restricted["regret"],"1/2")

    def test_common_optimum_no_conflict(self):
        rows=[{"id":"x","signal":"all","losses":(0,1),"p":"1/2"},
              {"id":"y","signal":"all","losses":(0,3),"p":"1/2"}]
        self.assertEqual(certificate(rows)["exact"],"0")
        self.assertEqual(certificate(rows)["minimal_conflicts"],[[]])

    def test_bad_probability_rejected(self):
        with self.assertRaises(AssertionError):validate([
            {"id":"x","signal":"a","losses":(0,1),"p":"1"},
            {"id":"y","signal":"a","losses":(0,1),"p":"1"}])

    def test_missing_signal_rejected(self):
        with self.assertRaises(ValueError):
            optimize_signals(restic_worlds(),{"x":{"prepaid":0}},{"x":1})

    def test_unauthorized_name_rejected(self):
        with self.assertRaises(ValueError):
            optimize_signals(restic_worlds(),{"x":{"prepaid":0,"metered":1}},{"x":0},
                             authorized=["nonexistent"])

if __name__=="__main__":
    unittest.main(verbosity=2)
