# P36-O10 — Fixed-Contract Dual-Policy Repair in Two Naturally Evolved Original Go Routers

**2026-10-10 KST · PROSPECTIVE PRE-SOURCE SEAL · P36 OPEN / P35 CLOSED / LAW-R2 NOT_AUTHORIZED**

## Causal design and scope

Previous original core router native [O9](https://github.com/WhoSia/EvoNOMOS/actions/runs/37969103183) found naturally evolved, incompatible preference semantics: original Chi core radix path tree enforces STATIC before PARAM, original Gorilla core registered route slice enforces chronological precedence. This O10 must NOT rank architectures by comparing different accepted contracts. Freeze **one identical new client contract Q21** and implement it in both actual pinned Go modules, with no edits to upstream source files.

Original pinned upstream modules:
- `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`, package `chi`, actual core `NewRouter`, `Mux.Match` and `Mux.ServeHTTP` available.
- `gorilla/mux@b4617d0b9670ad14039b2739167fd35a60f557c5`, package `mux`, actual core `NewRouter` and registration-ordered `Router.Match` / `ServeHTTP` available.

These **baseline structures evolved independently**; the Q21 policy selection extensions are project-authored *new* files, never falsely called naturally evolved maintainer repairs.

## Frozen shared public API in each original package

```
func P36O10NewSelectableRouter(policy string) (*P36O10SelectableRouter, error)
func (*P36O10SelectableRouter) Register(pattern, label string) error
func (*P36O10SelectableRouter) Handler() http.Handler
```
`policy` exactly `"specificity"` or `"chronology"`; unsupported policy rejected. `Register` only permits the **explicit fixed grammar** `/members/me` (STATIC) or `/members/{id}` (PARAM) for HTTP GET in this O10; unsupported patterns, empty labels, and registration after Handler are rejected; duplicate route templates are rejected. The new object is configured **serially before Handler publication**, and only the resulting handler is used concurrently. This finite restricted grammar is essential; do not generalize O10 to arbitrary Chi/Gorilla route patterns or all HTTP middleware.

## Exact same acceptance contract Q21 in both original modules

Register STATIC tag `STATIC` and PARAM tag `PARAM`, in both histories `PS` (param first) and `SP` (static first). Request `GET /members/me` meets both patterns. Under `specificity`, output STATIC in both histories. Under `chronology`, output PARAM for PS and STATIC for SP. Request `GET /members/42` must always output PARAM; `GET /outside` must always produce 404, no result tag. Repeat 128 dispatches per triple (policy, history, route). Return exact HTTP status and `X-P36-O10-Winner` header label. Registered handler must be immutable once published and race free under concurrent request calls. Legacy public `chi.NewRouter` and `mux.NewRouter` are **not replaced or changed**; existing original full Go tests/race/vet must pass.

## Prospective two source repair designs and strongest baseline rivals

**Chi project repair**, additional original-module file only: treat each registered route as a one-pattern **real Chi core Mux** rather than implement a fake regex matching function; `Mux.Match(NewRouteContext(), method,path)` discovers whether each entry matches. Choose order of testing entries according to policy (specificity static first, chronology original registration order), then **dispatch through the same actual Chi Mux.ServeHTTP** for the winning entry. This works around core Chi's baked-in static precedence by performing a sequence of independent real core route matches. It incurs selection / mini-router overhead; do not call this minimal or native upstream performance.

**Gorilla project repair**, additional original-module file only: preserve actual `mux.NewRouter` original route-list evaluation, and when policy is specificity sort only the two frozen permitted templates by exact STATIC before PARAM at Handler construction; for chronology preserve original registration order. The resulting **original Gorilla Router.ServeHTTP** does runtime matching. No edit to the original route list implementation.

**Strong classical rival B**: existing trie static-node priority, ordered route-list matching, policy adaptation by explicit extra dispatch structure and classic architecture/economics can already predict both implementations' semantic success if coded correctly. It predicts implementation pathways differ. No quantitative performance ratio or universally better architecture is preregistered, because allocations/GC, runner CPU and source-specific implementation are not controlled analytically. Strong `B` can explain any measured sign absent a calibrated quantitative model; thus **no new-law DIP49 split** from this experiment alone.

## Freeze measurements and constraints

Measure on **one GitHub Actions Runner**, both pinned original upstream repos checked out as siblings, same Go 1.23, same CPU/GOMAXPROCS=1. After native `go vet ./...`, old full `go test -count=1 ./...`, relevant `go test -race -count=1 ./...` and new Q21 frozen tests, run matched benchmark names and workloads with `-count=5 -benchtime=200ms -benchmem -cpu=1`: dispatch each (policy=2 × history=2) on **overlap GET /members/me**, plus new-router construction and Handler publication for each policy, plus nonoverlap GET /members/42 as negative control if included. Request object outside timed loop; recorder generated within loop in both. Capture raw `ns/op`, `B/op`, `allocs/op`, source SHA and CPU environment. Costs for registration/build vs dispatch kept separate; startup allocations not inferred from dispatch results. **Do not** assume one-runner averages and wrapper choices identify intrinsic runtime performance of upstream Chi vs Gorilla.

## Required negative controls and falsification

Old O9 Q19/Q20 existing frozen tests correctly classify original cores under different Q. O10 all variants MUST pass same Q21; **NO expected-negative new source arms**. If any variant fails Q21/old Go/race/vet, CI must fail as a technical source/test failure; diagnose from actual logs and **edit source only**, never silently weaken frozen Q21. Any claimed equivalence holds only the finite grammar and disclosed observation. The compat restriction is intentionally additive: users must opt in to the new API, no global migration or automatic legacy behavior change.

**Pre-treatment verdict** `P36_O10_IDENTICAL_Q21_FROZEN__CHI_AND_GORILLA_NEW_SOURCE_UNWRITTEN__ORIGINAL_GO_NATIVE_UNVERIFIED__COST_NO_PREDECLARED_SIGN__DIP49_HOLD`.
