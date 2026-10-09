# EvoNOMOS G8 LAW-R1-P35-P2 — Native Restic Eight-World Regression and Frozen-Architecture Admissibility

> **Historical P2 scope; subsequent correction:** [P35-P3](P35_P3_FROZEN_DECODER_REPAIR_FAMILY_AND_RIVAL_VERDICT.md) exhibits an additional native Restic-tested COMPOSED four-method patch that **preserves the independent read decoder**. P2's previously best-observed C5 is **not** a lower bound. Original P2 evidence remains unchanged; do not revise historical measured outcomes.

**Date:** 2026-10-09  
**Phase result:** `P35_P2_NATIVE_RESTIC_PACKAGE_PASS__P35_MAINLINE_OPEN__LAW_R2_NOT_AUTHORIZED`

## Original repository and executed receipt

**Real upstream:** [restic/restic](https://github.com/restic/restic), commit **`495982232cf1af184eac0a97871ef8161e8708ee`**. Its `internal/restic.Backend` declares 12 public methods, including six core storage operations. Native tests ran inside this pinned original repository at `internal/backend/p35pair`, not under the local fake Restic shim.

- **[Actions run #37895607800](https://github.com/WhoSia/EvoNOMOS/actions/runs/37895607800)** — SUCCESS.
- **Human-authored source and workflow commit:** [`0dfa2ede622f9d5ccfce4585f98f04d8f73bd908`](https://github.com/WhoSia/EvoNOMOS/commit/0dfa2ede622f9d5ccfce4585f98f04d8f73bd908); GitHub author and committer both `WhoSia`.
- **Execution:** Go **1.23.12**; eight source packages each ran `go vet`, `go test -race -count=1` selected prior behavior and demand-specific tests.
- **Evidence artifact:** `g8-law-r1-p35-pinned-restic-8worlds`, **ID 11599942843**, SHA-256 `49d38c9c60a7415c9b9395cb7c52db5e33cdf25e55297de6888d5f52fa89f85b`. Logs include original SHA, Go version, each source verdict, both expected negative controls and SHA-256 manifest.
- **Security:** `contents: read`, `actions: read`; no bot-authored commits, no workflow push/merge/tag/ref mutation.

## Original native Go source worlds

| Source world | Native vet + race | P34 prior 18-event history | Requirement-specific result | Frozen independent read decoder |
| --- | --- | --- | --- | --- |
| `baseline` | PASS | PASS | new demands expected FAIL | YES (P0) |
| `u-local` | PASS | PASS | KeyFile 8-byte bound PASS | U architecture |
| `c-local` | PASS | PASS | KeyFile 8-byte bound PASS | YES |
| `u-encoded` | PASS | PASS | versioned storage and legacy-prefix collision PASS | U architecture |
| `c-encoded` | PASS | PASS | versioned storage and legacy-prefix collision PASS | YES |
| `c-encoded-tagged` | PASS | PASS | versioned storage and legacy-prefix collision PASS | YES |
| `c-encoded-instore` | PASS | PASS | versioned storage and legacy-prefix collision PASS | **NO**; decoder moved |
| `c-encoded-compact` | PASS | PASS | versioned storage and legacy-prefix collision PASS | **NO**; decoder moved |

Both new-demand tests were run against unedited `baseline` and intentionally returned nonzero with the expected specific failure reason: **`EXPECTED_BASELINE_FAIL LocalKeyFile`** and **`EXPECTED_BASELINE_FAIL VersionedStorage`**.

The read-only source runner is [`tools/p35-p1/run_pinned_restic.sh`](../../tools/p35-p1/run_pinned_restic.sh), each world's Go source is under [`tools/p35-p1/worlds/`](../../tools/p35-p1/worlds/baseline/backend.go), and the common [P34 public history oracle](../../tools/p35-p1/tests/p34_public_oracle_test.go) is visible.

**Important:** Eight packages compiled inside one original Restic checkout, with replace-in-place of the separate P35 Go package. This does **not** imply the complete upstream Restic test suite, long-run durability, or concurrency stress beyond the selected `-race` tests passed.

## Coupled repair-family result, admissibility corrected

- Single-capability KeyFile change: one modified existing Go method U versus one C.
- Versioned representation: U observed two modified existing methods.
- C6 side-map and C5 tagged-entry designs pass the same original Restic observable oracle while keeping a distinct read decoder.
- C5 in-store and C4 compact reduce edit footprints partly by **moving decoding into the writable payload store**. They pass behavioral tests, but under the precommitted P35-C frozen interpretation are `ARCHITECTURAL_TREATMENT_DRIFT`, not equal-architecture successes.
- Therefore a truthful observed within-grammar comparison of source edit site counts is **U2 versus a best observed admissible C5**, **not** a theorem that `min_R(U)=2 < min_R(C)=5`; these are selected repairs, not a full exhaustive search, and source line/type/interface costs also matter.

Version information is necessary to disambiguate old arbitrary byte streams from encoded new streams with overlapping output representations. That information-cut fact is classical mathematics; moving it between stores changes the source-edit surface, not the theorem.

## Strong rival and next discriminating measurement

A conservative source-aware AST candidate baseline already covers every actually changed source method (U2 among six candidates; C5 within twelve candidates). Full CSDG/DRSpaces, historical B1 and repair-synthesis baselines were not defeated. A valid new structural-prediction result would require a *pre-demand*, information-matched claim about admissible repair families or maintenance cost that a strong rival fails on independently selected real source evolution.

**P35-P2 CLOSED as a bounded native module-method validation. P35 remains OPEN** for that stronger scientific comparison. Do not promote to LAW-R2 or hide the earlier 4-method structural-admissibility correction. Persist with new counterexamples and requirements, not repeated assertion of SOLID slogans.
