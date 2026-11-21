import unittest
from finite_court import *

class Court(unittest.TestCase):
    def test_branch_traces_equal_but_bisim_fails(self):
        a,b=branch_countermodels()
        for n in range(7):
            self.assertEqual(trace_language(a,"s",n),trace_language(b,"s",n))
        self.assertNotIn(("s","s"),largest_cost_labelled_bisimulation(a,b))
    def test_rights_do_not_follow_observations(self):
        a,b=rights_countermodel()
        self.assertEqual(a.observation["s"],b.observation["s"])
        self.assertEqual(shortest_repair(a,"s","owner","extend"),1)
        self.assertIsNone(shortest_repair(b,"s","owner","extend"))
        self.assertNotIn(("s","s"),largest_cost_labelled_bisimulation(a,b))
    def test_identical_reflexive(self):
        for a in [*branch_countermodels(),*rights_countermodel()]:
            self.assertIn(("s","s"),largest_cost_labelled_bisimulation(a,a))
    def test_missing_transition_state_rejected(self):
        a=Graph({"s":"ok"},{"s":((("owner","a",1),"unknown"),)})
        with self.assertRaises(ValueError): a.validate()
    def test_incomplete_graph_rejected(self):
        a=Graph({"s":"ok","t":"ok"},{"s":()})
        with self.assertRaises(ValueError): a.validate()
    def test_negative_cost_rejected(self):
        a=Graph({"s":"ok"},{"s":((("owner","a",-1),"s"),)})
        with self.assertRaises(ValueError): a.validate()
    def test_empty_actor_rejected(self):
        a=Graph({"s":"ok"},{"s":((("","a",1),"s"),)})
        with self.assertRaises(ValueError): a.validate()
    def test_observer_mismatch(self):
        a=Graph({"s":"ok"},{"s":()});b=Graph({"s":"bad"},{"s":()})
        self.assertNotIn(("s","s"),largest_cost_labelled_bisimulation(a,b))
    def test_edit_label_cost_mismatch(self):
        a,b=rights_countermodel()
        c=Graph({"s":"old_client_ok","target":"old_client_ok"},
                {"s":((("owner","extend",2),"target"),),"target":()})
        self.assertNotIn(("s","s"),largest_cost_labelled_bisimulation(a,c))
    def test_edit_label_actor_mismatch(self):
        a,b=rights_countermodel()
        c=Graph({"s":"old_client_ok","target":"old_client_ok"},
                {"s":((("contractor","extend",1),"target"),),"target":()})
        self.assertNotIn(("s","s"),largest_cost_labelled_bisimulation(a,c))
    def test_shortest_repair_compares_all_edges(self):
        g=Graph({"s":"ok","t":"ok"},{"s":((("owner","extend",10),"t"),
                    (("owner","extend",1),"t")),"t":()})
        self.assertEqual(shortest_repair(g,"s","owner","extend"),1)
    def test_empty_trace(self):
        a,b=rights_countermodel()
        self.assertEqual(trace_language(a,"s",0),{()})
    def test_labeled_language_detects_missing_right(self):
        a,b=rights_countermodel()
        self.assertNotEqual(trace_language(a,"s",1),trace_language(b,"s",1))

if __name__=="__main__":
    unittest.main()
