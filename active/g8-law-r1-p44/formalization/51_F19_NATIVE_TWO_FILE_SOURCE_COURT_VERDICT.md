# P44 F19 — Verified source-changed dependency-slice certificate, original Go CI and strong classical benchmark

Research director original-court verdict, 2026-11-05.

**Verdict: F19 CLOSED-WORLD CHANGED-SOURCE SLICE REUSE PASS / CLASSICAL DEPENDENCY CACHE TIE (slightly faster in ONE run) / GENERAL BUILD-MANIFEST AND RIGHTS SOURCE PROOF OPEN / G1–G7 OPEN / LAW-R2 HOLD.**

## Exact original-source test chronology

The F19 [protocol was presealed before code](49_F19_DEPENDENCY_SCOPED_CERTIFICATE_TRANSFER_PRESEAL.md), following F18's negative classical token-cache result. Original Go source analyzer and tests:
- `sourcealias/slice.go`: closed two-source grammar and source-slice certificates;
- `sourcealias/slice_test.go`: source changes, 11 negative source construct tests, native Go compile/release tests;
- `sourcealias/slice_bench_test.go`: conventional typed full analysis, exact classical dependency cache, F19 certificate verification and certificate issuance with same original source inputs.

[Earlier CI #41992280777 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41992280777) on commit `8e120ec237b330656a49de1f96db3af1c4efa212` verified existing pre-F19 tests but did not contain F19 tests: no retrospective F19 PASS may be inferred.

[First F19 tests CI #41992388390 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/41992388390), tested commit `1422929372ec024a086f0fc29752eae28a803bfb`: all new F19 source-invalidation tests passed, but generated native Go test code failed to parse in `TestF19NativeGoCompilesAndRunsChangedAuxiliary` owing to incorrect quote insertion around expected `new` string. Raw log: `fixture_test.go:3:74: expected ';', found new`. Separate commit `662dd3b2cdd5aa53063177a932f03410df38ee72` corrected generated assertion to use `strconv.Quote`; [CI #41992458225 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41992458225), actual job raw logs showed all tests including all 4 separately native Go compiled source-pair examples passed; vet/race passed. Failed run preserved, not erased.

Expanded fair-rival benchmark code committed `ad0538e49d381a13347757393924c34194a3de87`, CI selector amended in commit `0877ac22e153de7bc7bbd0e13c2d3abb04a02626`.

**FINAL ORIGINALLY EXECUTED CI:** [#41992707164 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41992707164), **exact tested source commit** `0877ac22e153de7bc7bbd0e13c2d3abb04a02626`, original job **127128634839**, Go 1.23.2 Linux amd64. F17/F18/F19 suite, `go vet`, `go test -race`, and 8 benchmarks (4 F18 + 4 F19, 200 iterations per function) PASS; raw original logs separately inspected.

## Actual original positive and negative observations

Positive: three actual changes to `aux.go` return literal (`new`, `alternative`, `other`) produced `F19_CHANGED_AUX real_source_changed=true slice_reused=true classical_cache_reused=true`; full source classical `Analyze` agreed with previously pinned client-relevant F17 alias facts. The Go native compiler independently compiled/executed four two-source package examples (shared vs separated pointer, auxiliary old vs new), all PASS.

Negative: source core pointer-alias change `shared→disjoint` invalidated certificate; 11 cases adding unexpected functions, package globals/initializers, cross-file call/writes, unsafe imports, compiler directives, comments, illegal function signatures/references rejected. Forged certificate contents against the assumed externally trusted original seal rejected. A core identifier renamed without corresponding reference updates was ill-typed and rejected; this does not establish alpha-renaming transport.

**A crucial observer bound:** Auxiliary's return-value change is observably different to an external client calling `Aux()`. Therefore the proof retains ONLY the previously specified old client `Build(); Write(c); observe c.Legacy.Value,c.Future.Value`, which does not call Aux. It does NOT establish full-package contextual or observational equivalence. There are no runtime schedules/concurrency in this closed grammar.

## Original strong comparable computational cost (single small synthetic benchmark, 200 iterations each)

| Method (same pair of Go source strings) | ns/op | B/op | allocs/op |
|---|---:|---:|---:|
| Ordinary classical full typed reanalysis | 106,423 | 48,567 | 905 |
| Classical dependency scope + exact core token cache | **91,269** | **40,703** | **820** |
| F19 sealed source-slice certificate verification | 92,002 | 41,248 | 827 |
| F19 initial two-file certificate issuance | 121,372 | 56,394 | 1,107 |

These figures were reported by **one GitHub-hosted Go benchmark pass** and are descriptive, not statistically stable comparisons or evidence about production workloads. The matched conventional dependency cache was slightly faster than F19 verification (~0.8% difference), used less memory/allocations, and requires no extra layer of receipt hashing. Both are slower than ideal incremental systems that do not repeatedly typecheck all files, which we have NOT implemented as a source-level competitor here. F19 also incurs initial issuance cost and invalidation/reissuance cost that cannot be dropped in an all-in comparison.

F18 contemporaneous re-run measurements are in the same raw log but are not directly comparable across one-file and two-file source workloads.

## Correct theorem scope and prior-art risk

See [F19 mathematical assumptions](50_F19_TWO_FILE_SOURCE_SLICE_MATHEMATICAL_THEOREM.md). The two-file package manifest is **only an external premise supplied as two SourcePair strings**, NOT authenticated by enumerating a real repository build. The trusted original receipt is externally anchored by assumption; the code does not sign or verify a signature. The auxiliary function is purposely sealed to a pure string literal so noninterference follows immediately; no arbitrary Go dependency graph is inferred. This is a bounded, classical static dependency/frame proof, already in the space of ADAPTON/Nominal ADAPTON, compositional separation logic/bi-abduction and standard source caches.

**P44 F19 genuine changed-source transport** is a technical milestone relative to F18 exact full-token cache, but it is a very simple, known form of proof reuse and shows NO law novelty, no super-classical performance, no external maintainer holdout, no human cost, and no G1–G7 broad closure.

## Mandatory BFS decision / next gate

Stop making bigger toy packages merely to increase F stage numbers. The next research should reopen the original structural safe future-repair question against source-generated genuine owner-authorized maintenance obligations, and more complex clients with change-sensitive dependency closures. A practical next action is collect an independent maintainer patch cohort with pinned original baseline, declared edit authority and observable client contracts, and calculate whether source proof portability reduces end-to-end validation burden compared with exact dynamic/static baselines. A second mathematical direction is to prove a source-sound dependency slice under guarded function calls/alias captures instead of hand-forbidding all cross-boundary effects. Its classical rivals must include bi-abduction and Nominal ADAPTON. Any new F20 protocol must be presealed separately before implementation.

Status: F19 bounded two-file original source PASS; classical dependency cache at least equal and marginally better in this run; LAW-R2 HOLD.
