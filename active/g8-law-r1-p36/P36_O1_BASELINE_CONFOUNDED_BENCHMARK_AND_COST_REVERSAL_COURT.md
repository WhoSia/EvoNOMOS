# P36-O1 — Baseline-Confounding Correction, Conditional EAGER/LAZY Workload Reversal and Strong-Rival Ceiling

**2026-10-10 KST; P36 active.** This document is a **post-treatment calibration**, not blinded prospective confirmation or a new law. The user's P35→P36 flowing transition has already been effected in [P36 opening](P36_OPENING_PROSPECTIVE_STRUCTURAL_LAW_DISCRIMINATION.md).

## Real source and verified distinction

Both P35 O6 sources were committed before this measurement diagnosis:
[EAGER](../../tools/p35-o6/arms/eager/p35_epoch_router.go) /
[LAZY](../../tools/p35-o6/arms/lazy/p35_epoch_router.go).
They add two alternative synchronized publication wrappers inside the pinned original go-chi/chi v5.1.0 module, not two independently evolved original repositories. Existing [frozen original Chi O6 oracle](../../tools/p35-o6/tests/chi/p35_o6_eager_lazy_test.go) specifies same registration/dispatch behavior, 32 initial registrations, and two exact workloads each with 16U + 16R. Source timing and correctness remain distinct. Original Go hosted O6 [Actions #37951885323](https://github.com/WhoSia/EvoNOMOS/actions/runs/37951885323) remained **QUEUED** at this report; do not call it native PASS.

## Newly found measurement confound

Earlier P35 `BenchmarkP35O6Burst` and `BenchmarkP35O6Interleaved` time **the construction and first consumption of 32 preexisting routes**, in addition to 16 new updates and 16 requests. In EAGER the initial 32 registrations publish 32 times. In LAZY the initial 32 registrations are coalesced into one publication at first request. A raw benchmark difference cannot be attributed solely to the post-baseline update/read ordering. The functional frozen oracle is not wrong; its auxiliary benchmark is measuring a different *lifecycle window*.

P36 adds a **separate, post-treatment benchmark**, leaving the preregistered P35 correctness tests unchanged: [P36 source](../../tools/p36-o1/tests/chi/p36_o1_postbaseline_benchmark_test.go). It constructs 32 initial registrations and forces one initial snapshot publish **outside the timer**, then times identical 16 update + 16 request words. The original Chi read-only [Actions workflow #37954396262](https://github.com/WhoSia/EvoNOMOS/actions/runs/37954396262) runs BOTH the old cold-start and the new maintenance-only benchmarks on **both** source structures with pinned identical original Chi, vet, race, full upstream tests and job artifacts. All hosted measurements were QUEUED at creation; results have NOT been observed.

## Local source-pattern reproducer: measured, non-native, preliminary

A self-contained local Go reproduction using the *same HeaderRouter method semantics and same publication algorithms*, but **not the full untouched original Chi repository**, successfully compiled and passed `go test -race` with both arm sources. With `GOMAXPROCS=1`, `-benchtime=150ms -count=3`, and baseline initialization excluded, illustrative observed `ns/op` were:

| Local reproduction; scope-only, no CI | EAGER ns/op | LAZY ns/op |
|---|---:|---:|
| 16 updates followed by 16 requests (`U^16R^16`) | approx 63,488 | approx 50,683 |
| 16 alternating updates+requests (`(UR)^16`) | approx 62,736 | approx 68,439 |

These figures are **not original Chi hosted numbers**; they are short local checks on one machine with timing noise and frequent bench timer toggles. They are not statistically independent causal samples and are not a publication-grade performance estimate. Their purpose is to reveal which measurement comparison must be made next and check sign feasibility. Raw allocation numbers also differ between workload treatments.

## Conditional classical cost model

Let `b_i` denote actual registry snapshot rebuild work after the i-th update (may vary with size); `m_i` per-update lazy bookkeeping, and `h_j` per-request lazy revision/publish check. For exact workloads with different rebuilt subsets `I_E` and `I_L`, conditional model:
```
DeltaWork := Work(EAGER)-Work(LAZY)
           = sum_{i in I_E} b_i - sum_{i in I_L} b_i
             - sum_{i=1}^U m_i - sum_{j=1}^R h_j + residual
```
Residual includes placement-sensitive contention, branch costs, Go allocations, GC, request dispatch and any nonidentical implementation interactions. Under constant `b,m,h` and no residual this reduces to P35's classical `(U-C)b-Um-Rh`. The **same total operation counts do not imply the same timing distribution or preference ordering**. A short local sign reversal is consistent with this classical model, but does not independently estimate b/m/h nor prove the model universally true.

## Strong-rival scientific boundary and required next move

Classic eager publication/lazy invalidation and workload batching already predict reduced extra rebuilds for burst sequences and no rebuild-count saving under strict interleaving. A source-backed sign reversal may be useful practical conditional design guidance, but absent prospective model-pair separation it is **not** a novel beyond-SOLID software law. Native O6 and P36 O1 must first be independently verified; full original Go CI/race, method-value tests, benchmark receipts. Then seek a real **semantically equivalent** pair of independent source implementations and new future demands whose predictions diverge from the best classical repair/abstraction/caching explanation, not different theory labels for equal signatures.

**Verdict now:** `P36_OPEN__P35_CLOSED__LOCAL_SCOPED_MEASUREMENT_SIGN_REVERSAL_OBSERVED__NATIVE_ORIGINAL_CHI_BENCHMARK_QUEUED__CLASSICAL_EXPLANATION_UNDEFEATED__LAW_R2_NOT_AUTHORIZED`.

## 2026-10-10 KST — Original Chi P36-O1 Native Source and Scoped Benchmark Receipt

**This supersedes earlier QUEUED snapshots as an execution result, not the preregistered hypotheses or the mathematical scope.** [Original Chi hosted Actions #37954396262](https://github.com/WhoSia/EvoNOMOS/actions/runs/37954396262) has final `completed/success`, two of two jobs SUCCESS. Both variants were sourced from their exact previously published original-Chi insertion files and compiled in upstream `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`; `go vet`, middleware race and original Go full tests succeeded. Both jobs ran the identical old lifecycle and new post-baseline `BenchmarkP36PostBaseline*` tests with `GOMAXPROCS=1`, `-benchtime=250ms -count=5 -benchmem`. The two raw artifact ZIPs were downloaded and inspected:

- EAGER artifact `11630317058`, ZIP SHA256 `370a41e1a74d01c113ce03f653ac03bfb37be214a76dbb909c5fca3be3025006`, runner AMD EPYC 7763. Post-baseline Burst raw ns/op: `79584,78384,79529,76571,80018` (**median 79529**), allocations `160014 B/op, 417 allocs/op`. Interleaved: `73846,74879,82428,81870,80782` (**median 80782**), `159758 B/op, 401 allocs/op`.
- LAZY artifact `11631347148`, ZIP SHA256 `4cd8c78c711e12a644412c351a5a42c602c248e0e452003a75f3cd9074ea514c`. Post-baseline Burst ns/op: `61984,62903,66161,62840,66072` (**median 62903**), `107962 B/op, 357 allocs/op`. Interleaved `83984,84413,85522,77786,80837` (**median 83984**), `159759 B/op, 401 allocs/op`.

**Descriptive observed median pattern:** LAZY faster in burst (62.903 µs versus EAGER 79.529 µs) and EAGER faster under interleaved updates/requests (80.782 µs versus LAZY 83.984 µs). The timing difference under interleaving is small (3.202 µs, around 3.8% relative to LAZY), and **the raw five-repeat ranges overlap**. Each arm was a distinct hosted job, not a randomized paired same-runner experiment, so statistical inference and unconditional Pareto ordering remain **HOLD**. Burst also has a clear allocation difference; interleaved allocation counts are effectively identical. In this narrow measured window, Go original source-level *median signs* agree with prior small local reproduction. This is a real native **conditioned pattern**, not yet a robust controlled performance experiment.

**Classical rival:** The eager snapshot builder performs 16 work-generating updates; lazy coalesces them to one for batch. Under strict alternation both compile 16, so publication check placement and residual costs can affect the sign. This is understood by classical cache invalidation and amortized performance engineering. No beyond-SOLID law identified; `DIP49_STRONG_PAIR_NOT_SEPARATED` and `LAW_R2_NOT_AUTHORIZED` remain.

**CI verdict:** `P36_O1_ORIGINAL_CHI_HOSTED_POSTBASELINE_NATIVE_PASS__DESCRIPTIVE_MEDIAN_SIGN_REVERSAL__INFERENTIAL_PREFERENCE_HOLD__CLASSICAL_CACHING_UNDEFEATED`.
