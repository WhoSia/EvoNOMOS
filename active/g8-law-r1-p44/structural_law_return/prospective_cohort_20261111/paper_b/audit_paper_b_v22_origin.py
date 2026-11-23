"""Source/claim guard for idea-first Paper B v22; validates text structure only."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent
V21=ROOT/"PAPER_B_BILINGUAL_INTEGRATED_21_20261122.md"
V22=ROOT/"PAPER_B_BILINGUAL_INTEGRATED_22_20261122.md"

def audit(current,prior):
    bad=[]
    if not current.startswith("# Paper B — Bilingual Integrated Manuscript 22"):bad.append("version")
    if not prior.startswith("# Paper B — Bilingual Integrated Manuscript 21"):bad.append("prior")
    if [int(x) for x in re.findall(r"^### ([1-7])\. ",current,re.M)]!=list(range(1,8))*2:bad.append("sections")
    for item in ("## 한국어 원고","## English manuscript","### 부록 A · 재현 자료","### Appendix A · Reproduction"):
        if current.count(item)!=1:bad.append("boundary:"+item)
    for item in ("원칙과 강제 규칙","operational quasi-axiomatization",
                 "2026년 7월 29일","October 9, 2026",
                 "NONE","HARD_SOLID","SCOPED_SOLID","EVIDENCE_CONDITIONAL",
                 "Lexical echo","어휘 반복","PRE-AGENT-RUN",
                 "no completed agent outputs","추가 설계 원칙",
                 "1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er",
                 "P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md"):
        if item not in current:bad.append("missing:"+item)
    for banned in ("we proved P!=NP","world first theorem","model weights contain SOLID"):
        if banned in current:bad.append("overreach:"+banned)
    if len(current)<=len(prior):bad.append("shortened")
    return bad
if __name__=="__main__":
    errors=audit(V22.read_text(encoding="utf8"),V21.read_text(encoding="utf8"))
    if errors:raise SystemExit("\n".join(errors))
    print("Paper B v22 original July chat / Oct four-arm prespec, bilingual 7+7 and non-run claims PASS")
