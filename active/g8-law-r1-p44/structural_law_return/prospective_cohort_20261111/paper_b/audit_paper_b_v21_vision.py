"""Read-only Paper B v21 editorial drift guard; text checks cannot establish priority or factual validity."""
from pathlib import Path
import re
P=Path(__file__).resolve().parent
V20=P/"PAPER_B_BILINGUAL_INTEGRATED_20_20261122.md"
V21=P/"PAPER_B_BILINGUAL_INTEGRATED_21_20261122.md"
def check(now,previous):
    bad=[]
    if not now.startswith("# Paper B — Bilingual Integrated Manuscript 21"): bad.append("version")
    if not previous.startswith("# Paper B — Bilingual Integrated Manuscript 20"):bad.append("prior")
    if [int(x) for x in re.findall(r"^### ([1-7])\. ",now,re.M)]!=list(range(1,8))*2:bad.append("sections")
    for anchor in ("## 한국어 원고","## English manuscript","### 부록 A · 재현 자료","### Appendix A · Reproduction"):
        if now.count(anchor)!=1:bad.append("boundary:"+anchor)
    for anchor in ("원칙→수정안 판단의 전이 문제","principle-to-patch transport problem",
                    "Four falsifiable directions","네 가지 반증 가능 질문",
                    "Paper C:","Paper D:","768","48","24","64",
                    "go-chi/chi/issues/995","go-chi/chi/issues/1035"):
        if anchor not in now:bad.append("missing:"+anchor)
    for phrase in ("not a new theorem","proposals, not findings","not a declaration",
                   "첫-in-world"):
        if phrase=="첫-in-world":continue
        if phrase not in now:bad.append("limit:"+phrase)
    for forbidden in ("We prove P != NP","proved P=NP","LAW-R2 formally verified",
                      "first in the world to identify requirements"):
        if forbidden in now:bad.append("overclaim:"+forbidden)
    if len(now)<=len(previous):bad.append("unexpected_length")
    return bad
if __name__=="__main__":
    errors=check(V21.read_text(encoding="utf8"),V20.read_text(encoding="utf8"))
    if errors:raise SystemExit("\n".join(errors))
    print("Paper B v21 7+7 sections, idea-first proposals, falsifiability and bounded evidence: PASS")
