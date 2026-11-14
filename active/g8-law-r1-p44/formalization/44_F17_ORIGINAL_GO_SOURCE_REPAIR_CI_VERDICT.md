# EvoNOMOS P44-F17 — source-derived alias and executable Go source-repair court

Date 2026-11-05. **CLOSED GO AST SOURCE-REPAIR FIXTURE PASS; EQUAL-INFORMATION CLASSICAL ANALYSIS TIE; G1–G7 OPEN; LAW-R2 HOLD.**

## Exact original source and CI provenance

Initial [Actions #41981642673](https://github.com/WhoSia/EvoNOMOS/actions/runs/41981642673), source commit ce50ed987fa79d4ce8313e91cce60018ff779d2d, FAILED at compilation because `analyzer_test.go:10:26: string literal not terminated`. Original failure preserved; no test/effect verdict can be drawn from it.

In separate correction commit `7edef9b709f3bfdb5bc2ea41bac923ce5320dad8`, fixed Go fixture string quoting. [Actions #41981819965](https://github.com/WhoSia/EvoNOMOS/actions/runs/41981819965) SUCCESS (4 tests plus vet/race; raw logs inspected). Results:
- SOURCE_DERIVED_ALIAS shared=true legacy_after_write=new disjoint=false legacy_after_write=stable.
- NATIVE_SOURCE_ALIAS shared=true/false runtime_matches_static=true.
- SOURCE_ESCAPE_CONTROLS rejected=7.
- CLASSICAL_ALIAS_BASELINE shared_safe_cost=2 detached_safe_cost=1 method=exact_two_operation_BFS.

An additional original AST source patch transformation and native compiled/executed repair was added in commits `63739ada6ba476695a496cb44aed4f4b7d56b3dd` and `29b298ac33adf21951c27cb785fe758488e77b38`. [Final original Actions #41982338576](https://github.com/WhoSia/EvoNOMOS/actions/runs/41982338576), exact tested commit `29b298ac33adf21951c27cb785fe758488e77b38`, original job `127095084490` completed SUCCESS, raw logs inspected, 6 named Go1.23.2 tests, go vet and race PASS. Logged:
- GO_SOURCE_PATCH before_alias=true after_alias=false source_patch_cost=1 runtime_write_not_counted=true.
- NATIVE_REPAIRED_GO_SOURCE legacy_contract=true future_requirement=true.

## Verifiable formal domain

The source analyzer accepts precisely one comment-free `package fixture` file with two types `Cell{Value string}`, `Clients{Legacy,Future *Cell}`, and two functions `Build() Clients`, `Write(c Clients)`. Build allocates one or two distinct fresh `&Cell{Value:"stable"}` expressions and returns keyed pointers from those allocation sites; Write has exactly one assignment `c.Future.Value="new"`. Any extra function, hidden mutation, build directive, arbitrary input or reference is rejected. Go `go/types` must accept the parsed source. Under these specific semantics, allocation-origin identity is a sound points-to equality decision.

The concrete `DetachFutureSource` operation modifies Go AST Build from shared `Clients{Legacy:p,Future:p}` to allocate q and return `Clients{Legacy:p,Future:q}`, reformat/reparse and validate with source analyzer, then native-compile and execute. The Write runtime operation is unchanged.

This finite *source-patch* metric allows only the `DetachFutureSource` transformation and no-op, with synthetic cost 1 for the former. Thus under the explicitly declared future demand "after invoking unchanged Write, Legacy stays stable and Future becomes new", source repair cost is shared=1 and disjoint=0. This differs from F16's earlier **runtime operation metric** shared=2/disjoint=1, for which split and write both counted as actions. These two cost results are consistent but cannot be exchanged as identical concepts.

## Critical validity limitations

1. Source alias facts are derived from REAL Go syntax but the source grammar is deliberately closed. It is not a generic points-to analysis or a full source-complete authorized edit relation.
2. The only allowed code patch is artificially declared; other legitimate Go edits and human labor costs are not modeled.
3. Execution in the native Go runtime matches the checker on two generated constructors and the repaired source, not all Go programs/environments, concurrent interleavings or server/client contexts.
4. The source transformation may change formatting; byte identity beyond the declared edit and AST semantics is not claimed.
5. The conditional optimization is trivial for a standard compiler-aware alias/points-to analysis plus one AST refactoring. No precision, speed, certificate-size or repair utility gain over the classical rival has been shown.
6. The original program's `Write` method is already in the source; the future *requirement* is the post-write joint client outcome, not an as-yet-unseen independent maintenance issue. This is not a sealed external future-demand cohort.

## Director's verdict and next gate

**F17 BOUNDED SOURCE-AWARE REPAIR PASS / CLASSICAL ALIAS ANALYSIS TIE / REAL SOURCE GENERALITY OPEN.**

The significant scientific correction is the distinction between dynamic operations and source patches, and the closing of one F16 source evidence gap. It would be unsound to publish this as a new software law. Next: derive source ownership/permission provenance and check whether a footprint certificate transfers across **independent, later source revisions** with less verification effort than conventional points-to analysis; preseal tests and grant equal information to classical methods. Continue BFS exploration of real client observers, source completeness and measured developer costs. LAW-R2 HOLD.
