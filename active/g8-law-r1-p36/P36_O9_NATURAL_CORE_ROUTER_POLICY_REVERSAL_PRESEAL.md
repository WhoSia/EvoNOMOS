# P36-O9 — Naturally Evolved Core Router Policy Reversal: Specificity-First vs Registration-First

**2026-10-10 KST · FROZEN prospective source-aware D19/D20 comparison. P36 OPEN; P35 CLOSED.**

## Why O9 is independent of O7 and what it does not prove

P36-O7 studied Chi **middleware.HeaderRouter** (a public map) against original Gorilla Router (ordered route slice) for competing header fields and future cross-header registration precedence. O9 changes to the genuine Chi **core path router**, `chi.NewRouter`, and Gorilla's corresponding original core path router. It must NOT be counted as the same Chi architecture used in O7; the different Chi subsystems have different source representations.

Exact independent original upstream snapshots unchanged:
- `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. Original `tree.go` `children [ntCatchAll+1]nodes` and `nodeTyp`: `ntStatic` ordinal 0, then regexp, then param. `findRoute` iterates node groups in this order, irrespective of route registration chronology.
- `gorilla/mux@b4617d0b9670ad14039b2739167fd35a60f557c5`. Original `Router.NewRoute` appends route to `routes []*Route` and `Router.Match` walks it in insertion order. Unlike Chi, route path matching precedence is based on this registered route order.
- Neither is an author-created EvoNOMOS policy wrapper.

## Fixed shared route grammar and baseline

Two GET path patterns sharing the same exact prefix:
- generic `/members/{id}`, parameter route, tag `PARAM`;
- literal `/members/me`, static route, tag `STATIC`.

Same Go HTTP `GET /members/me` request satisfies **both** patterns. `GET /members/42` matches only PARAM. Two chronological registration histories `PS` (parameter first) and `SP` (static first) under both original libraries. Q0 baseline: `/members/42→PARAM`, missing route `/outside→404` in both histories and both libraries.

Declare two **separate, incompatible future client contracts**, not one simultaneous required contract:
- **D19 SPECIFICITY:** literal STATIC must win when both match, regardless of registration chronology. Predict original Chi **PASS** in PS and SP; Gorilla **scientific expected-negative** in PS (`got PARAM want STATIC`), PASS SP.
- **D20 CHRONOLOGY:** the earliest registered matching route wins regardless of static-vs-param specificity. Predict original Gorilla **PASS** in PS and SP; Chi **scientific expected-negative** in PS (`got STATIC want PARAM`), PASS SP.

Both Q19 and Q20 are tested against the exact same original source, same request, same route templates, two histories and fixed result projection. Do not present two mutually incompatible client policies as simultaneous requirements or call either library wrong for following its established semantics.

## Measurement and fair structural comparison

- Original native full Go module, `go test -race -count=1 ./...`, `go vet ./...`.
- Freeze the two original library tests *before* native CI. The workflows classify Q0 positive plus D19/D20 outcomes using expected-signature checks on test logs, keeping both informative negatives as SUCCESS only when failure is exactly the sealed behavioral difference.
- Within each **original library**, optional microbenchmarks comparing PS vs SP on the overlap may measure route lookup cost under same host, but the output differs across registrations/contracts. No post-hoc declaring winners by a single scalar, and never compare timings for configurations that fail the requested client's semantic oracle.
- Strong source-aware classical rival `B_classical_priority` predicts everything here from trie static-node precedence and ordered route-list iteration. The result is a genuine **conditional design preference reversal** under different functionality contracts, but not a newly discovered beyond-classical law.

**Key prediction**: each original evolved core routing representation wins **one** distinct requested semantic policy without a repair and fails the other in one registration order; neither is globally preferable. This improves on a unilateral Gorilla winner from O7's particular D18 demand without forcing artificial SOLID scoring.

**At seal:** `P36_O9_ORIGINAL_CORE_ROUTERS_TWO_CONFLICTING_CLIENT_POLICIES_FROZEN__NATIVE_UNVERIFIED__DIP49_NEW_LAW_PAIR_HOLD`.


## 2026-10-10 — Native original-source run completed, immutable prior seal preserved

[Original core Chi/Gorilla two-job CI #37969103183](https://github.com/WhoSia/EvoNOMOS/actions/runs/37969103183) finished **SUCCESS 2/2**. Both original upstream pins ran `go vet ./...`, `go test -race -count=1 ./...`, `go test -count=1 ./...` and Q0 disjoint path PASS. The new D19/D20 independent functional acceptance predicates were tested individually without source edits.

- **Actual original Chi core** `chi.NewRouter`: D19 SPECIFICITY PASS for both route registration orders; D20 CHRONOLOGY scientific expected-negative for generic-first, literal `P36_O9_D20_CHRONOLOGY_MISMATCH paramFirst=true trial=0 tag=STATIC code=200 want=PARAM`. Artifact id `11634424128`, ZIP SHA256 `d02c2a6578362e4b45d5887007c7a7c7a96cc32cc6b1271c1edf1e0472716b3f`.
- **Actual original Gorilla core** `mux.NewRouter`: D19 SPECIFICITY expected-negative for generic-first, literal `P36_O9_D19_SPECIFICITY_MISMATCH paramFirst=true trial=0 tag=PARAM code=200 want=STATIC`; D20 CHRONOLOGY PASS for both orders. Artifact id `11635230474`, ZIP SHA256 `1e19a62baa162991bc2bf49d998fdc4c667957a43d56be943678bb7c2c843bf5`.

All FOUR cells in the preregistered two-source × two-contract predicted result matrix agree with actual original source behavior. The workflow's **SUCCESS** encodes two expected scientific negatives, not universal D19 and D20 PASS. The original source feature behavior is not labeled an upstream bug. The clients demand incompatible outcomes in generic-first world and therefore **no universal architecture preference** follows. Unlike O2's research-authored EAGER/LAZY policies, the dispatch structures here are existing original *core* router designs.

**Strong classical rival `B_classical_priority` fully predicts this matrix** from ordered radix node-type traversal vs route registration slice. Consequently `DIP49_DISTINCT_NEW_LAW_IDENTIFICATION_HOLD`. The real scientific gain is strong prospective **context-specific structure-choice evidence across two genuinely independent libraries**, not new theory beyond established route precedence semantics.
