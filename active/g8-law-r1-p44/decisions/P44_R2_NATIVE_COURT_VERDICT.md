# EvoNOMOS Generation VIII LAW-R1-P44 — R2 Native Source Repair Court Verdict

Date 2026-11-04. **R2 bounded original-source experiment PASS; CLASSICAL RIVAL TIE; LAW-R2 HOLD.**

## Immutable custody

Preexecution demand seal: [commit 90ebeef67618054071010933b1c587ca0ce9f9e0](https://github.com/WhoSia/EvoNOMOS/commit/90ebeef67618054071010933b1c587ca0ce9f9e0) before the first new source tests. Original source CI: [GitHub Actions run 41759485506](https://github.com/WhoSia/EvoNOMOS/actions/runs/41759485506), exact tested commit 97f693c19b9c5db11b570f7c3772d8028ef070c8, job 126343690443. Run status completed, conclusion SUCCESS; job summary and **raw job logs independently inspected**, native source and both classical rivals tests, vet and race succeeded.

Go: go1.23.2 linux/amd64. Chi: github.com/go-chi/chi/v5 v5.1.0 with module checksum h1:acVI1TYaD+hhedDJ3r54HyA6sExp3HfXq7QWEEY/xMw= and go.mod checksum h1:DslCQbL2OYiznFReuXYUmQ2hGd1aDpCnlMNITLSKoi8=.

The first CI attempt [#41758875735](https://github.com/WhoSia/EvoNOMOS/actions/runs/41758875735) was YAML-INVALID before any job launched; minimal workflow syntax repair [245f311e](https://github.com/WhoSia/EvoNOMOS/commit/245f311e374c2ca168e7d64d14e8fafa78d636fe) was retained. Intermediate runs cancelled under deliberate concurrency settings are not silently relabeled failures or passes.

## Native source R2 observation

Original-backed standard ServeMux and Chi (full H+D+M application adapter) were compiled and exercised under the same 12 named old-client wire HTTP requests. The frozen future requirements were:
1. GET /ledger/alpha/revisions -> 200, revisions:alpha
2. GET /ledger/alpha/audit -> 200, audit:alpha
3. GET /ledger/alpha/summary -> 200, summary:alpha

Raw CI log:
- stage 0 protected 12, achieved 0, future route units both 0, totals Stdlib 0 / Chi 3;
- stage 1 protected 12, achieved 1, future units both 1, totals 1 / 4;
- stage 2 protected 12, achieved 2, future units both 2, totals 2 / 5;
- stage 3 protected 12, achieved 3, future units both 3, totals 3 / 6.

All six possible insertion orders of these three disjoint routes passed their own old-client preservation and incremental-demand checks. The deliberate WRONG-response negative control was detected: old standard GET response alpha versus WRONG.

## Independent ordinary classical competitors

Formal 3-bit authorized application route-edit graph: all 8 source states × 8 goals × 8 rights = 512 possibilities, feasibility and minimum synthetic edit count. Original CI formally ran its pure Go unit suite, vet and race: PASS. This is ordinary guarded reachability, not a new EAC law.

Source-aware classical analyzer: Go AST extracts all three literal paths from FrozenDemands, checks limited slash-segment literal/{variable} disjointness versus protected old route, and detects deliberate wildcard collision negative controls. Original CI test, vet and race: PASS. This is a narrow grammar-level analysis, **not** a sound/complete Go-Chi program-semantic or unrestricted routing proof.

No evidence of superior source-repair prediction beyond these classical rivals in the named bounded experiment: **CLASSICAL TIE**.

## Scientific stop gate

The future tasks were investigator-selected then precommitted before execution, not a third-party blind sample. The 12 protected HTTP observations were already known from R1; they are not all clients. The simulation uses application-owned route registrations and synthetic one-unit costs, not independently verified upstream rights or measured developer time. No G1–G7 general source certification. No universal architectural superiority. No LAW-R2.

Next: P44-R3 should shift away from simply adding disjoint GET routes to independently selected stateful or middleware-dependent source changes with a strong equal-information semantic competitor, source-path certificate, failure receipts, and actual patch rights. P44-R2 is a successful **negative novelty court**: an original-source confirmed classical tie.
