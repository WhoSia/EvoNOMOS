# EvoNOMOS R50 — Observational Selection Bias Can Reverse Architecture Rankings

**2026-11-23 · constructed counterexample, reproducible in [R49 Python source](94_EVONOMOS_R49_CONFOUNDED_ARCHITECTURE_COMPARISON.py).** An equivalent Python 3 standard-library script was locally executed successfully with exact Fraction assertions. All task costs and architecture selection proportions below are fabricated. The familiar Simpson-type reversal is NOT a new theorem, software observation or SOLID effect.

## A causal difficulty beyond the R41 future-signal toy

Even with full historical maintenance costs, architectures were **not randomly assigned**. Teams may introduce more elaborate abstractions exactly when the future change demands are harder. Then a naive cross-repository comparison confounds architecture with anticipated severity.

### Completely constructed 2-by-2 example

Architectures B (direct editing) and X (abstraction) are stipulated to preserve all protected contracts:

| Maintenance regime | B cost | X cost | X minus B |
| --- | ---: | ---: | ---: |
| Easy | 2 | **1** | **-1** |
| Hard | 12 | **11** | **-1** |

X is strictly better within both environments. But historical teams chose X for 90% hard cases and B for only 10% hard cases. The naive averages then reverse the conclusion:

- Observed B = 0.9 × 2 + 0.1 × 12 = **3**.
- Observed X = 0.1 × 1 + 0.9 × 11 = **10**.
- A hasty engineer would call B better (3 versus 10), even though X is cheaper **for both task strata**.

Under a matched common 50/50 easy–hard task distribution:

- Matched B = (2+12)/2 = **7**.
- Matched X = (1+11)/2 = **6**.
- The apparent preference reverses; X is cheaper by one unit.

This is a **Simpson-type selection reversal** from nonrandom treatment allocation; it is no evidence of actual design performance or original causal theory.

## Competitors already know context and economics

[Owned Sullivan et al. (2001) full text](https://drive.google.com/file/d/1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr/view) explicitly extended design structure matrices with EXOGENOUS ENVIRONMENT PARAMETERS because design-only matrices cannot represent forces driving changes. The [2025 Cai et al. industrial architectural complexity study](https://research.google/pubs/understanding-architectural-complexity-maintenance-burden-and-developer-sentiment-a-large-scale-study/) reports observational correlations across 1,200+ projects and 7,200 survey responses. These are important predictive and descriptive results, but cross-sectional correlation by itself does not identify a controlled architectural intervention effect.

Thus the research target must separate:
1. **Prospective selection**: can a policy using only pre-change information choose an architecture with lower future costs?
2. **Causal architecture value**: if the same plausible future tasks are enacted on paired feasible architectural forks, how much does architecture alone change the result?

Strong prediction can coexist with wrong causal interpretation when an architecture proxies for task severity. Conversely a genuine causal architecture effect could exist yet be hard to select prospectively without informative signals.

## Upgrade to proposed R45 real-source experiment

- Never infer OCP treatment effects from naturally observed SOLID versus non-SOLID repository comparisons without handling architecture selection confounding.
- Create **matched architecture forks**, protect identical client contracts and interface behavior, and apply the same sealed future change series. Counterbalance agents/maintainers and task order.
- Keep a separately versioned timestamp cutoff for **pre-change feature extraction**; do not let post-change metrics, future tests or later developer decisions leak into a predictor.
- Compare against strong preexisting Parnas and Baldwin–Clark information hiding/modularity baseline models as well as simple slogans. Report metric vectors and negative cases.
- Label claims as predictive (source signals), causal (paired intervention), descriptive (observed associations), or semantic contract feasibility (hard constraint).
- Neither the positive controlled [Cabral et al. (2024) code-comprehension experiment](https://drive.google.com/file/d/1Jej4TkYvBj-5IXZ_FUiO62aihMK5MsRf/view) nor the [Yanakiev et al. (2025) industrial experience report](https://drive.google.com/file/d/1AgrvMjuayztaJ9yp6JtYbzeRyOOcGCG3/view) by itself measures the new target of multi-horizon future-blind maintainability selection.

## LIRA v35 implication

v35 already addresses environment, maintainer, cost horizon, hard protected contracts and source-blind future choice. Those phrases merit high subjective retain-worthiness (0.94), but a technical follow-up must explicitly separate prediction from causal effect. Add at most one short clause to a short position paper; this counterexample stays in the independent research appendix.

**Status:** LOCAL EXACT CONFOUNDED TOY PASS / ARCHITECTURE CAUSAL EFFECT UNMEASURED / REAL FUTURE MAINTENANCE OUTCOMES UNMEASURED / NEXT PAIRED-SOURCE DESIGN PROPOSED.
