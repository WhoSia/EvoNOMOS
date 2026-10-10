# P39-MATH-G — Acyclic Owner-Hypergraph Gluing, Invariant-Coupled Separator Obstructions & Exact Ternary Shattering Capacity

**2026-10-10 KST · USER-REQUESTED MATHEMATICS-FIRST SOURCE-REPAIR LAW COURT · NO ORIGINAL GO · NEW PURE-MATH THEOREM IDENTIFICATION HOLD.**

Canonical continuity: [MATH-C safe source-edit cuts](P39_MATH_C_MINIMUM_SOURCE_EDIT_CUTS_OWNER_PRECEDENCE_AND_ANTIMATROID_SURVIVAL.md) → [MATH-D Nerode history memory](P39_MATH_D_HISTORY_DEPENDENT_OWNER_REPAIR_RESIDUAL_MEMORY_AND_TRACE_OBSTRUCTIONS.md) → [MATH-E Stanley pairwise source-memory](P39_MATH_E_CHROMATIC_INTERACTION_MEMORY_AND_STRUCTURAL_BOUND_COURT.md) → [MATH-F ternary owner rights & unbounded sparse directed-cycle obstruction](P39_MATH_F_TERNARY_OWNER_CONSTRAINTS_CYCLIC_MEMORY_AND_FOUR_LOCAL_OBSTRUCTION_COURT.md) → **MATH-G**.

## G0. Types, assumptions and why this restriction is substantive

Let V be n distinct **one-shot physically commuting source-edit events**. Baseline legal histories contain **every permutation** of V and end at the same actual-source *snapshot*. The only future owner questions are independently named, selectable, **triple-local** permission tests q_e, for e={i,j,k} in a 3-uniform hypergraph H; q_e returns the relative-order parity \(t_e(\pi)\) of its triple under history π. Both values 0/1 count as potential individually legal future right states. Each distinct profile is distinguishable by a concrete future q_e query, so the exact additional memory at the fully applied source is \(\lceil\log_2 |\{t_H(\pi):\pi\in S_V\}|\rceil\) bits by classical Myhill–Nerode. This is **not** a claim about arbitrary real Go ownership without code/reviewer proof.

An optional **prefix safety / authority invariant** is a poset P of mandatory one-shot edit precedences; then only its linear extensions are legal and each intermediate set of applied edits must be an **order ideal**. Crucially, adding P is a different model from the all-permutations baseline; "α-acyclic H" alone does not certify the joint H+P model.

A hypergraph is α-acyclic when it admits a **join tree (running-intersection tree)** for its hyperedges, equivalently (for a finite hypergraph) when GYO reduction removes all nonempty scopes; equivalently primal graph chordality plus hypergraph conformality. This is a pre-existing acyclic database/CSP concept, not a newly coined property.

## G1. Exact universal realization theorem under α-acyclic triplet scopes

**Theorem G1 (classical join-tree/order-amalgamation transport).** If H is a finite 3-uniform α-acyclic hypergraph of distinct triples on V, **no extra edit prerequisite P is imposed**, and all one-shot edit permutations are permitted, then *every* assignment \(y:E(H)\to\{0,1\}\) of triple right answers is simultaneously realized by one legal full source edit order π:

\[
H\ \alpha\text{-acyclic}\quad\Longrightarrow\quad
\forall y\in\{0,1\}^{E(H)}\;\exists\pi\in S_V:\;
t_e(\pi)=y_e\quad(\forall e\in E(H)).
\]

**Constructive proof.** Root a join tree. Choose any local cyclic/linear order of the root triple realizing its one-bit sign. Attach each child triple in parent-first order. By running intersection, its intersection with ALL previously attached edit vertices is exactly its intersection S with its parent. Since different 3-element hyperedges cannot include one another, the child introduces at least one new edit and \(|S|\le2\). A desired triple cyclic orientation can always be realized by inserting these new edits into the existing cyclic order while preserving the relative ordering of S and all previously placed vertices:
- |S|=0: insert the 3 new edits in an orientation that has the desired parity.
- |S|=1: insert the 2 new edits on the circle on the correct side of the shared vertex.
- |S|=2: insert the one new edit in the correct arc between the two shared vertices.
By induction no earlier triple parity changes. Add any unmentioned isolated edits arbitrarily. This produces a complete legal order with every requested right value.

**Sharp memory corollary (within the declared model):**
\[
N_H=2^{|E(H)|},\qquad M_H=|E(H)|\text{ bits}.
\]
All |H| rights bits are genuinely independently realizable, and each has its own future distinguishing query. Because each edge of an α-acyclic triple hypergraph after the first contributes at least one previously unseen edit, \(|E(H)|\le n-2\) for nonempty H. **Neither result is a new graph/CSP theorem**; the corollary transfers established join-tree gluing to a precisely specified repair-right language.

**Constructive program proof court:** [P39 Math-G code](../../tools/p39-math-g/hypergraph_gluing_and_shattering_court.py) *constructs* a legal full edit order for every sign assignment of every α-acyclic 3-uniform hypergraph with up to five vertices, rather than checking mere cardinalities.

## G2. Exhaustive small-hypergraph census and the converse counterexamples

For all simple 3-uniform hypergraphs on n≤5 labeled source edits (n=5 has 2^C(5,3)=**1,024** distinct hypergraphs), the checker compares **two independent** α-acyclic recognition methods: GYO reduction versus primal chordality PLUS conformality. Independently, it enumerates every anchored circular edit order to count all realizable future permission patterns.

| source edit vertices n | total 3-uniform hypergraphs | α-acyclic and every sign realized | α-cyclic but every sign realized | α-cyclic with some sign impossible |
| --- | ---: | ---: | ---: | ---: |
| 3 | 2 | 2 | 0 | 0 |
| 4 | 16 | 11 | 0 | 5 |
| 5 | 1,024 | 126 | **40** | **858** |

Thus **acyclicity is sufficient, not necessary**. An original exact 5-vertex α-cyclic-but-universally-realizable witness from the exhaustive finite scan is H={014,023,123}. All 8 right-value patterns are realizable although the hypergraph fails the GYO/join-tree test. It is therefore unsound to equate "cyclic owner interaction" with "some future owner combination impossible."

**Boundaries:** the counts are exhaustive only at the stated n and model, not prevalence in real maintained repositories. They are not 1,024 separate Go projects. No full universal characterization of arbitrary 3-uniform "shattered" hypergraphs has been proved.

## G3. A strong source invariant falsifies the naive unrestricted G1 corollary

Let V={0,1,2,3}, owner-triple scopes H={012,013}, and original source authorization/safety precedence P be

\[
0<2,\quad 1<2,\quad 0<3,\quad 1<3.
\]

The triple owner interaction H **is α-acyclic**, and the AUGMENTED hypergraph containing all four binary P scopes is still α-acyclic, since every binary scope lies inside one triple scope.

Legal source-edit orders respecting P are EXACTLY
\[
0123,\quad 0132,\quad 1023,\quad 1032.
\]

Their two triple right profiles are only \((0,0)\) or \((1,1)\). Each owner on its own can demand either 0 or 1, but their joint opposite demand \((0,1)\) is impossible—even with an α-acyclic combined constraint hypergraph.

**The precise failing separator:** the two triple scopes share the source edit separator \(\{0,1\}\). The locally feasible order under site 012 and sign 0 requires \(0<1\); the locally feasible order under 013 and sign 1 requires \(1<0\). These are incompatible restrictions on THE SAME source edit pair. Every local factor is nonempty, but their projections onto the shared separator have **empty intersection**.

This refutes the stronger but tempting rule **"α-acyclic source-owner constraints + individual owner satisfiability ⇒ global safe source repair"**. The correct condition is separator-message compatibility, NOT mere nonempty local options or H's acyclicity.

## G4. Exact join-tree repair-gluing theorem WITH source invariants

Let \(\mathcal C\) be the *combined* constraint scope hypergraph encompassing **every ternary future owner relation and every source-invariant/permission constraint that must hold** (plus any binary prerequisite scopes). Suppose \(\mathcal C\) is α-acyclic and a join tree T is given. For each hyperedge scope S let \(R_S\subseteq\operatorname{Sym}(S)\) be the set of **locally admissible total relative source-edit orders**, combining all constraints whose variables lie entirely in S. For each adjacent join-tree edge S--S', let separator \(D=S\cap S'\).

**Theorem G4 (classical join-tree CSP exactness):**

\[
\boxed{\begin{array}{c}
\exists\text{ one global source edit order satisfying every owner and safety constraint}\\
\iff\\
\exists(\rho_S\in R_S)_{S\in T}\;
\forall (S,S')\in T,\
\rho_S|_D=\rho_{S'}|_D.
\end{array}}
\]

**Proof:** a global order projects to pairwise compatible orders on every scope. Conversely, choose a compatible tuple along the join tree, root it and amalgamate child orders into the existing global order. Running intersection ensures the child's previously placed source vertices lie precisely in its separator with the parent; separator agreement lets us insert all new edits without changing existing relative orders. Thus all local source/owner invariants are preserved.

**Algorithmic consequence:** on a join tree, bottom-up message passing (the allowed orders of each separator that have a consistent extension to the subtree) decides existence and constructs a global edit sequence. If \(\max|S|=w\), then each local table has at most w! relative orders; for **fixed w≤3** this yields linear-size message processing (O(number of scopes + n), given the join tree and precomputed local tables). This is **Yannakakis' classical acyclic-database/junction-tree constraint propagation**, not a newly invented source-repair algorithm. The algorithm does not confer missing real maintainer approval rights.

**Scope limitation:** a persistent global source invariant that cannot be factored into the declared bounded local scopes can destroy α-acyclicity after it is modeled correctly or require larger scopes. Claiming this fast algorithm for unrestricted legal source edits would be unsound.

## G5. Exact independent higher-order *shattering capacity* at n=3,…,6 — mathematical candidate beyond α-acyclicity

Define the ternary future-right shattering rank
\[
d_3(n)=\max_{H\subseteq{V\choose3}}\Bigl\{|H|:\ \forall y\in\{0,1\}^{H}\ \exists\pi\in S_V,\ t_H(\pi)=y\Bigr\}.
\]
This is the usual **shattering/VC dimension of the finite concept class of cyclic orders** when the “data points” are named triples and their 0/1 labels are cyclic relative orientations. It is a defined mathematical quantity, **not** the everyday VC dimension of a hypergraph's vertex-subset family.

The information upper bound follows from Math-F: n! linear orders identify in cyclic classes of size n, hence at most (n−1)! different sign vectors:
\[
d_3(n)\le\Big\lfloor\log_2((n-1)!)\Big\rfloor.
\]

**Theorem G5 (EXACT for the stated four sizes):**
\[
\boxed{d_3(3)=1,\quad d_3(4)=2,\quad d_3(5)=4,\quad d_3(6)=6.}
\]
At every one of these sizes the elementary cyclic-order information bound is **achieved** by a constructive finite 3-uniform query witness:

| n | independently shattered triples H | \(|H|\) | distinct witnessed signatures | total possible cyclic orders |
| --- | --- | ---: | ---: | ---: |
| 3 | 012 | 1 | 2 | 2 |
| 4 | 012,013 | 2 | 4 | 6 |
| 5 | 012,013,014,234 | **4** | **16** | 24 |
| 6 | 012,013,045,145,234,235 | **6** | **64** | 120 |

**Proof:** the upper bounds are 1,2,4,6 because 2^{d_3(n)}≤(n−1)!. For each lower bound, the specified H forms a witness: enumerate circular-order representatives with edit 0 first and collect \((t_e(\pi))_{e\in H}\). The [independent reproducible checker](../../tools/p39-math-g/hypergraph_gluing_and_shattering_court.py) verifies **all 2^{|H|} label patterns** have an actual edit-order witness. This constitutes a **finite, auditable mathematical existence proof with explicit testable certificates** at n=3,4,5,6; it is NOT a proof that the information upper bound is attained for n≥7.

The n=5 witness shatters 4 triples while any α-acyclic n=5 triple hypergraph has at most n−2=3 hyperedges. The n=6 witness shatters 6 while α-acyclic families have at most n−2=4. Thus the α-acyclic safe-approval theorem is a strict sufficient structural class and misses **other fully flexible source-owner systems**.

**Novelty status:** Unlike G1/G4, which reduce directly to established join-tree/CSP theory, the project-specific \(d_3(n)\) rank and exact values 3..6 are **a potentially worthwhile combinatorial research avenue**, but we have **not established that the rank or four values are absent from prior cyclic-order shattering/VC literature**. The original 1977 NP-completeness of general cyclic ordering and later 1989/2003 cyclic-order research are strong competitors. The bound for n≥7 is OPEN in this project; DO NOT infer \(d_3(n)=\lfloor\log_2((n-1)!)\rfloor\) for every n from four finite cases.

## G6. Hosted finite verification receipt

[Read-only GitHub Actions #38038051805](https://github.com/WhoSia/EvoNOMOS/actions/runs/38038051805) **SUCCESS** on checked code/workflow HEAD \`75677f45e3d20e9ead40a160bd8f86cecaa54aee\`. It separately used GYO and primal chordal+conformal recognition, direct anchored permutation projections, explicit constructive join-tree assembly, n≤5 hypergraph census and n≤6 shattering witnesses. Artifact \`11663749048\`, SHA-256 \`b871890be890f46a99e34cdf903d7ee3d064345f27e78601642d7158b22921ae\`.

**Stronger follow-on verification:** [GitHub Actions #38038118306](https://github.com/WhoSia/EvoNOMOS/actions/runs/38038118306) runs the subsequently updated checker HEAD \`146aa109298badcfb8ef4da89b85dfc28049f587\`, which additionally asserts the **opposite separator orders** in G3 rather than inferring failure only from missing final profiles. Record its actual final conclusion/artifact only after a readback. No external Go modules compiled.

## G7. Strongest direct mathematical competitors and verdict

- [Yannakakis (1981), *Algorithms for Acyclic Database Schemes*](https://www.vldb.org/dblp/db/conf/vldb/Yannakakis81.html) — classic α-acyclic hypergraph join-tree and semijoin global compatibility. G1 and G4 are **classical transports**.
- [Galil & Megiddo (1977), *Cyclic ordering is NP-complete*](https://doi.org/10.1016/0304-3975(77)90005-6) — generic sparse ternary cyclic-owner order extension is already NP-complete. Do not universalize G4 to arbitrary sparse owner policies.
- [Fiorini & Fishburn (2003), *Extendability of Cyclic Orders*](https://doi.org/10.1023/B:ORDE.0000009252.21331.22) — restricted classes of extensible cyclic orders; original full text not claimed ingested.
- [García-Colín, Montejano, Montejano & Oliveros, *Transitive Oriented 3-Hypergraphs of Cyclic Orders*](https://arxiv.org/abs/1210.6828) — strong direct predecessor on 3-hypergraph cyclic orders and extendability.
- [Ramassamy (2018), *Extensions of Partial Cyclic Orders, Euler Numbers and Multidimensional Boustrophedons*](https://doi.org/10.37236/7145) — enumerations of restricted cyclic orders, including consecutive triples.
- Standard database α-acyclicity, conformality/chordality, GYO reduction, join trees, constraint-semijoin and combinatorial shattering/VC dimension. Need **full prior-art reading** before any priority claim on G5.
- **Neither owner rights nor source invariants were imported from original Go**. The mathematical model may fail as a real software law until independent source and authority evidence is established.

**P39-MATH-G VERDICT:** structural restriction produces a sharp **positive local-to-global theorem**, invariant coupling exposes a minimal **negative separator-order counterexample**, and exact cyclic-query shattering for n≤6 exceeds the α-acyclic sufficient class. G1/G4 are classical; G5's broader mathematical priority is **OPEN/HOLD**, not “discovered novel law.” P39 remains OPEN, DIP49 IDENTIFICATION HOLD, LAW-R2 NOT_AUTHORIZED.

## G8. Next math gate, not automatic stage creation

Continue to **P39-MATH-H (proposed only)** if the user wishes: attack d_3(7) and a nontrivial general lower/upper bound with independently checkable certificates; investigate forbidden subhypergraph characterizations of cyclic-order shattering; derive when physically meaningful source-invariant constraints preserve a tight projection/gluing theorem. Do not substitute empirical leaderboard benchmarks or relabel standard database/CSP theory as independent math.
