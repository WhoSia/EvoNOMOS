# P44-F28 — First Go-source-anchored factorization certificate, deliberately closed fragment

2026-11-06, research-only branch. **C3-FRAGMENT / conditional syntactic source certificate; NOT full source evidence G1–G7, NOT LAW-R2.**

## Source language and exact scope

Assume a COMPLETE Go compilation unit containing exactly these two real files and **no hidden Go, assembly, cgo, generated, test-only, overlay or imported packages**, with fixed Go1.23.2 semantics:
- a.go: `package fixture` with exactly `func Legacy() string { return "<old>" }` and `func FutureA() string { return "<literalA>" }`.
- b.go: `package fixture` with exactly `func FutureB() string { return "<literalB>" }`.
- No comments, build directives, imports, methods, fields, type parameters, package globals, call expressions, variables or other declarations. Each return must be one ordinary or raw Go string literal.
- A specific *synthetic laboratory grant* authorizes owner-A to replace only the FutureA return literal and owner-B to replace only the FutureB return literal. No authentication of these grants by parsing source; caller must establish actor scope separately. The actual maintained upstream owners have not provided grants.
- Observer contract concerns the three declared pure no-argument string functions under ordinary Go1.23.2 compilation; old customers require `Legacy() == "old"`. Future demands in this experiment are `FutureA()=="new"` and `FutureB()=="new"`, each unit literal replacement price 1.

## Statement F28-SOURCE-FRAME, strictly conditional

Given a complete compilation unit from the language above, a prior valid `Legacy()=="old"` contract, externally authenticated editing actors/grants, and only the specified single-return-literal edit grammar, the original old-client output remains unchanged after each permitted edit, and the opposite Future port output also remains unchanged. Therefore, in the complete four-state 2-by-2 local source grammar, each interleaving of the two distinct future demands has the same unit-cost staged repair optimum 2 from `a0,b0`, with all previously accepted demands preserved.

**Justification:** The AST grammar excludes any source expression or declaration capable of reading the opposite component, modifying shared data, invoking a function, initialization or depending on imported packages. A permitted edit alters only one return literal; `Legacy`'s AST and the other Future function's AST are unchanged. Under ordinary Go semantics each zero-argument literal-return function evaluates to its literal and has no effects. Thus the observable triple is exactly `("old",A,B)`. The only changes in the stipulated edit universe are A and B literal replacements; paths commute, have independent grants and unit additive price. F27's classical staged product theorem applies. This is a **source-language-fragment proof**, not a novel theorem about all Go programs. Even the assumption of a complete source universe and authenticated grants is NOT established by `Check`.

## Implemented conservative source-to-fragment checker

[`f28_go_cert/cert/cert.go`](f28_go_cert/cert/cert.go) uses standard Go `go/parser` AST, rejects imports and any unexpected declarations/expressions, checks exact package/ports/function signatures, and emits SHA-256 digest over *filename-scoped bytes* and the three literal values. Its positive receipt explicitly includes "caller grants supplied, NOT independently verified". Missing grant, unexpected filename, cross-call, global variable, comments/build tag or altered grammar results in `ErrHold` rather than an unsafe approximation. `RepairCost` handles only two named synthetic demands; no generalized Go repair search.

Crucial epistemic limit: the checker cannot itself establish there are no third-party files, dependency behaviors, different Go compiler, build overlays or falsely asserted source ownership. SHA is an integrity binding of the supplied two files, not an attestation of an official repository build closure or a signature from a maintainer. In unrestricted Go, an AST-only independence claim is not sound.

## Native execution and negative controls

Locally: `go version go1.23.2`; `go test -count=1 ./...`, `go vet ./...`, `go test -race -count=1 ./...` all PASS. Original cert package: 16 atomic tests (source grammar and synthetic costs) and independent fixture package: two tests. Native mutation test executes **all four** compiled source combinations (a0/b0, new/b0, a0/new, new/new), checking actual old and current client outputs through Go's compiler and test runner. In the GitHub research branch the equivalent source and tests have been committed, and a strict Go1.23.2 CI workflow was installed; the workflow outcome must be separately read before claiming its PASS.

Adversarial cases: cross-component function call, shared global, import, build directive/comments, added function, nonliteral source expression, wrong package, missing actor grant, incorrect file name. Rejected source states are `HOLD`, not automatically unsafe or impossible. No held-out real issue or independently administered source permits used.

## Priority and equal-information rivals

Any competent compiler-aware AST/slice analysis can demonstrate this literal-only fragment's independence using the SAME source, rights assumptions and observations. Go's `go/types`, `golang.org/x/tools/go/ssa`, traditional interprocedural alias analysis and a program-slicing baseline are natural comparators for larger fragments. The published `golang.org/x/tools/go/pointer` documentation explicitly discusses both whole-program MayAlias guarantees and omissions involving unsafe, reflection and native code. Do not represent the F28 toy as novel or superior to these methods. Independent source certificates for actual Go aliases/effects/permissions, all-client contracts, plus strong measured comparators remain the next research gate.

## Science court

**P44-F28: SOURCE-FRAGMENT-1 CONDITIONAL PASS** for a complete supplied two-file/literal-only world and *research-defined* grants; actual Go test execution of four states locally PASS. **General-source G1–G7 OPEN, LAW-R2 HOLD**. F27 remains a classical factorization theorem, not a new universal SOLID mathematics.
