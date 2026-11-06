# P44-F19 — closed-world two-file Go source-slice transport theorem and limits

2026-11-05. Mathematical research claim is CONDITIONALLY VALID ONLY under the following closed-world setup. It does not claim a general package-level or repository-level source dependency proof.

## Source model and observer
Let P=(C,A) be a two-file Go package with a trusted fixed build manifest listing exactly `fixture.go` and `aux.go` and an unchanged Go 1.23.2 compiler/build context. C is the F17 typed, comment-free, no-import/no-global exact program grammar with `Cell`, `Clients`, `Build()`, and `Write(c)`. A contains exactly a separate no-argument function `Aux() string` whose body returns one valid string literal. `A` contains no other declarations, package initializer, globals, imports, build directives or comments, and all declared code is jointly accepted by `go/types`.

The PROTECTED old-client observer executes **only** the finite `Build(); Write(c)` client interaction and reads `(c.Legacy.Value,c.Future.Value)`. The observer does not call Aux. Other external clients that DO call Aux will see the returned string change; their contracts are not protected by this lemma.

Let `effect(C)` denote the F17 source-derived alias relationship and two post-write client values. There are no function calls or references to A in the exact grammar of C, while A has no effects and is not used in the Build/Write observer. Therefore for any A and A' satisfying the grammar and typechecking constraints with the SAME C, the restricted client observation is unchanged:

\[
\operatorname{Obs}_{BW}(C,A)=\operatorname{Obs}_{BW}(C,A').
\]

The formal result follows from the closed syntax/semantics; it is a textbook noninterference/frame property, not a newly discovered P44 structural law.

## Implementation and trust
- `IssueSlice(P)` calls the original F17 full typed `Analyze(C)`, verifies the complete two-file grammar and package typechecking and stores H(Go tokens(C)), alias/effect facts and a fixed scope identifier. The certificate receipt hash MUST be externally pinned by a trusted authority; `SliceReceipt` is not a cryptographic signature.
- `VerifySlice(P',certificate,trustedReceipt)` authenticates the supplied certificate against the externally *assumed* pinned receipt, revalidates the entire current two-file grammar and `go/types`, and checks the core token digest. If C's token stream is unchanged while A changes, the old effect facts are REUSED. If core tokens change, it is INVALIDATED, even for a harmless core rename. Unsupported code and tampering return UNKNOWN/error.
- `ClassicalDependencyCache` receives the SAME source, same manifest assumption and same source grammar/verification; it does the same precise token identity test without certificate receipt overhead. `ClassicalFullSliceReanalysis` typechecks both and re-extracts effects.

## Adversarial tests and exact limitations
Positive fixtures: change Aux return literals while protected Build/Write results remain. Negative fixtures: alias change in C must invalidate; A's new package global/init, indirect Build call, cross-file mutation, imported unsafe, build directive, hidden function, comments, ill-typed source must reject. Forged certificate against unchanged trusted receipt must reject. Native Go compiles and runs both files for shared/detached pointer and before/after Aux states. Every provided file is **researcher-selected** and cannot count as independent repository maintenance holdout.

CRITICAL ASSUMPTIONS:
1. No files beyond the explicitly supplied two `SourcePair` strings are included in the actual build. The API cannot independently inspect the user's full repository, build tags, generated files, dependencies or authenticated actor rights. This is a conditional manifest contract, not end-to-end artifact provenance.
2. The trusted receipt is externally pinned; the implementation does not fetch/verify a signed original source manifest.
3. The verifier STILL rechecks the entire two-file AST/typechecking to rule out new interactions, so a speedup is not guaranteed and a conventional exact dependency cache is expected to match or beat it.
4. The old-client observable boundary specifically excludes Aux. For whole-package contextual equivalence including calls to Aux, the two programs are NOT equivalent.
5. One module and one tiny source grammar, deterministic no-concurrency interaction; nothing about Go runtime scheduler, IO, middleware, dynamic linking, reflection, general module dependencies or human editing effort follows.

## Scientific value and skepticism
This is the first P44 source certificate test that actually transports across a **changed Go source file** while retaining a proved customer-independent core. However the noninterference premise is encoded in an exceptionally narrow grammar, and the same proof/behavior is elementary to conventional modular verification. It advances the experimental method one step but has NO demonstrated theoretical novelty, generality or engineering advantage.

Do not mark final original CI PASS or cite benchmark ratios until independently inspected at exact source SHA. Earlier initial F19 native fixture test CI failed due to a string-literal oracle quoting defect; preserve it and the separate corrected CI.

Next BFS must ask whether source-derived dependency frontiers can handle realistic callbacks, aliasing and dependency additions with meaningful incremental advantage over ADAPTON-style dependency graphs and bi-abduction. Keep G1–G7 OPEN, LAW-R2 HOLD.
