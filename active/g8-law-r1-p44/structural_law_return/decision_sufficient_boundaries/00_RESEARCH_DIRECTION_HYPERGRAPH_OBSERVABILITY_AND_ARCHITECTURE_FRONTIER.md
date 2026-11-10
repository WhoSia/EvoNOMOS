# EvoNOMOS — Decision-Sufficient Software Boundaries: Minimal Conflict Hypergraphs and Costed Observation Frontiers

**Research-direction prototype · 2026-11-11 KST · FORMALLY CHECKED FINITE PROTOTYPE · NOT A NOVELTY-ESTABLISHED THEOREM · LAW-R2 HOLD**

## 0. Research-lead scientific decision

EvoNOMOS's ambition is NOT merely a syntax rule, another SOLID slogan, generic design-rule recapitulation, or doing a fourth historical bug patch. We pursue a source-extractable, useful **decision boundary**: What information must a software boundary expose, and which actions must a maintainer be authorized to perform, in order to adapt correctly to distinct future maintenance environments **without exceeding the cost of building, observing and governing that boundary**?

The new direction is a **candidate research program**, not a confirmed mathematical invention. Parnas (1972) already theorized hiding decisions likely to change; Baldwin–Clark and design-rule research already price modular design options; classical Blackwell-style comparison and value of information already formalize better-informed Bayes decisions; finite hypergraph transversals are classical combinatorics. It would be false to treat the individual formulas as intellectually novel. The actual possible contribution is **a useful compositional, source-validated and prospectively predictive bridge** among (1) bounded legitimate source edit rights and old-client contracts, (2) observational distinctions across future demands, (3) minimal multi-context incompatible design requirements, (4) actual information-transfer and maintenance costs, and (5) reproducible equal-information classical rivals. We have not established that this combination is absent from prior research.

## 1. Why the existing archive leads here

- [EvoNOMOS founding constitution](https://app.notion.com/p/3cbef561cf928127a917c84bc0056546): identify conditional source-structural interventions, outcome reversals and failure boundaries rather than universal "SOLID helps."
- 2026-07 initial 0.3 *scripted synthetic* 2×3 architecture×maintainer experiments reported sign reversals and 0.4 valid DAG-dependency atom configurations; real independent maintainers/agents were NOT executed.
- [P37-MATH-K](../../../g8-law-r1-p37/P37_MATH_K_CLASSICAL_EXPRESSIVITY_BARRIER_AND_OWNER_OBLIGATION_IDENTIFIABILITY_COURT.md) proves unconstrained complete-source classical LTS has no truthful reachability discriminator; research differentiation must move to compressed observation, feasible action, cost, or causal generalization.
- [P44 founding six-role audit](../03_FOUNDING_LOGICAL_OBJECT_MULTIROLE_AUDIT_AND_DECISION_IDENTIFIABILITY.md) already proved a simpler common-optimum/fiber decision-sufficiency equivalence. Do NOT rebrand that old lemma.
- Independent original external [Restic issue #22140](https://github.com/restic/restic/issues/22140) proposes separating variable external storage billing policy from Restic's \`prune\` mechanism. [Original-source audit](../restic_future_policy_22140/00_ORIGINAL_RESTIC_SOURCE_AND_INDEPENDENT_POLICY_DEMAND_VERDICT.md) pinned 2024 Restic \`PruneOptions → planPrune → decidePackAction\` and distinct storage \`Backend/Repack\` operation. The 23 later Restic issues were audited as a denominator; #22140 is an outside user architectural request, NOT a user-approved specification or implemented source intervention.

## 2. Mathematical object and its observational provenance

Let finite demand/environment states \(\Omega\), weights \(p_\omega>0\), \(\sum_\omega p_\omega=1\), source-backed **observation interface** \(z:\Omega\to V\), and fixed feasible action menu \(\mathcal A\) (at this stage only *common* action menus: state-dependent source-owner permission remains an OUTSTANDING extension). Loss \(L(\omega,a)\) may be ordinary finite scalarized lifecycle cost, with weights and units stated. The attainable policy sees \(z(\omega)\) BEFORE acting, but not \(\omega\).

Define irreducible expected (oracle-relative) observation regret:

\[
\mathcal R(z)=\sum_{v\in V}\min_{a\in\mathcal A}
                 \sum_{\omega:z(\omega)=v}p_\omega L(\omega,a)
              -\sum_{\omega\in\Omega}p_\omega
                 \min_{a\in\mathcal A}L(\omega,a).
\]

All \(\min\) are **ex ante attainable expected cost**, no hindsight patch oracle in the policy. This is standard finite Bayesian decision theory. A finer deterministic observation cannot increase \(\mathcal R\) when its delivery and governance cost are excluded.

Define the action-optimum set \(\operatorname{Opt}(\omega)=\arg\min_{a\in\mathcal A}L(\omega,a)\). In a fiber \(F_v=z^{-1}(v)\) the existing observation admits *zero full-information oracle regret* iff
\[
\bigcap_{\omega\in F_v}\operatorname{Opt}(\omega)\ne\varnothing.
\]
This is P44's preexisting common-optimum criterion. Fulfilling it is not the same as achieving low real maintenance cost or out-of-sample architecture performance.

### A non-pairwise obstruction

For each observational fiber, let \(\mathcal H_v\) contain **inclusion-minimal** context subsets \(S\subseteq F_v\) with
\[
\bigcap_{\omega\in S}\operatorname{Opt}(\omega)=\varnothing.
\]
We call these *minimal decision-conflict coalitions*. The set system is a hypergraph, not necessarily an ordinary edge graph.

**Constructive three-context counterexample (verified by native exhaustive code)**. Three actions \(A,B,C\) and equally weighted contexts:

| Context | Loss(A) | Loss(B) | Loss(C) | Optimal actions |
|---|---:|---:|---:|---|
| \(\omega_1\) | 0 | 0 | 1 | \(\{A,B\}\) |
| \(\omega_2\) | 1 | 0 | 0 | \(\{B,C\}\) |
| \(\omega_3\) | 0 | 1 | 0 | \(\{A,C\}\) |

Every **pair** shares a zero-loss best action, but **all three** do not. A pairwise conflict graph has NO edges and falsely suggests no problem. The minimal conflict hypergraph has one 3-element edge \(\{\omega_1,\omega_2,\omega_3\}\). With no differentiating context signal, exact regret is \(1/3\). This is a classical finite-set counterexample, not claimed as a new theorem. It establishes that a proposed pairwise-only *software decision boundary classifier* is formally insufficient.

### A conservative explicit lower-bound certificate

For each context let \(g_\omega=\min_{a:L(\omega,a)>\min_b L(\omega,b)}[L(\omega,a)-\min_bL(\omega,b)]\), with \(g_\omega=0\) if all actions tie. Every actual decision \(a\) chooses a set of suboptimally served contexts \(T_a\). That set **hits every minimal conflict coalition** \(S\in\mathcal H_v\): if it didn't, \(a\) would be optimal for every \(\omega\in S\), contradicting the definition.

Hence a valid lower bound is:

\[
\boxed{
\mathcal R(z)\ \geq\
\sum_{v\in V}
\min_{T\in\operatorname{Transversals}(\mathcal H_v)}
\sum_{\omega\in T}p_\omega g_\omega.
}
\]

The inequality follows because every feasible policy's suboptimal-context set is an eligible hypergraph transversal, and its realized context loss is at least \(g_\omega\). **Not every transversal is necessarily the error set of some actual action**, so the inequality may be strict. An empty hypergraph yields a bound of zero. Both the three-way example and the two-world Restic example attain equality. This is an elementary derived combinatorial certificate in the above abstraction, *not* a proven new combinatorial theorem. It is potentially useful because it identifies small, inspectable conflicting witness sets instead of a huge unstructured source-state table.

Complexity is exponential in source context/action enumeration; a polynomial-time scalable checker is NOT provided. Minimal hitting set may be computationally hard. Source-to-\(\operatorname{Opt}\) extraction remains entirely unresolved.

## 3. The real Restic external requirement as a bounded mathematical instance

Same observed pack usage: unused fraction \(u=0.05\), 11 months remaining; hypothetical one-off rewrite price \(r=0.01\) normalized **pack-month**. This is **NOT actual Restic cost data, code behavior or cloud invoice**.

Two billing contexts with identical currently considered pack observation:
- \(\omega_L\): nonrefundable prepaid old pack, \(L(REPACK)-L(KEEP)=+10.46\): keep.
- \(\omega_M\): metered pay-as-you-go pack, \(L(REPACK)-L(KEEP)=-0.54\): repack.
- Hypothetical 50/50 context prior, NOT estimated from the 23 issues.

Without observing contract type: choose KEEP to avoid large expensive locked rewrite, but suffer regret \(0.5 \times 0.54 = 0.27\) normalized pack-month relative to an omniscient controller. Choose REPACK instead and lose \(0.5\times 10.46=5.23\); this verifies why KEEP is optimal with current information. The 2-element minimal conflict coalition yields **exact matching hypergraph lower bound \(0.27\)**.

If source-authorized interface exposes billing context *before the choice*, the model's decision regret becomes zero. But a signal costs engineering work, runtime query, maintenance, security review and possible governance; there is no free information miracle.

### Boundary-signal design frontier

For candidate source-authorized observation fields \(S\) with fixed prices \(c_j\ge0\), define:
\[
\mathcal F(\mathcal S_{\mathrm{allowed}})
=\min_{S\subseteq\mathcal S_{\mathrm{allowed}}}
\left[\mathcal R(z\oplus S)+\sum_{j\in S}c_j\right].
\]
This is a **finite feature acquisition/decision problem**, classically related to value of information and feature selection. It is not a purported new universal architectural law.

In the illustrative Restic two-context case:
- If a contract signal costs **0.10 pack-month**, use it: total \(0.10\) instead of \(\mathcal R(z)=0.27\).
- If it costs **0.40**, don't use it: total \(0.27\) instead of \(0.40\).
- If the maintainer is **not authorized to observe/receive** the billing signal, adding the feature is infeasible; regret remains \(0.27\) even at a nominal 0.01 price.

The inequality \(c_{\rm contract}<0.27\) is a **hypothetical break-even rule for this toy prior and toy costs**, not a claim about Restic profitability, best abstraction, or real storage economics. Signal price and prior must be measured independently for any real prediction.

### Why context combination may be genuinely more interesting

We also verified a four-world XOR-style client scenario: observing field \`x\` alone leaves regret 1/2, and observing \`y\` alone leaves regret 1/2, but observing **both together** reduces it to zero. This disproves naive independence or simple additive ranking of individual metadata fields for decision sufficiency. Again, XOR feature synergy is classical; the research challenge is detecting such *source-level interface* interactions under real future maintenance changes.

## 4. Executable results and what tests actually prove

[Reference implementation](decision_conflict.py) implements finite fiberwise Bayes risk, exact minimal incompatible optimizer hyperedges, minimum weighted-transversal lower bound, and exhaustive *source-permitted signal subset* cost optimization. [Research tests](test_decision_conflict.py) cover:
- Restic locked/metered regret 0.27, certificate tight;
- 3-way conflict invisible to pairwise checks;
- all **3^4=81** binary-action/three-cost two-context tables and **2^9=512** three-action/binary-cost three-context tables — **593** exhaustive cost configurations — verify \(\text{bound}\le\text{exact regret}\);
- refinements, missing info, explicit authorization gate, high vs low information prices and four-context XOR synergy;
- invalid probabilities and incomplete feature labels.

[GitHub Actions #42921991182 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/42921991182): **11 Python unit tests**, 593 finite cost-table checks, original mathematical examples printed. **NO new native Restic source patch, no source-ownership authorization check, no real coding agents or future requirement forecast** in this workflow. CI PASS establishes correctness only within the coded finite model, not research novelty.

## 5. Serious prior art and novelty audit (source-backed, not full literature review)

Primary public works reviewed via abstract/source landing and earlier original EvoNOMOS documents:
- Parnas (1972), *On the Criteria To Be Used in Decomposing Systems into Modules*, DOI [10.1145/361598.361623](https://doi.org/10.1145/361598.361623): hiding likely-to-change design decisions is established.
- Baldwin & Clark (2000) *Design Rules* / related options analysis ([HBS paper](https://www.hbs.edu/ris/Publication%20Files/01-075_3a180fce-22c4-4d49-97ed-956e3bdbccc8.pdf)): independently varying modules generate real options with exploration and visibility costs. Only search-retrieved excerpt inspected this turn; do not claim the entire PDF was read.
- Glynn et al. (2022) [NIST publication](https://www.nist.gov/publications/value-information-and-decision-pathways-concepts-and-case-studies): information acquisition has cost and value; broad prior art.
- [Prior-free Blackwell (2026)](https://link.springer.com/article/10.1007/s40505-026-00307-6) and [comparison of information structures (2024)](https://doi.org/10.1016/j.jet.2024.105841): information ordering / decision risk exist independently of this project.
- [Software design analysis and technical debt management based on design rule theory (2023)](https://doi.org/10.1016/j.infsof.2023.107322): source design-rule/debt measurement and option-oriented technical debt are substantial relevant prior art. No paper full-text reading claimed this turn.

**No established patent, paper, or claim of algorithmic novelty** from this small finite hypergraph tool. We must examine minimal conflict sets, source-change impact analysis, contract-based verification, Bayes risk and selective prediction literature more deeply before stating priority. If a strong prior art model gives the same compact source-action-conflict certificate at the same budget, the correct outcome is a CLASSICAL TIE. A source-level predictive generalization could still offer software-engineering contribution without an original math theorem.

## 6. The real potentially publication-worthy questions (not solved yet)

1. **Extraction theorem:** Given real typed source edit rights \(\Gamma\), old/new client contracts and program dependency structure, can a compositionally computable source invariant soundly overapproximate minimal *decision-conflict coalitions* without enumerating all futures? Tight soundness, precision and complexity bounds would be nontrivial. Current prototype does not read Go source; it receives a predeclared cost table.
2. **Architectural boundary design:** Can we introduce a *minimal set of source-visible metadata and permitted policy actions* that measurably reduce out-of-sample maintenance-policy regret after charging implementation and review cost? We need real competing old-correct R0/R1/R2 source variants and authentic later demands.
3. **Action-rights interaction:** Even with perfect observation, a needed action may be barred by owner permissions; compare separately **information regret** and **authority regret**, neither conflated with bug reachability. With varying action feasibility by context, the current common-action loss formula **must be extended**, not misapplied.
4. **Maintainer interaction:** Different agents have different information search costs and ability to use exposed fields; test on actual source-repair attempts with identical source/time rights and independent tool logs. Initial 0.3's synthetic interaction cannot validate real actors.
5. **Adversarial evaluation:** Against Parnas/DSM/full-source static analysis, Blackwell value of info, decision-focused feature selection and exact source LTS at their appropriate budgets. No impossible "beat full-information oracle" challenge.
6. **True source experiment:** Independent Restic #22140 offers a real *request* but not yet a complete accepted client oracle or implementation. A production-safe dry-run/plan-export interface must specify race/TOCTOU, stale pack versions, allowed deletion, external engine outage and protocol versioning; do not test against real user repository data or claim security.

## 7. Research-lead verdict

**KEEP as primary new mathematical research candidate:** observability-induced minimal action-conflict hypergraphs plus costed boundary-signal frontier, applied to real source decision structures. It is more discriminating than "more modular = better" and directly gives falsifiable information/pricing/authorization conditions.

**DO NOT PROMOTE AS NEW LAW:** finite decision risk, weighted hitting sets, 3-way non-Helly example, signal costs and simple 0.27 break-even are mathematically classical or straightforward consequences, and source-to-cost inference is unverified.

**NEXT EXPERIMENTAL GATE:** perform independent source-level bounded old/new client policy-action R0/R1 experiments **before proposing R2's high-IPC complexity**; preregister actual source contracts and scope; model real permitted actions and costs; validate changes across independent later user demands. If actual coding agents are unavailable, do not manufacture a scripted-maintainer effect.

**P44 OPEN / G1–G7 OPEN / LAW-R2 HOLD.**
