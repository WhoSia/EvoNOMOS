# EvoNOMOS — Corrected Two-Probability Classical Chi Cochange Gate, Source-Native Negative Result

**2026-11-10 KST · VERIFIED ORIGINAL CHI V5.1.0 GIT HISTORY / 10 UNIT TESTS PASS / NO NEW CONDITIONAL SOFTWARE LAW**

## Chronology
- Original P35-P5 Go experiment (Oct 9) froze before-2020 B1 partner predictions from real old Go Chi, measured post-2020 cochanges. Its reported aggregate evaluation was already read prior to this new session.
- At [d9ccccfb](01_P35_B1_CLASSICAL_SELECTIVE_GATE_PREEXECUTION.md), first 0.5 threshold rule was sealed before our new source rerun, but **after** P35 historical aggregate results were known. Source replay [CI #42755665543](https://github.com/WhoSia/EvoNOMOS/actions/runs/42755665543) PASS: 40 original qualifying source commits / 47 seed queries, and first new threshold losses.
- The first 0.5 rule was mistakenly called Bayes-optimal in its preseal, although B1's frozen rate estimated partner cochange probability \`p_top\`, NOT any extra-file cochange \`p_any\`. After-run [scientific correction](02_SOURCE_NATIVE_HELDOUT_GATE_VERDICT_AND_BAYES_TARGET_CORRECTION.md) preserved the mistake and stated the correct equal-unit expected-loss rule.
- At [733510f2](03_CLASSICAL_TWO_PROBABILITY_GATE_PREEXECUTION.md), that corrected 2-rate rule was sealed **before implementation and second rerun**, but with FIRST threshold results known. This is **post-aggregate/post-model exploratory**, not an independent blind prospective holdout.
- Initial workflow [#42756096278](https://github.com/WhoSia/EvoNOMOS/actions/runs/42756096278) failed on an invalid synthetic unit test fixture: the fixture claimed context→mux had zero cochanges even though its constructed row contained mux+context. Only the synthetic **test fixture** changed at [eed0b6ad](https://github.com/WhoSia/EvoNOMOS/commit/eed0b6adc12f4df0ef7f155df895c002ad862dc1); code, frozen policy, original source, outcomes and metrics unchanged. Intermediate CI [#42756118337](https://github.com/WhoSia/EvoNOMOS/actions/runs/42756118337) passed the test suite. Final updated source-execution workflow [#42756138967](https://github.com/WhoSia/EvoNOMOS/actions/runs/42756138967) **SUCCESS**: pinned full Git history, 10 native Python unit tests, original source-history extraction, and upload of source-derived JSON artifacts; no GitHub Actions[bot] authored repository commits.

## Actual original PRE-2020 fitting: exact per-file counts

Original source tag \`go-chi/chi v5.1.0\` commit \`67be7d9cafdaeb4e04e887ff78d09e030ee43b00\`, same original cutoff and end date as P35-P5, with 121 pre-2020 qualifying source commits (43 multi-triad). The script rederived all original frozen \`B1SeedEvents/B1PairEvents\` exactly from original full Git history.

| Seed file | Frozen top partner | pre-2020 total seed events | partner cochange | ANY extra cochange | p_top | p_any | alert iff p_top+p_any>1 |
|---|---|---:|---:|---:|---:|---:|---|
| mux.go | tree.go | 83 | 34 | 40 | 34/83 | 40/83 | NO |
| tree.go | mux.go | 64 | 34 | 37 | 34/64 | 37/64 | YES |
| context.go | mux.go | 33 | 22 | 25 | 22/33 | 25/33 | YES |

**All three source-derived p_any ≥ p_top**, confirming conceptual distinction. The original 2020–2024 count control again recovered 40 source commits, 47 seed-queries, 13 positives, 34 singleton negatives. The corrected Bayes risk comparison with equal losses produced **exactly the same decision-by-file pattern** as the naive top-partner >0.5 gate on this particular training set.

## Actual post-2020 descriptive comparison

| Policy | alerts | positive top-partner hits | positive wrong partner | singleton false alerts | missed positives | observed equal-unit classification loss |
|---|---:|---:|---:|---:|---:|---:|
| Original always B1 | 47 | 9 | 4 | 34 | 0 | **38** |
| Earlier top-only 0.5 threshold | 26 | 6 | 2 | 18 | 5 | **25** |
| **Corrected p_top+p_any>1 source-conditional rule** | **26** | **6** | **2** | **18** | **5** | **25** |
| No-alert baseline | 0 | 0 | 0 | 0 | 13 | **13** |

At these explicitly chosen, UNMEASURED task prices, the corrected separate-probability rule remains *worse* than the do-nothing comparator. A 50%/risk-based gate cannot automatically solve covariate shift from training multi-edit incidence (43/121 commits) to heldout incidence (6/40 commits), and the related seed observations share commits. This does not prove the rule is intrinsically bad or statistically inferior on future repositories.

Even a correct-top-partner location label could miss another required file on events with 3-file edits. And **actual coediting is not proof of necessary joint modification**; original historical developer intent and functional contract evidence are not captured by path-only labels. We cannot claim this tests a real maintainer's patch.

## Exact interpretation and research action

This run **rejects two temptations**:
1. Source dependency or historical pair cochange as a universal "must edit" law.
2. A 0.5 threshold on one partner frequency as calibrated any-extra-change decision probability.

It supports the founding 0.1–0.4 research method: condition real software architecture decisions on **maintainer search capacity, demand semantics, actual source evidence, cost preference, legal rights, and accumulated client correctness** rather than assigning utility to syntax/control graphs themselves.

**Next test needed:** actual paired architecturally different and semantically equivalent Go source, genuine independent externally authored task (not known unsolved D11 copied from prior research), equal-information but independently executed maintainer policies or agents, preregistered repairs and old/new-client oracle; one learnable any-change classifier and partner ranker as strong classical comparator. The current model's negative cost result belongs in the corpus as a warning, not used as a positive law.

**Factual authority:** verified original Git history, original pre-2020 model, eight→ten source-audit unit tests, audited Github Actions logs. **No** beyond-classical model advantage, no reliable transfer to human agents, no source governance inference, no LAW-R2 promotion.
