# EvoNOMOS Generation VIII LAW-R1-P35-P7 — Return to Original Go Structural Competition

**2026-10-09; bounded result:** `P35_P7_ORIGINAL_GO_TWO_STRUCTURE_NATIVE_PASS__OPPOSED_TEMPORAL_ENVIRONMENT_REACTIONS__CLASSICAL_CACHE_EXPLANATION_NOT_DEFEATED__P35_OPEN__LAW_R2_NOT_AUTHORIZED`.

## Scientific priority restored

EvoNOMOS does **not** exist to perfect responsibility boundaries, cochange scores, AST metadata, code-edit location forecasts, or econometric costs. It seeks discoverable, testable and revisable **conditions under which real software design alternatives win, fail or reverse under evolving requirements**, with novel hypotheses beyond SOLID where justified. P6 Go AST/historical NONE/ablation methods are preserved as tools; they are **not** the new main question.

This P7 is actual A/B Go source competition, not a new ontology: two distinct internal algorithms are substituted into the **same original production Go file** of [go-chi/chi `v5.1.0`](https://github.com/go-chi/chi/tree/67be7d9cafdaeb4e04e887ff78d09e030ee43b00), `middleware/route_headers.go` / `HeaderRouter.Handler`. The public `HeaderRouter map[string][]HeaderRoute` and `Route`/`RouteAny`/`RouteDefault` signatures and actual complete upstream module tests remain intact.

## Independent source organizations and frozen tests

- **LIVE** [full original-source Go alternative](../../tools/p35-p7/arms/live/route_headers.go) reads actual current map registry per request, alphabetically sorts the header names, selects the first matching registered route within that header, and falls back once.
- **SNAPSHOT** [full original-source Go alternative](../../tools/p35-p7/arms/snapshot/route_headers.go) builds a sorted array of groups and copies route/match-pattern slices **when a handler is constructed**; subsequent requests read this compiled state without reading the mutable source map. Both are independent algorithms, not differently named delegation to one shared routing kernel.
- [Frozen protocol](P35_P7_GO_STRUCTURAL_RETURN_PRESEAL.md) and [common/mode acceptance tests](../../tools/p35-p7/tests/p35_p7_common_test.go) were committed **before source treatments**, in human WhoSia commit [`3fd1097`](https://github.com/WhoSia/EvoNOMOS/commit/3fd109746b72b80e890fb3eb329ad971e074a666). Source arms and read-only original-Go workflow then committed in child human [`a478765`](https://github.com/WhoSia/EvoNOMOS/commit/a47876564d7463b76f7ddbf130a8ac357d6e5691).

**D0 COMMON:** deterministic priority across simultaneously matching headers (lexical header name); same-header first registered route; `RouteAny` wildcards; default fallback; empty-rules registry dispatches its downstream handler exactly once. Original untouched pinned Go source fails the empty-registry case as expected: its previous `len(hr)==0` case invoked downstream but failed to return before invoking it a second time.

**D-LIVE and D-FROZEN are different environment contracts, not one shared later demand:** after handler construction, sequentially register a new matching route (no concurrent read/write). D-LIVE requires the existing handler to reflect it; D-FROZEN requires that handler to keep its old state. LIVE expected D-LIVE PASS / D-FROZEN FAIL, SNAPSHOT expected the reverse. These demands are mutually incompatible for the same handler/state without a more complex version-selection API, so only context-relative admissibility follows.

## Actual native Go evaluation and negative tests

Initial original-source [read-only Actions #37908529775](https://github.com/WhoSia/EvoNOMOS/actions/runs/37908529775) **FAILED** because the *test observer* overwrote an earlier middleware's `X-P35-P7` response tag in the downstream test handler. This was test-fixture observer damage, not source algorithm failure. [Human commit `421eb91`](https://github.com/WhoSia/EvoNOMOS/commit/421eb91a86cff15b7c89eb7aa9e564dc57eb77b1) fixes only the downstream recorder's overwrite logic and the shell label; **both production Go treatment files, prespecified demanded outcomes and pass criteria remain unchanged**.

The corrected original-source [read-only Actions **#37908914089**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37908914089) is **SUCCESS**. The hosted Go 1.23 runner:
1. Checks original exact upstream commit SHA and adds the unchanged experimental Go test paths.
2. Verifies original D0 **EXPECTED FAIL** with reason `P35P7_D0_EMPTY_ROUTE_FAILURE`.
3. Replaces **actual original `middleware/route_headers.go`** with LIVE; checks `go vet ./middleware`, `go test -race -count=1 ./middleware`, complete original `go test -count=1 ./...`, frozen D0 tests and conditional time-mode label. **All PASS**.
4. Independently replaces original source with SNAPSHOT; repeats exactly the same Go original regression and race suite and frozen D0 with expected opposite time-mode label. **All PASS**.
5. Runs two non-gated Go benchmarks (`SteadyLookup`, `ConstructOnce`), retains per-arm raw output and source unified diffs. Their raw logs were archived, but **numeric timing/allocations are not interpreted as a robust architecture speed ranking in this court**.

Native receipt artifact [**11605402735**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37908914089/artifacts/11605402735), SHA-256 `62c1fe81ba16913212e1ae627cad35276e600c207bcb976fdf703473354ad5cb`. Read-only GitHub Actions `contents: read`; neither workflow authored a commit.

| Actual scenario | LIVE | SNAPSHOT | Meaning |
| --- | --- | --- | --- |
| Original bounded common routing D0 | PASS | PASS | same initial functionality and API |
| Whole original Go module tests | PASS | PASS | existing regression checks preserved |
| Original middleware Go race suite | PASS | PASS | no race in tested cases; sequential mutations only |
| Handler observes new registration after construction (D-LIVE) | PASS | FAIL | live mutable state is observable |
| Handler retains old registration after construction (D-FROZEN) | FAIL | PASS | snapshot retains frozen state |
| Performance | native benchmarks executed | native benchmarks executed | no robust, independently replicated timing winner established |

**Safety/validity limits:** Existing `HeaderRouter` is a mutable map. Neither test runs concurrent routing-table mutation while requests execute; no claim of concurrent live-registry mutation safety. Native `go test -race` covers the exercised registered tests, not arbitrary concurrency. The two temporal contracts are distinct future environments, so they do not form a controlled **same-demand** lifecycle cost reversal. No new formal proof or behavior-preserving migration across both time contracts is established. The old lack of deterministic map traversal and classic snapshot-vs-live cache behavior are already explainable by established data-structure semantics. No new SOLID or beyond-SOLID law is identified from these results.

## Identical subsequent demand D8 — independent real-Go repair extension

**D8 was sealed AFTER P7 D0 results, but BEFORE any D8 treatment or D8 CI**: [pre-implementation protocol](P35_P7_D8_EQUAL_DEMAND_PRESEAL.md) and original-scope [frozen D8 Go acceptance test](../../tools/p35-p7/tests/p35_p7_d8_same_requirement_test.go), human `WhoSia` commit [`2d92ec0`](https://github.com/WhoSia/EvoNOMOS/commit/2d92ec05c86b33d3f7521569de4a919c149d59d1). Thus this is **not pre-P7-outcome randomized requirement selection**.

**Same new requirement in both source worlds:** When two different header names simultaneously match, an *exact literal pattern* must outrank a wildcard, regardless of earlier lexical header name. Equal-specificity ties preserve alphabetical header-key preference. First matching registration **within the same header** remains the winner even if later registrations are more specific. `RouteAny` may contain an exact match alongside a wildcard; either must be considered correctly. Prior default/empty routing and each arm's original sequential-update semantics must survive.

Actual previous D0 source arms LIVE and SNAPSHOT separately **fail** the new frozen D8 test as expected. Independently patched source variants [LIVE D8](../../tools/p35-p7/d8/live/route_headers.go) and [SNAPSHOT D8](../../tools/p35-p7/d8/snapshot/route_headers.go) each change the existing `HeaderRouter.Handler` and introduce one `p35P7MatchStrength` helper; no exported Go API changed. A source-only implementation was committed [`55693c6`](https://github.com/WhoSia/EvoNOMOS/commit/55693c6f851b5145c47913c595554e3ca60f888b) following the source-free D8 seal.

The first D8 run [#37910105820](https://github.com/WhoSia/EvoNOMOS/actions/runs/37910105820) failed on a **Bash receipt-variable typo** after the LIVE native Go tests already passed, so it did not adjudicate both source worlds. A human-only workflow text correction in [`6ebb9b8`](https://github.com/WhoSia/EvoNOMOS/commit/6ebb9b88b7047b498942b335ef7c5abca4552cc7) left source and demands unchanged.

The final [read-only original Go Actions **#37910415486**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37910415486) **SUCCESS**: negative D8 test on both previous source arms, then for **each independent D8 repair** original entire Go `go test -count=1 ./...`, middleware `go test -race -count=1`, old D0, new D8, and its own D-LIVE or D-FROZEN mode indicator. Artifact [11605489532](https://github.com/WhoSia/EvoNOMOS/actions/runs/37910415486/artifacts/11605489532), SHA-256 `02c0e6ac651300b3e828a3373eab9d04934cff1a019a0381d6fd5e6a998355c6`. Distinct source patches and SHA receipts are retained.

**Bounded comparison:** both D8 witnesses require one observed existing method edit and one added helper. This supports **same-demand repair feasibility and an observed equality of those particular source coordinates**, NOT equality of the minimum admissible repair families, nor developer effort, nor an architecture-wide Pareto equivalence. It is classical specificity-order selection under two different data materializations and does **not** defeat existing algorithmic/caching explanations. It is especially important that prior D-LIVE/D-FROZEN uses **different mutually exclusive demands**; D8 alone is the proper matched-demand repair experiment in this phase.

## Founding program versus narrow local finding

This P7 restores the missing **real structural rival + original native behavior contact** to the EvoNOMOS mainline. The next substantive law-discovery experiment must now move beyond easy indexing/caching examples by comparing *multiple independent source organizations* under the **same future change demand sequence**, full `S/L/C/A/Q` outcome vector, pre-outcome predictions of rank/sign reversal, and a strong information-matched existing explanation. Generate non-SOLID hypotheses from surprising real code constraints rather than preloading dependency ownership or responsibility as the expected answer.

The interpretation must remain: **P7 bounded experimental native PASS, mainline structural-law discovery still OPEN**, and **LAW-R2 NOT_AUTHORIZED**. The P6 observer/ablation methods remain subordinate. `INFRASTRUCTURE PASS != CORE ADVANCE`.
