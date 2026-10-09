# P38-P2B — Open Natural Cross-Repository Change Request and Source-Confirmed Fasthttp Export Boundaries

**2026-10-10 KST · READ ONLY / P38-P2 NATURAL SOURCE REQUEST SCREENING · NOT a prospective prediction preseal.** Supersedes no prior opening: [P38-P2 original dependency candidate](P38_P2_FIBER_FASTHTTP_NATURAL_DEPENDENCY_CANDIDATE_SOURCE_SCREEN.md).

## Actual unresolved upstream/downstream change request

[Real Fiber original issue #4605](https://github.com/gofiber/fiber/issues/4605), **“Align with fasthttp: adopt existing helpers, propose upstream exports and documentation asks”**, was created 2026-08-11T10:12:14Z and API-verified **OPEN at screening time**; latest recorded issue metadata update 2026-08-21T13:15:08Z. **This is a potential future-change requirement with its *eventual* disposition not yet observed in this P38 screening**, NOT a guaranteed accepted issue, not the registration of a P38 H/B forecast. [Related issue #4604](https://github.com/gofiber/fiber/issues/4604) (normalization/sanitization duplication) was also API-verified open during screening; it already records some subitems checked, therefore those particular past-completed subitems cannot be presented as future holdouts.

#4605 explicitly specifies a natural coordination problem: Fiber may replace its duplicate helper with existing fasthttp helpers; where fasthttp functionality is private, the downstream project proposes independent upstream exports; after upstream acceptance, Fiber aims to remove its own implementation in the same release cycle. The issue's **unresolved checklist** is a source of possible future demand *only after an exact target item is fixed and historical labels excluded*. Its “acceptance” text distinguishes (A) directly adoptable Fiber-only change and (B) upstream-approval-contingent export/removal.

Two comments dated 2026-08-21 express a volunteer claim for the **independent** Charset/VisitHeaderParams item and response; these show community discussion, **not upstream acceptance, exclusive maintainer authority, permission to modify two projects, or an independent completed result**. Because that one item may have pre-existing partial development, it is not a suitable blind novelty demonstration without extensive cutoff audit.

## Verified original source bindings, NOT simulated graph edges

**Frozen downstream Fiber main** `56cd561f7d57addc730992c75a8bde59f050c413`:
- [Original module file](https://github.com/gofiber/fiber/blob/56cd561f7d57addc730992c75a8bde59f050c413/go.mod) directly requires `github.com/valyala/fasthttp v1.75.0`.
- [Original app.go line 83](https://github.com/gofiber/fiber/blob/56cd561f7d57addc730992c75a8bde59f050c413/app.go#L83) stores `*fasthttp.Server`.
- [CODEOWNERS](https://github.com/gofiber/fiber/blob/56cd561f7d57addc730992c75a8bde59f050c413/.github/CODEOWNERS) assigns review routing `* @gofiber/maintainers`, which is **not** a legal guarantee of complete edit and release sovereignty.

**Frozen actual imported upstream fasthttp v1.75.0** tag resolves to `818be799bc0b086b5df262d6382bf5875fbd58f4`:
- [Unexported `appendQuotedPath` at bytesconv.go line 501](https://github.com/valyala/fasthttp/blob/818be799bc0b086b5df262d6382bf5875fbd58f4/bytesconv.go#L501). GitHub contents blob SHA `5394c0772a63f097667763d420ced443e665dad3`.
- [Unexported `hasHeaderValue` actually invoked within header.go at line 229](https://github.com/valyala/fasthttp/blob/818be799bc0b086b5df262d6382bf5875fbd58f4/header.go#L229). Blob SHA `9abc8a6d57278d85643788b12be451d85707c010`.
- [`hasDotDotPathSegment` invoked at fs.go line 1375](https://github.com/valyala/fasthttp/blob/818be799bc0b086b5df262d6382bf5875fbd58f4/fs.go#L1375). Blob SHA `a01d6a7a84592cd47f7c6a45664e764368bf69e3`.
- [`stringContainsCTLByte` invoked at uri.go line 310](https://github.com/valyala/fasthttp/blob/818be799bc0b086b5df262d6382bf5875fbd58f4/uri.go#L310). Blob SHA `7fb6c3b306582a4c31833277ed257b957ebfa4a5`.

These are original current **symbol occurrence / visibility** checks. They **do not prove that adding a public export is needed, correct, safe, approved or adopted**, nor how many alternative repair paths exist in the complete Go edit space. In particular, a direct symbol occurrence is not a complete AST/reachability proof; exact accessibility depends on qualified package API, wrappers and calls.

## Real identification problem, not retrospectively chosen answer

This open request could support a genuinely prospective scientific question, if the following are eventually frozen **without viewing an outcome**:
- A single still-unresolved numbered export request from #4605, its expected concrete public API and downstream removal invariant. The original mixed-version deployment/compatibility rule must be explicitly specified.
- A *real* upstream reviewer/maintainer approval boundary and downstream integrator/owner boundary. GitHub repository identity, CODEOWNERS and ordinary user comments are insufficient to infer veto/deploy authority automatically.
- The strongest available classical source-aware assume–guarantee and co-change/impact rival's **actual implementable predictions**, matched source/query/precompute/annotation budget and sealed outcome contract.
- An explicit **H vs B** different label or rank on the same target *before* upstream/downstream PR merge/tests/review actions are inspected. If no disagreement, no native Go library trial.

**Censoring:** #4605 might be held or abandoned for reasons unrelated to formal source repair, including effort, priorities and release policies. Nonacceptance is not the same as proof no valid program patch exists. Record unknown/missing/censored outcomes.

**G0 natural source+actual demand anchor: partial PASS; G0 authentic cross-owner permissions/invariant: HOLD; G1 fair computational cost: HOLD; G2 predictive discordance: HOLD; P3 native Go: BLOCKED.**

`P38_P2B_ISSUE_4605_OPEN_WITH_PINNED_SOURCE_APIS__FUTURE_OUTCOME_NOT_PRESEALED__RIVAL_COMPARISON_HOLD__NO_NATIVE_GO__DIP49_HOLD`.
