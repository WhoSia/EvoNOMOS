# EvoNOMOS Generation VIII LAW-R1-P37 — Repair-Graph Geometry Beyond Current Equivalence: Provenance Boundaries, Authority-Constrained Change Paths & Cross-Domain Predictive Falsification

**Status: P37 OPEN · P36 CLOSED AS FLOWING STAGE · 2026-10-10 KST**
**Scientific status: DIP-49 LAW_PAIR_IDENTIFICATION_HOLD · DIP-50 source fidelity REQUIRED · LAW-R2 NOT_AUTHORIZED**

## 0. Central scientific mandate — beyond SOLID, not a performance contest

The question is: **what mathematical structures govern the possible evolution of software while present behavior and legitimate constraints are preserved?** This is not a search for a SOLID metric, modularity score, more LOC reduction, or a latency winner. SOLID is merely a historically influential family of design conjectures and possible rival conditions. Runtime/allocations are measured as potential secondary constraints; they do not define the phenomenon.

Study **typed source states, contexts, observation equivalences, future demands, legal source edits, invariant-preserving paths, and repair-option survival**. Derive conditional invariants and minimal counterexamples, then attempt faithful realization on independently evolved actual software (routers AND JSON parsers) and compare strongest existing frameworks.

## 1. Precise primitives

A software state `s ∈ S` comprises code, stored representation, public API, and accessible provenance (fix this scope before any theorem). Context `c ∈ C` supplies inputs and external facilities. Current observations `O_c(s)` induce an equivalence `s≈_0 t ⇔ ∀c∈C_0, O_c(s)=O_c(t)`, with finite bounded `C_0` stated in each experiment. A future requirement `d∈D` is an observation/test predicate, not necessarily derivable from present values. Allowed edits `Γ` define a typed transition relation `s —[γ]→ s'`. An allowed *repair path* is a sequence of Γ transitions that preserves stipulated legacy invariants at each required stage, terminating in a state meeting d.

Define the **typed repair reachability fibre**
```
F_{Γ,I}(s,d) := { t : there exists an admissible Γ-path s ->* t,
                         every required checkpoint satisfies I,
                         and t satisfies d }.
May_{Γ,I}(s,d) := [F_{Γ,I}(s,d) != empty]
Must_{Γ,I}(s,d,P) := [F != empty] and [every t in F satisfies P(t)].
```
Here `I` includes present contract invariants, API compatibility, legal ownership and any no-history scope. Avoid turning finite tested candidate paths into the full relation Γ.

## 2. Structural object: continuation-sensitive quotient of source

Present-behavior quotient `S/≈_0` does **not** automatically determine future repair outcomes. Define the *future structural signature* for a fixed declared family `D,Γ,I`:
```
Φ_{Γ,I,D}(s) := ( [May_{Γ,I}(s,d)]_{d in D},
                      [Must_{Γ,I}(s,d,P_d)]_{d in D},
                      [observable outcome classes of authorized terminal repairs] ).
s ≈_{future}^{Γ,I,D} t  iff  Φ(s)=Φ(t).
```
The displayed signature is only meaningful when finite source states and complete Γ reachability have been established; for real repositories estimate bounded signatures with explicit UNKNOWN on unenumerated paths. Do not identify future equivalence as universal equality of two programs, and do not presume it always refines ≈0: future signatures may coincide while present outputs differ. For the joint quotient use `≈_0 ∩ ≈_{future}`.

**Candidate structural principle (to be proved/falsified, not a new law):** A present abstraction `q:S→A` safely represents an entire family of *future repair feasibility queries* iff the corresponding Boolean May signatures are constant on each q-fibre. An `A`-only decision cannot distinguish two states sharing q(s) but needing different future answers. This is a classical factorization criterion; actual conceptual research starts from the smallest **additional source observables** that make q sufficient across multiple future demands under fixed Γ.

## 3. Mathematical deductions with precise scope

**Factorization lemma (classical).** For fixed Γ,I and D, a map `g:A×D→{0,1}` with `g(q(s),d)=May(s,d)` for every s,d exists **iff**
```
∀s,t,d: q(s)=q(t) => May(s,d)=May(t,d).
```
Proof forward: replace q(s)=q(t) in the claimed equation. Backward: set g(a,d) to the common May value of any s in that nonempty fibre; assign an arbitrary value for unused a. This requires fixed full Γ and an unambiguous May relation. No statistics or latency enters.

**Repair projection obstruction.** If present equivalence merges two source histories and a future demand requires different outputs, then no deterministic current-state-only repair function can satisfy both. This is the P36-MATH6 / DIP42 classical indistinguishability mechanism, not a new theorem. Introducing an event log or new caller-supplied provenance changes the source state or Γ and dissolves the obstruction.

**Graph-path invariant warning.** Two repair graphs may have identical May sets while differing in number of internally disjoint paths, required API-crossing edges or invariant-preserving intermediate states. They are not therefore identical as typed graphs, and nothing in the factorization lemma alone proves these graph features affect any *later* demand. Candidate novelty lies in identifying a new, transportable conditional relation tying those structural path features to observable future survivability **that cannot be explained by a strong classical source-aware theory**.

## 4. P36 → P37 flowing lineage (the exact claims retained)

- [P36 mathematical lineage](../g8-law-r1-p36/P36_MATHEMATICAL_LINEAGE_REPAIR_SURVIVAL_AND_IDENTIFICATION_REGISTER.md): P35 finite-trace, products, set-valued May/nonvacuous Must, repair order and DIP42/48/49/50 are classical foundations; **do not take machine-checked Go/Lean re-execution as discovery of new mathematics**.
- [P36-MATH6](../g8-law-r1-p36/P36_MATH_6_NATURAL_REGISTRATION_PROVENANCE_AND_INFORMATION_BOUND.md): Chi header map lacks cross-header historical order, Gorilla ordered route-list stores it. AB/BA histories collapse in map under no-history Γ; the no-go is conditional and classical.
- [P36 original cores O9](../g8-law-r1-p36/P36_O9_NATURAL_CORE_ROUTER_POLICY_REVERSAL_PRESEAL.md): Chi radix specificity and Gorilla chronology solve *incompatible* client contracts, not a single fixed-Q universal ranking.
- [P36 Q21 O10/O11](../g8-law-r1-p36/P36_O11_ORIGINAL_INTEGRATED_LIFECYCLE_NATIVE_VERDICT.md): both independently evolved original cores admit **project-written** additive repair witnesses for an identical Q, with conditional execution costs. Adapter choices are a confound, not naturally evolved repairs.
- [P36 Q22 O12](../g8-law-r1-p36/P36_O12_JSON_ORIGINAL_Q22_NATIVE_VERDICT_AND_BASELINE_FAILURE_AUDIT.md): original independent gjson/jsonparser retain recoverable JSON number lexemes under limited first/last policy. Both native Q22 PASS; upstream jsonparser vet and PR286 failures preexist before research addons. Strong classical provenance explains.
- [P36 P37 proposal](../g8-law-r1-p36/P37_FLOWING_HANDOFF_REPAIR_GRAPH_GEOMETRY_PROPOSAL.md) is **historical name proposal, superseded for OPEN/CLOSED state by this document**; retain it unchanged as dated provenance.

**P36 closure means only stage transition**: no claim DIP49 discovered law, no R2 gate, no need to resolve every inherited issue.

## 5. First P37 structural attack — not an arbitrary cost search

**MATH-A.** Enumerate small finite typed repair graphs with state labels (present output, stored provenance, allowed Γ transitions, invariant flags) and calculate actual May/Must future signatures. Find pairs with identical present observation and differing future repair signatures; audit the exact edge/invariant that separates them.

**MATH-B.** Search *opposite* pairs: graph structures differ (many paths vs one; different API crossing) but future repair signatures are identical for a fixed D. These are essential **negative controls** proving that a naive graph complexity scalar is not itself a law.

**MATH-C.** Test whether a proposed repair-graph morphism preserving typed demands and allowed transitions preserves May, and specify the additional surjectivity/back-lifting condition necessary for Must. Require proof or bounded exhaustive counterexample; do not casually invoke bisimulation if only a forward simulation exists.

**NATIVE-A.** Next source attack Q23: on genuine gjson and jsonparser, select duplicate semantic keys `"id"` vs `"i\\u0064"` and preserve *original key spelling*, under explicit full-input ownership and source-edit authority. Original gjson `key.Raw` supplies a direct lexeme; original jsonparser `ObjectEach` exposes unescaped key and source offset of value, but a new source addon can still rescan preserved full input. Do not claim impossibility under Γ permitting retained original bytes. Classify actual source edits by information provenance boundary and API compatibility, not only speed.

## 6. Competitors, precommit and exit gates

The **strongest classical rivals** are automata continuation equivalence, bisimulation/simulation, abstract interpretation, representation independence, program slicing, database provenance, program repair and graph reachability, plus requirements-trace and API compatibility models. Most obvious P37 finite lemmas belong to these frameworks. A genuinely new law requires (a) nontrivial conditional statement not already a renaming; (b) precise mathematically grounded prior-art differentiation; (c) an independently sealed `σ_q(H)≠σ_q(B_*)` on new software sources; and (d) faithful actual software outcome under DIP-50.

A secondary calibrated prediction benchmark (nested `B_*` vs `H_G`, log-loss increment ≥0.05 nats per repo-balanced episode) is *supporting evidence about prediction usefulness* only. It does not replace the mathematical law. The existing synthetic scoring CI establishes the evaluator works, **not** holdout science.

**Current court:** `P37_OPEN__MATHEMATICAL_SOURCE_AND_REPAIR_GEOMETRY_PRIMARY__P36_STAGE_CLOSED__NATIVE_Q23_TO_SEAL__DIP49_LAW_PAIR_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
