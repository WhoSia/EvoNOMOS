# P44 F15 — Complete branch-literal edit grammar and joint client observations

2026-11-05. This is a classical finite source-model result.

Accepted grammar: a single comment-free Go file named package fixture, exactly Legacy() string returning a constant and Future(flag bool) string returning either of two constant strings using one conditional. The only permitted edits independently replace one Future return literal with one of m declared strings.

The graph has m² semantic states and 2m²(m−1) directed edits. For m=3, these are 9 states and 36 edges. Each generated Go source is parsed and checked; the native Go runtime compiled all nine generated versions in original CI #41962052369 (success, Go 1.23.2, vet and race). Classical exact BFS gives cost 2 for (off,on) to (beta,off).

Two states (off,on) and (on,off) have the same set of possible outputs but differ in their flag-conditioned input-output relation. Therefore preserving an output set does NOT prove a client contract.

After the false-input client contract Future(false)=on becomes protected, changing Future(true) from off to beta costs one authorized edit; any goal demanding Future(false)=off violates that protected contract. A stage-constrained regression test was added and separately passed in GitHub Actions #41962356928.

The first F15 workflow #41961920487 failed because the test file contained incorrectly escaped source strings. That error was fixed in a separate commit and the successful run #41962052369 is retained, not substituted for the original failure.

This proves completeness only relative to the narrow declared finite source-edit grammar and its stipulated pure Go semantics. It does not cover general Go edits, mutable state, concurrency, source permission provenance, measured developer effort, or superiority over exact classical search. G1–G7 OPEN, LAW-R2 HOLD.
