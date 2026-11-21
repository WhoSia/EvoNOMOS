# Chat 26 — External Issue Triage for F38 (NONBLIND, NO EDIT EXECUTED)

Authoritative source: original go-chi/chi GitHub issue pages and timestamps retrieved with connected GitHub tool 2026-11-21. **These issues predate the F37 task selection today but were selected *after* reading both arms. They therefore cannot be called blind samples.**

| Issue | Created UTC | External assertion | Why it is not immediately a clean F38 outcome |
|---|---|---|---|
| [go-chi/chi #995](https://github.com/go-chi/chi/issues/995) | 2025-05-02 13:06 | Singleton middleware handler shared across Group can overwrite next handler and misroute requests | Depends on middleware ownership and temporal aliasing, heavily overlapping P44-R3; F37 arm grammar currently lacks group-specific middleware setup |
| [go-chi/chi #1035](https://github.com/go-chi/chi/issues/1035) | 2025-11-18 05:41 | Regex path segment with suffix subpath yields unexpected matching | May demand upstream router behavior change; lacks a matched task on both app-arm selectors and authenticated upstream editing rights |
| [go-chi/chi #1263](https://github.com/go-chi/chi/issues/1263) | 2026-11-16 16:54 | Header-router middleware range over map produces nondeterministic selection on overlapping matches | Issue author already describes outcome; both F37 app arms share Chi dependency; neither has existing RouteHeaders in its frozen baseline |

**Selection decision:** All three remain *external-issue candidates, not issued tasks*. No source modifications, task outcome or forecast score is assigned. If the experimental goal is interface-vs-callback **app source** distinction, choosing a defect inside a shared upstream dependency likely results in TIE/OUT_OF_SCOPE, which must be recorded rather than hidden.

## Valid next-selection protocol

1. Freeze a **pre-existing timestamped issue sampling population**, e.g. fixed repository+issue-number range and a reproducible lexical filter, before arm-specific fixes are designed.
2. Annotate issues by task feasibility, actor authority, shared-upstream versus application-owned edit locus, independent customer oracle and previous exposure. Annotators cannot erase failed/out-of-scope candidates.
3. Label the current three as researcher-selected exploratory. An independently blind holdout requires task allocation or independent authoring without looking at arm-specific cost.
4. Apply each eligible request to identical F37 source commit and explicit application-only edit rights. Upstream library bugfix cannot be falsely credited to user-owned handler/callback structure.
5. Preserve a classical source-aware rival with same source, issue and budget. If no eligible issue remains, ABSTAIN instead of manufacturing F38 PASS.
