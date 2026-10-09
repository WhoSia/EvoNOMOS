# P36-O7 — Naturally Evolved Routing Topology: Registration-Order Provenance, Overlapping Matchers & Compatible Repair Authority

**2026-10-10 KST — PROSPECTIVE PRE-SOURCE TEST SEAL. P36 OPEN; P35 remains CLOSED; DIP-49 IDENTIFICATION HOLD; LAW-R2 NOT_AUTHORIZED.**

## Original, independently evolved sources (not project-authored wrappers)

1. **go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00** `middleware/route_headers.go`, lines 42–106, unmodified original upstream source:
   `type HeaderRouter map[string][]HeaderRoute`; `Route` adds a HeaderRoute to map bucket for lowercase header; `Handler` loops `for header,matchers := range hr`. The Go language provides **no meaningful original chronological iteration order for map keys**. Within each bucket, registration sequence is stored; **across distinct headers it is not**. Direct public map writes remain part of the legacy exposed type and cannot be covertly eliminated by a source edit.
2. **gorilla/mux@b4617d0b9670ad14039b2739167fd35a60f557c5** `mux.go` lines 57, 138–150, 279–283: `routes []*Route`, `Router.NewRoute` appends, and `Router.Match` explicitly scans `for _,route := range r.routes`. This is naturally evolved original route precedence, not an EvoNOMOS adapter. Existing external method `Router.Headers` calls `NewRoute` in original Gorilla.

Pinned source SHAs and exact line ranges are auditable via GitHub originals. No claim either OSS maintainer intended the **same** priority policy for simultaneous matches; the different precedence semantics were not necessarily software bugs.

## D18 prospective changed functionality

A *new* client functional contract, not a claim about upstream default:
- A pair of distinct exact-match header predicates `A := (X-P36-O7-Alpha: on)`, `B := (X-P36-O7-Beta: on)`, with same HTTP method/path and distinguishable handlers, may be registered in either `AB` or `BA` chronological order.
- Baseline `Q_0`: requests with only one matching header route to its unique handler under **both** libraries.
- Fresh `Q_{18}`: requests with **both** matching headers must dispatch the *earliest registered handler*. `AB→A`, `BA→B`, deterministically across 128 repeated requests per history. The same fixed request input, tag projection and registration semantics are declared. Gorillla route precedence and original Chi API are observed with native original Go code.
- Record first evidence that Chi does not realize Q18 *without modifying its upstream source*. The Chi negative branch is considered scientific if it has at least one mismatch to the new client requirement; this is not a failure against Chi's prior public contract. Do not call it a regression against the maintainers.

## Matched native experiment / O7-A

Prior to treatment:
- Freeze the native Chi and Gorilla D18 Go test packages, with Q0 single-header and Q18 overlapping-header tests, before **any** proposed repair code.
- Run original pinned upstream `go test -count=1 ./...`, `go test -race -count=1 ./...`, `go vet ./...` in each independently evolved original repository. Evaluate Q0 positive and Q18: expect **Gorilla positive** and **Chi scientific negative**, reflecting different chronology representations.
- Keep each original repository's default semantics recognized. A Chi failure of *the new optional D18 requirement* is **not** reason to label Chi generally invalid.

## Pre-source competing repair hypotheses and cost exposure

- `REPAIR_PUBLIC_MAP_STILL_EXPOSED`: a patch restricted to editing the existing `HeaderRouter map` value's `Handler` method **without adding registration-history state, an external append-only log or a changed API** cannot reconstruct cross-bucket chronological registration order for **both** AB and BA histories. The final bucketed map has the same entries when the *same middleware closure objects* are registered in opposite histories, so any deterministic state-only map evaluator must behave identically on them. This is an elementary **classical indistinguishable-state impossibility**, not a novel theory. It does NOT mean a caller cannot supply priority as a new parameter, a wrapper, log, altered map representation, or lexicographic choice instead of insertion order.
- `ORDERED_CHI_COMPAT_SURFACE` (optional O7-B repair): introduce a **new opt-in order-tracking type** within original Chi's `middleware` package, leaving existing exported `HeaderRouter` behavior/API entirely untouched and allowing callers to migrate to the new surface for Q18. Every registered pair must be logged as an ordered event before publication. All old upstream Chi tests must still pass, and the new order-aware method must pass Q0/Q18. The ability is gained by **different authority/state and migration effort**, not by magic optimization of the old map. Publication and dispatcher costs measured separately for each native package without ranking different libraries solely by unpaired ns/op.
- `B_classical` (strong rival): standard collection semantics, information loss and API-compatibility already predict the exact winner and repair limitation. A result agreeing with this **does not identify any new beyond-classical structural law**. A novel candidate law H* needs a prospective query where it and the strongest classical source-aware baseline disagree; none has yet been derived.

## O7 forward theoretical objective

Test whether a **naturally evolved representation choice** bounds a future client-demand repair reachability relation `R_{18}^Γ`, rather than selecting only synthetic RETAIN/STABLE_ORDER policies. The important three-dimensional outcome is:
(1) original semantics/repair eligibility under explicit source/API authority,
(2) persistence of ordering invariant under changed registration histories, and
(3) conditional publication/dispatch/memory/edit-cost vector, not one SOLID score.
A future additional D19 will target new opt-in priority API under repeated updates and third-party public-map mutations **only if** that authority is frozen beforehand, avoiding retroactive requirements.

**At preseal**: `P36_O7_NATIVE_ORIGINAL_SOURCE_PENDING__D18_NEW_CLIENT_REQUIREMENT_NOT_UPSTREAM_BUG__CLASSICAL_RIVAL_UNDEFEATED`.
