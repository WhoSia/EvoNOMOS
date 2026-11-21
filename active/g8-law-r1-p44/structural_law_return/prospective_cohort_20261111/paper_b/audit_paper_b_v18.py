"""Check Paper B v18 source integrity and the distinction between classification and justified disposition.

Text-level checks only: not a substitute for human source reading or scientific peer review.
"""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
V17 = HERE / "PAPER_B_BILINGUAL_INTEGRATED_17_20261121.md"
V18 = HERE / "PAPER_B_BILINGUAL_INTEGRATED_18_20261121.md"

def audit(new: str, previous: str) -> list[str]:
    problems = []
    if not new.startswith("# Paper B — Bilingual Integrated Manuscript 18"):
        problems.append("wrong_version")
    if not previous.startswith("# Paper B — Bilingual Integrated Manuscript 17"):
        problems.append("wrong_predecessor")
    if new.count("## 한국어 원고") != 1 or new.count("## English manuscript") != 1:
        problems.append("bilingual_boundary")
    if new.count("### 부록 A · 재현 자료") != 1 or new.count("### Appendix A · Reproduction") != 1:
        problems.append("appendix_boundary")
    if len(re.findall(r"^### [1-7]\. ", new, flags=re.M)) != 14:
        problems.append("section_count")
    if [int(x) for x in re.findall(r"^### ([1-7])\. ", new, flags=re.M)] != list(range(1,8))*2:
        problems.append("section_order")
    for anchor in ("768", "48", "24", "64", "793", "Papotti", "Widyasari",
                   "Jin and Chen", "Ling, Zou", "1 ACCEPT", "5 REJECT"):
        if anchor not in new:
            problems.append("missing_anchor:"+anchor)
    for anchor in ("분류 결과에서 수정안 거절까지", "From a classification to a patch disposition",
                   "$A(E,B)=\\neg E\\land\\neg B$", "기존 호출 경로도 요구의 일부일 때",
                   "When the original call path is part of the requirement"):
        if anchor not in new:
            problems.append("missing_bridge:"+anchor)
    ko = new.split("## 한국어 원고", 1)[1].split("## English manuscript", 1)[0]
    en = new.split("## English manuscript", 1)[1].split("## 검증한 주요 참고문헌", 1)[0]
    if "http.HandlerFunc" in ko or "http.HandlerFunc" in en:
        problems.append("off_topic_p44_go_in_body")
    if "17판 본문에 싣지" in ko or "manuscript 17 does not reframe" in en:
        problems.append("stale_edition")
    if "원칙이 오용되는 빈도" not in ko or "do not estimate how often OCP is misused" not in new:
        problems.append("prevalence_boundary")
    if not len(new) > len(previous):
        problems.append("unexpected_shortening")
    return problems

if __name__ == "__main__":
    issues=audit(V18.read_text(encoding="utf-8"),V17.read_text(encoding="utf-8"))
    if issues:
        raise SystemExit("\n".join(issues))
    print("v18 bilingual 7+7 source, novel-claim ceilings, classification/action bridge: PASS")
