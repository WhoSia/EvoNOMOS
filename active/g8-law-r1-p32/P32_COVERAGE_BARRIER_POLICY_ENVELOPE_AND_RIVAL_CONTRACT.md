# P32 — Cost-Sensitive Obligation Semantics: Coverage Barrier and Policy-Envelope Counterexample

**Status:** THEOREM-INSTANCE CHECKER / CLASSICAL MATHEMATICS. NOT_NEW_THEOREM. SOURCE EXTRACTION CI UNVERIFIED until readback of hosted run. No new conditional OO law or LAW-R2.

## What is being modeled?

Let D be a finite set of externally specified maintenance demands and M a finite set of source-maintenance owner units, with weights w_m >= 0. A source-grounded *fixed* obligation activation map U:D -> 2^M maps each demand d to units that would be affected by implementing it **under fixed architecture and semantics**. Define a set-of-demands cost

C(X) = sum_{m in union_{d in X} U(d)} w_m.

This is a *hypothetical additive owner-site cost*, not the measured P3 hand-written churn L, not multiobjective S/L/C/A/Q, and not a generically valid change transition semantics.

**Classical proposition.** C(empty)=0 and C is monotone submodular. For x!=y:

I(x,y) = C({x,y}) - C({x}) - C({y}) + C(empty)
       = - sum_{m in U(x) intersect U(y)} w_m <= 0.

Proof: Each owner's indicator contributes +1 to C({x,y}) iff x or y activates it, and its two single-demand indicators subtract 1 for each activation. The contribution is -w_m if activated by both, otherwise 0. Sum over m. This is the standard weighted-coverage property, not a novel EvoNOMOS result.

### First barrier
If a *complete factorial* under the same fixed architecture, cost definition, and implementation policy yields I>0, the static weighted-coverage model is false. It does **not** follow that an intrinsic inter-obligation interaction or specific SOLID defect was established. Context-dependent activation, stateful order, variable owner cost, policy switching, error in cost measurement, or selection could each break its assumptions.

P3's observed sequential #7316 then #7559 is **NOT** a factorial {none,x,y,x+y} and P3 L cannot be substituted into this identity.

## Two constructive warnings against premature novelty

**Marginal-count insufficiency without strong-rival defeat.** Let A: U(x)={a,b}, U(y)={a,b}; B: U(x)={a,b}, U(y)={b,c}. With unit costs both have equal marginal affected-owner counts 2 and 2. But the mixed difference is -2 vs -1. Marginal site-count B0 cannot distinguish. **However an overlap-aware B0+, Design Rule Spaces B2, or semantic coupling B1 could already distinguish them. This is not H's independent novelty.**

**Selection envelope produces positive interaction without within-architecture interaction.** Consider two admissible architectures, A with disjoint owner costs C_A(x)=1, C_A(y)=3, C_A(xy)=4 and B with C_B(x)=3, C_B(y)=1, C_B(xy)=4. Each fixed architecture is modular and has zero mixed difference. If a single architecture can be selected before processing each demand **set** and the researcher reports V(X)=min(C_A(X),C_B(X)), then V(x)=1, V(y)=1, V(xy)=4, so I_V=+2. This positive sign is caused by *set-dependent architecture selection*, not by intrinsic cost coupling. Do not attribute a favorable or unfavorable sign to shared responsibility without accounting for selection and admissible realizations.

The selector is a *set-of-demands oracle* in this toy, not a legitimate online policy with unknown future requirements. The distinction prevents retrospective minimization from becoming an empirical prediction.

## Actual P2/P3 source interface

Frozen Uptime Kuma birth `398482d590daaac0d44e288c9be3bc6f6667f8b8`; pair #7316→#7559. The bounded source extractor [P32 tool](../../tools/law-r1-p32-obligation-extract.py) binds five logical declaration types to source line, SHA, owner and declared direction, not to a proved propagation mechanism. P3's S=5 versus S=2 is an edit-site semantic metric, neither the total number of obligation *types* (5 vs 5) nor the physical source owner files (3 vs 2). P3 L phase0+14 / phase1-5 DUAL-DISPERSED arises from measured implementation change on those fixed demands. No interaction I may be computed from that two-stage sequence.

## Rival baseline contract, stronger than a straw man

- B0: module counts, class count, actual change sites, *typed/weighted impact overlap*, dependency direction. Use B0+ for the coverage theorem test, not just graph edge count.
- B1: semantic coupling and historical co-change with temporal split and demand conditioning, no hindsight leakage.
- B2: Parnas information hiding, Design Rule Spaces including overlapping concerns/design rules, ISP/SDP/SRP and configuration-aware change impact analysis (CSDG).
- H: outcome-blind owned obligation typing/direction plus context-sensitive contract constraints. Compare only with a predeclared demand where the stronger rivals and H produce different exact sign, Pareto frontier, Q or principled abstention forecasts.

**Prior-art pressure:** CSDG (Angerer et al., Automated Software Engineering 2019, https://link.springer.com/article/10.1007/s10515-019-00253-7); DRSpaces (Cai et al., IEEE TSE 2018, https://doi.org/10.1109/TSE.2018.2797899); co-change functions (Information and Software Technology 2024, https://doi.org/10.1016/j.infsof.2024.107547). Their general graph and change-impact ideas are not the novelty claim.

## Executable/check status

`tools/law-r1-p32-coverage-check.mjs`: 16x16=256 enumerated fixed-map pairs with integer weights [1,2,3,5], overlap identity check, same-marginal rival example, and two-arm policy-envelope counterexample. Mathematical verification in workflow remains **UNVERIFIED** until an actual run is fetched; tool code existing in GitHub is not the same as a completed test.

**Court:** `P32_THEORY_BARRIER_AND_RIVAL_ESCALATION__NO_EMPIRICAL_MECHANISM_CLAIM`.
