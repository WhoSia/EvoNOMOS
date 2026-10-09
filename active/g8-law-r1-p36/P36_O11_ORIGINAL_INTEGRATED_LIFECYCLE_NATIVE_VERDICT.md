# P36-O11 — Native Integrated Source-Lifecycle Court: What the Separated-Cost Model Got Wrong

**2026-10-10 KST · POST-RESULT, two independently hosted original Go codebases · P36 OPEN / LAW-R2_NOT_AUTHORIZED.**

## Prospective provenance and intact original source

[O11 sealed integrated lifecycle design](P36_O11_INTEGRATED_LIFECYCLE_FINITE_N_GRID_PRESEAL.md) committed before identical [Chi](../../tools/p36-o11/tests/chi/p36_o11_lifecycle_bench_test.go) and [Gorilla](../../tools/p36-o11/tests/mux/p36_o11_lifecycle_bench_test.go) benchmark files and before CI execution, **after** observing first-run O10/replicated O10R source costs. No Q21 source treatment or frozen source test was altered. This is prospective against **actual integrated N behavior**, not a blind prediction of all underlying effects.

[Original pinned Chi + Gorilla integrated native CI #37972048630](https://github.com/WhoSia/EvoNOMOS/actions/runs/37972048630) completed **SUCCESS 2/2 independent runner jobs**; both ran old original-module full Go, race `go test -race -count=1 ./...`, `go vet ./...`, and **unchanged** identical selectable Q21 policy acceptance, all PASS. Exact source Q21/test SHA correspond to prior O10/O10R artifacts; new benchmark files SHA likewise identical in both O11 replicas:
- Chi production extension `236a207fddfb18e9aa823afdb3962c673bb4d83b3b861650cb81ed47549d1306`, previous Q21 test `39b832771154b5fc958e8ad75b07de5b878d7c1fef629af908fd2cc75213a55e`, new O11 benchmark `1bd8dda7c695be83d497294f4f90a3657650881d82b4f89ae4bd3e42cd194378`.
- Gorilla extension `e3fb1496aad99e09ba4188bf7451f382ee551ac70dd8598c42a344fb3f400111`, Q21 test `1274de0d9b22a823b1214c833699135efd46e4f458213ec27e0ad32d4b1aa7b6`, O11 benchmark `4d5a6eb32833829b778e8a832aa8fb65a41fd5f79139a6f561a8f52622a32eb7`.

Original independent runner ZIP artifacts:
- `CHI_FIRST` AMD EPYC 9V74, artifact **11636421845**, ZIP SHA256 `fbe46e368371ed52c42b2c85470d17959cca0028a1b0012e0d4057e72c46afb7`.
- `GORILLA_FIRST` AMD EPYC 7763, artifact **11637795337**, ZIP SHA256 `b8876baf9a98d980922c5760169a6b6ccb0ae5357c0ea99a3b6f9581298477f0`.

On each physical runner Go 1.23.12 Linux amd64 `GOMAXPROCS=1`, 2 reversed order blocks 5 repetitions each, `-benchtime=100ms -benchmem -cpu=1`. Each source, workload and N cell has **10 raw Go benchmark observations per runner**, no post-hoc benchmark subset. Workload `specificity, PS`, both Q21-valid request paths: `single=/members/42` and `overlap=/members/me`. Each benchmark **operation** builds a fresh actual source adapter, registers both patterns, publishes the handler, then serves **exactly N** HTTP requests with a freshly allocated `httptest.NewRecorder()` per request. Request itself is preconstructed outside timed loop; last handler retained outside timed loop to prevent dead-code elimination. Units ns/op and B/op are **per entire lifecycle build+N operation**, not per request.

## Actual integrated timing, not added microbenchmark medians

All rows are **Q21-correct and full original-Go/race/vet PASS**.

| Request | N | EPYC 9V74 Chi ns/op | EPYC 9V74 Gorilla | EPYC 7763 Chi | EPYC 7763 Gorilla |
| --- | ---: | ---: | ---: | ---: | ---: |
| single generic | 0 | **1254.5** | 12314.5 | **1633** | 16279.5 |
| single generic | 64 | **83835.5** | 92985 | **109650** | 122942.5 |
| single generic | 128 | **164954.5** | 173932.5 | **214210** | 229863.5 |
| single generic | 256 | **328137** | 332462 | **425221** | 441374 |
| single generic | 384 | 491850.5 | **486488.5** | **636318.5** | 655124.5 |
| single generic | 512 | **651929** | 652664.5 | **849742.5** | 865443.5 |
| single generic | 1024 | 1306658.5 | **1281641.5** | **1703043.5** | 1709114.5 |
| overlapping static | 0 | **1250.5** | 12350 | **1634** | 16328.5 |
| overlapping static | 64 | **55983** | 79915.5 | **74912.5** | 106847.5 |
| overlapping static | 128 | **112318** | 147142 | **146276.5** | 196373.5 |
| overlapping static | 256 | **219420** | 279707.5 | **292358** | 374684 |
| overlapping static | 384 | **327923.5** | 416953 | **437152** | 553736 |
| overlapping static | 512 | **438812.5** | 551162.5 | **581341** | 731986 |
| overlapping static | 1024 | **871738** | 1087412.5 | **1166552.5** | 1444851 |

**Primary negative finding:** previously measured separate build+single-request median `T(N)=B+N L` proxy forecast first temporal crossovers at ~195 requests (EPYC 9V74 prior replica) and ~355–415 (EPYC 7763 prior sessions). In actual integrated whole-lifecycle measurement, 9V74 single generic Gorilla wins at N=384 and 1024 but not N=512 (0.11% opposite margin); EPYC 7763 **does not show a Gorilla timing win at any measured N through 1024**, though the N=1024 gap is tiny (~0.36%). Therefore do **not** claim an observed unique, monotone, source-general request-count switch or a validated specific 195–415 timing threshold. The nonmonotone winner sequence includes small/noisy gaps; it refutes naive confidence in exact static crossover predictions, **not** the general possibility of a sufficiently calibrated additive model or amortized explanation.

**Positive workload control:** when `/members/me` matches the first static handler, Chi remains lower in entire-lifecycle ns/op **for all N=0,64,128,256,384,512,1024 on both physical runners**. This aligns with measured smaller initial setup and per-dispatch costs for the *selected* Chi source repair.

## Actual integrated allocated bytes and allocation counts

Per *entire* operation, both independent runners report nearly identical integer allocation fingerprints (Go allocator and benchmark resolution can shift 1–2 bytes at larger N).

| Single generic N | Chi B/op | Gorilla B/op | Chi allocs/op | Gorilla allocs/op |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 2000 | 13376 | 31 | 203 |
| 64 | 143790 | 147534 | 1254 | 1227 |
| 128 | 285108 | 281692 | 2470 | 2251 |
| 256 | 567743 | 550006 | 4902 | 4299 |
| 384 | 850381 | 818321 | 7335 | 6348 |
| 512 | 1133014 | 1086636 | 9767 | 8396 |
| 1024 | 2263563 | 2159894 | 19496 | 16590 |

This provides an **actual integrated resource-cost reversal**, more robust than small timing margins:
- Chi uses fewer **total bytes** at N≤64, Gorilla at every measured N≥128, on BOTH independent source runners.
- Chi uses fewer **total allocation events** at N=0, Gorilla already at N=64 onward, on both.
- The MATH-9 **proxy** had predicted respective crossing scales ~102 requests (bytes) and ~58 requests (allocation count). The integrated finite N grid resolves these only into intervals **(64,128]** for bytes and **(0,64]** for allocation count, consistent with the proxy; **do not claim exact thresholds were observed**.
- Overlapping route remains lower for Chi on lifecycle time and total allocated bytes/alloc counts throughout the recorded N-grid under these **project-authored source adapters**.

## Mathematical interpretation and unblocked stronger research

The *same Q21*, same source treatments and same N-grid can yield:
1. robust **workload-conditional** positive Chi dominance on all measured dimensions for overlapping path;
2. a **component-wise lifecycle tradeoff** on generic-only path: Chi cheaper to construct, Gorilla less costly to dispatch and allocate per additional request;
3. a real, repeatable **allocation reversal with N**, but **no stable monotone timing crossover** within this finite grid on the two environments.

This is more precise than either `Chi is faster`, `Gorilla wins`, or a universal per-request threshold. Classical amortized fixed-plus-variable costs, GC interaction and route-matching data structures explain plausible mechanisms and are **not** beaten by any prospectively calibrated law H*. Relative ranking is a **vector under (contract Q, allowed edit Γ, workload distribution μ, lifecycle N, environment c)**; absolute architectural quality remains undefined.

Neither repair is claimed to be an optimal implementation. The original core software libraries evolved independently, **but the one-file opt-in Q21 extensions were chosen by EvoNOMOS**, so adapter design is a confound. A genuine predictive new law must beat strong source-aware classical theories on independent, presealed new systems and avoid retrofitting a novelty claim to a favorable rank reversal.

**Final court:** `P36_O11_INTEGRATED_ORIGINAL_GO_2_RUNNERS_Q21_PASS__RESOURCE_ALLOCATION_RANK_CROSSOVER_NATIVE_CONFIRMED_IN_FINITE_N_GRID__SIMPLE_TIME_THRESHOLD_UNSTABLE__OVERLAP_CHI_DOMINANCE_ADAPTER_CONDITIONAL__DIP49_LAW_PAIR_HOLD__LAW_R2_NOT_AUTHORIZED`.
