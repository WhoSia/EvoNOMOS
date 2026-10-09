# P36-O8 — Retrospective Natural Chi Repair vs Prospective Cross-Header Information Demand

**2026-10-10 KST · HISTORICAL RETROSPECTIVE CASE · no blind seal.** Actual naturally evolved upstream Chi source maintenance. Do NOT treat a 2026 maintainer's known correction as an independently prospective discovery or as a newly identified structural law.

## Verified upstream maintainer change

The **actual upstream commit** [go-chi/chi #1045, `05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723`](https://github.com/go-chi/chi/commit/05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723), authored February 5, 2026, changed `middleware/route_headers.go` exactly at the empty map case:
```diff
 if len(hr) == 0 {
     next.ServeHTTP(w,r)
+    return
 }
```
It separately added native upstream RouteHeaders and Pattern tests. The pinned historical v5.1.0 source `67be7d9cafdaeb4e04e887ff78d09e030ee43b00` contains the pre-fix code. The bug calls `next.ServeHTTP` once on empty routing and again after checking unmatched/default, violating a 'call exactly once' client contract. This is a real naturally developed one-line repair rather than project-authored synthetic alternative.

## Causal contrast with O7 D18

For pre-fix empty map, the necessary next step is a **control-flow early return**; all relevant data (whether map empty, next handler pointer) is present, and the fix does not alter the public `HeaderRouter map` type. A minimal line edit is enough.

For D18 cross-header *registration-order precedence*, Chi's `map[string][]HeaderRoute` representation has already discarded the chronological order of **distinct header keys**; no implementation of its `Handler` using only final map state can recover arbitrary AB vs BA order histories. Actual original Gorilla preserved ordered route list and passed D18, while Chi did not under the new optional client contract. An opt-in additive Chronological Chi API introduces new registration-order state without breaking the old public map surface. **Repair feasibility is conditional on what the representation still encodes and what API change/migration the client permits.** This is classical information conservation plus API compatibility, not a newly discovered law.

## Historical O8 test scope (added AFTER knowing the real upstream patch)

Run the same untouched Go test for exactly-one next-handler call, original pinned Chi v5.1.0 versus actual maintainer fixed commit 05f1ef7, using read-only GitHub CI and original upstream full Go/race/vet. Pre-fix expected-negative for this newly introduced test, fixed-commit positive. Original author credit to upstream maintainers; project test and CI authors human WhoSia. Record SHAs and avoid conflating historical upstream bug correction with own O7 source treatment.

## Strong competitor and negative warning

Standard bug fixing vs missing historical information already predicts these outcomes. Do not turn 'one-line fix vs new API' into design goodness rank: the demands are different, source versions differ by more than one commit, and editing authority/acceptance conditions differ. For exact causal attribution to `return`, use commit patch itself as evidence, or a matched pre-fix branch with just the one line, clearly labeled a project-authored treatment, **not** actual naturally evolved version. Version-level native tests alone cannot isolate the causal effect of a one-line patch if intervening changes are present.

**Status before native O8 run:** `ORIGINAL_MAINTAINER_FIX_IDENTIFIED__RETROSPECTIVE_NATIVE_VALIDATION_PENDING__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.


## 2026-10-10 — Post-outcome actual native upstream receipts

[Historical real-upstream original Chi CI #37968399257](https://github.com/WhoSia/EvoNOMOS/actions/runs/37968399257) is final **SUCCESS**, both historical source revision jobs. Exact test [`TestP36O8EmptyRouteHeadersInvokeNextExactlyOnce`](../../tools/p36-o8/tests/chi/p36_o8_historical_empty_router_test.go) was authored after reading the actual maintainer patch (retrospective, NOT blind). The original full Go module, middleware race, and `go vet` passed in both versions **without** the retrospective test; then the same external test was added.

- Older original pinned Chi `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`: original native exact output `P36_O8_UPSTREAM_EMPTY_MAP_DOUBLE_DISPATCH actual=2 wanted=1`, expected scientific negative; artifact id **11633644654**, ZIP SHA256 `3a897287d7c2833d8c8602b4855107b4a6f832918799d4153f5d0306d0ba79f1`.
- Real upstream maintainer fix commit `05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723`: exact same native test **PASS**, next handler called once. Original full Go/race/vet PASS; artifact **11633639780**, ZIP SHA256 `a3bb1f25a6010559ed9574959c5f46a19a75b0822b2da1222679591e17cf2187`.

The actual [upstream commit diff](https://github.com/go-chi/chi/commit/05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723) directly establishes the one-line `return` addition. Version-level tests separately confirm the associated behavioral contrast but do not by themselves isolate the single line from all intervening source changes. Earlier false technical CI statuses were NOT part of this historical O8 experiment.

**Historical verdict:** `ACTUAL_UPSTREAM_MAINTAINER_REPAIR_CONFIRMED_ON_TWO_REAL_GO_REVISIONS__RETROSPECTIVE_NOT_PROSPECTIVE__CLASSICAL_CONTROL_FLOW_AND_STATE_INFORMATION_RIVALS_EXPLAIN__LAW_R2_NOT_AUTHORIZED`.
