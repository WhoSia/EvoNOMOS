# EvoNOMOS P44-F30 — Fresh Local Pointers, Exact Source Edit Framing

**Conditional research artifact only:** This module extends F29 from immutable struct-value projections to **locally fresh pointers** with provably non-escaping aliases under an extremely restricted Go syntax. It does not certify arbitrary Go, signed maintainer ownership, actual source inventory beyond the supplied directory, or a new universal SOLID theorem.

## Reproduce committed source

```sh
cd active/g8-law-r1-p44/formalization/f30_fresh_pointer
go test -count=1 -v ./...
go vet ./...
go test -race -count=1 ./...
```

Tested Go: **1.23.2**, original committed GitHub Actions run [#42555065535](https://github.com/WhoSia/EvoNOMOS/actions/runs/42555065535) **SUCCESS**; independently read original job logs, 30 PASS records (8 top-level + 22 subtests). First source CI [#42554957109](https://github.com/WhoSia/EvoNOMOS/actions/runs/42554957109) **FAILED due to test-local variable declarations**, repaired in commit `d5476e23`, then verified with fresh CI; failure remains in history.

## Narrowly accepted grammar

`cert.CheckDir` inventories exactly two ordinary files, `a.go` and `b.go`, in one directory; Go AST accepts only `type Left/Right struct{Value string}`, `Legacy() string` returning a fixed literal, and `FutureA/B() string` with exactly `p := &Left/Right{Value: "canonical literal"}; return p.Value`. No globals, imports, comments, extra functions, methods, pointers in fields, interfaces, dynamic initialization, other aliases, calls, channels, build tags, extra source files or symlinks. All other input **HOLD**, not necessarily unsafe.

A positive structural receipt is `DIRECTORY_AST_FRESH_POINTER_RIGHTS_UNVERIFIED`; caller-supplied A/B grants are not independently attested. `CheckEdit` verifies a before/after AST-located one-token source literal change with a byte-identical other file and unit synthetic cost. Two edit orders lead to the same final file bytes and the same SHA-256 under the declared complete source grammar.

## Native Go negative control

The actual compiled case `var shared = &Left{Value:"a0"}; FutureA() string{return shared.Value}; FutureB() string{shared.Value="new";return shared.Value}` retains `Legacy()=="old"` yet makes FutureA change after FutureB executes. F30 correctly **HOLD**s that source. It does not infer that every shared pointer is unsafe; it merely does not certify that broader source language.

## Theorem / limitation / literature

[Proof, native countermodel and source limitations](../71_F30_FRESH_POINTER_FRAME_SOURCE_THEOREM_AND_NATIVE_COUNTERMODEL.md) · [Verified missing originals and classical prior art](../72_F30_MISSING_PRIMARY_SOURCES_AND_POINTER_PRIOR_ART.md).

A classical Go SSA/points-to or separation-logic analyzer with equal inputs can infer the same simple non-escaping fresh allocation; **no unique predictive advantage or proof economy was measured**. The authentic whole-source and rights gates remain OPEN. F30 is a significant reproducible, honest *source-fragment* expansion, NOT LAW-R2.
