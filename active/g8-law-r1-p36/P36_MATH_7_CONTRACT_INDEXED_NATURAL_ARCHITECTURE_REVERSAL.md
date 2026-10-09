# P36-MATH-7 — Contract-Indexed Feasibility, Policy Reversal and the Non-Existence of Unconditional Winners

**2026-10-10 KST · P36 OPEN.** This study connects actual original core routing source structure to a classical conditional design-choice argument. It is NOT a beyond-classical law, and its native O9 source-level outcome remains provisional until the two pinned CI jobs complete.

## No architecture ranking independently of its semantic contract

Let `A` be a genuine software architecture source and `Q` an explicitly specified acceptance contract. Define:
```
Feasible(A,Q) := all pinned Q tests pass on the stated histories and inputs.
Cost(A,Q,c) := measurable vector of correctness, latency, allocation,
                registration burden, migration burden and permitted-edit cost
                under context c; undefined as fair comparison when Q fails.
```
The apparent statement `A is a better design than B` is **ill-typed** unless the same Q and the same relevant context are fixed. If distinct future demands `Q_s` and `Q_c` are incompatible, then `Feasible(A,Q_s)` and `Feasible(B,Q_c)` may both hold while opposite combinations fail. This proves no *unconditional* preference between A and B, but is a standard order/decision fact.

## Prospective original implementation world O9

Real original `go-chi/chi` **core radix-tree Mux**, unlike its independent header-map middleware studied in O7, groups static path nodes before parameter nodes by `tree.go` `ntStatic=0` then `ntRegexp` then `ntParam`, searching in node-type order. Original `gorilla/mux` core `Router` uses registered-order route slice.

Both register the same two routes, `/members/{id}` (PARAM) and `/members/me` (STATIC), in both orders. `GET /members/42` must route to PARAM in both and `GET /outside` must 404. When both patterns match `GET /members/me`:
- `Q_s`: static specificity beats earlier generic registration, in both registration histories.
- `Q_c`: earliest registration wins, in both histories, including generic-first.

Same program world/paths and changed *policy contract*, not changed hardware or unit: expected `Feasible(Chi,Q_s)=1`, `Feasible(Gorilla,Q_s)=0` on generic-first, and `Feasible(Chi,Q_c)=0`, `Feasible(Gorilla,Q_c)=1`. The precise tests and opposite expected scientific negatives are independently frozen in [O9](P36_O9_NATURAL_CORE_ROUTER_POLICY_REVERSAL_PRESEAL.md) before first native run [#37969103183](https://github.com/WhoSia/EvoNOMOS/actions/runs/37969103183).

This is a **context-dependent functional preference reversal**, NOT the proposition that runtime cost ranking reverses under fixed functionality. The contracts are mutually incompatible on a generic-first overlapping request. It therefore cannot serve as a fixed-Q counterexample to a total ordering based on cost alone; it demonstrates why Q must be an index of a design-law statement.

## Classical theories and actual next frontier

Radix/static-vs-param precedence, list/insertion-order priority and general decision-making with incompatible objectives predict the O9 sign matrix. Even if O9 native PASS, strong `B_classical_priority` wins; `DIP49_NEW_LAW_PAIR_HOLD`.

More useful future inquiry is **repair reachability after requirements shift**:
```
R_{Q_s→Q_c}^{Γ}(A) = { B : A --(allowed edit Γ)--> B
                            ∧ B satisfies the new priority policy
                            ∧ B preserves all required prior non-overlap tests }.
```
The Γ restrictions must be realistic: API/ABI compatibility, external clients whose registration order cannot be rewritten, code ownership, runtime availability, and delivery budget. To prevent a straw classical rival, compare actual source patches with classical code-data abstraction, dispatch-table design, trie ordering, refactoring and program-repair economics. If no prospectively separable strong-rival prediction emerges, retain HOLD.

**MATH-7 verdict pre-native:** `CONTRACT_INDEX_NECESSITY_CLASSICAL__NATURAL_CORE_SOURCE_POLICY_REVERSAL_PREDICTED__O9_NATIVE_PENDING__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.


## Actual natural core-source readback, prospectively predicted

[Original Chi + Gorilla unchanged native core CI #37969103183](https://github.com/WhoSia/EvoNOMOS/actions/runs/37969103183) completed **SUCCESS 2/2**: Q0 disjoint path PASS in both. On generic-first registration of `/members/{id}` then `/members/me`, actual source outputs on GET `/members/me` are Chi STATIC and Gorilla PARAM. Under new *specificity-first* client policy D19, Chi passes while Gorilla fails; under mutually exclusive *chronology-first* D20, Gorilla passes while Chi fails. The original source logs with exact test case/ZIP SHA are at [O9 preseal's post-result section](P36_O9_NATURAL_CORE_ROUTER_POLICY_REVERSAL_PRESEAL.md). No source repairs were applied to produce either behavioral result, and no special project-written routing wrapper was used. This is a genuine **conditional functional feasibility reversal** across two naturally evolved core routers.

**Policy index is mandatory**: a statement `A > B` detached from `Q` is ill-typed here. Under `Q19`, `Feasible(Chi)=true, Feasible(Gorilla)=false`; under `Q20`, `Feasible(Chi)=false, Feasible(Gorilla)=true`. That does not establish opposite **runtime cost** signs at equal Q, because one arm fails the compared contract in each pairing. Classical radix-tree priority and ordered route evaluation completely predict the outcome; `DIP49_NEW_LAW_HOLD`.
