# EvoNOMOS Generation VIII LAW-R1-P42 — P42-P2-R4 Demand-Indexed Repair Transition Systems: Source-Realized Option Fibers, Non-Congruence of Present Behavioral Quotients, Order-Sensitive Change Paths & Conditional Lifecycle Reversal

**2026-10-12 KST · RAVEL-R4 in P42-P2 · RETURN TO P31 FOUNDING EXPLANANDUM · original Echo source-bounded native verdict PASS · independent Lean verdict checked separately · P42 RUNNING · LAW-R2 NOT_AUTHORIZED.**

## 0. Founding scientific question: not another test partition or quasi-axiom

[P31's authoritative return](../g8-law-r1-p31/P31_ORIGIN_RETURN_STRUCTURAL_EXPLANANDUM.md) requires source-realized OO structure, two rivals meeting the **same present demand**, new external demand, exposed mechanism, vector consequences and a sign reversal or justified no-claim. [P42-P2 R2/R3](P42_P2_RAVEL_ORIGIN_RETURN_REAL_FAULT_DOMAIN_AND_ARCHITECTURAL_REPAIR_OPTION_GEOMETRY.md) recovered:
- Twelve actual original Echo v4 historical revisions on sixteen contexts → **192 source queries**, six selected observational classes and seven cardinality-four minimum distinguishing context subsets; independent 2,517-subset checks.
- Critically, one pair of researchers' rival source architectures using *unchanged* original Echo both passes D0. One `SINGLE` route needs one **late** source registration for D_legacy and `SPLIT` (two routes initially) needs zero.
- Prior R3 **never proved SPLIT was cheaper for the entire lifecycle**. In the late-legacy branch the final route count coincides; labeling a late-cost shift as an intrinsic design winner would be false.

**R4 shifts the principal mathematical object from observation classes to demanded-edit transitions.** It tests what is necessary to predict the repair *options* of architectures that look identical to their current customers.

## 1. Direct answer: a source-based repair-option fiber

Fix source state `s`, a selected old-client contract `D0`, an edit grammar `E` grounded in original compilable source, and a stream of externally arriving demands `\sigma=(d1,...,dk)`. Define the *admissible source evolution fiber*
```text
Repair(s, sigma; D0, E) =
 { s0=s --e1--> s1 --e2--> ... --em--> sm
   : each edit belongs to E,
     every demanded stage satisfies di,
     every stage preserves declared D0 clients }
```
and the minimum permitted late source-edit count `\ell_E(s,\sigma)` among those paths. In the real architecture study, S/L/C/A/Q outcomes remain separate coordinates; `\ell_E` is only an explicitly declared **one-action source registration** count, not a magic whole-life scalar.

Let the present observation map be `O0(s)=observed D0 results`. **The central P42-R4 source witness is a failure of factorization**:
```text
O0(SINGLE) = O0(SPLIT),
but
minimum_edits(SINGLE, L) = 1 and minimum_edits(SPLIT, L) = 0.
```
Thus `\ell_E(-,L)` cannot be expressed as a function of `O0(-)` on both source states. The same pair reverses for demand `N`. A *single actual source structural bit*—whether a generic fallback is registered—suffices for this bounded two-architecture repair-cost classifier. In the presence of an initially all-equal observable `O0`, zero bits of additional structural information cannot suffice for the two distinct repair outputs. No universal information-minimum architecture theorem is implied.

**TCS positioning:** The mathematically appropriate question is whether observational equivalence induced by `D0` is a congruence/bisimulation for **source-edit-enabled demand-labeled transitions**. Here it is not, *on the declared source edit grammar*. This is standard transition-system reasoning and should be evaluated against feature transition systems, delta-oriented evolution formalisms and classical shortest-path dynamic programming, not marketed as newly invented logic.

## 2. Pretest frozen epistemic and source contract

[Exact six-history frozen contract](../../tools/p42/p2-r4/frozen_demand_edit_game.json) committed at SHA **`5fa5cf2c752dd490b8735ecb2b931ce62b69acfd`** before **either authored Go state implementation existed**. Independently verified [freeze Actions #38205881398 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38205881398), tested HEAD `708ce517f3a2bdc43acec7bd93ed77dd8113a58f`, artifact `11727820048`, SHA-256 `a3fb98673db974aa691704b16ffff337f79d60d82919519272a443f08849b0ee`.

The original untouched upstream router is [Echo v4 at merged commit `f085ffbe8f99de165bd920746920000ab56bd6bc`](https://github.com/labstack/echo/tree/f085ffbe8f99de165bd920746920000ab56bd6bc). R4 research sources:
- [SINGLE Go source](../../tools/p42/p2-r4-native/states/single/routes.go), `GET /r/:name\\:cancel`;
- [SPLIT Go source](../../tools/p42/p2-r4-native/states/split/routes.go), **the exact same source** except for one `e.GET("/r/:name",legacy)` registration, and the necessary Go package declaration difference;
- [Original Go client-demand runner](../../tools/p42/p2-r4-native/demand_stream_source_test.go);
- [Independent source diff and exhaustive shortest-edit grader](../../tools/p42/p2-r4/audit_repair_game.py).

**D0 frozen initial clients:** `GET /health → 200/health` and `GET /r/foo:cancel → 200/new:foo`, with verb route identity. The two *different* future demands are:
- **L — legacy restoration:** `GET /r/foo → 200/legacy:foo` and `GET /r/foo:other → 200/legacy:foo:other`;
- **N — deny generic:** the **same two** paths must return 404.

These two future demands are deliberately **incompatible** in a single unchanged source state, so a requirement stream can force source edits back and forth. This is an adversarial game, not a factual prediction of future Echo customer requests. They are legitimate *conditional interventions* for stress-testing an architecture.

## 3. Original Go and exhaustive finite edit-game result

[Original unchanged Echo native Actions #38206188516 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38206188516), tested EvoNOMOS source HEAD `12c39f9f60512322cb21480e19c9e3a4cd247591`, artifact **`11727521737`**, SHA-256 **`a434a262dbeeaa62b2d3c66dadcfd8ce11941aaedcaf410e55cd5744f25aac2f`**. CI verified frozen manifest byte equality with its ancestor, pretest absence of the new source programs, exact untouched upstream Echo SHA, and inspected the two local Go source files.

**The local source delta was proved by an exact textual check** to be one route registration added (or reversed/removed); the compiled source variants themselves were executed in original Echo. This is more than merely labeling two Python nodes `SINGLE`/`SPLIT`. Yet **CI did not apply arbitrary Git patches to a production repository**. It validated the two source programs and their exact edit relation under a restricted grammar.

Each of six frozen requirement histories was run from both source states. **12 source repair histories × source stages (32) × four actual original Go client requests per stage = 128 native Go observations.** A separate checker independently enumerated every possible state choice at every stage under the two-state action grammar and compared its exact minimum with the preregistered path costs. All matched.

| Future requirement history | SINGLE minimal late source edits | SPLIT minimal late source edits |
| --- | ---: | ---: |
| **L** (support generic client) | 1 | **0** |
| **N** (deny generic client) | **0** | 1 |
| **L→N** | 2 | **1** |
| **N→L** | **1** | 2 |
| **L→L** | 1 | **0** |
| **N→N** | **0** | 1 |

At every selected stage, `D0` still produced the original `health` and `new:foo` responses. In SPLIT the generic route satisfies L; in SINGLE it rejects both generic paths as 404, satisfying N. One exact source line add/remove transfers between those states. **This is a program-source-grounded change of the preferred architectural starting point with future demand and stream order**, rather than an isolated program-output difference.

### Three radically different cost notions must not be conflated

1. **Birth-time source surface:** SINGLE 1 extra route registration versus SPLIT 2. SINGLE has less up-front source surface.
2. **Late structural source edits:** reversible table above. Under L, SPLIT avoids a late edit; under N, SINGLE avoids one.
3. **End-to-end cost:** *not measured*. A source registration edit is not an engineer-hour, risk probability, integration duration, rollout expense or verified S/L/C/A/Q ranking.

For transparent mathematical **sensitivity only**, let `p` denote a *hypothetical* probability that a one-shot late demand is L (otherwise N) and `w>0` a *hypothetical* late-edit weight relative to a birth-time route registration:

```text
C_SINGLE = 1 + p·w
C_SPLIT  = 2 + (1-p)·w

C_SINGLE − C_SPLIT = −1 + (2p−1)w.
```

The conditional cost order changes at `(2p−1)w = 1`. For the *illustrative, unmeasured* weight `w=2`, SPLIT is numerically preferred only if `p>0.75`. For `p=0.25`, SINGLE is preferred; for `p=0.9`, SPLIT. The native R4 checker independently calculated these exact **rational** sensitivity examples. **Neither `p` nor `w` was inferred from actual engineering data**, so this is a mathematical moderator/reversal boundary, not empirical evidence of developer productivity or design-choice superiority.

## 4. Restricted finite TCS formalization

[Lean `P42DemandIndexedRepairGeometry.lean`](../../tools/p42/lean/P42DemandIndexedRepairGeometry.lean) encodes a **two-source-state, two-demand, three-edit** system:
- Source edit labels `noop`, `addFallback`, `removeFallback` and explicitly partial admitted transitions.
- `D0` observation is the same for the two states; the source fallback bit distinguishes them.
- `requiredExtraEdits` depends on current source state and future demand, not D0 output alone.
- Two opposing future demands reverse one-step modification preference.
- Order-sensitive two-event paths, with repeated-demand idempotence.
- **Nonfactorization**: there is no total future edit-cost classifier that consumes only the shared D0 observation for both states.
- **A single actual source feature bit is sufficient on this two-state family** to classify the entire declared one-step repair demand alphabet.

This is a classical finite transition-system theorem and a transparent formal interpretation of the original Go source witness; it is **NOT** a compiler-verified abstraction/concretization relation for arbitrary Go programs or a new universal OO law. Do not claim the TCS formal theorem is kernel-verified until the exact independent GitHub Actions Lean receipt is SUCCESS.

## 5. Strong classical challengers and real novelty boundaries

- Andreas Classen et al., 2014, *Formal semantics, modular specification, and symbolic verification of product-line behaviour* ([DOI 10.1016/j.scico.2013.09.019](https://doi.org/10.1016/j.scico.2013.09.019)): featured transition systems already model family-specific admissible behavior.
- *Incremental model checking of delta-oriented software product lines*, 2016 ([DOI 10.1016/j.jlamp.2015.09.004](https://doi.org/10.1016/j.jlamp.2015.09.004)): DeltaCCS already covers source-change-style delta conflicts and **variability-aware congruence**.
- Beohar, Varshosaz & Mousavi, 2016, *Basic behavioral models for software product lines: Expressiveness and testing pre-orders* ([DOI 10.1016/j.scico.2015.06.005](https://doi.org/10.1016/j.scico.2015.06.005)): testing and behavioral product family preorders.
- Parnas, 1972, *On the Criteria to Be Used in Decomposing Systems into Modules* ([DOI 10.1145/361598.361623](https://doi.org/10.1145/361598.361623)): variation-knowledge hiding and change locality.
- Ordinary shortest-path finite graph dynamic programming and change-timing real-options analysis already explain the R4 path table and cost sensitivity.

**None of these serious classical alternatives is falsified by R4.** If the strongest family-aware classical model predicts every requested repair sequence when given identical edit-graph evidence, the correct conclusion is *classical adequacy*. Potential EvoNOMOS scientific novelty remains in finding a reproducible **source-structural and capability/authority mechanism** that predicts repair option sets or their Pareto frontiers across **new, genuinely independent OO maintenance ecologies**, above matched classical challengers, not in naming another graph.

## 6. Epistemic limits and next authentic structural gate

- **What is genuinely native:** both program source states differ by an exact Go line; they compile/run through the unchanged pinned original Echo router; each of 128 observations is emitted by real Go; the frozen action grammar and shortest paths are independent of test-author fiction.
- **What is not historical:** the two source assembly alternatives are authored *for the research*, not established choices made by Echo maintainers.
- **What is not measured:** developer hours, real third-party prospective demands, actual permission of the historic upstream merge actor, speed or deployment risk.
- **What is not new mathematics:** finite nonfactorization, path-dependent finite-state repair cost, sufficient state bit or product-line transition system semantics.
- **What R4 leaves open:** a genuine cross-feature/capability-interface engineering fault domain from original maintainers, source-to-Lean operational refinement, a quantitatively *uncalibrated but separately measured* S/L/C/A/Q comparison on real change histories, and prospectively held-out predictions compared to strong classics.

**Proposed P42-P2-R5 research question:** Can original Go interface/capability organization generate demand-co-occurrence-dependent edits whose modular boundaries cause different **source ownership/implementation conformance/propagation** vectors, including reversals impossible to explain by trivial route registration counts? Concrete rival families: `BUNDLE` versus `SEGREGATE` and `DIRECT` versus `PORT`, with real repositories, source-review gates and unchanged upstream libraries. A strong source-aware delta/refinement competitor gets exactly the same information. If classic theory predicts all, the discovery is an empirically grounded boundary, not a new universal law.

**R4 scientific verdict: SOURCE_REALIZED_BOUNDED_GAME_PASS. FULL_LIFECYCLE_SIGN_CLAIM HOLD. CLASSICAL_CHALLENGERS SURVIVE. P42 RUNNING; LAW-R2 NOT_AUTHORIZED.**
