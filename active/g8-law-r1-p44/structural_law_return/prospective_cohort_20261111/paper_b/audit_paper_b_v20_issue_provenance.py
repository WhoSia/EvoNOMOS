"""Paper B v20 static provenance and scope auditor; not a scientific oracle."""
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
V19=HERE/"PAPER_B_BILINGUAL_INTEGRATED_19_20261122.md"
V20=HERE/"PAPER_B_BILINGUAL_INTEGRATED_20_20261122.md"

def check(new,older):
    errors=[]
    if not new.startswith("# Paper B — Bilingual Integrated Manuscript 20"):
        errors.append("version")
    if not older.startswith("# Paper B — Bilingual Integrated Manuscript 19"):
        errors.append("predecessor")
    if new.count("## 한국어 원고")!=1 or new.count("## English manuscript")!=1:
        errors.append("bilingual_boundary")
    headings=[int(x) for x in re.findall(r"^### ([1-7])\. ",new,re.M)]
    if headings!=list(range(1,8))*2:
        errors.append("section_order")
    if new.count("### 부록 A · 재현 자료")!=1 or new.count("### Appendix A · Reproduction")!=1:
        errors.append("appendix")
    for anchor in ("go-chi/chi/issues/995","go-chi/chi/issues/1035",
                   "우회", "workaround", "정정", "corrected",
                   "2025", "post hoc", "연구자", "768", "48", "24", "64"):
        if anchor not in new:
            errors.append("missing:"+anchor)
    for anchor in ("원래 요청이 해결됐다는 증거", "original API request",
                   "정규식 주장을 같은 수준의 확정 사실", "regex problem did not reproduce"):
        if anchor not in new:
            errors.append("missing_caveat:"+anchor)
    if "F38 결과가 확인됐다" in new or "prospective F38 success" in new:
        errors.append("unsupported_f38_success")
    if "원칙이 오용되는 빈도를 보여 주지는 않는다" not in new:
        errors.append("prevalence_ceiling")
    if len(new)<=len(older):
        errors.append("source_regression_length")
    return errors

if __name__=="__main__":
    problems=check(V20.read_text(encoding="utf-8"),V19.read_text(encoding="utf-8"))
    if problems: raise SystemExit("\n".join(problems))
    print("v20 7+7 bilingual issue chronology, provenance caveats and source framing: PASS")
