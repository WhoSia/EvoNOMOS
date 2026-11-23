# Paper B R40 — v34 LIRA Red-Team: Hard Question Restored, Novelty Still Open

**2026-11-23 · source-grounded internal manuscript review.** Read original 2026-07-29 chat, P35, v33, v34 GitHub readback, R36/R39. Scores are subjective editorial recommendations or judgments, not probabilities and not an independent peer-review result.

## One-sentence main thesis
**Software design principles should be treated as context-dependent, refutable intervention hypotheses, and research should seek conditions for their usefulness and potentially better principles rather than granting the five SOLID names unconditional veto power.**

## What v34 fixes
- The core research object is now *conditional architecture inference and possible principle discovery*, not a 2026 prompt-label manipulation.
- The lexicon/axiomatization issue returns to its historically correct role as **the motivating objection and one empirical lens**.
- The possibility of a higher-order rule is stated inside the thesis, rather than placed in an appendix as an unrelated stretch goal.
- The paper openly acknowledges different sorts of principles (notably LSP semantic obligations vs the cost tradeoffs of other heuristics); it does NOT presuppose a single law.
- A short English and Korean version preserve the question, technical distinctions and one historically meaningful Martin example.

## LIRA selective sentence review
| Span (v34, bounded quotation) | Keep | Importance | Adversarial assessment |
| --- | ---: | --- | --- |
| “좋은 설계 원칙이란 무엇이며, 어느 조건에서 좋은가?” | 0.99 | CORE | Recovers first archive's conditional principle formalism and no-universal-best boundary; strong question |
| “검증 가능한 조건부 가설” | 0.98 | CORE | Anchor concept. Needs prospective measurement plan in independent research artifacts |
| “그 법칙이 어떻게 발견되거나 기각될 수 있어야 하는지” | 0.98 | CORE | Ambitious but honestly question-framed |
| “좋은 원칙을 외워도, 지금 그 원칙을 적용해야 하는지는 여전히 모르기 때문이다.” | 0.94 | HINGE | Keep short line; not generic writing-AI boilerplate |
| “같은 추상화가 불필요한 우회를 늘릴 수도 있다.” | 0.88 | CONTRAST | Hypothetical counter-world is a thought experiment, not observed data |
| “보호할 기존 계약” | 0.97 | CONSTRAINT | Structural feasibility before optimizations; accurate boundary |
| “LSP의 행동적 계약을 ... 단기간 수정 비용 ...” | 0.97 | COUNTEREXAMPLE | Protects the proposal from reducing all principles to scalar cost |
| “기존 원칙이 설명하는 유리함과 불리함을 비교한다.” | 0.86 | RESEARCH OPERATION | Procedural but necessary for falsifiable framing; avoid more steps in short manuscript |
| “SOLID라는 이름을 미리 정답으로 지정하지 않은 채 ... 재조합” | 0.99 | ORIGINAL PROGRAM | Reconnects with archive 0.4 principle induction; do not demote |
| “더 나은 원칙을 배울 수 있는가” | 0.99 | ORIGINAL PROGRAM | Crucial difference from judging instruction compliance |
| “그 구별을 찾는 과정 자체가 연구가 된다.” | 0.76 | SUPPORT | Mildly self-justifying sentence; optional deletion for concision |
| “원칙이 오랫동안 살아남았다는 사실은 존중할 이유다. 그 원칙을 시험하지 않아도 된다는 이유는 아니다.” | 0.98 | ENDING | Characteristic natural ending, protects authorial voice |
| “Learning the rule does not tell us whether this is the moment to use it.” | 0.96 | EN HINGE | English counterpart with natural cadence |
| “It asks what it would take to discover—or reject—one.” | 0.96 | EN CORE | Makes both risk and ambition clear |

## Hard objections, not euphemisms

**O1—Classical pre-emption, serious.** The general insight that architecture choice depends on expected change, requirements, maintainers and utility already belongs to modular design, economics of software evolution, requirements and decision theory. *Proposing a general conditional-principle research programme is a synthesis, not yet an established novel theory*. The publication-worthy unit must be made specific: a falsifiable central conjecture, a research design with real discriminating counterexamples, or an original selection/induction method. v34 raises the right hard question but still lacks that one narrow substantive technical differentiator.

**O2—Not enough operational contrast.** “If many types change prefer extension / if shared workflow changes maybe not” is intuitive. For scientific progress, specify prospective observable conditions **before** knowing the next change, rather than retrofitting the explanation after a result. Study must test whether a genuinely predicted boundary choice outperforms a matched alternative across future changes and permitted contracts.

**O3—"Superior law" may be a category error.** LSP can be a semantic invariant while SRP/OCP/DIP often supply heuristic architecture choices. A shared *decision procedure* might subsume several questions without being a single law that proves all five. Better to distinguish (a) higher-order structure, (b) policy choosing among heuristics, (c) new normative rule, (d) empirical causal effect.

**O4—Risk of conflating two papers.** User's Paper B historically began as history and epistemology of quasi-axiomatization, while EvoNOMOS program sought architectural principle induction. A concise position paper may connect these but must avoid claiming to be a completed full EvoNOMOS technical paper. v34 is a research manifesto in the best sense; claim that scope explicitly.

**O5—Agent novelty not guaranteed.** AI instruction compliance and repository precedent have very close prior art (both user-provided original Oct 2026 PDFs). If actual agent experiment only varies rule adjectives, it does not answer the architecture discovery question. Future independent studies must measure design choices/costs over changing tasks, not exclusively prompt text.

## Priorities for the next research iteration
- **Theoretical challenge (0.94):** derive a concrete, prospective falsifier of a candidate higher-order relation, including the LSP irreducibility case. Use old EvoNOMOS conditional policy certificate where helpful rather than quietly reinventing it.
- **Source fidelity (0.93):** return to Martin original text and distinguish strategic closure from later SOLID acronym history.
- **Live evaluation (0.61 readiness):** stage bounded paired architecture comparisons with legitimate contracts and varying change horizons; do not claim executor-independent generality.
- **Main paper compression (0.91):** preserve the 4-section clean bilingual position and the short ending. Additional technical caveats belong here, not in every sentence.

## Decision
v34 is recommended over v33 as the current author-review narrative because it better reflects the original source, **not because its scientific novelty is proven**. Do not produce v35 without a meaningful new result or a substantive author-requested change. Main unmet issue: what new structure could be both **nontrivially predictive** and **distinguishable from existing conditional engineering judgment**?

**State:** FOUNDING THESIS RESTORED / LIRA SECOND PASS COMPLETE / NOVELTY OPEN / LIVE AGENT AND PRINCIPLE DISCOVERY UNRUN / LAW-R2 HOLD.
