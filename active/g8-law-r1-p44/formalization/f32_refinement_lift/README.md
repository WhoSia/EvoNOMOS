# F32 — Refinement-Stable Repair-Event Path Lift

A reproducible **finite classical simulation court** extending F31's source/build methodology with a *newly explicit scientific question*: will an abstract promise of future source repair remain implementable in **every** concrete representation of that abstract state?

This module does NOT read Go repositories, authenticate actor rights, measure real-world developer cost, or prove persistent source-goal satisfaction. It accepts fully declared FINITE graph tables as input. Current results are best treated as strong classical negative controls and requirements for a future source extractor, not a unique new SOLID law.

## Exact reproducibility

\`\`\`sh
cd active/g8-law-r1-p44/formalization/f32_refinement_lift
go test -count=1 -v ./...
go vet ./...
go test -race -count=1 ./...
\`\`\`

Verified locally with Go1.23.2. [F32 original GitHub Actions workflow](https://github.com/WhoSia/EvoNOMOS/actions/workflows/p44-f32-refinement-lift.yml) runs exactly these commands. See [theorem and original Jones (1983) audit](../76_F32_REFINEMENT_STABLE_REPAIR_OPTIONS_JONES_AND_PATH_LIFT.md) and [directional cost proof-level judgement](../77_F32_DIRECTIONAL_COST_CERTIFICATES_AND_JONES_1981_PRIORITY.md).

## Source model and actual tests

\`lift.go\`: exact finite edit-action graph, named actor, demand EVENT, nonnegative integer cost, old-client observable, abstraction α, strict labelled two-way simulation, Dijkstra over finite action-event words. \`witness.go\`: stable error witness naming a concrete representative and an unliftable abstract edit. \`polarity.go\`: separate FORWARD path projection from BACKWARD path lifting and declare lower bound / upper bound / equality / HOLD. Every positive result bears an explicit \`...SOURCE_UNATTESTED\` grade.

A hidden permission-gate synthetic countermodel keeps the old-client output \`"old"\` constant and gives both individual edits, but completing A makes B impossible. Abstract \`[A,B]\` costs 3 while concrete \`[A,B]\` is unreachable. This is NOT a real observed GitHub permission revocation.

\`lift_test.go\`: 256 graph exhaustive court (all subsets of 8 named candidate edits); 81 two-way-certified graphs; 81×2 concrete initial states×15 action words = 2,430 exact cost comparisons, all equal. Additional tests for Jones's 1983 printed equation (3.40), permission failure witness, wrong actor/cost, observation mismatch, mapping holes, incomplete graph, negative costs and finite cost sentinel overflow.

\`polarity_test.go\`: all 4 logical proof grades, and why a *projection-only* certificate is not a constructive safe-repair promise. The resulting four-grade classification is conventional refinement/abstract interpretation, not new category theory.

## Epistemic boundaries

- A \`Demand\` string is an EDIT-EVENT label, not a persistent state-goal predicate. For multi-stage accepted requirements, F27's retention invariant or equivalent must be added.
- This tool assumes COMPLETE graph tables; it cannot attest that no unrecorded Go edits or actor rights exist.
- Costs are synthetic nonnegative ints. \`math.MaxInt\` is reserved as the no-path sentinel; a finite path reaching or exceeding that value returns HOLD, rather than a false impossibility claim.
- A graph homomorphism alone yields only a lower bound; source-edit existence requires lifting witnesses. A matched classic weighted-bisimulation implementation receives the same graphs and is an EXACT TIE.
- Future promotion needs actual verified source/build edit representation, authenticated legal permission, independent prospective demands, and classical source-aware rivals evaluated on equal information.

**G1–G7 OPEN · LAW-R2 HOLD · PR #13 Draft.**
