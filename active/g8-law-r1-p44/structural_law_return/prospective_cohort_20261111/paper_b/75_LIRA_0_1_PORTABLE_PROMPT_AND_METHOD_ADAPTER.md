# LIRA 0.1 — Localized Iterative Recommendation Audit
**Portable prompt / operational adapter** · 2026-11-23. Authoritative reusable Notion method: [LIRA 0.1](https://app.notion.com/p/420ef561cf928159986dc36b3c6464f8). This repository copy is an EvoNOMOS demonstration; other Labs should link to the Notion method rather than silently fork a second global doctrine.

## Ready-to-copy prompt

```text
LIRA 0.1(Localized Iterative Recommendation Audit, 국소 단위 반복 채택·검토법)을 적용해 다음 원고를 평가하고 수정해 줘.

원고/소스: [텍스트 또는 검증 가능한 정확한 링크]
장르·독자·제출처: [없으면 잠정적으로 판단하고 표시]
원문에서 보존할 질문·주장·말투: [직접 기재 또는 텍스트에서 확인]
비교할 구판과 원전: [있으면 정확한 목록]
검토 단위: [문단 / 문장 / 구절 / 어절; 기본값 문단 + 논증 핵심 문장]
결과 저장 위치: [이 채팅 / 지정한 Notion, GitHub, Drive 등]

1. 원고 전체를 먼저 읽고 '핵심 알맹이'를 1~2문장으로 밝혀. 저자가 원래 하려는 말을 작은 실험이나 정교한 표현으로 대체하지 마.
2. 실제 소스가 뒷받침하는 내용과 해석·추정·향후 계획을 분리해. 사실/근거 상태는 별도 표지(EVIDENCED, QUALIFIED, UNSUPPORTED, UNVERIFIED)로 남겨.
3. 각 단위에 ID, 0.00~1.00의 '그 표현을 그대로 채택하고 싶은 편집 추천도', 논증 기능, 존재 이유, 반론 및 수정 대안을 달아. 0.9는 참일 확률 90%가 아니야.
4. 저자·회의적인 심사자·독자·근거 감사자·문체 편집자 역할을 따로 적용해. 하나의 AI가 다역 검토한 것을 외부 독립 심사라고 주장하지 마.
5. 좋은 문장은 보호하고, 어정쩡한 표현은 최소 수정안/과감한 대안 중 필요한 것만 제시해. 단문·장문의 길이는 논증 기능에서 자연스럽게 나오도록 하고 저자 특유의 질문, 반전, 재치가 정확하면 남겨 둬.
6. 평가가 모두 고득점으로 몰리면 과잉 호의 가능성을 다시 검토하되 강제로 낮은 점수 분포를 만들지는 마. 문장 점수 평균을 논문의 독창성이나 실증적 신뢰도와 혼동하지 마.
7. 수정 후 문단과 전체 원고를 다시 읽고 의미·리듬·용어·인용·다국어 주장 강도가 유지되는지 검토해. 실패가 발견될 때만 다시 돌고, 취향 차이만 남으면 멈춰.
8. 최종 출력은 깨끗한 원고와 분리된 점수·코멘트 원장, 가장 강한 반론과 미해결 부분, 실제 수정·저장된 경로 및 검증 결과를 제공해. 나의 최종 채택 권한을 존중해.
```

## Execution and quality contract

- First use **Research OS WRITING 3.0** for drafting and fidelity, then use LIRA as optional manuscript-editor pass; do not generate each sentence as the answer to a scorecard cell.
- No random artificial humanization, detector evasion, fabricated mistakes, generic anti-AI style rules.
- Maintain distinct records for stylistic recommendation, originality hypothesis, factual support, and completed experiment.
- Score thresholds: ≥.90 protect; .75–.89 local polish; .50–.74 rethink/offer alternatives; .25–.49 restructure; <.25 reject unless author explains an override. Thresholds are adjustable suggestions, not calibrated science.
- Example source: [Paper B v28](PAPER_B_BILINGUAL_POSITION_28_20261123.md), [v29](PAPER_B_BILINGUAL_POSITION_29_20261123.md), [v30](PAPER_B_BILINGUAL_POSITION_30_20261123.md), and their audit ledgers. These are *workshop experiences*, not proof the method performs better in blinded cross-lab evaluation.
