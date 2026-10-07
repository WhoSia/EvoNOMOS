# LAW-R1-P30 Mathematical Dossier — Fiber Sufficiency, Prospective Refinement and State-Collision Geometry

## 0. Authority and scope

This dossier is frozen after P29 administrative closure and before any P30 fresh candidate outcome is inspected.

P29 remains authoritative at its tested grain: implementation-route loss can preserve the public action while the repaired action-level quotient remains fixed. P30 does not reopen that result. P30 asks a strictly stronger question: whether the repaired observable state itself is sufficient for the public action.

Let

\[
Z=(Q,R,G):\Omega\to\mathcal Z,\qquad Y:\Omega\to\mathcal Y
\]

on a prospectively declared admissible interventional support \(\Omega_I\subseteq\Omega\). G may be vector-valued.

The core hypothesis is deterministic factorization:

\[
\mathbf{H}_{\mathrm{suff}}:\quad \exists f:\operatorname{im}(Z)\to\mathcal Y\text{ such that }Y=f\circ Z.
\]

This is a statement about fibers, not about coordinate names.

## 1. Fiber-factorization criterion

Define equivalence relations on \(\Omega_I\):

\[
s\sim_Z t\iff Z(s)=Z(t),\qquad s\sim_Y t\iff Y(s)=Y(t).
\]

### Theorem 1 — Exact factorization criterion

The following are equivalent:

1. there exists \(f\) on \(\operatorname{im}(Z)\) such that \(Y=f\circ Z\);
2. every \(Z\)-fiber is \(Y\)-homogeneous;
3. \(\ker Z\subseteq \ker Y\), where kernels are understood as the induced equivalence relations.

### Proof

If \(Y=f\circ Z\), then \(Z(s)=Z(t)\) implies \(Y(s)=f(Z(s))=f(Z(t))=Y(t)\), so every \(Z\)-fiber is \(Y\)-homogeneous.

Conversely, if every \(Z\)-fiber is \(Y\)-homogeneous, define \(f(z)=Y(s)\) for any \(s\) with \(Z(s)=z\). Homogeneity makes this definition independent of the representative. Then \(Y=f\circ Z\).

Thus one exact pair

\[
Z(s_1)=Z(s_2),\qquad Y(s_1)\neq Y(s_2)
\]

is a complete logical falsifier of deterministic sufficiency on the declared support.

## 2. What one collision does and does not prove

A valid same-Z/different-Y witness proves

\[
\neg\mathbf{H}_{\mathrm{suff}}
\]

for the frozen observable map \(Z\) at the adjudication grain.

It does not prove:

- that no finer observable state can restore sufficiency;
- that no finite-dimensional state representation exists;
- that an unobserved variable is metaphysically necessary;
- that LAW-R2 is true;
- that a candidate-specific implementation detail deserves promotion into the state ontology.

Therefore P30 separates factorization failure from ontology impossibility.

## 3. Finite-sample non-certification theorem

Suppose only a strict subset \(S\subsetneq\Omega_I\) has been observed and no collision appears on \(S\).

### Proposition 2 — Absence of observed collision is not global proof

Without an additional coverage theorem, structural restriction, or exhaustive finite support, collision-free observation on \(S\) does not imply \(\mathbf{H}_{\mathrm{suff}}\) on \(\Omega_I\).

### Construction

Take any unobserved \(u,v\in\Omega_I\setminus S\). Extend \(Z,Y\) so that all observed points preserve the collision-free record while \(Z(u)=Z(v)\) and \(Y(u)\neq Y(v)\). The observed data are unchanged, but global sufficiency fails.

Hence a negative P30 search can authorize only bounded survival relative to the searched support, not universal sufficiency.

## 4. Prospective hidden-coordinate refinement

Let \(\mathcal A_0\) denote the prospectively frozen family of outcome-independent observables admissible before candidate \(Y\) is inspected.

A hidden-coordinate rescue is a map

\[
H:\Omega_I\to\mathcal H,\qquad H\in\mathcal A_0
\]

such that

\[
Z'=(Z,H)
\]

satisfies

\[
\ker Z'\subseteq\ker Y.
\]

This is a legitimate state refinement.

### Forbidden retrospective repair

The formal refinement \(H=Y\) always makes \((Z,H)\) sufficient, as does any injective state identifier. These are scientifically vacuous because they encode the outcome or identity directly.

More generally, the coarsest retrospective partition that repairs \(Z\) can be constructed from the common refinement of the \(Z\)-partition and the \(Y\)-partition. Because that construction uses \(Y\), it is not admissible evidence for a prospectively valid ontology.

P30 therefore distinguishes mathematical existence of a refinement from prospective scientific admissibility of a refinement.

## 5. Quotient comparison and nonuniqueness

A quotient coordinate is identified extensionally by the partition it induces on reachable states.

For maps \(Z_1,Z_2\), write

\[
Z_1\equiv_{\mathrm{fib}} Z_2
\]

when

\[
Z_1(s)=Z_1(t)\iff Z_2(s)=Z_2(t)
\]

for every reachable \(s,t\).

### Proposition 3 — Coordinate syntax is not ontology

If \(Z_1\equiv_{\mathrm{fib}} Z_2\), then the two quotients differ only by a bijection between their reachable images. They have identical deterministic sufficiency content.

Thus cross-mechanism quotient nonuniqueness is scientifically meaningful only when the induced partitions or interventional response structure differ, not merely when variable names, encodings, or backend-specific representations differ.

### Incomparable sufficient refinements

Two admissible refinements may both be sufficient yet induce incomparable partitions under the refinement order. Therefore P30 does not assume a unique minimal hidden coordinate. It asks whether a stable, prospectively interpretable refinement exists and transports.

## 6. Structured-gate residualization

Let a coarse gate \(G_c\) be refined prospectively into

\[
G_*=(g_1,\dots,g_m)
\]

through direct component measurements independent of \(Y\).

If an apparent collision satisfies

\[
(Q,R,G_c)(s_1)=(Q,R,G_c)(s_2),\quad Y(s_1)\neq Y(s_2)
\]

but

\[
(Q,R,G_*)(s_1)\neq(Q,R,G_*)(s_2),
\]

then the coarse-state collision is resolved by gate under-resolution. It falsifies the scalar/coarse \(G_c\) representation, not the refined state.

If instead

\[
(Q,R,G_*)(s_1)=(Q,R,G_*)(s_2),\quad Y(s_1)\neq Y(s_2),
\]

the collision survives structured-gate residualization and becomes stronger evidence against the repaired state.

## 7. Intervention signatures and minimal separating bases

For a finite intervention family

\[
\mathcal I=\{I_1,\dots,I_n\},
\]

define the response signature of state \(s\) under a subset \(J\subseteq\{1,\dots,n\}\) by

\[
\Sigma_J(s)=\big((Z,Y)(I_j(s))\big)_{j\in J}.
\]

A subset \(J\) is rival-separating if every pair of prospectively declared rival explanations that make different predictions is distinguished by at least one \(I_j\), \(j\in J\).

For each intervention \(I_j\), let \(D_j\) be the set of rival pairs it distinguishes. Then the minimum rival-separating intervention basis is exactly the minimum set-cover problem on the universe of rival pairs with sets \(D_j\).

Consequences:

- one exact fiber collision is logically sufficient to falsify deterministic factorization;
- more interventions are generally required to localize why the collision occurred;
- minimal localization is combinatorial and may have multiple equally small bases;
- P30 may solve bounded finite instances exactly without claiming a universal closed-form basis.

## 8. Observational equivalence breaking

Two mechanism states are observationally equivalent under the passive map \(Z\) when they share a \(Z\)-fiber. Interventions break that equivalence when their response signatures differ.

P30 therefore distinguishes:

1. passive equivalence;
2. equivalence under the frozen intervention family;
3. action equivalence.

A repaired ontology is stronger when its fibers remain action-homogeneous after interventions explicitly selected to break plausible hidden equivalences.

## 9. Stochastic extension

If repeated trials show irreducible stochasticity, deterministic \(Y(s)\) is replaced by a conditional response law

\[
\mathsf P_s(Y\in\cdot).
\]

Distributional sufficiency requires equal response distributions within each matched \(Z\)-fiber at the frozen tolerance and test regime.

A one-off discordant trial is not a deterministic state collision when stochasticity is admitted. P30 must either establish deterministic repeatability at the declared grain or predeclare a distributional comparison and error criterion before adjudication.

## 10. Escalation ladder

### Level 0 — survival

No admissible collision is found on searched support. Repaired sufficiency survives only on that support.

### Level 1 — apparent collision

A same-coarse-state/different-Y contrast appears but is resolved by measurement, route, environment, oracle, timing, or structured-G refinement.

### Level 2 — exact frozen-state collision

A prospectively frozen exact \(Z\)-fiber contains different \(Y\). Deterministic sufficiency of \(Z\) is falsified at that grain.

### Level 3 — admissible hidden-coordinate rescue

A predeclared \(H\in\mathcal A_0\) restores fiber homogeneity. The result is ontology refinement, not LAW-R2.

### Level 4 — persistent prospective refinement failure

Exact collisions persist after predeclared structured-G and admissible-H refinements and replicate independently. This may establish LAW_R2_PRESSURE_ESTABLISHED.

P30 itself does not authorize LAW-R2. A later entry gate must decide whether the surviving failure warrants a new law layer.

## 11. Claim ceiling

P30 can establish any of the following, if directly supported:

- bounded survival of repaired-state sufficiency;
- failure of a coarse measurement map;
- structured-gate under-resolution;
- necessity of one prospectively admissible additional coordinate on tested support;
- exact failure of deterministic repaired-state sufficiency at a frozen grain;
- replicated pressure against the current finite repaired ontology.

P30 cannot prove from finite software experiments that no possible finite ontology exists. It cannot promote LAW-R2, macro law, SOLID derivation, manuscript authority, or a universal latent-state impossibility theorem.
