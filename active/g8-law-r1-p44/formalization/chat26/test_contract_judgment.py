"""Independent source-level tests of contract_judgment.py's bounded semantics."""
import unittest
from collections import Counter
from itertools import product

from contract_judgment import (
    Fact, Verdict, WORLDS, accepts_fixed_patch, all_consistent_disclosures,
    compatible_worlds, reveal, verdict,
)


class FixedPatchJudgmentTests(unittest.TestCase):
    def test_four_authored_worlds_match_paper_b_table_two(self):
        cases = {(w.errata_required, w.book_prefix_protected):
                 accepts_fixed_patch(w) for w in WORLDS}
        self.assertEqual(cases, {
            (False, False): True,
            (False, True): False,
            (True, False): False,
            (True, True): False,
        })

    def test_all_nine_disclosure_states_and_1_5_3(self):
        all_states = list(all_consistent_disclosures())
        self.assertEqual(len(all_states), 9)
        self.assertEqual(
            Counter(verdict(x) for x in all_states),
            {Verdict.ACCEPT: 1, Verdict.REJECT: 5, Verdict.HOLD: 3},
        )

    def test_acceptance_requires_two_negative_facts(self):
        self.assertEqual(verdict({Fact.REPORT_ONLY, Fact.BOOK_UNPROTECTED}),
                         Verdict.ACCEPT)
        self.assertEqual(verdict({Fact.REPORT_ONLY}), Verdict.HOLD)
        self.assertEqual(verdict({Fact.BOOK_UNPROTECTED}), Verdict.HOLD)

    def test_errata_is_a_standalone_rejection_witness(self):
        self.assertEqual(verdict({Fact.ERRATA_REQUIRED}), Verdict.REJECT)
        self.assertEqual(verdict({Fact.ERRATA_REQUIRED, Fact.BOOK_UNPROTECTED}),
                         Verdict.REJECT)

    def test_protected_book_is_a_standalone_rejection_witness(self):
        self.assertEqual(verdict({Fact.BOOK_PROTECTED}), Verdict.REJECT)

    def test_contradictory_source_statements_are_not_acceptance_or_rejection(self):
        self.assertEqual(verdict({Fact.ERRATA_REQUIRED, Fact.REPORT_ONLY}),
                         Verdict.INCONSISTENT)
        self.assertEqual(compatible_worlds({Fact.BOOK_PROTECTED,
                                            Fact.BOOK_UNPROTECTED}), ())

    def test_question_does_not_always_settle_the_issue(self):
        self.assertEqual(reveal(set(), "errata"),
                         {False: Verdict.HOLD, True: Verdict.REJECT})
        self.assertEqual(reveal({Fact.REPORT_ONLY}, "book"),
                         {False: Verdict.ACCEPT, True: Verdict.REJECT})
        with self.assertRaises(ValueError):
            reveal(set(), "ocp_label")

    def test_compatible_worlds_shrink_under_added_facts(self):
        states = list(all_consistent_disclosures())
        for a, b in product(states, states):
            if a.issubset(b):
                self.assertTrue(set(compatible_worlds(b))
                                .issubset(compatible_worlds(a)))

    def test_robust_verdict_persists_on_consistent_evidence_refinement(self):
        states = list(all_consistent_disclosures())
        for a, b in product(states, states):
            if a.issubset(b) and verdict(a) in (
                    Verdict.ACCEPT, Verdict.REJECT):
                self.assertEqual(verdict(a), verdict(b))

    def test_full_information_never_holds(self):
        for evidence in all_consistent_disclosures():
            if len(evidence) == 2:
                self.assertIn(verdict(evidence),
                              (Verdict.ACCEPT, Verdict.REJECT))


if __name__ == "__main__":
    unittest.main()
