# P44-F27 — Minimal source-level factorization certificate: obligations and falsifiers

## Proposed checked artifact, NOT certified on real Go yet
A certificate for architecture split A | B should include:
1. SOURCE: pinned tree SHA, Go compiler/build tags, dependency graph, versions and exact file/AST ranges; no anonymous source edit.
2. PERMISSION: a named actor/right scope for every admitted edit with evidence of owner/maintainer authority; absent evidence -> HOLD, not "forbidden".
3. EFFECT FRAME: every admitted A edit provably leaves B's code/alias/heap/resource and dispatch-observable state unchanged, and symmetrically B edits preserve A. Cross links must be represented, not silently discarded.
4. CLIENT FRAME: OLD clients' joint observable trace contracts, exceptions, dynamic interface/method capabilities and concurrency schedules factor or are explicitly checked as cross-observer constraints; marginals alone insufficient.
5. DEMAND GRAMMAR: independently registered demand alphabets, including impossible demands, are disjoint; each stage's satisfaction is a local predicate. Prior accepted demands persist at every edit checkpoint.
6. COST/RESOURCES: cost is additive across independent steps, and no common labor capacity, license, review budget, file lock, synchronization or global quota creates cross-edit coupling.
7. TRANSITION COVERAGE: a complete bounded edit grammar with both local source edit witnesses and evidence that no other admitted edit can change both components. Missing scope -> UNKNOWN, not a universal impossibility claim.

## Formal certificate contract
Given a source-to-graph extractor E and real source semantics S, a positive Factorized(S,A,B) receipt is trustworthy only after a proof that concrete admissible step transitions correspond to the declared A||B steps with action, authorization and cost preserved, and that concrete old-client safety and demand truth coincide with abstract predicates. A one-way overapproximation may justify LOWER cost bounds but cannot by itself certify a constructible upper repair witness. A one-way underapproximation may witness one repair but cannot establish exact optimality. For equality, need the appropriate two-sided completeness/correspondence over the declared grammar.

## Must-fail attacks
- Introduce a Go interface method that causes an alias to a shared object; expect a refused factorization certificate.
- Introduce a middleware or old client observing joint request correlations; expect refused factorization.
- Allow a single app-maintainer change touching both components; expect refused certificate even if that change is beneficial.
- Couple separate edit workflows to one review quota; expect refused certificate.
- Remove a promised actor grant without signed authority; expect HOLD.
- Present a demand impossible in all valid states; projection must preserve it and return infinite within the bounded complete model.

A source extractor that silently ACCEPTS any of these has failed before empirical tests. Competing classical source-aware static analyzers/CEGAR must receive the identical source, rights, observer and cost input. All G1–G7 OPEN; LAW-R2 HOLD.
