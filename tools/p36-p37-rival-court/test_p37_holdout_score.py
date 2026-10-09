#!/usr/bin/env python3
"""Unit tests on SYNTHETIC fixtures only; never scientific holdout evidence."""
import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE=Path(__file__).with_name("p37_holdout_score.py")
spec=importlib.util.spec_from_file_location("p37_court", MODULE)
assert spec and spec.loader
court=importlib.util.module_from_spec(spec)
spec.loader.exec_module(court)

def write_fixture(root: Path, positive=True, duplicate=False, small=False):
    out=root/"holdout.csv"
    with out.open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f)
        w.writerow(court.COLUMNS)
        for repo_index in range(5 if small else 6):
            domain=f"domain_{repo_index//2}"
            for case in range(4):
                y=int(case%2==0)
                pb=0.55 if y else 0.45
                ph=(0.8 if y else 0.2) if positive else pb
                w.writerow([f"repo_{repo_index}",f"e{case}",domain,"holdout",y,pb,ph])
        if duplicate:
            w.writerow(["repo_0","e0","domain_0","holdout",1,0.55,0.8])
    return out

class StrongRivalCourtSyntheticChecks(unittest.TestCase):
    def test_positive_evidence_not_a_law(self):
        with tempfile.TemporaryDirectory() as d:
            result=court.judge(write_fixture(Path(d),True))
            self.assertEqual(result["prediction_feature_test"],"PASS_INCREMENTAL_GAIN")
            self.assertEqual(result["law_r2"],"NOT_AUTHORIZED")
            self.assertEqual(result["scientific_law_status"],"DIP49_IDENTIFICATION_HOLD")
            self.assertEqual(result["n_repositories"],6)
            self.assertEqual(result["n_episodes"],24)
    def test_null_competitor_retains_hold(self):
        with tempfile.TemporaryDirectory() as d:
            result=court.judge(write_fixture(Path(d),False))
            self.assertEqual(result["prediction_feature_test"],"HOLD_NO_GAIN")
    def test_duplicate_episode_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError,"duplicate"):
                court.judge(write_fixture(Path(d),True,True))
    def test_underpowered_sources_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError,"too few independent repos"):
                court.judge(write_fixture(Path(d),True,False,True))
    def test_probability_bounds_strict(self):
        for p in [0.0,1.0,float("nan"),float("inf")]:
            with self.assertRaises(ValueError):
                court.safe_logloss(0,p)

if __name__=="__main__":
    unittest.main()
