import unittest
from audit_paper_b_v22_origin import V21,V22,audit
class SourceOrigin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=V21.read_text(encoding="utf8")
        cls.now=V22.read_text(encoding="utf8")
    def test_actual(self):self.assertEqual(audit(self.now,self.old),[])
    def test_original_chat_id_must_remain(self):
        self.assertIn("missing:1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er",audit(self.now.replace("1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er","HIDDEN"),self.old))
    def test_hard_condition_must_remain(self):
        self.assertIn("missing:HARD_SOLID",audit(self.now.replace("HARD_SOLID","HIDDEN"),self.old))
    def test_unexecuted_status_kept(self):
        self.assertIn("missing:no completed agent outputs",audit(self.now.replace("no completed agent outputs","no result",1),self.old))
    def test_section_deleted(self):
        self.assertIn("sections",audit(self.now.replace("### 5. When the same patch warrants different decisions","Deleted heading",1),self.old))
    def test_overreach_rejected(self):
        self.assertIn("overreach:we proved P!=NP",audit(self.now+"\nwe proved P!=NP",self.old))
if __name__=="__main__":unittest.main()
