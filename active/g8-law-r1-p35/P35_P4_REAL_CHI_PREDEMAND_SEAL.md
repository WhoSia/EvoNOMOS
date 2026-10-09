# EvoNOMOS G8 LAW-R1-P35-P4 — Independent Real-Repository Maintenance Tournament, PRE-DEMAND SEAL

**Pre-registration date:** 2026-10-09 (Asia/Seoul). **Stage:** P35-P4 OPEN; **P35 overall OPEN**; LAW-R2 NOT_AUTHORIZED. This text and the acceptance tests are committed **before any treatment-arm Go source is written or evaluated**.

## Independence, substrate, and leakage firewall

- **Independent upstream repository:** [go-chi/chi](https://github.com/go-chi/chi) Go HTTP router, release `v5.1.0`, exact native base SHA `67be7d9cafdaeb4e04e887ff78d09e030ee43b00` (release-tag commit authored 2024-06-28).
- Production frozen sources: `middleware/content_charset.go` and `middleware/content_type.go`. The first owns `ContentCharset/contentEncoding`; the second owns `AllowContentType`. Actual source and prior test files were read at `v5.1.0`; **no post-baseline solution diff may be consulted before the following predictions are frozen**. An unrelated later commit title was accidentally visible during source selection; neither its diff nor source is used as treatment, label or prediction evidence.
- This is **a fresh independently authored change demand on a real historical codebase**, not a claim that a future upstream maintainer actually made this exact change or that the patch is a replay of a historical fix. The source, predecessor history, and original tests are genuine.
- Pre-demand history cutoff: upstream tag date 2024-06-28T14:29:27Z. Observed history under this cutoff: `content_charset.go` one creation change 2017-12-11; `content_type.go` five commits (2017–2020); zero verified same-commit changes of both production files among their histories. Major v5.0.0 release sweep in 2021 changed many *tests* and is **not** a feature cochange label.
- No patch outcome, discovered repair site or future commit becomes a feature of B0/B1/B2.

## New external requirement D4 — canonical Content-Type observation

For requests using existing `middleware.ContentCharset` and `middleware.AllowContentType`, recognize MIME media-type parameters consistently instead of naively splitting raw headers. Same test oracle for both mutually independent implementations.

1. Case-insensitive `Content-Type` media type matching, including surrounding legal whitespace; case-insensitive parameter key `charset` and case-insensitive **charset value**.
2. Accept quoted charset values, quoted unrelated parameters that contain semicolons, and arbitrarily reordered well-formed MIME parameters. Using the two middlewares together must satisfy both policies.
3. Invalid MIME parameter syntax and duplicate/conflicting `charset` parameters must result in HTTP 415 for a request with a non-empty body; malformed headers must not silently bypass either guard when that guard is active.
4. Preserve previous semantics: AllowContentType allows bodyless requests without a MIME header; matching allowed media type with ordinary well-formed charset still succeeds; ContentCharset may admit a missing charset only when `""` is listed among allowed charsets; nonmatching media/charset fail as before.
5. No changes to public exported function signatures; avoid changing other chi middleware or HTTP transport code.
6. Tests are input/output HTTP `httptest` checks through actual Go router/middleware combinations, not self-adjudication by the patcher.

Invariance: no changes in exported endpoint signatures; no expected requests involving malformed Content-Type pass when non-empty. This is an explicitly **synthetic maintenance requirement** using a **real repository**, not a purported security fix assigned to upstream.

## Pre-registered arms and rival predictions (fixed before intervention)

**R0**: original untouched v5.1.0 negative control; should FAIL at least quoted/invalid-header test cases.

**R-IND** (strong simple rival, not a straw man): independently use Go stdlib `mime.ParseMediaType` in each existing guard, without adding cross-file helper or extra dispatch; predict two changed production files `content_charset.go`, `content_type.go`, two existing functions `contentEncoding`, `AllowContentType` plus import blocks. No shared helper.

**R-SHARED** (Parnas-style information-hiding rival): introduce one internal canonical parse function in a new `content_media_parse.go` and change both existing guards to call it. Predict three changed/added production files and the same two existing functions plus one new helper. This is an **alternative representation of the same semantics**, not automatically a better design. New helper overhead, future semantic change localization, unit tests and runtime dispatch are separate dimensions.

**B0+ (source-aware static):** from original sources and target names predict both production guards need changed semantics, and `ContentCharset` exported wrapper is a possible but nonnecessary edit (two true production functions among three method/function candidates). Refuse to count test files as production edits. This baseline sees the same frozen demand as both arms.

**B1 (true pre-baseline cochange):** using actual, disjoint 2017–2024 file histories, no verified cross-file cochange edge. A historical cochange rank cannot confidently recommend both files: mark `NO_HISTORY_SUPPORT_FOR_PAIR` rather than fabricate a historical success or score zero as certain evidence against B1. A strong B1 needs a history-rich independent second case; planned without outcome-dependent cohort cherry-picking.

**B2 (Parnas/Design Rule Spaces):** representation of MIME parsing is a likely *hidden design decision*. Source-level module responsibilities predict `contentEncoding` plus `AllowContentType` when the common semantics evolve; isolated standard-library parses may be adequate for one demand, while a shared helper may gain under additional changes but incurs immediate indirection and module cost. This is an interpretation with explicit conditional predictions, not a formal implemented CSDG. **Known prior art can fully explain a treatment outcome.**

**EvoNOMOS candidate H (rival, not favored):** a necessary distinction (valid MIME grammar vs quoted raw bytes) must reach both outputs; when both decisions depend on that distinction, source edit propagation can occur even without a static direct-call arrow between them. Prediction: both require semantic intervention under D4, but there is *no claimed predictive improvement over B0+/B2* unless a predeclared edge-restricted static comparator actually misses one. A null outcome is legitimate.

## Outcomes, admission and stopping rule

- *Primary*: honest original upstream `go test ./middleware` and `go test ./...`, new D4 acceptance test exact failures for baseline and PASS for independently patched arms; `go test -race` on middleware.
- *Secondary*: actual source production file count, modified existing functions (Go AST normalized), +/- source lines, new helpers/modules, downstream behavioral regressions; no imaginary human time or scalar design quality.
- *Comparators*: B0+ candidate-set precision/recall on each realized arm; B1 cochange support; B2 ability to explain without post-hoc authority; H's predeclared ability or failure to discriminate.
- *Stop*: one native original upstream test and finite arm comparison, at most bounded corrections for implementation defects without relaxing frozen tests. If all strong rivals explain result, report `NO_NEW_PREDICTIVE_LAW`, preserve source proof and proceed to a richer independent world.
- **GitHub governance:** only human `WhoSia` authored/committed source history, no GitHub Actions bot commit. Actions `contents: read`; original upstream remains unmodified; test arms are copies in CI only.
