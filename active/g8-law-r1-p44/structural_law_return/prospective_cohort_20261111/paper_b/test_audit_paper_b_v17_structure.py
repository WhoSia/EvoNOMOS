"""Negative controls for manuscript integrity audit, not scholarly peer review."""
import unittest
from pathlib import Path
from audit_paper_b_v17_structure import V16, V17, check


class BilingualAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = V16.read_text(encoding="utf-8")
        cls.current = V17.read_text(encoding="utf-8")

    def test_current_manuscript_passes(self):
        self.assertEqual(check(self.current, self.original), [])

    def test_omitted_english_fails(self):
        self.assertIn("missing or repeated bilingual body boundary",
                      check(self.current.replace("## English manuscript", ""), self.original))

    def test_wrong_edition_fails(self):
        self.assertIn("wrong v17 title",
                      check(self.current.replace("Bilingual Integrated Manuscript 17", "Bilingual Integrated Manuscript 16", 1), self.original))

    def test_missing_primary_rival_fails(self):
        self.assertIn("primary competitor Papotti missing",
                      check(self.current.replace("Papotti", "AuthorHidden"), self.original))

    def test_stale_appendix_reference_fails(self):
        s = self.current.replace("12판에 있던 그림 1과 파일 배치 실험은 17판 본문",
                                 "12판에 있던 그림 1과 파일 배치 실험은 14판 본문")
        self.assertIn("stale v14 appendix statement", check(s, self.original))

    def test_prohibited_law_promotion_fails(self):
        self.assertIn("prohibited novelty promotion",
                      check(self.current + "\nproved LAW-R2", self.original))


if __name__ == "__main__":
    unittest.main()
