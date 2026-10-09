# P37-MATH-F — Rectangularity, Local–Global Repair Factorization and the Limit of SOLID-Style Modular Invariants

**2026-10-10 KST · AFTER E1/E2 NATIVE CHECKS. Structural algebra, not a claimed new beyond-classical theorem.**

## Abstract problem

For two owners A and B, let finite state sets be S_A, S_B, local edit relations Γ_A and Γ_B, and a composite safety/compatibility predicate I⊆S_A×S_B. A legal independent-authority composite step changes only one coordinate, using its original local Γ edit. Future demand is a product D_A×D_B and every visited state must satisfy I.

A classic *independence mistake* treats global safety as if two local predicates could independently decide it:
```
I(a,b) ?= I_A(a) ∧ I_B(b).
```
A dependency-inverted API alone does not make this equality true; it changes source coupling, not the actual admissible pair relation.

## Theorem F1 — exact rectangularity characterization

For a **nonempty** finite admissible relation I⊆S_A×S_B, the following are equivalent:
1. I=U×V for some U⊆S_A, V⊆S_B.
2. Whenever (a,b)∈I and (a',b')∈I, **both crossed pairs** (a,b'),(a',b) are in I.

**Proof.** If I=U×V, crossed pairs are obviously allowed. Conversely pick any a∈π_A(I), b∈π_B(I). There exist b₀,a₀ such that (a,b₀),(a₀,b)∈I. Mixed-pair closure implies (a,b)∈I. Thus I=π_A(I)×π_B(I). Empty I is separately the trivial empty product case.

The condition is classical *rectangularity of relations* and close to relational database independence / constraint satisfaction; do not call it a newly discovered software law.

## Theorem F2 — factorization of future repair existence under true independence

Assume **all four** conditions:
1. global invariant I=I_A×I_B, and both starting states and final target satisfy it;
2. composite authorized Γ is the asynchronous product of Γ_A and Γ_B (exactly one coordinate changes; any local edit is permitted while other coordinate is held fixed);
3. target requirement D=D_A×D_B, with no cross-module acceptance predicate;
4. every intermediate local path must satisfy its own invariant and neither module exposes an additional cross-owner edit authorization rule.

Then
```
May_{Γ,I}((a,b),D)
  ⇔ May_{Γ_A,I_A}(a,D_A) ∧ May_{Γ_B,I_B}(b,D_B).
```

Proof (⇒): project every global path onto each coordinate; ignore stuttering edits of the other owner; all projected states obey their own invariant by I=product, and endpoints reach demanded sets. Proof (⇐): choose successful local paths and first execute all A steps while B stays in its safe initial state, then all B steps while A stays in its safe final state; rectangularity guarantees every intermediate global state is safe. Both are finite. This is an elementary asynchronous-product path theorem.

The theorem does **not** survive generally if the invariant is nonrectangular, if the demand is relational, if a source edit requires another owner's simultaneous approval, or if intermediate deployment states are not actually represented.

## Concrete nonrectangular original-Go counterexample

Original `gorilla/sessions` is naturally composed with original `gorilla/securecookie`. Old and new issuing/read keys are represented by W0/W1 and R0/R1; the reader R* admits both. Original source checks in [E1](P37_E1_NATURAL_SESSIONS_SECURECOOKIE_TWO_OWNER_COMPATIBILITY_PRESEAL.md) and [E1/E2 verdict](P37_E1_E2_NATIVE_COMPOSITE_INVARIANT_AND_STRONG_RIVAL_VERDICT.md) use exact original code and two separate original repositories. Under live-only compatibility `I_live`, pairs (W0,R0) and (W1,R1) are valid but crossed pairs (W1,R0) and (W0,R1) are invalid. Therefore I_live is **not rectangular**; no pair of individual Boolean local safety predicates characterizes the combined compatibility table exactly. Owner-local ability to switch versions can coexist with absence of a safe one-owner-at-a-time path. R* adds safe cross-owner bridge states. This is a structural incompatibility, **not** a runtime cost difference.

A separate `I_legacy` obligation that readers must continue accepting old persisted cookies throughout a migration window makes a further distinction: (W1,R1) remains invalid during that window even if live-only safety permits it. The expiry/permission change must be **explicitly represented as a new state transition**, not silently assumed.

[P37-E2 finite checker](../../tools/p37-e2/owner_product_repair_graph.py) tests all 4 binary square mixed-state signatures, exhaustively rules out factorization of the six-pair owner compatibility table into two unary predicates (2²×2³ assignments), and finds a legal dual-reader bridge path only when Γ permits it. It also checks alternative synchronized atomic authority without confusing it with sequential permission.

## Where this goes beyond ordinary SOLID metrics, and where it does not go beyond prior mathematics

The operational source architecture can obey ISP/DIP/SRP in a bounded sense while I_live is nonrectangular; those principles say little about asynchronous multi-owner compatibility across a release window. That locates SOLID within a broader **typed source, edit authority, product invariant** framework; it does not show that relational constraints or staged migration were invented by EvoNOMOS.

The strongest classical rivals include relational databases' rectangularity/factorization, assume–guarantee compatibility checking, compositional model checking and expand/contract distributed upgrade planning. They fully explain F1, F2 and E1/E2 evidence. Thus `DIP49_NEW_LAW_IDENTIFICATION_HOLD` and `LAW-R2_NOT_AUTHORIZED`.

## Next genuinely discriminating research problem

Construct a new source-derived typed graph metric for **which cross-owner obligations can be discharged by authorized bridge morphisms** and compare it with full classical assume-guarantee, compatibility checking and change-impact analysis. Freeze the graph construction and opposing quantitative/structural predictions *before* independent release ecosystems are inspected. One simple nonrectangular I and its dual-reader repair are calibration examples, not a discovery holdout.

**Verdict:** `P37_MATH_F_RECTANGULARITY_AND_COMPOSITE_MAY_FACTORING_CLASSICAL__P37_E1_E2_TWO_REPO_NATIVE_PASS__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
