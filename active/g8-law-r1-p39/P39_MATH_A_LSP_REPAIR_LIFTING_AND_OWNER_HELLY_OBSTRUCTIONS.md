# P39-MATH-A — LSP, Source-Edit Path Lifting, and Higher-Order Owner-Option Obstructions

**2026-10-10 KST · PURE/THEORETICAL COMPUTER SCIENCE FIRST · FINITE CLASSICAL PROOF COURT · NO NOVEL LAW YET.**

P39 [scientific opening and accepted owner direction](P39_P0_OPENING_MATHEMATICAL_FOUNDATIONS_AND_SOLID_IMPLICATION_PROGRAM.md). Source prior: [P37 future-repair quotient](../g8-law-r1-p37/P37_MATH_I_MINIMAL_FUTURE_SUFFICIENT_QUOTIENTS_AND_CONTEXT_NONCOMMUTATION.md); [context/permission equivalence](../g8-law-r1-p37/P37_MATH_J_COMPOSITIONAL_MINIMALITY_CONTEXT_CLOSURE_AND_AUTHORITY_PARTITION_RECONFIGURATION.md).

## A0. Do not misquote or weaken the original LSP

Liskov and Wing, *A Behavioral Notion of Subtyping* (1994), [original PDF actually held in Drive](https://drive.google.com/file/d/1g7ruRxKmmki7ts6fQ09MIOwuYPCeCVvl/view), define behavioral subtyping through specifications, method pre/postconditions, invariants and **operational object histories**. They are not content with one output or present behavior. Their history constraint concerns *runtime state evolutions of objects*, which may be shared across clients. It does **not automatically quantify over future modifications of library source code, changed ownership permission and deployment responsibilities**. This source/runtime distinction must be explicit.

For the following mathematics fix an observation map \(o:S\to O\), where \(o(s)\) denotes *all operational behavior and historical safety guarantees promised to the chosen pre-change client contexts*—not just a sample test return value. Two source implementations \(s,t\) with \(o(s)=o(t)\) conform to the same operational observations; this is a strong current observational equivalence **within that declared client/operation grammar**, not a claim of subtyping across all possible future APIs.

Fix **separate meta-level** source-edit transitions \(s\xrightarrow{\ell,\gamma}s'\), whose label can include owner authorization, source transformation, edit costs, demanded future contract and invariant-preserving checkpoints. Such edges are *not runtime method calls*.

## A1. No-go: operational LSP does not entail equivalent future-source repair

Let \(\operatorname{May}_{\Gamma,I}(s,d)\) mean an authorized finite **source edit path**, staying in invariant-admissible source states I, ends in a state satisfying demand d.

**Countermodel (three source states, one edit):** \(S=\{a,b,g\}\), \(I=S\), \(G_d=\{g\}\), \(o(a)=o(b)\) even for every admitted old runtime history, and \(\Gamma=\{a\to g\}\). Then both a,b satisfy the same old operational client contract, but

\[
\operatorname{May}(a,d)=1,\qquad \operatorname{May}(b,d)=0.
\]

One implementation's permitted owner edit can reach a future accepted source and the other's cannot. This **refutes** the implication "operational LSP \(\Rightarrow\) future-repair equivalence" **for source edits not included in the operational type's specification**. It does not refute the real Liskov–Wing theorem; no source-edit promises were encoded in the original subtype contract. If one augments an "LSP" definition to explicitly include all source edits and future demands, the stronger conclusion can become a definitional restatement; the extra edit-lifting assumption needs independent justification.

**More general factorization/no-go:** Any future repair signature \(F:S\to\{0,1\}^D\) is inferable exactly from current operational observation o **if and only if** \(\ker o\subseteq\ker F\). This is classical factorization (P37-MATH-I). Any structural predicate (owner right, module decomposition, OCP/ISP-like dependency metric) that varies within an o-fiber cannot be a logical consequence of o **alone**. That establishes only model-relative *non-entailment*, because SRP/OCP/ISP/DIP have no unique universal formal semantics; a source-level formalization might add other axioms.

## A2. Positive classical theorem: source-edit p-morphisms extend LSP-like abstraction to future repair

Take concrete source-edit graph \((S,\to_S)\), abstract graph \((T,\to_T)\) and a total abstraction \(p:S\to T\). Fix invariant-admissible sets \(I\subseteq S\), \(J\subseteq T\) and matching future-goal sets \(G\subseteq I\), \(H\subseteq J\). Assume:

1. **Exact admissibility reflection:** \(I=p^{-1}(J)\).
2. **Exact goal reflection:** \(G=p^{-1}(H)\).
3. **Forth:** every admissible concrete edge \(s\to_S s'\) projects to \(p(s)\to_T p(s')\).
4. **Back / local path-lifting:** for every admitted \(s\in I\) and **each** admissible abstract edge \(p(s)\to_T t\), there exists an admitted concrete edge \(s\to_S s'\) with \(p(s')=t\).

Then for every admitted \(s\in I\):

\[
\boxed{s\models EF\,G \quad\Longleftrightarrow\quad p(s)\models EF\,H.}
\]

**Proof:** Forward project each step in a finite source repair witness; invariant and goal assumptions preserve acceptance. Conversely, choose any finite abstract accepted path and lift its first step using (4) from the actual concrete current state; iterate using (4) after every lifted step, then reflect H-membership at the final state. The empty path is handled by (2). All steps remain admitted by (1). This is a standard **bounded morphism / back-and-forth transition argument**, closely related to classical simulation/bisimulation, not a newly invented mathematical law.

**Weighted labelled corollary:** If concrete/abstract edit labels and nonnegative edge costs match along projected and lifted transitions, then the infimum finite safe repair cost for G from s **equals** that for H from p(s), with \(+\infty\) for impossible goals. Proof: both directions transport finite paths of *identical total cost*. If a lift only guarantees reachability, no statement about optimal cost follows; if owner authorization prevents a lift, the converse implication fails.

**Important caveat:** The positive theorem is *far stronger than LSP as ordinarily specified*. We have not derived a general SRP/OCP/ISP/DIP corollary. We have characterized what **extra source-edit structure** suffices. Strong classical p-morphism prior art already captures this exact theorem. A useful paper must identify a *new natural restriction* or independently verifiable obstruction not reducible to that standard argument.

### Finite scope verified independently of any original Go

[P39-MATH-A Python finite checker](../../tools/p39-math-a/repair_lifting_court.py) exhausts **all 512 directed source graphs** on three vertices (self-edges allowed) and **all 16 abstract graphs** on two vertices, total **8,192** graph pairs, for p(a)=p(b)=u and p(g)=v, with invariant all states and goal g/v. It validates the path-lifting theorem for **160** graph pairs satisfying both forth and back, and finds **128** source graphs in which a,b have different future-May despite the stipulated same old client observation. These counts characterize **this finite design only**.

## A3. Three-owner obstruction: pairwise valid repair alternatives need not glue globally

Let U be a **single shared universe of candidate concrete source-repair options** (never conflate unrelated local programs). Each real owner i permits a subset \(F_i\subseteq U\). Then a globally authorized solution exists exactly when

\[
\bigcap_{i=1}^{m}F_i\ne\varnothing.
\]

Pairwise nonempty intersections \((F_i\cap F_j\ne\varnothing)\) do **not** suffice. Minimal three-option witness:

\[
U=\{0,1,2\},\quad F_A=\{0,1\},\quad
F_B=\{1,2\},\quad F_C=\{0,2\}.
\]

Every pair has a common candidate, but no candidate is accepted by all three. This classical constraint-satisfaction/global-section obstruction is more useful than slogans about three owners or "responsibility": no local pairwise review can prove global source repair without additional structure.

This model is intentionally NOT the same as a real institution's legal approval authority; membership must be derived from actual edit/contract evidence before transport to software. If each owner controls independent patch coordinates rather than selecting from one shared U, use a **constraint satisfaction problem on compatible assignments**, not naive intersection of disjoint option names.

## A4. A conditional structural result: Helly geometry of repair-option sets

Suppose U is the vertex set of a **tree of admissible repair options** \(T\), and each owner's allowed option set \(F_i\) induces a **nonempty connected subtree** of the *same tree*. Then

\[
(\forall i,j,\ F_i\cap F_j\ne\varnothing)
\quad\Longrightarrow\quad \bigcap_i F_i\ne\varnothing.
\]

**Proof:** Root the tree arbitrarily. For each connected subtree F_i let \(r_i\) be its vertex closest to the global root (this vertex is an ancestor of all other members of F_i). Pick \(r_k\) of maximum depth. For any i choose \(x\in F_k\cap F_i\). Both \(r_k\) and \(r_i\) lie on the root-to-x path, with \(r_k\) at least as deep; thus \(r_k\) is on the unique path \(r_i\leadsto x\) entirely contained in F_i, and hence belongs to F_i. Since i was arbitrary, \(r_k\) is globally feasible. This is the **known Helly property of subtrees of a tree**, not a new result.

To prevent accidental overclaim, test a 3-vertex path \(0-1-2\):
- Among the seven nonempty arbitrary subsets, the exhaustive checker finds **six ordered triples** with all pairwise intersections nonempty but total intersection empty.
- For the six **connected intervals** \(\{0\},\{1\},\{2\},\{0,1\},\{1,2\},\{0,1,2\}\), the checker finds no failures among **216 ordered triples**.

**Scientific opening rather than theorem promotion:** The source repair option space is generally a directed branching graph with merges, cycles and compatibility constraints, *not necessarily a tree*. The necessary original research is: derive a natural class of source/owner repair complexes with provably bounded Helly number, or a real higher-order obstruction that beats existing constraint-solving and sheaf-gluing methods. Merely noticing pairwise-versus-triple incompatibility is classical. See Abramsky/Brandenburger (2011) global-section obstruction prior art; no false claim that source code inherits physical contextuality theorems.

## A5. Candidate implication diagram — logical status, not a SOLID branding diagram

| Claimed implication | Status under specified source-edit/operational semantics |
| --- | --- |
| Full Liskov–Wing operational subtype conformance ⇒ every future source edit can be reproduced | **FALSE without extra meta-level hypotheses**, A1 countermodel |
| Runtime observation quotient ⇒ exact future repair signature | **IFF** future signature is constant on each old observation fiber (classical P37 factorization) |
| Runtime observation + *exact edit path lifting / reflection* ⇒ identical future repair reachability | **TRUE conditionally**, A2 classical bounded-morphism theorem |
| Edit path lifting with matching labels/costs ⇒ equality of minimal future repair costs | **TRUE conditionally**, weighted theorem |
| Each pair of owner option sets has an admissible common patch ⇒ all owners have one | **FALSE in general**, A3 three-owner obstruction |
| Pairwise overlap of connected owner-acceptable *subtrees of one shared repair-option tree* ⇒ common patch | **TRUE**, A4 classic Helly theorem |
| "LSP ⇒ SRP/OCP/ISP/DIP" unqualified | **NOT A WELL-TYPED UNIVERSAL THEOREM** until all principle predicates/program-model assumptions are defined; extensional observations alone cannot force nonconstant source-dependency properties |

## A6. Strongest original theory and prior-art audit

- [Liskov & Wing (1994), original PDF actually held in user's Drive](https://drive.google.com/file/d/1g7ruRxKmmki7ts6fQ09MIOwuYPCeCVvl/view) — behavioral subtyping includes runtime history constraints, explicitly read. A1 is **not** a refutation of their original theorem.
- [Joyal, Nielsen & Winskel (1996), *Bisimulation from Open Maps*](https://doi.org/10.1006/inco.1996.0057) — classical categorical path-lifting/bisimulation; verified publication description, not claimed held full PDF.
- [Category Theoretic Models of Data Refinement (2009)](https://doi.org/10.1016/j.entcs.2008.12.064) — classical simulations and categorical refinement; verified abstract/landing.
- [Abramsky & Brandenburger (2011), *Sheaf-Theoretic Structure of Non-Locality and Contextuality*](https://arxiv.org/abs/1102.0264) — classical global-section obstructions; mathematical analogy only; original full PDF not read here.
- Standard graph Helly property of subtrees (theory predates EvoNOMOS); no newly claimed originality for A4.

## A7. What could genuinely be paper-grade *mathematics* next?

**Priority I — Owner-labelled edit-fibration failure invariant.** Define a minimal certificate for a failed abstract edit lift in terms of independently justified source ownership, branching repair contexts and persistent invariant. Compare equivalently strong classical open-map/coalgebraic notions. Seek a nontrivial exact minimality characterization or constructive realization theorem; otherwise HOLD.

**Priority II — Hypergraph/nerve structure of source-repair options.** Find source-grounded contexts with pairwise source patch compatibility but higher-order obstructions, and derive a **new, nontrivial conditional Helly bound or obstruction invariant** under a natural source-grammar restriction. Test minimal counterexamples and try to break the assumed tree/convex property. Do not use sheaf language without explicit restriction maps and a global-section theorem.

**Priority III — Formal SOLID hierarchy.** Specify modest typed model-dependent versions of ISP (client-demand projection), OCP (cost/permission of changing implementation under new demand), DIP (dependency inversion via allowed interface abstraction), SRP (independent change-reason partition), and LSP (operational contracts). Compute the implication/nonimplication Hasse diagram over a finite grammar, prove negative examples and add **independently justified** assumptions for positive corollaries. Never present this as the historically unique intended semantics of SOLID.

**Paper track:** a serious *theory* paper might be “From Behavioral Subtyping to Evolvability: A Source-Edit Fibration and Higher-Order Compatibility Calculus,” **only if** Priority I or II actually yields a novel theorem beyond open maps, modal bisimulation, Helly/CSP and sheaf gluing. The current A1–A4 mathematics is correct but **classical**, so PAPER-THEOREM-NOVELTY HOLD.

**End state:** \`P39_MATH_A_LSP_SOURCE_EDIT_NONIMPLICATION__CLASSICAL_P_MORPHISM_FUTURE_LIFT__THREE_OWNER_HELLY_OBSTRUCTION__8192_GRAPH_PAIRS_216_SUBTREE_TRIPLES__NO_NEW_LAW_IDENTIFIED__DIP49_HOLD\`.
