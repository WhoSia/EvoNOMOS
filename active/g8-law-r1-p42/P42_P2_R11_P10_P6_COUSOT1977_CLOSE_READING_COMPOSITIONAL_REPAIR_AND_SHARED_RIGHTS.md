# EvoNOMOS G8 LAW-R1-P42 — R11-P10-P6: Cousot 1977 Close Reading and Compositional Repair-Abstraction Obstructions

**2026-10-17. P42 RUNNING, P43 HOLD, LAW-R2 NOT_AUTHORIZED.** P10-P6 is bounded classical mathematical source-effect work; no universal SOLID theorem or classical-priority claim.

## I. Exact original source custody / comparison

Original reference: Patrick Cousot and Radhia Cousot (1977), *Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints*, Fourth ACM Symposium on Principles of Programming Languages, pp. 238–252; DOI 10.1145/512950.512973.

Two distinct source artifacts have been physically inspected in Google Drive and downloaded locally:

1. [Canonical searchable text PDF, 15 pages of original pp. 238–252](https://drive.google.com/file/d/1hZfipMMYFSwpOVx4ZuhAIvkzt4jDptIl/view): 1,184,973 bytes, SHA-256 `a7a0b70a69487ea4952df8a7dff2eecd3f5efdf00232319ebb4e9056225e2b35`. Already in Research OS Literature Commons **10_PAPERS** before this turn. Text search is useful, but source transcription has OCR errors and two-column ordering artifacts; formal expressions must be verified against the facsimile.
2. [1977 ACM conference original-facsimile scan, 16 pages including conference cover](https://drive.google.com/file/d/1IH6ZPnHQ35RCCdLbrRhxh_gl87SxUrK3/view): 941,105 bytes, SHA-256 `5d2956eed13b2d40f6e15c2087fb870c3dea54a332fe46ee07cea608ca417238`. It was uploaded to **00_INTAKE — Literature Radar** on 2026-10-17 and has now been renamed and MOVED to **10_PAPERS**; relocation was checked by Drive metadata. Its image-only contents and extra ACM cover page make it an alternate provenance artifact, not a byte-identical duplicate. Neither file was deleted or silently replaced.

Both actually contain the article title/author and printed article p. 238 at the beginning of the scientific paper and p. 252 at the end; scanned PDF page 1 is the POPL conference cover and pages 2–16 are the actual pp. 238–252.

## II. Original paper's argument, not a retrospective modern synopsis

Read the article in printed-order sections 1–12 and inspect the facsimile where OCR damages equations. Claim-by-claim source mapping:

- **§§1–2, p.238.** The denotation in an abstract domain summarizes selected facets of concrete computations. The rule-of-signs example illustrates useful but incomplete abstract evaluation. The paper carefully separates an abstract interpretation that is *computable* from a concrete semantics that is too expensive or impossible to exhaustively run.
- **§3, pp.238–240.** The source language is finite flowcharts; states include control arcs and environments; deterministic next-state operations define computation sequences, and least fixed points enter its denotational presentation. Not a calculus of Git commits, patches, reviewer actions or source-owner rights.
- **§4, p.240.** The concrete program-point environments are collected as a context vector. The forward equation system has a monotone transformer; its **least fixed point** agrees with reachable concrete environments. The authors explicitly distinguish states that actually occur from overapproximating states considered by practical analysis.
- **§5, pp.240–242.** Abstract contexts form suitable complete semi/lattice structures, local instruction interpretations are monotone, and global abstract properties arise as solutions to recursive equation systems. §5.2 permits forward, backward, and combined equation forms; §5.3 contrasts syntactic justification with semantic consistency.
- **§6, pp.242–243 — most relevant.** The authors introduce order-preserving abstraction α and concretization γ; their printed equations 6.3 and 6.4 express α∘γ identity on abstract contexts and **concrete inclusion** x≤γ(α(x)), respectively. Local condition 6.5 (equivalent to a commuting or conservative simulation diagram for primitive constructs) is used to obtain **global consistency** of the program interpretation, via appendix T1/T2. This is the true historical comparator for our desired source-to-effect theorem. A mere AST detection of a guard is not the same as discharging local consistency.
- **§7, pp.243–245.** Abstract interpretations are ordered by refinement; interpretations equivalent under the ordering become equivalence classes, and a lattice of abstraction degrees is developed, including interval and sign examples. Our proposal to search for sufficient quotient coordinates lives squarely in this classical lineage.
- **§8, pp.244–245.** Constructive definition and correctness of fixpoint iteration under explicitly stated monotonicity/continuity assumptions. Need not conflate existence of a mathematical least fixed point with effective termination of its exact computation.
- **§9.1.3, pp.246–247 and §9.3.4, pp.248–249.** **Widening** accelerates ascending approximation to achieve a finite stopping behavior; **narrowing** refines certain upper approximations, not guaranteed in general to restore the exact least fixed point (§9.4). These procedures control computability/precision, not repair rights or real engineer-hours.
- **§9.5 and §10, pp.249–250.** The authors recognize different approximation directions and emphasize that their unifying formal model can be enriched for particular applications. Their claimed generality should not be appropriated as new EvoNOMOS theory.

**Source-boundary correction:** Our R11-P10-P5 repair-cost inclusion K_must⊆K_conc⊆K_may and weighted optimum sandwich is a classical extension in a *new costed repair application*. It is not a theorem explicitly stated in these 1977 pages. The authors did NOT analyze SOLID, human maintainer edit authorization, modern GitHub PR lifecycle, or comparative software architecture ranking.

## III. The question Cousot leaves for us — source edit composition

Let component i have concrete state space S_i, source action alphabet E_i, protected client observations O_i and admissible cost-labelled source-edit transitions `s_i --(e,c_i)--> t_i`. An abstraction α_i to A_i has verified local forward simulation: for each legal concrete action there is a labelled/cost-matching abstract step, preserving the promised old-client effect projection.

A global program is **not automatically** the bare Cartesian product. Global authorization may be a shared owner permission or shared review budget, runtime effects can share resources or interact via reentrancy, and protected client observations can distinguish interleaving order.

### Theorem P6-C1 — sufficient local-to-global MAY composition (classical)

Assume:
1. Global *source states and authorized source-edit transitions* really are a framed asynchronous product S_1⊗S_2. An edit of i leaves the other component's source, ownership rights, and **all client-relevant effects** unchanged or observationally frame-equivalent.
2. Each local α_i is a forward simulation preserving action label and nonnegative cost in the same independently declared cost monoid.
3. The global protected old-client predicate and future demand interpretation are compatible with the component observation composition; for order-sensitive clients, the combined abstraction retains adequate labelled interleaving traces, rather than just event multisets.
4. Total edit cost is the declared associative, additive combination of local edit costs, and global authorization factors according to the framed rights assumptions.

Then α_1⊗α_2 is a forward simulation of every finite authorized concrete product repair path; the abstract MAY set overapproximates the concrete reachable repair-cost set.

**Proof.** Induct on path length. A first global action is a framed local action in exactly one component. Match it by that component's local simulation; frame/authorization conditions ensure the other component remains admissible and observations combine. Preserve the action cost and append the inductive abstract suffix. Goal and old-client predicates transfer by assumption 3. QED.

### Theorem P6-C2 — additional condition for exact repair-path lifting (classical)

In addition to P6-C1, if *each abstract local step* has a permitted executable concrete step for every related reachable concrete state, preserving cost and required old-client observations, and the framed product has **no hidden global authorization/resource coupling**, then every finite admissible abstract product repair path lifts to a genuine concrete path. Together with C1, this gives equality of attainable cost sets and their Pareto-minimal frontiers, for the declared state/client/edit language.

**Proof.** Induct on the abstract edit sequence; lift the current component step under the local backward simulation condition, using the frame to keep the other component and global rights valid. The symmetric forward result gives reverse cost-set inclusion. QED.

**Warning:** These hypotheses are strong and are NOT established merely by GitHub source metadata, an AST parse, or the fact that two public interfaces compile. They are the next source-extraction **proof obligations**, not accomplishments.

### Countermodel P6-N1 — global shared-rights budget

Take separate source components A,B each needing one edit. Each local abstraction sees an edit available at vector cost (1,0) or (0,1), and the naive product predicts both edits as a legal path of cost (1,1). But suppose the global concrete system contains **one jointly consumed authorization token**; either edit is permitted, yet after the first the other is forbidden. No path reaches the demand that both components be repaired. With two global tokens, both edit orders are allowed. Thus legitimate local repairs do **not** compose unless authorization factors. This refutes promoting source-file-level rights to program-level rights without a certificate.

### Countermodel P6-N2 — ordered effects remain observable

When local edit A emits event A and edit B emits event B, both schedules reach the same terminal source bits, but yield distinct client-observable traces `A,B` and `B,A`. A projection preserving only the final state or multiset of events is **not** fully abstract for order-sensitive protected clients. A valid compositional rule must retain the relevant trace alphabet and scheduling/frame hypothesis, or report UNKNOWN.

### Exhaustive finite control, and its limit

[Finite implementation](../../tools/p42/p2-r11/p10_p6_compositional_repair_rights_countermodels.py) and [read-only original GitHub CI #39022194658 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39022194658) enumerate 64 independent-source/right/irrelevant-tag states and 12 shared-budget states. The rights-complete quotient passes strong cost-labelled bisimulation; dropping rights does not. The budget-one counterexample blocks simultaneous repair, while budget-two permits (1,1), and distinct A→B / B→A event traces are retained as negative controls.

**Critical limit:** This is a *hand-specified finite edit semantics*, NOT automatic source-to-global-Go simulation certification. The seven P10-P5 source obligations G1–G7 remain open for the full real source and full client domain. The finite CI does not certify any third-party maintainer's actual source edit permission.

## IV. Noncircular SOLID implications and immediate research next step

Under independently validated framed edit supports and theorems P6-C1/C2, SRP/OCP/DIP/ISP/LSP may be derived as the **specific conditional port/client observations** previously set out in HARC R11-P5. However, for general programs with shared effects, rights, clients and histories those factorization premises fail, so neither SOLID's unconditional optimality nor a novel general architecture law is proved.

What matters next is to build a *proof-producing compositional source fragment checker* that accepts explicit effect/alias/rights certificates, rejects hidden shared budgets, and reports whether forward simulation and backward repair lifting are individually established. Compare its predicted future repair costs against an information-matched classical abstract interpreter and an actual independently authored source repair, not merely test the same simple class pattern repeatedly.

**Scientific disposition: P42 RUNNING; P10-P6 mathematically CLASSICAL/BONDED PASS, new global source soundness HOLD, P43 HOLD, LAW-R2 NOT_AUTHORIZED.**
