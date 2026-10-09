# P36-MATH-9 — Same-Q21 Life-Cycle Cost Crossover Under Different Valid Workloads

**2026-10-10 KST · P36 OPEN · POST FIRST ORIGINAL-GO Q21 RESULTS / BEFORE O10R REPLICATION READBACK. This is classical fixed-plus-variable amortization, not a novel law or measured physical crossover.**

## Unit-consistent, contract-correct cost objects

Original Chi and original Gorilla, both using specifically authored additive Q21 API source repairs, passed the SAME presealed functional contract under the first native CI [#37970800075](https://github.com/WhoSia/EvoNOMOS/actions/runs/37970800075). We measured **build+publish once** and per-request dispatch, each in independent Go benchmark loops on the same host. For a homogeneous request workload `w` and N requests, define an **approximate analytic proxy**, in nanoseconds:
```
T_A(N;w) := median_go_build(A) + N * median_go_dispatch(A;w).
```
Likewise `M_A(N;w):=Bbuild_A+N*Bdispatch_A` in allocated bytes and `K_A(N;w):=alloc_build_A+N*alloc_dispatch_A` in count of allocations. These are **additive projections built from separate benchmarks**, not observed joint lifecycle traces; they ignore GC coupling, warmup/cache, concurrency, tail latency, initialization dependencies and migration costs. `N` is dimensionless and measures the chosen workload's request count, not elapsed time. The benchmark includes `httptest.NewRecorder()` inside dispatch loops on both sides.

## First-run data from Q21 specificity policy, PARAM registered first

Same EPYC 7763 runner, 10 raw Go benchmark repetitions per variant from counterbalanced two library-order blocks:
```
build:   Chi 1,623.5 ns,  2,000 B,  31 allocs
         Gorilla 16,726.5 ns, 13,376 B, 203 allocs

w=overlap GET /members/me: Chi 1,122.0 ns, 1,568 B, 12 allocs
                           Gorilla 1,346.5 ns, 1,792 B, 15 allocs

w=single GET /members/42: Chi 1,646.0 ns, 2,208 B, 19 allocs
                           Gorilla 1,603.5 ns, 2,096 B, 16 allocs
```
For **overlap**, Chi is smaller on all *measured* fixed and incremental dimensions, so this simple proxy shows **no positive N crossover** for Gorilla. This does **not** establish Pareto dominance over migration, all client methods, error semantics or memory residency.

For the **single generic-only match** despite same policy/functional contract:
```
ΔT(N) := T_Gorilla(N) - T_Chi(N)
       = (16,726.5 - 1,623.5) ns
         + N * (1,603.5 - 1,646.0) ns/request
       = 15,103 ns - 42.5 N ns.
```
Hence a purely *model-implied* crossover at
```
N_T* = 15,103 / 42.5 ≈ 355.36 requests
```
(**Gorilla lower** for integer N≥356 *in that proxy*). Separately, bytes and allocation counts have different crossing scales:
```
ΔM(N) = 11,376 B - 112 N B
=> N_B* = 101.57 requests (integer 102);

ΔK(N) = 172 allocs - 3 N allocs
=> N_K* = 57.33 requests (integer 58).
```
**Important:** these are **not** three observed “break-even points”; they are numerical implications of assuming linear composition of benchmark medians with constant per-request costs. They also do not incorporate any costs of moving clients to the new opt-in API. Future actual end-to-end N-sweep is needed to test if T(N) truly approximates joint lifecycle behavior.

## Conditional structural insight, and strongest rival

The same functional contract `Q21` admits opposing allocation and weak timing dispatch preference signs when the input workload changes between overlapping and generic-only requests. The exact source mechanism is obvious under classical routing/evaluation: Chi add-on checks a list of real mini-Mux route matchers; Gorilla add-on delegates to a single original route-list Mux configured in a different order; negative predicate tests and separate core matching costs differ. The selected adapter implementations are a confound. Even a confirmed multi-runner cost sign reversal is not a beyond-classical law.

The stronger reusable research program is **function-and-authority-indexed lifecycle reachability and vector-valued cost**:
```
For fixed Q, Γ, c, route distribution μ:
  Feasible(B;Q,Γ) first,
  then compare (build, dispatch, allocations, migration)
  among eligible B across controlled μ and N.
```
A static per-request 'best' and a per-lifecycle 'best' can disagree without any surprising new mathematics. What may be novel later would require a *prospectively separable stronger rival prediction* on independently evolved systems after controlling known memory/route matching costs, not this simple threshold.

[O10R pre-replication seal](P36_O10R_TWO_RUNNER_COST_SIGN_REPLICATION_PRESEAL.md) was committed after initial medians were read, before new runner data. **If replication changes the weak ~2.6% single-match time sign, the 356-request time proxy loses empirical support in that environment.** Preserve that negative instead of promoting an unconditional threshold.

**Court:** `CLASSICAL_LINEAR_LIFECYCLE_BREAK_EVEN_EXPLORATORY__SAME_Q21_NATIVE_PASS__INDEPENDENT_CPU_REPLICATION_PENDING__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.


## Independent cost replication and direct integrated-lifecycle challenge

[Native O10R two independently hosted matched original-module runners #37971308882](https://github.com/WhoSia/EvoNOMOS/actions/runs/37971308882) **2/2 SUCCESS**, after the first-run cost sign predictions were frozen. Both full original Go/race/vet/Q21 PASS and identical source/test SHA. Exact [O10R two-runner raw cost receipt](P36_O10R_TWO_INDEPENDENT_RUNNERS_NATIVE_COST_VERDICT.md). On specificity/PS overlapping request, Chi dispatch has lower latency and allocations in **all three** physical runner sessions; on specification/PS generic-only request, Gorilla has lower dispatch latency and allocations in **all three**, under the SAME Q21. The chronology/PS/overlap near tie **switches sign** across runners; no stable universal ranking.

The simple linear setup+N*request latency proxy predicts three distinct generic-only break-even counts: ~355.36 requests (first EPYC 7763), ~195.37 (EPYC 9V74) and ~414.97 (other EPYC 7763). Byte and allocation model-only crossings 102 requests and 58 requests are stable across these runs. **None** is a measured integrated lifecycle threshold.

[O11 integrated lifecycle grid was preregistered before O11 benchmark code](P36_O11_INTEGRATED_LIFECYCLE_FINITE_N_GRID_PRESEAL.md): freeze N={0,64,128,256,384,512,1024}, specificity/PS, both Q21-legal requests single and overlap; time **whole operation** of fresh handler build + N requests with same recorder construction, on two fresh runners counterbalancing Chi/Gorilla source order. [Native O11 CI #37972048630](https://github.com/WhoSia/EvoNOMOS/actions/runs/37972048630) **PENDING at this inscription**. The work explicitly tests whether addition of *separate* first-run medians predicts real integrated source behavior, not just a ratio from arithmetic.

**Mathematical caution:** a conditional Pareto ordering on dispatch-cost vectors under a specified workload is no universal total order on software design; a different workload can reverse it without violating classical cost theory. Maintain `DIP49_HOLD / LAW-R2_NOT_AUTHORIZED`.


## Direct original-Go lifecycle outcome: allocation threshold survives, precise timing threshold does not

The separately sealed [O11 integrated build+N original Go experiment](P36_O11_INTEGRATED_LIFECYCLE_FINITE_N_GRID_PRESEAL.md) finished [native 2 independent runners SUCCESS #37972048630](https://github.com/WhoSia/EvoNOMOS/actions/runs/37972048630). Full [per-N raw medians, source hashes and ZIP receipts](P36_O11_ORIGINAL_INTEGRATED_LIFECYCLE_NATIVE_VERDICT.md). Each lifecycle operation constructs a brand-new frozen Q21 adapter and performs N requests for N∈{0,64,128,256,384,512,1024}; both original Chi and Gorilla full Go/race/vet/Q21 PASS without changing original source or previous treatments. The previous additive model's time break-even values ~195/~355/~415 requests are **not validated observed lifecycles**: on EPYC 9V74 generic-only Gorilla is faster at N=384 and N=1024 but Chi slightly faster at 512; on EPYC 7763 Chi remains slightly faster on observed timing through 1024. Gaps near crossovers are tiny and independent GPU/CPU/runner replication is limited. Do not conclude a unique time threshold from such nonmonotone medians.

The **actual integrated allocation** comparison is more stable: under the SAME specificity-PS Q21 but generic-only input, Chi uses fewer TOTAL B/op for N≤64, Gorilla less for all tested N≥128, on two independent runners. Chi uses fewer total ALLOCATION COUNT at N=0, Gorilla at N≥64. Thus the original model-only thresholds ~102 B-break-even and ~58 allocation-count-break-even have become **observed crossing intervals** (64,128] and (0,64], respectively, not measured precise integer thresholds. For Q21 overlapping static input Chi is smaller in timing, total bytes and total allocation count at **all tested N** in both runners.

The richer lifecycle estimand is **vector-valued** `C_A(N;Q,Γ,w,c)=(time,bytes,alloc_count,migration,..)`; the sign of differences may depend on which coordinate is optimized. A separable model `C^proxy(N)=C^build+N C^dispatch` is a useful classical first approximation but a full execution may include `G_A(N,w,c)` for GC, allocation and cache interactions. **The data do not uniquely identify the G term:** separate and integrated benchmarks were not one randomized joint causal experiment and runner load differs. Do not infer a unique Go GC mechanism from residuals alone.

The finding remains a **source-adapter-conditioned, finite-workload cost phenomenon explained by classical engineering**, not a new software law. `DIP49_IDENTIFICATION_HOLD`.
