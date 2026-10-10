# P39-MATH-H — Exact Seven-Edit Ternary Shattering, Two-Vertex Amalgamation and an Improved Infinite Lower Bound

**2026-10-10 KST · USER-AUTHORIZED P39-MATH-H COMPLETE IN MATHEMATICAL MODEL · P40 PROPOSAL TO FOLLOW, NOT OPEN · NEW MATH PRIORITY UNVERIFIED · DIP49 HOLD / LAW-R2 NOT_AUTHORIZED.**

[Mathematical predecessor P39-MATH-G](P39_MATH_G_ACYCLIC_HYPERGRAPH_GLUING_INVARIANT_SEPARATORS_AND_SHATTERING.md) established α-acyclic triple rights, a shared-separator failure when source prefix invariants are added, and a 6-vertex/6-triple fully shattered witness. Math-H attacks exact d3(7) and the structural growth mechanism instead of replacing science with paper/output metrics.

## H0. Mathematical semantics and the scope of every theorem

A finite source event set V has n distinct physically commuting **one-shot** edits. Unless an invariant is separately declared, all n! edit permutations are legal and create exactly the same fully installed source. A named future owner query q_{ijk} for i<j<k reports whether the induced permutation of the three edits has odd parity. Formally, with ranks rπ:

\[
t_{ijk}(\pi)=[r_\pi(i)>r_\pi(j)]\oplus[r_\pi(i)>r_\pi(k)]\oplus[r_\pi(j)>r_\pi(k)].
\]

A family H⊆\(\binom V3\) is **shattered** iff \(\{t_H(\pi):\pi\in S_V\}=\{0,1\}^H\). The ternary shattering rank d3(n) is max |H| among shattered H. Cyclic rotation of π preserves every triple parity, hence it suffices to examine (n−1)! orders with 0 first. At fixed complete source snapshot, the |H| genuinely independent separately queryable future rights have exactly 2^|H| residuals / |H| extra fixed-length bits; that is classical Myhill–Nerode, NOT the size of a full source-history automaton.

**Nothing in these synthetic permission rules certifies a real Go repository's actual owner approval, LSP compliance or source compatibility.** Original Go and real ecosystem experiments remain outside this step.

## H1. Exact d3(7)=7 — complete finite combinatorial certificate

**Theorem H1:**
\[
\boxed{d_3(7)=7.}
\]

**Explicit constructive lower witness** (the triplets in ascending order):
\[
H_*=\{012,013,014,015,016,234,256\}.
\]
Enumerate every anchored seven-edit circular order \((0,\pi(1),\ldots,\pi(6))\), of which 6!=720. Their projections to H_* realize all **128** binary seven-question signatures. An independent Python checker verifies this witness.

**Exhaustive upper certificate (algorithmic proof with defined full search universe):** There are C(7,3)=35 ternary question candidates, ordered lexicographically. Start from empty H. For each currently shattered k-question subset and every lexicographically later candidate e, compute the (k+1)-bit signatures of all 720 anchored cyclic orders; recursively retain H∪{e} **iff all 2^(k+1) signatures occur**. Every shattered family has every subfamily shattered, so no potential shattered 8-family can be skipped by this pruning. Every k-element question set has exactly one increasing enumeration, so no set is duplicated.

**FULL f-vector of the seven-edit ternary shattering simplicial complex**, independently reproduced:
| k queries | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Shattered k-subfamilies of 35 triplets | 1 | 35 | 595 | 6,405 | 46,410 | 204,246 | 274,890 | **39,930** | **0** |

Because there is no shattered 8-family, no shattered family larger than eight exists by downward closure.

**Independent second upper check (not merely repeating DFS histogram):** For ALL 39,930 shattered seven-family H, construct 128 **bitsets of source histories** from the original 720 permutation rows, one for each H-answer signature. For each of all 28 omitted triples e, test whether BOTH e-sign alternatives appear within EACH of the 128 buckets. None of
\[
39,930\times28=\boxed{1,118,040}
\]
seven-to-eight extension attempts succeeds. This uses explicit bitset intersection rather than the DFS's array-of-profiles test. The agreement is a *reproducible finite exhaustive proof certificate*, not a hand proof reducing it to a short prior graph theorem.

[Complete independent C++ upper-certificate source](../../tools/p39-math-h/exact_d3_7_exhaustive.cpp), compiled with \`g++ -std=c++17 -O3\`; [independent Python positive witness and structural checker](../../tools/p39-math-h/two_anchor_gluing_verifier.py). Both locally run. The new **GitHub Actions workflow write was blocked**, so **NO P39-H hosted CI success is claimed**. Previous P39-G hosted CI #38038339518 is a different checker, not an H-run.

### Finite-obstruction local upper transfer

Every restriction of a shattered family to fewer vertices is shattered. Thus the exact H1 n=7 cap is inherited on every seven-vertex subset of an n-vertex H. Double-count all incidences (e,S) with |e|=3, |S|=7, e⊆S. Each triple occurs in C(n−3,4) seven-vertex sets and every such set contains at most seven H edges, so:
\[
|H|\binom{n-3}{4}\le7\binom n7.
\]
Therefore
\[
\boxed{d_3(n)\le\left\lfloor\frac{7}{35}\binom n3\right\rfloor
=\left\lfloor\frac15\binom n3\right\rfloor,\qquad n\ge7.}
\]
For n=8 this yields d3(8)≤11, improving the raw cyclic order cardinality cap floor(log₂(7!))=12. For growing n, the information-theoretic (n−1)! bound is eventually stronger; do NOT market the density bound as an asymptotic solution.

## H2. Two-common-source-vertex circular-order amalgamation

**Theorem H2 (amalgamation).** Suppose H_A and H_B are two shattered ternary question families over edit sets A and B with |A∩B|≤2 and with **no cross-family triple questions**. Then their union H_A∪H_B is shattered on A∪B.

**Proof:** Choose independently for any prescribed binary answers a circular order of A satisfying H_A and one of B satisfying H_B. If A,B are disjoint, concatenate; if they share exactly one edit, rotate both circles to place that edit first and concatenate their remaining parts. If they share exactly **two** source edits a,b, rotate both to place a first; write each as a, U_j, b, W_j. Combine them into the circular order a,U_A,U_B,b,W_A,W_B. Restricting the resulting circle to A (resp. B) reproduces EXACTLY its original circular order and hence every ternary parity. Thus every combined rights assignment has a realizing one-shot source edit order. This is a clean extension of the one-anchor G9 construction. This is classical circular-order amalgamation mathematics; its priority as a theorem about the project-defined d3 is **not established**.

**Corollary H2a (shifted superadditivity):** For p,q≥3, relabel optimal shattered witnesses to overlap on exactly two edits. Then:
\[
\boxed{d_3(p+q-2)\ge d_3(p)+d_3(q).}
\]
In particular f(k)=d3(k+2) is superadditive for k≥1. This does NOT imply all possible joins along three common vertices are valid: a shared triple has two different cyclic orientations and may be forced inconsistently.

## H3. Stronger all-n construction — six independent triple queries per four new edits

Take the Math-G shattered six-edit, six-question seed
\[
H_6=\{012,013,045,145,234,235\}
\]
with 64 verified realizable rights signatures. For n≥6 let n−2=4k+r, k≥1, 0≤r≤3. Glue k disjoint renamed copies of H_6 sharing BOTH edits 0,1; every copy adds four new edit vertices and six independently selectable rights questions. For each of the remaining r new vertices z, add one query {0,1,z}; placing z in either of the two circular arcs between 0 and 1 lets its answer be chosen independently without altering prior signs.

**Theorem H3 (improved general lower):**
\[
\boxed{
d_3(n)\ge6k+r
=n-2+2\left\lfloor\frac{n-2}{4}\right\rfloor,\qquad n\ge6.
}
\]

This strengthens G9's \(n-1+\lfloor(n-1)/5\rfloor\) bound, especially for n≥10, and has a **valid arbitrary-n structural proof**. Python independently enumerates all possible 2^(6k+r) assignments and actually produces a witnessing full edit sequence for each n=6,…,12, including 16,384 different signatures at n=12.

| n | old G9 lower | new H3 lower |
| --- | ---: | ---: |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | 10 | **12** |
| 11 | 12 | **13** |
| 12 | 13 | **14** |

**Strong qualification:** These are lower bounds for the exact declared ternary-query shattering capacity, not statements about arbitrary owner permissions. The gluing is rooted in classical circular-order representations; whether the *specific H3 inequality* is genuinely a previously unknown bound must be determined from original cyclic-order/permutation VC literature. Until then PRIORITY HOLD.

## H4. Anchor-star family: a precise forest if-and-only-if theorem

Fix a reference source edit 0 and let H={ {0,i,j} : {i,j}∈E(G)} for a simple graph G on the remaining n−1 edits.

**Theorem H4:**
\[
\boxed{H\text{ shattered}\iff G\text{ is a forest}.}
\]

**Proof:** Rotate all edit histories to put 0 first. The triple bit t_{0ij} now records precisely the relative linear order of i,j. All 2^m assignments of pair directions are realizable by a total order **iff every orientation of G is acyclic**. If G is a forest, every orientation is acyclic and extends to a topological linear order. If G contains an undirected cycle, orient that cycle consistently to create a directed cycle, whose required comparisons cannot be realized by any total order. This is a classical directed graph/poset equivalence, not a novel theorem.

The Python checker independently traverses **every graph** on n−1=3,4,5 nonanchor edits: 8,64,1,024 graphs, with corresponding exact forest counts **7,38,291**, and checks all candidate question assignments against all (n−1)! anchored source-edit permutations.

**Consequences:** In the anchor-star class the largest shattered family has n−2 triples and its minimal non-shattering forbidden patterns are ordinary undirected cycles, while the unrestricted cyclic-order class has larger shattered H (already d3(6)=6>4). Therefore "all higher-order owner obstructions are just precedence cycles" is false as a universal full-model **classification**; it holds for this explicit restricted subclass.

## H5. Strongest classical-theory / original-paper priority court

1. [García-Colín et al. (2013), *Transitive Oriented 3-Hypergraphs of Cyclic Orders*](https://arxiv.org/abs/1210.6828) studies partial cyclic-order realizability and 3-hypergraph transitivity; related but does not automatically establish H1's exact rank count.
2. [Johnson & Wickes (2021/2023), *Shattering k-Sets with Permutations*](https://arxiv.org/abs/2112.01946) uses **a family of permutations** to shatter **k-element subsets of edits** in all k! orders; this is NOT the same quantifier structure as selecting independently labelled ternary *queries* and requiring one total order for every joint query-label vector. Do not conflate these problems.
3. [Raz (2000), *VC-dimension of Sets of Permutations*](https://doi.org/10.1007/s004930070023) defines VC dimension of a **chosen subset of permutations** via their restrictions to selected vertex sets; again different from VC dimension of the *concept class of all cyclic orders acting on triple-query coordinates*. 
4. [Stanley (1973), *Acyclic Orientations of Graphs*](https://doi.org/10.1016/0012-365X(73)90108-8) already identifies the edge-relative-order quotient (Math-E); H4 directly reduces to it, but **H3's nonanchor ternary amalgamation is not simply the exact same pairwise orientation count**.
5. [Fiorini & Fishburn (2003), *Extendability of Cyclic Orders*](https://doi.org/10.1023/B:ORDE.0000009252.21331.22), [Galil & Megiddo (1977), *Cyclic Ordering Is NP-Complete*](https://doi.org/10.1016/0304-3975(77)90005-6): strong older competitors, especially for nonshattered hypergraph constraints.
6. Cyclic orders are a classical relational structure. H2 gluing is a natural Fraïssé-style amalgamation property at overlap of two, and H1 exact finite proof is computational. **Claim neither pure mathematical originality nor an actual software architecture law without a deeper original-paper audit.**

**Prior-art retrieval limitation:** Public titles and abstracts and some accessible article text were inspected. No comprehensive full-paper priority determination for d3(7), H2 or H3 has been made; do not infer novelty from missing results in a keyword search.

## H6. Reproducibility receipts and experimental exclusions

- Locally compiled and ran the exhaustive seven-edit C++ combinatorial search (pure mathematical model); 720 anchored orders, 35 candidate ternary rights, 39,930 shattered seven-query families, NO shattered eight-query family. Second independent bitset test attempts all **1,118,040** seven-to-eight extensions and finds none.
- Locally ran a Python explicit two-anchor construction and checked all 2^m labels for n=6,…,12; n12 m14 has **16,384** witness orders; the final submitted Python source also checks anchor-star forests and independently validates the seven-query witness.
- New read-only GitHub Actions workflow creation was attempted and **blocked by a tool write gate**. Previous [Math-G CI #38038339518](https://github.com/WhoSia/EvoNOMOS/actions/runs/38038339518) SUCCESS validates only the Math-G code. **NO HOSTED P39-MATH-H CI PASS or original Go execution can be claimed**. GitHub-hosted source is committed, and both mathematical verifier scripts can be rerun via documented Python/C++ commands.

**Scientific verdict:** d3(7)=7 exactly with a complete finite calculation certificate; two-anchor amalgamation H2 and all-n stronger constructive lower H3 proved; anchored forest characterization H4 proved. These are genuine theorems IN THE SPECIFIED MATHEMATICAL MODEL, with strong classical connections and **independent novelty PRIORITY HOLD**. No law beyond historical source semantics has been identified.

**Status:** P39 OPEN, MATH-H VERIFIED LOCALLY, P40 FORMAL NAME PROPOSED ONLY, DIP49 IDENTIFICATION HOLD, LAW-R2 NOT_AUTHORIZED.
