# LAW-R1-P30 Phase II Theorem Supplement — Collision Graphs, Admissible Refinement Complexity and Interventional State Indistinguishability

## 0. Status and non-retroactivity

This supplement is written **after** the first P30 zlib candidate outcome and therefore does not alter, strengthen, weaken, or reinterpret that candidate's frozen confirmatory adjudication.

It governs only later P30 candidates whose outcomes are inspected after the Phase II preseal.

The first zlib candidate is retained as a calibration witness:

- frozen repaired state (Z=(Q,R,G)) matched exactly across the two arms;
- public action (Y) differed;
- prospectively admitted dictionary state (H_{mathrm{dict}}) separated the arms;
- therefore the original (Z) was insufficient at that grain, while one admissible refinement repaired the collision;
- this is **refinement success**, not persistent ontology failure.

Phase II asks a harder question: how complex must a legitimate prospective refinement be, and can two states remain interventionally indistinguishable under the admissible observable/intervention family while still differing in public action?

## 1. Partition formulation

Let (Omega_I) be the finite or finitely sampled adjudication support. For any observable map (A:Omega_I	omathcal A), define the induced equivalence relation

[
ssim_A t iff A(s)=A(t).
]

Write (mathcal P_A) for the corresponding partition.

We use the refinement order

[
mathcal P_A preceq mathcal P_B
]

to mean that (mathcal P_A) is at least as fine as (mathcal P_B): every (A)-class is contained in a (B)-class.

Then deterministic sufficiency is exactly

[
Y=fcirc Z
quadLongleftrightarrowquad
mathcal P_Zpreceq mathcal P_Y.
]

Adding an observable (H) replaces (mathcal P_Z) by the common refinement induced by the joint map ((Z,H)).

The scientifically relevant problem is not whether *some* refinement exists. The retrospective refinement ((Z,Y)) always exists and is vacuous. The problem is whether a refinement exists inside a prospectively frozen admissible observable family.

## 2. Collision graph

For a fixed repaired state map (Z), define the **heterogeneous collision graph**

[
Gamma_Z=(V,E),qquad V=Omega_I,
]

with

[
{s,t}in E
iff
Z(s)=Z(t) 	ext{and} Y(s)
eq Y(t).
]

Thus (E=arnothing) iff (Z) is deterministically sufficient on the adjudicated support.

A candidate hidden observable (H_j) **separates** an edge ({s,t}) when

[
H_j(s)
eq H_j(t).
]

For a prospectively frozen observable family

[
mathcal A_0={H_1,ldots,H_m},
]

let (D_jsubseteq E) be the set of collision edges separated by (H_j).

### Theorem 4 — Prospective rescue as set cover

A subset (Ssubseteq{1,ldots,m}) makes the joint state

[
Z_S=(Z,(H_j)_{jin S})
]

deterministically sufficient on the finite adjudication support iff

[
igcup_{jin S}D_j=E.
]

Therefore the minimum-cardinality prospective hidden-coordinate rescue basis is exactly the minimum set-cover problem on universe (E) with sets (D_1,ldots,D_m).

### Consequence

The bounded minimum-repair problem is NP-hard in general by direct reduction from SET COVER.

This separates three notions that must not be conflated:

1. **logical repairability** — some refinement exists;
2. **prospective admissible repairability** — some subset of (mathcal A_0) repairs all observed collision edges;
3. **simple/stable repairability** — a small interpretable basis repairs and transports.

P30 Phase II treats only (2) and (3) as scientifically informative.

## 3. Unrestricted information lower bound

Within one fixed (Z)-fiber (F_z), let

[
k_z=left|{Y(s):sin F_z}ight|.
]

Any auxiliary label (H) that makes ((Z,H)) sufficient must take at least (k_z) distinguishable joint values across outcome classes inside that fiber.

Hence an unrestricted auxiliary alphabet obeys

[
|operatorname{im}(H)|ge max_z k_z.
]

If (H) is encoded by (b) binary coordinates, necessarily

[
bge
leftlceil
log_2max_z k_z
ightceil.
]

This is only a mathematical lower bound. Constructing (H) from (Y) attains it retrospectively but is scientifically inadmissible. Prospectivity and causal interpretability can make the admissible repair complexity strictly larger.

## 4. Nonuniqueness of minimal repairs

Let (mathfrak R) be the collection of prospectively admissible subsets (S) whose joint observables repair all collision edges.

There need not be a unique inclusion-minimal or cardinality-minimal member of (mathfrak R).

Therefore a successful one-coordinate rescue does not establish a unique ontology. It establishes only that at least one prospectively admissible refinement is sufficient on the tested support.

A stronger claim of **state-coordinate necessity** for (H_j) requires a deletion test:

[
Z_{Ssetminus{j}} 	ext{is insufficient}
]

while (Z_S) is sufficient, under the same support and oracle.

A claim of transportable necessity further requires the analogous deletion property in an independent mechanism or a justified structure-preserving transport map.

## 5. Interventionally enriched state signatures

Passive equality of (Z) is a weak notion of state matching. Let

[
mathcal I_0={I_0=mathrm{id},I_1,ldots,I_n}
]

be the prospectively frozen admissible intervention family.

Define the **interventional observable signature**

[
Phi_{Z,mathcal I_0}(s)
=
ig(
Z(I_0(s)),
Z(I_1(s)),
ldots,
Z(I_n(s))
ig).
]

Two states are **interventionally (Z)-indistinguishable** when

[
Phi_{Z,mathcal I_0}(s)=Phi_{Z,mathcal I_0}(t).
]

This is strictly stronger than passive (Z(s)=Z(t)) whenever the intervention family can expose latent structural differences.

### Definition — Strong state-collision witness

A pair (s,t) is a strong P30 collision when

[
Phi_{Z,mathcal I_0}(s)=Phi_{Z,mathcal I_0}(t)
]

yet

[
Y(s)
eq Y(t),
]

with the common oracle, environment, and stochastic adjudication rules held fixed.

Such a witness defeats not merely passive-state sufficiency but the sufficiency of the entire frozen interventional observable signature.

## 6. Interventionally admissible refinement

For a hidden observable family (H_S), define

[
Phi_{(Z,H_S),mathcal I_0}(s)
=
ig(
(Z,H_S)(I_j(s))
ig)_{j=0}^{n}.
]

A refinement is **interventionally sufficient on tested support** when equality of these signatures implies equality of the public outcome under the frozen adjudication contract.

Phase II therefore distinguishes:

- passive rescue: ((Z,H_S)) separates current collision arms;
- interventional rescue: the enriched signatures remain outcome-homogeneous under the frozen intervention family;
- transportable rescue: the same structural coordinate semantics and separation property survive an independent mechanism mapping.

Only the latter two materially pressure a general ontology claim.

## 7. Dynamic quotient equivalence across mechanisms

Let mechanisms (A,B) have state spaces (Omega_A,Omega_B), intervention families (mathcal I_A,mathcal I_B), repaired maps (Z_A,Z_B), and outcomes (Y_A,Y_B).

A proposed transport consists of:

- a state correspondence (arphi:Omega_A'	oOmega_B') on declared reachable support;
- an image bijection (psi:operatorname{im}(Z_A)	ooperatorname{im}(Z_B));
- an intervention correspondence (	au:mathcal I_A'	omathcal I_B').

Static quotient equivalence requires

[
Z_Bcircarphi=psicirc Z_A.
]

**Dynamic quotient equivalence** additionally requires interventional commutation at the observable level:

[
Z_B(	au(I)(arphi(s)))
=
psi(Z_A(I(s)))
]

for all declared (s,I).

Two quotients can therefore be statically fiber-equivalent yet dynamically nonequivalent. P30 Phase II treats dynamic nonequivalence as genuine cross-mechanism quotient nonuniqueness only when it survives measurement and correspondence audits.

## 8. Stable versus patch-like coordinates

A prospectively admissible rescue coordinate (H) is classified along three axes:

1. **deletion necessity** — removing (H) reintroduces a collision;
2. **interventional stability** — (H)'s semantics remain coherent under the frozen intervention family;
3. **transport stability** — an independently justified analogue preserves its structural role in another mechanism.

A coordinate that succeeds only on one constructed pair without deletion necessity or transport evidence is a **local repair coordinate**, not a promoted ontology primitive.

The zlib dictionary witness currently authorizes local prospective refinement only.

## 9. LAW-R2 pressure criterion — strengthened

For Phase II, passive same-(Z)/different-(Y) is insufficient for LAW-R2 pressure if an admitted refinement repairs it.

The strongest authorized P30 endpoint requires all of:

1. at least one strong interventional collision under (Phi_{Z,mathcal I_0});
2. direct measurement and confound audits passed;
3. all prospectively admitted structured-(G) refinements exhausted or shown irrelevant;
4. no subset of the prospectively frozen admissible observable family repairs the collision on the tested support;
5. replication in an independent mechanism class or a second independent state family;
6. no direct intervention on (Y).

Even this establishes only

[
	exttt{LAW_R2_PRESSURE_ESTABLISHED},
]

not LAW-R2 itself and not impossibility of every finite latent-state ontology.

## 10. Phase II target hierarchy

**Tier 0 — calibration:** exact passive collision with immediate prospective (H) rescue.  
**Tier 1 — minimality:** rescue exists, but deletion tests identify a necessary coordinate basis.  
**Tier 2 — interventional stress:** passive rescue fails to remain sufficient under intervention signatures.  
**Tier 3 — admissible-family exhaustion:** no prospectively frozen observable subset repairs the tested collision graph.  
**Tier 4 — replicated strong collision:** interventional indistinguishability with different (Y) replicates independently.

P30 should not close merely because Tier 0 has been achieved if higher tiers remain feasible within reasonable cost.

## 11. Claim ceiling

This supplement can support:

- exact finite-support repair complexity;
- minimum prospective rescue bases on bounded candidate families;
- deletion necessity of coordinates;
- passive versus interventional sufficiency separation;
- static versus dynamic quotient nonuniqueness;
- replicated pressure against the current observable ontology.

It cannot prove that no finite sufficient state exists, cannot authorize LAW-R2, and cannot promote macro law, SOLID derivation, universal latent-state impossibility, or manuscript authority.
