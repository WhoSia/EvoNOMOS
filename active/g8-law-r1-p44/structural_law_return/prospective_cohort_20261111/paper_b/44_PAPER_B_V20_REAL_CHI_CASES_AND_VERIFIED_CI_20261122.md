# Paper B v20 / P44 Historical Go Sources — Direct Readback, CI and Ruling (2026-11-22 KST)

## New external evidence, with original-source authority boundaries

These issues are real, third-party-authored and externally timestamped, but were **researcher selected after inspecting problem areas**: not randomized, not blindly registered and not an independent maintenance-cost cohort. Source provenance read directly via GitHub issue and issue-comment API, not inferred from code alone.

| Original third-party source | Observed historical report | Follow-up and normative status | What we actually verified |
|---|---|---|---|
| [go-chi/chi #995](https://github.com/go-chi/chi/issues/995), 2025-05-02 | One mutable singleton middleware in nested Groups sends `/`, `/foo`, `/bar` to last registered handler | Comment proposes **fresh instance per middleware-construction call**; reporter acknowledges this workaround but still asks for **singleton-safe routing OR explicit error** | [Read-only native-Go CI #44924853984](https://github.com/WhoSia/EvoNOMOS/actions/runs/44924853984) on Chi pinned v5.1.0, Go 1.23.2: singleton returns `Hello Bar!\n` for all three; fresh instance returns World/Foo/Bar expected. This verifies an app-owned workaround, **not** original requested singleton API behavior |
| [go-chi/chi #1035](https://github.com/go-chi/chi/issues/1035), 2025-11-18 | Static GET `/users/me` vs parameter PUT `/users/{id}`: request PUT `/users/me` falls to param route, not 405 | Reporter **withdrew separate nested-regex subpath allegation** in 2025-11-18 follow-up. App commenter later suggested static-method route guard, third party suggested upstream StrictRouting idea; not a merged upstream promise | [Read-only native-Go CI #44925028205](https://github.com/WhoSia/EvoNOMOS/actions/runs/44925028205) pinned Chi v5.1.0 gives `PUT /users/me` => 200 `updated:me`; explicit app-owned static PUT route returns 405 and preserves selected GET /users/me + PUT /users/123 calls. Does **not** prove upstream global static precedence |
| [go-chi/chi #1263](https://github.com/go-chi/chi/issues/1263), 2026-11-16 | RouteHeaders map iteration alleged nondeterministic under overlapping headers | Source author claims behavior on 2026 contemporary development master and Go 1.27.3, not pinned old F37 libraries | Read thread only; **no verified executable F37 reproduction**, no inferred version parity |

## Paper B contribution and its bound

[Version 20 full Korean/English manuscript](PAPER_B_BILINGUAL_INTEGRATED_20_20261122.md) is a new preserved file, with [Notion v20](https://app.notion.com/p/41fef561cf9281a7849bd8c8a6322130) separately created and both languages read back. Paper B now introduces genuine public source evidence of *what the reporter actually asked for*, what other participants recommended, and what observed test behavior demonstrates. It is **not** evidence that an OCP label actually caused an external reviewer to reject code, and **not** a quantitative reviewer adoption trial.

Core normative distinction: the requester need not treat a *change of implementation* that makes tests pass as authorization to revise the actual library-level acceptance rule. This parallels Meyer-style protected interface/old-client questions but does not assert a new theoretical rule absent in conventional requirements engineering.

## Verified workflows and source audit

- [Chi #995 raw CI #44924853984](https://github.com/WhoSia/EvoNOMOS/actions/runs/44924853984), test source SHA `8030ddefd3a62cdeb4bf1f9b41bf2e24cad55128`, job `136908609712`: original Chi v5.1.0 misrouting reproduced; fresh-instance app-owned workaround functional; go mod verify, go vet, full tests and race all PASS.
- [Chi #1035 raw CI #44925028205](https://github.com/WhoSia/EvoNOMOS/actions/runs/44925028205), test source SHA `73c66d1d2772b5977133657b09aa74fa1184e866`, job `136909122688`: 200 `updated:me` misroute observed, explicit 405 guard PASS; go mod verify, vet, all tests, race PASS.
- [Paper B v20 source audit CI #44925138801](https://github.com/WhoSia/EvoNOMOS/actions/runs/44925138801), source SHA `1e646b8feef62146d73dae70340bae2c967a8457`, job `136909454943`, **8/8 Python negative-control tests PASS and bilingual 7+7 source checks PASS**. First run [#44925085028](https://github.com/WhoSia/EvoNOMOS/actions/runs/44925085028) failed on a tester mutation which left the section number intact; preserved and corrected without altering its scientific premise.
- [Chat26 contract/F38 metadata CI #44925268152](https://github.com/WhoSia/EvoNOMOS/actions/runs/44925268152), source SHA `0e9df051cd4410860c3e1bb6544a64365470e5f7`, job `136909852499`, **31/31 Python tests PASS**. The gate now marks executed-but-not-independently-checked evidence as `EXECUTED_UNVERIFIED` rather than prematurely promoting `EXECUTED_EVIDENCE_OPEN`; Chi #1035's app-owned route-guard option is correctly represented as historical nonblind exploratory. Intermediate [#44925253318](https://github.com/WhoSia/EvoNOMOS/actions/runs/44925253318) failed as code and tests were updated in separate commits; the failure is retained.

## What remains unproved

No measured F38 cross-architecture source-edit cost on an independently prospective request; no independent human patch-review outcomes, no verified complete contract for Chi #995 singleton desired behavior, no verified upstream Chi #1035 global fix; no novel universal engineering law. The F37 handler/callback baseline, the typed-adapter classical rival and these app-only workarounds are not estimates of causal superiority.

**Ruling:** PAPER B v20 complete bilingual working draft, real third-party source assertions tracked, historical Chi 995 and author-corrected 1035 **bounded Go regressions PASS**, review and field identification OPEN, P44 F38 OPEN / LAW-R2 HOLD.
