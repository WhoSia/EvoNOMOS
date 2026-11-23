# EvoNOMOS R42 — Prospective Selection Gate: Exact Toy and Classical Novelty Counterexamples

**2026-11-23 · one fresh reproducible *constructed* finite probability experiment, not a real repo, human maintenance trial, LLM agent experiment or discovery of a new law.** Exact-reference implementation: [R41 source](86_EVONOMOS_R41_PROSPECTIVE_SELECTOR_TOY.py). A Python 3 standard-library equivalent was executed locally (all embedded assertions passed; Fraction arithmetic avoids Monte Carlo sampling error). The repository script was then committed. Interpret results **only** under the declared fabricated costs and stationarity assumptions.

## The harder research question
*Can a selector choose an architectural boundary before future changes occur using only legitimate pre-change signals, and can we identify when its advantage disappears?*

This is more specific and testable than “good design depends on context,” but it is emphatically **NOT** a previously unknown insight that expected costs or option values exist.

### Severe classical competitor
- David Parnas (1972), [modularization criteria](https://doi.org/10.1145/361598.361623), recommends encapsulating difficult / likely-to-change design decisions. The idea of choosing boundaries with anticipated change is **54 years old**.
- Carliss Y. Baldwin & Kim B. Clark (2000), [*Design Rules, Vol. 1: The Power of Modularity*](https://doi.org/10.7551/MITPRESS/2366.001.0001), modeled modularity and design options under uncertainty; their [2002 specific option-value example](https://scholarsarchive.byu.edu/facpub/8944/) accounts for the value of module-level alternatives less the cost of adopting modular architecture. Therefore an "expected change / modularity option-value" formula is **not a novel EvoNOMOS discovery**.
- [Sullivan, Griswold, Cai & Hallen (2001) work noted in modularity valuation literature](https://www.sciencedirect.com/science/article/pii/S1044028307000233) applied options models to software. Secondary contextual source only in this pass, not original 2001 source full-text reviewed.
- [2025 IEEE architectural change prediction study](https://xplorestaging.ieee.org/document/11077764) directly investigates just-in-time architecture prediction. Title/abstract evidence only; full article not independently inspected here. Must be fully compared before firstness claims.

**Residual research ambition:** prospectively infer *which conditions can be observed ahead of future maintenance*, whether an approach withstands distribution shift and is valuable in real source-code interventions, and whether a reusable rule is recoverable from data **without feeding SOLID names as labels**. Even that proposal may already have close prior art; no global firstness claim.

## Fully declared toy
- Architecture `B`: build/setup 0, a future *new variant* modification costs 6 arbitrary units, a future *shared-workflow* modification costs 1.
- Architecture `X`: build/setup 12, a future *new variant* modification costs 1, a future *shared-workflow* modification costs 4.
- All alternatives are stipulated to satisfy the protected functional contract; semantics, concurrency and real maintainability are intentionally **not simulated**. In a realistic experiment, contract violations must render an alternative infeasible before cost comparisons.
- Future horizon `H ∈ {6,12,24}`; each future task is independently new-variant with probability `p` and shared-workflow otherwise.
- Unobserved regime before choice: `p_L=1/4` or `p_H=3/4`, each with probability `1/2`. The selector knows the two candidates and prior but not which applies to future tasks.
- **Only observable advance signal:** count of new-variant changes in `n=6` past requests. Under stable control signal tasks are iid from the *same* p as the future. Under distribution-shift negative control signal tasks are iid from the *opposite* regime (unannounced to the policy).
- Bayesian (not novel) inference of `p` from signal count `k`, followed by choosing lower expected future cost. At equal costs choose `B` as a deterministic fallback and mark a tie (for `H=12, k=3`, this is a **flag**, not actual source-code abstention).
- Evaluator averages future costs over p worlds, signal randomness and future tasks. The exact enumerator sums all binomial counts with Python `Fraction` and asserts normalization and crossover. No reward was tuned to unseen test sequences or real measurements.

### Derivation, not a new theorem
For H tasks and prevalence p:
```text
E[Cost(B)|p,H] = H (1 + 5p)
E[Cost(X)|p,H] = 12 + H (4 - 3p)
X is lower-cost iff p > (3H + 12)/(8H)
```
At `H=12` the crossover is `p=1/2`. Given the preceding six requests and equal prior p-regime weights, the posterior expected p exceeds 1/2 iff the observed count `k>=4`; at `k=3` expected costs tie. A posterior is a **model assumption-dependent inference**, not a measured probability that the future will behave that way.

### Exact executed outputs
| Horizon H | Signal condition | Always B | Always X | Oracle with forbidden future-regime knowledge | Advance-signal selector | Selector gain versus best constant |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 6 | stable | 21.000000 | 27.000000 | 18.000000 | **18.846680** | +2.153320 |
| 6 | opposite-regime shift | 21.000000 | 27.000000 | 18.000000 | **28.362305** | -7.362305 |
| 12 | stable | 42.000000 | 42.000000 | 30.000000 | **32.484375** | +9.515625 |
| 12 | opposite-regime shift | 42.000000 | 42.000000 | 30.000000 | **51.515625** | -9.515625 |
| 24 | stable | 84.000000 | 72.000000 | 54.000000 | **58.177734** | +13.822266 |
| 24 | opposite-regime shift | 84.000000 | 72.000000 | 54.000000 | **96.240234** | -24.240234 |

At `H=12` the `k=3` tie flag occurs with exact probability `135/1024=13.18359375%` in the stipulated stable mixture; during a tie the script selects baseline B as a deterministic *action*, so do not report the tie flag as a literal agent abstention.

### What this toy can and cannot support
**Supports:** A complete prospective prediction procedure can be constructed without peeking at future samples; a single fixed always-use-B or always-use-X policy need not minimize expected costs under a stable informative signal; the same prospectively frozen policy may **lose** to both fixed policies when the signal/future relationship reverses; a preselected horizon affects the decision threshold. Exact numerical results are conditional on our arbitrary, manufactured cost/world assumptions and are algebraically expected.

**Does not support:** that SOLID principles were empirically shown inferior/superior, that we invented Bayesian architecture choice or modularity option value, that AI agents make or revise such choices, that maintenance costs are actually 1/4/6/12 units, that a universal upper-level structure exists, or that the distribution of real future requests can be learned from six past tasks.

## Design a real discriminating benchmark, do not backfit it
1. Preselect several real repositories, baseline implementation and behaviorally equivalent architecture alternatives; document why comparison is feasible, including protected legacy contracts. Avoid leaking tomorrow's test tasks into feature extraction.
2. Define a pre-change **signal capture cutoff**. Only dated historical requests before cutoff may feed architecture selector features; reserve later tasks as a sealed prospective test.
3. Freeze architectures, selector, baseline heuristics and cost/feasibility evaluators before running future changes. At minimum include direct-fix baseline, conventional architecture experts and standard change-prediction heuristics; **Baldwin–Clark / Parnas-conditioned benchmark baselines**, not merely fixed SOLID slogans.
4. Distinguish observational policy evaluation from causal intervention: independent execution of comparable task sequences on paired architectural forks is needed to estimate differences; account for shared developer/agent effects and order/carryover.
5. Report vector outcomes, not just dollars or tokens: semantic correctness/contract feasibility, regression failures, human reviews, number of edited files, semantic propagation, time and tool/tokens. Treat protected contracts as hard constraints.
6. Test explicit nonstationarity (changes in product direction), unknown p, weak signals, open-world change types, model/harness variation and out-of-domain repositories. Do not make an abstention claim without a real deferral/review protocol and cost.
7. Only say a *discovered* principle is new if it predicts beyond original conditional modularity/real-options theory, survives cases purposely chosen to favor competitors, and identifies the domain where it should NOT apply.

## Epistemic status
- The historical antecedents above are existing scholarly claims with linked sources.
- The toy model and its exact output are this iteration's genuinely **executed constructed calculation**.
- Real repository performance, agent data, generalization and a distinctive new law are still **unmeasured**.
- Previous initial July 29 0.1 artifact already contained formal conditional policies and synthetic tests. This is a **new, simpler prospective test fixture**, not a claim that the first-ever EvoNOMOS formalization occurred now.

**Gate:** ACCEPT as reproducible toy + severe negative control / HOLD any real-world empirical or originality claim. No pressure to expand Paper B with equations; one bounded example sentence suffices if it sharpens the thesis.
