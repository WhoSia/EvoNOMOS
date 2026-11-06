# F29 paper-positioning note — The source/abstract bridge, not another SOLID slogan

## Working title
**Certifying When Modular Repairs Commute: A Source-Aware Semantics for Rights-Constrained Evolution**

## Working abstract (NOT ready for external scientific submission)
SOLID principles articulate useful design preferences but do not determine source-edit permission, implementation effects or future repair paths. Prior EvoNOMOS results formalized an exact cost-labelled repair congruence (P42 RC1) and a conditional sequential product cost decomposition (F27); both depend on classical bisimulation and asynchronous-product theory. We bridge the latter premise to a real, strictly limited Go source fragment. Our checker inventories exactly two regular source files, parses their AST, verifies each component returns a field of a freshly built **value** struct with no imports, globals, calls or aliases, and binds the supplied bytes to SHA-256. A separate edit-witness checker validates exact replacement of one AST-located literal token while preserving every other source byte. Four native Go source states and both two-step edit orders yield the same final source digest, while a valid Go cross-component call passes a legacy-client regression yet is rejected as non-independent. Go1.23.2 tests, `go vet` and race instrumentation pass in an independent research-branch CI. **The checker does not authenticate user-supplied editor grants, global repository/build closure, future independent customer demands, or any empirical advantage over a standard source-aware dataflow checker.** Its current contribution is a reproducible conditional source-framing experiment, not a new mathematics theorem or publishable general SOLID law.

## Publication staging and honest scorecard
- C1 Existing P42 weighted repair bisimulation and conditional SOLID operational readings: **PRIOR**; not freshly discovered.
- C2 F27 finite complete product decomposition with interaction countermodels: **CONDITIONAL PASS**, classical theory.
- C3 F28 literal-only original-Go syntactic certificate: **PASS in restricted fragment**, CI independently logged.
- C4 F29 two-file inventoried value-struct certificate and *actual byte-precise source edit witnesses*: **PASS in restricted fragment**, native CI independently logged.
- C5 Signed original maintainer authority, complete source/build closure, alias/heap/effect and dynamic-dispatch coverage: **OPEN**.
- C6 Independent future issue source-edit outcome, non-leaking prediction and equal-information classical rivals: **OPEN**.
- New mathematical priority or law: **NOT ESTABLISHED**, LAW-R2 HOLD.

## Strongest next decisive falsification
Freeze the same old-client contract and update set, expand source just enough to permit a shared pointer, and compare source-aware classic Go compiler SSA/callgraph/alias analysis with our certificate. Require source ownership and build closure from an independently authenticated repository snapshot. A test showing that *both* approaches correctly reject/hold alias effects does NOT demonstrate a new method; measure genuine precision, error, run cost, and coverage on independently authored source edits. Stop claiming novelty if equal input gives classical tie.

## Concrete research output
The falsifier already exists: cross-port call `FutureA() { return FutureB() }` compiles as Go and maintains `Legacy()=="old"` but FutureA changes as B's literal changes. This refutes inferring long-run modularity from old-client pass. But modern static dependency analysis trivially recognizes it, so no priority claim is available.

**Research branch draft only, no publication/merge authorization requested.**
