# EvoNOMOS Generation VIII LAW-R1-P42-P2-R7 — Demand-Indexed Typed Obligation Hypergraphs & Repair-Policy Duality: Original Interface Revisions, Minimal Hitting Sets, Consumer-Specific Compatibility and Classical Adequacy

**2026-10-12 KST · R7 opening bounded structural court · R6 real native compiler SUCCESS inherited, R7 finite classical transversal enumeration SUCCESS · P42 RUNNING · LAW-R2 NOT_AUTHORIZED.**

## Core TCS question: what is the invariant, rather than another SOLID axiom?

R6 showed real 2024 historical interface transitions in the independent original go-chi/chi and grpc/grpc-go repositories, with all seven client tests compiling/rejecting in the predicted PRE/POST pattern (14/14 original Go), and a source-aware classical Go structural type model explaining the same 14/14. R7 deliberately **does not repeat the already defeated claim** that raw interface size predicts compatibility. Instead it asks:

> Fix a concrete source revision, an actual client-demand set, a typed requirement set and an explicitly constrained set of permissible source edits. Which *inclusion-minimal* repair combinations restore structural conformance, and how does a change of permitted edit grammar change the minimum?

### 1. Real underlying historical source

- [go-chi/chi PR #926](https://github.com/go-chi/chi/pull/926): PRE `7957c0d4ddaee560a01110145dbf2809ffdb6663`, POST `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`; required `Discard()` added to existing `middleware.WrapResponseWriter`. Native old implementation PRE compiled, POST rejected, additional stub method restored structural compilation but **does not prove correct discard behavior**.
- [grpc/grpc-go PR #7356](https://github.com/grpc/grpc-go/pull/7356): PRE `7e12068baffd8e6328e99d901409cd49d0edebf6`, POST `9ab8b62505c85a5e03be1ae97949e960e24b6d4f`; `mem.BufferPool.Get(int) []byte` and `Put([]byte)` replaced by `Get(int) *[]byte` and `Put(*[]byte)`, keeping two **method names but not signatures**. `encoding.Codec` survives unchanged while new `CodecV2` is added in parallel.
- [R6 original-Go compiler 14/14 #38209926838 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38209926838), artifact `11729171932`, source-aware classical method-set comparator also 14/14.
- [R6 independent unmodified Heroku consumer test #38210450426 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38210450426) for postdated Heroku source against both historical chi versions.

**Critical temporal correction reinforced in R7:** GitHub commit metadata for the tested Heroku snapshot `59fc5216e297df6368fbf4e214bc91c7bb64a8ed` reports **2026-08-18T17:31:48Z**, and Cortex `1c18027a4e3ca8aea1a8ffbf2570184db1d4e30d` reports **2026-10-12T00:54:38Z**. These snapshots postdate the 2024 library revisions. External consumer tests are **cross-temporal controlled observations**, not a demonstration that those exact clients existed at the 2024 merge time.

### 2. Formal repair geometry

For changed typed requirements (U) (each atom a *full Go method signature*, not merely a method name), allowed repair atoms (E), and a finite coverage relation (A:E\to 2^U), a candidate repair set (X\subseteq E) is structurally adequate in this model iff:

\[
U \subseteq \bigcup_{e\in X} A(e).
\]

A *minimal* repair is an adequate (X) with no strict adequate subset. This is classical hypergraph transversal / set cover with a finite designated grammar. The minimum number of selected edits is (min\{|X|:X\subseteq E, X\text{ adequate}\}). Neither source legality nor semantic runtime correctness is implied.

Three R6-grounded models are preregistered in [the R7 typed-obligation source manifest](../../tools/p42/p2-r7/frozen_typed_obligation_cutsets.json):

1. **chi incumbent interface addition:** one unmet method obligation `Discard()`. One method addition, provider substitution or adapter atom can cover it. Under the *restricted* edit grammar in which only `addDiscardMethod` is allowed, the minimum is one. A no-op `Discard()` makes the provider type-conforming but can violate its intended behavior; this separates type conformance from contextual refinement.
2. **grpc changed pool signatures:** two exact unmet obligations `Get(int) *[]byte` and `Put(*[]byte)`. Under the *restricted* declaration-edit grammar, each changed signature is a separate edit atom, giving lower bound and witness of two. An allowed whole-provider adapter or replacement covers both in the **abstract grammar**, reducing the minimum to one. **Those alternative full-provider edits have not yet been compiled against original Go, so this is a declared possibility not a source-realized one-edit repair.**
3. **grpc old Codec consumer:** zero new obligations, hence empty repair set is the unique minimum. This matches actual Go compiler compatibility for the unchanged old interface. Newly introduced opt-in `CodecV2` is a distinct client demand rather than a mandatory burden imposed on all old codecs.

In particular,
\[
\operatorname{MinRepair}(P,I; E_{\mathrm{decl}})
\neq
\operatorname{MinRepair}(P,I; E_{\mathrm{adapter}})
\]
can hold **within the declared finite repair language**. It is wrong to claim a global lower bound on all Go patches without first fixing the set of admissible transformations and semantic obligations.

### 3. Independent finite enumeration and evidence scope

[GitHub Actions R7 #38212449491 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38212449491), exact audited HEAD `aa51d4275fd456827e4e72847f11dd4060577b3a`, artifact `11729516677` SHA-256 `6f78e37cfba50a36e301389276a396d06a6b80864b48172f28710d3e8843fdd1`.

[Auditor](../../tools/p42/p2-r7/audit_transversals.py) exhaustively enumerates all subsets of the declared edit atoms, tests complete obligation coverage, prunes every non-inclusion-minimal candidate, tests deletion of each member of each minimal repair and verifies expected grammatically restricted minima:

| Case | Inclusion-minimal repair sets in declared universe | Restricted grammar minimum | Globally minimal *declared atom count* |
| --- | --- | --- | --- |
| chi added method | `{addDiscardMethod}`, `{adapterImplementor}`, `{replaceProvider}` | 1 | 1 |
| grpc pool | `{editGetSignature,editPutSignature}`, `{wholeProviderAdapter}`, `{replacePoolProvider}` | 2 | 1 |
| grpc old Codec | empty set | 0 | 0 |

This verifier independently validates the finite **combinatorial statements**, **not** native feasibility, source patch count, time cost or semantic correctness. R6 Go CI, which is separate, remains the original source evidence for the interface compatibility mechanism. The classical Go method-set model and classical hitting set theory explain all current results; no novel TCS advantage claimed.

### 4. Structural fault-domain rather than arbitrary OO axiomatization

The more promising EvoNOMOS direction is to work with a source-constrained **fault domain** (ℱ) whose candidate repair operators are backed by source-realized patches. Four distinctions matter:

- **Demand projection:** only clients actually demanding an interface or a feature incur its obligations. A factory-based consumer such as the tested Heroku middleware can remain compatible even while researcher-authored *implementors* of the old interface fail. Thus compatibility is consumer-indexed, not merely interface-version-indexed.
- **Exact typed requirements:** two interfaces with the same number of method names can have incomparable conformance sets if the complete signatures differ.
- **Edit-grammar dependence:** source-repair minima are conditional on allowed edit sites, atomicity and whether adapters/provider substitutions are admitted.
- **Operational meaning:** compilability alone does not certify the behavior of `Discard`, ownership semantics of pointer buffers, codec lifetime or actual old-client outcomes. Source-realized semantic repair needs explicit tests separate from the Go type checker.

For a genuine additional structural discovery, preregister a fault domain built of multiple **actual source-checkable alternative repairs** and a client/observer family (Q), then compute a minimum distinguishing (Q'\subseteq Q) relative to that domain using exact program observations. Compare with the strongest classical methods: method-set constraint solving, hypergraph transversals, contextual refinement and characterization sets under the same known source budget. If these classical algorithms are sufficient, that is a legitimate negative novelty conclusion and a useful architecture analysis method.

### 5. Open gates

1. **R7-P2 source realizability:** write and compile original pinned Go adapters/provider replacements (not stubs alone), and classify structural compatibility separately from `Discard`/pointer pool runtime semantics. Recompute any minimum only after explicitly verifying what counts as an edit atom.
2. **Historical consumer cohort:** locate read-only 2024 effective historical client commits, inspect and compile their actual interfaces where available. Do not label 2026 snapshots contemporaneous.
3. **Independent consumer demand:** construct source-aware dependency/consumer graph and verify graph edges against real imported interface types and original method calls—not only authored toy callers.
4. **Fault-domain minimal distinguishing suite:** use multiple original source-checkable repair variants and independently preregistered old/new client tests. Finite minimality must have an explicit fault domain and cost model.
5. **Formal strength:** if appropriate, verify source-to-finite-interface abstraction and constrained repair minimality in Lean, but require a real source-to-model bridge before inferring global Go results.

**R7 current verdict: finite classical typed-obligation repair geometry VERIFIED; real R6 cross-ecology interface behavior retained; abstract adapter feasibility, historic contemporaneous external consumers and source-to-model completeness OPEN. P42 RUNNING; LAW-R2 NOT_AUTHORIZED.**
