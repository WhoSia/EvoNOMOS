# P44-F32 — Towards a Fiber-Based Semantics of Software Evolvability (Hypothesis, not new categorical law)

**Purpose:** revive the original, larger SOLID-superstructure ambition while distinguishing CONJECTURE, CLASSICAL THEOREM and SOURCE EVIDENCE. 2026-11-09. No unconditional claims.

## 1. Candidate upper mathematical object
For a public/abstract API-contract state \`a\`, define the *fiber* \`Fib(a)={c | α(c)=a}\` of concrete software versions implementing that abstract state. Concrete versions can have identical current customer behavior and different legally permitted, costed paths for future demands. Hence an architectural design's future repair cost is not generally a function of only the abstract state: \`Value(c1,d)!=Value(c2,d)\` even when \`α(c1)=α(c2)\`.

A proposed enriched object is a graph/category of concrete source versions and rights/cost/observer-indexed edit paths projecting to abstract interface/contract changes. A **repair-option lifting** obligation requires every anticipated abstract edit to have a compatible actor-/source-/cost-constrained witness from EVERY concrete representation in the fiber. Future changeability is then a property of a projection and its fibers, not a fixed SOLID checklist.

## 2. Already classic mathematics
- F32's exact two-way finite cost preservation is strong labelled bisimulation/bounded morphism with weights.
- One-way lower and backward upper bounds are conventional abstract interpretation.
- Mere existence of graph-edge lifts is **NOT** a Grothendieck opfibration: the latter needs additional opcartesian/universal factorization structure, which F32 tests do not verify.
- Jones (1981 monograph / 1983 paper), Hoare, Milner, Park, O'Hearn/Reynolds, CEGAR and source alias/effect analysis present hard priority barriers.

## 3. Concrete falsifier
Abstract state \`x0\` has edits A (stutter, cost 1) and B (progress, cost 2). Its fiber contains \`open\` and \`closed\`, both with identical old-client observation. Concrete A takes \`open→closed\` and closes B availability; B exists from open only. The abstract event sequence [A,B] costs 3; the concrete sequence cannot be completed. It is the **choice of concrete representative in the same abstract fiber** that changes realizable future development paths.

The F32 two-way checker rejects this false-safe projection; the four proof grades express which weaker cost claims remain certified. This is a synthetic finite graph, not a measured real GitHub authorization revocation.

## 4. Stronger study worth attempting
Can a compact source certificate automatically demonstrate sufficiently many repair lifts for independently frozen Go source/build snapshots with authentic maintainer edit rights, across independently created future demands, at lower total verification cost than equal-information traditional alias/SSA/CEGAR/rely–guarantee tools?

Mandatory falsification: if traditional methods given identical source, rights, observations and cost information perform equally well or better, record TIE/LOSS. Preseal demand sampling/model and baselines; include abstentions even for unresolved truth.

## 5. What F32 really establishes
A reproducible 4-grade FINITE GRAPH certificate (lower, upper, exact, HOLD), an exact classical path-induction proof, a complete 256-graph toy court with 81 certified models and 2430 comparisons, a minimal missing edge diagnostic and original Jones data-refinement failure reading. NO unrestricted Go extraction, independently authenticated rights, prospective source predictions or original category-theoretic law.

Provisional paper positioning: theory-informed source certificate **research program**, not discovery of a general law. **LAW-R2 HOLD**.
