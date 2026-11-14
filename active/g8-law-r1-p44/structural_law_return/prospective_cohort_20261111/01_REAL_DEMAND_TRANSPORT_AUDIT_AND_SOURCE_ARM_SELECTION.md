# EvoNOMOS P44 — Real-Demand Transport Audit and Source-Arm Selection
**2026-11-11 KST | Historical cohort readback + prospective-arm preparation; NO causal effect estimated | LAW-R2 HOLD**

## 1. What was independently checked now
Read these existing research artifacts at branch `research/law-r1-p44-r3-stateful-alias-court`:
- `structural_law_return/experimental_gate_20261110/03_RESTIC_23_ISSUE_POSTBODY_SOURCE_SCOPE.json`, with pre-body freeze commit `8b13ba1cc408471f96251286c6016795abbf3c12` and scoping rule commit `3ae16eec99a8313725632e80975f9b5d30c01f71`.
- `experimental_gate_20261110/00_REAL_SOURCE_COHORT_ELIGIBILITY_AND_NEXT_CAUSAL_STUDY.md`.
- Original `tools/p35-p4/arms/{independent,shared}` and `tools/p35-p4/tests/acceptance_test.go`, original acceptance test blob `79b8d3007eef1a842e5e5070d7171407e4a8dd79`.
- Original Oct 9 P35-P7 two-arm commit `a47876564d7463b76f7ddbf130a8ac357d6e5691` and source blob IDs reported in the existing eligibility audit.

These are source/metadata reads; this note did not run native Go programs, recruit maintainers, or independently reexamine all external issue bodies.

## 2. Exact retrospective observed cohort denominator
`03_RESTIC_23_ISSUE_POSTBODY_SOURCE_SCOPE.json` contains 23 entries: 8 `bug_report`, 8 `new_feature`, 2 `ci_build`, 2 `security_release`, 1 `ci_release`, 1 `architecture_proposal`, 1 `test_infrastructure`. Exactly 6 carry a broad, researcher-assigned `high_recall_storage_related=true`: issue IDs 22116, 22120, 22140, 22150, 22164, 22168. **All 23** have `can_claim_p35_unified_composed_same_client_repair=false`; **all 23** have `result=unexecuted_on_both_p35_arms`. This is a source-target eligibility/transport failure, not 23 observed negative causal effects. The query sample is not a globally verified census and has no random sampling foundation; 0/23 must NOT be treated as a software-wide rate with a binomial interval.

Even among 6 high-recall hits, several refer to other storage subsystems or new features. An upstream full-application bug cannot be presumed to act on our narrow P35 backend-interface substitute.

## 3. Concrete source pair whose baseline is actually in the repository
P35-P4 is a preferable narrow source-paired *candidate* for an initial controlled study (but NOT yet a valid prospective cohort):
- Independent: `tools/p35-p4/arms/independent/content_charset.go` (Git blob `7ecb4a2d5e91d7ef775f824e64f2210bf360e5f2`), `content_type.go` (Git blob `8751cb40ca041b8f56bc1c6b9260db0a28434ee6`). These each invoke Go's `mime.ParseMediaType` independently.
- Shared: `tools/p35-p4/arms/shared/content_media_parse.go` (Git blob `1144b1fd275994fde766a331a9995cafc2ed0eb9`) defines `parseCanonicalContentType`, which centralizes parsing for the two middlewares.
- Frozen common test: `tools/p35-p4/tests/acceptance_test.go` has 16 table cases including quoted charset, reordered parameters, malformed syntax, duplicate charset, bodyless bypass, and optional charset. This test provides a finite old-client observation set ONLY, not full contextual equivalence. Tests previously passed in historical work; this research turn checked the source blobs and test content rather than re-running the Go test.

## 4. Candidate physical mechanism, with a discriminating rival
A shared parse boundary can reduce repeated future updates when both consumers are obliged to adopt the same new parsing semantics, but it can unnecessarily propagate a semantic change when one consumer must preserve an old behavior and another must change. In the second situation an independent or selectively adapted boundary may retain more permissible repair actions. These are **untested conditional hypotheses**, not discovered effects. The simplest equal-information rivals are conventional call-site/dataflow change-impact analysis, Parnas' uses relation, DRSpaces, and an explicit conventional setup-vs-future-maintenance cost model.

**Before external future demand is known, freeze source-arm baseline and a selection rule.** A candidate selection rule is: externally originated Go HTTP Content-Type/charset middleware demand published **after 2026-11-12 00:00 UTC**; include all matching reports in dated monthly windows, irrespective of whether parsing is actually affected; a source-target eligibility decision is made without inspecting solutions or outcome patches. Distinguish request publication time from the time a researcher first sees it. Do not yet claim this is an *active sealed study*: source-pair equality outside the 16 test cases, third-party source/demand independence, real maintainer actor assignment, authenticated owner edit rights and locked selection/analysis receipts remain unverified.

## 5. Identification impossibility given current observations
Let Y_shared(d,h), Y_independent(d,h) denote actual maintenance outcomes on the same future demand d and actor stratum h, under explicit fixed repair rights and old-client contracts. The current archives contain neither valid paired outcomes nor an experiment assigning independent actors under matched constraints. Both hypothetical completions Y_shared<Y_independent and Y_shared>Y_independent are compatible with every currently observed eligibility count, because no counterfactual repair outcomes were observed. Thus the sign of a source-specific causal advantage is not identified by the 23-issue census, its six scoped candidates, or the known Chi #1247 repairs. Even a structural *prediction* is not an observed effect.

## 6. Decision and next technical gate
1. Preserve P35-P4 as a source-paired **pilot** with stated finite old client oracle; independently check any future demand's applicability to BOTH arms before enabling the experiment.
2. Do not retrofit Restic issue narratives into these middleware source variants, and do not choose only "favorable" issues after reading the answers.
3. Before testing a new demand, freeze source tree SHA, toolchain and dependencies, repair rights, maintenance actors, complete old/new oracles, time/effort logging, change budget and equal-information conventional baseline.
4. Retain ALL failures/timeouts and compute a vector of correctness, effort and regression; do not equate syntax-site count with labor.
5. If a strong conventional baseline predicts the contrast equally well, report a negative novelty result rather than escalating LAW-R2.

**Verified in this review:** exact existing 23-entry metadata counts; six high-recall IDs; zero validated same-contract U/C paired tests; P35-P4 original source blob identities and 16-case old oracle; original P35-P7 Oct9 commit chronology. **NOT verified:** independent new demand, native rerun now, authenticated owner permissions, actual maintainer effort, prospective sign, external generalization. **P44 RUNNING / G1–G7 OPEN / LAW-R2 HOLD.**
