# EvoNOMOS R36 — A Possible Higher-Order Structure Behind SOLID: Independent Conjecture Ledger

**2026-11-23 · Independent research lane B (foundational structural hypothesis).** This is intentionally NOT the Paper B thesis, a proved theorem, an achieved universal design law, or a measured causal result.

## Original user aspiration, verified in Archive 1
The [first EvoNOMOS archive, 2026-07-29](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view) identifies two related but distinct aims:
1. Reject uncritical treatment of SOLID as automatic binding rules or formal axioms; restore conditional, revisable epistemic status.
2. Go beyond evaluating existing names: decompose architecture interventions, search for combinations, distinguish different change objectives and repository situations, and (if evidence warrants) discover more general **conditional structural principles**. Older reports in the archive had synthetic and limited-source work, not accepted universally valid laws.

The current user explicitly asked to preserve the second as an ambitious longer research direction **without stretching the concise Paper B**.

## Candidate underlying structure: preservation under change

Take a software state `S`, a possible requested change `Δ`, a set of **protected observations** `C`, a future-change distribution `P(Δ | context)`, an evaluation horizon `H`, legitimate agent/developer constraints `A`, and a cost vector `K` (implementation, regression, coordination, review, token/tool, long-term maintenance) with utility weighting `U`. Candidate structural study:

> Among behaviorally permitted architectures, how should an extension boundary and dependency structure be chosen to preserve protected observations over plausible changes while trading off immediate and future costs, given the actual humans/tools that will maintain the program?

This **could** organize some existing principles as task-conditioned special cases. It is a research hypothesis or *design decision problem*, not a new theorem. Its mathematical ingredients overlap established software evolution, requirements engineering, causal decision theory, modularity and multiobjective optimization; novelty, if any, must come from a specific identified relation and independently observed prediction beyond those theories.

### Hypothesis library, not a confirmed reduction
| Principle | Possible projection onto change/preservation problem | Crucial competing interpretation/counterexample |
| --- | --- | --- |
| SRP | Group responsibilities by correlated reasons to change so change propagation is localized | A reason to change may be organizationally defined and not identifiable from code diffs; correlated co-change can favor grouping, not separation |
| OCP | Place stable abstraction boundaries at genuinely expected extension points | Wrong extension taxonomy leads to over-engineering; one-off variation favors direct changes |
| LSP | Preserve substitutability of derived instances where clients' behavioral contracts matter | **Behavioral substitutability is a semantic correctness condition, not reducible to edit cost**; any 'unification' that loses this is inadequate |
| ISP | Limit forced client dependence on operations they do not use under realistic interface churn | Too many small interfaces increase coordination, discovery and testing burden |
| DIP | Stabilize dependencies around change-sensitive boundaries and replaceable providers | Higher abstraction setup cost or unstable protocol can make direct concrete coupling preferable |

**Risk:** This table is *our conjectural interpretation*, not a faithful formal translation of all five original primary texts; must not say "all SOLID reduce to one formula" without derivation and disconfirming cases. Architecture may have many incomparable quality axes (security, timing, performance, privacy, ergonomic clarity, semantics) that a single scalar 'maintainability' cannot capture.

## Discriminating thought experiments

**T1 Expected change flips.** Identical current feature tests, two maintenance forecast worlds: next 30 tasks vary extension kinds vs next 30 tasks mainly modify shared behavior. Would OCP extension boundary be preferred in the first and centralized edit preferred in the second? Prediction conditional; if all design rankings robustly unchanged, horizon-based account is weakened.

**T2 Protect legacy behavior.** Same code patch, current demand and two protected contract regimes. We already own an *author-constructed* finite demonstration (book prefix) where verdict differs. But this tells nothing about agent language effects and does not prove a universal principle.

**T3 Cross-paradigm counterexample.** Functional data-oriented solution can preserve change separation without class inheritance, and inheritance can satisfy superficial OCP syntax while violating behavioral substitution. If the 'higher-order principle' only rewards OOP style, it fails to be a genuine unifying structural account.

**T4 Short vs long horizon.** An adapter/setup cost may dominate at H=1; repeated replacements may amortize at large H. One 'SOLID best' benchmark at one horizon cannot settle principle validity across both. The crossover point itself depends on empirical task, maintainer and system properties.

**T5 Maintainer & agent differences.** A micro-boundary may help an experienced maintainer but increase search/tool-token cost for a naïve coding agent; cost metric and executor must be separated.

**T6 LSP objection.** Even zero-change programs can have substitutions violating client contracts; pure propagation-cost reduction misses the principal concern. Either the higher-order theory includes semantic invariants *independently* or acknowledges that the SOLID cluster spans multiple irreducible axes.

## Three independent next research tracks (not claims of execution)
- **Foundations:** Compare this structure with information hiding, behavioral subtyping, family-based variability and existing architecture decision/maintenance cost theory. Aim for an explicit counterexample before proposing an elegant law.
- **Causal architecture test:** Freeze requirements, permitted client observations and maintainer/tool profiles; compare paired architectures under random task change sequences and multiple horizons. Report cost vectors and non-dominance; no promise of a universal winner.
- **Principle induction:** Compose structural features without using SOLID labels during search, then test whether any learned context-dependent policies resemble SRP/OCP/ISP/DIP/LSP (or counterexamples), using truly out-of-domain repositories and independently checked bounded contracts.

## Strongest adversarial judgment
The attractive story that five SOLID rules are shadows of a hidden single equation can be **false**. LSP concerns semantic substitutability; other rules are design heuristics of cost, complexity or expected changes. A scientifically productive question is whether **some** share a common conditional structure and **which** fail to reduce. Forcing the theory to accept every classic principle would recreate the dogmatism EvoNOMOS questions.

## Paper B embedding rule
Paper B may use **one or two sentences** in its conclusion to invite exploration of higher-order conditional architecture structures, explicitly saying these have not been discovered. All six thought experiments, risks and tests stay in this separate lane.

**Status:** POSSIBLE HIGHER-ORDER FRAMEWORK / HISTORICAL PRIOR ART STILL TO BE COMPARED / NO PROVED UNIFICATION / NO NEW ARCHITECTURE BENCHMARK EXECUTED.
