# P44-F37 R2 — Two Source-Separate Architecture Arms, Frozen Initial Oracle: Native Go CI Verdict
**2026-11-21 · BOUNDED BASELINE PASS · PROSPECTIVE DEMAND NOT REVEALED · LAW-R2 HOLD / G1–G7 OPEN**

## Auditable sequencing

1. [Pre-implementation requirements and oracle seal](./94_F37_TWO_INDEPENDENT_ORIGINAL_GO_ARMS_PREEXECUTION_SEAL.md), [commit `3fd71c6`](https://github.com/WhoSia/EvoNOMOS/commit/3fd71c6ba9e2ccd64dfa1ac57f62e8f1bcab49aa).
2. [Interface-owned `handlerarm` source](../f34_original_router_capability/f37arms/handlerarm/handlerarm.go), [commit `3ade63e`](https://github.com/WhoSia/EvoNOMOS/commit/3ade63ed77447e5d7269ea169b7df8ca75626106).
3. [Function-owned `callbackarm` source](../f34_original_router_capability/f37arms/callbackarm/callbackarm.go), [commit `260c885`](https://github.com/WhoSia/EvoNOMOS/commit/260c8851824e31641de008e47ee75359b508e518).
4. [Separate authored expected-output tests, isolation probes and sensitivity control](../f34_original_router_capability/f37_baseline_parity_test.go), [commit `4cc2fb3`](https://github.com/WhoSia/EvoNOMOS/commit/4cc2fb302888ecbe72f6a683d97eff18378b261a).
5. [Native GitHub Actions #44908134492](https://github.com/WhoSia/EvoNOMOS/actions/runs/44908134492), **SUCCESS**, tested exact git SHA `4cc2fb302888ecbe72f6a683d97eff18378b261a`, job `136858003280` (`native-original-routers`). Source pin and toolchain identity, native dependencies, `go mod verify`, `go vet -mod=readonly ./...`, `go test -mod=readonly -count=1 -v ./...`, `go test -mod=readonly -race -count=1 ./...` all succeeded. Workflow had read-only GitHub permissions and no bot-authored commit.
6. Decoded raw job logs were fetched and inspected. `TestF37IndependentArmsMeetFrozenInitialOracle` and its **10 named subtests** PASS, and `TestF37IndependentArmsConcurrentReadOnlyProviders` PASS. The F35/F36 named tests and original F34 tests still pass.

## What is actually shown

The separately written packages have **no shared research application selector source**: one `handlerarm` dispatches through `map[Kind]http.Handler` and the other `callbackarm` through `map[Kind]func(http.ResponseWriter,*http.Request)`. Each creates original `go-chi/chi@v5.1.0` and `httprouter@v1.3.0` router instances, with identical frozen baseline routes `GET /legacy` and `GET /item/{id}`. No upstream source was modified.

The independent *expected-value oracle* (not just cross-arm agreement) checked exact old `old` response, versioned item responses, uppercase provider labels, invalid headers yielding 400/`unknown router\n`, and 404 for unknown paths. Both packages passed. Creating a second instance with different provider labels left the earlier instance's responses unaffected. Concurrent read-only requests (32 per arm) passed under normal and Go race CI. A deliberately corrupted `/legacy` test wrapper must differ from the expected old output; that internal sensitivity check passed.

**Identity limits:** The two source arms were both written by the same research process from one baseline protocol. “Independent” here means *source-disjoint application dispatch, with no calls to each other's selector*, not independent authorship or independently selected tasks. Both rely on upstream `http.Handler` implementations and Go's `http.HandlerFunc` adapter. The test only probes a finite matrix and cannot establish all-request/contextual equivalence.

## Critical boundary: future demand and source repair still NOT TESTED

This baseline is one evidence step toward a valid comparison, not a repaired third-party issue. The research process itself selected the baseline; **no external party had authored or frozen a future requirement prior to measuring costs**. The old clients and allowed edit boundaries for such a demand have not been authenticated. No future source edit, PR acceptance decision, implementation effort, permissions, tool failure or matched-information historical rival was evaluated.

In particular, it would be improper to infer that interface dispatch is universally superior/inferior to callbacks because the toy baseline programs happen to pass the same HTTP requests. An issue might require versioned routing, config freezing, path-constrained authorization, request metadata, or unrelated changes; which architecture is easier depends on the task, protected caller routes and allowed edits. Setup LOC and abstraction overhead must be counted when comparing.

## F38 gate protocol

1. Freeze this passing baseline commit before disclosing the next task.
2. Record an **independently authored existing requirement/issue**, with its historical timestamp and source. Document whether task selection was made with or without access to the arm differences, and avoid calling a selected task blind when the researcher chose it.
3. Document which actor can actually edit which files. A writable fork is not evidence of permission in an upstream maintenance project.
4. Give both arms identical task text, code context and test-oracle quality; require a documented pre-task forecast and *strong classical competitor* (simple function dispatch, conventional adapter, source-aware static alias/frames) with equal evidence.
5. Execute both proposed edits and compile/test. Count old/new file deltas, setup, verification, failures, manual hours, and any deferred/unresolved obligations. Include negatives. Classical tie is an important permitted verdict.
6. If independent demand or authenticated permissions are unavailable, stop at matched baseline readiness; **LAW-R2 HOLD**.

**Director's ruling:** F37 is a reproducible, source-separated, behavior-matched *baseline* with raw native Go CI; its main contribution is to avoid comparing a purpose-built flexible implementation with an unrelated weaker original. F37 has not established predictive architectural value or original new mathematical law.
