# P37-MATH-B — Composition and Congruence of Observation and Future-Repair Equivalence

**2026-10-10 KST · P37 OPEN · THEORY FIRST.** This document states exactly which composition and graph-morphism conditions are sufficient, where tempting weaker conditions fail, and which results are already classical process semantics.

## 1. Typed source and context

Let a typed program state be a node of a labeled transition system `(S,Λ,→,O)`. `Λ` are **authorized edits** (Γ), not merely runtime events. An invariant predicate `I:S→Bool` specifies legacy functionality, API ownership and admissible intermediate states. Future demand `d` has accepting set `D_d⊆S`. `May_I(s,d)` means there exists a finite (including length zero) path from s, with **all** nodes I-admissible, to D_d. Relative `Must_I(s,d,P)` is nonvacuous and universally quantifies the terminal outcomes in the declared reachable family.

A context operation `C:S→S_C` may compose a service with a client, a module with dependencies or a producer with a consumer. One must name its observation ports, permitted environment edits, and whether it can inspect hidden state.

## 2. Theorem B1: exact context congruence criterion (elementary, not novel)

For a fixed class of context constructors `𝒞`, define the contextual closure of an equivalence `≈` by
```
s ≈^𝒞 t  iff  for every C∈𝒞, C[s]≈C[t].
```
If 𝒞 includes identity and is **closed under context composition**, then `≈^𝒞` is a congruence for every C∈𝒞: if `s≈^𝒞t`, then `C[s]≈^𝒞C[t]`. Proof: any D∈𝒞 gives `D[C[s]]≈D[C[t]]` since D∘C∈𝒞. Identity gives `≈^𝒞 ⊆ ≈`. The statement holds regardless of whether ≈ is present observational equivalence or future repair equivalence; the difficulty is *which contexts have legal authority and can preserve Γ*. This is classical contextual equivalence.

**Failure without closure:** contexts only `{id,C}` may produce `C[s]≈C[t]` even though `C[C[s]]` distinguishes them. Thus a claim of congruence for arbitrary composition using a nonclosed context family is invalid.

## 3. Theorem B2: forward repair simulation preserves existential futures in one direction

Let `h:S→T` preserve start-state admissibility, target acceptance, and authorized edit transitions:
```
I_S(s) => I_T(h(s));
s --γ--> s' and I_S(s') => h(s) --γ'-->* h(s') with admissible T intermediates;
s∈D_d => h(s)∈D'_d.
```
Then `May_{I_S}(s,d) => May_{I_T}(h(s),d)`, by image of a witnessing finite path. **One-sided forward simulation does not yield reverse implication or nonvacuous Must.** Source deadlock a with image x→y accepting is a counterexample: target has new repair path not liftable in source.

For a reverse implication, demand **acceptance reflection** and a lifting property: for any admissible target path starting at h(s), an admissible source path ending in some t with h(t) in target acceptance can be constructed. This is stronger than simply preserving runtime outputs and must be justified for source edit semantics.

## 4. Source composition is not automatically homomorphic to repair

A tempting claim:
```
Repair(C[s],d) = C[Repair(s,d)]
```
is generally false. A composed client can ban edits allowed in isolation, introduce new invariant obligations, or supply an authorized event log absent in the isolated state. Even if current outputs match, future May can change after composition. Exact repairs form **relations**, so equality of sets requires both an extension (every component repair lifts into a compatible contextual repair) and a reflection (every contextual repair projects onto a component repair). Both premises frequently fail at API and provenance boundaries.

**A useful conditional proposition:** If C is *repair-transparent* for Γ and I, meaning (1) every allowed local path is lifted by C with identical legacy invariants and demand translation, and (2) every admissible contextual path starting at C[s] projects to a legal local path reflecting demand acceptance, then `May(s,d)↔May(C[s],C[d])`. This is a direct path-bijection / back-and-forth claim, not a new law; it is a strong property to test in real software.

## 5. First finite counterexamples and research questions

**Counterexample 1 — contextual loss of equivalence:** two states have same visible number `1` but different stored lexemes `1e+0` and `1.0`. A consumer whose port sees only numeric value cannot distinguish them; a future full-source/lexeme observer can. Under a no-original-input/no-log Γ their distinct future outputs cannot both be reconstructed from the normalized interface. Under Γ permitting original input/provenance the obstruction disappears. This is P36's original router history lesson transported to JSON.

**Counterexample 2 — path count not sufficient:** graph X has one successful authorized path and graph Y has two; both have same `May(d)=true` for fixed d. No simple 'more edits = better design' law follows.

**Counterexample 3 — one-way simulation:** source blocked, target unblocked, so one-sided graph morphism alone does not reflect `May`.

**Next theory gate:** seek a genuinely *nontrivial* constraint on composition of separate ownership/provenance boundaries that can be checked before future repair, beyond classical contextual equivalence, data refinement, game semantics, logical relations and bisimulation. Source inspection and native Q23 outcomes are data to challenge this premise; until a strong competitor prediction differs, `DIP49_IDENTIFICATION_HOLD`.

**Verdict:** `P37_MATH_B_CONGRUENCE_CLASSICAL__PATH_TRANSPARENCY_CONDITIONAL__CONTEXTUAL_COUNTEREXAMPLES_DEFINED__NO_NOVEL_LAW_IDENTIFIED`.
