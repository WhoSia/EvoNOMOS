# P31 — An Observational Sieve for Conditional SOLID Projections

**Type:** P31 mathematical working note / elementary internal theorem plus source-checked counterexample; NOT a newly discovered deep theorem, not a structural law, no LAW-R2 authority. Origin: *causal discovery of context-conditional software design principles*. Previous P26/P27 already established finite-intervention quotients, non-nested rival mechanisms and typed kernel orientation. This document extends the **question**, not the P27 empirical claim.

## 0. Non-isomorphism warning

A SOLID label is a natural-language design heuristic, not yet a mathematical object with specified operations. Therefore `concrete OO architecture ≅ SOLID` is presently **ill-typed**. There is no canonical inner product, so "orthogonal projection" is likewise unjustified. The natural first candidate is a **partial quotient / policy factorization**, not an isomorphism.

The distinction between an abstraction and its concrete program semantics has major prior art: Cousot & Cousot (1977), *Abstract Interpretation*, existing Drive PDF `1hZfipMMYFSwpOVx4ZuhAIvkzt4jDptIl`; preservation of contextual equivalence appears in fully abstract compilation, e.g. Abate, Busi & Tsampas (2020/2021), Drive `1Z2jDJclMhLjV-UKFx58Ct2EL16LGfyda`; design-rule DSM/real options prior art exists in Sullivan, Griswold, Cai & Hallen (2001), Drive `1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr`. None of the factorization lemmas below constitute research novelty by themselves.

## 1. Typed empirical decision object

Fix a **finite, predeclared** set X of admissible demand×environment×lifecycle contexts and a finite, fixed family A of candidate OO structural interventions. Each a∈A is run against the **same complete functional oracle** for x, giving a feasibility predicate `Q(a,x)` and a **non-scalarized** cost vector `c(a,x)=(S,L,C,A_cost)`; avoid notation confusion between architecture set A and A_cost.

Let `F(x)={a∈A | Q(a,x)=PASS}`. Among feasible interventions define the Pareto set

`P(x)={a∈F(x) | there is no b∈F(x) with c(b,x)≤c(a,x) in every coordinate and < in at least one}`.

This is a **choice correspondence**, not a numerical universal design quality. If F(x) is empty, the output is an explicit `INFEASIBLE` state, not an arbitrary maxim.

A proposed short design principle (or "SOLID projection") is an abstraction `α:X→Z`: e.g. `"introduce shared membership boundary"`, intentionally omitting many observed contexts. We ask **when any policy derived solely from α can retain the exact admissible Pareto choices**.

## 2. Theorem A — exact frontier factorization iff fiber invariance

There exists `p:α(X)→𝒫(A)` with `P=p∘α` **if and only if**
`∀x,y∈X: α(x)=α(y) ⇒ P(x)=P(y)`.

**Proof.** (⇒) If α(x)=α(y), then `P(x)=p(α(x))=p(α(y))=P(y)`. (⇐) Define `p(z)=P(x)` using any `x∈α⁻¹(z)`; fiber invariance guarantees independence of representative. Unique on α(X). □

This criterion is a *mathematical obstruction test* for a lossless human maxim; it is NOT an empirical claim that any SOLID rule passes it.

## 3. Theorem B — coarsest data-supported repair (the sieve)

Define `α*(x)=(α(x),P(x))`. Then α* refines α, `P` factors through α*, and **every refinement β of α through which P factors must refine α***.

**Proof.** `α*(x)=α*(y)` iff both α(x)=α(y) and P(x)=P(y). Hence its equality relation is `ker α ∩ ker P`. A refinement β with `α=f∘β` and `P=g∘β` has `ker β⊆ker α∩ker P`, so it refines α*. □

**Interpretation:** "sieving" means splitting abstract context classes only where an *observed* outcome contradicts compression. However α*(x) explicitly includes observed outcomes, so it is **an after-the-fact diagnostic partition, NOT a prospective predictor**. The scientific challenge is finding a *source-before-outcome* coordinate h(x) (change obligation pattern, semantic invariant, lifecycle stage, etc.) that predicts these splits on new, held-out demands. Do not leak P into a future feature.

## 4. Theorem C — sound fixed recommendation is weaker than lossless compression

A selector `r:α(X)→A` satisfying `r(α(x))∈P(x)` for all x exists **iff** every observed fiber has nonempty intersection:

`∀z∈α(X), ∩_{x∈α⁻¹(z)}P(x) ≠ ∅`.

**Proof.** A valid selector must lie in every P(x) in its fiber, hence the intersection. Conversely choose any element of each nonempty intersection (finite sets) and obtain r. □

**Crucial caution:** Failure of Theorem A does not imply that *no useful stable maxim exists*. A useful fixed action may survive even though it loses information about alternatives and tradeoffs. Conversely a named action may be safe only on a restricted part of the context domain. This prevents exaggerating a local Pareto shift as "SOLID falsified".

## 5. Source-backed P3 illustration (NOT a new experimental law)

Read the actual repository evidence `active/g8-law-r1-p3/P3_TERMINAL_SEAL.json` (Uptime Kuma demands #7316 and #7559). `S,L,C,A_cost` values:

| Observed context | DISPERSED | DUAL_RUNTIME_MEMBERSHIP_REGISTRY | Pareto frontier |
| --- | --- | --- | --- |
| phase 0, Q=1 for both | (5,22,0,0) | (2,36,0,3) | {DISPERSED, DUAL} |
| phase 1, Q=1 for both | (5,80,0,0) | (2,75,0,0) | {DUAL} |

Both Q flags are **bounded-no-network**, not production service equivalence. No scalar tradeoff weights.

Take the deliberately coarse α mapping both rows to one label `"membership-boundary design problem"`. Exact Pareto-frontier compression FAILS: `P(phase0)≠P(phase1)`. The minimum *observed* refinement adds the phase label. Nevertheless DUAL belongs to both frontiers, so a constant selector DUAL is **possible**; no claim that it is globally best, or that this selector is future-safe. This example is a **mathematical reinterpretation of P3 evidence**, not a separate randomized architectural treatment.

The earlier LawKit L-only `14-5n` extension is a sensitivity calculation under unverified repeated savings, not a theorem of context transport. It should **not** be used as a proof of three-demand payback, nor should it collapse A_cost into L.

## 6. Theorem D — finite source contact cannot entail universal projection

Suppose X_seen is a proper subset of a wider context universe X_all and no unobserved-context structural restriction is assumed. For two different actions a,b, one can construct two extensions of P agreeing on all X_seen but giving different Pareto frontiers on one fresh x_new. Hence the observed sieve alone cannot prove a universal fixed SOLID principle or identify a unique hidden architectural structure.

**Proof.** Keep P fixed on X_seen. Define extension E1 with `P(x_new)={a}`; define extension E2 with `P(x_new)={b}`. They agree with all old data but disagree on fresh intervention choice. Feasible cost witnesses exist (assign cost 0 to selected action, 1 to other, with both Q=1). □

This is a generic underdetermination construction, not a surprising new theorem. The research problem is to find **genuine structural axioms**, restrictions on OO program transformations and demand composition, that rule out the spurious extensions and have independently testable consequences.

## 7. Deep-TCS development fork (not yet established)

For mathematical structure worthy of an eventual paper:

1. Define concrete objects as *typed OO architecture + public behavior + legal demand transformations*. Morphisms must preserve observable contracts; do not invent category composition before examining actual software semantics.
2. Build interventional observation `Ω_I` and the known P26/P27 quotient `Architecture / ~_I`. Quotients are relative to a bounded intervention basis, and rank alone does not identify architecture.
3. Find a **source-computable obligation invariant** h that predicts action-frontier splits (the unseen `ker P`) across novel maintenance demands, versus the strongest Parnas, DRSpaces, semantic cochange and design-space baselines.
4. Only then test a stable factorization or structure-preserving map from h to the conditional action correspondence. A "principle" becomes a **certified local compression**, never a preassigned ontology.
5. Demand-composition operations / interaction hypergraphs might support a stronger theorem (e.g. a necessary condition for local-to-composite transport), but P17/feature-interaction work has already killed the novelty of generic higher-order interactions. No sheaf, functor or cohomology claim without an operationally forced algebra and a new prediction.

**Scientific gate:** Proof of A–D = mathematical hygiene and implementable diagnostics. Proving that h exists, is computable, and is more predictive than established source-grounded baselines is the difficult, open, object-oriented scientific problem. Keep both code experiments and proofs in the SAME P31 research program.

Status: `P31_OBSERVATIONAL_SIEVE_THEOREMS_FORMAL_ONLY__OO_MECHANISM_HOLD`; P31 OPEN, LAW-R2 NOT_AUTHORIZED.
