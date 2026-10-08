# G8 LAW-R1-P33 — Six-Paper Canonical Intake, Conflict–Cut Duality, and Source-Checked Repair Feasibility

**Stage:** P33 OPEN. **Outcome:** Original PDF acquisition 6/6; bounded computational cut-certificate METHOD PASS; prospective OO generative law HOLD. **LAW-R2:** NOT_AUTHORIZED.

## 1. Exact original-PDF custody

Each item was opened in Google Drive, the actual first-page title and author line inspected, source parent `00_INTAKE — Literature Radar` confirmed, canonical duplicate search performed, renamed without replacing bytes, moved to `10_PAPERS — Canonical Literature Commons` and its new parent/name re-fetched. Existing conventional filenames use one em dash `—` separating author/year and title, ASCII hyphen `-` for title-internal subtitle punctuation, no en-dash substitutions.

| Original paper | Actual Drive PDF ID | Principal original contribution | Specific P33 novelty boundary |
|---|---|---|---|
| Mechtaev, Yi & Roychoudhury (2015), *DirectFix: Looking for Simple Program Repairs* | `16QMAUMiJc3gG8Wzg-spz1xhdPmF1LrYX` | Partial MaxSAT combines fault localization and component-based synthesis, prioritizing structurally simple fixes | Small patch synthesis and low regressions already studied; do not pretend a minimal-support optimization is new |
| Mechtaev, Yi & Roychoudhury (2016), *Angelix: Scalable Multiline Program Patch Synthesis via Symbolic Analysis* | `15I7adM7arPLYTsqyPGZAK8dog9d7Udh1` | Angelic forests and controlled symbolic analysis produce dependent multi-location patches; authors explicitly state angelic forest is an underapproximation, sound for test passage but incomplete for all solutions | No unrestricted exact repair-enumeration claim for P33 |
| Reiter (1987), *A Theory of Diagnosis from First Principles* | `17-uaqjK-ZidPYnGt_6hoflnBEKTKlvVx` | Theorem 4.4: diagnoses precisely minimal hitting sets of conflict sets under its diagnosis definitions | Hitting-set duality is classical; diagnostic component suspicion ≠ necessarily valid program edit |
| Nguyen, Qi, Roychoudhury & Chandra (2013), *SemFix: Program Repair via Semantic Analysis* | `16oNRPxDrS7hsllT-0g5Xtyjo8L8mk5p8` | Fault localization, symbolic execution, repair constraints and layered expression synthesis | Basic semantic constraint synthesis is a strong repair baseline |
| Smith, Barr, Le Goues & Brun (2015), *Is the Cure Worse Than the Disease? Overfitting in Automated Program Repair* | `1C8y3I-lajj4bQy8zz_-molwA0DmTTHi7` | Independent test suites on 998 buggy student programs; repair overfitting and test-suite provenance | Correctness of a candidate tested against design-time oracle cannot count as independent corroboration; domain expansion is a true adversarial gate |
| Guigue (2014), *Approximation of the Pareto Optimal Set for Multiobjective Optimal Control Problems Using Viability Kernels* | `1cwzxZvx7nnOdLHYikB5A4QbFYzFPEvFR` | Set-valued return; epigraph equals a viability kernel of an augmented dynamical system; convergent finite set-valued approximation | Pareto fronts, viability and set-valued Bellman recursion are NOT new EvoNOMOS mathematics |

**DOI record:** DirectFix `10.1109/ICSE.2015.63`; Angelix `10.1145/2884781.2884807`; Reiter `10.1016/0004-3702(87)90062-2`; SemFix `10.1109/ICSE.2013.6606623`; Smith `10.1145/2786805.2786825`; Guigue `10.1051/cocv/2013056`.

## 2. Contract-constrained information loss and necessary repair locations

Let X be a source execution-state domain, f:X→M the complete downstream-visible observation through a frozen interface, and g:X→Y the desired externally specified result.

**Classical factorization equivalence:** A deterministic downstream-only function h satisfying `g=h∘f` exists iff `ker(f) ⊆ ker(g)`. This is not novel. A colliding pair x,y with f(x)=f(y), g(x)≠g(y) certifies that downstream-only computation without an auxiliary channel cannot correct both states. In a policy edit grammar, repairs must either cross/modify the observation boundary, add an independent information channel, or change/restrict the requirement/domain.

**Finite source witness:** pinned Uptime Kuma commit `398482d590daaac0d44e288c9be3bc6f6667f8b8` encodes certificate message `[name][url]` with no escaping and gives the dispatcher no `monitorJSON`. Program A edits the caller to forward context and passes the bounded strengthened oracle; program B edits dispatcher-only parsing and fails adversarial collisions. Original source fails even the simple context oracle. Details in `P33_INFORMATION_CUT_REPAIR_FAMILY_AND_THEORETICAL_PRIOR_ART_COURT.md`.

**New executable finite certificate (not new theorem):** `tools/law-r1-p33-repair-cut-certificate.mjs` reads the source-method execution output, generates 64 parametrized distinct pairs of legitimate string/URL states with equal legacy observations and different desired results, then checks obstruction supports for an explicitly frozen three-location edit grammar (caller channel, dispatcher parser, template fallback). With no side channel and no ability to modify the required output, the sole necessary cut-crossing source location among these candidates is `server/model/monitor.js`. This is a **grammar-relative necessary hitting set**, not a globally necessary edit in all programs. Exact hosted read-only CI **37810762909 SUCCESS**, artifact **11564738090**, sha256 `45b031289c538a67a07a5c37ce458ed7e50dd4b0660313038e362c78c93fc940`. The source method and oracle tests were run before computing the certificate; it is not a blinded prospective requirement.

### Necessary-versus-sufficient caveat

Let C_1,...,C_n be obstruction escape sets of allowed edit locations, each a sound necessary condition (`S∩C_i != empty`) for a valid repair S. Then every valid support hits each C_i. Inclusion-minimal hitting sets are **lower-bound candidate families** for supports and do not guarantee a compiling, correct, efficient or future-stable repair. The proof is one-line set logic, and Reiter gave a richer diagnosis-level characterization in 1987. To claim a source-repair equivalence, P33 would need a completeness direction that normally fails unless the edit grammar and oracle are extraordinarily restricted.

### Correct source-level decision targets
- `PotentialChangeImpact(a,source_edit,configuration)`: configuration and dataflow dependence exposure.
- `CandidateRepairFeasibility(a,d,grammar,oracle)`: typed, permitted patches + observed pass/fail.
- `InformationObstruction(a,d,interface,grammar)`: exact colliding source states and required outputs, plus allowed sites capable of changing the observation.
- `ContinuationValue(a',d_{future},policy)`: policy- and environment-indexed set-valued future lifecycle outcome; not determined by local edit-support minimality.

A stronger B2 is not just CSDG; it includes existing program repair synthesis, string/contract reasoning, diagnostic conflict/hitting-set methods, and design-rule structures. If P33's H reduces to these when given the same input, downgrade novelty. The existing P33 source witness is a **negative control** against the weak claim that downstream code can recover arbitrary lost information.

## 3. New joint theoretical research question (NOT YET CLAIMED)

Can a **source-extracted family of observation cuts and capability/authority constraints**, combined with an *explicit edit grammar and environment-indexed, nondeterministic repair transition relation*, predict **which valid repair policies preserve the future Pareto frontier** under an independently frozen sequence of maintenance demands, **beyond** (a) semantic APR, (b) conditional SDG/DRSpaces, (c) edit-size heuristics and (d) established set-valued control?

This may justify a thesis/paper only if a new *mechanism-discriminating source-pair* is found: same frozen demand and full functional oracle, outcomes held out at forecast time, rivals with information parity and a direct contrary prediction in signed cost, admissibility or Pareto set. P32 and P33 retrospective Uptime Kuma results cannot substitute for that.

## 4. Cross-Shelf Harvest transport rules

Primary [Harvest LR-20261009-P33](https://app.notion.com/p/3f3ef561cf9281819a9fd930746e5ca5) integrates these six original PDFs into the P23 mapping-failure → P27 typed orientation → P32 demand-obligation → P33 source-information-cut lineage. **Transfer is a research hypothesis, not scientific-law authority.** No separate nested Harvest created for each paper.

**Verdict:** `P33_SIX_CANONICAL_PAPERS_VERIFIED__FINITE_CUT_CERTIFICATE_HOSTED_PASS__GENERAL_REPAIR_SYNTHESIS_NOT_NOVEL__STRONG_RIVAL_PROSPECTIVE_HOLD__LAW_R2_NOT_AUTHORIZED`.
