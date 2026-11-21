"""Verify four paper-B pre-run skeletons differ only in declared treatment text.

This does not run models, prove unbiased selection, or establish experimental outcomes.
"""
from pathlib import Path
HERE=Path(__file__).resolve().parent
ARMS=("NONE","HARD_SOLID","SCOPED_SOLID","EVIDENCE_CONDITIONAL")
SPLIT="## Design-advice treatment\n"
PLACEHOLDER="[TASK_TEXT_AND_SOURCE_SHA_NOT_YET_ASSIGNED]"
def audit(contents):
    bad=[]
    if set(contents)!=set(ARMS):bad.append("arm_set")
    if not all(SPLIT in text for text in contents.values()):return bad+["delimiter"]
    common={arm:text.split(SPLIT,1)[0] for arm,text in contents.items()}
    if len(set(common.values()))!=1:bad.append("common_task_differs")
    if not all(text.count(SPLIT)==1 for text in contents.values()):bad.append("duplicate_delimiter")
    if not all(PLACEHOLDER in text for text in contents.values()):bad.append("premature_task_claim")
    treatments={arm:text.split(SPLIT,1)[1] for arm,text in contents.items()}
    if len(set(treatments.values()))!=4:bad.append("duplicate_arm_treatment")
    if not treatments["HARD_SOLID"].startswith("Treat all five SOLID principles as mandatory"):bad.append("hard_missing")
    if not treatments["NONE"].startswith("No additional design-principle advice"):bad.append("none_missing")
    if not treatments["EVIDENCE_CONDITIONAL"].startswith("Choose the repair based on actual code"):bad.append("conditional_missing")
    return bad
if __name__=="__main__":
    contents={arm:(HERE/(arm+".md")).read_text(encoding="utf8") for arm in ARMS}
    errors=audit(contents)
    if errors:raise SystemExit("\n".join(errors))
    print("P35-B1: FOUR pre-run arms; common task byte-identical; treatment-only variation PASS; no agents run")
