"""Read-only bilingual v16->v17 manuscript structural and claim-boundary checker.

This tests manuscript integrity, not the truth of primary-source quotations or
the reliability of a new real reviewer sample. Never rewrite earlier versions.
"""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
V16 = HERE / "PAPER_B_BILINGUAL_INTEGRATED_16_20261121.md"
V17 = HERE / "PAPER_B_BILINGUAL_INTEGRATED_17_20261121.md"
NEEDED = {
    "jin": "10.1007/s10515-026-00638-5",
    "widyasari": "10.1145/3708518",
    "papotti": "10.1007/s10664-024-10506-z",
    "ling": "10.3390/systems14101312",
}


def check(source: str, predecessor: str) -> list[str]:
    errors = []
    if not source.startswith("# Paper B — Bilingual Integrated Manuscript 17"):
        errors.append("wrong v17 title")
    if not predecessor.startswith("# Paper B — Bilingual Integrated Manuscript 16"):
        errors.append("not comparing correct frozen predecessor")
    if source.count("## 한국어 원고") != 1 or source.count("## English manuscript") != 1:
        errors.append("missing or repeated bilingual body boundary")
    if source.count("### 부록 A · 재현 자료") != 1 or source.count("### Appendix A · Reproduction") != 1:
        errors.append("missing bilingual appendices")
    for n in range(1, 8):
        ko = re.findall(r"^### " + str(n) + r"\. [^\n]+$", source, re.M)
        en = re.findall(r"^### " + str(n) + r"\. [^\n]+$", source, re.M)
        # Both languages share numbered headings. Require exactly two matches.
        if len(ko) != 2:
            errors.append(f"section {n} count {len(ko)}; expected two")
    for k in ("768", "48", "24", "64"):
        if k not in source:
            errors.append(f"archival audit count {k} missing")
    for k in ("Widyasari", "Papotti", "Jin and Chen", "Ling, Zou"):
        if k not in source:
            errors.append(f"primary competitor {k} missing")
    # Version and DOI consistency: Jin's retained PDF is arXiv; publisher page
    # may be cited in audit notes, and must not be silently asserted as read.
    for k, doi in NEEDED.items():
        if k != "jin" and doi not in source:
            errors.append(f"verified DOI for {k} missing")
    if source.count("10.1145/3708518") < 2:
        errors.append("Widyasari not placed in prose and references")
    if "12판에 있던 그림 1과 파일 배치 실험은 14판 본문" in source:
        errors.append("stale v14 appendix statement")
    if "실제 리뷰에서 원칙이 오용되는 빈도" not in source:
        errors.append("missing Korean external-validity ceiling")
    if "do not estimate how often OCP is misused" not in source:
        errors.append("missing English external-validity ceiling")
    if "30개 테스트" not in source or "30-test" not in source:
        errors.append("bounded CI verification not bilingual")
    if "LAW-R2 신규성을 증명했다" in source or "proved LAW-R2" in source:
        errors.append("prohibited novelty promotion")
    if len(source) <= len(predecessor):
        errors.append("revision unexpectedly shorter than predecessor")
    return errors


if __name__ == "__main__":
    previous = V16.read_text(encoding="utf-8")
    current = V17.read_text(encoding="utf-8")
    errors = check(current, previous)
    if errors:
        raise SystemExit("\n".join(errors))
    print("Paper B v17: bilingual 7+7 structure, appendices, source rivals, bounded claims verified")
