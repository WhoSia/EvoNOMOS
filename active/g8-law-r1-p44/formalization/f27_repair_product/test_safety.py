import unittest
from math import inf
from product import Local,Edit,cost,combine
from test_factorization import models

class SafetyCourt(unittest.TestCase):
 def test_permission_reduction(self):
  a,b=models();a.rights=frozenset()
  self.assertEqual(cost(combine(a,b),("a","b")),inf)
 def test_repeated_demand(self):
  a,b=models()
  self.assertEqual(cost(combine(a,b),("a","a","b")),5)
 def test_bad_demand_rejected(self):
  a,b=models()
  with self.assertRaises(ValueError):cost(combine(a,b),("unknown",))
 def test_overlapping_alphabets_rejected(self):
  a,b=models();b.demands=frozenset({"a","b"})
  with self.assertRaises(ValueError):combine(a,b)
 def test_bad_cost_rejected(self):
  a,b=models();a.edges["0"]=(Edit("alice",-1,"1"),)
  with self.assertRaises(ValueError):a.validate()
 def test_bad_table_rejected(self):
  a,b=models();a.edges.pop("1")
  with self.assertRaises(ValueError):a.validate()
 def test_quantifier_polarity(self):
  a,b=models();a.rights=frozenset()
  self.assertEqual(cost(a,("a",)),inf)
  a.rights=frozenset({"alice"})
  self.assertEqual(cost(a,("a",)),2)
  invariant={"good":True,"bad":False}
  self.assertTrue(all(invariant[x] for x in ["good"]))
  self.assertFalse(all(invariant[x] for x in ["good","bad"]))
