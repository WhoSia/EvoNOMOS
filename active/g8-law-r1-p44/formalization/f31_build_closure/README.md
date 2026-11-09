# P44-F31 — Frozen Build Closure and Conditional Source Frame

This module strengthens F30 by requiring a **three-file complete source package** and checking actual Go compiler package metadata on a **separately frozen copy**, not only source AST.

## Reproduce committed code
```bash
cd active/g8-law-r1-p44/formalization/f31_build_closure
go test -count=1 -v ./...
go vet ./...
go test -race -count=1 ./...
```
The module uses a local Go-module replacement to sibling `../f30_fresh_pointer`; it requires that F30 source grammar checker on the research branch.

Original GitHub Actions Go1.23.2 CI:
- [Failed first run #42556626936](https://github.com/WhoSia/EvoNOMOS/actions/runs/42556626936): negative control left an unused pointer variable, so the purported *valid Go* example failed to build. Preserved, not hidden.
- [Corrected original committed-source run #42556983915](https://github.com/WhoSia/EvoNOMOS/actions/runs/42556983915): **SUCCESS**, original logs checked, unit tests/vet/race pass, including compiler-success-but-repair-frame-HOLD and compiler-ignored-extra-source-HOLD.

## The actual evidence layers
1. Exact original module bytes `go.mod`, `a.go`, `b.go` and strict directory inventory. No hidden source, test-only file, build-tag-excluded file or symlink inside this **input package directory**. Other repository directories are NOT audited.
2. F30 AST structural source-fragment analysis executed on the same copied Go source bytes, and an SHA-256 source digest.
3. `go list -json .` must enumerate precisely these two GoFiles and no others, imports or dependencies; `go build -trimpath .` must succeed in an isolated copy, requested Go1.23.2 linux/amd64, fixed Go flags.
4. Original source bytes re-read after checking; this is **not** an atomic git-tree snapshot or a signed build attestation.
5. Positive grade `FROZEN_PACKAGE_GO_BUILD_AND_AST_RIGHTS_UNVERIFIED`, no independent maintainer grants, source ownership or verified compiler binary. No modern Go SSA/alias generality.

## Distinct important falsifiers
- A program that calls FutureB from FutureA may **compile successfully**, but frame independence is false. F31 rejects it via F30 source grammar.
- An extra Go file excluded by a build tag may allow **go build to succeed**, yet the source universe is not the declared complete universe. F31 rejects the extra file.
- A source module with changed import/dependency/build environment or symlink is rejected rather than silently assigned a false-safe repair cost.

The source/build closure verifier is a classical integration of an elementary source checker with ordinary Go tools. **No new mathematical law or classic rival superiority claim.**

[Formal source-bound conditional theorem](../73_F31_FROZEN_GO_BUILD_CLOSURE_AND_SOURCE_FRAME_LEMMA.md) · [Acquired Jones (1983) rely–guarantee original, a major priority counterweight](../74_F31_JONES_1983_RELY_GUARANTEE_PRIMARY_READING_AND_PRIOR_ART.md).

**G1–G7 OPEN · LAW-R2 HOLD · PR #13 Draft, main unmerged.**
