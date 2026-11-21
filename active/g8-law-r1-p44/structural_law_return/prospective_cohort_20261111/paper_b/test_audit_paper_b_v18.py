import unittest
from audit_paper_b_v18 import V17,V18,audit

class V18Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous=V17.read_text(encoding="utf-8")
        cls.current=V18.read_text(encoding="utf-8")
    def test_actual_manuscript(self):
        self.assertEqual(audit(self.current,self.previous),[])
    def test_missing_korean_bridge(self):
        errors=audit(self.current.replace("분류 결과에서 수정안 거절까지","(누락)"),self.previous)
        self.assertIn("missing_bridge:분류 결과에서 수정안 거절까지",errors)
    def test_missing_english_bridge(self):
        errors=audit(self.current.replace("From a classification to a patch disposition","(missing)"),self.previous)
        self.assertIn("missing_bridge:From a classification to a patch disposition",errors)
    def test_p44_tangent_disallowed(self):
        part="### 6. 기존 호출 경로도 요구의 일부일 때\nhttp.HandlerFunc\n"
        errors=audit(self.current.replace("### 6. 기존 호출 경로도 요구의 일부일 때",part),self.previous)
        self.assertIn("off_topic_p44_go_in_body",errors)
    def test_wrong_version(self):
        self.assertIn("wrong_version",audit(self.current.replace("Manuscript 18","Manuscript 17",1),self.previous))
    def test_section_deleted(self):
        self.assertIn("section_count",audit(self.current.replace("### 3. 자료와 방법","자료와 방법",1),self.previous))
    def test_stale_edition(self):
        self.assertIn("stale_edition",audit(self.current.replace("18판 본문에 싣지","17판 본문에 싣지",1),self.previous))

if __name__ == "__main__":
    unittest.main()
