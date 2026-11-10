import unittest
from fractions import Fraction
from selective_gate_original_history import assess, SOURCE

MODEL={"Predict":{
"mux.go":{"B1":"tree.go","B1PairEvents":34,"B1SeedEvents":83},
"tree.go":{"B1":"mux.go","B1PairEvents":34,"B1SeedEvents":64},
"context.go":{"B1":"mux.go","B1PairEvents":22,"B1SeedEvents":33}}}
class SelectiveOriginalGateSmoke(unittest.TestCase):
 def test_frozen_selective_seed_decisions(self):
  chosen={seed:Fraction(p["B1PairEvents"],p["B1SeedEvents"])>Fraction(1,2)
     for seed,p in MODEL["Predict"].items()}
  self.assertEqual(chosen,{"mux.go":False,"tree.go":True,"context.go":True})
 def test_refuse_synthetic_47_query_claim(self):
  # A small fake list must not be represented as the original source study.
  with self.assertRaises(AssertionError):
   assess([("synthetic",("mux.go","tree.go"))],MODEL)
if __name__=="__main__":unittest.main(verbosity=2)
