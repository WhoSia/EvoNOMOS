# P36-MATH-6 — Registration Provenance as a Maintenance-Sufficient State: Natural Map-vs-Sequence Sources

**2026-10-10 KST · P36 OPEN. This is a CLASSICAL information/minimal-state deduction, not a beyond-classical law.** Authored from pinned upstream source inspection and prior O7 D18 preseal, not a blind new theorem.

## Native source facts

Original `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00` `middleware/route_headers.go`: `HeaderRouter map[string][]HeaderRoute`, route registration appends within a header key only, and `Handler` loops `for header,matchers := range hr`. At most **within-header order** is represented. Original `gorilla/mux@b4617d0b9670ad14039b2739167fd35a60f557c5` `mux.go`: `routes []*Route`, `NewRoute` appends and `Match` visits `r.routes` in order. These are genuinely independently evolved routing source representations; their maintainers did not necessarily intend identical precedence contracts.

## Two-history no-go under a sharply bounded repair grammar

Let A and B be independently fixed handler closures and two distinct matching header names `alpha` and `beta`. Histories `h_{AB}` and `h_{BA}` register the **same** closure values A and B into the same header buckets, but in opposite time order. The terminal Chi map has equal key/value buckets (one route per key in both worlds); its exposed state has no cross-key order field. The *new client D18* wants first-registration precedence on simultaneous match:
```
D18(h_AB, both_match)=A
D18(h_BA, both_match)=B.
```
For any deterministic evaluator `g(terminal_map,request)`, terminal state and request are identical, so `g` must return the same answer in both worlds; the D18 contract demands different answers. Therefore **no deterministic D18 implementation using only that final map state** can satisfy both histories. This is noninjectivity/observational distinguishability. Permitted external log, altered public representation, user-supplied ordering, or new opt-in ordered API invalidate the no-log premise, not the proof.

**Important caveat:** Go map iteration is implementation-dependent, not a lawful chronology signal. Separate maps with AB and BA histories may incidentally yield the desired answer on one request; do not identify chance ordering with storage of registration provenance.

## Quantitative lower-bound generalization (conditional, classical)

For n≥2 **distinct uniquely tagged and simultaneously matchable header routes**, if a client only asks the first current route's winner under one all-match request, the evaluator has to distinguish at least n possible winners. Hence its state distinguishes ≥n classes (at least ceil(log₂ n) bits in a finite-code idealization) **if all n chronological winners are admissible**.

If the permitted future API additionally supports *repeatedly disable/pop the earliest remaining registered route* and observe each winner until none remain (an extra contract NOT part of legacy Chi, nor of current O7 D18), then all n! chronological registration permutations yield distinct observable winner sequences. A correct deterministic retained state under that stronger API must distinguish at least n! classes (ceil(log₂(n!)) bits of order-distinguishing information in a fixed-length binary encoding). This is standard automata distinguishability / information lower bounds, NOT an observation of existing Gorilla's byte cost, a minimal physical memory bound including Go runtime overhead, or a proof an n-element ordinal slice is the unique correct representation. For n=3, 6 permutations need at least 3 idealized bits.

The bound is about **what future queries require from the retained representation**, not abstract static package 'modularity'. It needs fixed equal initial function closures and future priority/disable semantics.

## Maintenance-repair graph and costs are separate judgments

Under `Γ_old` which allows editing only the existing original Chi `HeaderRouter.Handler` body while retaining exactly the same map state and no additional log, D18 cannot be implemented for every AB/BA history. Under `Γ_optin` authorizing one extra original-module Go file with an opt-in chronological registration surface, D18 can be implemented while old exported map API remains unchanged, *provided the caller migrates to the new constructor*. Under `Γ_break` replacing an exported map type globally, migration/API breakage can be measured and might be disallowed by real client constraints. Thus **repair feasibility is indexed by source authority, historical provenance and API contract**.

Cost vectors: registering and matching via Chi per-header map, Gorilla ordered routes, and Chi additive chronological surface use different algorithms. Native measurements of latency, allocations, mutation cost, code surface and migration workload are needed. O7 native sources must be checked before treating exact success/failure as empirical; source-inspection implication is separate.

## Candidate stronger structural-law program, with honest classical rivals

A naive scalar static-modularity comparator is under-specified and a straw opponent. The strongest source-aware classical theory already distinguishes map-versus-slice information, bisimulation under enriched labels, program refinement, data abstraction and API migration. It predicts the basic result. **DIP-49 remains HOLD** until a future fully specified H* and strong rival B* yield different signatures on the *same preregistered real-source query*. The present study gives a rigorous **necessary-state moderator** for repair-option preservation, not a new law.

**Court:** `NATURAL_SOURCE_STATE_PROVENANCE_OBSTRUCTION_CLASSICALLY_DERIVED__O7_NATIVE_PREDICTION_TO_VERIFY__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
