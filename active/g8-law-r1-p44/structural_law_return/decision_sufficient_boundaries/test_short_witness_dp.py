from itertools import combinations
import random
import unittest
from short_witness_dp import shortest_conflict_witness

def brute_witness(opt_sets):
    for k in range(1,len(opt_sets)+1):
        for ids in combinations(range(len(opt_sets)),k):
            shared=set(opt_sets[ids[0]])
            for i in ids[1:]:shared.intersection_update(opt_sets[i])
            if not shared:return ids
    return None

class ShortConflictWitnessTests(unittest.TestCase):
    def test_three_way_has_no_pair_certificate(self):
        self.assertEqual(shortest_conflict_witness(({0,1},{1,2},{0,2}),3),(0,1,2))

    def test_tight_action_count_bound(self):
        for k in range(2,9):
            obs=tuple(set(range(k))-{i} for i in range(k))
            self.assertEqual(shortest_conflict_witness(obs,k),tuple(range(k)))

    def test_common_action_no_conflict(self):
        self.assertIsNone(shortest_conflict_witness(({0,1},{1,2},{1,3}),4))

    def test_random_against_combinatorial_bruteforce(self):
        rng=random.Random(2411)
        for k in range(2,6):
            for n in range(2,8):
                for _ in range(45):
                    sets=tuple({i for i in range(k) if rng.random()<0.5} or
                               {rng.randrange(k)} for _ in range(n))
                    self.assertEqual(shortest_conflict_witness(sets,k),brute_witness(sets))
                    winner=shortest_conflict_witness(sets,k)
                    if winner is not None:self.assertLessEqual(len(winner),k)

    def test_invalid_actions(self):
        with self.assertRaises(ValueError):shortest_conflict_witness(({0},set()),2)
        with self.assertRaises(ValueError):shortest_conflict_witness(({3},),3)

if __name__=="__main__":
    unittest.main(verbosity=2)
