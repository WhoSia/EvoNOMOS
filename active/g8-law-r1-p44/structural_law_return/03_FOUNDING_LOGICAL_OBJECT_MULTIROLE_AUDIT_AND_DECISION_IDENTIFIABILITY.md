# EvoNOMOS — Founding Logical Object, Six-Role Adversarial Audit and Decision Identifiability

**2026-11-10 KST · EPISTEMIC CORRECTION / MATHEMATICAL AUDIT · NOT A NEW LAW, NEW CI, OR GATE PROMOTION**

## 0. Source authority and scope

The founding Notion Constitution and Origin & Drift Audit unambiguously define the object: discover *falsifiable conditional structural interventions* in source-level software organization that change a vector of lifecycle outcomes under the **same old and future functional requirements**, and predict sign/Pareto reversals in independent environments. The goal is NOT to axiomatize SOLID as a universal theorem, create bigger certification/receipt systems, or get an exact finite graph to beat itself under a different name.

Audited original documents:
- [Founding Constitution](https://app.notion.com/p/3cbef561cf928127a917c84bc0056546) — scope/condition/action/effect/failure boundary, causal intervention and vector outcomes.
- [Origin & Drift Audit](https://app.notion.com/p/3c8ef561cf9281faa057d75c35762837) — explicit recurring means/end inversion, 2026-09-30 deeper-theory aspiration.
- [P35 real Chi changes](../..//g8-law-r1-p35/P35_P4_P4B_REAL_CHI_TWO_DEMAND_TOURNAMENT_VERDICT.md) — 2 vs 3 initial Go files; 2 vs 1 next-demand modified files; no full held-out sign inference and B0+/B2 not defeated.
- [P37-MATH-K classical expressivity barrier](../../g8-law-r1-p37/P37_MATH_K_CLASSICAL_EXPRESSIVITY_BARRIER_AND_OWNER_OBLIGATION_IDENTIFIABILITY_COURT.md) — exact full-information classical LTS expresses the same repair May label; restricted-information factorization theorem already known.
- [P40-MATH-A](../../g8-law-r1-p40/P40_MATH_A_OBJECT_REPAIR_STRUCTURES_AND_SOLID_STRICT_REDUCT_PROGRAM.md) — typed source/rights/client/partial composition model, strictly scoped SOLID* proxies, global gluing obstruction but classical naming constraints explain.
- [P42-R5](../../g8-law-r1-p42/P42_P2_R11_P10_P13_R5_ACTUAL_CHI_1215_SOURCE_PATHS_384_NEW_COMPOSITE_REPAIR_GOALS_RESULT.md) and [P42-P14](../../g8-law-r1-p42/P42_P2_R11_P10_P14_DISCLOSURE_ORDER_REPAIR_OPTIONS_SOURCE_GRAPH_MATH.md) — actual-source-supported restricted edit grammar, classical option antitonicity, crucial information-disclosure quantifier order.
- [Zerolog original historical replay](02_ZEROLOG_REAL_MAINTAINER_CONTEXT_REPAIR_HISTORICAL_VERDICT.md) — original real merged bug fix, already read before tests; no blinded prediction, full-information dataflow competitor tied.

## 1. Correct mathematical scientific object

Let:
- $A\in\mathcal A$: actual source architecture chosen *before* later demand;
- $e=(r,w,t,h,\Gamma)$: future requirements/time order, workload, tooling, maintainer and *authorized edit constraints* (the latter may change over time);
- $C_0$: protected present and accumulated clients; $d$ future demand;
- $x(A,e_0)$: **available-at-design-time** covariates, with information cutoff; later unrevealed $d$ is **not** allowed in $x$;
- $p(x)$: architecture/design action under a declared admissible action class;
- $\pi$: later feasible source-repair policy, conditional on genuinely disclosed observations;
- $Y(A,p,\pi,e)\in\mathbb R^k$: correctness, incremental/initial labor and edits, runtime, defect risk, cognition, deployment; no forced single score.

The experimental causal quantity is a same-contract, same-demand *paired intervention effect*:
\[
\Delta_j(A,e;p_1,p_0)
=Y_j(A,p_1,\pi^*_{p_1},e)-Y_j(A,p_0,\pi^*_{p_0},e)
\]
for a **stated** repair policy class $\pi^*$, allowed rights and horizon. The architecture intervention cannot quietly change the new requirement or old contract. If intervention/repair are jointly optimized, their allowed budget and optimization algorithm must be disclosed. Potential outcomes from real projects require identification assumptions and controlled assignments; observed pull-request diffs do not identify counterfactuals by themselves.

For an explicitly stated nonnegative preference/utility weight vector $w$ only, define cost $J=w^\top C$; otherwise retain the Pareto vector and do not rank incomparable designs. Discovery objective: find stable, source-observable moderator $m$ making a sign/recommendation boundary predictive OUTSIDE the training case, after strong conventional baselines. Not claim novel mathematics merely from defining a state graph.

## 2. Previously overlooked logical trap: stronger-than-omniscient oracle is impossible

**P37-MATH-K had already proved** that any complete classical source/contract/permission transition system computes the exact same May property as a sound/complete EvoNOMOS repair solver. A demand for a *different correct May value* from the same complete information is contradictory. Repeating it in F27–F34 as a novelty gate conflates scientific ambition with impossible representation separation.

Correct competition must be **specific about cost and information**: fixed finite observation budgets, structural feature acquisition costs, source-extraction soundness, sample efficiency, generalization to independent demand families, causal effect under real interventions, algorithmic scaling or succinct explanatory invariants. Classical rivals must receive the SAME information actually accessible at the relevant decision time and a fair training/compute budget. A full-information LTS can remain the correctness reference; it need NOT be beaten on exact truth.

## 3. Finite decision-sufficiency lemma (classical; an audit instrument, NOT a newly original theorem)

Let $\Omega$ be a **finite** set of genuinely possible decision contexts and $T$ a fixed finite design-action set. Let $z:\Omega\to Z$ be a feature representation containing only information revealed at design time. Let $J:\Omega\times T\to\mathbb R$ be a **finite real** scalar cost with fixed meanings/weights (or encode inadmissibility by a sufficiently large *finite* penalty). Define oracle loss $J^*(\omega)=\min_{t\in T}J(\omega,t)$ and regret $R(\omega,t)=J(\omega,t)-J^*(\omega)\ge0$.

**Proposition.** There exists a deterministic policy $p:Z\to T$ with **zero worst-case regret over every context** iff for every feature fiber $F_z=\{\omega:z(\omega)=z\}$,
\[
\boxed{\bigcap_{\omega\in F_z}\operatorname{Argmin}_{t\in T}J(\omega,t)\ne\varnothing.}
\]
**Proof, necessity:** a single $p(z)$ must be chosen for every $\omega$ in the fiber. Zero regret requires this same $p(z)$ to minimize $J$ at each $\omega$, so it belongs to the intersection. **Sufficiency:** independently choose an action from the nonempty intersection for each nonempty fiber. Its regret is zero for every constituent context. QED.

The optimal **fiberwise deterministic minimax regret** is
\[
\rho(z)=\min_{t\in T}\max_{\omega\in F_z}\left(J(\omega,t)-J^*(\omega)\right),
\]
which is positive precisely when the argmin intersection is empty. This is elementary finite decision theory, extending the older P37-MATH-K binary label-factorization question from "can this projection predict a fact?" to "can this projection choose an action without avoidable regret?" **This is not theoretical novelty by itself.**

**IMPORTANT:** If future demand is not revealed at decision time, even an excellent policy cannot choose different actions in two contexts sharing $z$. Its positive oracle regret is an **irreducible information limitation**, not a failure or inadequacy of the proposed architecture theory. Only compare against the best policy permitted to see the same $z$. Full-information oracle is an upper bound, not a fair practical competitor.

A check of all $4^4=256$ two-context/two-action cost matrices taking costs in $\{0,1,2,3\}$ found zero discrepancies between the proposition's two sides. This only sanity-checks the finite proof; it is **not source evidence**.

## 4. Re-read the empirical evidence without turning proxies into laws

P35's measured **production-file visits**:
- first new demand D4: independent=2, shared=3;
- second demand D5 *incremental*: independent=2, shared=1;
- cumulative through D5: 4 vs 4 file visits, **a tie**.

Illustrative UNTESTED extrapolation if there are $k$ **additional requests with the exact same edit footprint**:
\[
C_I(k)=2+2k,\quad C_S(k)=3+k,\quad C_S-C_I=1-k.
\]
For $k=0$ independent wins; $k=1$ tie; $k\ge2$ shared wins. Direct arithmetic, not observed future projects, not real labor effort. If a future history contains random $K$ same-kind maintenance demands, and this proxy remains linear, $\mathbb E[C_S-C_I]=1-\mathbb E K$; any practical threshold requires an empirical demand distribution and heterogeneous effort coefficients. This is established modularity/setup-vs-maintenance economics, not a new conditional law.

P42's $\operatorname{Future}(Y)\subseteq\operatorname{Future}(X)$ after a legitimate $X\to^*Y$ is tautological from path concatenation for a FIXED demand family, rights grammar and old obligations. More currently satisfied goals or cheaper target cost at $Y$ does not contradict it. But option antitonicity alone does NOT establish that delaying edits is optimal: it says nothing about the utility of current work, delay penalties, demand revelation and acceptable repair budgets. P42-P14 already proved the necessary $\forall d\,\exists$ vs $\exists\,\forall d$ timing distinction: reuse it, don't rediscover it.

P36-O9's Chi-vs-Gorilla source contrast changes between INCOMPATIBLE contracts Q_specificity and Q_registration_order. It is valid contract-indexed **feasibility reversal**, NOT a same-Q engineering cost sign reversal.

Zerolog PR #811 correctly illustrates how an object-copy operator fails to preserve hidden state, but historical solution was known and ordinary Go field def-use analysis predicted it completely. Such examples are causal mechanism *illustrations*, not independent discoveries.

## 5. Six independent adversarial reviews

**(R1) Mathematician:** The state tuple is a definition, not an axiom system proven to derive original SOLID. Exact finite reachability and antitonicity are classical. The only honest next question is a falsifiable *nontrivial restriction or efficient invariant* with new implications. Avoid rebranding finite transition logic as new law.

**(R2) Programming-language semanticist:** “Preserves old client” means preserves the declared observation/context grammar, not all possible Go contexts. Dynamic types, reflection, aliasing, races and ownership can invalidate source-to-abstract path lifting. G1–G7 OPEN cannot be silently erased by green narrow tests. Distinguish LSP semantic constraints from OCP/DIP design economics.

**(R3) Causal inference reviewer:** An observed old vs fixed PR does not isolate the treatment effect of an *architectural alternative* under the identical future customer demand. Confounding from different clients, intervention budgets, programmer strength and post-treatment repair selection must be controlled. Use matched pairs and preregistered directions; separate author-visible source proofs from truly outcome-blind task predictions.

**(R4) Empirical SWE reviewer:** Changed files, generated snapshots and test counts are surrogate metrics. File-level edit visits ignore file size, cognitive cost, testability and future followups; P35 net result through two changes was 4–4. Report the quality vector and uncertainties, not a symbolic sign over proxy counts as if engineering welfare were established.

**(R5) Prior-art and novelty reviewer:** Parnas, Sullivan et al., Baldwin–Clark, DSM, ordinary guarded LTS/dataflow, and P37-MATH-K already explain many claimed results. P37's full-information expressivity ceiling means “beat exact classical LTS on exact May” is invalid. Compete on grounded empirical moderator predictions, sample efficiency, usable policies, bounds or genuinely stronger source theorems, not invented result distinctions.

**(R6) Skeptical systems architect:** No architecture can be selected from facts only learned after a demand has arrived unless the design decision can be deferred. A purported policy must name the choice time, available telemetry, authorizations, customer contract, allowed repairs, risk and abandonment option. If no actionable condition emerges for an actual maintainer, treat the research statement as descriptive rather than prescriptive.

## 6. Revised core research gate, starting immediately

A new experimental mainline must supply, **before any treatment outcome is viewed**:
1. A real source architecture pair both satisfying the **same** frozen current customer contract. Source clones and architecture variants must be authentic and identifiable.
2. At least one not-previously-opened real future maintenance request, independently sourced and frozen **before inspecting its solution/diff**; verify training/test cutoff by immutable commits. If already read, classify retrospective and do not claim C5.
3. A bounded design action and honest exposure timeline $z$; no future requirement leakage into the action choice.
4. Source-grounded structural moderators for interface stability, responsibility/ownership boundary, co-change, information flow; a predeclared predicted effect/reversal with falsifiers.
5. Strong equal-observation conventional alternatives (refactoring, static impact/DSM, source-aware dataflow, options economics), same requirements and repair-budget limits.
6. Multiobjective actual outcomes: old/new functionality, edit effort and burden, regression, runtime, tests, human/agent execution distinctions; Pareto incomparability is an allowed result. Unknown owner-right means HOLD, not $\infty$.

**Stop rule:** if the same-info classical model completely explains the outcome, record a legitimate negative and move to a *new* independent structural moderator; don't run another equivalent source archetype merely to count CI passes. If a truly effective new rule arises, derive its assumptions mathematically and validate out-of-sample BEFORE trying to present a broad theorem about SOLID.

## 7. Decision

**Scientific object preserved:** discover the conditions under which interventions on real software organization alter future lifecycle quality and when their advantage reverses. **Observed drift real:** recent F33/F34, pflag and zerolog primarily generate narrower descriptive confirmations with no newly predictive architecture-selection rule. **Mathematical correction:** move from “source repair possibility is computable” toward **information-timed, regret- and causal-effect-grounded structural policy identification**, but acknowledge this is preexisting decision theory until independent source evidence and new mechanism support a substantive law.

**No new law. No theorem priority. No blind future result. No LAW-R2 authorization.**
