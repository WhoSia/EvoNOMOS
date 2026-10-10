# P38-P2C — Natural Maintainer Rejection, Contract-Indexed Substitution and Documentation-Only Upstream Closure

**2026-10-10 KST · RETROSPECTIVE ORIGINAL-SOURCE/HUMAN-REVIEW EVIDENCE · NOT A PROSPECTIVE HOLDOUT · NO NEW GO EXECUTION · DIP49 HOLD.**

## Historical sequence: authenticated original repository facts

1. **2021-10-24–25:** [valyala/fasthttp PR #1131](https://github.com/valyala/fasthttp/pull/1131) already proposed exporting the exact private hasHeaderValue utility. Closed **without merge** on October 25; maintainer erikdubbelboer rejected enlargement of the library's already large public API for a simple operation. Thus exposing this helper was **not first proposed in the 2026 Fiber issue**, and source presence is not evidence of owner acceptance.
2. **2026-08-11:** [gofiber/fiber issue #4605](https://github.com/gofiber/fiber/issues/4605) asked for three distinct treatments: adopt existing public fasthttp functions, request upstream exports of private helpers, and document upstream source behavior. Still **OPEN** in our October 10 screening, but not a label-unseen P38 presealed test.
3. **2026-08-21–September 7:** [gofiber/fiber PR #4628](https://github.com/gofiber/fiber/pull/4628) sought to replace the local Charset parameter scanner with public fasthttp.VisitHeaderParams. It was **closed unmerged** after maintainer ReneWerner87 reported **five divergent results among six common input probes**. The most consequential historical example made the replacement return an adversary-influenced bad charset where the existing scanner returned utf-8. Retrospective maintainer *report*, not our source-run. This is a real **semantic contract objection to an apparent implementation-reuse improvement**.
4. **2026-09-07–13:** [fasthttp issue #2385](https://github.com/valyala/fasthttp/issues/2385) reported that VisitHeaderParams prematurely returns when encountering an empty/invalid parameter. It was **closed** by [commit b38a993a](https://github.com/valyala/fasthttp/commit/b38a993a542a8d874b5d06441340d74fca37499a), which modified **only documentation (+5 / −0 lines)**. ISSUE_CLOSED ≠ BEHAVIOR_FIXED. The accepted resolution documents early termination rather than promising a semantic fix.

## Pinned original source corroboration after documentation closure

Original downstream [Fiber main commit 56cd561f7d57addc730992c75a8bde59f050c413](https://github.com/gofiber/fiber/tree/56cd561f7d57addc730992c75a8bde59f050c413) depends on [fasthttp v1.75.0 source commit 818be799bc0b086b5df262d6382bf5875fbd58f4](https://github.com/valyala/fasthttp/tree/v1.75.0) in its natural Go module graph. On the actual version's [header.go lines 877–944](https://github.com/valyala/fasthttp/blob/818be799bc0b086b5df262d6382bf5875fbd58f4/header.go#L877-L944), VisitHeaderParams skips an immediately empty separator (lines 890–893), but retains **return**, not skip, on an invalid token at lines 896–898 and missing equals/value at lines 904–905. Its documented behavior explicitly allows a truncated valid prefix when encountering an invalid later parameter.

The weaker demand "skip empty semicolon separators" and the stronger demand "continue after invalid/valueless parameters while preserving downstream semantics" are **different contracts**. A public ABI that compiles is not a sufficient demonstration of semantic substitutability. The same original upstream has a public URI.SetPath/RequestURI path invoking private appendQuotedPath, yet the wrapper applies URI path normalization and is NOT automatically a pure path-segment encoding substitute.

## Formal scope, existing mathematical priority, executable finite audit

Let A be **exactly the rejected PR's implementation**, not the entire admissible edit space. Let Q_0 require only the single normal input example and Q_6 require identical outputs on the six maintainer-reported examples. Their reported observations show:

\[
\operatorname{Pass}(A,Q_0)=1,\qquad \operatorname{Pass}(A,Q_6)=0.
\]

For demand family Q subset Qprime, any exact set of allowed patches satisfying Qprime is a subset of the patches satisfying Q. This is classic predicate conjunction/order theory, not an EvoNOMOS discovery. Therefore **this one failed implementation does not prove a source repair is impossible**. A different wrapper, corrected upstream function, local helper or policy-adjusted implementation might preserve the demanded contract.

[Machine-readable historical observation table](../../tools/p38-p2c/historical_semantic_receipt.json) and [read-only Python verifier](../../tools/p38-p2c/historical_contract_court.py) validate precisely **six reported source-derived observations (one equal, five different)**, 64 demand-subset monotonicity checks, and explicit leakage negative controls. They do **not** execute original Go or prove all-input behavior or human acceptance causality.

### Three targets that MUST NOT be conflated

- **E_SOURCE:** can a specific API or source-edit action be accessed/constructed, with owner authorization and source API constraints?
- **E_SEMANTIC:** does the *specific implementation* satisfy the fixed input/trace/invariant contract? One happy-path pass does not prove full refinement.
- **E_REVIEW:** will upstream/downstream maintainers approve, merge and release the patch? Rejection may reflect public API policy, behavioral risk, time/cost priorities or unresolved requirements, not impossibility.

Classical behavioral refinement, assume–guarantee analysis, Parnas information hiding and repair-search economics can explain these axes. [Papotti, Paramitha & Massacci (2024)](https://doi.org/10.1007/s10664-024-10506-z) provides independent relevant research on technical patch correctness versus reviewer acceptance. [Plein et al. (2026)](https://arxiv.org/abs/2606.03378) provides a serious modern change-effects prediction competitor. These original PDFs are NOT found in current Drive metadata search, so we only verified external abstracts/landing text, not full original PDFs. Original Parnas (1972), Sullivan et al. (2001) and Hong et al. (2024) are held in canonical Drive.

## P35–P37 original continuity and explanatory outcome

- **P35**: one code patch satisfying demand Q is not the entire set of future admissible edits; merge conflicts and valid repair paths must be separated.
- **P36**: architecture rankings are contract-indexed; requirements Q0 and Q6 need not yield the same preferred implementation. The real reviewer report reinforces this as a **natural historical example**, not as a new cross-architecture quantitative cost reversal.
- **P37**: original source evolution is contextual and owner-capability constrained; actual authority must be verified, not imputed from GitHub repository identity. The earlier Gorilla/SCS dual reader graph remains a research-built abstraction, whereas PR #4628 is a natural external human decision.
- **P38**: a genuinely live outcome-separating prediction still needs prospectively sealed exact Q, real cross-owner permissions, matched resource budget, and strongest implemented classical rival. PR #4628 is historical calibration and **must not contaminate holdout scoring**. Issue #4605 is still a *potential* future-demand source, not an observed successful prediction.

**Verdict:** P38_P2C_HISTORICAL_NATURAL_SEMANTIC_REJECTION_VERIFIED · UPSTREAM_ISSUE_DOC_ONLY_CLOSED · REAL_BEHAVIOR_REPLAY_NOT_PERFORMED · BEST_CLASSICAL_RIVAL_UNDEFEATED · P3_GO_BLOCKED · DIP49_HOLD · LAW_R2_NOT_AUTHORIZED.
