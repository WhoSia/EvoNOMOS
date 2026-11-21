# P44-F37 R1 — Independent Architecture Arms: Pre-Implementation Equivalence Seal (2026-11-21)

**PRE-EXECUTION / NO NEW PASS / FUTURE-DEMAND BLINDNESS NOT YET DEMONSTRATED / LAW-R2 HOLD / G1–G7 OPEN**

## Why not another map-mutation toy?

F36 already showed that both interface and callback selectors capture mutable configuration maps, and that a basic snapshot copy can defeat a post-construction map update. This is ordinary alias/capture semantics, not a first theory of source repair. Its old `/legacy` probe could not observe provider-version changes that `/item/x` did. The next relevant work is to **freeze two genuinely separately implemented application architectures at the same initial externally observable capability** before a future independently authored task can be chosen. This record precommits to the baseline before source code is written.

## Artifact and actor boundary

We use unchanged original `github.com/go-chi/chi/v5@v5.1.0` and `github.com/julienschmidt/httprouter@v1.3.0`. New *researcher-authored application* sources live in separate Go packages:

1. `f37arms/handlerarm` constructs original routers and dispatches through `map[Kind]http.Handler`, using the original `ServeHTTP` call; the exported constructor returns `http.Handler`.
2. `f37arms/callbackarm` separately constructs original routers and dispatches through `map[Kind]func(http.ResponseWriter,*http.Request)`; the exported constructor returns a **function**, with conversion to `http.HandlerFunc` allowed only within the test witness to apply identical HTTP requests.

The two packages must **not** call `originalrouters.Build`, `Pick`, `independentCallbackPicker` or one another. Both independently implement the same two original upstream route registrations; share only the Go standard library and the same untouched upstream pinned libraries. No router internals are copied or edited. As `http.Handler` still exists in upstream routers and `http.HandlerFunc` adapts functions to the HTTP server, `callbackarm` is an *application-owned dispatch rival*, not a claim of end-to-end interface-free architecture.

Source baseline and module file lock: `go.mod`, `go.sum` unchanged; Go v1.23.2 pinned on CI; different source files and separate packages are maintained without a shared helper that would collapse the comparison.

## Initial acceptance oracle, fixed BEFORE writing code

Use `chi:v1` and `httprouter:v2`; two separate constructed app instances with `chi:v3` and `httprouter:v4` must not change the first app's behavior.

Input matrix: `GET /legacy`, `GET /item/a`, `GET /item/abc`, `GET /missing` with `X-Router=chi,httprouter,CHI,HTTPROUTER` as applicable. Require:

- old route always 200 with exact body `old`;
- item route always 200 with exact version+identifier body (for chi `v1:a`, for httprouter `v2:a`);
- missing path returns the original router's 404 status in both arms (body equivalence tested if stable across original upstream routers);
- absent and unsupported `X-Router` produce HTTP 400 and exact `unknown router\n`;
- concurrent **reads of immutable constructed app instances** keep outputs independent (32 requests; race test);
- one deliberately corrupted callback inserted **only in a test witness** must be detected against independently specified required old response; this is a positive sensitivity check, not evidence of new code behavior.

The exact expected results, not just two candidates' agreement, must be checked. Other HTTP methods / URLs or URL-encoding semantics are outside baseline contract until explicitly added in a pre-registered task. Do not infer all-client contextual equivalence.

## Evidence and future-task gate

A baseline PASS supports only the bounded claim that two independently implemented application configurations provide the frozen baseline outputs. **No future task is part of F37 yet**. Later F38, if pursued, must choose a previously timestamped, independent demand source that was not written after seeing F37 costs, specify the owner/right/scope, both arms' admissible edit grammar, a bidirectional source change diff, tests, cost vector, timeouts and failures. Both arms must receive the same request, evidence and budget. Pre-existing source size and setup cost are measured, not forced to be equal or omitted. Equal end capabilities do not entail equal total development cost.

Classical challenge: Baldwin–Clark (2000) design operators/options, Jones (1981) rely/guarantee, Brookes (2004) ownership/alias and any suitable source-aware static checker. Explicit `TIE`, `ABSTAIN` and `HOLD` statuses are permitted. No proprietary maintainer authority is inferred from researcher ownership of these new files.

## Separate commit order required

1. This preseal, source-only.
2. Two source arm packages, separately committed.
3. External oracle regression tests and controls, separately committed.
4. Existing read-only native Go CI run and raw log receipt.
5. Research verdict, with branch SHA and strict claim ceiling.

**If baseline produces parity but the future demand is not independently selected, do not advance LAW-R2.**
