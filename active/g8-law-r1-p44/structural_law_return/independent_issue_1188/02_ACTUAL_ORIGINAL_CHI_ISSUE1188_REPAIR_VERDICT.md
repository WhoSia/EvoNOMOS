# EvoNOMOS — P44 Independent External Go-Chi Issue #1188: Actual Source Regression and Two Bounded Repairs

**2026-11-10 KST · actual ORIGINAL GO source executed · baseline new contract FAIL / old contracts PASS / two valid source-repair arms PASS · NOT architecture×maintainer causal factorial · LAW-R2 HOLD**

## 1. Independent demand and experimental custody

Outside reporter [go-chi/chi #1188](https://github.com/go-chi/chi/issues/1188), created **2026-09-23**, states that routing regexp placeholder followed by suffix may erroneously consume a slash in one named segment. Reporter observed it on a later v5.3.2 release; that later source/diff was not inspected for a repair in this study. The 2026 issue text **was read** and contains a complete reproduction, so this demand is independent in **author**, not blind in information or genuinely issued after our experimental architecture selection. Original authentic upstream Go source **v5.1.0** at \`67be7d9cafdaeb4e04e887ff78d09e030ee43b00\` was fixed before reproduction; it predates issue.

[Pre-native source-reproduction contract](00_ORIGINAL_CHI_ISSUE1188_SOURCE_BASELINE_PRESEAL.md), human GitHub commit \`6e410e4d9cc41ce5a682fcca61335f91b1d0272d\`, froze public old and new route behaviors before execution. Research-owned [Go customer test](evo_issue1188_contract_test.go) was copied into an **ephemeral checkout** of original upstream, without modifying original production files.

## 2. Source-native prior-version red/green evidence

[Baseline original GitHub Actions #42763113563 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/42763113563) on pinned Go1.23.2 Linux, original exact source, 4 old customer route cases and 3 issue cases:
- GET \`/re/a.json\` →200 name=a; \`/re/b.json\` →200 name=b; \`/bare/a\`→200 name=a; \`/plain/a.json\`→200 name=a: all **old protected clients PASS**.
- GET \`/re/a/b.json\`: original **HTTP200 name=a/b**, while issue asks 404. An **intentionally inverted expected-red check** verifies that exact regression and fails CI if the original no longer reproduces.
- \`/bare/a/b\` and \`/plain/a/b.json\` are already 404: pass.
- With the deliberately failing research test temporarily removed, original \`go test -count=1 ./...\` and \`go vet ./...\` PASS.
- **Green overall CI** here certifies the asserted source old-PASS/new-RED negative control; it does NOT indicate original Chi passes the new issue requirement.

## 3. Freeze and actual two source modifications

[Research-owned two-variant pre-execution contract](01_TWO_REPAIR_INTERVENTIONS_PREEXECUTION.md), committed \`b36a8f1c2631e524e59e65cbc3a4e3eb22d01e9b\` after baseline RED and original \`tree.go\` code inspection. The identified source defect is the original conditional chain that checks a slash only in an \`else if\` branch when the candidate is NOT matched via a non-nil regexp. No claim of independently discovering a previously unknown maintainer fix.

Real original \`tree.go\` source changed in two separate ephemeral original checkouts by [exact-slice guarded script](apply_source_repair.py):
- **Inline guard**: relocate slash prohibition before regexp match, so both regexp and plain parameter nodes receive the same segment constraint.
- **Helper extraction**: introduce \`validSingleSegment(s)\` with the same slash predicate, call it from that boundary, and retain regexp verification.
- Both preserve current old-client tests, reject all three named invalid cross-segment cases, pass \`go test -count=1 ./...\`, \`go vet ./...\`, and original core \`go test -race -count=1 .\`.
- Both have **1 original production file changed: tree.go**. The helper arm additionally declares **1 new Go function** (five added source lines in its declaration). No wall-clock human maintenance, semantic equivalence across all Go/route inputs, downstream client deployment, performance advantage or post-change independent demand was measured.
- Native CI [**#42763380085 2/2 SUCCESS**](https://github.com/WhoSia/EvoNOMOS/actions/runs/42763380085). Both job logs read back: original Go source diff, old-contract named tests, new-contract named tests, full native Go suite, vet and core race all green.

This shows **two different ways to implement the same required constraint**. It does NOT create an authentic pre-demand architecture treatment pair: both source fixes were authored after seeing the issue and old failed source. Nor does the fact a helper adds lines prove a negative general architectural value of helper extraction.

## 4. Mathematical interpretation and limits

For the declared 7 URL cases, \`Observation(Inline)=Observation(Helper)\` after their repairs, with the same source authorization in the disposable Go checkout. This is a **finite observation equivalence**, not a contextual equivalence under arbitrary public or internal callers. Two strongly valid repairs tie on declared correctness and modified file count. A classical local guard/dataflow analysis already predicts the sufficient condition; no new general inference rule over classic source reasoning.

This is a calibration source for re-entering the 2026-07 founding program:
- **A** original source structural intervention, but currently only two chosen remedies to one pre-known issue (not independent architecture comparison).
- **M** research-script patches, explicitly NOT actual independently operating coding-agent maintainers. Original P35-B1 [agent assignment](../../../../tools/p35-b1/assignment_manifest.json) still says \`agentRuns=0\`, model/version/time budget/observability undefined. Do not infer maintainer × architecture interaction from these two patches.
- **D** a genuinely external author-issued issue, but its description/source location was already seen, and original version predates its appearance; a later truly unrevealed change request must be protected from hindsight.
- **Y** measured bounded source old/new functionality and regression tests only; missing repair labor, source inspection cost, failure denominators, cognitive work, deployment and long-horizon utility.

## 5. Scientific disposition

**Original issue reproduction validated independently on earlier exact source, two normal source repairs both pass; no unique helper/interface ability or conditional law.** Retire repeated small Go syntax fix demos at this point. The next high-value trial must genuinely run different **equal-input** maintainer actors or source-analysis tools on **preselected architecture variants** before revealing a further independently authored demand, score failed attempts and full customer conformance, and compare the strongest ordinary modularity/source-analytical rival. No unsupported numerical cost or new theorem promotion.

**P44 G1–G7 OPEN / PR #13 DRAFT / LAW-R2 HOLD.**
