# EvoNOMOS G8 LAW-R1-P34-P3 — Temporal Wire Contract and Capability Co-Requirement Court

**Status:** P3 bounded execution PASS; P34 OPEN; LAW-R2 NOT_AUTHORIZED. No retrospective promotion of ORIGIN-R1-P12 outcomes.

## A. Real original P11 Go oracle — temporal trace, not imagined tool behavior

The original source is [EvoNOMOS historic Go oracle main.go](https://github.com/WhoSia/EvoNOMOS/blob/e2e5a2e43c899e9e3574b615ba2375b32d0895fb/lawkit/oracles/provider-surface-v01/main.go), frozen before this P34 court. It implements Exa /search and /contents and Tavily /search and /extract, explicit authentication, status and JSON response, and a JSONL ledger of **successful** requests labeled `demand-required` (search) or `conformance-only` (fetch/extract).

P34 test [p34-p3-temporal-oracle_test.go](../../tools/p34-p3-temporal-oracle_test.go) runs the **actual original handler** with local `httptest`. Ten ordered HTTP calls: four accepted with structured JSON and success ledger events (Exa search; Exa contents; Tavily keyless search; Tavily bearer extract), and six invalid calls (bad/missing auth, wrong method, missing input) returning rejection statuses without creating success events. The test verifies both HTTP responses and ordered ledger provider/surface/class/auth, not just function names.

[Read-only hosted Actions 37887161953](https://github.com/WhoSia/EvoNOMOS/actions/runs/37887161953) **SUCCESS**, artifact `11597370040`, sha256 `02101059bcf8fba31774ee082fbf582ea9886c18ad37c573674665669e42340c`. The original Go handlers are not modified. This is a **mock HTTP wire-temporal proof for specific bounded traces**. No network-vendor contact, no runtime treatment-arm TypeScript replay, no unbounded interface-automata simulation, and no source repair optimality.

## B. Original P12 Restic — explicitly terminal NONRESULT

Read [ORIGIN-P12 terminal closure](../../lawkit/fixtures/p12-terminal-closure.json), [P12 source/admission discovery](../../lawkit/discovery/p12_candidates.json), and original `restic/restic` commit `495982232cf1af184eac0a97871ef8161e8708ee`. Restic [original Backend interface](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/internal/restic/backend.go) requires Save, Load, Stat, List, Remove, Delete along with the rest of its twelve public methods; the [original conformance source](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/internal/backend/test/tests.go) references all six.

[Executable lexical scope checker](../../tools/p34-p3-restic-core.mjs) confirms the six demand names against the frozen discovery fixture, their presence in the pre-demand interface and conformance test code, and the **P12 scientific firewall**. Its lexical evidence is not a Go AST certification and does not execute the OCI/OneDrive arms. Original P12 explicitly ended `TERMINAL_NONRESULT`: OCI hosted execution never reached the required successful parent gate before closure; S/L/C/A/Q and churn stayed sealed; OneDrive phase1 never opened; CBL-C1 verdict unadjudicated. The 6/6 *source contract geometry* is real; any claimed design winner from those source records is fabricated.

## C. Mathematically sharp contrasting mechanism

For boundary capability set B and required demand capabilities D, define the **excess conformance count**
`E(B,D)=|B\\D|`. This is a classical finite-set statistic, **not** a universal maintainability or design utility.

- TrueForge WIDE for Exa/Tavily: B={search,fetch}, D={search}, E=1. A truthful extra fetch implementation is required by the frozen WIDE treatment; SEG has no such demand-extraneous promise, E=0. Historical C coordinate matches 1→0.
- Restic native Backend: B={Save,Load,Stat,List,Remove,Delete}, D=B, E=0. Both FULL_BACKEND_REUSE and internally CAPABILITY_COMPOSED_BACKEND must expose the same public backend contract; segregation cannot reduce `E` below zero *by shedding an unrequested public capability*.

**Bounded proposition:** If D=B, then E(B,D)=0 and any internal repartition leaving the public B unchanged cannot gain by eliminating demanded-extra capabilities. Proof: `B\\D=∅`. This **does not** show composition is bad, equal cost, or no reuse benefit: internal separation can still affect testing, fault isolation, lifecycle and coordination costs. Predictive cost and overall winner remain empirically unidentified.

Thus the CBL-C1 mechanism is **conditional on mismatch**; its treatment payoff may vanish when the actual demand exhausts the capability bundle, but the source-only P12 court cannot say whether overall interface decomposition becomes worse or better.

## D. Evidence and future gate

P11 exact [terminal receipt](https://github.com/WhoSia/EvoNOMOS/blob/e2e5a2e43c899e9e3574b615ba2375b32d0895fb/active/g8-origin-r1-p11-p3/receipts/P3_TERMINAL.json) shows search-only two real demands, Q=1 both, early L birth tax +27 for SEG and phase1 L saving −31, no general design winner. P12 Restic is a **different world with a stronger full bundle** but an unexecuted treatment outcome. Original archive 10.md and 11.md preserve this chronology; LAW-R1-P12 is a different numbered later policy study.

Next P34-P4 should investigate original full six-capability conformance as *time-indexed traces*, paired with a truly independently admitted source world if an empirical conditional law is sought. Do not let a structural zero-mismatch statement masquerade as a prospective source-outcome result.

**P3 ruling:** `P34_P3_FROZEN_GO_HTTP_TEMPORAL_PASS__RESTIC_CO_REQUIREMENT_SOURCE_PASS__MISMATCH_MECHANISM_BOUND_IDENTIFIED__P12_EMPIRICAL_EFFECT_UNIDENTIFIED__LAW_R2_HOLD`.
