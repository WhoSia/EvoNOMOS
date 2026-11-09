# P44-F31 — Frozen Go Package Closure: Build-Bound Source-Frame Certificate

**Date:** 2026-11-09. **Stage:** C3-FRAGMENT, not a general Go soundness theorem or LAW-R2.

## Scientific problem and previous boundaries
F27 proved the *classical* exact sequential repair-factorization lemma given complete independent finite edit graphs. F28–F30 built small source-grammar certificates; F30 recognizes only locally fresh, non-escaping pointers and exact one-token edits. However merely checking `a.go` and `b.go` in an arbitrary directory did not establish which source files an actual Go build would compile, nor the module/build context. This is a **source/build closure evidence gap**.

## New F31 assumption-controlled contract

The *input package* is **exactly** three regular (not symlink) files:
- `go.mod` with **byte-exact** content `module example.com/evonomos-f31-closed\n\ngo 1.23\n`.
- `a.go` and `b.go` satisfying the prior F30 grammar: package fixture, pure Legacy string literal; fresh local `p := &Left/Right{Value: "<canonical literal>"}; return p.Value`, scalar string field, no imports/calls/globals/alias/escape.
- no other entries including `*_test.go`, ignored build-tag sources, C files, nested directories, dotfiles, go.sum, go.work, or other auxiliary source. A deliberately narrow *closed research language*, not a statement about a typical Go project.

**F31 implementation** creates fresh temporary directories and copies the exact bytes. It runs F30's existing AST source checker on one frozen two-Go-file copy, and independently runs `go version`, `go list -json .` and `go build -trimpath .` on a second frozen three-file copy. It rejects compiler file metadata other than precisely `GoFiles=[a.go,b.go]`, and refuses CgoFiles, IgnoredGoFiles, invalid Go, test files, other/embedded files, imports, dependencies and incomplete/error package. Go subprocess environment explicitly requests GO111MODULE=on, GOFLAGS=empty, GOWORK=off, CGO_ENABLED=0, GOTOOLCHAIN=local, GOPROXY=off, GOSUMDB=off, GOOS=linux, GOARCH=amd64 and exact **reported Go1.23.2**. Hash SHA-256 binds name and bytes of all three copied files. It compares the three original files before and after to catch ordinary source drift.

**Positive grade** = `FROZEN_PACKAGE_GO_BUILD_AND_AST_RIGHTS_UNVERIFIED`. Source rights remain mere caller-asserted boolean claims, not authenticated maintainer grants. The Go executable's binary SHA/signature and platform trust chain are not verified; PATH, inherited environment, tool compromise, cache and OS effects are out of scope. Even the source-directory reread is not an atomic authenticated repository snapshot, nor a signed provenance statement. None of this proves arbitrary real source tree closure or external customer observational equivalence.

## F31 conditional soundness lemma

If the three-file universe is complete and byte-identical to the frozen verified compilation, the Go1.23.2 compiler corresponds to its declared ordinary semantics, real editor permissions match the declared grants, and the admitted edit grammar remains the F30 unit-priced one-token mutation, then the F30 source-frame lemma applies to the **same copied files the Go toolchain recognizes and compiles**. Therefore edits to A and B commute and preserve the declared Legacy and opposite future-port outputs, and two initially unmet local future demands require exactly two unit source edits.

The proof is composition of (i) literal/locally fresh pointer no-escape source effect lemma from F30, (ii) exact copied byte identity across AST and compile paths, (iii) checked compiler package source list and actual successful compile, and (iv) F27 product lemma over the admitted edit grammar. We have **not** proved that compilation success itself implies repair independence: a Go-valid cross-call program compiles yet F30 AST correctly returns HOLD.

The mathematical argument is conventional software build reproducibility + source integrity + static program slicing, *not an independent general theorem* and not priority over typed compiler checking, separation logic, rely-guarantee, or classical points-to analysis.

## Reproducible test court
Go1.23.2 local: `go test -count=1 ./...`, `go vet ./...`, `go test -race -count=1 ./...` PASS. Tests include positive frozen build, extra hidden build-tag Go file, test Go file, C source, nested folder, go.work/go.sum/dotfiles/README, module name/version/dependency corruption, symlink, cross-function call and global shared pointer, absent actor grant, changed source checksum, and positive-Go-build-yet-repair-frame-HOLD negative control.

CI log history: initial F31 run [#42556626936](https://github.com/WhoSia/EvoNOMOS/actions/runs/42556626936) FAIL due to test generator leaving unused p in cross-call negative control; corrected in later commit [`745734fb`](https://github.com/WhoSia/EvoNOMOS/commit/745734fb3a1378eaeabceddfe7abf81113a448c1), after direct GitHub file readback. **Do not call corrected CI success until fresh job conclusion and logs are independently seen.**

## Baseline/novelty and research direction
The F31 package closure check is deliberately elementary: a classical Go build metadata check and a standard source parser with identical input can establish it. It does not improve over classic program analysis. Value: correctly separates three evidence layers `SOURCE_FRAGMENT`, `BUILD_SNAPSHOT`, `EXTERNAL_RIGHTS`, refusing to promote an AST result to full Go/unrestricted maintainer authority. It supplies auditable failure modes for actual later Go support. Next decisive research is authenticated pinned git/tree closure and equal-information alias/SSA benchmark on independent changes; an ordinary source parser+compiler is not a weak rival to be dismissed.

**Verdict:** F31 limited build-closure methodology, general G1–G7 OPEN, LAW-R2 HOLD, PR #13 Draft unmerged.
