# P44 — Mathematical Problem Contract (candidate v0.1, 2026-11-04)

**Status: DEFINITION AND PROOF-OBLIGATION WORK, NOT NEW LAW.** P44 stays open until the mathematical objects, comparable rights, observation semantics, target demand language, feasible paths, costs, evidence and classical rival can be specified with counterexamples. R1–R3 source outcomes are retained but are not substitutes for these definitions.

## F0. Levels of discourse
Distinguish (I) the actual source/runtime semantics, (II) the **specified** observer/rights/demand experiment, (III) analysis algorithm and certificate, and (IV) the empirical statement that code and human organizations behave as modeled. Do not turn a finite test of II into a global result about I, or a formal theorem about II into an empirical result about IV.

## F1. Implementations, environment and traces
Let P be a set of typed, versioned program artifacts. Let E be an admissible environment/context set, including dependency versions, upstream API behavior, scheduler and middleware composition assumptions. Let Sigma be the program state space. For p∈P and e∈E, define a possibly nondeterministic trace semantics:
  Tr(p,e) ⊆ Trace.
A trace can record inputs, externally visible outputs, exceptions, temporal order, divergence, resource effects, or state transitions. The semantical universe must state finite/infinite trace choice, fairness and undefined-behavior assumptions. Original Go source soundness is a separate proof obligation.

## F2. Observer-indexed equivalence
An observer family O is a typed collection of context/trace projections o:Trace→Obs_o, with **joint** vector projection:
  vecO(t) = (o(t))_(o∈O).
Define the *joint observation set* for each environment:
  JObs_O(p,e) = { vecO(t) | t∈Tr(p,e) }.
For a fixed declared context family E0⊆E:
  p ≡_(O,E0) q  iff  for every e∈E0, JObs_O(p,e)=JObs_O(q,e).
The joint representation is essential: merely asserting separate marginal sets {o(t):t∈Tr(p,e)} match for each observer loses cross-observer correlations. Example: program A admits traces (0,0),(1,1) and B admits (0,1),(1,0); each individual bit has observed set {0,1} in both, yet the joint observations differ. If the client contract is itself indexed by explicit request and trace fields, O must preserve their same-run grouping, temporal correlation and schedule constraints.
For deterministic finite HTTP probes, the indices are (method, encoded target, headers, execution layer, schedule, result field). For nondeterministic concurrency, sampled observation equality is **not** universal equivalence.

If O⊆O', then ≡_(O',E0) refines (is a subset of) ≡_(O,E0), under shared trace semantics. A finite passing probe suite only establishes a finite-observer result for the executions actually controlled.

## F3. Client obligations and preservation
Represent a protected client contract C as a predicate over the observable trace family with an explicit quantifier over environments and schedules:
  Safe_(C,O,E0)(p) ∈ {true,false}.
The contract can include temporal constraints (e.g. capture(A) before update(B) before response(A)); ordinary status-only contract is insufficient.

For modification histories and multiple demand disclosure events use k∈{0,...,n}, and a contract family C_k = C_0 ∧ d_1 ∧ ... ∧ d_k (assuming demands are compatible). The requirement 'all old clients safe' may refer to C_0 throughout, and 'all previously accepted demands safe' to C_k at each stage. Explicitly distinguish staged activation of demand constraints from *retroactively* requiring D_n at the original state.

## F4. Authority-sensitive, typed edit relation
A right is an authorization token with actor, owned component, permitted operation, precondition and affected boundary (not merely a string such as 'can edit'). Let π be a policy. Define:
  p --[a,π,δ,c]--> p'
when concrete edit δ by actor a is authorized by π, yields source p', and has nonnegative cost vector c∈R^m_{>=0}. Define E_π as the resulting labeled directed graph.

Do not infer a full permitted transition relation by enumerating one chosen three-switch or one app-owned edit grammar. Source ownership, third-party license, dependency upgrades and compile validity are part of an admissibility predicate. Non-authorization must not be mistaken for formal infeasibility in a broader owner model.

## F5. Safe repair paths
For starting state p, future demand d and protected contract C, a finite **strict-prefix-safe** path is
  h=(p=p_0, δ_1, p_1, ..., δ_l, p_l)
such that all transitions belong to E_π, Safe_(C,O,E0)(p_i)=true for every i=0,...,l, and p_l satisfies d. Distinguish strict internal-prefix safety from deployment-checkpoint safety; continuous source editing may not be deployable at every keystroke, so the granularity must be specified.

For a staged demand sequence d_1,...,d_n, define grouped history h=(h_1,...,h_n), with h_k ending at p^(k) satisfying C_0 and all d_j, j≤k, and every edit prefix of h_k satisfying the currently protected obligations C_{k-1}. At stage completion activate d_k; after that stage's edits C_k becomes protected. A simultaneous path-level rather than per-demand model is necessary when demands conflict or priorities change.

## F6. Cost, Pareto front and nonidentifiability of effort
Define a cost vector c(h)=(synthetic source-edit units, review burden, test coverage burden, deployment/operational risk, *measured developer effort if actually observed*, ...). Costs require units, accumulation rule and missing-data markers. Additivity is **an explicit model assumption**, not a fact of human maintenance. For nonnegative scalar path costs:
  K(p,d;π,C,O,E0) = inf{ c(h) : h safe and realizes d } ∈ [0,∞].
The infimum of empty set is +∞. For vector costs use the attainable set and its Pareto-minimal elements; there need not be a unique total 'best architecture'.
A constructive execution path with validated cost U proves K≤U **relative to the declared relation and observer**, never K=U. A lower bound needs complete coverage of all cheaper permitted paths or a sound lower-bound abstraction.

## F7. Structural comparison is conditional
Two initial structures p and q are eligible for a fair comparison if p≡_(O,E0)q, the future demand and protected-observer interpretations are aligned, permission sets are mapped with actor/ownership preservation, and cost units are comparable. A claim:
  K(p,d;π_p,C) < K(q,d;π_q,C)
is conditional on all these. It does not imply global architecture supremacy, superiority for every demand, or greater human productivity. If initial normalization differs, report both future incremental cost and total cost including normalization.

## F8. Source certificate, checker, classical baseline
A proposed source certificate Γ is a finite artifact containing source/dependency IDs, relevant observations, modification rights, program-derived dependency/effect claims, an admissible path or a sound obstruction, cost evidence, and a machine-checkable proof object. A checker V(Γ,p,d,π,C,O) reports PROVED / REFUTED / UNKNOWN; UNKNOWN must not be silently treated as REFUTED. A meaningful soundness theorem must say what PROVED entails in the **actual** source semantics. Finite tests are evidence but alone do not discharge universal soundness.

Challenge: is there a certificate class whose sound checking, size, compositional reuse, or prospective cost under bounded compute is better than a strong **equal-information** classical separation-logic / contextual-refinement / alias-effect / exact finite-search baseline? If both prove the same claims at comparable cost, record a classical tie.

## F9. Formal questions to close within P44
Q1: What trace/context and observation universe is fixed, and which remain unknown?
Q2: What is the exact universe of authorized edits (including source revisions, actor rights, patch granularity)?
Q3: Does stagewise contract preservation quantify all source edit steps or deployment checkpoints?
Q4: Which costs are measurable, and how are missing/uncertain components represented?
Q5: Can Γ imply a source-sound feasibility upper witness, and under what assumptions a lower bound?
Q6: Under which relation between architectures can source-repair simulation lift along arbitrary finite paths?
Q7: Which claims are classical immediate consequences, and what genuinely nontrivial source-level or algorithmic problem remains?
Q8: What observations falsify the model in an independent maintained-repository cohort?

**Completion rule:** a P44 mathematical formulation is complete only when all F0–F9 receive explicit definitions, assumptions, countermodels, proof targets, and an externally reviewable rivalry/novelty audit. No future P45, no LAW-R2 promotion merely from naming these definitions.

## 2026-11-05 amendment — F10. Future information and online repair strategies

The fixed-demand minimum cost K(p,d) defined above is **offline / clairvoyant** with respect to d: it optimizes after the full demand is revealed. This is a valid source repair problem but does NOT by itself define the actor's ability to handle an unknown future requirement after an earlier release.

Explicitly index demand disclosure time and legal decision information:
- time k: already accepted contract C_k and source release checkpoint q_k;
- information I_k: all legitimately observed past demands, source changes and client effects, NOT hidden future d_{k+1},...;
- environment legal choices D_{k+1}(I_k) and an authorized editing actor policy σ(I_k,d_{k+1}) subject to the specified ordering of disclosure versus edit;
- required progress and deadline/checkpoint semantics.

In the simplest two-round case a stage-one commitment s must be chosen before the future demand d is revealed. The key distinct statements are:
  OfflineCover := forall d exists an eligible first-stage commitment s_d and a protected future repair;
  OnlineCommitWin := exists one eligible commitment s such that forall d a stage-one-contract-preserving repair exists from s.
The latter implies the former; not conversely. This is a CLASSICAL online-game quantifier distinction. If first commitment can be delayed until after disclosure, the difference can disappear. If rollback/cross repairs are authorized, they must be included in the edit relation; inferring infeasibility from an artificially restricted grammar is invalid.

For arbitrary finite multi-round settings a valid policy must be history-dependent but nonanticipating. Costs may be worst-case, distributional or competitive to an offline oracle under explicitly declared environmental assumptions; do not silently use a ratio if offline optimum is zero.

## 2026-11-05 amendment — F11. Alternating source abstraction

The ordinary CEGAR-style lower bound for one disclosed fixed demand uses a sound overapproximation of all admissible existential repair paths with cost projection. For an online winning strategy the system chooses edits EXISTENTIALLY while the environment chooses future demands UNIVERSALLY. An overapproximation that invents **system** edits may produce false winning claims, and adding **environment** demands may produce false losing claims.

Therefore a strategy certificate requires a separate alternating source-game simulation: every environment action must be represented, every abstract system move actually implementable by the authorized concrete source editor, activated contracts maintained at every prefix, an adequate information relation for nonanticipating policies, and eventual progress requirements. Simple state/path overapproximation from F6/F8 is NOT enough to certify source-level winning.

[Formal finite source-state countermodel and adversarial review](09_INFORMATION_TIMING_AND_ONLINE_REPAIR.md); [alternating-abstraction polarity](11_ALTERNATING_ABSTRACTION_POLARITY_PROOF_GATE.md); [verified finite Go CI court](13_ONLINE_FINITE_GAME_CI_VERDICT_20261105.md). These are classical semantic distinctions, not G1–G7 closure or a LAW-R2 result. The main P44 target remains source-sound allowed repair under joint client observations and precise rights; online semantics is an optional extension only when forced early commitment is empirically grounded.

## F12. Finite edge-local cost simulation (2026-11-05)

For a fixed, complete, finite, permission-labelled safe source-edit graph, define a state abstraction alpha preserving initial release, disclosure stage, old-client safety and demand goals. Require every authorized safe same-stage concrete edit of cost c to have an authorized abstract image edit with the same rights label and cost no greater than c. Induction over path length then maps every concrete admissible path into an abstract path without increased cost. Consequently abstract optimum L is at most concrete optimum K; a separately verified concrete safe path costing U yields L <= K <= U. This is a classical weighted forward-simulation lemma.

The test checker only validates the supplied finite graph. A missing permitted source edit can lower the actual source optimum and invalidate conclusions about all real source patches. Completeness of source-to-graph extraction, source-level Safe/Goal meaning and actual permission identities remain open proof obligations. This existential path abstraction is not a certificate of an alternating winning policy (see F11). Linked evidence: 15_EDGE_LOCAL_REPAIR_SIMULATION_THEOREM_20261105.md and 20_EDGE_LOCAL_CERTIFICATE_CI_VERDICT_20261105.md. No new law; G1-G7 OPEN.

## F13. Safety and incorrectness evidence have opposite approximation directions (2026-11-05)

Fix one versioned source release, a declared environment and joint trace observer, and the currently active customer contract C. Let T be the feasible observed trace set.

* A sound overapproximation U with T subset U, and C(t) for **every** t in U, certifies universal source safety.
* A sound underapproximation W with W subset T, and some actual t in W violating C, certifies a reachable client-contract failure.
* In every other case, unless additional proof exists, the verdict is UNKNOWN; neither empty tests nor a spurious abstract error establishes a universal or existential source claim.

This is conventional correctness/incorrectness logic; in particular O'Hearn's 2020 original text already studies underapproximate reachable errors. The implementation in evidence/oracle.go proves only the consistency of these rules in a **supplied finite trace universe**. Its certification flags do not self-authenticate real source traces.

For a staged source repair sequence, every protected deployment checkpoint needs a universal safety certificate to claim the entire path safe; a certified bad checkpoint refutes THAT path, not every possible repair. Source-edit graph completeness, right ownership, cost and completeness of runtime trace exploration are independent proof obligations. Do not use the existential source edit F12 abstraction to establish this universal runtime property without separate quantified semantics.

Source reading and Drive canonical intake: 21_NEW_EIGHT_PAPERS_CANONICAL_READING_20261105.md. Detailed conditional evidence gate: 22_OVER_UNDER_EVIDENCE_TRIVALENT_REPAIR_GATE_20261105.md. General G1–G7 source soundness and LAW-R2 still OPEN.

## F14. First source-derived *closed fragment* certificate: Go AST literal-only language (2026-11-05)

After classical F12 edit-graph and F13 execution-trace coverage were shown to be independent, the next deliberately tiny source syntax fragment was fixed. Allowed actual input is **a single comment-free Go source file** with `package fixture` and exactly `func Legacy() string { return "<literal>" }` and `func Future() string { return "<literal>" }`. Both return expressions must be single valid string literals, with no imports, other declarations, parameters, receivers, statements, side effects, comments, build directives, concurrency or external context. A fixed Go compiler/parser version and build context are assumed. The only app-authorized source edit is to replace `Future`'s literal with a member of predeclared finite set D; all other edits are outside the policy universe.

Within this STRICT closed source/rights language, an AST-based enumerator constructs |D| permitted version states and |D|(|D|-1) nonidentity edits, cost one each, and reparses each transformed Go source file. Joint customer observation is exactly the literal outputs of `Legacy` and `Future` in the pure no-input language. Every generated program preserves the older client result. The source-edit graph is complete **by explicit grammar enumeration**, and client trace interpretation is exact **by the stipulated pure source semantics**. An equal-information classical exact graph search returns the same optimal edit distance, so no novel advantage or graph compression is claimed.

This fragment does not model real Go package imports, hidden build contexts, aliasing, scheduler, HTTP middleware, arbitrary patches, or human effort. The main next open obligation is *conservative language extension* with individually verified new constructs and cost/observer-preserving simulation, not claiming arbitrary Go completeness. [Detailed closed-grammar theorem](29_CLOSED_GO_SOURCE_GRAMMAR_FORMAL_THEOREM_20261105.md).

Formerly missing bibliography: [White et al. 2014 original](https://drive.google.com/file/d/1n4vr5-CR7P-_HHBzpkmHmoNzFqzmghDp/view) is now in canonical 10_PAPERS, and the Borodin & El-Yaniv 1998 titled PDF is present but has corrupt streams, kept under 00_INTAKE HOLD rather than misfiled as a readable 11_BOOKS source. [Custody and source limitations](27_WHITE2014_ORIGINAL_AND_BORODIN_QUARANTINE_20261105.md).

## F15. Joint input-output observational contracts under a closed conditional source grammar (2026-11-05)

Extend F14 to one exactly specified pure Go `Future(flag bool) string` with one conditional return and a trailing return. The two branch literals range independently over a predefined finite set D. The only authorized edit changes ONE of the two Future literal values to another member of D, with declared unit synthetic cost; `Legacy() string` is protected and remains constant. Comments, other declarations, imports, statements, nonliteral expressions, aliases and concurrency are outside this versioned source language.

A version is represented by (t,f)∈D², and its joint client observational semantics is `flag=true → (Legacy,t)`, `flag=false → (Legacy,f)`. This restricted source/edit grammar has m² states and 2m²(m−1) directed nonidentity branch-labelled authorized edits, where m=|D|. For m=3, the original Go AST source enumerator produced 9 source states and 36 edits; all nine generated Go source versions were independently compiled and executed with Go 1.23.2. The exact equal-information classical source graph oracle obtained the same optimal cost.

Counterexample: (off,on) and (on,off) have identical marginal output sets {off,on} yet different input→output relations. Thus a marginal-output-only observer is NOT sufficient to certify clients whose contract conditions on the input. A previously accepted `flag=false` return of `on` forbids any later goal returning `off` for false, even when classical unconstrained edit distance is finite. The future `flag=true` requirement `beta` remains obtainable in one authorized safe edit from (off,on). This is established classical contextual equivalence / state graph logic, not new law.

Provenance: corrected [source CI #41962052369](https://github.com/WhoSia/EvoNOMOS/actions/runs/41962052369) and protected-stage [CI #41962356928](https://github.com/WhoSia/EvoNOMOS/actions/runs/41962356928), both source-executed and raw logs verified. Initial F15 GitHub CI #41961920487 failed due to generated Go test source quoting bug; retain that original error record and its separate correction. The new bounded source check does not cover general Go source, scheduler, aliasing, source owner rights, actual maintenance labor or a superior certificate to known CSP/model checking. [Scope and graph theorem](36_F15_BRANCH_SOURCE_RELATIONAL_OBSERVER_VERDICT.md), [backward F12–F15 audit](37_F12_F15_BACKWARD_AUDIT_AND_THEORY_CEILING.md), [White 2009/2012/2014 edition distinction](34_WHITE_2009_2012_2014_LINEAGE_CUSTODY.md). G1–G7 OPEN, LAW-R2 HOLD.

## F16. Shared mutable alias structure and prospective safe edit cost — bounded native Go test (2026-11-05)

Two `Clients` structures contain `Legacy *Cell` and `Future *Cell`, with original observed values both `stable`. In one structure the two pointers refer to the SAME heap cell; in the other they refer to DIFFERENT heap cells. Current declared observation pair is the same `(stable,stable)`; this is NOT proof of full contextual equivalence across all future edits or contexts.

The declared finite edit grammar permits `SplitFuture`, which creates a fresh `Future` cell copied from the existing value, and `WriteFuture(new)`, which writes its existing `Future` cell. Each costs one **synthetic unit**, subject to maintaining `Legacy.Value==stable` after every edit. For an aliased initial state, direct write violates the old-client contract, while split-then-write costs 2. For separated initial pointers, direct write preserves Legacy and costs 1. A naive source-local model that ignores aliasing falsely reports the shared safe cost as 1. A classical alias-aware exact finite graph BFS reports the correct 2 and 1: **classical tie**.

This shows why one cannot infer future independent modifiability from matching current outputs or syntactically localized writes without a verified heap ownership/alias relation. The phenomenon is already explained by classical separation logic and its frame/ownership conditions, not new architectural novelty. Native Go pointer effects were tested in real Go runtime, but the finite allowed edit graph was hand-declared and NOT automatically extracted from arbitrary source patches. Read [F16 native CI](40_F16_NATIVE_ALIAS_CI_VERDICT_AND_BFS_RESET.md) and [KSGT-inspired BFS/DFS root-reassessment protocol](38_BFS_DFS_RESEARCH_DIRECTOR_OPERATING_LOOP.md). Arbitrary program proof, complete source rights and G1–G7 remain OPEN; LAW-R2 HOLD.

## F17. Source-derived Go alias footprint and source-patch versus runtime-action cost (2026-11-05)

In F16 the two operations `SplitFuture` and `WriteFuture` were declared *runtime/structural actions* with synthetic unit cost, giving safe-action distances 2 (shared pointer) versus 1 (disjoint pointer). These numbers MUST NOT be silently called numbers of source code patches or human maintenance effort.

A distinct, tightly closed, **actually parsed and typechecked Go source** grammar is now defined by exactly `Cell struct{Value string}`, `Clients struct{Legacy,Future *Cell}`, `Build() Clients` allocating either one shared or two disjoint stable-valued heap cells, and `Write(c Clients)` consisting solely of `c.Future.Value="new"`. The analyzer computes the two pointer origins in Build's keyed return and thus an exact alias bit for THIS no-escape grammar. It predicts whether the Write runtime action also changes Legacy. Outside constructs (build comments, extra functions, references, effects, unsupported values) are rejected.

A permitted **SOURCE PATCH** `DetachFutureSource` rewrites the original Go Build AST to insert a fresh q allocation and repoint Future to q; it is reparsed/typechecked and the generated code is native compiled and executed. Fix the only source-patch grammar `{no-op, DetachFutureSource}` with declared unit source-edit cost for detach and zero for no-op, and require post-Write joint client observation `(Legacy,Future)=(stable,new)`. The complete allowed-source-patch optima are then 1 for initially shared Build and 0 for already disjoint Build. The `Write` call is a RUNTIME EVENT, NOT an extra Go source edit. The old F16 cost 2/1 remains valid only for its different runtime-operation metric.

The source semantics theorem here is conditional on the exact closed Go grammar, correct compiler/source interpretation and declared patch rights; it does NOT certify the complete edit universe of general Go programs or empirical human engineering costs. Simple exact classical points-to/alias analysis predicts the same effect, and classical bounded source patch search gets the same 1/0 result. **CLASSICAL TIE, G1–G7 OPEN, LAW-R2 HOLD.** [F17 original CI and tests](44_F17_ORIGINAL_GO_SOURCE_REPAIR_CI_VERDICT.md); [runtime/source cost correction](43_F17_SOURCE_PATCH_VERSUS_RUNTIME_ACTION_CORRECTION.md); [BFS competing options](42_P44_BFS_PORTFOLIO_AND_STOPPING_RULE_20261105.md).

## F18. Original-source certificate identity transport and classical baseline failure (2026-11-05)

Let a source s be recognized and typechecked in the explicitly limited F17 single-file Go language, and let c=Issue(s) contain the digest H(tokens(s)) of the complete parser-accepted Go lexical token sequence plus F17 source-derived alias and post-write effects. The syntax scanner treats whitespace as irrelevant but retains Go's automatically inserted semicolon tokens; file comments/build directives are forbidden in this fixed-build domain. A separate TRUSTED ledger must independently pin the exact content receipt H(c); an ordinary SHA-256 next to a self-authored certificate is NOT a digital signature or proof of issuer authority.

Define a **conditional** transport verifier for later source s': if the trusted receipt matches c and H(tokens(s'))=H(tokens(s)), then the old analysis facts can be reused, conditional on collision resistance, the unchanged compiler/build environment and correctness of the previously typechecked original source. If the token sequence changes, verdict INVALIDATED; unsupported source or failed integrity gives UNKNOWN/error. This is ordinary conservative token-identity caching, not source-semantic repair proof transport. In particular even a harmless renaming of a local variable invalidates; changed heap alias relation also invalidates, correctly.

Original [GitHub Actions #41988168928 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41988168928) tested source SHA fa7817e137837392848201f372ae5fcbfb1b1a54; full original Go 1.23.2 tests, vet, race and 200x microbenchmarks PASS. In one run: classical exact-token cache 19,092 ns/op, F18 receipt-verified cache 24,086 ns/op, full source typed alias analysis 45,510 ns/op, initial certificate issuance 55,865 ns/op. Hence classic cache was faster than the F18 verification algorithm in this one tiny benchmark. The speed advantage over full from-scratch reanalysis is not uniquely EAC and disappears as a novelty claim when the fair classical token cache is included. One-run timings are NOT an estimate of population efficacy or developer labor.

The first F18 CI #41987593516 FAILED a whitespace-transport test because the source-position-sensitive AST formatter digest was not invariant to layout; separate code corrected to token-stream hashing. An additional first benchmark CI #41987907647 FAILED due to malformed shell quoting; separately fixed and later CI passed. The failures are retained as model/CI provenance.

Classical relevant primary results directly read from Drive: Hammer et al. 2014 ADAPTON demanded computation graph, Hammer et al. 2015 Incremental Computation with Names/from-scratch consistency, Diemert et al. 2023 incremental assurance, Calcagno et al. 2009 bi-abduction. Harvest P33 F01/F03/F05/F06 gives information cut and future-support counterexamples but transfers no new theoretical authority. [Original reading audit](46_F18_DRIVE_ORIGINAL_AND_HARVEST_BACKFLOW_AUDIT.md); [soundness and skeptical null](47_F18_CERTIFICATE_TRANSPORT_SOUNDNESS_AND_EXPECTED_NULL.md); [raw CI/benchmark verdict](48_F18_ORIGINAL_SOURCE_CI_NEGATIVE_BENCHMARK_VERDICT.md).

**Status: bounded source token cache PASS, classical rival better in one benchmark, true source-changed footprint certificate transport unproved, G1–G7 OPEN, LAW-R2 HOLD.** This section documents a negative research result rather than a new law.

## F19. Conditional source-slice proof transport across an ACTUALLY changed Go file (2026-11-05)

**Domain:** a fixed, externally authenticated (ASSUMED, NOT implemented) build manifest of exactly two code files `fixture.go` and `aux.go` at Go 1.23.2 in one package. The core `fixture.go` obeys the complete F17 single-file no-calls/no-imports/no-globals pure closed grammar `Build()` and `Write(c)` with source-derived alias effects; the sole declaration in `aux.go` is a no-input `Aux() string` returning exactly one literal, with no other code/imports/comments/build directives. Go parser and `go/types` check BOTH files. The *protected old-client observer* calls only Build/Write and observes `(Legacy.Value, Future.Value)` after the Write; it NEVER calls `Aux()`. Other clients that DO call Aux can distinguish the change, so full package contextual equivalence is FALSE.

Under this strict source language, `Obs_{BW}(Core,Aux_1)=Obs_{BW}(Core,Aux_2)` for any typechecked Aux literals, because the core cannot call/access Aux and the auxiliary declaration has no effects or package initialization. This is the classical frame/noninterference property applied to a syntactically restricted complete program, not a novel EAC theorem.

An issued F19 `SliceCertificate` records the Go token-stream digest of the entire core file, source-extracted alias/post-write client effects, and a fixed scope descriptor, with a receipt hash that must be pinned by an external TRUSTED authority. On changed two-file source, `VerifySlice` rechecks the full grammar and `go/types` for both files, then if the core token digest matches, reuses the prior source fact. A true core pointer-relationship change invalidates; unsupported cross-file call, initializer, hidden import or extra declaration yields UNKNOWN/REJECT. A lexical core rename can still invalidate, even if semantically harmless; arbitrary Go source changes are NOT certified.

**Original source experiment:** [Actions #41992707164 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41992707164), exact tested source SHA 0877ac22e153de7bc7bbd0e13c2d3abb04a02626, job 127128634839. Changed `aux.go` content 3 variants reused a prior certificate; changed alias in core invalidated; 11 adversarial scope violations rejected; 4 two-file programs independently compiled/executed; original full tests/go vet/race PASS. Initial [F19 CI #41992388390 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/41992388390) only at generated Go native test quoting, preserved; corrected run [#41992458225 PASS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41992458225), followed by final benchmark CI.

A single 200x-iteration per method Go benchmark on this tiny source pair measured (ns/op): typed classical full reanalysis 106,423; strong classical dependency-token cache 91,269; F19 certificate verify 92,002; F19 initial certificate issue 121,372. The classical equal-information dependency cache matched correctness and was slightly faster in this one run. No reproducible source-wide efficiency superiority or real developer cost demonstrated. Rechecking every file/type means F19 is only a modest cache, not full incremental computation or bi-abduction. More realistic historical maintainer source patches, rights, client contexts and dynamic aliasing remain OPEN. [Formal scope](50_F19_TWO_FILE_SOURCE_SLICE_MATHEMATICAL_THEOREM.md), [original CI/negative rival verdict](51_F19_NATIVE_TWO_FILE_SOURCE_COURT_VERDICT.md). **G1–G7 OPEN; LAW-R2 HOLD.**
