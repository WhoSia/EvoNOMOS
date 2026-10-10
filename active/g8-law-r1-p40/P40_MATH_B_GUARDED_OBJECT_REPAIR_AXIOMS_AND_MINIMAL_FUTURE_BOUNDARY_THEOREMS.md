# P40-MATH-B — Guarded Object-Repair Axioms, Behavioral Simulation and Minimal Future-Edit Boundary Semantics

**EvoNOMOS Generation VIII LAW-R1-P40 · 2026-10-10 KST · SCOPED MATHEMATICS, FINITE SYNTHETIC VERIFICATION · P40 OPEN · NEW OO LAW HOLD · LAW-R2 NOT_AUTHORIZED.**

Lineage: [P40-MATH-A](P40_MATH_A_OBJECT_REPAIR_STRUCTURES_AND_SOLID_STRICT_REDUCT_PROGRAM.md) · [P40-P4 original pinned chi](P40_P4_ORIGINAL_CHI_BOUNDARY_GLUING_AND_MINIMUM_SOURCE_CONTRACT_COURT.md) · [P39 Math-B](../g8-law-r1-p39/P39_MATH_B_TYPED_SOLID_IMPLICATIONS_AND_CONDITIONAL_OCP_COROLLARY.md).
Executable [finite continuation checker](../../tools/p40-math-b/dynamic_boundary_continuation_court.py) · [read-only CI workflow](../../.github/workflows/g8-p40-math-b.yml). A successful CI run must be independently read back before declaring hosted PASS.

## 1. Claim discipline and typed objects

The goal is to find **independent source and behavioral premises** yielding useful conditional SOLID* properties. Merely naming a larger signature containing all five labels is not a mathematical derivation. Each of historical SRP/OCP/LSP/ISP/DIP lacks a unique universally agreed extensional predicate; a star denotes a specifically scoped technical property, not the complete historical norm.

Let a repair configuration be \(x=(p,h,\alpha)\), with a typed source state \(p\), rights/release history \(h\), and any extra shared-boundary state \(\alpha\) that affects future legality. For a designated **finite** edit alphabet \(E\), define guarded partial source transformations \(e:x\rightharpoonup x'\), with typed-source safety \(I(x)\) and old-client observations \(o_C(x)\). **Runtime method execution is distinct from source edit transitions.** Actual source edit witnesses require the language's compiler and the specified client tests; declared permission does NOT certify actual third-party maintainer authority.

This signature should not assume:
- that different source edit operators commute;
- that local interface satisfaction implies contextual behavioral substitutability;
- that old-client observational equivalence determines future edit rights;
- that SOLID properties hold by default;
- that an observable trace signature can recover source dependencies.

The following are **independent kinds of premises**, not yet proved logically independent as a minimal axiom basis: (A) static type and source-state acceptance; (B) client-labeled operational semantics; (C) guarded and history-sensitive edit permissions; (D) declared goals, invariants and closed source regions; (E) composition constraints and typed shared-boundary effects; (F) source dependency and capability incidence. An actual irredundant axiom-system theorem remains OPEN.

## 2. Theorem B1 — local forward simulation implies scoped history-aware LSP*

Fix an abstract interface protocol with states \(A\), a candidate concrete implementation with states \(B\), and a set of permitted client method calls \(M\). Let the labeled operations be transitions \(a\xrightarrow{m/o}_A a'\) and \(b\xrightarrow{m/o}_B b'\), where \(o\) is the full event visible under a **declared interface-restricted client grammar**. Let \(R\subseteq B\times A\) satisfy:

1. Every admitted concrete initial state \(b_0\) is related to an admitted abstract initial state \(a_0\).
2. At every reachable \(bRa\), any method \(m\) allowed by the abstract precondition is enabled by the concrete provider (no strengthened precondition).
3. For every such concrete method transition \(b\xrightarrow{m/o}_B b'\), there exists an abstract transition \(a\xrightarrow{m/o}_A a'\) with \(b'Ra'\). All observed method effects, errors and events have the same relevant labels.
4. Any abstract state invariant or history contract appealed to by admitted clients is transported along \(R\), and clients cannot bypass the method protocol via representation identity, reflection or unmodeled shared effects.

**Conclusion:** every finite concrete client interaction trace has a matching permitted abstract trace, and all trace-closed abstract safety/history properties expressed over the chosen observations transfer to the concrete implementation. Hence a scoped behavioral substitutability/LSP* condition holds.

**Proof:** induction on finite method-call sequences. The base case uses initial related states; the induction step applies the local transition matching condition and preserves \(R\). Prefix-closed safety properties then follow by trace inclusion. Infinite-trace/liveness or divergence-sensitive refinement additionally requires a matching progress/fairness condition; it is NOT proved by the finite induction.

This is classical data refinement and behavioral subtyping, not a new theorem. Critically, the hypotheses are **per-method simulation obligations**, not simply the global conclusion "substitutable"; the stated abstract-spec scope must be checked. Compare Liskov & Wing (1994), including history constraints.

## 3. Theorem B2 — minimal exact future-edit observation quotient

For the **deterministic finite** guarded repair model, totalize illegal edits with a sink \(\bot\). Let \(\bar S=S\cup\{\bot\}\), \(\delta:\bar S\times E\to\bar S\), \(\delta(\bot,e)=\bot\), and \(o:\bar S\to O\). The observation \(o\) may include old-client observations, current compile/source acceptance, and demand completion. History that changes permissions MUST be encoded in a state coordinate; see B3.

Define:
$$
s\equiv_{\mathrm{future}}t
\quad\Longleftrightarrow\quad
\forall w\in E^*:\ o(\delta^*(s,w))=o(\delta^*(t,w)).
$$

**Theorem:** \(\equiv_{\mathrm{future}}\) is a right congruence and induces an exact Moore quotient \(\bar S/{\equiv_{\mathrm{future}}}\). Among deterministic state quotients whose transitions and outputs faithfully preserve every finite edit continuation, it has the **smallest number of classes**.

**Proof:**
- For any edit \(e\), the future observations from \(\delta(s,e)\) on suffix \(w\) are exactly those from \(s\) on \(ew\). Thus \(s\equiv t\) implies \(\delta(s,e)\equiv\delta(t,e)\), proving right congruence.
- The quotient output \(o([s])=o(s)\) and transition \(\bar\delta([s],e)=[\delta(s,e)]\) are well-defined (including suffix \(w=\epsilon\)).
- If a deterministic exact abstraction \(q\) collapses \(s,t\), then all future transitions from \(q(s)=q(t)\) remain equal and their outputs match. Consequently \(s\equiv t\). Therefore \(\ker q\subseteq\equiv_{\mathrm{future}}\): every exact quotient has at least as many classes.
This is a Moore/Myhill–Nerode style classical theorem, now given a **specific guarded-source-edit interpretation**. It makes no claim to priority for automata minimization.

**Limitations:** nondeterministic source edits require a specified may/must/trace semantics; an ordinary deterministic quotient cannot be asserted without determinization. Unbounded histories may make the abstract state set infinite. Infinite traces, fairness, edit cost and probabilistic policies require separate observation grammars.

## 4. Theorem B3 — a source-only quotient can fail to be Markov

Take two histories \(h_a,h_d\) reaching identical typed source \(p\) but giving different rights for a future edit \(e\): \(\Gamma(p,h_a,e)=1\), \(\Gamma(p,h_d,e)=0\). Both configurations have the same source projection \(\pi_P(p,h)=p\). If an abstract source-only transition function \(\delta_P(p,e)\) exactly reflected the enabledness of the history-sensitive transition, it would need to be both defined and undefined at \((p,e)\), contradiction.

**Conclusion:** whenever such history-dependent rights occur, source text alone is NOT an exact transition state. History/rights must be carried in the source repair state, or exact reachability is lost. This is a basic Markov/state-refinement obstruction, not a discovery about all owner policies. The existence of such rights in a particular third-party repository requires separate evidence.

## 5. Exact finite court: route/middleware staging

The [pinned original chi experiment](P40_P4_ORIGINAL_CHI_BOUNDARY_GLUING_AND_MINIMUM_SOURCE_CONTRACT_COURT.md) verified that global middleware Use after route registration fails, while middleware-first can pass. The following is a **synthetic deterministic abstraction** of that measured order constraint, not a second native Go execution:

- States: \(00,U,M,UM,\bot\).
- Edit symbols \(E=\{U,M\}\).
- Legal edges: \(00\xrightarrow U U,\ 00\xrightarrow M M,\ U\xrightarrow M UM\).
- Every absent edge goes to \(\bot\). Goal \(G=\{UM\}\).

With goal-only output \(o_g(s)=[s=UM]\), minimization yields exactly FOUR future-continuation classes:
$$
\{00\},\quad\{U\},\quad\{UM\},\quad\{M,\bot\}.
$$
With the stronger output \(o_c(s)=([s\ne\bot],[s=UM])\), minimization yields FIVE distinct classes because \(M\) is still a legal intermediate source but \(\bot\) is not.

The Python checker uses partition refinement, checks suffix-observation equivalence over all edit words of length at most 6, verifies right-congruence, distinguishes \(UM\) from \(MU\), and tests a minimal source-identical/permission-different history countermodel. These **finite checks support this five-state model only**; the theorem's general correctness follows from the written proof, not from bounded enumeration. Expected terminal marker: P40_MATH_B_FINITE_SYNTHETIC_COURT_PASS.

**A valuable boundary consequence:** the smallest sufficient boundary depends on the **observation contract**. Exact capability to predict *future goal achievement* may require less source-boundary information than exact capability to predict *present compile status and future goal achievement*. This is ordinary observation-relative automata minimization, not a universal numeric bound.

## 6. Conditional SOLID* consequence map: no hidden circularity

| Principle | Exact result so far | Additional independent proof obligation / failure mode |
| --- | --- | --- |
| SRP* | Coordinate-local ownership/edit effects plus rectangular invariant imply commute-and-frame locality, **already P39 Math-B**, classical | Responsibility partition and its social/requirements meaning are NOT derived from algebraic independence |
| OCP* | For a finite per-demand edit plan with acyclic prerequisite partial order, all down-set checkpoints source/type/contract safe, all prerequisite-enabled edge permissions independently verified, closed core preserved and final goal satisfied: any topological order gives a valid extension path | Strong plan construction premises; no OCP from LSP alone. This is a constructive sufficient condition, not the weakest one or a universal OCP theorem |
| LSP* | **B1: conditional derived result**, finite protocol trace/history safety under a local forward simulation relation | Representation-exposing contexts, diverging protocols or hidden shared effects invalidate the claim |
| ISP* | The old-client observation quotient and client demand projection are representable, **already P39 Math-B** | Native selector/method-set/source-embedding preservation not derivable from observation factorization |
| DIP* | Source dependency factoring is measurable from the typed dependency graph | Runtime trace equivalence does NOT determine dependency arrows; no independent theorem forcing stable abstraction direction yet |

**Formal nonentailment:** let \(U(\mathcal M)\) forget source dependency and owner relations. Two repair structures can have identical \(U\)-behavior but different source dependency edges. Any \(U\)-definable predicate has equal truth on the pair, while DIP* as a source graph predicate can differ. Therefore no axiomatization based solely on \(U\)'s runtime observations can derive source-level DIP*. Similarly, old-client trace preservation alone does not entail guarded future OCP*. These independence observations agree with and do not supersede P39 Math-B.

**Research-level obstruction:** a conjunction of independently checked SRP*/LSP*/ISP*/DIP* conditions does NOT yet identify all future source-edit gluing obstructions. Conversely, adding all strong cross-boundary constraints as premises may merely restate the desired repair result. Establish minimality by deleting one condition and constructing a real source counterexample for each deletion.

## 7. Classic prior art and deliberately open questions

1. [Liskov & Wing (1994), A Behavioral Notion of Subtyping](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf): method pre/post, invariants, history rule; source-owner permissions are not deducible from the behavioral protocol.
2. [Go specification](https://go.dev/ref/spec) and [official module-compatibility advice](https://go.dev/blog/module-compatibility): physical interface/method-set hazards and the new-interface alternative defeat naive claims of a new ISP law.
3. [Yannakakis (1981)](https://www.vldb.org/dblp/db/conf/vldb/Yannakakis81.html): acyclic join/CSP local-global algorithms. Any boundary-gluing result must state what exceeds ordinary constraint satisfaction.
4. [Abramsky–Brandenburger (2011)](https://arxiv.org/abs/1102.0264): global-section obstructions; the software analogy requires explicit restriction-map/typed-source proofs before a sheaf claim.
5. Classical Moore machine minimization, Myhill–Nerode, automata partition refinement, rely/guarantee, separation logic/frame rule, trace and event-structure theory remain undefeated.

**Most valuable next falsification:** replace purely deterministic finite source edits with genuinely competing owner-authorized partial source morphisms where local contracts include evolving interfaces, dynamic observations and release histories. Search for a theorem **not equivalent at matching assumptions** to ordinary automata minimization, forward simulation, guarded reachability or CSP. A natural maintainer-source counterexample is needed before any general OO law claim.

## 8. Verdict

- **PROVED (classical conditional):** local forward simulation implies scoped finite-trace LSP*, continuation-observation equivalence is the coarsest exact deterministic repair quotient, source-only state projection fails under history-dependent rights.
- **FINITE SYNTHETIC VERIFIED:** chi-calibrated ordering machine has 4 vs 5 minimal quotient classes under two declared outputs; edit order is noncommutative in admissibility.
- **NOT PROVED:** full historical SOLID derived from one irredundant minimal OO axiom basis; general unbounded source theorem; superiority to classical theories; LAW-R2.
- **Research state:** P40-MATH-B is a P40 subdocument, not P41. P40 remains OPEN and novel-law identification remains HOLD.
