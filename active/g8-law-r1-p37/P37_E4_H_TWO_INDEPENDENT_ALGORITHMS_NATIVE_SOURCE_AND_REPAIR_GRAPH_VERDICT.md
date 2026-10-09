# P37-E4/H — Native Two Independent Session Algorithms, Source-Derived Capability Graph, and Orthogonal Composition Obstructions

**2026-10-10 KST · POST ORIGINAL-Go RECEIPTS · P37 OPEN · DIP49 IDENTIFICATION_HOLD · LAW-R2 NOT_AUTHORIZED**

## 1. Source/experiment chronology and actual algorithms

The [E4 prospective contract](P37_E4_INDEPENDENT_GORILLA_SCS_CAPABILITY_BRIDGE_PRESEAL.md) was committed before [immutable native test](../../tools/p37-e4/bridge_test.go), before the [project-authored bridge](../../tools/p37-e4/bridge.go), and before GitHub Actions outcome. It compared **genuinely independently developed state representation algorithms**:
- `gorilla/sessions@bb4cd60c952a9ce48ea0dc6cc7b282ff79c38263`, naturally depending on `gorilla/securecookie@eae3c1840ec4adda88a4af683ad0f60bb690e7c2`: original `CookieStore.New/Save` reads/writes signed serialized session data held in a client cookie.
- `alexedwards/scs/v2@209de6e426de9259665975ce16b91331d228f052`: independently evolved original `SessionManager.Load/Commit` and original memory store, session data held **on the server**, client only retains an opaque token.

**Strict ecological qualification:** These two algorithms **do not** originally depend on each other. A dual-reading capability bridge was authored **by EvoNOMOS** for this controlled comparison. The source implementations are independent, not the composite application. The test-only fixed 32-byte Gorilla key and generated SCS token are non-production fixtures; no real personal session, credential, crypto security claim or attack test.

## 2. Original native code execution — verifiable PASS, not just proposed

[Original Go native E4 run #37987574221](https://github.com/WhoSia/EvoNOMOS/actions/runs/37987574221) finished **SUCCESS**. Original source checkouts pinned all three stated commits; `go list -m all` and per-source SHA256 archived. Real Go `go1.23.12 linux/amd64`.
- Research-authored composite `go vet ./...` PASS, `go test -race -count=1 -v ./...` PASS, all three frozen parent tests and all six capability subcases PASS.
- Entire pinned original **SCS** module `go vet ./...` and `go test -race -count=1 ./...` PASS across `scs/v2`, `memstore`, `mockstore` packages. Pinned original Gorilla modules were already full-race/vet verified independently in E1 [#37985028491](https://github.com/WhoSia/EvoNOMOS/actions/runs/37985028491); **E4 did not rerun Gorilla module full tests**. The native E4 program exercised their actual original exposed APIs.
- E4 original artifact **11643901657** downloaded; ZIP SHA256 **`ba1af8a3c54554271cef7e1086e975c707a808ebc6760c00dd6d058d859f8113`**, 8 auditable file logs (source SHA, module receipt, original full SCS Go results, native race, scoped vet, metadata, verdict).

Exact source SHA256 from that original CI checkout:
- Gorilla original store.go `8595a504fa4e07020b23a8e3daa2c75bf6f2a5d5130e6abbc0faaa8ce48c9da3`.
- Securecookie original securecookie.go `543f45dcc1383ca7a08657c7e8b058a14594ebac3d34a5b2c4b22cc069f15e52`.
- SCS original data.go `b88e31e898c973232855991f2a985619d5cf45a2c81992d5da495adc72f90db5` and session.go `f529c14f90eac0112482a49c77f12b14470542133a292dac6726f74039d3c139`.
- Research bridge `2900753f0d2370f8df72c17ce7d18a36cd445047f839e20118ce43796fa55719`, frozen test `75dad435edb78343e5f7b641867b0bb088d266f135c9996edad0aa535b316220`.

## 3. Recovered original-source semantic results (not inference from algorithm names)

The original native source APIs were executed through:
- Gorilla `gsessions.NewCookieStore` → `CookieStore.New/Save` → `securecookie.DecodeMulti/EncodeMulti`, checking `Session.IsNew` and `Values["stage"]`.
- SCS `scs.New` → `SessionManager.Load` → `Put` → `Commit` (new opaque token + server-store state) → `Load(token)` and `GetString` on the **matching existing server store**.
- A new EvoNOMOS reader `Bridge.CanReadStage` uses original public APIs and a declared set of optional `Gorilla` and `Server` handles. It chooses the result only when original decoded legitimate test session contains `stage=kept`.

**All frozen cases native PASSED:**

| Authorized reader capability | Existing G client-state cookie | Existing S server-token state |
|---|---|---|
| Original Gorilla-only reader | PASS | FAIL |
| Original SCS-only reader WITH matching state store | FAIL | PASS |
| Both original API handles | PASS | PASS |
| SCS handle but no G key/reader | FAIL | PASS |
| G reader but no SCS store | PASS | FAIL |
| G reader plus a distinct WRONG SCS store | PASS | FAIL |

Both issuing algorithms satisfy the same *current semantic* session-value observation, but their serialized representations are not interchangeable under a fixed one-source reader context. Scope: **only the declared legitimate test inputs**; the test is not a security or comprehensive session validator.

The actual original Go test also verified safe original G-reader → dual reader → S issuer sequence at each future-demand checkpoint, and unsafe premature S-only contraction before old-cookie obligation expiry. Another test explicitly distinguishes the two representations under an SCS-only future context despite the same current decoded value.

## 4. Source-to-graph evidence, and WHAT graph means

[Source-API probe](../../tools/p37-e4/model/probe_original_source_contract.py) mechanically checks the exact original pinned Go callsites `securecookie.DecodeMulti`, `securecookie.EncodeMulti`, `SessionManager.Load`→`doStoreFind`, `Commit`→`doStoreCommit`, random token generator, and new bridge's **capability-guarded** original API calls. These are real source-level edges, not merely documentation.

[Typed owner/capability repair graph](../../tools/p37-e4/model/capability_repair_graph.py) composes source-based G/S writer modes, G-only/S-only/dual reader modes, G key/decoder vs matching SCS store capabilities and a persisted historical obligation flag:
- without B's dual-reader authorized path, sequential migration to S-only cannot maintain the live + legacy invariant;
- with both original-source capabilities, a **four-transition** path exists: B dual reader expansion → A issuer switch → **explicit external expiration of legacy duty** → B legacy reader contraction;
- withdrawal of either original reader capability prevents the declared successful `Γ` path; this is a **restricted program grammar** obstruction, **not** a claim cryptographic key recovery is mathematically impossible;
- current semantic session-value equality is **not a congruence** for all future authorized reader contexts.

[Source-linked graph CI #37987979480](https://github.com/WhoSia/EvoNOMOS/actions/runs/37987979480) finished **SUCCESS**, original-source callsite checks, finite graph invariants, and explicit [MATH-H orthogonal authority/invariant countermodels](../../tools/p37-e4/model/owner_permission_countermodels.py) PASS. Artifact **11643852205**, ZIP digest `sha256:87b7fcb5652f3ec3409fb5f1c5624450b5e93b3ac7a77f61648c48723cff5a9a`.

The graph is **research-authored from verified APIs and frozen finite semantics**, not fully automatically extracted AST state-space or proof over every legal source patch. A source probe establishes its edge provenance but cannot establish its reachability completeness.

## 5. What actually changed in mathematical understanding

[MATH-G](P37_MATH_G_CAPABILITY_INDEXED_REPAIR_CONGRUENCE_ACROSS_SESSION_ALGORITHMS.md) adds **representation and capability handles** to ownership-typed repair states. [MATH-H](P37_MATH_H_CAPABILITY_BISIMULATION_AND_ORTHOGONAL_COMPOSITION_OBSTRUCTIONS.md) separates two logically independent reasons local repair possibility fails to imply global possibility:
1. **I nonrectangular**, even though global Γ is a complete asynchronous product.
2. **Γ nonproduct/permission-coupled**, even if global I is perfectly rectangular.

A source-level, capability- and owner-labeled **bisimulation** preserving observations, invariant, demand acceptance, and both directions of legal source edits is a classical sufficient condition for the declared finite future May signatures to coincide. The E4 original sources violate the required contextual equivalence under one-source-only reader contexts, but the research dual reader realizes a conditional bridge when authority/capabilities allow.

**Classical rival court:** the strongest actual source-aware baseline `B_*` already knows state representation independence, program slicing, server-side storage, opaque IDs, ownership capabilities, relational product invariants, and staged deployment. It predicted all the E4 outcomes, including negative controls. There is currently NO law-level prospective signature `σ(H)≠σ(B_*)` in this experiment. Therefore E4 is a meaningful **cross-algorithm transport and source-derived structural synthesis**, **not discovery of a novel principle logically stronger than all classical theories or a refutation of SOLID**.

## Next prospective discriminating attack

Move from author's small bridge to **independent historical maintenance episodes with documented real owners and pre-existing evolution**, or build a fresh independent source ecosystem with different state ownership (e.g. event-based vs snapshot backends). Derive allowed edit grammar from real source API/ownership, freeze context and legacy invariant *before candidate patches*. Construct quantitative or logical predicted outcomes from full state-of-the-art classical verification/assume-guarantee rivals, and commit predictions independently before observing repair success. If the strongest classical signature equals ours, register classical transport and retain DIP49 HOLD.

**Final:** `P37_E4_TRUE_INDEPENDENT_ORIGINAL_SESSION_ALGORITHMS_NATIVE_RACE_VET_PASS__FULL_SCS_ORIGINAL_RACE_PASS__SOURCE_DERIVED_CAPABILITY_GRAPH_AND_H_NEGATIVE_MODELS_PASS__BOTH_PREDICTED_BY_STRONG_CLASSICAL_PRIOR__DIP49_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
