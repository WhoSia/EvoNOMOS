# EvoNOMOS G8 LAW-R1-P34-P4 — Paired Real Restic-Backend Implementations, Internal Dispatch and Demand-Indexed Contract Widening Court

**Scientific status:** `P34_P4_TWO_NEW_SOURCE_ARMS_HOSTED_PASS__PUBLIC_TEMPORAL_TRACE_EQUAL__ADAPTER_DISPATCH_DIFFERENCE_MEASURED__CLIENT_CONTRACT_WIDENING_PASS__DEVELOPER_MAINTENANCE_COST_UNMEASURED__ORIGIN_P12_UNTOUCHED__LAW_R2_NOT_AUTHORIZED`. P34 remains OPEN.

## 1. Before observation: separate old P12 and new P34 experiment

[P34-P4 registration](P34_P4_PAIRED_RESTIC_BACKEND_PRECOMMIT.md) was committed *before any new implementation or CI result*, specifying two independent **new Go adapter source arms**, functionally equal public contracts, frozen Restic source and explicit dispatch measurement. After initial P4a pass, a **separately labeled P4b demand-widening supplement** was registered before adding its test and seeing its outcomes. The follow-up is not portrayed as part of the initial preregistration.

The old [ORIGIN-R1-P12 terminal receipt](../../lawkit/fixtures/p12-terminal-closure.json) is still `TERMINAL_NONRESULT`. It neither yielded original OCI/OneDrive cost coordinates nor adjudicated an architecture winner; no existing P12 treatment source or outcome was used. This P34 fixture **does not reactivate that experiment**.

**Source lock:** exactly `restic/restic@495982232cf1af184eac0a97871ef8161e8708ee`, [original twelve-method public `restic.Backend` interface](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/internal/restic/backend.go), including the six required `Save, Load, Stat, List, Remove, Delete`. CI copies the two **new test fixtures** into an isolated package within this precise checkout and compiles with real type checking. No OCI SDK, OneDrive credentials or live production backend.

## 2. Genuine newly implemented architectural alternatives

Source: [pair.go](../../tools/p34-p4/pair.go), test: [pair_test.go](../../tools/p34-p4/pair_test.go).

- **DIRECT**: the public backend calls the local protected in-memory storage kernel directly for each mandatory operation.
- **COMPOSED**: the same public contract routes the six operations through four internal units (`writeUnit`, `readUnit`, `indexUnit`, `deleteUnit`), which then use the *same storage semantics*.

The storage kernel and the other six public Restic methods are deliberately shared. This is **designed isolation of additional functional dispatch**, not a head-to-head of independent algorithms or independently maintained libraries. The kernel map is keyed by real `restic.Handle`, guarded by a mutex; methods apply cancellation, read callbacks, missing-object errors, deterministic lists and update/deletion logic.

Explicit type assertions `var _ restic.Backend = (*direct)(nil)` and likewise for COMPOSED make public contract completeness a compile-time condition.

## 3. P4a — original identical public behavior / internal dispatch paths

**Frozen 18-operation trace:** save alpha, beta and key; stat; full read; partial read; list; list callback error; missing load with no callback; callback failure; cancelled save; overwrite and stat; remove and missing remove; delete; stat and list after delete.

Results from actual hosted report, checked without reusing the old P12 data:

| Measured dimension | DIRECT | COMPOSED | Scope |
|---|---:|---:|---|
| Original Restic public methods compiled | 12 | 12 | Type-checked |
| Six required functions exercised | 6 | 6 | Fixed local test |
| Public stateful operations | 18 | 18 | Same inputs |
| Public projected traces | identical | identical | 18/18 |
| **Additional adapter→capability-unit boundary dispatches** | **0** | **18** | Precise controlled-path instrumentation |
| Internal capability units | 0 additional | 4 | Source-defined |

The *DIRECT* arm still invokes the shared storage kernel. **Zero means zero extra adapter→capability-unit hops, not zero function calls or zero internal coordination.** Conversely COMPOSED's 18 visits are not evidence of 18× runtime cost or any maintenance-hours increase.

## 4. P4b — widening the client demand over time

Without changing adapter source between the phases:
- Client contract **D0** = `{Save,Load}`: one successful Save and one exact content Load.
- Client contract **D1** = `{Save,Load,Stat,List,Remove,Delete}`: add Stat, List, Remove, Delete and a post-delete missing Stat, on the same stateful instance.

P4b hosted result: first phase **2 public calls / 2 extra COMPOSED dispatches**, second phase **5 public calls / 5 extra dispatches**; public traces between DIRECT and COMPOSED identical in both phases. Thus both *already have* the six-capability extension when the client starts requiring it.

**Important negative boundary:** No developer actually modified the implementation code between D0 and D1. This is a **demand-indexed client-contract widening test**, not a measured transition patch, new architectural mutation, or empirical source-change burden comparison. `source_change_cost_measured=false` is written into the artifact.

## 5. Execution custody, failed gate and corrected outcome

Initial `37887867814` ran the new Go test successfully (18/18 traces) but the JS postprocessor incorrectly read Go JSON tagged snake_case using capitalized property names, failing the **harness check only**. Fixed the mapping without modifying Go implementations or required outcomes. Read-only [P4a hosted 37887934272](https://github.com/WhoSia/EvoNOMOS/actions/runs/37887934272) **SUCCESS**; independently inspected earlier artifact.

After P4b source and explicit gate were added, final [hosted 37888110765](https://github.com/WhoSia/EvoNOMOS/actions/runs/37888110765) **SUCCESS**. Exact archive `g8-law-r1-p34-p4-restic-pair`, GitHub artifact id `11596179928`, SHA256 `9b35a9c80c72d4f5c0ca76ccb58a3bcd4dcef6f7aa3e9ec6a76e61f1b39d133a`. Archive files include `p34-p4-pair.json`, `p34-p4-widening.json`, Go test transcript and per-file checksum manifest, independently read back. Workflow [g8-law-r1-p34-p4-backend-pair.yml](../../.github/workflows/g8-law-r1-p34-p4-backend-pair.yml) uses only `contents:read` and `actions:read`, creates no bot-authored commits.

## 6. Formal conditional interpretation (credited conventional theory)

Let (B) be the exposed capabilities and (D_t) the client-required set. The *excess offered capability* `E(B,D_t)=|B\\D_t|` drops to zero in full co-requirement `D_1=B`. A modular implementation may still offer fault isolation, maintainability or future option value; none of these is settled by `E`.

The present objective vector is narrowly (J(a)=(1-Q(a),V(a))), where (Q) denotes the **tested finite trace equivalence** and (V) means the **extra adapter→capability-unit visits** under the fixed call schedule. Both satisfy (Q=1), and DIRECT has (V=0) versus COMPOSED (V=18) on P4a. Thus DIRECT **dominates only in this preselected narrow two-coordinate vector**. It does not imply a universal design or maintenance winner. Changing the evaluation objectives or demand schedule can change the Pareto ordering.

Underlying original theory **Drive HELD** and previously read: [Liskov & Wing (1994)](https://drive.google.com/file/d/1g7ruRxKmmki7ts6fQ09MIOwuYPCeCVvl/view) behavioral history/refinement; [Robert C. Martin (1996)](https://drive.google.com/file/d/1fZQi6039W58RcQxTKFHiJZw22mU9kw7g/view) source dependency inversion; [de Alfaro & Henzinger (2001)](https://drive.google.com/file/d/1NUV-6p3ANXDT6ftnURRb8LpwbSp1xTSV/view) input/output assume-guarantee interface composition. No external unheld paper introduced.

## 7. What would change the actual result?

- A **real software-maintenance intervention**, not a changed test demand alone: create reproducible issue-like patches to DIRECT and COMPOSED at the same frozen revision, blind-cost edit sites and review burden, and test identical functional contracts before exposing costs.
- An independently source-backed **implementation with nonshared algorithms and persistence/network failure modes**; otherwise extra boundaries were introduced by construction.
- Probe whether separated components make independently scheduled modifications cheaper (or safer) enough to offset the extra indirection. Compare strong baseline with static call structure, not just weak graphs.
- If source ownership or review costs matter, collect change-control evidence independently rather than deducing it from an interface arrow.

**P4 verdict:** `P34_P4_METHOD_AND_REAL_TYPED_IMPLEMENTATION_PASS__BEHAVIOR_EQUIVALENCE_BOUNDED__EXTRA_COMPONENT_DISPATCH_MEASURED__MAINTENANCE_EDIT_COST_HOLD__P34_OPEN__LAW_R2_NOT_AUTHORIZED`.
