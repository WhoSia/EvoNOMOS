# P35-O4 — Quote-Origin Information Loss: D12 Prospective Go Demand and Calibration

**2026-10-09.** Parent: P35 OPEN; LAW-R2 NOT AUTHORIZED. O3/D11 source outcomes were already known. **The information-loss example is POST-O3 exploratory calibration, not a blind confirmation. The proposed D12 behavior below is prospective relative to any D12 original-source treatment.**

## Origin and distinct historical authority
This note responds to actual [15.md](https://drive.google.com/file/d/1zQ9j6GmfFaijbfz024-CQ2sJpj_SnpJV/view) and [DIP-49](https://app.notion.com/p/3ccef561cf92818484a4d55302715e84)/[DIP-50](https://app.notion.com/p/3ccef561cf92811291b4c56437bc5b4b). It does not rediscover bisimulation, observational quotient, APR, or Parnas information hiding. The previous [O3/D11 source result](P35_O3_D11_TWO_GO_REPOSITORIES_REAL_REPAIR_VERDICT.md) established seven bounded source-repair witnesses without law identification. It already contained two helper decoders using a `[]string` token output. This note directly inspects both Go implementations.

## Calibrated negative observation (known-source, not new-law)
For the synthetic research-only header, O3 source function `p35O3ResearchTokens` returns `[]string`, both for `ping` and for `"ping"`. The two distinct physical inputs are therefore mapped to the same decoded token `["ping"]`. If a downstream matcher receives **only** that decoded token, no deterministic downstream function can distinguish the physical representation. Formally for `E(x)=E(y)` and every function `g`, `g(E(x))=g(E(y))`. This is elementary factorization/information loss, completely explained by classical semantics and parsing theory.

A new, self-contained Go calibration in `tools/p35-o4/provenance` reproduces the two O3 algorithm shapes for this counterexample. Local `go test -count=1 ./...`, `go test -race -count=1 ./...`, and `go vet ./...` passed. **This is NOT native verification against upstream Chi or Gorilla, NOR a full parser equivalence claim.** Reproduction code is not an independent original source intervention and does not entail any `MUST` edit location; repairs may re-read raw fields elsewhere.

## D12 future source-change demand (frozen before D12 source intervention)
Retain all D0/D8/D9/D10/D11 behavior, LIVE/SNAPSHOT's existing separate temporal contracts, and published APIs. Add an opt-in quote-sensitive exact-match capability for synthetic `X-EvoNOMOS-Mode`:
- Ordinary preexisting registrations still match both `ping` and `"ping"`, as under D11.
- An explicitly new `RouteQuoted("X-EvoNOMOS-Mode", "ping", middleware)` registration matches the *quoted* physical token `"ping"` but not bare `ping`. This new API name is a proposed Chi-local extension, not an existing upstream method. Invalid quoted physical fields remain excluded atomically and independent repeated fields must still work.
- The D12 source treatments must separately implement this in pinned original Chi LIVE/SNAPSHOT × INLINE/HELPER alternatives, maintaining original full Go/race/vet tests. Any Gorilla replication requires a separately frozen API-preserving analogous contract, not a fabricated identical API.
- Freeze D12 acceptance Go tests and hash BEFORE any D12 production edits. Include positive/negative, repeated physical field and previously valid D11 cases, and distinguish expected baseline D12 FAIL from regression failures.

## Competing forecasts and their epistemic status
**B2 (strong classical information loss / parser abstraction):** only the erased string token stream cannot realize the new quote-sensitive query; a working source patch must access or preserve additional quote-origin information somewhere. This predicts the *necessary information*, not a globally necessary source location or edit count.

**B0 (strong source-aware repair baseline):** source readers can locate token decoding, registration and matching, and propose multiple valid edit sites; no invariant about a unique minimal patch or design winner is committed.

**H-temporal (EvoNOMOS scoped candidate):** whether a registry is LIVE or SNAPSHOT is not, on its own, enough to determine whether D12 is source-repairable. It predicts at least one valid patch per architecture, but this positive prediction overlaps B0/B2 and therefore **cannot by itself identify a beyond-SOLID law**.

**H-option (open competitor):** source-level parser choice may shape the future set of *selected* admissible edits even if current D11 behavior is the same; this requires a frozen, explicit admissible edit grammar and at least two independent repairs per compared structure before any `May/Must`, repair-option dominance or architecture superiority is attributed. **Prediction signatures for strong model-pair identification are NOT yet separated: `DIP49_IDENTIFIABILITY_HOLD`.**

The new D12 query separates *decoded-string-only* from *quote-origin-aware* implementations as a classical negative control. **It does not separate classical B2 from EvoNOMOS H-temporal.** It is barred from LAW-R2 promotion unless a different genuinely competing structural signature is prospectively identified and faithful source-level D12 demand/carry-forward is demonstrated under DIP-50.

## Gates
`O4_LOCAL_GO_CALIBRATION_PASS / D12_NATIVE_GO_NOT_RUN / D12_GO_ORACLE_FROZEN__ORIGINAL_NEGATIVE_PENDING / STRONG_RIVAL_PAIR_NOT_SEPARATED / P35_OPEN / LAW_R2_NOT_AUTHORIZED`.

Next concrete action: [frozen original-Chi D12 acceptance](../../tools/p35-o4/tests/chi/p35_o4_d12_test.go) was committed in human [579bb74](https://github.com/WhoSia/EvoNOMOS/commit/579bb7469f5791b0deb6f0716dd2177098d914c3) before any D12 production-source treatment, with an expected-negative pinned-original [Actions workflow](../../.github/workflows/g8-p35-o4-d12-negative.yml). Its hosted outcome must be checked separately. After confirming original negative, execute original-version source interventions and inspect which B0/B2 explanations remain undefeated; terminate this path if classical predictions are sufficient rather than manufacturing a law.