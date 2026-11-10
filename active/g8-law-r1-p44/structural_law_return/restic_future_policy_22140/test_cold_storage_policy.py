from fractions import Fraction
import unittest
from cold_storage_policy import (
    PackObservation, BillingEnvironment,
    incremental_cost_of_repack, optimal_action
)

class ExternalColdStoragePolicyTests(unittest.TestCase):
    def test_identical_pack_observation_different_correct_action(self):
        pack = PackObservation(Fraction(5, 100), 11)
        locked = BillingEnvironment("prepaid_locked")
        metered = BillingEnvironment("pay_as_you_go")
        self.assertEqual(incremental_cost_of_repack(pack, locked), Fraction(523, 50))
        self.assertEqual(incremental_cost_of_repack(pack, metered), Fraction(-27, 50))
        self.assertEqual(optimal_action(pack, locked), "keep")
        self.assertEqual(optimal_action(pack, metered), "repack")

    def test_reported_overlap_arithmetic_is_195_percent(self):
        self.assertEqual(1 + (1 - Fraction(5, 100)), Fraction(195, 100))

    def test_payg_repacking_has_declared_operation_cost_threshold(self):
        pack = PackObservation(Fraction(5, 100), 11)
        self.assertEqual(optimal_action(pack, BillingEnvironment("pay_as_you_go", Fraction(56, 100))), "keep")
        self.assertEqual(optimal_action(pack, BillingEnvironment("pay_as_you_go", Fraction(54, 100))), "repack")

    def test_reject_invalid_context(self):
        with self.assertRaises(ValueError):
            PackObservation(Fraction(11, 10), 11)
        with self.assertRaises(ValueError):
            PackObservation(Fraction(1, 10), 0)
        with self.assertRaises(ValueError):
            BillingEnvironment("unsupported")

if __name__ == "__main__":
    unittest.main(verbosity=2)
