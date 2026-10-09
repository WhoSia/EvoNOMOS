# P36-O10R — Independent Runner Native Readback: Robust Same-Q Resource Ranking Reversal, Fragile Near-Tie

**2026-10-10 KST · POST-REPLICATION SOURCE-AUDITED VERDICT · P36 OPEN · LAW-R2 NOT_AUTHORIZED.**

## Temporal and original-source integrity

The [O10 first original-source run #37970800075](https://github.com/WhoSia/EvoNOMOS/actions/runs/37970800075) revealed a substantial conditional overlap Chi advantage (~17%), a small **opposite** generic-only Gorilla advantage (~2.6%), and ambiguous chronology-PS near-tie. We **then preregistered** these exact signs in [O10R two-independent-runner preseal](P36_O10R_TWO_RUNNER_COST_SIGN_REPLICATION_PRESEAL.md), and performed a new native CI **without any changes to Q21 tests or source treatments**.

[O10R CI #37971308882](https://github.com/WhoSia/EvoNOMOS/actions/runs/37971308882) completed **SUCCESS, 2/2 independent-runner jobs**. Both new independent VMs cloned both original pinned `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00` and `gorilla/mux@b4617d0b9670ad14039b2739167fd35a60f557c5`; the same one-file-per-module project additive sources and frozen Q21 tests. Both original modules' **full Go, race, vet, and Q21** tests PASS in both independent jobs. Every artifact confirms **exact source and test SHA identity** across all 3 host runs:
- Chi additive source `236a207fddfb18e9aa823afdb3962c673bb4d83b3b861650cb81ed47549d1306`; frozen test `39b832771154b5fc958e8ad75b07de5b878d7c1fef629af908fd2cc75213a55e`.
- Gorilla source `e3fb1496aad99e09ba4188bf7451f382ee551ac70dd8598c42a344fb3f400111`; frozen test `1274de0d9b22a823b1214c833699135efd46e4f458213ec27e0ad32d4b1aa7b6`.

**Archive receipts:**
- **First source runner**, AMD EPYC 7763, O10 artifact **11634968676**, ZIP SHA256 `4994e98bd5fefbd8bc9ebdebdc2d8c192e141b38e637aa56e30efa9d71fbb647`. 10 repeated Go bench records per library/variant over 2 reversed-order blocks.
- **Independent replica CHI_FIRST**, AMD EPYC 9V74, O10R artifact **11635398463**, ZIP SHA256 `fb9c20f84748a09ce8bb325390bfba63817d21d1676663d2f219e7f0c3403b2a`. 12 repeated samples (6×2 order blocks) per library/variant.
- **Independent replica GORILLA_FIRST**, AMD EPYC 7763, O10R artifact **11635034445**, ZIP SHA256 `b57bd2a4e831d1aae708358d278c506dbec56bc820764146464a631bbb877bbd`. 12 per library/variant.

All use Go 1.23.12 Linux amd64, `GOMAXPROCS=1`, 150ms benchmark windows, Go `-benchmem -cpu=1`; each physical runner pairs both packages and reverses benchmark block order. Benchmark's `httptest.NewRecorder()` allocations **are included**. Two machines are named EPYC 7763, one EPYC 9V74. Same CPU label does not imply identical contention/VM conditions. The two blocks are not fully independent random samples.

## Exact independent-runner Q21 median results (ns/op)

Here Q21 is **identical accepted policy-selectable functional semantics** in both library extensions. `PS` = PARAM route first. `SP` = STATIC route first. All cells are PASS Q21, full Go and race/vet.

| Same-runner benchmark | First EPYC 7763 Chi / Gor | Replica EPYC 9V74 Chi / Gor | Replica EPYC 7763 Chi / Gor | Label |
| --- | --- | --- | --- | --- |
| specificity, PS, overlap `/members/me` | 1122 / 1346.5 | 833.75 / 1003.5 | 1115 / 1363.5 | **Chi lower all 3** |
| specificity, PS, single `/members/42` | 1646 / 1603.5 | 1251.5 / 1195.5 | 1642.5 / 1607 | **Gorilla lower all 3** |
| specificity, SP, overlap | 1115.5 / 1352 | 833.9 / 1003.5 | 1114 / 1360.5 | **Chi lower all 3** |
| chronology, PS, overlap | 1541.5 / 1558.5 | 1169.5 / 1144.5 | 1537 / 1553.5 | **sign varies across environments** |
| chronology, SP, single | 1650.5 / 1619.5 | 1249.5 / 1190 | 1644 / 1613 | Gorilla lower all 3 |
| build+publish, specificity, PS | 1623.5 / 16726.5 | 1245.5 / 12186 | 1621.5 / 16353 | **Chi lower all 3** |
| build+publish, chronology, PS | 1619 / 16695.5 | 1235.5 / 12169 | 1609 / 16310 | Chi lower all 3 |

Per-request allocation in **every runner**:
- specificity PS overlap: Chi **1568 B/op and 12 allocs**, Gorilla **1792 B/op and 15 allocs**.
- specificity PS single: Chi **2208 B/op and 19 allocs**, Gorilla **2096 B/op and 16 allocs**.
- build specificity: Chi **2000 B/op and 31 allocs**, Gorilla **13376 B/op and 203 allocs**.

This is a **replicated same-contract, different-workload, reversal of the measured source-repair cost-vector ranks**; at fixed Q21 the two workloads have different predicate hit/miss paths. Absolute ns/op speeds differ substantially between hosts. It is **not** a general Chi vs Gorilla conclusion: the selected research-authored adapters, finite Q21 grammar and Go httptest loop mediate the effect. This is entirely consistent with classical data structure/dispatch cost reasoning.

**Important preserved negative:** chronology PS overlap first EPYC 7763 Chi faster by ~1%, replica EPYC 9V74 Gorilla faster ~2.2%, replica EPYC 7763 Chi faster ~1%. Hence no stable absolute rank under this near-tie workload. One may NOT attribute the difference exclusively to CPU generation (VM/runner differences remain).

## MATH-9 fixed/variable lifecycle proxy recalibration (NOT observed full lifecycle break-even)

On specificity/PS/single `GET /members/42`, let `T_A(N)=median_build_A+N*median_dispatch_A` (a **model**, not measured joint N-request execution). Crossover at Gorilla vs Chi:
- first EPYC 7763: `(16726.5−1623.5)/(1646−1603.5)=355.36`, integer N≥356 in model;
- independent EPYC 9V74: `(12186−1245.5)/(1251.5−1195.5)=195.37`, N≥196 in model;
- independent EPYC 7763: `(16353−1621.5)/(1642.5−1607)=414.97`, N≥415 in model.

The **variation from ~195 to ~415 requests** across environments invalidates a universal single time break-even even under the proxy. Byte and allocation counts remain identical across these runners, yielding the same proxy crossing at **102 requests** (allocated bytes) and **58 requests** (allocation count), assuming linear accumulation and ignoring real GC interactions. For specificity/PS/**overlap**, Chi has both lower build and lower per-request measured time/bytes/allocs under these source variants, so that simplistic proxy has no Gorilla crossover.

Actual integrated build+N dispatch lifecycle measurements are REQUIRED before stating a measured crossover. The next test should freeze an N grid around those ranges and bench both modules' *whole* lifecycle with exactly matching Q21. No after-the-fact N-only selection.

## Source repair, invariant and compatibility authority

The original Chi core tree and original Gorilla ordered core route list **evolved independently**; Q21 adapters were research-authored. One added source file per original module is a valid `Γ_add` repair witness in exactly the frozen finite scope. Legacy public APIs remain unchanged and original suites/race/vet pass; new policy requires explicit caller adoption, so `Γ_add` success is not `Γ_legacy` no-migration success. The Q21 invariants are exact dual-policy winners on PS/SP and /members/me, /members/42, /outside; rejected invalid/duplicate/post-publication registration; concurrent request safety. Not validated: generic arbitrary router semantics, static-vs-param over many routes, middleware, path variable context in arbitrary nested routers, method negotiation, unlimited dynamic updates.

**Scientific verdict:** `O10_Q21_SOURCE_NATIVE_3_RUNNERS_PASS__SAME_CONTRACT_MULTI_WORKLOAD_COST_RANK_REVERSAL_REPLICATED__NEAR_TIE_TRANSPORT_FAILS__MATH9_LIFECYCLE_THRESHOLDS_MODELS_ONLY__CLASSICAL_ROUTE_COST_RIVALS_UNDEFEATED__DIP49_NEW_LAW_HOLD__LAW_R2_NOT_AUTHORIZED`.


## Subsequent independent direct end-to-end lifecycle result

[Original-Go native O11 #37972048630](https://github.com/WhoSia/EvoNOMOS/actions/runs/37972048630) finished SUCCESS 2/2, measuring real **build + N actual dispatches** on the same original module sources and frozen Q21 test, rather than summing separate median times. Full [14-point × 2-workload original source native data](P36_O11_ORIGINAL_INTEGRATED_LIFECYCLE_NATIVE_VERDICT.md). The resource cost ordering flips in generic-only case with increasing N (total bytes Chi favored at N≤64, Gorilla at N≥128; total alloc events Chi favored at N=0, Gorilla at N≥64), while a unique **time** crossover remains unsupported and median timing is nonmonotone near projected thresholds. Exactly this distinction forbids treating a linear cost proxy as an observed engineering invariant. The underlying naturally evolved cores and our project-authored adapters remain causally distinguishable.
