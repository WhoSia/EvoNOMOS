# P36-O4 — Stable Registration Identity vs Mutable Index: Multi-Disable Repair Survival and Order Preservation

**2026-10-10 KST · PROSPECTIVE D16 PRE-SOURCE SEAL · P36 OPEN / P35 STAGE CLOSED.**

## Observation that motivates a new independent test (source-read, not native outcome)

[Original Chi O3 RETAIN](../../tools/p36-o3/arms/chi/retain/p35_epoch_router.go) earned [D14+single-D15 original Go PASS #37961233537](https://github.com/WhoSia/EvoNOMOS/actions/runs/37961233537), while ERASE D15 failed as expected. The source stores disabled route records as `{index: i, route: HeaderRoute}` where i is the route's **current slice index at removal time**, not a stable registration ordinal. When the head route is removed, the next route shifts to index 0. Two successive head disables thus save indices [0,0], which are not unique records of original relative order. Saving exact middleware closures does not ensure preserving their **relational order under repeated deletions/reinsertions**.

This is a *post-O3 source-inspection hypothesis*, NOT a blind theoretical discovery.

## Predeclare a distinct future requirement D16 before editing any O4 repair source

D16: For one exact-match header, at least three registration-ordered handlers A,B,C exist, first-match precedence A→B→C. Calls `DisableRoute(header,match)` twice must disable A then B (the first currently enabled route each time); the remaining enabled handler C must serve. Calling `EnableRoute(header,match)` first restores **the earliest disabled handler A** at its original position, and a second call restores B **without displacing A's priority**. Each successful disable/enable is published synchronously; zero-change returned on missing disable/enable. Exact old D14 and D15 must remain valid, as well as O6 trace, other headers, default route and concurrent registration contract.

**Frozen D16 output sequence with A, B, C registered**:
```
before:                  A
disable one:             B
disable two:             C
enable one:              A
enable two:              A
disable again:           B
```
Each successful operation increments revision exactly 1 and publishes completed updates. This is a *new future demand*, not a retroactive replacement of D14's previously frozen two-world first-restore test.

## Two legitimate source responses and signed predictions before O4 treatment

- `POSITION_INDEX`: the **unchanged original O3 RETAIN source** with mutable saved slice indices. Predict **D14/D15 PASS** but **D16 FAIL** after second enable: restored B occupies index 0 and unexpectedly masks A. This is expected-negative scientific evidence, not a CI tooling FAIL.
- `STABLE_ORDER`: a source edit preserving an immutable increasing registration-order token per entry (and the original middleware closure), retaining the tokens on disable and reinserting a recovered route in **order-token rank**, not mutable deletion-time index. Predict **D14/D15/D16 PASS** in the same original Chi module. `Register`, `RegisterAny`, `RegisterDefault`, Disable and Enable must consistently maintain order, with all relevant operations synchronized. No external logs/reflection, no changing test fixtures, and no extra repair permitted after frozen D16 acceptance.

Two source files are checked as original Chi package additions; same pinned commit `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. Record original-source SHA256, full module `go test -count=1 ./...`, middleware race, vet, frozen O6, D14, D15 and D16 separately.

## Mathematical distinction and strongest classical rivals

**Claim currently challenged:** retention of the complete old value/closure ensures future **sequential-repair correctness**. False unless sufficient *relational provenance* is retained or reconstructible. This is not about information quantity or caching rebuild count. Position indexes fail to be invariant under deletion. Stable keys/ordinals recover an order embedding (standard database primary keys, order-maintenance data structures, event-sourcing identities).

More precisely let the original registration order be `a < b < c`. The map `position_t : route→Nat` changes with t, and two distinct routes may have the same position at their separate deletion times. Restoring by those positions need not preserve `<`; a stable `orderId : route→Nat` with injectivity and monotone insertion, and reinsertion sorted by `orderId`, preserves it. Proving that correspondence for all original Go programs needs a separate formal model and a faithful source mapping; one 3-rule Go test does not prove global correctness.

This is **classical relational identity/order maintenance**, and advanced classical prior precisely predicts what the simple-index source could do. However it is a worthwhile new bounded source *counterexample* to a naive principle that preserving deleted values is sufficient for preserving their future structural affordances. `DIP49_NEW_LAW_PAIR_HOLD`; `LAW_R2_NOT_AUTHORIZED`.

## Scientific falsification and future extrapolation

If POS_INDEX passes D16, inspect actual signed behavior and preserve result; do not assume invalid just because indexing looks suspicious. If STABLE_ORDER fails CI, fix source only while retaining D16; record repairs separately. The old O3 frozen oracle is **not edited**. Next independent task after D16 should vary insertion of new duplicate handlers between disables and restores and repeated operations; test stable ordinal preservation before any broad claim. No unfounded universal correctness or Pareto ranking.

**At preseal**: `P36_O4_D16_FROZEN_BUT_NATIVE_UNTESTED__CLASSICAL_ORDER_MAINTENANCE_HYPOTHESIS__DIP49_IDENTIFICATION_HOLD`.
