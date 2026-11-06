# EvoNOMOS P44-R3 — External Maintenance Issue #825 Native Source Court

Date 2026-11-04. **EXTERNALLY MOTIVATED SOURCE REPRODUCTION PASS · APP-ONLY REPAIR PASS · CLASSICAL DATAFLOW EXPLANATION · LAW-R2 HOLD.**

## External evidence, preexecution seal and executable custody

Actual maintained upstream issue: [go-chi/chi #825 — Duplicate Request ID if Use middleware several times](https://github.com/go-chi/chi/issues/825), opened 2023-06-08; still marked open when inspected 2026-11-04. The original reporter claims double application of RequestID regenerates a new ID and proposes reading context or propagating the ID into the header. This experiment has **real external problem motivation**, unlike the earlier researcher-invented mutable Shared fixture. However the outcome was already publicly reported; therefore this is NOT blind prediction or a new discovery.

Before writing any issue-specific Go code, the source issue and exact contract were frozen in [GitHub preexecution commit 27ac2418](https://github.com/WhoSia/EvoNOMOS/commit/27ac2418a7693d82f82c1971862b11ea34251138).

Tested [original GitHub Actions run #41777130111](https://github.com/WhoSia/EvoNOMOS/actions/runs/41777130111), job 126399974936, exact source commit `8212e297c03bbe42143632ecdf5e88edb5c440da`. The workflow completed **SUCCESS**; original job logs were read. Go 1.23.2, pinned `github.com/go-chi/chi/v5@v5.1.0`; upstream source file `middleware/request_id.go` Git blob `4903ecc2144e186a74a25a3a4552cf9a74098ed6`. Module sum `h1:acVI1TYaD+hhedDJ3r54HyA6sExp3HfXq7QWEEY/xMw=` and GoModSum `h1:DslCQbL2OYiznFReuXYUmQ2hGd1aDpCnlMNITLSKoi8=` were verified in the job log. Go test, vet and race ALL PASS.

## Raw original-source bounded results

Two nested calls to the *unmodified original Chi* middleware.RequestID, one before intermediate observer and one after:
- Without explicit request-id header, stdlib-backed and chi-backed apps both yield **nonempty but unequal** intermediate/final request IDs (native `EXTERNAL_825_RAW ... same=false` for both).
- With explicitly supplied `X-Request-Id: user-7`, both observers in both apps see `user-7` even without repair, satisfying preserved old client behavior.
- Authorized **application-owned** `PreserveRequestID` adapter reads the existing outer context ID, clones the request and its Header, sets the forwarded `X-Request-Id`, then invokes the second unmodified middleware. Both source-backed apps yield **equal, nonempty** intermediate/final IDs (native `EXTERNAL_825_BRIDGE ... same=true` for both).

The fixture directly nests RequestID twice. It does **not** recreate the third-party httplog module mentioned by the reporter, nor does it change any upstream Chi source or prove a released upstream fix.

## Repair rights, cost and scientific interpretation

Rights: app-owned middleware chain insertion and cloned request headers only; upstream Chi source, global RequestIDHeader and Go runtime are not mutable. Under this named intervention grammar the bridge is one synthetic app edit for both router stacks; actual engineering labor unknown. Other repairs (removing duplicate wrapping, editing upstream middleware, changing logger configuration) might be preferable under different rights and must not be ruled out.

Classical context/header dataflow already predicts the duplicate ID and the bridge: outer WithContext stores ID, inner original RequestID checks only request header, and cloned forwarded header makes both read same string. Conventional reasoning explains everything in this source slice; no incremental EAC prediction, no new LAW-R2.

## Remaining source-certification obligations and next court

G1–G7 still general OPEN; no full client observational equivalence, arbitrary middleware chain, independent code-review approval, human effort, or broad source-law proof. This is a meaningful *external-issue reproduction and conditional app-only repair demonstration*, not universal architecture ranking.

Next move: source-supported task #892 ([URL params are not available inside middleware on the root router](https://github.com/go-chi/chi/issues/892)) is a separate candidate, not yet preregistered or tested. Avoid post-hoc claiming discovery from public issue text. Study actual independently maintained application PRs with known patch provenance and compare semantic rival/cost under identical rights before any LAW-R2 promotion.
