# EvoNOMOS Generation VIII LAW-R1-P41 — Minimal Semantic Preconditions for Object-Oriented Evolution: Source–Behavior–Authority Alignment, Counterexample-Guided Axiom Reduction, Conditional SOLID Reconstruction & Classical Adequacy Tests

**Official user-approved stage name · P41-P0: Semantic Signature, Independent Evidence Domains & Falsification Architecture · 2026-10-11 KST · P41 RUNNING · LAW-R1 · LAW-R2 NOT_AUTHORIZED.**

## 0. Research decision: P41 is now STARTED; no new law is asserted

The P40→P41 transfer [canonical handover](../g8-law-r1-p40/P40_TO_P41_FORMAL_HANDOVER_AND_PROPOSED_TITLE.md) is **accepted as the stage title**. The scientific inheritance is only the *source-grounded* and *formally scoped* results from P40 Math-B-P2–P6. Do not confuse an official stage name with authorization to promote a fundamental new OO law or LAW-R2.

**Question:** Under what precisely declared observational, native-source, authority and dependency assumptions does an edit preserve old clients and achieve new goals? Is a minimal noncircular premise system possible? Which carefully scoped versions of SRP/OCP/LSP/ISP/DIP are derivable? Could a classical CSP/constraint-satisfaction, data-refinement, separation-frame or rely-guarantee theory explain every observed claim instead?

**Research modes:** (i) typed semantics, (ii) individually audited source data, (iii) formally checked implications, (iv) real-source and independent countermodel attacks, (v) equal-information classical alternative. Explicitly distinguish these stages.

## 1. Canonical typing of A–F evidence, not axioms assumed true

A candidate is specified by a **source of evidence**, an **observable independent predicate**, and a distinct **sort**. The present typed Lean record is a deliberately free finite example signature; it does not axiomatically force any of these propositions to hold.

| Candidate | Domain and independent predicate | How it is measured | Epistemic status at P41-P0 |
| --- | --- | --- | --- |
| **A — type/compile** | compiler judgement `CompilerAccepts(S,e,env)` | pinned original compiler invocation; source/type flags | Original-Go **NATIVE_BOUNDED** (P40-P6) |
| **B — old clients** | `Obs_Old(S)=Obs_Old(Apply(S,e))`, for explicitly declared observers, full outputs and stateful effects when relevant | HTTP response status, headers, body, chosen traces and handler side-effect count | **NATIVE_BOUNDED** (P40-P5) |
| **C — edit rights** | `Permitted(principal,owner,revision,e)` from legitimate historical governance | authentic audited maintainers, revisioned ACL, approval and rights changes | **SYNTHETIC_ONLY**; *not* inferred from a public repository or code |
| **D — new goal/dispatch** | target route and source-selected handler agree **and** new demand output agrees with actual client outcome | P40 Echo overwrite, wrong-handler independent client cases | **NATIVE_BOUNDED** in chosen cases |
| **E — source admission** | native source parser/tree `Accept(S,e_1;e_2)` | unchanged original chi, httprouter and Echo Go registration cases | **NATIVE_BOUNDED** |
| **F — dependencies** | edit-required provider port/capability satisfied by actual graph | versioned provider metadata, import/port binding and independent external execution | **SYNTHETIC_ONLY** at this P41 evidence gate |

Machine-readable audit: [P41-P0 evidence registry](../../tools/p41/p0_evidence_registry.json); [standalone provenance auditor](../../tools/p41/p0_registry_audit.py). It rejects the silent promotion of C or F from synthetic to original native and requires exact P40 original upstream commits and independently passed CI run identifiers for the four bounded categories.

**Important:** Six free-product fields do **not** constitute a demonstrated foundational independent axiom basis. Any theorem of the form `A∧B∧C∧D∧E∧F → A∧B∧C∧D∧E∧F` is merely logical bookkeeping, not a law of evolvability. A future theorem must connect **independently testable premises** to an *external, nondefinitionally equivalent* semantic target.

## 2. Exact model language and three orthogonal judgements

Let a source- and history-indexed world contain source state `S`, principal `p`, version `v`, client observers `O`, permission history `R_v`, dependency graph `G`, edit `e`, and a concrete transition `Apply(S,e)` whose semantics must be independently established. The three explicitly different outcomes are:

1. **Admissibility** `Admit(S,e)`: the compiler/parser/native source registers the change without rejection; *not* synonymous with correctness.
2. **Contextual behavior** `Preserve(S,e,O)`: for every stated old-client observer, the before/after observation agrees; plus independent new-client demand/route identity `Fulfill(S,e,T)`. Header/hidden side effects/route identity are part of O or T only if declared in advance.
3. **Legitimacy and capability** `Permission(R_v,p,e)` and `PortCompatible(G,e)`: authorization and provider contract, which cannot be recovered from ordinary HTTP traces or the public visibility of source.

The intended target is an **observationally and institutionally bounded** `ValidEvolution(S,e,O,T,R_v,G)`, not a universal notion of good object orientation. Its semantics must be defined using client observations and independent governance records, NOT by relabeling six guard predicates as a new target.

**Old/new clients and version histories are separate indexed sets.** Some clients may not be valid after an explicitly allowed breaking change, so P41 must declare allowed edit classes and exactly which obligations survive, rather than claiming that all possible old behaviors always persist.

## 3. First formal results: proof strength versus source realization

[P41-P0 Lean 4 source](../../tools/p41/lean/P41SemanticP0.lean) defines 12 typed data fields composing a deliberately *unconstrained product* of evidence coordinates: type accept, source-register, before/after old observation, owner/actor, target/resolved route, desired/produced output and requested/provided port.

It establishes:
- an internally consistent six-premise witness;
- six **scoped synthetic omission models**, where each candidate premise is false and the five other candidates hold;
- a **source/behavior projection authority nonfactorization witness**: the same compile/source/client/provider results with a different legitimate owner produce opposite authorization results. Therefore no classifier taking only that reduced projection can decide authorization for all worlds in this product;
- a distinct **response-only route identity nonfactorization witness**: source register and old/new scalar response equivalence do not identify which handler/route was selected;
- provenance tagging (`originalNativeGo`, `originalAST`, `authorityRecord`, `dependencyAudit`, `syntheticCountermodel`) without faking a native receipt.

General mathematical lemma: if `view(x)=view(y)` but `decision(x)≠decision(y)`, then no total `f` satisfies `decision=f∘view` for all states. This is **ordinary classical factorization**, not original new mathematics.

**Strict limitation:** The six omission witnesses are synthetically independent in an unrestricted product signature; no theorem shows all six are mutually independent in an actual OO implementation. In particular, C and F lack independent original-world evidence, and some source/runtime facts can logically couple A to E or D to B. Keep P41's main irredundancy claim OPEN.

## 4. Real source and bounded prior results with provenance

- [P40-P2 original chi syntax namespace and alias/temporal guard](../g8-law-r1-p40/P40_MATH_B_P2_AXIOM_INDEPENDENCE_AND_ORIGINAL_CHI_SOURCE_GLUING_COURT.md): Source-specific Go regression, not a universal OO axiom.
- [P40-P3 three original routers](../g8-law-r1-p40/P40_MATH_B_P3_CROSS_ECOLOGY_SOURCE_ADMISSION_AND_AXIOM_IRREDUNDANCY_COURT.md): Identical named GET pattern obligations can be jointly registered by Echo but rejected by httprouter; classical implementation-specific CSP survives.
- [P40-P4 prospective 16 source admissions](../g8-law-r1-p40/P40_MATH_B_P4_PROSPECTIVE_SOURCE_BOUNDARY_CONTRACTS_AXIOM_IRREDUNDANCY_AND_CLASSICAL_REDUCTION.md): **16/16 source-admission predictions**, but one accepted Echo overwrite breaks an independent new-client promise; only 9 jointly preserve the selected old/new observations.
- [P40-P5 issue-derived Echo/Gin](../g8-law-r1-p40/P40_MATH_B_P5_REAL_MAINTENANCE_ISSUE_DERIVED_SEMANTIC_SIMULATION_AND_CLASSICAL_COURT.md): **6/6 previously locked forecasts + two explicit abstentions**, including Echo v5 wildcard wrong-handler and Gin param-colon grammar rejection; no authority claims.
- [P40-P6 AST HEAD semantics slice](../g8-law-r1-p40/P40_MATH_B_P6_SOURCE_AST_SEMANTIC_BRIDGE_AND_MINIMAL_REPAIR_CERTIFICATES.md): original Echo HEAD switch two statements extracted *verbatim* via Go AST, compiled as bounded fixture, **8/8 native HEAD Boolean states agreed**; unique one-bit repair only relative to a three-bit edit language. The unrelated Echo wrong-handler countertrace remains OPEN. Lean verified restricted translation, not general Go operational semantics.

**No new P41 source experiments are implied by importing these results.** Every new source evidence claim must cite its *own* checked run, source commit, contract and oracle.

## 5. Classical competitors — primary literature and precise distinctions

Original theory the P41 project must not ignore:

- **D. L. Parnas (1972), *On the Criteria to Be Used in Decomposing Systems into Modules***, CACM 15(12), DOI [10.1145/361598.361623](https://doi.org/10.1145/361598.361623): change-robust module boundaries and information hiding are classical.
- **B. Liskov & J. Wing (1994), *A Behavioral Notion of Subtyping***, TOPLAS 16(6), DOI [10.1145/197320.197383](https://doi.org/10.1145/197320.197383): substitutability requires behaviorally preserved properties, not a syntactic subtype name.
- **J. C. Reynolds (2002), *Separation Logic: A Logic for Shared Mutable Data Structures***, LICS, DOI [10.1109/LICS.2002.1029817](https://doi.org/10.1109/LICS.2002.1029817): frame/separating conjunction and disjoint mutable resources already capture much of P40's repair safety.
- **C. B. Jones (1983), *Tentative Steps toward a Development Method for Interfering Programs***, TOPLAS 5(4), DOI [10.1145/69575.69577](https://doi.org/10.1145/69575.69577), foundational rely/guarantee specifications for controlled interference.\n- **P. O'Hearn, J. Reynolds & H. Yang (2001), *Local Reasoning about Programs that Alter Data Structures***, CSL, DOI [10.1007/3-540-44802-0_1](https://doi.org/10.1007/3-540-44802-0_1), local reasoning and frame-style approaches.\n- **C. A. R. Hoare (1978), *Communicating Sequential Processes***, CACM 21(8), DOI [10.1145/359576.359585](https://doi.org/10.1145/359576.359585), a distinct communication/process account. **Terminology warning:** P40's “source-aware CSP” comparator is typically a **constraint satisfaction problem** encoding of source admission. It is not automatically a theorem of Hoare's Communicating Sequential Processes. The P41 papers must spell out which meaning is used and avoid conflating them.

**Priority status:** Conventional compiler semantics, observational refinement, CSP (constraint satisfaction), separation logic, Parnas module decomposition and rights/capability models explain existing bounded source outcomes. Novelty **HOLD** until P41 identifies a source-realizable implication not reducible to these with matched information budgets.

## 6. Independent gate sequence — P41-P0 through P41-P5

- **P41-P0 (current):** fix canonical sorts/signatures, statuses and error modalities. Initial free-product Lean independence is a **synthetic smoke test** for definitions, not real A–F irredundancy.
- **P41-P1 — Observational Source/Authority Contractization:** identify verifiable rights data (repository branch-protection/authenticated maintainer records, versioned approval, permissible edit classes) and provider graph evidence. Without independent C and F evidence, explicitly HOLD broad theories relying on them. Specify clients with full headers, route identity and effect contracts.
- **P41-P2 — Irredundancy & Reduction Court:** each candidate axiom has an (N-1) model and a proposition that fails without it; source-realized examples must survive *exactly the same* admissible edit grammar and observer budget. Distinguish logical independence, semantically restricted independence, practical measurement independence and causal intervention.
- **P41-P3 — Conditional SOLID Reconstruction:** separately formalize SRP, OCP, LSP, ISP, DIP as scoped theorem *conclusions*; do not presuppose them or claim whole historical SOLID equivalence. Each theorem needs a specified observer class, applicability conditions, countermodel and best classical equivalent.
- **P41-P4 — Prospective Cross-Ecology Falsification:** use real unsettled maintenance issues, freeze predictions before reproducing new outcomes, do not treat previously known issue reporter observations as blind. Match source evidence access across novel-model and strong classical comparator.
- **P41-P5 — Publication Decision:** mathematical priority PASS only after a precise nonclassically reducible property, kernel proof and source evidence. Otherwise publish a rigorous negative reduction/adequacy result.

## 7. Explicit P0 closure / P1 entry requirements

P0 bounded completion requires three separate receipts: (i) exact formal candidate signature compiled/kernel checked, (ii) typed empirical vs synthetic evidence matrix independently audited, and (iii) canonical P41 Run + GitHub research contract linked with P40 transfer. If the Lean compiler/provenance CI fails, leave the corresponding gate unverified. P0 completion *does not* complete P41.

**P41 stage RUNNING. P41-P0 bounded typed-definition court PASS**: source/evidence audit [Actions #38062650626](https://github.com/WhoSia/EvoNOMOS/actions/runs/38062650626) verified at checked HEAD `59226d455e0379caf167039f912c0e67defe6fa6`, artifact `11673158706` digest `sha256:a872646458728c5d8fecdaf9c2036463a81e6a571dd55d1a52088892aa65f21d`; Lean 4.34.1 standalone [Actions #38062585674 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38062585674), exact tested formal-source HEAD `9c4e92a90571e1bfaa20306bdc3e0d800e5be13f`, artifact `11673927623` digest `sha256:6b6bc5b47e0ab770043a0b1b39ef1c695aa97db8e16ee6cd2c177b8596864344`. Earlier Lean failures #38062448745 (missing Lake manifest) and #38062503504 (missing decidability for `decide` on custom predicates) were corrected without changing theorem statement intent; the final bounded proof compiled and independent leanchecker passed. **Neither PASS proves empirical A–F independence or full software semantics. P41-P1 evidence gate NEXT. A–F independent universal axioms OPEN. Historical SOLID full derivation OPEN. Classical competitors UNDEFEATED. New fundamental OO law HOLD. LAW-R2 NOT_AUTHORIZED.**
