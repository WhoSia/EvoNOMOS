# G8 LAW-R1-P34-P4 — Prospective Paired Restic-Compatible Backend Micro-Experiment Precommit

**OPEN (registered before either treatment implementation/outcome).** P34 remains open. Prior **ORIGIN-R1-P12 terminal NONRESULT** is never reopened, re-run, re-labeled or used as source of hidden S/L/C/A/Q.

## Question
When all six public Restic backend operations are mandatory, does a capability-composed internal architecture offer an observable advantage that compensates for its internal coordination indirections, while satisfying identical public behavioral histories?

## Real source lock and theory lineage
- Exact pre-demand Restic repository `restic/restic@495982232cf1af184eac0a97871ef8161e8708ee`. **Public interface:** `internal/restic/backend.go`, 12 methods, including Save/Load/Stat/List/Remove/Delete; it is *not* only a six-method interface.
- Original 6-of-6 demand and `TERMINAL_NONRESULT` receipts: [P12 candidates](../../lawkit/discovery/p12_candidates.json) and [non-result](../../lawkit/fixtures/p12-terminal-closure.json).
- P34-P3 [wire/capability court](P34_P3_TEMPORAL_WIRE_AND_RESTIC_COREQUIREMENT_COURT.md). P11 source outcome dimensions are history only, not calibrated to these new metrics.
- Original Drive literature **HELD**: [Liskov & Wing 1994](https://drive.google.com/file/d/1g7ruRxKmmki7ts6fQ09MIOwuYPCeCVvl/view), [Martin 1996](https://drive.google.com/file/d/1fZQi6039W58RcQxTKFHiJZw22mU9kw7g/view), [de Alfaro & Henzinger 2001](https://drive.google.com/file/d/1NUV-6p3ANXDT6ftnURRb8LpwbSp1xTSV/view). No newly proposed outside papers.

## New independent A/B implementations
Construct two new, non-OCI, no-network, in-memory adapters in an isolated Go test package, each **compile-time conforming to the actual original restic.Backend interface**:
- DIRECT: one concrete backend implements six operations over private state.
- COMPOSED: one public adapter delegates six operations to separate write/read/index/delete functional objects sharing a protected state, maintaining exactly the same public twelve-method Restic contract.
No code is taken from the prior unpublished P12 treatment arms. The storage is a controlled fixture, *not* a replacement for OCI/OneDrive production conformance.

## Locked outcome contract
Use the same seeded operation schedule in both new arms, including Save, Stat, Load, List, Remove, Delete, overwriting data, absent-object errors, partial load, failed callback and cancellation. The canonical trace projects to `(method, input, outcome, result digest)`. Observable traces must be equal and tests must explicitly reject missing/public-method regressions.

Instrumentation (separate measurements):
1. **Functional:** trace equality and all six mandatory methods actually exercised.
2. **Boundary crossings:** count concrete internal *adapter-to-component dispatches* per public core operation. This is an exact execution-path structural count, **not a direct proxy for developer hours or wall-clock latency**. Prediction: DIRECT 0, COMPOSED ≥1 each.
3. **Stateful temporal obligations:** check callback exactly once on successful read, no spurious callback on failed/missing read, deterministic list, update/delete lifecycle; neither a full Restic conformance suite nor unbounded LSP.
4. **Source geometry:** compile-time 12-method Restic interface, separate count of inner capability components; any LOC/churn must be reported as fixture-specific, never interchanged with historic P11/P12 L.
5. **Runtime timing (optional):** descriptive only, non-causal and environment dependent; not a maintenance-cost forecast.

## Locked interpretation / rivals
Both arms have (B=D) for six mandatory methods, so (E(B,D)=|B\setminus D|=0). No public-interface mismatch avoidance payoff can be attributed to COMPOSED. Even if it wins another metric, that is a separate mechanism. If COMPOSED adds internal crossings while maintaining observable equivalence, the *architectural indirection* cost is measured; user edits, review coordination, prospective maintenance and incident rates **remain unmeasured**.

**Fatal conditions:** missing public method, unequal behavior trace, different input policy, reliance on hidden P12 outcomes, only synthetic mock without original Go contract type, or bot-authored GitHub commit. Any test error is a harness/semantic HOLD until investigated.

Precommit ruling: `P34_P4_NEW_INDEPENDENT_PAIRED_SOURCE_EXPERIMENT_PRECOMMITTED__RESULTS_UNOPENED__LAW_R2_HOLD`.


## P4b declared extension — demand-indexed client contract sequence (registered after P4a result; before P4b test)
P4a produced 18 identical public traces and explicit 0 versus 18 *additional adapter-to-unit* dispatches at read-only run 37887934272. The P4a implementation is now fixed; it must NOT be retroactively labeled a change-cost experiment.

For P4b, run a **new clean stateful instance** of each unchanged adapter through two nested client contracts:
- **D0**, an initial client with `Save, Load` requirements: execute exactly one Save then one Load with exact data readback.
- **D1**, a widened client requiring all six public storage operations: on the same backend instance, subsequently call Stat, List, Remove and Delete, verify each response and final absent state (final absent check is an extra Stat). All public results must be identical between arms.
- Record exact additional adapter-to-unit visit counts per D0/D1 segment; predict DIRECT 0, COMPOSED one per public core call. Source edits to adapters are prohibited between phases; this measures **client demand widening already satisfied by both**, not maintainers implementing a changed API after shipment.
- Explicitly separate `client_contract_widening_tested` from `incremental_source_change_cost_NOT_MEASURED`. Adversarial fail if any public trace differs or old P12 terminal status changes.

No claim of prospective OO law or universal cost optimality.
