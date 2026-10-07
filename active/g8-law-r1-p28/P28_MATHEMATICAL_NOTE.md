# LAW-R1-P28 Mathematical Note — Exhaustiveness, Obstruction and Kernel Arrangement

## 0. Authority
This note is pre-fresh. It was frozen before any P28 candidate was selected or inspected for outcome.
Parent authority: G8 LAW-R1-P27, lineage head `a3bb659f5d19409dcc9ce938d4d3558855f4bc09`.

## 1. Scalar binary setup
Baseline state is

`B=(q,g,y)=(1,1,1)`.

For an admissible intervention `tau`, define the signed observed kernel

`kappa(tau)=(Delta q,Delta g,Delta y)`.

For `UPSTREAM_DROP`, q is forced from 1 to 0, y is not directly manipulated, and g may either remain 1 or fall to 0. Because y is binary and starts at 1, the complete weak-semantic signature set is exactly

`S_D={(-1,0,-1), (-1,-1,-1), (-1,0,0), (-1,-1,0)}`.

Name the four signatures prospectively:

- `N0=(-1,0,-1)`: layer-independent mediated response.
- `N1=(-1,-1,-1)`: cross-coupled mediated response.
- `X0=(-1,0,0)`: stable-gate bypass/persistence obstruction.
- `X1=(-1,-1,0)`: cross-coupled bypass/persistence obstruction.

X0/X1 are not automatically third architecture families. They are first-class *obstruction signatures* because they falsify at least the q-necessity part of the strong scalar ontology.

## 2. Proposition A — Complete scalar DROP census
Under the baseline, binary coordinates, direct measurement and the typed upstream DROP above, the four signatures in `S_D` are exhaustive.

Proof: `Delta q=-1` is fixed. Since `g' in {0,1}`, `Delta g in {0,-1}`. Since `y' in {0,1}`, `Delta y in {0,-1}`. The Cartesian product therefore has 2x2=4 exact rows and no others.

## 3. Proposition B — Conditional N0/N1 exhaustiveness theorem
Assume the strong scalar mediation axiom:

1. q is necessary for y: `q=0 => y=0` under admissible non-y interventions.
2. g is a genuine necessary local gate: `g=0 => y=0`.
3. q,g,y are directly measured and deterministic at the adjudication grain.

Then, for the typed upstream DROP from `(1,1,1)`, N0 and N1 are exhaustive.

Proof: q necessity fixes `y'=0`, hence `Delta y=-1`. Only g may either stay 1 or fall to 0. These are exactly N0 and N1.

Consequence: within the *strong scalar ontology*, there cannot be a third exact binary upstream-DROP family. A fresh X0/X1 witness would therefore be an ontology failure or semantic reclassification event, not merely an extra label beside N0/N1.

## 4. Proposition C — Weak-semantic obstruction partition
Under weak scalar measurement, N0/N1 and X0/X1 partition all possible upstream-DROP signatures.

- N0/N1 preserve q-necessity.
- X0/X1 violate q-necessity at the measured action grain because q falls to zero while y remains one.
- X0/N0 preserve the local gate under upstream DROP.
- X1/N1 exhibit q-to-g coupling under upstream DROP.

Thus the 2x2 arrangement factors into two independent binary questions at this intervention:

`M = did y fall?`
`C = did g fall?`

N0=(M=1,C=0), N1=(1,1), X0=(0,0), X1=(0,1).

## 5. Proposition D — Singleton separator for the four-row DROP census
If q,g,y are directly measured and all four weak-semantic signatures are admissible, the singleton basis `{UPSTREAM_DROP}` separates N0,N1,X0,X1 because every class has a distinct exact row.

Therefore the minimum separating-basis cardinality for this four-class census is 1; the empty basis cannot separate classes sharing baseline `(1,1,1)`.

This does *not* imply that one DROP separates latent mechanisms that share the same observed row.

## 6. Proposition E — Same-(q,g) action splitting is a direct sufficiency obstruction
Suppose two admissible states or interventions produce the same directly measured `(q,g)` but different y.

Then no deterministic scalar function `y=f(q,g)` can represent both observations.

This is a stronger obstruction to scalar sufficiency than merely observing an unusual kernel row. It forces at least one of:

- omitted/latent state h,
- structured gate state compressed into scalar g,
- history/path dependence,
- stochastic/non-deterministic action at the adjudication grain,
- measurement error or mismatched state.

P28 must adjudicate these alternatives rather than calling all such cases 'latent' by default.

## 7. Proposition F — Rank-3 obstruction needs a third admissible direction
With only `UPSTREAM_DROP` and `LOCAL_GATE_DROP`, the observed kernel matrix has at most two rows and therefore rank at most 2. Exact RESTORE from the matched dropped state is the negative of DROP and cannot increase rank.

A rank-3 observed kernel therefore requires a third admissible intervention direction. The canonical latent-direction form is

`L=(0,0,-1)`

under a non-y intervention that changes action while holding measured q and g fixed.

Then, together with mediated N0-style DROP and gate-DROP,

`(-1,0,-1), (0,-1,-1), (0,0,-1)`

are linearly independent and the observed kernel has rank 3.

Rank 3 is evidence against two-coordinate complete mediation only after excluding direct intervention on y, coordinate mismeasurement and unmatched-state confounding.

## 8. Proposition G — Structured-gate extension creates genuine intermediate families
Let the local gate be a directly measurable vector `G=(g1,...,gm)` with `m>=2`, and let y depend on q and G without hidden state.

Under upstream DROP, any subset of gate coordinates may respond. The coupling support is

`C_D={i : Delta g_i != 0}`.

For m=1, only `C_D=empty` (N0) or `{1}` (N1) exist. For m>=2, partial nonempty proper subsets are possible and constitute genuine coupling families that are neither scalar N0 nor scalar N1 before quotienting G to one bit.

Hence scalar-g exhaustiveness and architecture exhaustiveness are distinct claims. A scalar quotient may collapse partial-coupling families into N1 or hide internal architecture variation.

## 9. Boundary parameterization
For structured or repeated mechanisms define the coupling-support profile rather than an anonymous scalar rank. In a deterministic gate vector, the primary invariant is the signed support pattern of `Delta G`. In a repeated/stochastic mechanism, a prospective coupling coefficient may be defined only after the state grain and trial model are frozen.

P28 therefore treats N0<->N1 'boundary completion' as a structured-support problem, not as post-hoc interpolation between two endpoints.

## 10. Family-equivalence relation
For intervention basis I, architectures A and B are equivalent when every directly measured typed kernel row agrees:

`A ~_I B iff for all tau in I, kappa_A(tau)=kappa_B(tau)`.

For vector gates, equality includes coordinate labels/support. Enlarging I or refining g into G can only refine the observational equivalence partition when the old coordinates are retained as quotients.

## 11. Fresh-world decision table
After this note and the P28 preseal are committed:

1. Exact DROP N0 -> scalar strong ontology survives for that mechanism; no third family.
2. Exact DROP N1 -> scalar strong ontology survives for that mechanism; no third family.
3. Exact DROP X0/X1 -> strong scalar ontology fails at the chosen action grain; open obstruction adjudication.
4. Same measured `(q,g)` with different y under admissible non-y intervention -> deterministic scalar sufficiency fails directly.
5. Structured `G` with partial upstream coupling -> scalar-g architecture taxonomy is non-exhaustive even if y remains fully mediated by q and G.
6. Rank 3 without same-(q,g) action split -> inspect intervention typing and coordinate mismatch before latent promotion.

## 12. Claim ceiling
P28 may establish a conditional exhaustiveness theorem, a fresh scalar-ontology obstruction, a structured-gate third family, or a bounded family census. It may not infer a universal architecture taxonomy, universal latent-state theorem, macro design law, SOLID derivation, manuscript readiness or LAW-R2 without separate authority.
