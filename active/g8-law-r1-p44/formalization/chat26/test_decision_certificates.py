"""Exact negative/positive witness and question-selection regression suite."""
import unittest
from itertools import combinations
from contract_judgment import Fact, Verdict, all_consistent_disclosures, compatible_worlds, verdict
from decision_certificates import (
    consistent_evidence, minimal_certificates, ambiguity_witness,
    reveal_partition, exact_two_question_strategy,
)


class FiniteCertificateTests(unittest.TestCase):
    def test_minimal_rejection_certificates(self):
        self.assertEqual(set(minimal_certificates(Verdict.REJECT)), {
            frozenset({Fact.ERRATA_REQUIRED}),
            frozenset({Fact.BOOK_PROTECTED}),
        })

    def test_minimal_acceptance_certificate(self):
        self.assertEqual(minimal_certificates(Verdict.ACCEPT),
                         (frozenset({Fact.REPORT_ONLY, Fact.BOOK_UNPROTECTED}),))

    def test_hold_witnesses_are_real_opposite_worlds(self):
        for evidence in all_consistent_disclosures():
            pair = ambiguity_witness(evidence)
            if verdict(evidence) == Verdict.HOLD:
                self.assertIsNotNone(pair)
                self.assertTrue(all(w in compatible_worlds(evidence) for w in pair))
                self.assertNotEqual(pair[0], pair[1])
            else:
                self.assertIsNone(pair)

    def test_one_question_partition_never_loses_worlds(self):
        for facts in all_consistent_disclosures():
            for question in ("errata", "book"):
                parts = reveal_partition(facts, question)
                merged = {w for group in parts.values() for w in group}
                self.assertEqual(merged, set(compatible_worlds(facts)))

    def test_reject_certificates_are_inclusion_minimal(self):
        for target in (Verdict.ACCEPT, Verdict.REJECT):
            for witness in minimal_certificates(target):
                for fact in witness:
                    self.assertNotEqual(verdict(witness - {fact}), target)

    def test_question_prior_zero_one_boundaries(self):
        self.assertEqual(exact_two_question_strategy(1, 0)[0], ("errata",))
        self.assertEqual(exact_two_question_strategy(0, 1)[0], ("book",))
        self.assertEqual(set(exact_two_question_strategy(0.5, 0.5)[0]),
                         {"errata", "book"})

    def test_no_priors_are_silently_assumed(self):
        for bad_a, bad_b in [(-0.1, 0.5), (0, 1.1), (2, -1)]:
            with self.assertRaises(ValueError):
                exact_two_question_strategy(bad_a, bad_b)

    def test_reject_unrecognized_claims_and_contradictions(self):
        with self.assertRaises(ValueError):
            consistent_evidence({"OCP violation"})
        self.assertFalse(consistent_evidence({Fact.REPORT_ONLY, Fact.ERRATA_REQUIRED}))
        with self.assertRaises(ValueError):
            reveal_partition({Fact.REPORT_ONLY, Fact.ERRATA_REQUIRED}, "book")
        with self.assertRaises(ValueError):
            reveal_partition(set(), "unknown")

    def test_unknown_target_is_rejected(self):
        with self.assertRaises(ValueError):
            minimal_certificates(Verdict.HOLD)

    def test_all_16_signed_atom_subsets_well_defined(self):
        for size in range(5):
            for subset in combinations(list(Fact), size):
                expected = bool(compatible_worlds(subset))
                self.assertEqual(consistent_evidence(subset), expected)


if __name__ == "__main__":
    unittest.main()
