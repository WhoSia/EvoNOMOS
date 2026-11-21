# P44 — Exact post-architecture public Chi issue census, before opening the remaining issue body

**2026-11-10 KST | METHOD/SELECTION AUDIT | NOT an original unseen design-decision forecast**

- **Source architecture origin:** actual P35-P7 LIVE and SNAPSHOT complete source variants originally built 2026-10-09.
- **Candidate issue inclusion rule:** GitHub repository `go-chi/chi`; **issues, not pull requests**, regardless of current open/closed status; creation date from **2026-10-10 through 2026-11-10 inclusive**, all labels, all titles, all issue topics; exclude task only after logged upfront non-architectural category rule, never according to treatment success.
- **Census discovery:** authenticated GitHub issue search `is:issue created:2026-10-10..2026-11-10` sorted chronological asc, `topn=100`. Exactly TWO results surfaced (below), with URL and titles (a search response is not a certified exhaustive historical archive; API results may have indexing/permission lag).
- **Issue #1241:** 'Proposal: Native PASETO middleware', https://github.com/go-chi/chi/issues/1241
- **Issue #1247:** 'RouteHeaders misses exact mixed-case header value patterns', https://github.com/go-chi/chi/issues/1247

**Information timing:** #1247's full issue text, fix and CI result WERE already read in earlier turns; selecting this cohort today is retrospectively outcome-aware. #1241 **full body was NOT opened yet at this commit** (only title and issue identifier). It is NOT an independently randomly drawn new scientific holdout; preserving its existence in denominator still prevents silently depicting a single favorable issue as a representative independent-demand portfolio.

## Pre-body classification and gate
All issues remain in census denominator; classification **without looking at LIVE vs SNAPSHOT outcomes**:
1. Public patchable existing behavior regression: author provides old/client and new/client behavior on existing API. Eligible for same-contract repair test, if reproduces in pinned 2024 source.
2. New opt-in feature: requires an authorized new API or extension; **not an existing-function regression**. Separate feasibility study possible if clearly specified; never score as comparable to an existing behavior regression, never declare an arm loses because unrelated code is unavailable.
3. Documentation/support/environment-specific issue: record as non-code action category with zero or unknown structural signal.
4. Security/cryptography proposal: **no ad hoc production security feature or own crypto**, record evidence and scope; tested only if safe upstream maintainers issue actionable, constrained spec and library dependencies are audited.

A title that sounds like an optional middleware addition (#1241) suggests category 2/4, but this remains PROVISIONAL until issue description is read. The #1247 outcome is already known (two arm tie under one classical NewPattern fix). No code or customer tests for #1241 yet.

**Decision:** retain full two-issue cohort as a small historical *demand-type mixture*, report eligible/ineligible demand rates, never compute a statistical architecture-performance distribution from two selected issue reports. No C5, no LAW-R2.
