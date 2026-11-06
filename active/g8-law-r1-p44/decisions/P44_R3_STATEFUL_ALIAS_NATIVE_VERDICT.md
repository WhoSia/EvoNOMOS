# EvoNOMOS Generation VIII LAW-R1-P44-R3 — Original-Source Stateful Middleware Verdict

Date: 2026-11-04. Scope: one purpose-built application fixture using **real maintained Chi v5.1.0 RequestID middleware**, two independent routing engines, and fixed barrier-controlled temporal observations. **SOURCE NATIVE PASS; CLASSICAL ALIAS THEORY EXACT MATCH; LAW-R2 HOLD.**

## Immutable pre-execution provenance

- Requirement protocol GitHub commit [6cb41ff6](https://github.com/WhoSia/EvoNOMOS/commit/6cb41ff685bafe99846cec488819c88cebee5f3f) predates all new R3 implementation tests.
- First source workflow [41776010824](https://github.com/WhoSia/EvoNOMOS/actions/runs/41776010824) FAILED before tests because `go mod verify` could not verify locally replaced application module (`missing ziphash`). This is **not** a source experiment failure.
- Corrected CI commit [629b4696](https://github.com/WhoSia/EvoNOMOS/commit/629b4696d30c87f9c3d8551c1d04ffcd5b70996c) verifies pinned external Chi module `Sum` and `GoModSum` directly and uses local source checkout for the replaced application module.
- Original source GitHub Actions [41776319508](https://github.com/WhoSia/EvoNOMOS/actions/runs/41776319508), tested **exact commit 629b4696d30c87f9c3d8551c1d04ffcd5b70996c**, job **126397415822** completed **SUCCESS**. Original job logs independently read: Go 1.23.2 Linux amd64, original `github.com/go-chi/chi/v5@v5.1.0`, module sum `h1:acVI1TYaD+hhedDJ3r54HyA6sExp3HfXq7QWEEY/xMw=`, GoModSum `h1:DslCQbL2OYiznFReuXYUmQ2hGd1aDpCnlMNITLSKoi8=`.
- Source of upstream maintained middleware: Chi v5.1.0 `middleware/request_id.go`, Git blob SHA `4903ecc2144e186a74a25a3a4552cf9a74098ed6`. The Shared store and Capture implementation are our investigator-created app fixture, **not a production case or external historical maintenance PR**.

## Four native observations (all PASS)

After GET-A capture of value v1, POST-B updates the same synchronized shared object to v2, then GET-A resumes and subsequent GET-C starts:

| Router | app capture semantics | GET-A body | GET-C body | D1 snapshot |
| --- | --- | --- | --- | --- |
| Stdlib ServeMux | LiveAlias | v2\|req-A | v2\|req-C | violates |
| Stdlib ServeMux | FrozenValue | v1\|req-A | v2\|req-C | satisfies |
| Chi.NewRouter | LiveAlias | v2\|req-A | v2\|req-C | violates |
| Chi.NewRouter | FrozenValue | v1\|req-A | v2\|req-C | satisfies |

All old-client sequential GET(v1) / POST update(v2) / GET(v2) tests passed for both routers and both capture modes. Fixed X-Request-Id headers demonstrate upstream RequestID context propagation without random-generated request IDs.

A mutex protects the shared value. Native Go race checks passed for both implementations while LiveAlias violated the temporal request snapshot: race freedom **does not imply** temporal semantic preservation.

## Independent classical comparison and synthetic repair

Classic source-aware AST check confirms explicit pointer field, mutex field, frozen assignment, Context injection, shared LiveRead, value-copy read and use of original middleware.RequestID. Parser negative-control invalid source rejected. Core local and CI go test, go vet, go test -race PASS; native source test/vet/race PASS.

Ordinary alias and happens-before reasoning predicted all four source cases before execution. Under the fixed app-only Capture edit grammar, the repair from live pointer to immutable captured string has synthetic unit cost one in both routers. **The classical source-aware rival predicts the same result; no evidence of EAC incremental predictive advantage or structure-specific repair superiority.**

## Source and external validity limits

- A single deliberately scheduled capture(A) < write(B) < read(A) execution, not exhaustive scheduler exploration.
- Only named HTTP GET/POST inputs and response body semantics, not full client contexts.
- Pinned original Chi middleware is maintained upstream, but mutable app fixture and future task are researcher-designed, not externally sampled code maintenance.
- Go race detector is dynamic, not a static universal non-race theorem.
- The AST rival detects syntax facts and cannot establish complete alias/effect or contextual equivalence.
- No developer engineering labor cost or independent authorization study.
- All G1–G7 general source certification obligations remain OPEN. LAW-R2 HOLD.

## Research decision

**P44-R3 bounded original-source court COMPLETE; classical alias explanation wins equally.** Important result: extend EAC research from static requests to temporal observer indexing, without claiming novel theory. Next meaningful source problem: independently sourced stateful middleware change with multiple simultaneously aliased objects or a real version-history holdout, and a complete equal-information source-level competitor. Do not continue to accumulate only investigator-designed positive fixtures.
