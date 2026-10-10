# P40-MATH-B-P3 — Cross-Ecology Native Source Admission, Semantic Axiom Irredundancy and Method-Partition Falsification

**EvoNOMOS Generation VIII LAW-R1-P40 · 2026-10-10 KST · TWO ORIGINAL UNMODIFIED MAINTAINED ROUTERS · SCOPE-BOUND CONDITIONAL THEORY + ORIGINAL SOURCE TESTS · P40 OPEN · NEW GENERAL LAW HOLD · LAW-R2 NOT_AUTHORIZED.**

## 0. Evidence boundary and fixed original source receipts

Predecessor: [P40-MATH-B](P40_MATH_B_GUARDED_OBJECT_REPAIR_AXIOMS_AND_MINIMAL_FUTURE_BOUNDARY_THEOREMS.md), [P40-MATH-B-P2](P40_MATH_B_P2_AXIOM_INDEPENDENCE_AND_ORIGINAL_CHI_SOURCE_GLUING_COURT.md). Do not mistake this P3 subdocument for P41 or LAW-R2.

**Original maintained ecosystem χ (chi):** [go-chi/chi](https://github.com/go-chi/chi/tree/167e1e3bd039d060696b99c8da4e876ae04f42c1) exact pinned commit \`167e1e3bd039d060696b99c8da4e876ae04f42c1\`, unchanged source, Go 1.24, source-boundary integration [test file](../../tools/p40-p4/original_chi_math_b_boundary_test.go) + [read-only CI workflow](../../.github/workflows/g8-p40-p4-original-chi.yml). P2 independently verified that two individually accepted regex routes having disjoint HTTP-match languages cannot be simultaneously mounted, regardless of mount order. A new P3 test tests a **method-partition intervention** on the same regex route resources. The new χ matched method-partition intervention **PASSED** in [pinned original χ Actions #38047743739](https://github.com/WhoSia/EvoNOMOS/actions/runs/38047743739), test+workflow HEAD `e970b6b335eb2b39e9751b2b8f09aa93ce6e2a4c`, artifact `11668107247` SHA-256 `4559c145602a8e907ea443f0241729d2efb3341f9d11a2cf12e86898d4a0058b`; as predicted, child HTTP method partition does **NOT** bypass shared parent `Mount` reservations.

**Independent second publicly distributed source ecosystem H (httprouter; not verified as actively maintained in 2026):** [julienschmidt/httprouter](https://github.com/julienschmidt/httprouter/tree/484018016424d215c0b87c42f4c9b57d980fbd00) pinned commit \`484018016424d215c0b87c42f4c9b57d980fbd00\`, unchanged source; original \`go.mod\` declares \`go 1.7\` and was tested using a separate Go 1.24 integration harness without editing the original. [P3 original-Go test source](../../tools/p40-math-b-p3/original_httprouter_gluing_test.go) · [CI workflow](../../.github/workflows/g8-p40-math-b-p3-httprouter.yml) · [hosted Actions #38047621733 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38047621733), tested harness HEAD \`69897b31d9c8cb9190ef81fff625f23a9a4ef43e\`; artifact \`11667837335\` SHA-256 \`9eb0a181792c2e603925387ae936f7747a7f770ff25446bb251a35e90ffd8c4c\`. The checked independent job confirms exact original commit and all three source tests.

The pinned httprouter master HEAD is dated 2024-01-30. Do **NOT** label it actively maintained in 2026 solely because its repository exists; the independently released source and native Go executable counterexample remain valid.

No original upstream repo changed; hypothetical future maintainer rights and release contracts are NOT observed third-party permission evidence.

## 1. Direct source facts that preclude a universal router admission axiom

### χ / go-chi/chi
Original \`Mux.Mount\` calls \`tree.findPattern(pattern+"*")\` and \`tree.findPattern(pattern+"/*")\` to reject an existing structural route claim. It also checks \`subr.tree == mx.tree\` to reject self-mount aliasing. Internally mounting installs broad route nodes with \`mALL\` (plus optional \`mSTUB\`). Therefore even a child containing only \`POST\` endpoint methods is not guaranteed a separate **parent mount namespace reservation** from a child containing only \`GET\` methods. Original \`Mux.Use\` separately guards middleware registration after routes.

### H / julienschmidt/httprouter
Original \`Router.Handle\` indexes its radix roots by \`root := r.trees[method]\` and calls \`root.addRoute(path,handle)\`. Original \`tree.go\` detects wildChild/static collision on a single method-specific tree; when the path cannot reconcile the existing wildcard node and new static subpath it raises a source-level conflict panic.

These source facts motivate **different admissibility contracts**:
\[
A_\chi(\mathrm{parent\;mount\;tree},\;\mathrm{pattern},\;\mathrm{alias},\;\mathrm{stage})\quad\text{vs.}\quad
A_H(\mathrm{HTTP\;method\;tree},\;\mathrm{radix\;node\;shape},\;\mathrm{pattern}).
\]
Neither expression is proposed as an exhaustive formal characterization of all routes in the two libraries.

## 2. Second natural source counterexample with a controlled positive intervention

Fix original H route obligations:
- Local edit A: \`GET /service/:name/a\`, responds "A".
- Local edit B: \`GET /service/static/b\`, responds "B".

Their **HTTP request languages are disjoint** because the last path segment must differ: \`/a\` versus \`/b\`, regardless of wildcard value. Both separately preserve the old \`GET /old\` client and satisfy their own new request client. Yet on the same parent router, adding B after A OR A after B fails with the source wildcard conflict. This is not a fake abstract example: it is the original pinned maintained H implementation.

**Same-source-grammar positive control:** change *only B's method* from GET to POST, keeping its path and response. H now stores the route in a distinct method-indexed tree. With A-then-B and B-then-A, BOTH source edits register and the old client and both new clients pass. Separately, replacing the two patterns with flat distinct literal branches lets both same-method registrations pass in either order. Hence failure is not caused by an inherently invalid handler, generic Go compiler failure, or an immutable old client.

| H test | Local A | Local B | Two-edit combination |
| --- | --- | --- | --- |
| Structural wildcard/static same-method | GET /service/:name/a | GET /service/static/b | FAIL in both insertion orders |
| Method-partition intervention | GET /service/:name/a | POST /service/static/b | PASS in both orders |
| Literal/static control | GET /service/alice/a | GET /service/bob/b | PASS in both orders |

Verified at hosted [#38047621733](https://github.com/WhoSia/EvoNOMOS/actions/runs/38047621733), pinned H original source and three independent Go tests.

**Comparative χ negative control:** chi has an independent test replacing the second mounted child's new /item handler with POST rather than GET but keeping the same regex mount paths. Because the parent \`Mount\` reservation is not partitioned by child HTTP method, the predicted result is STILL failure in both orders. **Report this chi-specific matched intervention as PASS only after its independent workflow finishes.**

This is a conditional ***implementation-ecology-dependent reversal***, NOT a new universal law nor an apples-to-apples comparison of identical syntax: the H operation is \`Router.Handle\` and the χ operation is \`Mux.Mount\`. Their different source abstraction levels are the very explanatory variable.


## 2A. Actively updated contemporary alternative Echo — a stronger prospective counterecology

Independent [labstack/echo](https://github.com/labstack/echo) v5 main SHA \`3882266a3641a36fc2111b48cd597adab1c1ecea\` has a recent 2026-10-07 commit (unlike httprouter's 2024 last master update). Its original \`router.go\` uses \`DefaultRouter.insert\`, maintains separate static, parameter and any-route children and stores per-method handlers in one routing-node structure. Crucially it does **not** use httprouter's same single-method radix wildcard/static conflict rule. This supports the distinct **predicted** outcome for A=GET /service/:name/a and B=GET /service/static/b: both should register and both HTTP clients should work.

[Separate Echo source integration test](../../tools/p40-math-b-p3-echo/original_echo_gluing_test.go) · [read-only pinned-source Actions](https://github.com/WhoSia/EvoNOMOS/actions/workflows/g8-p40-math-b-p3-echo.yml). This is an actively updated independently maintained positive control, and validates or refutes whether H's inability to register disjoint static/parameter paths can be generalized to a different modern trie router. **Status must be read back from the exact corrected test run, not inferred from source alone.** The first Echo attempt #38047932553 FAILED test compilation because the harness called a nonexistent Echo.Routes method. The correction removed this unsupported ancillary API call and kept actual HTTP client assertions. This is a test-harness fix, not an upstream source change.


## 3. The logically valid impossibility claim

Fix a bounded class of two-edit programs and a coarse observation \(\sigma\) recording only (i) local acceptance of both edits and (ii) the Boolean fact that their HTTP request-language supports are disjoint. If \(\sigma(x)=\sigma(y)\) but \(\mathrm{SourceAdmit}(x)\neq\mathrm{SourceAdmit}(y)\), NO classifier \(f\) on \(\sigma\) alone decides source acceptance for all worlds.

The H same-method failure and method-partition success provide a concrete pair with identical coarse signature \((1,1,1)\) and different combined source legality. The χ test independently shows the same necessary *type of information*, namely the internal admission regime, but does **not** prove the same method-indexed rule. Exact \(\ker\sigma\not\subseteq\ker\mathrm{SourceAdmit}\) is classical nonfactorization. Neither case shows that a classifier with the *complete HTTP method-labeled route language sets plus the known implementation definition* fails; our proved proxy is deliberately coarser.

**Key distinction:** behavioral input-language disjointness is not the same as the implementation's source-level acceptance relation. A sound inference of source edit gluing must expose the actual admission predicates (or independently proven conservative approximations). This is already predicted by ordinary context-aware source semantics and CSP once constraints are modeled correctly.

## 4. Lean candidate: a conditional method-partition frame, not a source semantics proof

[P40 Lean theorem source](../../tools/p40-math-b/lean/P40MathBIndependence.lean) now contains a \`MethodScopedPair\` signature with local pass values, disjoint-language flag, shared-method-tree flag and wildcard/static collision flag. It defines a **synthetic checked contract**:
\[
\mathrm{Admitted}_{H^*}(x)
=\mathrm{LocalA}(x)\land\mathrm{LocalB}(x)
\land\neg(\mathrm{SameMethodTree}(x)\land\mathrm{StructuralConflict}(x)).
\]

Two witnesses differing only in the \`SameMethodTree\` flag share their coarse extensional observation but differ in source acceptance. A general no-factorization lemma then forbids predicting acceptance solely from the coarse extensional tuple.

A separate theorem, under independently stated local acceptance and \(\neg\mathrm{SameMethodTree}\), proves that the **constructed model** accepts the joint edit regardless of wildcard/static conflict. This corresponds to H's actual per-method source tree separation for the two chosen original-Go cases. It does not prove exact \`httprouter\` source semantics for arbitrary Go programs, and the predicate must not be rebranded as an implementation's formal specification. **Lean 4.34.1 formal PASS verified:** [Actions #38047672819](https://github.com/WhoSia/EvoNOMOS/actions/runs/38047672819), checked Lean source HEAD `fd44044f10858c5070d6038837dc85640926bd9a`, artifact `11668586127` SHA-256 `233bdd3ac09db649760e682c6dfc0bb822e72958171c94b74d9ed28ffc0d85c5`. Independent leanchecker accepted the augmented method-partition lemmas and earlier source-guard/kernel theorems.

### The irredundancy requirement for general OO axioms

P40's semantic domains A (typing), B (behavioral histories), C (rights), D (safe checkpoints), E (boundaries), F (dependency/capability) are NOT yet six independent formal axioms. One cannot prove independence of bare names or labels. For each meaningful proposed axiom \(A_i\), rigor requires:
1. noncircular formal semantics independent of desired SOLID conclusion;
2. a model satisfying all other declared axioms and refuting \(A_i\);
3. an explicit target implication that **fails** with \(A_i\) removed;
4. a real-source test for at least the claims labeled source-realizable, or a clear synthetic-only badge;
5. prior-art matching against compiler guarantees, frame rule, CSP, rely-guarantee and contextual refinement.

A six-bit unconstrained Cartesian product trivially establishes Boolean independence and is not a satisfactory new object-oriented theorem.

## 5. Strongest defeated and surviving theories

**Defeated as sufficient:** HTTP request language disjointness alone, local individual compile/client acceptance alone, flat route-name memory alone and source-state abstractions ignoring dynamic tree identity / stage (see P2). Even independent satisfiability of local route obligations does not imply global admissible composition.

**Not defeated:** accurate implementation-aware CSP, classical assume/guarantee and separation logic frame rules, ownership/alias analysis, route trie compatibility constraints, method-scoped state maps, Liskov–Wing behavioral refinement and Parnas' modularity/uses relation. In fact the successful H method-partition control is exactly an ordinary resource-disjoint frame theorem under a split method-keyed root map.

**Limitations:** two self-contained Go integration ecosystems, selected methods/routes, no human maintainer permissions, no real issue/PR-based prospective demand sampling, and no exact universal router specification.

## 6. Next tests

- Mine actual issue/PR/commit source changes of the pinned libraries **without assuming maintainer rights** and pre-register proposed source contract predictions before reading the test outcomes.
- Seek an independently measured cross-source edit boundary where CSP + frame + contextual refinement cannot predict a specified bounded outcome. If no such evidence is found, record the classical collapse rather than asserting new law.
- Ask Lean to check a truly conditional, scope-limited **compositional proof** whose premises can be separately established from native source, not a definition equating admissibility to a conjunction of the desired guards.
- Only after that attempt a reduction of scoped SRP/OCP/LSP/ISP/DIP to a smaller independent system; original full SOLID derivation remains OPEN.

**Verdict:** second maintained original repository cross-validation SUCCESS; method-key partition is a sufficient repair intervention for the tested H grammar; no cross-router transfer guarantee. Historical SOLID axiomatic derivation remains OPEN. A fundamental nonclassical OO law is NOT identified. P40 OPEN, LAW-R2 NOT_AUTHORIZED.
