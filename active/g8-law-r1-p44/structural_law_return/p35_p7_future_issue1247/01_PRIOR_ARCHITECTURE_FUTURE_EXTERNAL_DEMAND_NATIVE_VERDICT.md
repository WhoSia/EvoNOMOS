# EvoNOMOS — Historically Prior Architecture × Independently Later Maintenance Demand: Chi Issue #1247

**2026-11-10 KST — SOURCE-NATIVE CHRONOLOGICAL COHORT 2/2 PASS — ARCHITECTURE-SPECIFIC ADVANTAGE NOT DETECTED — LAW-R2 HOLD**

## 1. A better chronological unit than post-issue toy designs

Existing P35-P7 source architecture alternatives were created and validated **2026-10-09** in [P35-P7 report](../../../g8-law-r1-p35/P35_P7_GO_STRUCTURAL_RIVAL_AND_CONDITIONAL_ENVIRONMENT_VERDICT.md). Both are authentic compiled modifications of the exact same upstream go-chi/chi v5.1.0 \`middleware/route_headers.go\`, with unchanged public \`HeaderRouter\` API and matched initial old D0 customer outcomes:
- LIVE: on each request, traverse a mutable registry, sorted header names and in-header registration order;
- SNAPSHOT: compile/deep-copy sorted header groups at handler construction.
They are genuinely different *before* the new issue, not repairs proposed after seeing it.

The [**outside maintainer go-chi issue #1247**](https://github.com/go-chi/chi/issues/1247) was filed **2026-11-01**, AFTER both source architectures had been committed. It reports that a mixed-case configured exact header match fails because original \`RouteHeaders.Handler\` lowercases incoming values but \`NewPattern\` retains configured capitalization. This is external independent origin and a HISTORICALLY later customer demand, but the issue body and reproduction were already read before this run. Thus the study is **time-split but not analyst-blind**. The 2026-10 old alternatives were generated in anticipation of different header-routing functionality; causal task-selection independence was not randomized and no future-demand effect was prospectively inferred on October 9.

Current original base: real go-chi/chi v5.1.0 commit \`67be7d9cafdaeb4e04e887ff78d09e030ee43b00\`, with BOTH original research-authored source arm files intact. The new study never overwrote those arm snapshots; it copied them into independent ephemeral original upstream clones. The source module test harness runs Go1.23.2.

## 2. Pre-execution source contract, observed failure and source edit

[Pre-execution study contract](00_CHRONOLOGICAL_TWO_PRIOR_ARCHITECTURES_LATER_ISSUE_PRESEAL.md) initially froze protected original behavior and later new cases before this source execution. The customer oracle is actual [external Go test](evo_issue1247_future_contract_test.go) with:
- six old cases: lower-case exact and wildcard configured patterns still match mixed-case input, unrecognized request uses fallback, no match continues to default;
- four later cases: exact \`Gold\` and \`RouteAny(["Silver","Gold"])\` from independent issue (2 cases), plus source-derived wildcard prefix \`Go*\` and suffix \`*OlD\` (2 research-added cases).
- all are checked in BOTH architectures against unchanged initial source, then after an identically defined classical local fix.

Initial baseline for both original arms: **old protected cases PASS; all four new cases FAIL**, both externally reported exact/RouteAny cases returning fallback. Native CI expressly expects pre-fix RED and validates named cases; **green research CI at this stage does not mean old code satisfies later contract**.

One **identical app-research-authored** source repair normalizes the configured text once in shared \`NewPattern\` constructor (\`value = strings.ToLower(value)\`), consistent with existing lookup-time lowercasing. The repair runs against the two original PREDEMAND architecture variants and has no need to modify either LIVE per-request registry traversal or SNAPSHOT compilation mechanics. It is a conventional text normalization solution, fully predicted by ordinary Go source reading.

## 3. First-run eligibility failure and auditable correction

The FIRST [CI #42779006000](https://github.com/WhoSia/EvoNOMOS/actions/runs/42779006000) **FAILED** before any new #1247 source patch was applied. The harness unintentionally copied the **later P35-P7 D8** test along with Oct 9's original D0 tests. Original SNAPSHOT arm failed 2 D8 specificity tests, which are not initial Oct 9 customer requirements, so this was **retrospective contract leakage**. It does not indicate SNAPSHOT fails its frozen D0 (or #1247). The initial source variants and all frozen #1247 cases remained unchanged.

[Explicit protocol amendment committed as 619dd214](00_CHRONOLOGICAL_TWO_PRIOR_ARCHITECTURES_LATER_ISSUE_PRESEAL.md) recorded the problem and required only two pre-existing Oct D0 tests: \`p35_p7_common_test.go\`, \`p35_p7_modes_test.go\`. A workflow correction at \`bdd5183b\` made this change; no model/source/test outcomes or code repairs were silently altered. This retains a post-first-run protocol modification, so it cannot be falsely described as a single never-edited pristine preregistration.

**Methodological lesson:** a later feature's acceptance cannot be retroactively imposed as the baseline eligibility contract when comparing historical architecture alternatives. Otherwise a fabricated baseline disadvantage is introduced by information leakage.

## 4. Native actual result

[Final GitHub Actions **#42779140245 SUCCESS, 2/2 jobs**](https://github.com/WhoSia/EvoNOMOS/actions/runs/42779140245), each with original upstream source identity assertion, original Oct-9 arm, negative RED pre-fix reproduction, single common patch, protected old/later new named tests, original full \`go test -count=1 ./...\`, \`go vet ./...\`, native \`go test -race -count=1 ./middleware\`.

| Original pre-demand structure | pre-fix old D0 | pre-fix Nov issue cases | same common local edit | post-fix protected old + Nov customer | full original Go+vet+race |
|---|---|---|---|---|---|
| LIVE Oct-9 | PASS | FAIL (expected RED) | \`NewPattern\` lowercasing | PASS | PASS |
| SNAPSHOT Oct-9 | PASS | FAIL (expected RED) | \`NewPattern\` lowercasing | PASS | PASS |

Original source production file modified in both: \`middleware/route_headers.go\`. One identical common additional normalization point, equal conventional source-explanation. No independent actor patch times or multiple patch attempts, no long-run regression/human effort, and no true randomized external demand distribution.

Both final original Go job logs were read and independently show new tests' original four failures (2 source issue, 2 research expansion), then POST FIX new suite PASS, full Go PASS, vet and race PASS. The earlier invalid D8 spillover CI failure remains a separate artifact, not erased.

## 5. Causal and theoretical interpretation

This yields a **real time-ordered, source-level matched-design negative result** for the named demand: an October structural choice of LIVE versus SNAPSHOT does **not** alter the minimum demonstrated file-local repair mechanism, protected old test outcomes, or customer acceptance in November. It does NOT establish identical *optimal* repair effort, nor explain every possible future demand:
- LIVE and SNAPSHOT are different in their response to the prior contradictory D-LIVE and D-FROZEN demands.
- A complete optimum/unique minimal patch was NOT proven: only one successful identical one-location patch was demonstrated.
- The authors of both treatments are the same research team; **zero actual independent maintainer agents** ran and there was no randomized architecture×maintainer interaction.
- Issue had already been read by researcher before new fixture and patch, so hypothesis is retrospective source-informed, not blinded forecast.
- Classical equal-information code understanding fully accounts for the tie because both retain the same \`NewPattern\` data path and matching semantics.

**One valuable selection principle at this point is a methodological exclusion, not a new architectural law:** to identify a conditional design advantage, choose a later demand that actually exercises the structural distinction between the prior arms; otherwise a routine common-field correction can tie independent architectures. But choosing only favorable tasks *after seeing* both implementations introduces selection bias. The next cohort must be chronologically held out and issue-selected by a rule fixed independent of source outcome.

## 6. Highest-priority next concrete step

The pre-existing [P35-B1 four-guidance Latin-square assignment](../../../../tools/p35-b1/assignment_manifest.json) remains \`agentRuns=0\` and lacks frozen model/version/budget/executor. Do NOT call any of the two manually scripted repairs an actual maintenance-agent run. The next genuine science step is independent coding actors using the same old/new customer contract and observation/time budgets on pre-existing equal-current-function architectures, with original code changes and complete failures retained. If not available, perform no fake agent run.

Choose future issues by a transparent blinded or chronological protocol and include BOTH later demands interacting with architectural boundaries and those that do NOT, because the present **negative tie** is a necessary control against cherry-picking. Compare complete source-aware Parnas/dataflow/DSM baselines, source inspection costs, real edit/test effort and independent followup safety.

**P44 G1–G7 OPEN / C5 STILL NOT AUTHORIZED / LAW-R2 HOLD.**
