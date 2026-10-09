# P35-O6 — Real Original-Chi EAGER vs LAZY Publication Under Identical Maintenance Traces

**PRE-TREATMENT SEAL.** 2026-10-10 KST. P35 OPEN; LAW-R2 NOT_AUTHORIZED. This phase follows original [chat 15](https://drive.google.com/file/d/1zQ9j6GmfFaijbfz024-CQ2sJpj_SnpJV/view), [DIP-49](https://app.notion.com/p/3ccef561cf92818484a4d55302715e84) and [DIP-50](https://app.notion.com/p/3ccef561cf92811291b4c56437bc5b4b). The precise code and tests below are planned before O6 source treatment. D13 grammar testing is separate: O6 uses original normal header routing, not the research-only D11 CSV grammar.

## Concrete software and structures

Two separately authored source additions `middleware/p35_epoch_router.go` compiled into exact original upstream **go-chi/chi v5.1.0 SHA 67be7d9cafdaeb4e04e887ff78d09e030ee43b00**. The original `middleware/route_headers.go` and public Chi implementation are unchanged. Both research-only wrappers use genuine Chi `HeaderRouter.Route`, `RouteAny`, `RouteDefault`, and `HeaderRouter.Handler` on copied registries for real dispatch. These are actual compiled native Go source alternatives in an existing repository, **not two independently evolved upstream libraries** nor an upstream-accepted API. No assertion of original Chi LIVE concurrency support: direct external map mutations are expressly excluded.

Identical synchronized API: `NewP35EpochRouter(next http.Handler)`, `Register(header,match,wrap)`, `RegisterAny(header,matches,wrap)`, `RegisterDefault(wrap)`, `ServeHTTP`, `Stats() (revision,published,rebuilds uint64)`. A registry update increments revision. Each request sees every update that completed **before** the request enters its publication critical section. Simultaneous register/request overlap may linearize in either order. The frozen compiled snapshot contains copied route/rule slices and is immutable; no dispatch holds the lock through user middleware.

- **EAGER:** publish one new registry snapshot upon each completed registration; `rebuilds` increases once per such registration (excluding construction).
- **LAZY:** each update only marks a new revision. Publish one immutable snapshot on the first subsequent request if stale. Multiple updates before a request coalesce; `rebuilds` increases once per nonempty update burst followed by a request.

## Fixed oracle before source

Baseline: same 32 registered exact routes, then one probe request to guarantee baseline visibility before recording `rebuilds`. Each arm then receives 16 successful unique updates and 16 independent dispatch requests. Case 1: `U^16 R^16`; case 2: `(UR)^16`. Exactly identical U,R and accepted route-label outcomes per workload. Define `C(w)` as consumed nonempty update bursts; the exact mechanism prediction is:

| Case | U | R | EAGER extra rebuilds | LAZY extra rebuilds |
| --- | ---: | ---: | ---: | ---: |
| burst `U^16 R^16` | 16 | 16 | 16 | 1 |
| interleaved `(UR)^16` | 16 | 16 | 16 | 16 |

Also freeze: exact route correctness after completed updates (on a separate test stream), first-registration priority, wildcard/RouteAny, default fallback, sequential revision visibility, concurrent registration/read with race checks, and original full upstream module Go tests. Native `go vet ./middleware`, `go test -race -count=1 ./middleware`, `go test -count=1 ./...`; repeated microbenchmarks with `-bench`, raw throughput/allocations only (not causal claims; shared-host noise). Frozen test source precedes treatment source in Git history; CI invokes same exact frozen test for both arms and `P35_O6_ARM` selects only the predeclared numeric expectations.

## Rivals, semantics and refusal criteria

**Strong classical B-CACHE** predicts EXACTLY the same rebuild counts from write-through vs invalidation-on-read caching under these workload words. An EvoNOMOS H-epoch candidate also predicts these counts from intervention ordering and registry state. **They are observationally identical** here: `σ_q(B-CACHE)=σ_q(H-epoch)`. O6 cannot constitute a DIP-49 genuinely theory-separating law discovery. It is a native-source calibration of workload-conditioned architecture behavior, not beyond-SOLID novelty.

DIP-50 faithfulness is bounded to the new synchronized wrapper API, the declared sequential and overlap contract, frozen Go tests, and the revision/rebuild instrumentation. It does not factorize all possible lifecycle costs or all legal direct Chi APIs. Locking, compilation frequency, and route semantics are separate dimensions. Race PASS alone cannot establish linearizability for all schedules. Timings are context/executor-conditioned. A successful native O6 does not authorize LAW-R2; a failed prefix/correctness test blocks even local comparison.

Future true law discrimination requires predeclared stronger H* and B2 with genuinely different expected answers to a shared independent, realized demand, not merely different variable names explaining the same observations. Avoid making caching/obligation/locality the final explanandum.

## Next gate

After the actual source treatments and CI outcomes: bounded O6 closure (PASS/FAIL/HOLD as appropriate), selection of the next law-identification question, and only then **P36 formal name proposal** if the question shifts substantially. Do not start P36 or close P35 for administrative convenience.

## Post-source, pre-hosted-CI mathematical critic: classical cost crossover (NOT a newly presealed experiment)

The following was written after both source variants were authored but while all O6 native jobs remained QUEUED. It is a transparent theoretical calculation and **must not be counted as a preregistered, independent empirical forecast**.

Let `b>0` denote amortized work to clone and publish a registry of the fixed size range, `m>=0` the incremental LAZY dirty-marker bookkeeping per completed update, and `h>=0` the incremental LAZY revision check per request. Equal common route-dispatch cost is suppressed. Under this **simplified constant-cost model**, for `U` updates, `R` requests and `C` consumed nonempty update bursts:
```
work(EAGER) = U*b + W_common
work(LAZY)  = C*b + U*m + R*h + W_common
EAGER - LAZY = (U-C)*b - U*m - R*h
```
Therefore LAZY is lower in modeled total work iff `(U-C)*b > U*m+R*h`. In alternating `(UR)^16`, `U=C=16`, so EAGER is weakly better in this model when `m` or `h` is positive. In burst `U^16 R^16`, `U-C=15` and LAZY is lower for sufficiently costly rebuilds `15b>16m+16h`. For a dimensionless example `b=100, m=h=1`, the EAGER-minus-LAZY modeled work contrast is +1468 in burst and -32 in alternating. **Those figures are not observed Go performance.** Registry growth violates the strictly constant `b` assumption, and shared runners, allocator effects and scheduling change actual measurement. Request tail latency and update latency cannot be inferred from the scalar inequality; the former can increase in LAZY even if total work decreases.

This is a **classical lazy-cache/write-through threshold**, not a novel software-design law. If the native tests and source instrumentation succeed, O6 provides an implementation-grounded example of preference reversal under a change/request distribution. It still cannot separate a proposed new H* from B-CACHE or certify SOLID guidance.

**Conditional P36 formal-title proposal (do not open yet):** *EvoNOMOS Generation VIII LAW-R1-P36 — Prospective Structural-Law Discrimination Across Real Software: Demand-Sequence Reversals, Repair-Option Survival & Cross-Repository Transport*. Move to P36 only if a new scientific question is prospectively fixed with genuinely competing strong-theory predictions and faithful independent Go world-contact. O5/O6 implementation completion alone is insufficient.
