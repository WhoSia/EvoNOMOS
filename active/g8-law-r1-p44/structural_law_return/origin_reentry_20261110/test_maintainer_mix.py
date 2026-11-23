from fractions import Fraction
import unittest
from maintainer_mix import (
  NEUTRAL, AWARE, MANIFEST, DIP_EFFECTS,
  mean_loss_effect, neutral_threshold_when_other_groups_equal
)
class OriginReanalysis(unittest.TestCase):
    def test_exact_boundary(self):
        q = neutral_threshold_when_other_groups_equal()
        self.assertEqual(q, Fraction(6804,29303))
        self.assertEqual(mean_loss_effect(q, (1-q)/2, (1-q)/2), 0)
        self.assertLess(mean_loss_effect(Fraction(1,5), Fraction(2,5), Fraction(2,5)), 0)
        self.assertGreater(mean_loss_effect(Fraction(1,4), Fraction(3,8), Fraction(3,8)), 0)
    def test_equal_mix_computed_not_original_estimate(self):
        self.assertEqual(mean_loss_effect(Fraction(1,3), Fraction(1,3), Fraction(1,3)), Fraction(8891,3000))
    def test_heterogeneous_signs(self):
        self.assertGreater(NEUTRAL, 0)
        self.assertLess(AWARE, 0)
        self.assertLess(MANIFEST, 0)
        self.assertTrue(all(v>0 for v in DIP_EFFECTS.values()))
    def test_invalid_distribution_refused(self):
        for w in [(-1,1,1),(Fraction(1,2),Fraction(1,2),Fraction(1,2))]:
            with self.assertRaises(ValueError):mean_loss_effect(*map(Fraction,w))
if __name__=='__main__':unittest.main(verbosity=2)
