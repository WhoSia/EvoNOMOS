# P44-F22 — Repair Residual Structure above SOLID: Sequence-Sensitive Observational Congruence

2026-11-05. **THEORY / BOUNDED COUNTERMODEL, NOT LAW-R2.** Re-centers EvoNOMOS on its founding aim: explain SOLID-like modularity as conditional consequences of stronger mathematical facts about source histories, observers, rights, edit effects, demand disclosure and costs; do NOT postulate five SOLID slogans as independent axioms.

## A. Original-source return and priority audit
Read P42 `P42_P2_R11_P10_REPAIR_CONGRUENCE_SOLID_DERIVATION_AND_INDEPENDENT_GIN_ECHO.md` (RC1 cost-labelled bisimulation, RC2 optional method-set 2^k lower bound, operational SRP/OCP/LSP/ISP/DIP fragments), and P44 `00_P44_MATHEMATICAL_PROBLEM_CONTRACT.md` (F0–F14 and historical/online safety). **These earlier results are PRIOR results; this note does not re-claim them.**

Read original canonical Drive text: Parnas (1972), *On the Criteria to Be Used in Decomposing Systems into Modules* (ID 1EcQRy3iehx4lUN7uGsZ1BFXU33HggcEQ); Sullivan, Griswold, Cai & Hallen (2001), *The Structure and Value of Modularity in Software Design* (ID 1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr); Calcagno, Distefano, O'Hearn & Yang (2009), *Compositional Shape Analysis by Means of Bi-Abduction* (ID 1pO5rUHggdq1FFBzU_bOkFokK7E2WvNuA). Parnas explicitly treats module as responsibility assignment, not synonym for subprogram; Sullivan et al. already use design structure matrices and real options to connect modularity to changeability and value. Calcagno et al. already provide classical compositional source footprint/anti-frame analysis. Existing Drive holdings also confirmed: Reynolds (2002), Liskov & Wing (1994), White et al. (2014) and Martin (1996/2000). This novelty pressure is substantive.

## B. Repair profile indexed by an experiment, not a universal class score
Fix observer family O (joint trace projections), protected contract C, admissible rights-labelled safe edit relation E_pi with nonnegative cost c, and a future demand language D. For a state s define a *one-shot* profile:
  R_1(s) = (Obs_O(s), { K(s,d) : d in D })
where K is the minimum cost of a finite authorized prefix-safe repair satisfying d; +infinity is no path in the **DECLARED COMPLETE graph only**.

The kernel of R_1 is the coarsest partition preserving exactly those quantities, by definition. It need not be an edit congruence, and it may lose which changes are achievable *sequentially while preserving earlier demands*. Calling the kernel a new theorem or a universal modularity score would be circular.

Define the *sequential residual profile*
  R_*(s) = ( Obs_O(s), {K_stage(s,w): w in D*} )
where w is a finite word of demands whose accepted prefix obligations remain protected during later edits. At each stage, the current demand becomes protected after reaching a satisfying source state. A complete right language can additionally retain action, authorization and full cost-labelled outcomes rather than only scalar optima. Two states with equal R_* cannot be distinguished by these declared sequential-cost questions; no universal claim about all Go clients follows.

## C. Strict one-shot versus sequential separation countermodel
Build two finite source-analogue graphs A and B, each with unit-cost, authorized, old-client-safe transitions. Both start at state s with the same old-client observation. Neither s satisfies a nor b. Both have:
 s -> a (cost 1), s -> b (cost 1).
Graph A additionally has a -> ab and b -> ab (each cost 1); graph B has no transitions out of a and b. State ab satisfies a AND b; a and b satisfy only their respective demands. All have the same protected old client outcome.

Thus for each single demand d in {a,b}, K_A(s,d)=K_B(s,d)=1, and the initial old-client observations are identical: R_1(A,s)=R_1(B,s). But K_stage(A,s,ab)=2 while K_stage(B,s,ab)=+infinity, and similarly for ba. Therefore R_1-equivalence is NOT sufficient for sequential repair prediction.

This is a finite symbolic source-analogue; the extra edges do not establish implementation facts about Go. The significance is the need for a history-sensitive *residual* / compositional state rather than a single-demand score. Classical automata Myhill–Nerode/right-language and weighted transition theories already supply the conceptual machinery; the counterexample is a new illustrative research artifact, not a new mathematical priority claim.

## D. Meta-structure connecting, but not conflating, five SOLID fragments
- SRP: noninterfering factorization of demand-conditioned edits under rights/resource frames.
- OCP: existence of an extension-only authorized safe repair path preserving the protected core.
- LSP: context-indexed trace refinement sufficient for existing client substitution.
- ISP: correct projection/factorization of client observations; do not collapse joint trace correlations.
- DIP: core behavior factors through a stable, effect-complete interface/port with independently authorized substitution.
These are distinct conditional consequences of stronger semantics. Neither the acronym nor class/method counts are the premises. They do not jointly characterize all legal repair sequences unless source effects, rights, history and costs are additionally certified.

## E. Strongest novelty challenge
Parnas 1972 already argues for design decisions hidden behind modules; Sullivan et al. 2001 already value modular options; Reynolds 2002 and Calcagno et al. 2009 cover frames/bi-abduction; Liskov & Wing 1994 explain behavioral subtyping; White et al. 2014 covers multi-step CSP configuration. Therefore neither 'SOLID emerges from modular structure', 'future options matter', nor 'single-demand costs do not imply sequence costs' can credibly be sold as a wholly original general principle. A genuinely research-worthy result would derive a **source-checkable, observer-and-rights-indexed sufficient residual certificate** that predicts on unseen maintained-source sequences with lower all-in proof/check cost or better discrimination than equal-information classical comparators.

## F. Explicit stopping / promotion court
- A finite independently executable checker of C is useful for model consistency, but does not certify Go source extraction or source-edit graph completeness.
- General Go semantics, permissions and client traces remain G1–G7 OPEN.
- No evidence of prospective heldout sequential cost prediction over strong classical baseline, no measured labor.
- **F22 FORMAL DIRECTION ADVANCED; LAW-R2 HOLD.** Next focus: characterize minimal *certificate content* for preserving sequential residuals, including a counterexample where a dropped effect/authorization coordinate makes a false-safe prediction, and compare to weighted bisimulation / modal mu-calculus / classical model checking.
