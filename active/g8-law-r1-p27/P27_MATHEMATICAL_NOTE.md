# P27 Mathematical Note — Non-Nested Rivals and Interventional Kernel Rank

Status: **PRE-FRESH / BINDING**

## 1. Frozen rival signatures

Let a state be summarized by observable tuple

\[
(q,g,y)\in\{0,1\}^3
\]

with \(y=q\land g\) at baseline.

For an intervention \(\tau\), define the signed response vector

\[
\kappa(\tau)=(\Delta q,\Delta g,\Delta y)\in\mathbb Z^3.
\]

### N0 — layer-independent mediation

For an upstream DROP from \(q=g=y=1\),

\[
\kappa_{N0}(D)=(-1,0,-1).
\]

For an upstream RESTORE from \(q=0,g=1,y=0\),

\[
\kappa_{N0}(R)=(+1,0,+1).
\]

For a local-gate DROP from \(1,1,1\),

\[
\kappa_{N0}(G)=(0,-1,-1).
\]

### N1 — cross-coupled control

For upstream DROP from \(1,1,1\),

\[
\kappa_{N1}(D)=(-1,-1,-1).
\]

For upstream RESTORE from \(0,0,0\),

\[
\kappa_{N1}(R)=(+1,+1,+1).
\]

The local-gate DROP remains

\[
(0,-1,-1).
\]

## 2. Proposition A — Non-nestedness

N0 and N1 are non-nested under the frozen intervention typing.

### Proof

For the same typed upstream DROP starting from \(q=g=1\):

- N0 requires \(\Delta g=0\);
- N1 requires \(\Delta g=-1\).

Therefore no realization can satisfy both frozen rival definitions on that intervention. Neither model class contains the other under this intervention semantics.

## 3. Proposition B — One-intervention separating basis

Assume:
1. \(q\) and \(g\) are directly measured, not inferred from \(y\);
2. the upstream DROP is prospectively typed;
3. the initial state is \(q=g=1\).

Then the single intervention

\[
\mathcal I_{\min}=\{D\}
\]

separates N0 and N1 because their predicted \(\Delta g\) values differ.

No empty intervention set can separate two architectures that share the same baseline state. Hence the separator basis has minimum cardinality 1.

RESTORE is therefore a replication/consistency intervention, not logically required for minimal separation.

## 4. Proposition C — Kernel rank under N0

Using ordered interventions \((D,G)\), the N0 response matrix is

\[
K_{N0}=
\begin{bmatrix}
-1&0&-1\\
0&-1&-1
\end{bmatrix}.
\]

Its rank over \(\mathbb Q\) is \(2\).

Interpretation: quotient and gate perturbations expose two independent observable directions.

If RESTORE is added, its vector is the negative of DROP and does not increase rank.

## 5. Proposition D — Kernel rank under N1

For N1, using DROP and local-gate DROP:

\[
K_{N1}=
\begin{bmatrix}
-1&-1&-1\\
0&-1&-1
\end{bmatrix}.
\]

The rank is also \(2\).

Therefore **rank alone does not distinguish N0 from N1**. The orientation of the row space relative to the measured \(q\) and \(g\) coordinates matters.

This prevents a misleading claim that "rank 2" identifies architecture class.

## 6. Proposition E — Rank-3 obstruction to complete mediation

Suppose the deterministic architecture obeys

\[
y=f(q,g)
\]

for a fixed function \(f\), and interventions are evaluated only through their effect on measured \(q,g\).

Then the local differential/finite response of \(y\) is determined by the pair \((\Delta q,\Delta g)\) together with the starting point.

If a frozen intervention family yields three linearly independent response vectors in \((\Delta q,\Delta g,\Delta y)\) while matched starting states make the first two coordinates insufficient to determine the third, then no two-variable complete-mediation model \(y=f(q,g)\) can represent the packet without an additional latent coordinate or intervention-specific rule.

Rank 3 is therefore an obstruction signal, but only when direct q/g measurement and matched-state conditions hold.

## 7. Proposition F — Equivalence under a finite intervention basis

For architecture \(A\), define its kernel over intervention basis \(\mathcal I\) as

\[
K_A^{\mathcal I}=\{\kappa_A(\tau):\tau\in\mathcal I\}.
\]

Define

\[
A\sim_{\mathcal I}B
\]

iff the measured kernels coincide intervention-by-intervention.

This is an equivalence relation.

P27 may identify an architecture only up to the quotient set

\[
\mathcal A / {\sim_{\mathcal I}}.
\]

Increasing the intervention basis refines, never coarsens, this equivalence relation.

## 8. Court rule

- If the fresh measured DROP signature is \((-1,0,-1)\), N0 survives and N1 fails.
- If it is \((-1,-1,-1)\), N1 survives and N0 fails.
- Any other exact signature rejects both frozen rivals and opens the latent-obstruction lane.
- RESTORE checks symmetry/consistency.
- local-gate DROP is a negative control.
