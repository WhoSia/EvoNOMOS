# P44 F38 / Paper B — Real Chi Issue and Requirement Authority Preflight

**2026-11-22 KST. Source reads:** public GitHub issue REST JSON and issue comment REST JSON (external independent author timestamps). **Researcher selected post hoc** and research team has no asserted maintainer authority. No F38 prospective/blind cohort claim.

## Three historical issues and source assertions

| Issue and original author | Timestamp, source scope | Original request or observation | Crucial follow-up | Epistemic gate |
|---|---|---|---|---|
| [go-chi/chi #995](https://github.com/go-chi/chi/issues/995), mmmmmrob | 2025-05-02 13:06Z, app-authored `Middleware(next)` singleton and nested Group | Same mutable singleton used on multiple group constructions; user observed requests `/`, `/foo`, `/bar` being routed to last group. Author's requested outcome: singleton works correctly, **or** unmistakable error | [2025-05-20 independent comment with fresh-per-invocation instance](https://github.com/go-chi/chi/issues/995) is an app-owned workaround; original author confirms understanding, **but explicitly reiterates surprise and asks for singleton working or error** | genuine third-party issue; nonblind, upstream issue still open; app-only fresh allocation can restore outputs but **does not implement singleton support or explicit error** |
| [go-chi/chi #1035](https://github.com/go-chi/chi/issues/1035), bekabaz | 2025-11-18 05:41Z, static `/users/me` vs param `/users/{id}`, methods | Reported method 405 falling through to PUT `{id}`, and *separate* regex + trailing subpath failure | Same-day author comment: **regex issue was misleading and cannot be reproduced in isolated tests**. 2025-12-19 suggestion: explicit PUT/PATCH/DELETE static path; 2025-12-22 third-party suggests upstream StrictRouting | DO NOT count original regex claim as confirmed defect. 405 path-scope contested. Old-client contract and allowed upstream rights UNVERIFIED |
| [go-chi/chi #1263](https://github.com/go-chi/chi/issues/1263), pawangopallavudya-commits | 2026-11-16 16:54Z, `middleware.RouteHeaders` map iteration | Claims requests matching overlapping registered headers can choose differing middleware responses; asks deterministic selection or explicit unsupported configuration | Issue author claims test on contemporary master `c64ed7d`, Go 1.27.3, not pinned v5.1.0. No original F37 arm application source expresses this configuration | Nonblind, upstream-version mismatch, no F38 inference about pinned original F37 |

## #995 reproduction logic and separate acceptance criteria

For the **user-submitted** app-level source (not original F37 app code):
- Old observation expectation: three paths return distinct `Hello World!`, `Hello Foo!`, `Hello Bar!`.
- Original middleware is mutable `var singleton middleware`; its constructor overwrites `singleton.next` on each stack creation. This mutable state is independent of handler/callback map selection.
- Researcher app-only workaround creates a new `middleware{next:next}` on each constructor call; normal HTTP paths should pass.
- But original author's **normative acceptance** was singleton safety *or* a detectable error. Quietly rewriting their app's singleton into fresh allocation changes the implementation and **does not fulfill that precise upstream API expectation**.
- Tests may demonstrate a **known functional workaround** on pinned Chi v5.1.0, not resolve the upstream issue or establish authorized API compatibility.

## F38 and Paper B significance

This is the first in this series using the *literal external author's subsequent discussion* to distinguish a code-observation question, a permitted app-only implementation change and the actual requested API semantics. The relevant contract may live in the maintainer's public API or issue discussion; a passing authored test does not appoint the researcher to negotiate that contract.

Proposed bounded source-authored test: reproduce #995 request routings through pinned original Chi, compare singleton and per-invocation instance, no network listen, no writes or upstream source edits; record actual outputs, no forced assumptions about how unknown versions behave. Test is **nonblind exploratory**, not F38 outcome. Keep the F37 original handler/callback arms untouched.

## Disallowed inference

- Do NOT report #995 as solved by altering the submitted singleton API semantics.
- Do NOT promote #1035 original regex subpath statement as independently confirmed after author retraction.
- Do NOT infer #1263 F37 2025 pinned-library failure from 2026 development-head result.
- Do NOT call these three source-selected issues a prospective unbiased cohort, measured review accuracy, or new conditional software-architecture law.
