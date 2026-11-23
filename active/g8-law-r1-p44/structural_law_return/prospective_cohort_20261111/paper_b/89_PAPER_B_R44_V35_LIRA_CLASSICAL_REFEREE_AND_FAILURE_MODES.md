# Paper B R44 — LIRA v35: Cold Reader, Source Reviewer and Falsifier

**2026-11-23 · independent reread of v35 GitHub blob `3fdffbda3d4cfabc3f4690faf020ce9a7088ed30`.** This is a single assistant's sequential internal roles, NOT multiple independent experts. 0–1 scores below are subjective *editorial preference to retain the wording*, except explicitly named scholarly-dimension ratings. Evidence and writing quality are different axes.

## One-sentence extract

*What would justify choosing or discovering a structural principle **before** its purported benefit is known, and how can that principle be tested against protected contracts, future task changes, and credible alternatives?*

This represents the original EvoNOMOS 2026-07-29 aim substantially better than v33's exclusively SOLID lexical-veto framing.

## The editorial parts worth keeping

| Unit | Bounded actual v35 expression | Score | Why |
| --- | --- | ---: | --- |
| K-QUESTION | “좋은 설계 원칙이란 무엇이며, 어느 조건에서 좋은가?” | **0.99** | Founding epistemic task, accessible to an intelligent reader |
| K-CONDITION | “적용 범위와 반례를 갖는 검증 가능한 조건부 가설” | 0.98 | Defeasible principle programme |
| K-MARTIN | “전략적 닫힘 ... 앞으로 무엇이 바뀔 것인지에 따라” | 0.93 | Historically grounded first scene; source not identical to hypothetical synthetic reports |
| K-COUNTER | “원칙 사이에 우열을 매기기 전에, 무엇이 선택 가능한 설계인지부터 가려야 한다.” | 0.98 | Protected contracts are hard constraints, particularly relevant to LSP |
| K-TOY-1 | “과거 여섯 요청이 ... 42에서 32.48” | 0.89 | Novel to this **toy execution**, accurately conditional; risk of seeming empirical without '인공 모형' immediately nearby |
| K-TOY-2 | “과거 신호가 미래와 무관해지면 이점은 사라졌고 ... 51.52” | 0.95 | Real negative control and a useful nonstationarity warning |
| K-PROSPECT | “어떤 구조를 선택할지 결정하는 규칙과 사용할 정보는 변경 결과를 보기 전에 고정한다.” | 0.99 | Exactly what v34 lacked; central possible experimental contribution |
| K-PRIOR | “Parnas ... Baldwin–Clark ... 이미 변화 가능성과 ... 비용” | 0.95 | Makes older work a worthy comparator rather than a decorative citation |
| K-DISCOVERY | “SOLID라는 이름을 미리 정답으로 지정하지 않은 채 ... 조건부 설계 가설” | 0.99 | Protect the original ambition to *induce* principles |
| K-UNIQUE | “새로운 기여 ... 미래를 보지 않고도 ... 원칙 발견의 방법” | 0.86 | Aspirational; prospective methods also have prior art. Avoid implying ours already surpasses Parnas/real options |
| K-ENDING | “원칙이 오랫동안 살아남았다는 사실은 존중할 이유다. 그 원칙을 시험하지 않아도 된다는 이유는 아니다.” | 0.99 | A human conclusion, keep original shape |
| E-CROSSOVER | “The next question must be answered *before* future changes arrive.” | 0.96 | Effective natural rhythm, independent of Korean word order |
| E-DISCLAIMER | “These are exact calculations under invented costs...” | 0.90 | Necessary once numbers enter a short position paper |
| E-CLASSIC | “Parnas's work ... Baldwin and Clark's real-options ...” | 0.95 | A direct novelty ceiling |
| E-ADVANCE | “the information it can use *before* exposing it to the future tasks” | 0.97 | Proper temporal evaluation boundary |

## Internal reviewer hostility

### 1. Historical/software economics referee: dangerous competition
Baldwin & Clark (2000/2002) already model modularity, uncertainty, experiments and architectural investment. The Bayesian selector and convex-combination impossibility inequality are *elementary existing decision theory*. To use words like **new method** as a completed contribution would be misleading. A distinct paper would have to demonstrate a new, source-specific, generalizable architecture selection or induction result not implied by those models. Current v35 says 'could'; acceptable for a **position** essay only.

### 2. Causal empirical researcher: the principal defect
The toy's `p_L=0.25, p_H=0.75` and training signal model were **assumed**. The observed past six requests don't prove future stationarity; the posterior rule was Bayes-optimal within a deliberately easy two-regime class. It is not a learned predictor of real software changes. Under independent signals at `H=12`, expected cost exactly equals the fixed baseline (42); under inverted signals 51.52 is worse. The meaningful empirical design task is identifying useful *pre-change observable features* and protecting a held-out task sequence. A real experiment also needs edit authorization and semantic-contract feasibility.

### 3. Axiomatization historian: the core link
The founding complaint was ‘원칙 vs 규칙 vs 공리’: how a mnemonic can become over-authoritative for AI/reviewers. v35 correctly makes this the **motivation**, not a claim of a proven historical trend. It still owes careful evidence about teaching, explicit team policies and the internal conditions of Martin's strategic closure. LSP is heterogeneous, so “SOLID = five similar cost heuristics” remains wrong.

### 4. Scientific novelty examiner: uncomfortable verdict
A credible *problem synthesis* is not yet the same as a distinct technical discovery. Best prospective distinction would require (i) a decision variable available before future changes, (ii) contract-preserving architecture alternatives, (iii) comparable classical predictors and real-options baselines, (iv) measured out-of-domain improvement and explicit failure regimes. v35 mostly makes a high-quality **invitation**.

### 5. Literary editor: natural but overloaded
v35 kept v34's compact 4-section rhythm, but the detailed constructed numbers make §2 heavier. Acceptable if visible in a short paper as a method miniature, yet a version without figures may be preferable for some author audiences. Do not force every paragraph to the same sentence count. Preserve one-line punch and don't invent imperfections to hide AI origin.

## Dimension judgments (not the same as the unit keep-scores)

| Lens | Subjective rating | Explanation |
| --- | ---: | --- |
| Fidelity to first-chat ambition | **0.95** | Conditional policy and principle induction both central |
| Rhetorical clarity | **0.91** | Concrete Martin and toy scenes, explicit true ambition |
| Falsifiability of proposed **research gate** | **0.85** | Source-independent negative controls and future-blind selection clarified |
| Specificity beyond known classical theory | **0.56** | Baldwin–Clark, Parnas and prediction methods compete |
| Observed real-world design benefit | **0.28** | No source-level architecture trials in v35; earlier R11 real Go tests are a different track |
| Compactness for an invitation paper | **0.82** | New toy gives substance but potentially excessive quantitative detail |

## Criteria for legitimate next advancement
1. Do **not** call the exact toy a discovery of a new law.
2. Freeze **pre-change** signals before selection and real future tasks; test across different maintainers/horizons.
3. Compare the resulting policy to a smart baseline based on Parnas/real options as well as always-SOLID and never-SOLID.
4. Run actual contract-preserving source edits and evaluate outcome vectors; do not confuse synthetic unit costs with real human/time/tool costs.
5. Search for a falsifiable structural feature that could not simply be renamed expected change probability or modularity.
6. Stop cosmetic rewrites until one of these substantive gates advances; LIRA should protect good language.

**Review verdict:** v35 is a substantive improvement in *method specificity and intellectual integrity*, not yet an academic-priority certificate or demonstrated new policy. The toy is useful because its adversarial controls fail in intelligible ways.
