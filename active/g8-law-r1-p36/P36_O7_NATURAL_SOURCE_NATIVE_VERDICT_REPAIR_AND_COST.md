# P36-O7 — Native Natural-Source Court: Header Registration Provenance, Repair Authority, and Measured Cost

**2026-10-10 KST · P36 OPEN · P35 stage CLOSED · LAW-R2 NOT_AUTHORIZED.** This is a post-execution receipt following the separately authored [prospective original-source seal](P36_O7_NATURALLY_EVOLVED_ROUTING_PROVENANCE_PRESEAL.md), [supplementary pre-source additive repair seal](P36_O7_B_OPTIN_ORDERED_CHI_REPAIR_PRESEAL.md), and [classical lower-bound deduction](P36_MATH_6_NATURAL_REGISTRATION_PROVENANCE_AND_INFORMATION_BOUND.md).

## 1. Original independent source difference, real Go native PASS

[Genuine original-library cross-source CI #37967751731](https://github.com/WhoSia/EvoNOMOS/actions/runs/37967751731) completed **2/2 SUCCESS**:
- pinned `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`, **unchanged upstream** `middleware/route_headers.go` uses `HeaderRouter map[string][]HeaderRoute`. Unique-header Q0 PASS, full native old module test/race/vet PASS. Newly specified D18 requires across *different* header buckets earliest registration wins on a simultaneous match. Source-native **scientific expected negative**, literal frozen test log: `P36_O7_D18_ORIGINAL_SOURCE_PRIORITY_MISMATCH first=A request=2 got=B`. Artifact id **11633384355**, ZIP SHA256 `fb42c1464972a4c454ed7d937e37d5a55c06c476a037fde9a2fac2e2e80b49e6`.
- pinned original `gorilla/mux@b4617d0b9670ad14039b2739167fd35a60f557c5`, unchanged upstream `routes []*Route` traversed in original registration order. Original Q0 and future D18 both PASS for AB/BA over 128 repeats each; original module test/race/vet PASS. Artifact id **11634447366**, SHA256 `4051b2e1691300ac501ea56a722b846d288ab3ddcc2ca52abbf4bbedea482503`.

**Caveat:** D18 is an *independent client requirement*, not a claim either repository's maintainers promised precisely the same cross-header precedence policy. The old Chi failure is **not** an upstream bug verdict. Chi's map key iteration order is unspecified with respect to registration chronology, and can change during requests. Gorilla native route order is a retained source structure.

The original first CI [#37967600039](https://github.com/WhoSia/EvoNOMOS/actions/runs/37967600039) FAILED **only on ZIP source-hash test path** because test lives in `tests/mux`, while script looked under `tests/gorilla`. Neither native oracle nor original source needed a change. A human [workflow-only correction `ab6c6db`](https://github.com/WhoSia/EvoNOMOS/commit/ab6c6dbd89414704778840abaf1fafe0d1e62bd4) repaired the audit path and later run fully succeeded. The failure is retained in provenance, not hidden.

## 2. Opt-in additive original Chi package repair (NOT a preexisting upstream option)

[Chi O7B source/repair CI #37967872965](https://github.com/WhoSia/EvoNOMOS/actions/runs/37967872965) completed **SUCCESS**, single original-module job:
- Original source `middleware/route_headers.go` remains **bit-for-bit untouched**.
- New research-authored Chi module package extension [`P36O7OrderedHeaderRouter`](../../tools/p36-o7/arms/chi/additive-ordered/p36_o7_ordered_headers.go) uses an ordered route entry slice, copies it at Handler publication, and matches the same original Chi `HeaderRoute` pattern logic.
- Legacy public `HeaderRouter map` remains unchanged and is checked for continued map indexing and old-source routing. The *new opt-in API* Q0, D18 128-repeat AB/BA ordering, same-header priority, RouteAny and default fallback all PASS, full old Chi Go/race/vet PASS.
- Artifact ID **11633808829**, ZIP SHA256 `96728687ee61fdce2234fefcb42b36b8a9ad44cc9a8aaa15eb7e161a3927dd02`.

**Repair-grammar conclusion:** under `Γ_old` (modify old `HeaderRouter.Handler` but no new history state) D18 cannot be guaranteed for both AB/BA by any deterministic evaluator of the final public map: both terminal bucket maps are identical but new desired priority outputs differ. Under `Γ_optin` (new API and ordered event record permitted), a real original Chi module extension satisfies D18, **but old clients must opt in**; existing map users are not automatically upgraded. In the stronger `Γ_break` one may replace/alter exported structures at compatibility cost, not measured here. This is classical missing-state information and API authority, not new law.

## 3. Real hosted same-original-module costs; report the scope

Raw O7B [`bench.log` from artifact #11633808829](https://github.com/WhoSia/EvoNOMOS/actions/runs/37967872965), Intel Xeon Platinum 8573C, Linux amd64, `GOMAXPROCS=1`, `-cpu=1 -benchtime=200ms -count=5 -benchmem`; request `httptest.NewRecorder()` included in all benchmarks, registration was **outside** the timed loop:

| Original Chi benchmark, Q0 one matching header unless specified | five raw ns/op | median ns/op | B/op | allocs/op |
| --- | --- | ---: | ---: | ---: |
| legacy original map, single matching header | 488.2,487.5,491.3,488.9,486.2 | **488.2** | 592 | 7 |
| opt-in ordered, single matching header | 431.0,432.5,430.2,431.8,434.5 | **431.8** | 592 | 7 |
| opt-in ordered, **both matching headers**, chronological winner | 432.0,435.9,431.7,434.0,431.2 | **432.0** | 592 | 7 |

**Descriptive observation** within Q0 single-header functionality: the opt-in version measured ~11.6% less ns/op than old map on this one host and tiny route set, with equal allocated bytes and allocation counts. This is NOT a universal speed advantage, no paired randomized independent runners, and no computation of migration/registration memory costs. It is *invalid* to compare old Chi map against ordered Chi for Q18 as if both satisfy the same new functional contract: legacy fails Q18.

## 4. Additional historical naturally occurring repair comparator

In [actual upstream commit `05f1ef7` (Feb 5, 2026)](https://github.com/go-chi/chi/commit/05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723) the Chi maintainers fixed an **unrelated** empty-map double-next-dispatch bug with one `return` line and tests. That historical naturally evolved repair is documented in [O8](P36_O8_HISTORICAL_UPSTREAM_ONE_LINE_REPAIR_VS_MISSING_STATE.md), and its separate native [CI #37968399257](https://github.com/WhoSia/EvoNOMOS/actions/runs/37968399257) was **in progress** at this inscription. One-line existing-state flow fix vs new-state history requirement shows two qualitatively different repair tasks; because demands differ, **do not** compare raw patch size as evidence of generic modularity or repair efficiency.

## 5. Strongest classical rival and honest law-identification gate

The strongest theory is **classical information retention + abstract representation invariants + API compatibility + conditional performance modeling**. It already predicts the source behavior and why an opt-in ordering surface can work. No non-overlapping `σ_q(H)` vs `σ_q(B_classical)` prediction has emerged. Therefore `DIP49_LAW_IDENTIFICATION_HOLD`, `LAW_R2_NOT_AUTHORIZED`. Actual contribution: a source-backed **conditional maintenance reachability constraint** across naturally evolved libraries, with a functional witness, native repair and costs.

**Current O7 verdict**: `TWO_INDEPENDENT_ORIGINAL_LIBRARIES_CROSSHEADER_NATIVE_PASS__CHI_D18_EXPECTED_NEGATIVE__GORILLA_D18_NATIVE_PASS__CHI_OPTIN_REPAIR_NATIVE_PASS__CLASSICAL_INFORMATION_THEORY_EXPLAINS__NO_NEW_LAW`.
