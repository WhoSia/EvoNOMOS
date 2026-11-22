# Paper B R33 — LIRA v32 cold-read, concrete probes and objection ledger
**2026-11-23 · internal cold-read pass.** The v31 text, v32 readback, project-constructed patch, and full-text arXiv abstracts/introduction for 2610.33201 and 2610.38244 have been read. These are internal reviewer roles; no external model or human independent review.

## What the paper is now actually proposing
An integrative **research programme** on the (1) technical reasons supporting a design guideline's application, (2) legitimate instruction/action authority, and (3) causal influence on coding-agent patch decisions. These three cannot be collapsed into one notion of authority. Revisions, refusals and deferrals after authorized counterevidence are candidate observations. The project has no independent sampled agent data, source-uptake genealogy or general mathematical software-design theorem.

## LIRA unit-level review (subjective preference to retain wording, not truth/novelty probabilities)

| ID | Original v32 span / location | Keep score | Argument job | Claim status | Decision |
| --- | --- | ---: | --- | --- | --- |
| K-A1 | “좋은 설계 원칙은 코드를 개선할 이유를 준다.” | 0.91 | Plain opening | conceptual interpretation | Keep. Starts with positive claim; no bombast. |
| K-A2 | “설계 조언은 무엇을 근거로 실제 결정에 영향을 미치며, 그 근거가 달라졌을 때 판단은 어떻게 바뀌어야 하는가?” | 0.98 | Thesis | research proposal | Keep verbatim. Strong bridge from old design into AI action. |
| K-SCENE | “순서를 보장할 책임은 그리기 함수에 있는가, 호출자에게 있는가, 별도의 정렬 정책에 있는가?” | 0.97 | Source-anchored problem | historical illustration / proposed options | Keep, with note that variants are the author's question, not Martin's direct quotation. |
| K-PIVOT | “OCP라는 이름은 그 답을 대신하지 않는다.” | 0.99 | Hinge | author inference | Protect one-sentence paragraph. |
| K-TRANS | “다만 이런 조건이 현대의 지침으로 전해지면서 실제로 얼마나 생략됐는지는 아직 별도로 조사해야 한다.” | 0.95 | Historical missing link | untested documentary question | Keep, crucial corrective to false genealogical causal chain. |
| K-REASON | “원칙을 적용할 기술적 이유와 그 지시를 집행할 정당한 권한은 같지 않다.” | 0.98 | Construct repair | conceptual distinction | Keep. The strongest change vs v31. |
| K-BEHAV | “그것은 행동에 영향을 주었다는 관찰이지 그 결정이 옳았다는 판정은 아니다.” | 0.97 | Third distinction | proposed evaluation boundary | Keep; separates manipulation outcome and normative validity. |
| K-NEO | “운영상의 준공리화라는 표현은…” | 0.66 | New term | provisional theoretical framing | Must remain testable and non-psychological; optional to shorten. |
| K-EX1 | “우리가 구성한 도서관 사례에서는 기존 소스 파일은 그대로 두고 기술보고서용 제공자를 추가한다.” | 0.98 | Correct source provenance | confirmed project-authored fixture | Fixes a source-underdescription in v31; protect. |
| K-EX2 | “계약이 공개되지 않았다면 섣불리 합격이나 불합격을 정할 수도 없다.” | 0.92 | Missing premise | conditional inference | Could clarify evaluator's available authority, but not needed in short paper. |
| K-PLUS | “OCP에 맞춰 변경 가능성이 높은 부분을 분리한 설계가 실제로 기존 호출자를 더 안전하게 보호한다면…” | 0.96 | Positive rival | proposed case, NOT experiment outcome | Keep: method genuinely allows SOLID to help. |
| K-PRIOR | “2026년에는 코딩 에이전트가…” | 0.89 | Closest rival | 2026 paper sources | References correct but body should cite two closer papers explicitly; text is okay if bibliography visible. |
| K-DOCTRINE | “이 연구들이 Paper B의 질문을 대신 끝내 주지는 않는다.” | 0.71 | Defensive response | author position | Slightly self-serving; improve by naming *what remains unobserved* rather than declaring study unique. |
| K-LAST | “좋은 원칙이라면 더욱 물어야 한다. 이 코드를 바꾸라는 판단은 그 원칙의 어느 근거에서 나오는가?” | 0.99 | Distinct authorial ending | question | Preserve, does not pretend to provide the answer. |
| E-THREE | “We need to distinguish three senses of authority.” | 0.94 | Conceptual structure | author analytic lens | Keeps English legible without translating unnatural Korean word order. |
| E-RESEARCH | “Our proposed connection is narrower in its mechanics but broader in its historical object…” | 0.78 | Novelty positioning | proposal vs nearby work | Accurate but bureaucratic; consider an affirmative prose alternative. |
| E-END | “The better the principle, the sharper the question…” | 0.98 | Ending | rhetoric disciplined by exact conditions | Good. |

## Review dimensions & negative verdicts
- **Problem selection/ambition 0.92**: clear original user intellectual inquiry recovered.
- **Construct separation 0.85**: drastically better than v31's 0.57; three categories now explicit, though empirical indicators per category are not fully operationalized.
- **Historical transmission integrity 0.84**: no longer treats Parnas→Martin→AGENTS.md as demonstrated lineage; real documentary series remains undone.
- **Closest prior-art distinctness 0.61**: 2026 *Position, Role or Label?* already separates instruction-label effects; 2026 *Precedent or Intent?* already tests rules and existing code at scale. A contract-aware, *source-scoped principle authority* historical synthesis might still be interesting, but not certified unique.
- **Empirical support for the claimed AI phenomenon 0.29**: still no agent trials and no prevalence estimate. Not inflated because prose improved.
- **Reader cadence/voice 0.90**: concrete examples, short sharp hinge, longer reasoning; some sections still read like a research proposal prospectus, not a story.
- **Internal plausibility of test suite 0.73**: interesting but preregistration would need treatment scripts and independently decided authority order.

## Three adversarial falsifiers
1. A source-correct OCP classification leads to rejection because the **actual high-priority maintainer policy requires OCP**. This is legitimate instruction compliance, not overreach even if the patch is functionally correct. If we cannot tell policy authority, label result UNRESOLVED.
2. A neutral “preserve old clients” instruction causes the **same** patch behavior as named OCP. Then any distinction must come from principled technical content or generic salience, not unique design-principle name authority.
3. A design principle's qualifications are **fully preserved** through teaching and repository guidance: an attractive historical 'loss' story is falsified or becomes a story about correctly scoped adaptation.

## Next bounded action
v32 is directionally stronger. Apply a **small v32→v32b textual correction** only if needed: remove one defensive line “이 연구들이 ... 끝내 주지는 않는다”, replacing it with a positive explicit unresolved target; otherwise STOP. The cleaned v32 should not embed this scorecard; keep separate. Do not convert rhetorical quality score to scientific evidence or claim a new agent discovery.
