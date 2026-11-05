# P44 F14 — actual parsed and compiled Go source fragment CI verdict

Verified 2026-11-05. **REAL GENERATED GO SOURCE COMPILED AND EXECUTED IN A CLOSED FRAGMENT. No whole-Go completeness.**

## Original CI history preserved

1. [Initial AST enumerator success #41958998992](https://github.com/WhoSia/EvoNOMOS/actions/runs/41958998992), commit 550b70f1d93663eabb4ca5152a5265f113860bb3. The first grammar still allowed comments because Go parsing discarded them by default.
2. [Post-comment exclusion success #41959415018](https://github.com/WhoSia/EvoNOMOS/actions/runs/41959415018), tested commit e27bedbd16e7b5d0bfda01f0e58197e56a4dbd3f. Added strict rejection of all comments including //go:build and //go:linkname; six tests/vet/race pass.
3. [Expanded native-compiler test FAILED #41959681148](https://github.com/WhoSia/EvoNOMOS/actions/runs/41959681148), commit 35fc844f11fbfe4b249fbcbcab025b44a7725078. Source fixture test code had incorrectly escaped generated Go string syntax, yielding compiler parser error: source_test.go:84:44 expected ';', found testing. This is a real failure and is preserved as provenance.
4. [Corrected original Go compiler/runtime SUCCESS #41959756544](https://github.com/WhoSia/EvoNOMOS/actions/runs/41959756544), tested commit fb3d01cdf570ff1a19f20de2fe9c9d658a605b48, job 127023060194; original raw job log inspected, Go go1.23.2 linux/amd64, seven test groups, vet and race PASS. Every one of three generated source files was compiled and executed with native Go test runner: Future literal off, on, beta all PASS; Legacy still returned stable. CI logs:
- SOURCE_DSL complete_declared_edits=6 legacy_invariant=true exact_classical_cost=1;
- SOURCE_GRAMMAR_COMMENTS excluded_build_and_link_directives=true;
- NATIVE_GO_FRAGMENT_COMPILE_RUN literal=off/on/beta result=PASS.

## Precise mathematical claim

The standard Go AST parser and formatter on one comment-free file, exactly two zero-argument constant-string functions with no imports, allow enumerating an exactly defined single-edit literal-replacement grammar on predeclared finite set D. Three output literals yield 3 states, 6 nonidentity authorized source-edit pairs and a preserved old-client Legacy function; actual separately compiled/ran generated files agree with the AST semantics for the sampled 3-element D.

**Mathematical scope:** enumeration completeness is relative to the DEFINED finite edit grammar; it does not prove completeness for all source edits in general Go. The paired native execution supports the interpretation for three actual programs; it is not a machine-checked formal proof of compiler correctness for all Go source. A complete source editing proof still needs an independently validated chosen grammar, sound compilation/context semantics, correct environment and rights model.

The exact classical shortest-path baseline finds cost 1 to change Future from off to beta and is trivially optimal for this grammar. No compression, speed or new law claimed.

## Source files

- [Closed grammar and generator](sourcecourt/source.go)
- [Go native test and negative cases](sourcecourt/source_test.go)
- [F14 mathematical theorem and limits](29_CLOSED_GO_SOURCE_GRAMMAR_FORMAL_THEOREM_20261105.md)
- [White 2014 classical multi-step CSP original reading](30_WHITE2014_EXACT_COMPETITOR_AND_AUTHORITY_CORRECTION_20261105.md)

G1–G7 general source claims OPEN, LAW-R2 HOLD. Keep PR #13 draft, no merge.
