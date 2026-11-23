import unittest
from audit_paper_b_v21_vision import V20,V21,check
class Vision(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=V20.read_text(encoding="utf8")
        cls.now=V21.read_text(encoding="utf8")
    def test_original(self):self.assertEqual(check(self.now,self.old),[])
    def test_no_future_agenda(self):
        self.assertIn("missing:Four falsifiable directions",check(self.now.replace("Four falsifiable directions","Other paragraph",1),self.old))
    def test_no_korean_agenda(self):
        self.assertIn("missing:네 가지 반증 가능 질문",check(self.now.replace("네 가지 반증 가능 질문","검토 항목",1),self.old))
    def test_broken_section(self):
        self.assertIn("sections",check(self.now.replace("### 7. Conclusion","Conclusion heading",1),self.old))
    def test_unverified_formal_claim(self):
        self.assertIn("overclaim:We prove P != NP",check(self.now+"\nWe prove P != NP",self.old))
    def test_lost_historical_source(self):
        self.assertIn("missing:go-chi/chi/issues/995",check(self.now.replace("go-chi/chi/issues/995","hidden"),self.old))
if __name__=="__main__":unittest.main()
