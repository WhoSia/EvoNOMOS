# P44-F36 R2 — Post-Construction Selector-Map Aliasing: Pre-Execution Falsifier

**2026-11-21. SOURCE INSPECTION + PREDICTION ONLY / NO TEST OUTCOME YET. LAW-R2 HOLD.**

## Original-source basis and historical context

F34 source `active/g8-law-r1-p44/f34_original_router_capability/router.go` defines `Pick(handlers map[RouterKind]http.Handler)`. Its returned handler function retains the provided map value in a closure and reads `handlers[kind]` on **each request**. Maps are reference-like in Go, so replacing a map entry after creating the selector can change which provider receives a later request. F35's independent callback picker does the same with `map[RouterKind]func(...)`; its concurrent test only performs concurrent reads, not concurrent mutation.

This is *not an inherited failure of chi or httprouter*. The potential mutation is in application-owned policy map configuration. Jones (1981, Ch.4) and Brookes (2004) already teach that client guarantees under interference depend on environment/rely assumptions and heap ownership; no new concurrency frame theorem is claimed here.

## Frozen predictions

Use **sequential** reassignment only; no data race and no unsupported concurrency experiment.

- A: Build chi `v1` and `v2`, initial map `Chi: v1`, construct `Pick(map)`; pre-mutation `GET /item/x` with `X-Router:chi` produces `v1:x`; replace `map[Chi]=v2`; post-mutation request produces `v2:x`.
- B: Do the same through the separately implemented F35 callback selector with `map[Chi] = v1.ServeHTTP`, then `v2.ServeHTTP`; expect `v1:x` then `v2:x`.
- C: Independently implement an app-owned *snapshot callback picker* that copies the map once at construction, does not call `Pick` or the original independent callback picker. After changing the original input map, it must retain `v1:x`. Neither baseline map after mutation is immutable; a snapshot copy is a deliberately **stronger competing implementation**, not an observation of F35.
- D: Control cases include `GET /legacy` returning `old`, and a missing router header producing `400`; test must explicitly report the difference between old client observer `/legacy` and new version-specific observer `/item/x`.

If this prediction holds, the correct finding is **selector configuration aliasing makes outputs dependent on a post-construction edit**. The standard `GET /legacy` observer is too weak to distinguish these provider versions. This demonstrates a *scope gap in our old-client probes*, not a general unsafe concurrency claim and not proof one style is universally better.

## Failure, admission and novelty gates

- The snapshots must be constructed from the same two original pinned router implementations as F35. `go.mod`/`go.sum` unchanged and read-only `go mod verify`, `go vet`, `go test` and race CI required.
- Negative behavior is expected by tests, so the test itself should **PASS only if it observes the intended change**. If the mutable-map selector is unexpectedly stable, report mismatch; don't silently flip the hypothesis.
- Do not mutate the maps while requests are in flight, claim a data-race discovery, or attribute changes to the router dependencies.
- Do not infer either selector meets an unspecified old-client guarantee. Under an explicit “snapshot routing once published” contract, A/B fail and C passes, but the contract is **authored by us**.
- If a strong snapshot rival solves the same task by ordinary map copying, classically-known frame/copying suffices. **P44 novelty remains HOLD**, as do G1–G7.

**Test implementation and any outcome must arrive in separately subsequent commits.**
