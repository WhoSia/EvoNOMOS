import unittest
from itertools import product as words
from math import inf
from product import Local,Edit,cost,combine,separate

def models():
 a=Local("0",{"0":frozenset(),"1":frozenset({"a"})},{"0":(Edit("alice",2,"1"),),"1":()},frozenset({"alice"}),frozenset({"a"}))
 b=Local("0",{"0":frozenset(),"1":frozenset({"b"})},{"0":(Edit("bob",3,"1"),),"1":()},frozenset({"bob"}),frozenset({"b"}))
 return a,b

class Exhaustive(unittest.TestCase):
 def test_1984_model_word_pairs(self):
  seq=[w for k in range(5) for w in words(("a","b"),repeat=k)]
  count=0
  for ea,eb,ra,rb,ga,gb in words((False,True),repeat=6):
   a,b=models()
   if not ea:a.edges["0"]=()
   if not eb:b.edges["0"]=()
   if not ra:a.rights=frozenset()
   if not rb:b.rights=frozenset()
   if not ga:a.goals["1"]=frozenset()
   if not gb:b.goals["1"]=frozenset()
   p=combine(a,b)
   for w in seq:
    self.assertEqual(cost(p,w),separate(a,b,w),(ea,eb,ra,rb,ga,gb,w))
    count+=1
  self.assertEqual(count,1984)
 def test_cross_effect(self):
  a,b=models();p=combine(a,b)
  p.edges["0@0"]+=(Edit("alice",1,"1@1"),)
  self.assertEqual(separate(a,b,("a","b")),5)
  self.assertEqual(cost(p,("a","b")),1)
 def test_shared_budget(self):
  a,b=models();p=combine(a,b)
  p.edges["1@0"]=();p.edges["0@1"]=()
  self.assertEqual(cost(p,("a","b")),inf)
  self.assertEqual(separate(a,b,("a","b")),5)
 def test_unmet_demand_retained(self):
  a,b=models();a.goals["1"]=frozenset()
  self.assertEqual(cost(combine(a,b),("a","b")),inf)
