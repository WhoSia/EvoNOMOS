# P44 F14 — closed Go source sublanguage, complete declared edits and bounded observer semantics

Date 2026-11-05. Source-court research unit. **This is a delimited syntactic/semantic validation, not whole-Go source completeness or new software law.**

## Source grammar and policy
Consider source text accepted by standard Go parser with these exact AST restrictions:
1. `package fixture`; exactly two top-level declarations, each a `*ast.FuncDecl`, named exactly `Legacy` and `Future`, once each; no imports, variables or other declarations.
2. Both are parameterless (no receiver), one result type `string`, and body contains exactly one Go `return` statement whose sole expression is a valid string `token.STRING` literal. No type parameters, operations, control flow, calls, reflection or goroutines.
3. Closed, distinct finite literal domain D is predeclared; the current `Future` literal must belong to D. Current `Legacy` string is arbitrary but protected by client contract.

The actor's ONLY source-edit permission is to replace the constant literal of `Future` with any element of D. This restriction excludes every other Go source transformation by explicit scope, not by wishful inference. Each nonidentity legal replacement has synthetic cost exactly 1; no-decision cost 0.

## Bounded Go AST semantics
For this pure no-input two-constant-function fragment, define joint client observation of a release as the pair (value of Legacy(), value of Future()). A source-level interpreter based on `go/parser` and `strconv.Unquote` extracts these values directly from the only return literals. This is the declared fragment semantics; Go's ordinary function-return semantics agrees here, provided its standard string literal semantics and parser are trusted. The test does not dynamically execute all generated programs or establish an arbitrary Go contextual equivalence.

Let D contain m distinct strings and let initial legacy output be ℓ. The `m` admissible source states are `(ℓ,d)` for each d∈D. Between every two different literals a,b∈D there is exactly one defined authorized edit `ReplaceFutureLiteral(b)` at cost 1, giving m(m−1) directed labeled edges.

**Theorem (relative policy completeness, classical combinatorics).** Under the closed syntax, fixed D, and the defined edit policy, `Enumerate` includes every authorized concrete source edit between program states. Proof: every permissible edit is, by policy definition, a replacement of `Future` to some b∈D. Enumerate iterates every source a∈D and every destination b∈D with a≠b; the generator applies the mutation to an AST, formats it and reparses a source obeying the closed grammar. No other edit constructors are permitted. The legitimate no-edit path is represented by state identity/cost 0 rather than an explicit graph edge.

**Observer preservation.** All produced programs have the same parsed `Legacy` literal ℓ. Therefore old client contract `Legacy() == ℓ` holds at every state, relative to this no-input, no-IO finite semantics. Neither aliasing nor concurrency exists in this language fragment.

**Minimum edit count.** For target d in D, 0 if initial `Future=d`; otherwise 1. Exact classical graph search obtains the same optimum: record a **classical TIE** rather than new EAC accuracy or efficiency.

## Critical limits
- This grammar is far too weak for realistic maintainability; proving its closure does not establish completeness for arbitrary Go edits, middleware, aliasing or concurrent client observations.
- Source formatting may rearrange whitespace/comments; source identity equality is modulo parsed AST semantics and permitted edit meaning, not byte equality.
- The bounded observer includes only two function return values, not timing, network wire semantics, memory or execution scheduling.
- The policy is an artificially specified finite permission grammar; real organizational modification authority and human effort costs are not inferred.
- The exact classical algorithm is a sufficient competitor; no proven certificate compression, causal novelty or structural-law advancement yet.
- F10/F11 nonanticipating future demand game is orthogonal: this fixed demand is fully known and two-function source has no real commitment choices.
- New source program fragments could be introduced only with explicit expanded grammar and new proof obligations; do not silently extend the theorem.

Implementation: [sourcecourt/source.go](sourcecourt/source.go), [sourcecourt/source_test.go](sourcecourt/source_test.go). CI verdict only after original GitHub run readback.

## 2026-11-05 adversarial source-semantics correction

The first AST grammar sketch did not explicitly prohibit comments or Go build directives. This is unsafe: a text file with a syntactically identical pair of constant-return functions may contain a build directive or other compiler-significant comment that changes whether or how it participates in a build, invalidating simple AST-body-based runtime claims. The actual Parse function was tightened to use parser.ParseComments and REJECT any comment groups. This deliberately excludes also harmless comments (sound but restrictive) and Go //go:build, //go:linkname directives. A named negative test checks this restriction. The theorem now applies to a **comment-free, single-file, fixed build context** only. The post-correction GitHub CI result must be checked separately before claiming final pass; the earlier pass predates this fix.

## Original Go native execution now verified — 2026-11-05

[GitHub Actions #41959756544 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41959756544) on exact tested commit fb3d01cdf570ff1a19f20de2fe9c9d658a605b48, raw job log inspected: Go 1.23.2 Linux amd64, seven tests + vet + race PASS. The enumerator's three generated source variants (Future=off,on,beta) were separately compiled and executed using real Go test subprocesses, and Legacy=stable protected behavior remained unchanged. Three source states, six admissible nonidentity literal edit edges, classical exact cost 1, no compression. The earlier native-compiler test run [#41959681148](https://github.com/WhoSia/EvoNOMOS/actions/runs/41959681148) FAILED due to incorrectly escaped generated Go fixture test source; corrected separately and historical failure retained. [Full source/CI provenance and limits](32_CLOSED_SOURCE_NATIVE_CI_VERDICT_20261105.md).

These results demonstrate a **source-parsed and executable** narrowly closed fragment. They still do not prove general Go source soundness or user-maintained source edit authority. Comment/build directives were removed from the accepted grammar to prevent source-behavior escape routes.
