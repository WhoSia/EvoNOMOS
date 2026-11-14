# P44 — Classical lemmas, conditions, and countermodels (candidate v0.1)

This document does not claim originality. It supplies exact proof/defeater obligations for F0–F9.

## L1: Observer refinement
Assume fixed trace semantics Tr and projected observation for each individual o, and O ⊆ O'. Then p≡_(O',E0)q implies p≡_(O,E0)q. Proof: restrict the universal condition from O' to O. **Converse false**: GET-only ServeMux and Chi can agree under a restricted GET oracle and differ on HEAD or encoded URL behavior. Requirement: no observer-dependent recompilation of the compared source.

## L2: Protected-observer monotonicity
Fix transition graph E_pi, semantics and cost. If contract C' implies C on every source state, then every C'-prefix-safe repair is C-prefix-safe, so R(C')⊆R(C) and K(C)≤K(C') for scalar infimum. If the observer language changes but C' does not *logically* imply C, inclusion is not automatic. Requirements newly activated at stage k cannot be assumed protected at stage k−1.

## L3: Conservative rights monotonicity
Let E_pi⊆E_pi' with the same endpoints, costs, environment, demand and protection predicates for every old edge. Then R(pi)⊆R(pi') and K(pi')≤K(pi). A 'right extension' that changes editing semantics, repository ownership or old edge costs violates the premise. For vector costs, attainable sets are nested, but Pareto *frontiers need not* be nested.

## L4: Repair-witness upper bound, not optimum
An executable concrete source edit history h∈R(E_pi,C,d) implies K≤c(h). It does not imply K=c(h). Countermodel: h has length 3 but a separate permitted single-step app patch realizes d while preserving C. One 3-switch exhaustive proof is valid only over the closed switch grammar, never a lower bound for all possible Go patches.

## L5: Strict prefix safety versus final safety
Construct states s,u,g with Safe(s)=Safe(g)=true and Safe(u)=false; edges s→u cost1, u→g cost1, s→g cost4. Final-state-only search finds cost2, strict-prefix-safe search finds cost4. If s→g is unauthorized, no admissible strict-safe path exists. The final feature is reachable in a relaxed graph but not a safe repair in the declared rights model.

## L6: Baseline-output nonidentifiability
States a0,b0 have identical initial client observation, but the authorized edge a0→a1 (cost1, safe, realizes d) exists while b0 has no authorized path. Thus initial observational equivalence alone cannot determine future repairability. This is elementary model nonidentifiability, not a novel software theorem. If complete source edit relations are supplied, the two states are distinguished.

## L7: Demand-dependent preference reversal
Let A have costs X=1,Y=5 and B have costs X=5,Y=1, all under matched initial observations, safe paths and rights. Then A is cheaper for X and B for Y. Hence no unconditional scalar architecture order follows; a distribution of future demands is necessary for expected scalar comparison, and a vector cost may yield incomparability.

## L8: Cost-refining repair simulation (sufficient condition)
Let (S_A,E_A) and (S_B,E_B) be source-state graphs, R⊆S_A×S_B a relation satisfying:
(i) initial states R(a0,b0) and protected old-client observers match on related states;
(ii) for every *allowed, prefix-safe* A-edge a→a' with cost c from R(a,b), there exists a finite *allowed, prefix-safe* B-path b→*b' of total cost ≤c such that R(a',b');
(iii) if a related A state realizes the specified demand d, its B counterpart realizes d;
(iv) costs are scalar nonnegative and B uses comparable rights, environment, contract, and source granularity.
Then every finite admissible A repair path can be lifted via concatenated B paths to an admissible B path of no greater cost, so K_B(d)≤K_A(d), provided the infimum is over paths in the simulation domain. Proof: inductively match each A edge, sum inequalities, apply (iii); take infimum. The conclusion is vacuous for A unreachable and is not a necessary condition for B to be cheaper. Source-level construction and validation of R remain unsolved. Under varying stage demands, (ii) and (iii) must be indexed by stage and preserve earlier demands.

## L9: Unbounded completeness barrier
For general Turing-complete programs with unrestricted edit grammars and semantic specifications capable of expressing termination, an algorithm that decides all instances of existential safe repair under arbitrary edit grammars would subsume undecidable semantic properties (conditional reduction required). Thus P44 must declare bounded language / decidable fragment or permit UNKNOWN/timeout; do not claim general Go completeness from finite original-source runs. A formal reduction must be written before using this as an article theorem.

## Counterexample registry
CE1 GET-only equal, HEAD unequal (native).
CE2 Recoder vs HTTP wire HEAD body (native).
CE3 Same output, different repair-edge relation (synthetic).
CE4 Valid endpoint with unsafe intermediate (synthetic).
CE5 Shared mutex prevents races but LiveAlias violates temporal snapshot (native).
CE6 Authorized one-unit ID bridge works but possible alternative patches invalidate global minimality claim (native witness, untested alternatives).
CE7 Two demands reverse preference (synthetic).
CE8 Retrospectively tuning test observations destroys independent holdout (Harvest methodology, no new theorem).

Every counterexample has an evidence-level label and cannot be upgraded to full-program source completeness without new proof.
