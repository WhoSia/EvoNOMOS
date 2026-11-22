# EvoNOMOS R43 — No-Information Boundary, Exact Falsifier and Research Synthesis

2026-11-23 · completed a third, **independent-signal** negative control for the prospective toy, following the stable and inverted-signal analyses in [R42](87_EVONOMOS_R42_EXACT_PROSPECTIVE_DECISION_GATE_AND_PRIOR_ART.md). Exact executable Python updated and rerun locally, all assertions passed: [R41 runnable source](86_EVONOMOS_R41_PROSPECTIVE_SELECTOR_TOY.py). All costs, probabilities and signal-world mapping are **researcher-created**, not measured on real repositories.

## Important independent information negative control

Construct future regime `W ∈ {p=1/4,p=3/4}` as before. Supply the architecture selector six nominally historical change samples but let them be Bernoulli(`1/2`) **independently of W**. The selector is not told and continues to use its stationary two-regime posterior rule. For `H=12` the exact expected prospective-selector cost is **42**, equal to each always-use-one-architecture baseline **42** and worse than the unrealizable perfect-regime oracle **30**. Signal value is zero in expectation. For other horizons the uninformed selector can actually degrade relative to the best fixed baseline (H=6: 23.0625 vs B=21; H=24: 76.125 vs X=72).

Three entirely distinct cases must be kept separate:
| H | Signal relation to future | Always B | Always X | Selected | Gain relative to best constant |
| --- | --- | ---: | ---: | ---: | ---: |
| 6 | stable same-regime | 21 | 27 | 18.8466796875 | +2.1533203125 |
| 6 | independent | 21 | 27 | 23.0625 | -2.0625 |
| 6 | inverted | 21 | 27 | 28.3623046875 | -7.3623046875 |
| 12 | stable same-regime | 42 | 42 | **32.484375** | +9.515625 |
| 12 | independent | 42 | 42 | **42** | 0 |
| 12 | inverted | 42 | 42 | **51.515625** | -9.515625 |
| 24 | stable same-regime | 84 | 72 | 58.177734375 | +13.822265625 |
| 24 | independent | 84 | 72 | 76.125 | -4.125 |
| 24 | inverted | 84 | 72 | 96.240234375 | -24.240234375 |

The script models ties as a choice of B with an advisory tie flag; no actual run-time agent abstention happened.

## Elementary information-boundary statement (known decision-theoretic reasoning, NOT our original theorem)

Let `W` index the future scenario, `S` be the pre-change signal, `A={B,X}` an action set and `C(a,W)` an action/scenario cost with no other information hidden in S. Assume:
1. `S` is **independent of W** (no predictive relationship), and
2. `C(a,W)` is not itself additionally altered by `S` except through action choice.
Then for any signal-only policy `π(S)` (possibly randomized), writing `q=P(π(S)=B)`:
```text
E[C(π(S),W)] = q E[C(B,W)] + (1-q) E[C(X,W)]
              >= min(E[C(B,W)], E[C(X,W)]).
```
This is simply a convex combination of fixed-policy risks. It **does not** claim a new information theorem. It gives a useful gate: *without prospective information, a signal-based selector cannot outperform the best fixed architecture ex ante in the stipulated setting*. Hidden authorization, actions that alter the scenario, adaptive changing contracts and selection costs demand additional modeling.

**Falsifier of a cheap design-rule claim:** If an "EvoNOMOS predictor" claims an improvement when the task-signals are independently shuffled, check for future leakage, policy adaptation, evaluator bias or mismatched test tasks. The toy demonstrates one clean case with no improvement, not universal validity of shuffling.

## Connections to earlier project results, not erased

An uploaded prior EvoNOMOS R11-P1 project record describes **real native Go executions** against historical gRPC/Milvus/BuildKit/SpiceDB source slices and **bounded source-composition** conditions, alongside a 256-case finite model check. These are a different research track from current conditional architectural choice. They establish that the project previously ran source-level tests, so it would be wrong to say *EvoNOMOS never executed source tests*. The correct statement is: **this 2026-11-23 Paper B prospective selector is a synthetic exact calculation, and no new live architecture-change sequence or SOLID-prompt agent trial was executed in this iteration**. Source-specific historic Go claims still require direct canonical run log/diff reinspection before being used as evidence in a new paper.

Classical novelty hazards persist: Parnas 1972 prefigured likely-changing module boundaries; Baldwin & Clark 2000/2002 modeled modularity's value under uncertainty. Earlier EvoNOMOS Archive 1 already formulated conditional policies and synthetic no-universal-best results. Do not pass off the convex-mixture inequality or toy Bayesian selection as unprecedented mathematical discovery.

## Next discriminating objective
Design a **future-blind real repository comparator** in which historical change signals are timestamped and frozen, competing architectural interventions are contract-preserving, outcomes use held-out future changes, and the planned selector must beat a matched Parnas/Baldwin–Clark-type baseline rather than only arbitrary always-OCP/never-OCP rules. If it fails under shift, explicitly specify the shift-detection/deferral policy and its real cost before claiming robustness.

**Gate:** SYNTHETIC EXACT GATE PASS / THREE SIGNAL CONDITIONS EXECUTED / NO SOURCE-LEVEL ARCHITECTURE EFFECT / NOVEL THEORY CLAIM HELD.
