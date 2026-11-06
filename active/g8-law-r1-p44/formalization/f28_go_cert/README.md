# P44-F28: Source-aware Go independence laboratory

This is a deliberately **closed two-file Go 1.23.2 source language** under *researcher-defined*, not externally authenticated editor grants. Do not apply to unrestricted source, maintained upstream owners, hidden files, other build contexts, arbitrary clients or real effort.

## Reproduce

```bash
go test -count=1 -v ./...
go vet ./...
go test -race -count=1 ./...
```

Source files: `fixture/a.go`, `fixture/b.go`. Parser: `cert/cert.go`. Adversarial and native variant tests: `cert/cert_test.go`, `cert/native_variants_test.go`. SHA-256 binds the supplied filename/data pair (integrity, not authorization). A positive source-grammar receipt has grade **`STRUCTURE_ONLY_UNVERIFIED_SCOPE_AND_GRANTS`**. Missing claimed grants or unsupported syntax are `ErrHold` rather than pretend proof of globally safe repair.

Four separately compiled Go source configurations: A/B = a0/b0, new/b0, a0/new, new/new. Their existing `Legacy()=="old"` client assertion must survive, as must the other unchanged literal port. An external verifier needs to authenticate actual source inventory and permission grants before any source-ownership promotion.

GitHub Actions `P44 F28 Closed Go Source Grammar`: `go test -count=1 -v ./...`, `go vet ./...`, `go test -race -count=1 ./...`, using Go1.23.2, strict pipefail. First completed workflow ID **42179185906 SUCCESS** was independently inspected including raw job logs; later code edits require a new CI check, not reuse of the earlier PASS.

## Proof boundary and fair rival

[Bounded theorem, receipts, actual semantic assumptions and limitations](../67_F28_GO_AST_CLOSED_SOURCE_FRAGMENT_THEOREM_AND_RECEIPT.md). Any standard Go AST/compiler slicing analysis given the same closed world can derive literal independence; a strong comparative win is NOT shown. For a larger source language the rival must get the SAME source snapshot, rights and trace obligations and must include aliases/interfaces/dynamic dispatch and build tags. `go/types` and SSA and source-aware analysis are strong classical alternatives. The AST-only grammar check is a positive fragment construction, not a generalized modularity science proof.

**G1–G7 OPEN · LAW-R2 HOLD · PRs Draft**
