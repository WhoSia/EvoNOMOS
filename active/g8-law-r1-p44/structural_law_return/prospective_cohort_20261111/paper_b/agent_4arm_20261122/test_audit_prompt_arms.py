import unittest
from audit_prompt_arms import HERE,ARMS,SPLIT,PLACEHOLDER,audit
class FourArms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources={name:(HERE/(name+".md")).read_text(encoding="utf8") for name in ARMS}
    def test_actual(self):self.assertEqual(audit(self.sources),[])
    def test_common_task_must_match(self):
        alt=dict(self.sources)
        alt["HARD_SOLID"]=alt["HARD_SOLID"].replace("Follow the exact task requirement","Follow a different task requirement",1)
        self.assertIn("common_task_differs",audit(alt))
    def test_not_runnable(self):
        self.assertTrue(all(PLACEHOLDER in s for s in self.sources.values()))
    def test_duplicate_treatment_fails(self):
        alt=dict(self.sources);alt["SCOPED_SOLID"]=alt["NONE"]
        self.assertIn("duplicate_arm_treatment",audit(alt))
    def test_missing_arm_fails(self):
        alt=dict(self.sources);del alt["NONE"]
        self.assertIn("arm_set",audit(alt))
    def test_missing_delimiter_fails(self):
        alt=dict(self.sources);alt["SCOPED_SOLID"]=alt["SCOPED_SOLID"].replace(SPLIT,"")
        self.assertIn("delimiter",audit(alt))
if __name__=="__main__":unittest.main()
