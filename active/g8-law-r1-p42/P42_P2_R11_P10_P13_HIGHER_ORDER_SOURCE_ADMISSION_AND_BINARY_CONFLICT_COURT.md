# EvoNOMOS G8 LAW-R1-P42 — R11-P10-P13: Pairwise Source Admission Versus Higher-Order Repair Gluing

**2026-10-18 KST · RESEARCH QUESTION AND PREDICTIONS FROZEN BEFORE ANY P13 NATIVE CHECKER · P42 RUNNING / P43 HOLD / LAW-R2 NOT_AUTHORIZED**

## 0. What was already known, and why P13 is not a duplicate

This is NOT a new abstract-interpretation or SOLID theorem. The chronology is [P37-MATH-I](../g8-law-r1-p37/), [P39-MATH-D/E/G](../g8-law-r1-p39/P39_MATH_G_ACYCLIC_HYPERGRAPH_GLUING_INVARIANT_SEPARATORS_AND_SHATTERING.md), [P40-MATH-B-P2 original-Chi guard](../g8-law-r1-p40/P40_MATH_B_P2_AXIOM_INDEPENDENCE_AND_ORIGINAL_CHI_SOURCE_GLUING_COURT.md), [P40-P4 source boundary](../g8-law-r1-p40/P40_MATH_B_P4_PROSPECTIVE_SOURCE_BOUNDARY_CONTRACTS_AXIOM_IRREDUNDANCY_AND_CLASSICAL_REDUCTION.md), [P10 source-to-C/E admission](P42_P2_R11_P10_P10_SOURCE_TO_CAUSAL_NET_ADMISSION_AND_REPAIR_TRACE_QUOTIENT.md), [P11 genuine Gin A/B five-stage native diamond](P42_P2_R11_P10_P11_SOURCE_NATIVE_DIAMOND_COURT_AND_CLASSICAL_BOUNDARY.md), and [P12 Lean co-enabled square](P42_P2_R11_P10_P12_COENABLED_DIAMOND_ADMISSION_AND_SOURCE_BOUNDARY_FACTORIZATION.md). P39-MATH-G already refutes naive pairwise/gluing when separator constraints are incompatible. P12 proved saturation is distinct from coenabled square filling. P40-P4 already tested the 3-name two-bit *flat static* case. None of those is a new exhaustive **native three-edit source-admission census** for a mixed structural route grammar.

Original pinned go-chi/chi: `167e1e3bd039d060696b99c8da4e876ae04f42c1` (P40 existing native oracle). `Mux.Mount` (mux.go lines 295–353) checks `tree.findPattern(pattern+"*") || tree.findPattern(pattern+"/*")`, an independent alias check `subr.tree==mx.tree` and installs stub routes. Original `tree.findPattern` (tree.go 591–630) matches radix-tree structural node types and skips regex pattern text by matching brace, NOT by deciding disjointness of represented HTTP request languages. Reusing that code evidence is essential; caller-visible route-language disjointness does not decide admission.

## 1. Mathematical question fixed before source instrument

Let E be a finite one-shot set of **research-owned source-edit registrations** on a single pinned original maintained library, and H⊆E* the legal stagewise-source-admitted histories whose protected original client continues to pass. For each finite subset X⊆E define
\[
\mathrm{AllOrders}(X)=1 \iff \forall \text{ permutations }\pi\in \mathrm{Sym}(X),\;\pi\in H.
\]
(An existential variant \(\exists\pi\) is DISTINCT. Freeze both diagnostics and never conflate them with customer functionality.) For a three-edit set X, define a genuine **three-way obstruction** as every singleton and every **two-order pair** accepted but at least one three-action order not admitted:
\[
\big(\forall Y\subset X, |Y|\le 2: \mathrm{AllOrders}(Y)\big)
\quad\land\quad \neg\mathrm{AllOrders}(X).
\]
This isolates higher-order source admission beyond merely pairwise incompatible edits, not a client behavior verdict.

### Theorem P13-T1 — exact graph-conflict sufficiency (classical)

If a source action system has an installed-set state \(X\subseteq E\), edit e is admitted **iff** e∉X and no existing x∈X satisfies a fixed symmetric conflict relation C(x,e), each admitted transition sets X←X∪{e}, and protected original-client validity is preserved for every admitted transition, THEN any edit subset Y is admitted under **every permutation** iff it has no pair in C. Proof: induction over the permutation and the history-independent guard; an e has no conflict against any predecessor exactly when Y is C-independent. This is a standard graph independent-set/guarded-transition fact, not new mathematics.

**The target is to FALSIFY (or provisionally support on a bounded source grammar)** the transfer of this graph model to the real maintained Chi `Mount` guard. `findPattern` depends on the evolving radix tree, not just a declared fixed pairwise intersection graph. Even if no three-way witness appears, that proves **only the frozen finite grammar**, not arbitrary Chi patterns or a graph representation theorem.

### Theorem P13-T2 — a triple witness rules out any exact fixed binary-conflict model

Given a source corpus with all pair permutations admitted but some triple permutation rejected, there does NOT exist any fixed symmetric pairwise conflict C whose `AllOrders` outcomes agree on all these subsets. Proof: all two-element sets accepted forces C empty on the triple; T1 then predicts all its permutations, contradiction. Classical no-factorization reasoning (earlier P40 Lean), with source witness if discovered.

### Theorem P13-T3 — admission, protected safety and future customer success are distinct

The defined H tests edit registration and old-client stage validity. Even if all registered source edit orders exist, independent requests may be overwritten, shadowed or semantically incorrect. Exact client success requires *additional* source-native protected and new-client oracles for each final state; client history-order queries and cost invariance must be checked separately under P8–P10. Thus source-admission graph classification cannot be used as a future repair Pareto frontier without rights, effects, client and actual cost certificates.

## 2. Frozen source-native experiment and honest unknowns

Use one original unchanged Chi commit, fresh parent on each permutation, `GET /old → 200 "old"`, and 7 **research-owned child route-registration edits** using `chi.Mount` with fresh separately-owned child router (no shared-tree alias):
- A: `/svc/a` with child `GET /item`.
- B: `/svc/b`.
- C: `/branch/one`.
- D: `/branch/two`.
- E: `/svc/{num:[0-9]+}`.
- F: `/svc/{alpha:[a-z]+}`.
- G: `/svc/a/deep`.

A, B, C, D provide positive structural static controls, E/F the P40-like regex disjoint/external language but internal structural collision controls (different actual parameter labels from P40), G provides hierarchical prefix sharing. These are **new predeclared instances/family extensions**, not independent maintainer PR demands.

Enumerate every singleton (7), every two-action permutation (7·6=42), every three-action permutation (7·6·5=210) = **259 source-permutation programs**. For every stage: create an actual `chi.NewRouter`, perform `Mount` with panic recovery to record admission, test old GET /old as 200 old; retain first rejected action and full/source-stage trace. Every source test uses exact original Go code and a test oracle; registration success **does not automatically certify each new-client route**.

**Predeclared expectations and uncertainties:**
- All seven singleton edits are **predicted admitted** on fresh parent; old /old predicted intact, based on P40 source grammar. If any fails => scientific falsifier, not silently discard.
- A/B and C/D, static distinct siblings, each 2-order pair **predicted admitted**. E/F predicted both paired orders **REJECTED** by the structural regex reservation guard, as in prior P40 but with independent literal prefixes; neither counts as new phenomenon.
- Other mixed pairs and ALL three-way obstructions are **UNKNOWN prospectively**. Test without changing freeze to fit results.
- For 3-element subsets where all six orders register, call that `AllOrders3`; if pairs pass and a triple fails, collect *one full native source witness* for a non-binary conflict.
- Crucial: absence of a triple-only witness in the seven-pattern set is NOT a proof of general pairwise sufficiency. Do not infer architectural superiority, client success, actual source maintainer authority, or costs.

**Fair baseline:** A source-aware classical guarded transition/LTS or CSP model fed exactly the same original Chi admission evidence would be expected to explain any discovered higher-order source states; HARC has no preannounced unique theoretical advantage.

## 3. Future math before more code

If P13 finds a genuine ternary obstruction, extract minimal source/guard state separating its two identical pairwise compatibility profiles and place it into P39-MATH-G separator/gluing formalism. If none, derive the **exact induced binary graph** for the observed seven-pattern grammar, then **state an operationally falsifiable source-guard hypothesis for a NEW held-out pattern set before validation**, rather than re-run arbitrary cases and claim success. Both outcomes serve the same scientific question. Source-to-net B1/B2/B3 and client/rights G1–G7 remain OPEN beyond the bounded program corpus.

**Gate: P42 RUNNING, R11-P10-P13 PRESEALED before native code, P43 HOLD, LAW-R2 NOT_AUTHORIZED.**
