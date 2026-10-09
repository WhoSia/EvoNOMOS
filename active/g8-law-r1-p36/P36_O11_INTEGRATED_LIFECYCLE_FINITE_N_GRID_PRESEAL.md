# P36-O11 — Direct Build-plus-N-Requests Lifecycle Cost Falsification on Two Original Go Routers

**2026-10-10 KST · PROSPECTIVE INTEGRATED-LIFECYCLE SEAL, AFTER O10+O10R BENCHMARK OUTCOMES BUT BEFORE O11 CODE AND OUTCOME. P36 OPEN.**

## Why an independent action is required

Original pinned Chi and Gorilla Q21 additive source repairs [O10](P36_O10_IDENTICAL_CONTRACT_NATIVE_REPAIR_AND_COST_VERDICT.md) both pass the exact SAME fixed policy-selection API, original Go full/race/vet. [Two independent host replicas O10R](P36_O10R_TWO_INDEPENDENT_RUNNERS_NATIVE_COST_VERDICT.md) reproduce Chi's faster overlapping case and Gorilla's modestly faster generic-only case (same Q21, different valid request workloads); chronology-PS near-tie sign changes with host. Raw microbenchmarks timed **build** and **dispatch** separately. Simply adding their median values is **not a measured end-to-end lifecycle**.

[MATH-9](P36_MATH_9_SAME_CONTRACT_LIFECYCLE_BREAK_EVEN_AND_RESOURCE_VECTORS.md) proposed a *linear descriptive proxy* `T_A(N)=B_A+N*L_A` for source A under homogeneous Q21 request workload, not an observed result. Original Go runner models estimate a generic-only request count crossover at N≈355 (first EPYC 7763), N≈195 (independent EPYC 9V74), N≈415 (independent EPYC 7763). All are calibrated **post-O10**; O11 tests directly whether the proxy predicts real integrated source/runner lifetime times.

## Frozen source & single semantic Q

No treatments changed. Exact original upstream Chi pin `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`, Gorilla pin `b4617d0b9670ad14039b2739167fd35a60f557c5`. Add the exact previously committed one-file additive Q21 adapter source and frozen Q21 tests to each original package. O11 introduces a **new benchmark-only Go file**, in each original module, identical except package declaration, without modifying old/original source/treatment/frozen Q21 test.

Shared Q21: policy `specificity`, PARAM registered first followed by STATIC; GET `/members/me` must yield STATIC, GET `/members/42` must yield PARAM, `/outside` 404. The same Q21 semantic contract continues to hold; two *input workloads* differ, not client functionality.

## Exact integrated measurement and preregistered N grid

One **benchmark operation** is defined as:
1. **Build** a fresh identical Q21 source adapter (constructor + both route registrations + Handler publication).
2. Process `N` identical GET requests using that published Handler, allocating `httptest.NewRecorder()` **per request**, with the request itself precreated outside the timed loop (as in O10).
3. The Handler is retained until after benchmark loop to prevent dead-code elimination.
4. The source, test, Q21 and benchmark workload is identical for Chi and Gorilla, and original full/race/vet/Q21 still PASS before benchmark. No concurrent registration, no middleware, no arbitrary patterns.

Frozen N values `[0,64,128,256,384,512,1024]`, for **both** Q21-legal workloads: `single=/members/42`, `overlap=/members/me`. 14 pairs per original module. Report `ns/op` **per entire lifecycle operation**, `B/op` and `allocs/op` **per entire operation**, not per request. Exact sorted cell names `BenchmarkP36O11Lifecycle/(single|overlap)/N0000...`. Run 2 fresh Actions VMs, with within-VM library order counterbalanced across two blocks (CHI→GORILLA and GORILLA→CHI), `GOMAXPROCS=1`, `-benchtime=150ms -count=5 -benchmem -cpu=1`, raw log/CPU/source SHA immutable artifacts. Observe hardware differences; never pool raw timings across unrelated CPUs to invent universal cutoffs.

## Prospective predictions (calibrated after first O10, **not** novel or blind)

- `w=overlap`: previous measured Chi has both lower build cost and lower per-request dispatch cost; under additive proxy it remains lower at every N. This is predicted but must be compared with integrated measurements.
- `w=single`: prior calibrated additive proxy predicts Chi lower at small N, Gorilla lower at large N. In particular `N=64` expected Chi advantage and `N=1024` expected Gorilla advantage on either CPU environment. `N=256` crosses first model threshold only on EPYC 9V74, not earlier EPYC 7763; this is a **conditional prediction**, not an exact CPU-only causal attribution.
- Byte and allocation count model thresholds `N=102` and `N=58` for Gorilla to offset build costs in generic-only workload under the simple additive component model; benchmark-generated behavior and recorder allocations may differ.
- **Crucial alternative:** actual integrated cost may differ from proxy because of GC/scheduler/thermal effects, caching or dynamic allocation and cost correlation. Such counterevidence is not a reason to modify N-grid/tests.

## Honest scientific inference

Even if integrated lifecycle preference changes at an observed N, the mechanism remains well described by **classical fixed setup vs variable per-request costs** under this research-authored pair of adapters. The causal explanation includes how the new Chi source uses per-route real `chi.Mux.Match` and how Gorilla creates a single route-list `mux.Router` with regexp compilation. The source architectures are naturally evolved, but the two Q21 adapters are **chosen treatments** and may be nonoptimal. This is not an independent law defeating classical amortized analysis or a universal scaling theorem.

No statistical significance from correlated Go benchmark repeats alone. Don't claim a physical request threshold until integrated logs are read. If the predicted crossover fails, write negative evidence and inspect source/context before a new sealed experiment.

**Pre-code verdict:** `P36_O11_INTEGRATED_LIFECYCLE_14_CELLS_FROZEN__ORIGINAL_GO_SOURCE_UNCHANGED__NATIVE_UNTESTED__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
