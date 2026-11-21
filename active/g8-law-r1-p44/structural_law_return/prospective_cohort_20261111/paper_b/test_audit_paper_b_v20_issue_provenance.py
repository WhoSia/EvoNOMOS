import unittest
from audit_paper_b_v20_issue_provenance import V19,V20,check

class Version20Provenance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=V19.read_text(encoding="utf-8")
        cls.new=V20.read_text(encoding="utf-8")
    def test_actual_source(self):
        self.assertEqual(check(self.new,self.old),[])
    def test_missing_995_source(self):
        self.assertIn("missing:go-chi/chi/issues/995",check(self.new.replace("go-chi/chi/issues/995","hidden"),self.old))
    def test_missing_1035_source(self):
        self.assertIn("missing:go-chi/chi/issues/1035",check(self.new.replace("go-chi/chi/issues/1035","hidden"),self.old))
    def test_removed_english_correction_fails(self):
        self.assertIn("missing_caveat:regex problem did not reproduce",check(self.new.replace("regex problem did not reproduce","claim unknown"),self.old))
    def test_removed_korean_contract_distinction_fails(self):
        self.assertIn("missing_caveat:원래 요청이 해결됐다는 증거",check(self.new.replace("원래 요청이 해결됐다는 증거","단순 변경"),self.old))
    def test_fake_f38_success_rejected(self):
        self.assertIn("unsupported_f38_success",check(self.new+"\nprospective F38 success",self.old))
    def test_deleted_english_section_fails(self):
        self.assertIn("section_order",check(self.new.replace("### 5. When the same patch warrants different decisions","### 5. section removed"),self.old))
    def test_wrong_version_fails(self):
        self.assertIn("version",check(self.new.replace("Manuscript 20","Manuscript 19",1),self.old))

if __name__=="__main__":
    unittest.main()
