# F29 — Reproducible Go 1.23.2 value-frame source-edit court

```bash
cd active/g8-law-r1-p44/formalization/f29_value_frame
go test -count=1 -v ./...
go vet ./...
go test -race -count=1 ./...
```

**Positive inputs:** Complete source directory containing exactly `a.go` and `b.go`, each a regular file, with pure no-arg literal-owned struct-value construction, a fixed Legacy literal and no imports/calls/global mutable data. `CheckDir` checks the directory inventory and AST; its SHA-256 binds filename and file bytes. Unlike F28, this supports one value-struct projection per port, but **NO pointer/interface/shareable alias**. This only certifies one directory snapshot, not the rest of a repository/build environment.

**Exact patch witness:** `CheckLiteralEdit(beforeDir,afterDir,"A"|"B", grants)` requires two individually accepted complete directory snapshots and verifies raw bytes: the nonedited file is identical and the edited file differs ONLY in the AST-positioned quoted initializer literal token. It supplies a unit-cost abstract edit witness for this **declared bounded edit grammar**, not for other possible source changes. A no-op or combined edit is HOLD. Four native source variants and both two-stage edit orders are tested.

**Negative controls:** Go-valid `FutureA(){ return FutureB() }` remains old-client compatible but violates A/B independence; AST cert HOLD, while the same mutant compiles and its A output follows B's changed source value. Additional HOLD cases: pointers, interfaces, globals, imports, cross-type selector, functions, dynamic expressions, extra files, symlink, two-port edits, whitespace changes outside target token, and missing grants.

**Grade:** `DIRECTORY_AND_AST_CHECKED_RIGHTS_UNVERIFIED`. The parser cannot establish that a caller-supplied `true` grant is authentic, that a mutable directory did not race with analysis, or that Go1.23.2 matches another environment. No real upstream edits, no unseen future requirement and no strong classical source-aware baseline advantage.

**Independent CI:** [GitHub Actions #42228134629](https://github.com/WhoSia/EvoNOMOS/actions/runs/42228134629) `SUCCESS`; job source-frame, original logs inspected for Go unit tests, compiled original-Go variants, cross-call negative control, go vet and race. Later edits require fresh CI verification. [F29 source-frame theorem and proof](../68_F29_VALUE_FRAME_SOURCE_EDIT_COMMUTATION_THEOREM.md).

**Research decision:** F29 conditional closed-fragment progress, but general maintained-source G1–G7 OPEN; LAW-R2 HOLD. Compare strong conventional Go type/SSA/dataflow and slicing tools with equal inputs before scientific promotion.
