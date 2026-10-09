# P37-MATH-I — Minimal Future-Repair Sufficient Quotients: Demand Refinement and Context Noncommutation

**2026-10-10 KST · theory-first research pivot · P37 OPEN · no claim of new law**

## The problem we return to
The aim is *not* another cost comparison or new library wrapper. For a fixed, fully specified source-state domain S, legal edit relation Γ, checkpoint invariant I, future demand family D and context family C, ask: **What is the least information about present source state sufficient to decide every authorized future repair query? How does that information change when demands, composition contexts, or owner permissions change?**

Let `m_{Γ,I}(s,d)∈{0,1}` be nonempty existential reachability of demand d by finite I-preserving Γ edits. This is exact mathematical reachability, **not** whether a particular bounded repair search succeeded.

Define the signature `σ_D(s)=(m(s,d))_{d∈D}` and the induced equivalence `s ≡_D t` iff `σ_D(s)=σ_D(t)`. The canonical quotient `S/≡_D` distinguishes states precisely when some demand in D can distinguish their repair possibilities.

## Theorem I1 — coarsest future-repair-sufficient equivalence (classical)

Let an abstraction `q:S→A` be future-sufficient when some `f:A×D→{0,1}` satisfies `f(q(s),d)=m(s,d)` for every s,d. Then q is future-sufficient iff its kernel equivalence `ker q` is included in `≡_D`. Consequently `≡_D` is the **coarsest** such equivalence, and `|S/≡_D|` is the minimum number of distinct abstract classes for a deterministic exact sufficient predictor in the finite case.

Proof: the factorization condition from P37-MATH-A applied simultaneously to every d. If two states have the same q-value but differ on one m(s,d), no f exists. Conversely a q-fibre contained within a σ-fibre gives f a well-defined answer. The signature map attains the bound. This is a standard kernel/factorization result.

**Subtlety:** D includes an enumerated family of binary repair queries, not unrestricted future programs; adding arbitrary future contexts changes the equivalence. Even if future-sufficient, σ does not preserve path count, edit owners, safety certificates or bisimulation.

## Theorem I2 — monotone refinement under demand extension

If D⊆D', then `≡_{D'} ⊆ ≡_D` and `|S/≡_{D'}|≥|S/≡_D|` for finite S. Each new requirement splits prior equivalence classes or leaves them unchanged, never merges classes. The splitting partition is the meet of the old partition and the newly added Boolean outcome partition; a demand d is **redundant on S** relative to D exactly when it is constant within every `≡_D` class. Thus we can identify the *minimal discriminating demand set* for a finite state universe by subset search, but this set need not be unique and the problem of finding it can be combinatorially hard.

Proof: D' equality implies equality on the subset D. A newly added Boolean coordinate splits every old block by that coordinate; no other operation occurs.

## Observation quotient versus future-sufficient quotient

Given current observation q0, the **least joint refinement** that preserves both present and future information is the intersection `ker(q0) ∩ ≡_D`. Its number of classes can exceed both separately. There is no universal order between present observation equivalence and future-repair equivalence. A tool that collapses all current-equivalent states may therefore lose future sufficiency.

## Open structural question I3 — composition commutation

Let C be a typed context constructor that may add resource handles, ownership constraints, persistent state, and observation ports. Compare:

(1) first quotient module source by `≡_D`, then compose its representative with C; versus
(2) first compose actual source states with C, then form `≡_{D_C}` for contextual future queries.

The first is sound only if *the module's future-sufficient equivalence is a congruence for the admitted C and Γ*: whenever s≡_D t, we have C[s]≡_{D_C}C[t]. Otherwise the first quotient discards information that matters only after composition.

**Minimal countermodel (must be checked):** s and t currently have no repair path satisfying local demand d (local signatures identical). Context C supplies a capability token that only state t can use, opening an authorized edit to an accepting endpoint; s lacks that edge. Then `s≡_D t`, yet `C[s]≢_{D_C}C[t]`. No precomposition quotient on σ_D alone can support the contextual prediction. This does not imply an absolute impossibility when the abstraction retains source capabilities or a richer D. The countermodel is classical contextual equivalence/abstraction-refinement and does not alone identify a new software law.

## Strong classical benchmark / novelty boundary

Closest strong rivals: Myhill–Nerode continuation classes, abstract interpretation's complete abstractions, Myhill–Nerode-style future distinguishability, modal/temporal logic characterizations, contextual equivalence, game semantics and bisimulation. Our σ-based quotient is not conceptually new merely because D denotes software source repairs. The actual law search is whether *source-derived restrictions on authority/provenance/composition* force additional, independently testable relations that are not already consequences of these theories.

**Next:** enumerate state/transition/demand models, establish which minimal partition features are stable under compositional ownership change, develop a strongest-rival comparison on fresh source-generated graphs **before** broad new CI experiments. Refuse a law label without a nontrivial distinguishing prediction.

**Current:** `P37_MATH_I_FORMAL_CLASSICAL_MINIMAL_QUOTIENT__DEMAND_REFINEMENT__COMPOSITION_NONCOMMUTATION_COUNTERMODEL__DIP49_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
