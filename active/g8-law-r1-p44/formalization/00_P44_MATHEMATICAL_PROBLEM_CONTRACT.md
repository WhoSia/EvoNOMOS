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
