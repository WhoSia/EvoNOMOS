# P22 Mathematical Note — Property-Indexed Boundary Transport

Status: **P22 pre-fresh mathematical lane / independent of empirical promotion**

## 1. Base object

Let (G=(V,E)) be a directed multigraph and let (mathrm{Path}(G)) be its free category. Objects are vertices; morphisms are finite composable paths.

For a transported semantic property (o), let (S_o) be a state space and assign each edge (e) a map

[
T_e^o:S_o	o S_o.
]

For a path (p=e_ncdots e_1), define

[
T_p^o=T_{e_n}^ocirccdotscirc T_{e_1}^o.
]

Identity paths act by the identity map.

This construction is deliberately minimal: it says only that local boundary semantics compose.

## 2. Proposition 0 — P21 R4/R5 are the same Boolean classifier

Assume (S_o={0,1}) and each edge has Boolean carrier value (c_e(o)in{0,1}). Define

[
R_4(p,o)=igwedge_{ein p} c_e(o),
]

and

[
R_5(p,o)=1 iff 
egexists ein p:;c_e(o)=0.
]

Then

[
R_4(p,o)=R_5(p,o)
]

for every finite path.

**Proof.** By De Morgan duality,

[
igwedge_e c_e=1
iff
orall e,;c_e=1
iff

egexists e,;c_e=0.
]

Therefore P21's `ALL_EDGES_MUST_CARRY` and an existential `carrier_gap?` tree are not empirically separable representations. Their apparent tie is logical equivalence, not unresolved evidence.

## 3. Proposition 1 — Functoriality

If every composable boundary pair is interpreted by ordinary function composition and identity boundaries act identically, then for each property (o),

[
F_o:mathrm{Path}(G)	omathbf{Set}
]

with edge/path action (T_e^o,T_p^o) is a functor into the one-object transformation category on (S_o), or equivalently a representation of the path category by transformations of (S_o).

This is a structural statement about the abstraction, not yet a claim that real software always satisfies the abstraction.

## 4. Proposition 2 — Irreversible Boolean transport collapses path information

Let (S={P,L}), with carrier edge (I(P)=P,I(L)=L) and loss edge (D(P)=L,D(L)=L).

For any path built only from (I,D):

- if the path contains no (D), (Pmapsto P);
- if the path contains at least one (D), (Pmapsto L).

Thus the path quotient relevant to preservation has only two equivalence classes: **no gap** and **at least one gap**. Order and gap multiplicity are unidentifiable.

## 5. Proposition 3 — Repair breaks the Boolean quotient

Add a repair edge (R) with

[
R(P)=P,qquad R(L)=P.
]

Then

[
Rcirc D(P)=P
]

while

[
D(P)=L.
]

So the quotient “has any gap?” is no longer sufficient.

Moreover,

[
Rcirc D(P)=P
eq L=Dcirc R(P),
]

hence (D) and (R) do not commute. A repairable transport theory can therefore carry order information that the irreversible Boolean theory destroys.

## 6. Proposition 4 — Property indexing is mathematically substantive

Let properties (o_1,o_2) have binary states. An edge (e) may satisfy

[
T_e^{o_1}=I,qquad T_e^{o_2}=D.
]

Then no property-independent scalar label (c_e) can faithfully represent both transports simultaneously.

Therefore a successful cross-property empirical witness would force at least a property-indexed boundary representation, unless some coarser quotient is independently justified.

## 7. The P22 empirical question

The mathematics leaves a clean empirical fork.

### Irreversible model
[
M_0:quad D 	ext{ is absorbing.}
]

### Repairable model
[
M_1:quad exists R,;R(L)=P.
]

P22 must search for a fresh software mechanism where **repair/reconstitution is source-defined before outcome inspection**, then test whether a lossy boundary followed by that repair really restores the transported client-observable property.

A positive witness would not prove a universal law. It would only kill the Boolean absorbing quotient for that mechanism class.

## 8. Bridge to P19–P21

One candidate unification is:

- path transport determines the semantic state arriving at a decision boundary;
- local surface geometry selects which arriving state/action morphism is exposed.

Formally, a policy may factor schematically as

[
A = Digl(Q(T_p(o)),,X,,G,,Eigr),
]

where (T_p) is path transport, (Q) a boundary observation/quotient, and (D) the local decision/action map.

This is only a candidate abstraction. P22 explicitly permits a **two-family decomposition** if forcing this factorization requires extra assumptions or loses predictive sharpness.
