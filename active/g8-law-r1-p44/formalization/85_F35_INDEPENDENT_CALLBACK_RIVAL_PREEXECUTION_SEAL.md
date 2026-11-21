# P44-F35 R1 — Independent Callback Rival Re-test: PRE-EXECUTION SEAL (2026-11-21)

**STATUS: PRE-IMPLEMENTATION / NO NEW PASS YET / LAW-R2 HOLD / G1–G7 OPEN**

## 1. Source-critical finding from F34

In `active/g8-law-r1-p44/f34_original_router_capability/router_test.go`, the test called `TestCallbackRivalMatchesInterfaceSelection` defines:

```go
iface := Pick(handlers)
callback := func(w http.ResponseWriter, r *http.Request) { iface(w, r) }
```

The `callback` invokes the very selector whose output it is supposed to challenge. Equal output is a self-forwarding control, **not an independently implemented competing dispatch policy**. The F34 report's bounded original-router tests remain genuine, but its separate claim of an independently implemented callback rival is inadequately tested. This note is a correction of evidence quality, not a claim of a software defect in chi or httprouter.

## 2. Precommitted falsifiable test

Build a **distinct application-owned callback selector** that does not call `Pick` or the original selector. It receives `map[RouterKind]func(http.ResponseWriter, *http.Request)`, selects a callback by the request's `X-Router` header, and explicitly rejects unknown/missing keys with HTTP 400. Both implementations may still invoke the same unmodified original-router handlers through different wrappers; the separation concerns the app-owned selection code, not the original routing algorithms.

Freeze comparison cases BEFORE code:
- chi + v1, httprouter + v2; `GET /legacy` => 200/`old`;
- `GET /item/a`, `GET /item/abc` => 200 with expected version prefixes;
- uppercase `CHI` must normalize to chi;
- missing and unsupported header => 400;
- 32 concurrent requests alternating providers: no cross-provider result;
- deliberately faulty callback replacing the chi result must create an observed mismatch (negative control, **not** a failing CI test).

Outcome: compare status and body under the above bounded inputs, and explicitly verify the callback selector implementation is a separate function not forwarding into `Pick`. A passing test shows **bounded application dispatch parity**, not architectural superiority, future-maintenance equivalence, all-client bisimulation, performance equality, or verified owner rights.

## 3. Conditions for a fair design-rival study

F34 already uses real pinned `go-chi/chi@v5.1.0` and `httprouter@v1.3.0`, but the two original libraries are different router implementations, and their source was not edited. The strengthened callback test must not confuse a separately expressed `http.HandlerFunc` with an alternative end-to-end type system free of interfaces: original handlers remain `http.Handler` values.

Later studies should compare **typed function bundles versus interface injection**, initially matched under both current behaviors, against independent future maintenance tasks and true edit scopes. Each rival must be source-independent, tested with a negative control, and receive identical evidence, actor rights, toolchain and cost rubric. If a strong rival ties, mark TIE.

## 4. Research status

This preseal is a static F34 source audit and proposed test, no claim of execution. Implement the file as a separate source commit, run the existing read-only original-Go GitHub workflow, record the exact workflow result and preserve any failures. No new LAW-R2 promotion.
