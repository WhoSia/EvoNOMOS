# EvoNOMOS P44 F20 — three original maintainer source histories, native Go before/after, bounded epistemic grade

2026-11-05. **F20 HISTORICAL ORIGINAL-SOURCE REPLAY PASS (3 repos) / NO BLIND PROSPECTIVE PREDICTION / FULL OLD-CLIENT SAFETY UNKNOWN / STRONG CLASSICAL PROGRAM TESTING SUFFICIENT / G1–G7 OPEN / LAW-R2 HOLD.**

## Experimental structure: three substantive units (not empty commit padding)

- **Unit A · 11 individual commits:** metadata-only prepatch selection/custody of three external upstream repositories, exact historical commits/parents, selection leakage boundary, proposed client observers, permission/build limits, classical rival matrix, validity threats, evidence grades, stop gates. [Prepatch registry](../f20/00_F20_HISTORICAL_COHORT_PREPATCH_REGISTRY.md).
- **Unit B · 14 individual commits:** independently read original GitHub commit patches AFTER the selection registry, authored three posthoc Go contract oracles, original native Go parent/post runner with SHA checks, original GitHub Actions matrix, code-level mechanism notes and a genuine negative-control case. [Source and method audit](../f20/17_F20_UNIT_B_ORIGINAL_DIFF_COURT_GATE.md).
- **Unit C · 11 individual commits:** Go evidence typed audit code and negative tests preventing stage C3 historical reproduction from being represented as a blinded C5 future prediction, and disallowing a single helper test from proving complete public API/client contextual equivalence. [Research evidence gate](../f20audit/README.md).

The 36 commits above correspond to distinct source/test/protocol/analysis artifacts or corrections, not artificially empty metadata commits. The root README, mathematical contract, Notion and PR finalization are separate subsequent work.

## Exact independent original Go CI receipts — FINAL

**Original [GitHub Actions #41995425112 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41995425112)**, exact tested EvoNOMOS branch source commit `aa743bb8ddf665bae3a9a632fad583419b18e92a`, Go1.23.2 on hosted Linux. All three matrix jobs successfully fetched EXACT upstream parent and child SHA, ran original upstream named tests, injected a posthoc F20 contract test, showed parent FAIL at expected contract assertion and post PASS.

1. **chi job 127137439627**: Original `go-chi/chi` parent `882c15e6462ce0630529d04c330e84942ebd059d` and after `6ceb498b221efa11f559602beb2463b8b52c2161`. `Find(POST,/api/groups/v2/17)` returned `/{id}` before, `/api/groups/v2/{id}` after. Native `TestF20NestedRoutePattern` fails before and passes after. This is exported Mux.Find for ONE input, not all routers or clients.
2. **httprouter job 127137439769**: Original `julienschmidt/httprouter` parent `ef8578da8d8e1217ea44313b23edf46154b198ab` and after `484018016424d215c0b87c42f4c9b57d980fbd00`. Internal helper `allowed(/probe,POST)` when `HandleOPTIONS=false` returned `GET, OPTIONS` before, `GET` after. Native `TestF20AllowedOptionsDisabled` fails before and passes after. **This helper test is NOT a verified HTTP wire Allow header response**, since direct unexported `Router.allowed` was observed.
3. **gin job 127137439315**: Original `gin-gonic/gin` parent `9d11234efec1e5517b2887a6e7dfbc9c017bc52c` and after `ea53388e6ee4a6a0a1647b390c56eeed780e7e56`. Internal `node.insertChild("*all","*all",nil)` panic is runtime index-out-of-range [-1] before, descriptive `no / before catch-all in path '*all'` after. Native `TestF20WildcardErrorType` fails before and passes after. **A non-slash-prefixed internal helper input is not a public supported Gin route input contract.**

Original three independent job logs manually reread; each contains `F20_SOURCE_SHA stage=parent/post`, actual distinct observed outputs, `F20_PARENT_EXPECTED_REGRESSION`, `F20_POST_HISTORICAL_ORACLE_PASS`, and `F20_HISTORICAL_PARENT_POST_REPRO_PASS`. The parent failure is an EXPECTED test failure inside a SUCCESSFUL CI research workflow; not a failed upstream build. Job statuses all completed SUCCESS; original source/test name receipts are direct, not screenshots or guessed times.

## Original failed history and correction — leave visible

[Initial historical court workflow #41994958871 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/41994958871): chi and httprouter passed parent/post; Gin's first custom `tree.addRoute("/foo/b*r")` test unexpectedly PASSED at parent with the same descriptive panic string. This shows the custom oracle DID NOT discriminate the before/after change. The error was recognized as a scientific observer inadequacy, not a software bug that could be ignored.

Re-read the exact parent `tree.go` at `insertChild`: wildcard at index zero makes `i--` negative, then original immediately indexes `path[i]`; patched guard is `if i < 0 || path[i] != '/'`. A subsequent separate commit changed only our retrospective oracle to call that exact internal helper boundary. Intermediate CI concurrency-cancelled workflows are NOT failed tests. Final #41995425112 independently confirms old runtime bounds panic vs new descriptive panic.

**Extra issue in chi:** parent `TestMuxFind` contained wrongly directed assertions which the historical upstream patch corrected. A green pre-existing test did not certify the relevant nested-route pattern; original changes included both production logic and tests.

## Independent audit gate

[Original evidence-gate Actions #41996159467 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41996159467), original Go1.23.2 job `127139727142`, source commit `f092dba83b1b521bf09f5b89290523ce7c67aadd`. Go tests, vet and race SUCCESS. Go tests verify exact three full 40-character commit SHAs, unique external repositories, distinct old/new outputs, source dates/job IDs, observer scoping, negative tampered metadata and impossible C3→C5 promotion in the presence of pre-reveal issue-title leakage. A later docs-only workflow revision can be linked separately if successful, but the earlier exact audited code source run is already verified.

A typed evidence ledger is a quality gate; its booleans and manually transcribed source strings are NOT proof that the GitHub service itself or maintainers cryptographically attested every piece of metadata.

## Epistemic grading

**C1:** parent/post original commit SHA, issue subject and changed file metadata confirmed.
**C2:** upstream original source patch read and posthoc client test designed.
**C3:** original upstream Go native before-after source and tests reproduced at fixed parent/post SHA; three jobs PASS.
**C4:** still OPEN: equal-information independent full source-aware classical competitors beyond plain original Go tests and contract-aware source explanation; no complete G1–G7 source proof.
**C5:** NOT ACHIEVED: prediction committed before future issue/disclosure/outcome. All three historical issue subjects and changed files were known before posthoc oracle authored. No legitimate new forecasting accuracy claim.

## Scientific reasoning: why a retrospective result can mislead

The observed differential `o(before,x) != o(after,x)` for chosen input x proves only a witnessed changed observation for those exact sources, contexts and test conditions. It does NOT prove `∀x` contract equivalence, independently frozen future demand feasibility, source-edit minimality, actual maintainer authority, complete compiler/build provenance, or an advantage over ordinary program testing and feature/path analysis. The chi post patch contains added tests and changed assertions; Gin patch contains a separate lint workflow edit; neither automatically measures necessary engineering cost.

No KSGT/HARVEST authority transfer: this is a research operational improvement, not a new EvoNOMOS source-law theorem. Next BFS step should **not** rerun obvious historical behavior tests indefinitely. To address the founding question, require a truly pre-reveal prospective task or independently sealed chronological holdout and authenticated actor/observer rights; match static/dynamic classical analysis and actual repair cost. The exact reason our three successful reproduction events cannot be used as evidence of prediction is explicitly recorded.

**Final verdict:** Authentic three-source historical reproduction PASS; prospective source-certified safe future-repair prediction UNKNOWN; G1–G7 OPEN; LAW-R2 HOLD; no main merge.
