# P23 Mathematical Note — Repair Monoid, Canonical Observation Quotient & Two-Level Factorization

Status: **PRE-FRESH MATHEMATICAL LANE / EMPIRICAL AUTHORITY = NONE**

## 1. Carrier-repair transformation monoid

Let the property-state set be

[
S={P,L}
]

with (P=) PRESENT and (L=) LOST.

Define transformations

[
I(P)=P,quad I(L)=L,
]

[
D(P)=L,quad D(L)=L,
]

[
R(P)=P,quad R(L)=P.
]

Composition is ordinary function composition:

[
(fcirc g)(x)=f(g(x)).
]

The generated monoid is

[
M_{CR}={I,D,R}.
]

Its multiplication table is

| (circ) | (I) | (D) | (R) |
|---|---|---|---|
| (I) | (I) | (D) | (R) |
| (D) | (D) | (D) | (D) |
| (R) | (R) | (R) | (R) |

Thus (Dcirc R=D) and (Rcirc D=R).

## 2. Proposition A — Normal form

Every word over ({I,D,R}) evaluates to:

1. (I), if the word contains no (D) or (R);
2. otherwise the **leftmost non-identity symbol in composition notation**, equivalently the **last non-identity transformation executed in temporal order**.

### Proof sketch

(Dcirc x=D) and (Rcirc x=R) for every (xin M_{CR}). Therefore once a non-identity symbol occurs on the left of a composition word, every suffix to its right is absorbed. Induction on word length gives the result.

Operationally, if execution order is written left-to-right as (e_1;e_2;dots;e_n), the resulting composite is (T_{e_n}circcdotscirc T_{e_1}), hence the last executed non-identity operation wins.

## 3. Proposition B — Algebraic type

All elements are idempotent:

[
x^2=x.
]

Moreover

[
xyx=xy
]

for all (x,yin M_{CR}).

Hence (M_{CR}) is a **left-regular band monoid**, more specifically a two-element left-zero semigroup ({D,R}) with an identity adjoined.

This label carries no empirical authority; it identifies the finite algebra exactly.

## 4. Proposition C — Minimal faithful state size

A faithful transformation representation of (M_{CR}) requires at least two states.

### Proof

A one-state set has only one endomorphism, so no injective monoid homomorphism from a three-element monoid exists.

The action on (S={P,L}) above distinguishes (I,D,R), so two states suffice.

Therefore the minimal faithful transformation degree is exactly (2).

## 5. Proposition D — Unique nontrivial proper congruence

The only nontrivial proper monoid congruence on (M_{CR}) is

[
Dsim R,qquad I
otsim D.
]

### Proof sketch

There are only three two-block partitions of a three-element set.

- (Dsim R) is compatible with multiplication and yields a two-element quotient.
- If (Isim D), right multiplication by (R) gives
  [
  Icirc R=R,qquad Dcirc R=D,
  ]
  so (Rsim D), forcing the universal congruence.
- If (Isim R), right multiplication by (D) analogously forces (Dsim R), again universal.

Thus (Dsim R) is the unique nontrivial proper congruence.

## 6. Corollary — Boolean carrier theory is the canonical proper quotient

Quotienting by (Dsim R) gives

[
M_{CR}/(Dsim R)={[I],[C]}
]

with

[
[C]^2=[C],qquad [I][C]=[C][I]=[C].
]

This is exactly the two-element identity/non-identity carrier monoid.

So the Boolean theory is not merely an arbitrary simplification: **among proper nontrivial monoid quotients of (M_{CR}), it is unique up to isomorphism.**

What it erases is precisely the distinction between loss and repair.

## 7. Proposition E — Syntactic congruence versus semantic sufficiency

The path-language predicate “does the word contain (D)?” is compositional under concatenation:

[
h(uv)=h(u)lor h(v).
]

Therefore its kernel can define a syntactic monoid congruence.

But it is not semantically sufficient for final transported state once repair exists.

For example, in execution order:

[
D mapsto L,
]

while

[
D;R mapsto P.
]

Both words contain (D), yet yield different final states.

Hence **compositional quotient** and **prediction-sufficient quotient** are distinct notions.

## 8. Proposition F — Noncommutativity survives every nontrivial state observation

Let

[
Q:S	o Y
]

be an observation map.

The two orderings satisfy

[
(Rcirc D)(s)=P,qquad (Dcirc R)(s)=L
]

for every (sin S).

Therefore

[
Qcirc Rcirc D = Qcirc Dcirc R
]

on all reachable states iff

[
Q(P)=Q(L).
]

Thus **the repair/loss noncommutativity is observationally erased iff the observation collapses PRESENT and LOST themselves.**

Any observation that preserves the basic semantic distinction (P
eq L) must also preserve the order-reversal witness.

## 9. Property-indexed product actions

For properties (o_1,dots,o_k), define

[
S=prod_i S_{o_i}.
]

An edge (e) acts coordinatewise by

[
T_e(s_1,dots,s_k)
=
igl(T_e^{o_1}(s_1),dots,T_e^{o_k}(s_k)igr).
]

A property-independent scalar edge label is faithful only if the coordinate actions satisfy the imposed diagonal restriction.

If for the same edge (e),

[
T_e^{o_1}
eq T_e^{o_2}
]

under a fixed identification of state spaces, then no single diagonal scalar action can represent both coordinates faithfully.

## 10. Canonical observation quotient for the surface-selection bridge

Let (S) be arrived transport states, (C) the frozen local-context set (existing (X,G,E)), and (A) the action set.

Suppose the local policy is

[
Pi:S	imes C	o A.
]

Define the **action signature**

[
phi:S	o A^C,
qquad
phi(s)(c)=Pi(s,c).
]

Define behavioral equivalence

[
sequiv_Pi s'
iff
phi(s)=phi(s').
]

Let

[
Q_{min}:S	o S/{equiv_Pi}
]

be the quotient map.

### Theorem G — Coarsest sufficient observation quotient

There exists a unique induced map

[
D_{min}:(S/{equiv_Pi})	imes C	o A
]

such that

[
Pi(s,c)=D_{min}(Q_{min}(s),c).
]

Moreover, for any other observation map (Q:S	o Y) through which (Pi) factors,

[
Pi(s,c)=D_Q(Q(s),c),
]

we must have

[
Q(s)=Q(s')
Rightarrow
sequiv_Pi s'.
]

Hence every sufficient (Q) refines (Q_{min}), and there is a unique map on the image of (Q)

[
h:operatorname{im}(Q)	o S/{equiv_Pi}
]

with

[
Q_{min}=hcirc Q.
]

Therefore (Q_{min}) is the **coarsest action-sufficient observation quotient**, unique up to canonical isomorphism.

### Consequence

The bridge need not choose (Q) aesthetically. Given a frozen policy family and frozen context set, the minimal observation quotient is mathematically determined by action indistinguishability.

## 11. Decomposition uniqueness question

A two-level factorization

[
A=D(Q(T_p(o)),X,G,E)
]

has two separable ambiguity sources:

1. transport representation ambiguity;
2. observation refinement ambiguity.

Theorem G removes the second ambiguity by selecting (Q_{min}).

What remains empirical is whether a single restricted transport grammar (T_p) spans Rust/Ruby/Go/Flink without mechanism-local parameters.

If not, the current two-family decomposition remains the smaller falsifiable theory.

## 12. P23 empirical targets

P23 must test:

1. **order reversal**: source-defined loss (D) and repair (R) give different outcomes under (D;R) vs (R;D);
2. **property indexing**: a shared boundary acts differently on two predeclared properties;
3. **restricted bridge**: a non-arbitrary (Q_{min})-style quotient and shallow local decision grammar connect at least one surface-selection exact family with multiple path-transport exact families.

No empirical claim follows merely from the algebra.
