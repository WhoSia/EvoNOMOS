# R82 — External Audit Acceptance, Provenance Correction & Narrow Research Gate

**Date:** 2026-11-23. **Status:** Research program decision, not a new manuscript.
**External review:** [EvoNOMOS_grand_audit_ko.md](https://docs.google.com/document/d/1NDH9J3xsokv4eZidzQm__SzWEspZUDoygJhMp8Cy0QY/edit). Reviewer conclusion: **STOP** independent ATLAS; **NARROW** conditional-contract research; **MERGE** useful recording with existing ADR/AREL.
**Nonnegotiable:** An external model review is adversarial review, not independent human ground truth. Unread sources and results remain unverified.

## Critical provenance correction

The precise go-chi/chi v5.1.0 `middleware/route_headers.go` Git blob is `997bed569ad89aec1f30765bfc6e868a7f232b6d`.
The four R80/R81 research implementations are **not** that upstream blob:

| Experiment arm | Git blob |
| --- | --- |
| Original LIVE research variant | `ad9a2fbc0a30a39475f746068e74e2d3e6c93999` |
| Original SNAPSHOT research variant | `e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75` |
| D8-repaired LIVE research variant | `e481e73aa1d82497c25011b6468d7e8749c705f7` |
| D8-repaired SNAPSHOT research variant | `66e88964508cedc38740913a7c00fbf5b6e6220a` |

Verified directly through GitHub upstream tag and four EvoNOMOS `main` blobs. All four disagree with canonical upstream. Team's 7/7 source receipts are **within-repository byte identity**, not an upstream fidelity certificate. R80 native Go test and R81 microbenchmarks must always use the description **isolated native Go execution of team-maintained Chi-derived variants**. Do not claim upstream Chi regression, defect, repair, performance or deployment quality. Original D8 failures show failure of a *researcher-defined added contract*, not a confirmed defect in the upstream project.

R80 ZIP SHA-256 `050a8c291e760c907700606a5d23b17e6e4204ef2b6b6d2b3c5439c41ac96a2c` is now independently checked on a local R80 ZIP (size 12,684). The auditor had explicitly left this item NOT ATTEMPTED; it is verified by the subsequent R82 check, not retroactively attributed to the auditor.

Reproduction command from a checked-out repo (requires an actual local `go-chi/chi@v5.1.0` source):
`python tools/p35-p7/r82_upstream_fidelity_audit.py --upstream /path/chi/v5.1.0/middleware/route_headers.go --root /path/EvoNOMOS --r80-zip /path/R80.zip`.

- Exact upstream Git blob, all four variant blobs, ZIP SHA-256 and one upstream mutation control must pass.
- This establishes **source lineage mismatch**, not scientific value and not whole Chi module execution.
- Different diff algorithms give different line-change counts; the blob mismatch is authoritative.

## Research portfolio triage

| Line | Decision | Evidence status |
| --- | --- | --- |
| Independent ATLAS formalism / another new schema | **STOP** | Prior-art collisions; strong ADR synthetic tie; no independently observed superiority |
| Synthetic enumerations without independent truth | **STOP as discovery** | May remain as implementation regression tests |
| Contract-relative decision record | **NARROW** | Behavior of two team variants demonstrated; originality not established |
| Typed ADR / AREL implementation | **MERGE** | Existing representation treated as strongest baseline, never artificially weakened |
| R80/R81 source-native cost experiments | **RETAIN as engineering observations** | Reproduction on team variants only; not a test of ATLAS or human costs |
| Human reviewer decision accuracy / review burden | **CONDITIONAL E2** | Not measured; requires independent ground truth and recruitment |

## E1: decision-relevant external-source screen (preliminary protocol, NOT full preregistration)

**Question:** Does explicitly identifying the *actual existing temporal contract* change a reviewer decision on an external software change, after matching the information supplied to a strong ADR baseline?

- **Unit:** One naturally occurring, externally authored change episode from a publicly maintained repository. Cluster episodes by repository and maintainers; do not count commits in the same episode as independent.
- **Eligibility:** Public issue/PR and diff with a real contract ambiguity or observed change; independent project maintainers must have authored the source and initial requirement evidence before study selection.
- **Exclusion:** Researcher-written tests, researcher's own patches, generated synthetic stories, missing authoritative time order, source licensing/access restrictions.
- **Candidate selection:** An independent selector chooses and timestamps candidate episodes prior to outcome inspection. A fixed case manifest with repository commit SHAs and issue URLs is sealed **before** feature construction and evaluation.
- **Gold:** Two reviewers not involved in choosing the research method independently adjudicate observable repository behavior and the time-valid contract from source/issue/history; third reviewer adjudicates disagreements. Maintainer resolution is evidence, not an infallible gold label.
- **Conditions:** (A) strong typed ADR with trace links, change status, and the same evidence, (B) the exact same ADR plus an explicit temporal-contract field. An optional ATLAS encoding is included **only if it predicts a difference beyond those matched conditions**. No field-info asymmetry.
- **Primary endpoint:** Among gold-adjudicated episodes, paired difference in *correctly identified applicable contract*, false preservation/false withdrawal rates, and justified abstention. Mere output difference does not mean improvement.
- **Secondary endpoints:** Independent reviewer effort, total record-building time, evidence retrieval time, editor burden.
- **Safeguards:** Mask method labels, randomize order, separate decisions before/after source revelation; log order, re-review and reviewer clustering. Expose uncertainty, no pseudoreplication, no p-values from tiny case counts.
- **Negative result:** If (A) and (B) yield equivalent accuracy with (B) higher total burden, do **not** create a separate framework. Consider only a minimal optional ADR field.
- **Stopping gate:** Until independent selector, gold-adjudicators and externally authored case IDs exist, E1 remains `DESIGN_READY_NOT_EXECUTED`. No arbitrary 5% threshold presented as evidence.
- **Budget allocation (provisional 100 units):** upstream/source corrections 10; independent external cases/E1 30; strong ADR/AREL baseline 25; conditional human pilot E2 25; evidence audit/reserve 10. **ATLAS schema extension 0**.

This protocol is a narrow empirical decision, not a claim that “temporal contracts matter” is novel. Comparable requirements/assume–guarantee/behavioral-subtyping prior art must be screened before asserting any residual novelty.

**Final gate:** `STOP_ATLAS_AS_DISTINCT_THEORY · E1_DESIGN_ONLY · HUMAN_BENEFIT_UNMEASURED · PAPER_B_REJECT/HOLD · LAW-R2_HOLD`.
