# P44-F30 — Fresh-Allocation Frame Lemma, Exact Source-Edit Witnesses and Real Go Alias Falsifier

**2026-11-09; research-grade C3-FRAGMENT only.** Original mathematical ambition: understand conditional SOLID-like consequences from an underlying observer-, rights-, source-, edit-, cost- and demand-indexed repair structure. This experiment is NOT a novel general separation theorem, general Go verifier, or LAW-R2 claim.

## 1. Explicit source universe and actor assumption
Fix Go **1.23.2** and an investigator-defined complete build universe with exactly TWO ordinary regular source files, no build overlays, generators, cgo, assembly, imports or hidden files. File `a.go`: `package fixture`, `type Left struct { Value string }`, pure `Legacy() string` returning one constant literal, and `FutureA() string` with exactly `p := &Left{Value: "<canonical literal>"}; return p.Value`. File `b.go`: `type Right struct { Value string }`, `FutureB() string` with exactly the same local fresh-pointer pattern using Right. Each function is zero-arg, one result, no receivers or type parameters. No globals, calls, channels, other declarations, comments/build directives, extra statements, methods, imports or any pointer escape. Struct field is a scalar string (not a pointer or interface).

A directory inventory and AST parser check this narrow syntax. A SHA-256 digest binds supplied filenames and bytes. Neither this digest nor directory inventory is a signature or authenticated entire-repository closure; file system TOCTOU, underlying Go toolchain/build identity and actual maintained owner authority are separate premises. Positive grade explicitly states `DIRECTORY_AST_FRESH_POINTER_RIGHTS_UNVERIFIED`. Grants `{A:true, B:true}` are **caller assertions**, not independently authenticated rights.

## 2. F30-FRESH-FRAME: bounded Go source theorem

Let `P(a,b)` denote a closed source instance of the grammar in which FutureA is initialized from literal a and FutureB from literal b, and Legacy returns fixed old. Let `e_A(a→a')` change ONLY the AST-positioned canonical literal token in FutureA, preserving every other source byte. Define `e_B(b→b')` symmetrically. Assume the externally declared actor grants and unit token-edit prices actually hold.

**Statement.** For every permitted a,b,a',b':
(1) `Obs(P(a,b)) = (old,a,b)` under the specified three function callers and ordinary Go semantics;
(2) editing A preserves Legacy and FutureB, editing B preserves Legacy and FutureA;
(3) both two-stage edit paths `e_B ∘ e_A` and `e_A ∘ e_B` are authorized under the assumed grants and end with the SAME source bytes/digest;
(4) for two distinct unmet demands `A=a'`, `B=b'`, declared cost `K(P(a,b),[A=a',B=b'])=2` in the exact two-site, one-site-per-step edit grammar. No faster one-step joint edit is admitted by definition.

**Proof.** Every accepted FutureA invocation creates a fresh Go Left value and takes its address, binds it to a local p, then reads its own scalar Value field. Syntactic closure forbids publishing p, using an external reference, calling another function, reading a global or mutating shared memory. FutureB has the symmetric Right-private allocation. The Go observable return triple is therefore the literal triple. An authorized A token rewrite alters only a, leaving b and old unchanged; likewise B. Because these edits target distinct immutable source byte regions and may be applied in either order, they commute and yield byte-identical resulting files. A legal edit changes at most one of the two still-unsatisfied goal literals, giving lower bound 2; two legal edits construct the upper bound 2. QED, under the STRICT completeness/rights/compilation premises.

This is a simple source-reflected instance of classical separation/commuting-square and F27 asynchronous product reasoning. It is **NOT** new priority over O'Hearn/Reynolds separation logic, frame rules, SSA/points-to analyses, or P42 RC1.

## 3. Executable source checks and falsification
Go module `f30_fresh_pointer` contains actual independently compiled fixture source, `cert.CheckDir`, `cert.CheckEdit`, and native Go mutation tests. Local Go1.23.2: `go test -count=1 -v ./...`, `go vet ./...`, `go test -race -count=1 ./...` PASS; extended local code ZIP has 42 test/subtest pass events. Committed GitHub implementation also independently tested: [CI #42555065535](https://github.com/WhoSia/EvoNOMOS/actions/runs/42555065535) completed SUCCESS; raw job log inspected, exactly **30 pass records**, including four independently compiled Go source variants, two-stage commuting edit witnesses, 18 parser negative variations and an actual-Go aliased-global counterexample.

First CI [#42554957109](https://github.com/WhoSia/EvoNOMOS/actions/runs/42554957109) **FAILED to build tests** owing to missing local variable declaration in the newly transplanted Go test only, NOT a failed analyzer assertion. Correcting this led to independent green CI. Preserve failure and corrected result rather than claiming first-pass green.

Adversarial valid-Go program:
```go
var shared = &Left{Value:"a0"}
func Legacy() string {return "old"}
func FutureA() string {return shared.Value}
func FutureB() string {shared.Value="new";return shared.Value}
```
The old Legacy client remains stable; after FutureB, FutureA changes from a0 to new. F30 refuses to certify this source because a package-global shared pointer, source calls/effects and changed grammar violate frame assumptions. This is a **real code execution**, not a proof that every aliased source is unsafe. Safe shared read-only aliases are currently HOLD (conservative false negative).

## 4. Exact source witness vs actual maintainer authority
CheckEdit rechecks before/after directory snapshots; matches one token-level edit and identical opposite file bytes. This verifies a source change inside the declared grammar; it does not attest that an independent repository maintainer authorized it or that a source tree is globally complete. Nor does `go test` establish universal old-client contextual equivalence beyond the grammar. These are open G1–G7 gates.

## 5. Scientific priority and next decisive study
Strong classical matched-input comparator: Go SSA+points-to, dataflow and separation-logic proof framing. The `golang.org/x/tools/go/pointer` package documents classical Andersen-style analysis and important reflection, unsafe.Pointer, native-code and generic limitations; its package is deprecated, so selecting a modern maintained comparator needs further care. Source-aware methods predict both the fresh-allocation safe case and the shared-global counterexample with equal inputs. **No empirical or proof-economy superiority established.**

Candidate next direction: integrate a *non-escaping allocation and points-to certificate* into a source/build-closure receipt and test independently authored maintained source edit histories under the same source/right/observer/cost information as classical rivals. Generic alias-rich Go still OPEN; unseen future demand and rights attestation OPEN; LAW-R2 HOLD.
