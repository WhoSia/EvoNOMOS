# LAW-R1-P29 Mathematical Note — Semantic Quotient and Repaired Intervention Geometry

## 0. Authority and non-repair rule

This note is frozen after P28 closure and before any P29 fresh candidate outcome is inspected. P28 remains authoritative: its X1 witness showed that its action-grain `q` was not action-necessary, while N0/N1 remain conditionally exhaustive under the strong scalar assumptions. P29 does not rename P28 coordinates retroactively.

The repaired representation is prospective:

`S = (Q, R, G, Y)`

where `Q` is an action-contract capability, `R` is an implementation route, `G` is local gating structure, and `Y` is the public action/effect.

## 1. Operational semantics

`Q=1` means that the upstream/public action capability is admissible under a predeclared contract and is measured independently of the observed action and the selected implementation route. `Q=0` is produced only by an admissible capability intervention that does not directly manipulate `Y`.

`R=1` means that the nominated implementation route is available and selected. `R=0` means that route is unavailable or explicitly disabled. A route drop may expose a predeclared fallback while leaving `Q=1`.

`G` is a scalar only when the mechanism has one frozen local gate. Otherwise `G=(g_1,...,g_m)` is retained. A partial-coupling result changes a component of `G`; it is not silently recoded as route fallback.

`Y=1` means that the public action succeeds against one common oracle. `Y` is never used to define `Q`.

## 2. P28 X1 as a legitimate quotient refinement

A P28-style route-loss observation is a legitimate refinement when all of the following hold prospectively:

1. `Q` is measured by the action-capability contract rather than inferred from `Y`.
2. `R` is measured by route admission or selected-backend evidence.
3. The route intervention leaves `Q` unchanged and does not directly intervene on `Y`.
4. A common public oracle shows `Y=1` in both baseline and route-drop arms.

Then `(Q,R,G,Y)=(1,1,G,1)` to `(1,0,G',1)` is a fallback-preserving action factorization. It is not a failure of action necessity because `Q` did not drop. If the old scalar `q` was only a route-admission observable, the explicit map is `q -> R` at that grain; the old P28 verdict is preserved rather than repaired.

## 3. Strong scalar theorem and repaired separation

Assume the strong scalar axioms:

* `Q=0 => Y=0` under admissible non-Y interventions;
* a necessary scalar gate satisfies `G=0 => Y=0`;
* `(Q,G)` deterministically suffices for `Y` at the adjudication grain.

Under a typed upstream/capability drop from `(Q,G,Y)=(1,1,1)`, the only strong-scalar rows are `(-1,0,-1)` and `(-1,-1,-1)`, corresponding to P27 N0 and N1 after an explicit embedding. P28 X1 is outside this theorem because its observed action persists after its old q/g coordinates drop; it is an ontology-grain obstruction, not N2.

## 4. Minimal repaired intervention basis

For one scalar gate and one route, the minimal separating basis, in addition to one baseline observation, is:

* `Q_DROP`, holding `R,G` fixed: tests action necessity;
* `ROUTE_DROP`, holding `Q=1` and allowing only the frozen fallback: tests route/action separation;
* `G_DROP`, holding `Q,R` fixed: tests local gate necessity.

Removing any one of these interventions leaves at least one pair of the three roles observationally confounded. For `G=(g_1,...,g_m)`, the gate leg expands to the smallest componentwise set needed to distinguish each independently admissible gate direction; no scalar compression is allowed without a matched action-separating proof.

## 5. Same-repaired-state falsifier

The stronger P29 falsifier is an admissible non-Y intervention producing two observations with identical directly measured `(Q,R,G)` but different public `Y`. After excluding measurement mismatch, route misclassification, direct-Y intervention, and environmental confounding, this falsifies deterministic action sufficiency of the repaired quotient. It is the principal LAW-R2 pressure test, but no LAW-R2 authority is implied by seeking it.

## 6. Structured-G rival

A structured-gate candidate is admitted only when `m>=2`, each relevant component is directly measurable, and a proper nonempty subset of components is upstream-coupled while another component remains independently controlled. Such a witness is a partial-coupling architecture in `G`; it is not a route fallback and not a latent-state claim by default.

## 7. P27 embedding without retroactive change

P27 N0/N1 can embed coherently when its old `q` is independently shown to be an action-capability coordinate, its old `g` is a necessary gate, and the public action is deterministic at the declared grain. If a P27/P28 mechanism instead identifies `q` with route availability, P29 records the map `q -> R` for that mechanism only. The original P27/P28 measurements, verdicts, and authority ceilings remain frozen.

## 8. Claim ceiling

P29 may establish a repaired quotient, a route-preserving X1 transport, a structured-G discriminator, or a same-repaired-state action split. It may not infer a universal architecture taxonomy, a universal latent-state theorem, macro law, SOLID derivation, manuscript authority, or LAW-R2 from quotient repair alone.
