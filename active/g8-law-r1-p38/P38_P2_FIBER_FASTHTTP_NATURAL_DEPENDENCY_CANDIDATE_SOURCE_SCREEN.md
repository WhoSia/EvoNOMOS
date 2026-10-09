# P38-P2 — Natural Independent-Owner Candidate Screening: Fiber v3 / fasthttp, Evidence-Pinned but NOT Outcome-Eligible

**2026-10-10 KST · P38 OPEN / P2 READ-ONLY CANDIDATE SCREEN · G0 PARTIAL · G1/G2 NOT SEALED · NO NEW NATIVE GO TEST.**

## Natural dependency verified at pinned original sources

This **new-to-P38 screening candidate**, distinct from the P37 E1–E4 Gorilla/SCS/Chi integration corpus, is a natural existing dependency between two independently maintained upstream repositories:

- Downstream Go web framework: [gofiber/fiber](https://github.com/gofiber/fiber), original **main SHA `56cd561f7d57addc730992c75a8bde59f050c413`**. [Pinned `go.mod`](https://github.com/gofiber/fiber/blob/56cd561f7d57addc730992c75a8bde59f050c413/go.mod) declares module `github.com/gofiber/fiber/v3`, Go 1.26.0 and direct `github.com/valyala/fasthttp v1.75.0`. [Original `app.go`](https://github.com/gofiber/fiber/blob/56cd561f7d57addc730992c75a8bde59f050c413/app.go) imports `github.com/valyala/fasthttp` and declares a real `*fasthttp.Server` field. This is not a research-authored bridge.
- Distinct upstream original implementation: [valyala/fasthttp](https://github.com/valyala/fasthttp) pinned **module version `v1.75.0`**; [GitHub tag ref](https://github.com/valyala/fasthttp/tree/v1.75.0) resolves to source commit **`818be799bc0b086b5df262d6382bf5875fbd58f4`**. The later **master HEAD `d949b3e6c2d3fb5cc5b9d5abcb2666c6e54ed867`** was checked for repo status, but must **NOT** be substituted for the actually imported pinned `v1.75.0` source. Both publicly list MIT licenses, which is a repository metadata claim, not a complete license compliance audit.
- Actual downstream repository ownership pointer: [Fiber pinned `.github/CODEOWNERS`](https://github.com/gofiber/fiber/blob/56cd561f7d57addc730992c75a8bde59f050c413/.github/CODEOWNERS) contains `* @gofiber/maintainers`. That shows a repository *review routing declaration*, not exclusive legal authority to edit/deploy across all files or prove who can veto a release.
- A corresponding `.github/CODEOWNERS` file was **not present at the checked fasthttp repository path**. The two distinct repository owners and upstream release publication do **not** establish exactly which upstream reviewer or deployment gate has a legally enforceable veto. Mark **upstream edit authority UNKNOWN** rather than imputing it from a username.
- The fasthttp [v1.75.0 release](https://github.com/valyala/fasthttp/releases/tag/v1.75.0) was published 2026-10-05 and describes fixes and changes to HTTP parsing, URI handling and other behavior. These public *pre-screening historical notes* are background only, **NOT independent prospective P38 change outcomes**, and must never serve as unseen prediction labels.

These observations came from read-only source and release metadata. No source checkout, compilation, tests, package download, GitHub mutation, or run on external owner infrastructure was performed for these two projects.

## G0–G2 status

| Gate | Status | Reason |
| --- | --- | --- |
| G0a real natural distinct-source dependency | **PASS, source level only** | Original pinned Fiber `go.mod`, `app.go`, upstream tag ref |
| G0b authenticated distinct actual edit rights | **HOLD** | Downstream CODEOWNERS is useful but upstream veto/capability/deployment rights unknown |
| G0c exact restricted future edit grammar and invariant | **HOLD** | A real future change request/invariant not selected before outcome; no research-authored patch grammar to substitute |
| G1 fair identical source/time/cost ledger | **HOLD** | Actual source-query, CPU/parse, preprocessing and expert-annotation budgets not measured |
| G2 unequal **prospective** H / strongest B predictions | **HOLD** | No target future demand/outcome, no rivals' frozen implemented outputs |
| P3 original-source/native Go tests | **BLOCKED** | G0b/c, G1, G2 incomplete |

**Important:** This is a scientifically meaningful **new natural ecosystem** screening receipt, NOT a future-holdout test, NOT independent validation of a novel software law, and NOT an authorization to add a new Go native CI job.

## Suggested *questions*, NOT prospective predictions

Potential future requirement families include source-compatible HTTP request representation changes, middleware parsing assumptions and downstream adaptation to independently authored upstream semantic changes, **only if an actually future or cutoff-safe maintenance request becomes available and source-derived owner/invariant evidence can be frozen before seeing an outcome**. P38 should compare an owner-/obligation-indexed repair certificate with real strong classical compositional and historical-impact predictors under the **same** source and budget ledger. If both predict the same, classify agreement; no new Go trial.

## Preserve independent epistemic status

1. **READ:** pinned source import and tag identity as above.
2. **NOT VERIFIED:** correct full AST repair edit universe, approval/veto authority of the second repo, requirement/invariant traces, pre-outcome oracle, exact fair budget receipt and sign-separated predictions.
3. **STRICT NEXT:** Find eligible *future* maintenance demand and actual owner evidence, then seal H versus strong B outputs without label inspection. If impossible, report inadmissible instead of switching to already-solved historical examples.

**Final:** `P38_P2_FIBER_FASTHTTP_NATURAL_ORIGINAL_DEPENDENCY_PINNED__OWNERSHIP_PARTIAL__FAIR_PREDICTIONS_MISSING__NO_NATIVE_GO__DIP49_HOLD`.
