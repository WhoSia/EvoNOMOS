# P44-F29 — Closed Go Value-Frame and Exact Source-Edit Commutation Certificate

**2026-11-06, C3-FRAGMENT, not LAW-R2.** This is a conditional source-language result, *not* a new theorem of concurrency, a proof of all Go program behavior, or an attestation of maintainer edit authority.

## 1. Progress over F28
F28 accepted only `return "<literal>"`. F29 accepts a **closed Go value-structure fragment**:
- A `package fixture` directory, statically inventoried as **exactly** two regular, non-symlink source files `a.go` and `b.go`.
- `a.go` has a declaration `type Left struct { Value string }`, `Legacy() string` returning one literal, and `FutureA() string` returning `(Left{Value: "<literal>"}).Value`.
- `b.go` has `type Right struct { Value string }` and `FutureB() string` returning `(Right{Value: "<literal>"}).Value`.
- No imports, comments (including build directives), extra globals/types/functions, receivers, parameters, pointers, interfaces, calls, field tags, arithmetic, or external initialization.
- No hidden build overlays or generated files, no changes to compiler semantics, and a fixed Go1.23.2 compiler are **environment assumptions**, not proven by reading one directory.
- Authority grants `grantA/grantB` are caller-provided claims; receipts always carry `DIRECTORY_AND_AST_CHECKED_RIGHTS_UNVERIFIED`, never an authenticated legal edit certificate.

The directory inventory now closes one important omission in F28's caller-supplied two-byte-array receipt. However, a mutable filesystem check is a time-of-check snapshot, not an authenticated repository tree or atomic build closure. SHA-256 binds names and original file bytes but is not a signature.

## 2. F29-SOURCE-EDIT theorem: exact one-step witnesses under closed grammar

Fix a stable source directory with exactly the two verified Go files, named future ports A and B, and a separate actor-authorization premise. Permitted source edits are specifically and **only** replacement of the string-literal token occurring inside the `Value:` initializer in `FutureA` or `FutureB` with a canonical quoted new string, without changing any other byte. The `CheckLiteralEdit(before,after,port,grants)` code proves that the opposite component file is byte-for-byte identical and that the target file equals the original with exactly one AST-located literal token replacement. In-place whitespace-only edits, combined edits, hidden files and unverified permission produce HOLD, not a repair witness.

Let `P_{u,v}` denote the source program with A value `u` and B value `v`. Under the complete closed fragment, standard Go execution produces `(Legacy, FutureA, FutureB) = ("old",u,v)`. Therefore both local edits preserve the old client and the other future output, and for any new literals `u',v'`:

```
 P(u,v) ---edit A---> P(u',v)
   |                     |
 edit B                edit B
   |                     |
   v                     v
 P(u,v') --edit A---> P(u',v')
```

Both legal paths reach **byte-identical final source** with equal source SHA and cost two in the specified unit-cost edit grammar. Since no legal edit changes both components, two distinct unmet demands require at least two edits, so exact staged minimum repair cost equals 2. This is a classical commuting-square/frame fact with a source witness; it does not prove general optimal maintenance under real authorization, changing requirements or unknown edits.

## 3. Adversarial falsification and classical comparator

A legal Go program with `FutureA(){return FutureB()}` compiles and continues to satisfy `Legacy()=="old"`, but changing only `b.go` from `b0` to `new` changes the A output too. The new checker HOLDS. This is direct concrete proof that **old regression pass does not imply future edit independence**; it does not show a win over source-aware Go static slicing, SSA, `go/types`, or interprocedural call-graph analysis, which can also detect the dependency when supplied identical source and rights.

Additional rejection cases: `*string` pointer field, `interface{}` field, shared global, import, extra method, dynamic constructor, cross-type dependency, added hidden Go file, symlink, package change, change outside the single token, false caller grant, and simultaneous two-port edit. These HOLD cases do not establish that the rejected code is unsafe; they establish that F29 refuses to assert unsupported positive independence.

## 4. Locally and remotely executed evidence

Local Go 1.23.2: `go test -count=1 ./...`, `go vet ./...`, `go test -race -count=1 ./...` all PASS; 18 top-level sourcecert test functions, including grouped 14 mutation cases, 4 native Go source variants, 2 independent cross-call Go builds, 2-stage A→B path and B→A commutation/digest test. The generated Go fixture itself has a separate old+initial-client regression test. Test grouping and individual subtests must be distinguished from an unqualified 'N tests' performance claim.

Original branch GitHub CI [#42228134629](https://github.com/WhoSia/EvoNOMOS/actions/runs/42228134629) **SUCCESS**, workflow job `source-frame` and RAW logs read: `TestFourNativeSourceVariants`, `TestOldClientsPassButCrossComponentEffect`, `TestTwoStagePatchPath`, `TestSourceEditCommutativityWitness`, Go1.23.2 `go vet` and `go test -race` observed. CI validates committed source, not external source rights, source-inventory atomicity, or independent future issue evidence.

## 5. Connection to SOLID beyond slogans

The proof's primitive is *noninterference with source-edit witnesses*, not a class count or the existence of an interface. It has a conditional SRP-like consequence; stable old `Legacy` behavior with extension-only paths illustrates an OCP fragment. LSP demands context-indexed behavioral refinement, ISP requires sound joint observer projection, and DIP requires complete port/effect dependency certification: none of those three follows simply from this two-struct laboratory.

Previous P42 RC1 already formalized weighted rights-aware bisimulation and conditional SOLID fragments, and F27 already proved exact product factorization. F29's real value is bridging one extremely constrained Go source edit to that abstract relation, with unambiguous positive/negative source evidence. The remaining key scientific obstacle is generalizing this to *source-inventoried, actor-authorized*, alias-aware maintained program changes while retaining practical economy over equally informed classical analyzers.

**Verdict:** F29 CLOSED-VALUE-FRAGMENT source-edit witness PASS; G1–G7 open for general maintained Go, no C5 prospective claims, LAW-R2 HOLD; PR #13 DRAFT.
