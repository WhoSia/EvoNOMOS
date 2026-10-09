# P36-O10 — Two Original Go Module Repairs Under the SAME Q21: Native Functional and Cost Court

**2026-10-10 KST · P36 OPEN, P35 CLOSED · This is POST-TREATMENT native evidence.**

## Frozen lineage and code ownership

[First pre-source Q21 preseal](P36_O10_IDENTICAL_CONTRACT_DUAL_ORIGINAL_ROUTER_REPAIR_PRESEAL.md) committed before both identical [Chi Q21 test](../../tools/p36-o10/tests/chi/p36_o10_identical_q21_test.go) and [Gorilla Q21 test](../../tools/p36-o10/tests/mux/p36_o10_identical_q21_test.go), which were committed **before** [Chi additive source](../../tools/p36-o10/arms/chi/p36_o10_selectable.go) and [Gorilla additive source](../../tools/p36-o10/arms/mux/p36_o10_selectable.go). The Go tests are substantively identical except package declaration. No original upstream source files were altered: each pinned checkout had exactly two untracked files, one project-authored additive source and one frozen test, per native `source-status.txt`. These new adapters are **not naturally evolved upstream repairs**; original core Chi radix tree and Gorilla ordered route-list semantics are naturally evolved baselines.

`Q21` shared scope: finite GET route grammar `/members/{id}` and `/members/me`; selectable policy `"specificity"` or `"chronology"`; original PS or SP registration history; GET `/members/me`, `/members/42`, `/outside`; exact response status/winner tag; reject unsupported policy/pattern/duplicate/post-publication Register; concurrent read-only requests. Each new handler is immutable after construction, legacy original `chi.NewRouter` and `mux.NewRouter` remain unchanged. This is **NOT** all routes, methods, subrouters, middleware, redirects, dynamic registration or external-client migration.

## Actual original pinned source execution (first paired runner)

[Same-runner original Chi+Gorilla Q21 CI #37970800075](https://github.com/WhoSia/EvoNOMOS/actions/runs/37970800075) final **completed/SUCCESS**; one job `one-runner-matched-q21`, pinned `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00` and `gorilla/mux@b4617d0b9670ad14039b2739167fd35a60f557c5`. The job ran:
- `go vet ./...`, original `go test -count=1 ./...`, original `go test -race -count=1 ./...` for **both modules**, all PASS, including the new frozen Q21 tests.
- Both policies × both histories × all three paths, 128 observations each, same oracle in both packages; published handler concurrency, unsupported inputs and configuration lock tests PASS.
- Counterbalanced within one physical runner: block1 Chi→Gorilla, block2 Gorilla→Chi; `GOMAXPROCS=1`, Go 1.23.12, Linux amd64 on **AMD EPYC 7763 64-Core Processor** VM with 4 visible vCPUs; `-benchtime=150ms -count=5 -benchmem -cpu=1`. Each same-named benchmark has **10 raw ns/op observations per original module** (5 each block). HTTP test request created before timed loop; `httptest.NewRecorder()` **inside** timed loop in both.
- Artifact id **11634968676**, ZIP SHA256 **`4994e98bd5fefbd8bc9ebdebdc2d8c192e141b38e637aa56e30efa9d71fbb647`**, [GitHub native artifact and run](https://github.com/WhoSia/EvoNOMOS/actions/runs/37970800075). The artifact contains original/full/race/vet/Q21 logs, 2 blocks × 2 original-source benchmarks, CPU receipt and source SHA. **All metrics below were computed by parsing the archived raw logs**, not inferred from workflow success.

## Same-contract, same-runner measured dispatch and build costs

Units: **ns/op** median across **10 raw repeated Go benchmark observations** (two reversed benchmark-order blocks). Byte and allocation values are representative constant per case across these repeats. `PS`: generic parameter pattern registered first; `SP`: static pattern registered first. All rows are **Q21-correct** on frozen tests.

| Q21 mode | Registration | Request | Chi ns/op | Gorilla ns/op | Chi B/op / allocs | Gorilla B/op / allocs | Descriptive smaller ns |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| specificity | PS | overlap `/members/me` | **1122.0** | 1346.5 | 1568 / 12 | 1792 / 15 | Chi |
| specificity | SP | overlap | **1115.5** | 1352.0 | 1568 / 12 | 1792 / 15 | Chi |
| specificity | PS | single `/members/42` | 1646.0 | **1603.5** | 2208 / 19 | 2096 / 16 | Gorilla, **weak ~2.6% gap** |
| specificity | SP | single | 1644.5 | **1616.5** | 2208 / 19 | 2096 / 16 | Gorilla, **weak ~1.7% gap** |
| chronology | PS | overlap | **1541.5** | 1558.5 | 1968 / 18 | 2096 / 16 | near tie (~1.1%) |
| chronology | SP | overlap | **1119.5** | 1360.0 | 1568 / 12 | 1792 / 15 | Chi |
| chronology | PS | single | **1542.5** | 1560.5 | 1968 / 18 | 2096 / 16 | near tie (~1.2%) |
| chronology | SP | single | 1650.5 | **1619.5** | 2208 / 19 | 2096 / 16 | Gorilla, weak (~1.9%) |
| build | (PS) specificity | construct and publish 2 routes | **1623.5** | 16726.5 | 2000 / 31 | 13376 / 203 | Chi, **two chosen adapters only** |
| build | (PS) chronology | construct and publish 2 routes | **1619.0** | 16695.5 | 2000 / 31 | 13376 / 203 | Chi, **two chosen adapters only** |

The two reversed-order block medians agree in **direction** on the sizeable specificity-overlap effect, but the ~2% single-pattern opposite-direction effect is **not yet independently transportable**. Source-specific adaptation mechanisms and Go allocator/regex/routing costs explain plausible outcomes classically. No statistically defensible hardware-general speed ranking follows from correlated repeats on one runner.

## Original source repair reachability, invariants, costs and compatibility

`F(A;Γ_add,Q21,c)≠∅` demonstrated for BOTH pinned independently evolved cores by native original-Go source additions. Under `Γ_0` as strictly **no source addition**, this exact newly requested opt-in `P36O10NewSelectableRouter` surface does not exist; that is an API-existence observation, **not** proof the older routers cannot simulate either individual routing policy with existing client orchestration.

- **Chi**: its original core tree prioritizes static segments within one Mux; the new addon evaluates separately registered real `chi.Mux.Match` objects in selected priority order, dispatching the chosen real core Mux. The extra match operations (and route context work) can cost in generic-only paths. The new core policy is an opt-in construction rather than replacing the upstream radix algorithm.
- **Gorilla**: the new addon configures its real original registration-ordered mux with sorted registration order under specificity and original order under chronology; it does not edit `Router.Match`. Construction includes Gorilla route matching/regexp preparation, a meaningful non-equivalent implementation-cost mechanism.
- **Both** preserve the old public API by additive files and pass all old suites/race/vet; this is *noninterference in tested code*, not formal ABI/semantic equivalence for every third-party context. **New callers must migrate** to the opt-in surface, so no old client gains new Q21 automatically.

The experiment therefore shows a genuine **same-Q functional reachability witness and conditional cost-vector differences** in two naturally evolved core modules, *but* the particular policy adapters were human-authored research implementations. Do not mistake differences between these two adapters for inherent impossibility or globally optimal repair distance of their respective original cores. Old Q19/Q20 contrast from O9 was on incompatible Q, whereas **all O10 rows match exactly the same Q21**.

## Post-first-run preregistered independent runner replication

[O10R pre-replication seal](P36_O10R_TWO_RUNNER_COST_SIGN_REPLICATION_PRESEAL.md) fixed the observed large Chi-overlap advantage, weak opposite single-pattern sign and ~10× build-sign as **hypotheses to challenge** in two new independent paired-host runs **after first-run results were known**. [Replication workflow](../../.github/workflows/g8-p36-o10r-two-runner-cost.yml), source and test SHA pinned without change. **Original two-runner results not yet read at first inscription**. Disagreements must be preserved as negative evidence, and repeated Go loops do not give independent-novelty claims.

## Strongest rival and exact status

Source-aware **classical routing precedence, method selection, middleware composition, code-generated adaptation and allocation cost** already predict feasibility and permit all observed cost ranks. Current `σ_q(H*)≠σ_q(B*)` identification requirement fails because no calibrated stronger H* differs from that baseline. `DIP49_NEW_LAW_IDENTIFICATION_HOLD`; `LAW-R2_NOT_AUTHORIZED`.

**Court at first native result:** `P36_O10_TWO_ORIGINAL_MODULES_FULL_RACE_VET_IDENTICAL_Q21_PASS__SAME_RUNNER_10_REPETITION_CONDITIONAL_COSTS_OBSERVED__NEW_RUNNER_REPLICATION_PENDING__NO_NEW_LAW`.
