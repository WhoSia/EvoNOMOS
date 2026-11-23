# R81 — Prespecified native Go cost-mechanism comparison

- **Timestamp/context:** 2026-11-23; created before R81 benchmark measurements.
- **Research status:** exploratory mechanism measurement, **not** independent human maintainability evaluation, not a test of ATLAS's scientific novelty.
- **Inputs:** GitHub `main` fixed D8 Go implementations only: `d8/live/route_headers.go` blob `e481e73aa1d82497c25011b6468d7e8749c705f7`; `d8/snapshot/route_headers.go` blob `66e88964508cedc38740913a7c00fbf5b6e6220a`.
- **Workload:** 128 inactive registered header routes and one matching `X-ZZZ: ping`, deterministic 129 route entries. Benchmark one handler created once per iteration corpus, versus constructing the handler repeatedly. Both candidates must satisfy fixed D8 and temporal regression checks separately.
- **Primary endpoints:** `ns/op` and `allocs/op` separately for `BenchmarkR81SteadyLookup` and `BenchmarkR81ConstructHandler`; secondary `B/op`.
- **Plan:** isolated package, Go 1.23.2, `GOPROXY=off`, benchmark `-benchtime=200ms -count=5 -benchmem`, plus `-race` regression tests separately. Repeat each implementation with alternating order across available rounds where feasible; report raw repeated results, median and range; never infer significance from dependent microbenchmarks.
- **Expectation:** The frozen copy may reduce repeated lookup overhead at the cost of more per-handler construction work, but this is an unconfirmed mechanistic hypothesis, not an outcome asserted before measurement. If the observed pattern differs, preserve the unexpected result.
- **Exclusions:** no concurrency/mutable-map race claims, no throughput under realistic production traffic, no power calculation, no independent external replication, no human cognitive/work cost, no proof that either architecture is globally superior.
- **Invalidity gate:** a differing workload, failed D8 contract, modified Go sources, CPU or GC state confounding, or inconsistent benchmark setup invalidates comparative inference.
- **Research stop decision:** even a strong computer-time advantage is insufficient to reinstate ATLAS originality or Paper B; any additional study should target independently evaluated review accuracy/time under a strong rationale baseline.
