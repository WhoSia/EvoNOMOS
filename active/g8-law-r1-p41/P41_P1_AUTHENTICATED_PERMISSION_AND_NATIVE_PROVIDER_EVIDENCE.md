# EvoNOMOS G8 LAW-R1-P41-P1 — Authenticated Operational Rights & Original Go Dependency-Provider Contracts

**2026-10-11 KST · P41-P1 REAL C/F EVIDENCE VERIFIED: CURRENT ROLE + ACTUAL HISTORICAL MERGE EVENT, ORIGINAL GO PROVIDER; BRANCH POLICY, NORMATIVE RIGHTS AND COMPLETE DEPENDENCY CONTRACT OPEN · LAW-R2 NOT_AUTHORIZED.**

## 0. Empirical decision

P41-P0 had classified C (legitimate authority) and F (provider/dependency incidence) as synthetic-only. The present P41-P1 extends *evidence availability* without pretending to have proved the complete C/F semantic axioms.

- **C** now has an *authenticated, current GitHub platform-permission snapshot*: the connected GitHub collaborator permission endpoint reported **`admin`** for principal `WhoSia` on repository `WhoSia/EvoNOMOS`. A separate authenticated repo metadata query identified the same repository owner and `permissions.admin=true`. A repeat query returned the same status. This attests current operational platform capability in this authenticated context. Separately, a GitHub **historically timestamped successful merge event** can attest that the platform recorded one actor performing one specific merge. Neither proves earlier ruleset/branch authorization criteria, cross-repository universal permission, lawfulness or organizational consent.
- **F** now has a **source-realized, pinned Go type and provider-behavior experiment**, using the actual `echo.Router` interface exported by labstack/echo v5, pinned to `3882266a3641a36fc2111b48cd597adab1c1ecea`. A provider missing `Route(*echo.Context) echo.HandlerFunc` is rejected by the original Go compiler, while two valid interface-conforming providers compile and run but return **different** client responses.

The stronger **C_RevisionAuthority** and **F_SemanticDependency** propositions are STILL NOT PROVED. Exactly this refinement is intended: no epistemic jump from existence of a platform role or an interface signature to the general architectural law.

## 1. Authority C: actual independent provider record, exact limits

[Immutable query snapshot and limits](../../tools/p41/p1-authority/github_operational_authority_snapshot.json), [type-scope auditor](../../tools/p41/p1-authority/audit_authority_snapshot.py).

- GitHub authenticated `get_repo_collaborator_permission(WhoSia/EvoNOMOS,WhoSia)` returned `{"permission":"admin"}`.
- GitHub authenticated `get_repo(WhoSia/EvoNOMOS)` independently reported owner `WhoSia` and `permissions.admin=true` as repository metadata, and admin/maintain/push/pull/triage are all true.
- Repeating the authenticated query in this same research session produced the same result.
- External upstream `labstack/echo` collaborator-permission query and `WhoSia/EvoNOMOS` branch-protection query returned GitHub 403 under the connector's permissions. **FORBIDDEN does not mean the person lacks rights or that protection is disabled; it means insufficient evidence.**
- Actual [Echo PR #3132](https://github.com/labstack/echo/pull/3132) is merged and has two source-visible reviewer records in the accessible API, each in state `COMMENTED`; those two records **cannot be represented as `APPROVED`** or as a snapshot of historical edit authorization. The review contents make specific source-level claims, but their existence does not establish a legally or institutionally authorized edit for the broader theory.
- Current admin in 2026-10-11 cannot retroactively determine `permission(principal,artifact,revision,edit)` at an arbitrary earlier revision. Source signatures and HTTP tests alone cannot determine this history.

**Additional independent historical platform operation evidence:** [Echo PR #3132](https://github.com/labstack/echo/pull/3132) was actually merged by platform account `vishr` into branch `v4` on **2026-09-30T01:00:17Z**, producing commit `f085ffbe8f99de165bd920746920000ab56bd6bc`. The GitHub PR object and the timeline's **`merged` event** agree on actor, UTC timestamp and commit. The two separate review submissions inspected were `COMMENTED`, not `APPROVED`; do not infer an approval gate from them. This is more than a *current* admin role: it attests an actual, revision-specific **platform merge operation**, not the protection rules or wider legitimacy that governed it.

[Immutable historical event receipt](../../tools/p41/p1-authority/github_historical_merge_event.json) · [independent public API recheck script](../../tools/p41/p1-authority/audit_historical_merge_event.py) · [GitHub Actions #38064380066 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38064380066), source-test HEAD `453e64712778c9a2e5fdfc25cb89d7d907c1efe7`, authority audit artifact `11675035333`, SHA-256 `68ba81319de3ab85bcac1a1315686a90370ce26240435567608bc8091082441a`. This CI retrieves upstream public GitHub PR, event and review records **live** and verifies their exact fields. It does not make a new authenticated query for the local `WhoSia/EvoNOMOS` `admin` role, which was separately rechecked through the connected GitHub API.

C evidence category: **`PLATFORM_AUTHORITY_CURRENT_ROLE_AND_HISTORICAL_MERGE_LIMITED`**. Actual timestamped platform merge actor is now evidenced; full revision-indexed policy, per-edit authorization beyond that event and normative legitimacy remain **OPEN**.

## 2. Provider F: actual Echo interface, and where type checking stops

The original unchanged [Echo `Router` interface](https://github.com/labstack/echo/blob/3882266a3641a36fc2111b48cd597adab1c1ecea/router.go) declares `Add(Route)(RouteInfo,error)`, `Remove(method,path) error`, `Routes() Routes`, and `Route(*Context) HandlerFunc`. Echo's actual `NewWithConfig(Config{Router: custom})` accepts an implementation of this native interface.

[Executable original Go providers](../../tools/p41/p1-provider-echo/provider_contract_test.go) · [deliberately incomplete provider](../../tools/p41/p1-provider-echo/invalid-provider/negative.go) · [source workflow](../../.github/workflows/g8-p41-p1-provider-authority.yml).

There are three conceptually different source states:

| Original Go provider | Actual source/interface verdict | Original Echo HTTP observation | Contract result |
| --- | --- | --- | --- |
| Forwarding provider wrapping original `NewRouter` | `echo.Router` compile PASS; route logic forwarded | HTTP 200 `CONTRACT_OK`, expected provider header | selected client contract PASS |
| Diverting provider wrapping original `NewRouter` | `echo.Router` compile PASS; route method has correct signature | HTTP 200 `WRONG_PROVIDER` with divergent provider header | selected client contract FAIL |
| Incomplete provider, three of four real methods, missing `Route` | compile FAIL from native Go: `does not implement echo.Router (missing method Route)` | cannot be supplied to `Config.Router` at compile time | required structural interface FAIL |

**This is a two-level native dependency contract**: structural interface compatibility is enforced by compilation, but the semantic behavior of a substituted provider is not implied by type checking. It does not demonstrate that arbitrary dependency graphs have been verified or that an independent F axiom is necessary in every OO system.

[Original source provider AND authority-type audit Actions #38063852776 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38063852776), tested EvoNOMOS harness HEAD `5b1c3cc97ed9853fb9f796dd541a3680dee3486f` and pinned Echo SHA above. Positive/negative provider job artifact **`11673804473`** sha256 **`565ab039638a2c54dd321426a068e06cf845c12da56359809231dc0c30ec6964`**; permission-snapshot-scope audit artifact **`11673974273`** sha256 **`b448ff07701a65a5e07b2fc2165489c03dc88e3c3bbb3be8862117461cb86ffe`**.

The first permission CI checks the present-role snapshot’s **claimed scope and provenance metadata**, not a second authenticated collaborator role query. The live connector check was separately re-run. A **later CI #38064380066** independently re-fetched public upstream historical PR, merge-event and review data. These three trust mechanisms are distinct.

## 3. Conditional redundancy and minimality implications for P41-P2

A minimalist F predicate defined merely as `provider implements Router` is subsumed by a sufficiently strong **A compiler acceptance** premise, *in a client context that already contains the interface assertion*. Therefore it is not demonstrably irredundant on that grammar. Formally, when `A` is “this client/provider assembly compiles, including the `var _ echo.Router` assertion,” `A ⇒ F_structural`. Adding `F_structural` as a separate conjunct does not strengthen that chosen premise.

To preserve explanatory value, distinguish `F_structural` from `F_semantic`: a type-correct provider may violate the client behavior. But in the current selected-client grammar `F_semantic` also overlaps the behavioral/goal predicate D. Whether any irredundant independent F remains demands a different **prospective source-realized cross-ecology dependency graph** and separately testable provider capability, not an invented truth-table coordinate.

Likewise neither **C_current_platform_admin** nor the existence of **one historical successful platform merge** proves `C_historical_approval(principal,edit,revision)` for arbitrary edits. The authenticated GitHub branch protection/policy state applicable on 2026-09-30 was not available. Substituting either weak evidence type for the full C predicate would make the resulting safety theorem unsound.

This is a *negative* result against naive six-guard uniqueness, not a positive new semantics axiom.

## 4. Status and next scientific gate

- C evidence **grounded in present authenticated platform admin and a separate real historical platform merge event**, but historical protection/policy and normative legitimate rights **OPEN**.
- F interface contract **genuinely native-source grounded**, but complete semantic dependency architecture **OPEN**.
- The existing P41-P1 route identity witness [original Echo #38063086233 PASS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38063086233) remains distinct from provider interface behavior.
- [P41-P2 negative minimality & observational information court](P41_P2_NEGATIVE_IRREDUNDANCY_AND_CLASSICAL_REDUCTION_COURT.md) is the next bounded formal step. Six free-product synthetic omissions are NOT full OO axiomatic independence.
- Classical data refinement, CSP (constraint satisfaction), frame and capability logic **survive**. **P41-P1 remains partially OPEN** for time-indexed permissions and rich provider graph. **LAW-R2 NOT_AUTHORIZED.**
