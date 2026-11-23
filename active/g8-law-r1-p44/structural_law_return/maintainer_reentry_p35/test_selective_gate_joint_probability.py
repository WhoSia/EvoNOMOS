import unittest
from fractions import Fraction
from selective_gate_joint_probability import train_full_gate,evaluate_joint_gate
class TwoProbabilityGate(unittest.TestCase):
 def test_training_exact_partner_and_any_counter(self):
  model={"Predict":{
   "mux.go":{"B1":"tree.go","B1SeedEvents":2,"B1PairEvents":1},
   "tree.go":{"B1":"mux.go","B1SeedEvents":1,"B1PairEvents":1},
   "context.go":{"B1":"tree.go","B1SeedEvents":1,"B1PairEvents":0}}}
  rows=[("x",("mux.go","tree.go")),("y",("mux.go","context.go"))]
  # Use the pure logic without the original training 121 commit asserted oracle.
  result=train_full_gate(rows,model)
  self.assertEqual(result["mux.go"]["train_any_extra_events"],2)
  self.assertEqual(result["mux.go"]["p_top"],"1/2")
  self.assertTrue(result["mux.go"]["alert"])
  self.assertTrue(result["tree.go"]["alert"])
  self.assertFalse(result["context.go"]["alert"])
 def test_strict_tie_abstention(self):
  rows=[("x",("mux.go","tree.go")),("y",("mux.go",)),("z",("context.go",))]
  seal={"Predict":{
    "mux.go":{"B1":"tree.go","B1SeedEvents":2,"B1PairEvents":1},
    "tree.go":{"B1":"mux.go","B1SeedEvents":1,"B1PairEvents":1},
    "context.go":{"B1":"tree.go","B1SeedEvents":1,"B1PairEvents":0}}}
  result=train_full_gate(rows,seal)
  self.assertFalse(result["mux.go"]["alert"])
if __name__=="__main__":unittest.main(verbosity=2)
