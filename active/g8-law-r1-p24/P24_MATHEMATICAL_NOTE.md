# P24 Mathematical Note — Prospective Algebra Orientation, Faithful Degree & Boolean Bridge

Status: **PRE-FRESH / BINDING FOR P24 CLASSIFICATION**

## 1. Transformation setting

For a finite semantic state set (S), a transport operation is a transformation (T:S	o S). The generated transformation monoid is a submonoid of (mathrm{End}(S)).

P24 distinguishes four prospectively frozen algebra classes for two distinguished idempotent operations (D,R):

1. **LEFT-ZERO + identity**
   [
   Dcirc R=D,qquad Rcirc D=R.
   ]

2. **RIGHT-ZERO + identity**
   [
   Dcirc R=R,qquad Rcirc D=D.
   ]

3. **COMMUTATIVE IDEMPOTENT**
   [
   Dcirc R=Rcirc D.
   ]

4. **LARGER/NONBAND**
   if the closure contains more than ({I,D,R}) or idempotence fails.

## 2. Proposition A — Minimal faithful degree for the left-zero orientation

A one-state set has one endomorphism, so degree (1) is impossible for a three-element monoid.

On a two-state set, let (D,R) be the two distinct constant maps. Then

[
Dcirc R=D,qquad Rcirc D=R,
]

and together with identity they faithfully realize the left-zero orientation.

Therefore:

[
mu(M_L)=2.
]

## 3. Proposition B — Minimal faithful degree for the right-zero orientation

On a two-state set, the only distinct nonidentity idempotent transformations are the two constant maps, whose multiplication is left-zero, not right-zero.

Hence a faithful right-zero-with-identity action is impossible in degree (2).

A three-state witness exists. Let states be (L,C,A) and define

[
D:Lmapsto A,;Cmapsto C,;Amapsto A,
]

[
R:Lmapsto C,;Cmapsto C,;Amapsto A.
]

Then

[
Dcirc R=R,qquad Rcirc D=D,
]

with (I,D,R) distinct.

Therefore:

[
mu(M_R)=3.
]

## 4. Proposition C — Boolean quotient erases orientation

For either (M_L) or (M_R), identify (Dsim R). The quotient has two classes ([I],[C]) and

[
[C]^2=[C].
]

Thus the quotient multiplication table is identical for the two opposite orientations.

Consequently, any empirical observation that has already quotiented (D) and (R) into a single carrier/noncarrier class cannot identify left-vs-right temporal orientation.

## 5. Proposition D — AND uniqueness on a complete Boolean packet

Let

[
f:{0,1}^2	o{0,1}.
]

If the full held-out packet is

[
f(0,0)=0,quad
f(0,1)=0,quad
f(1,0)=0,quad
f(1,1)=1,
]

then by extensional equality of functions on the finite domain,

[
f(q,g)=qland g
]

is the unique Boolean function compatible with all four observations.

This is not yet evidence that a fresh software mechanism has these four cells. P24 freezes the function before searching for the held-out packet.

## 6. Classification rule

P24 does **not** classify orientation from the observed signs after execution.

Before hosted intervention, source semantics must supply a finite transition table or equivalent executable rule.

- If both (D,R) overwrite the same coordinate unconditionally to distinct constants: **LEFT-ZERO**.
- If each operation acts on a source/legacy state but preserves the other's already-canonical fixed point: **RIGHT-ZERO**.
- If the transformations commute on all predeclared states: **COMMUTATIVE IDEMPOTENT**.
- Otherwise: **LARGER/NONBAND**.

The predicted minimum faithful degree is then read from the frozen class where available.

## 7. Bridge hypothesis

The prospective bridge is frozen as

[
y=qland g,
]

where

- (q=1): the arrived transport state is action-sufficiently PRESENT/AVAILABLE;
- (g=1): the local geometry/authority gate independently permits the action.

No repository ID, mechanism ID, language ID, or post-outcome feature may enter the bridge.

## 8. P24 falsification conditions

P24 bridge fails if any complete held-out (2	imes2) packet differs from AND.

P24 orientation prediction fails if the pre-hosted source-derived class disagrees with the hosted generated transformation table.

P24 faithful-degree prediction fails if exhaustive enumeration finds a smaller faithful action than the frozen class predicts or the hosted mechanism requires a larger state space than predicted.
