# R82 — Authentic upstream fix corroboration (not an ATLAS discovery)

**Evidence status:** Verified via go-chi/chi GitHub upstream tag and actual maintainer commit. **Paper B remains REJECT/HOLD; independent ATLAS STOP.**

## Verified historical facts

- Earlier upstream source: `go-chi/chi@v5.1.0:middleware/route_headers.go`, Git blob `997bed569ad89aec1f30765bfc6e868a7f232b6d`.
- In the `Handler` closure, an empty route table triggers `next.ServeHTTP(w, r)` without immediately returning; the no-match/default branch can call `next.ServeHTTP(w, r)` again.
- Our independent isolated Go 1.23.2 reproduction using the verified original v5.1.0 source and P35 researcher D0 tests observed an exactly-once expectation failure (actual `2`). The research D8 exact/wildcard tests also failed under some conditions, but D8's priority contract was researcher-defined and its failures are **not** classified as upstream defects.
- **External upstream correction:** [go-chi/chi commit `05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723`](https://github.com/go-chi/chi/commit/05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723) / PR #1045, explicit title *fix(middleware): add missing return in RouteHeaders empty check*. The maintainer patch inserts `return` after the first call and adds regression coverage asserting exactly one call. This directly corroborates the historical defect, **without implying that EvoNOMOS caused, discovered first, or contributed to the upstream fix**.
- Team variants were not byte-identical with v5.1.0. Upstream `997bed56...`, team LIVE `ad9a2fbc...`, team SNAPSHOT `e9ca2c38...`. Thus the previous R80/R81 isolated tests remain **team-derived-source studies**. Two sources can share behavior or a fix without being the same software revision.

## Negative-control framing

An actual upstream fix constitutes independent evidence that a concrete software behavior was changed, but neither this defect nor the patch establishes a new architecture decision framework.

**Strong-baseline failure mode:** A conventional bug report, source diff, test and a linked ADR already supply sufficient information to understand the exact-once fix. Unless a matched-information study independently shows lower missed-change rate or lower human cost with some additional representation, no independent ATLAS contribution follows.

## Case-screen decision

PR #1045 is an **existing independent upstream repair case candidate** for E1 case inventory (external fix written by maintainers). It is **NOT** a preregistered blind E1 observation: the researchers have already seen its outcome, and it must be excluded from the held-out evaluation set or marked as a nonblinded development example.

An E1 case manifest needs externally selected unseen PR/issue histories, revision timestamps, source hashes, blinded gold adjudication and equal-information strong ADR arms. Without these, `E1_DESIGN_READY_NOT_EXECUTED`.

## Source integrity & limits

- Reproducer: [r82_real_upstream_test.py](https://github.com/WhoSia/EvoNOMOS/blob/main/tools/p35-p7/r82_real_upstream_test.py), full upstream verified before running.
- Team source provenance gate: [r82_upstream_fidelity_audit.py](https://github.com/WhoSia/EvoNOMOS/blob/main/tools/p35-p7/r82_upstream_fidelity_audit.py).
- Upstream observed header order also depends on Go map iteration; observed variability across repeated test runs cannot be promoted to a universal stable header precedence contract.
- The upstream commit is a historical verified artifact, not a new repair to submit or claim.
- This document does not assert that the whole go-chi module or all versions were independently tested.

**Status:** `EXTERNAL_PATCH_CORROBORATED · TEAM_VS_UPSTREAM_DISTINCTION_ENFORCED · E1_HELD_OUT_CASES_NOT_COLLECTED · STOP_ATLAS · NARROW/MERGE`.
