# R86 — Reclaim the Contextual Atlas by Prospective, Decision-Relevant Prediction
Date: 2026-11-23
Status: Research design, NOT a validated theory or completed empirical study.
Manuscript canonical page: https://app.notion.com/p/421ef561cf928129a180fd198217fe53
Context: Paper B v43/v45 original atlas agenda restored; v50 novelty objections still binding. R83 is supporting case study. LIRA is a rating aid, NOT the subject.

## Research program: compare *predictions* instead of competing representations

Core question: In real software changes, can a context-dependent warrant map, given the same evidence available to a rigorous typed ADR/AREL baseline, identify with less review effort which previous recommendations still apply, which are withdrawn, and which require review after a newly arriving requirement or changed policy?

The word "atlas" is not itself a scientific contribution. The prospective measurement is the proposed research contribution, subject to genuinely new prior-art review and independent data.

### Candidate A — Prospective Warrant-Survival Forecast (PWSF)
Before the outcome of a held-out change is known, timestamp a prediction of each existing rationale's state after the change. Allowed labels:
  PRESERVE / RECONSIDER / WITHDRAW / ABSTAIN.
A claim of PRESERVE means the *specific warrant* remains applicable under the revised context; it is not a claim that existing code will pass a new contract. All output labels require recorded provenance.

Key principle: Store the *pre-outcome forecast*, not a reconstruction after seeing the failing test.
Independent adjudicators define what the documented earlier warrant asserted; actual source tests independently judge code behavior. These are distinct gold labels.

Decision-relevant outcomes:
  - false preservation (critical missed reconsideration, predeclared cost)
  - false withdrawal (unnecessary redesign burden)
  - false alarm (reconsideration not needed)
  - correct retention and well-calibrated abstention
  - total capture + reading + revision + adjudication effort per episode
  - selective risk conditional on abstention coverage

Success requires better primary decision performance at comparable or lower total time than a strong fully informed ADR/AREL baseline, not a greater number of filled fields.
Cancellation: if a strong ADR achieves equivalent loss and lower total cost, separate atlas implementation is not justified.

### Candidate B — Counterfactual Repair-Regret Benchmark (CRRB)
For a version-pinned source snapshot and independently specified future requirement, run at least two feasible implementations or repairs against the SAME acceptance tests and contracts. Blind method proponents to the observed results at forecast time.
Record pre-outcome forecasts for (contract satisfaction, measured computation cost, estimated modification effort) with distinct outcome types. Only observable cost can be treated as truth; editing effort needs separately recorded human work.
Counterfactual data are available ONLY for the variants actually implemented and tested. No inference about every unrealized design.

Define observed pairwise cost regret for each admissible action a under context c:
  regret(a,c) = observed_cost(a,c) - min_{b in FEASIBLE_AND_OBSERVED(c)} observed_cost(b,c).
Invalid actions have CONTRACT_VIOLATION, not an artificially large numeric regret mixed into cost.
Do not select workloads after seeing outcomes. Use an independent source of future demands or presealed task episodes.
Cancel if case-dependent gains disappear under distribution shifts or rely on synthetic oracle labels.

### Candidate C — Minimum Sufficient Warrant Set (MSWS)
Given a decision episode and fixed independent outcomes, compare a full strong-ADR record, minimum subset selected from the same evidence, and an atlas map with equivalent access. Optimize the Pareto frontier between cost to create/maintain and the false-preservation loss. A smaller document is not automatically better; omission of rare safety-critical constraints is a failure. Do not call this novel until Falessi et al. 2013 and related active-selection/traceability literature are compared.

### Candidate D — Implicit Premise Recovery & Targeted Review
Candidate work must exceed existing premise-recovery baselines, not reproduce the idea. Nearby public source: Sandulu, Mesabah & Vollmer, *Premise Recovery in Software Design: What Does This Decision Rest On?*; web-accessed preliminary PDF reports ADR premises recovery, 1,060 ADRs from 36 repos, and held-out dependent review. Publication timing and all numbers must be independently reverified; don't claim a novel baseline here.
Potential contribution only if a new state transition (e.g., authorized contract invalidation) improves independently adjudicated review detection at less human cost than premise recovery alone.

### Candidate E — Conditional Principle-Dominance Regions
Compare OCP/YAGNI or other guidelines across actual contract and workload contexts. Avoid claiming a universal total order. Statistical support is contingent on selection protocol, and Simpson-style case selection bias (R49) must be controlled. Observing a different best action under two contracts is routine requirements engineering, not a new law.

## Fundamental prior-art collisions

- *Software Engineering Using RATionale* (2007) already reasons over requirements, criteria, assumption changes and impacts; no novelty from mere rationale propagation.
- AREL (Tang, Jin & Han, 2007) provides source-linked architectural rationale/traceability.
- *Change impact analysis for requirements: A metamodeling approach* (2014) explicitly models semantic change types and their propagation. Verify full text before claiming equivalence.
- Premise recovery from ADRs is being actively studied (2026 emerging work). Do not claim recovering hidden dependencies is new.
- Falessi et al. (2013) already investigates value of individual rationale information items; mere selective documentation is anteceded.

## Proposed first decisive trial (work plan, not conducted)

1. Freeze the exact unit: one external maintenance episode; separate cases by repository/developer to avoid pseudoreplication.
2. Freeze eligible episodes *without reading outcomes*; independent selector, immutable source SHA and issue creation cutoff.
3. Freeze pre-outcome evidence and user-provided policy authority; require version and timestamps.
4. Strong ADR + complete retrieval/traceability + forecast as baseline. Atlas gets the SAME evidence and tools; don't intentionally weaken ADR.
5. Two independent adjudicators: identify legitimate earlier warrant and revised applicable contract separately. Multiple annotators' agreement is NOT program behavior.
6. Both methods predict, with optional ABSTAIN, before reveal.
7. Reveal outcome and independently run behavior tests when appropriate. Score decision loss, false-preserve severity, coverage-adjusted risk, and TOTAL annotation time. Report unknowns.
8. Group-aware confidence intervals and sensitivity to cost weights; no pretend p-values without sufficient groups.
9. Stop separate implementation if strong ADR ties or beats it on the cost-correctness frontier.

## Research steering scores, only as aid (LIRA, subjective)

| Candidate | Originality possibility N | Discriminatory value V | Feasibility F | Prior-art collision K (higher worse) | Priority L |
| A | .36 | .95 | .72 | .84 | .96 |
| B | .44 | .94 | .62 | .80 | .94 |
| C | .21 | .86 | .80 | .95 | .90 |
| D | .18 | .82 | .60 | .96 | .87 |
| E | .29 | .80 | .73 | .88 | .85 |

These are not probabilities. Any novelty claim is gated by full primary-source comparison. E1 remains unexecuted; the already inspected Chi #1045 is development-only, not held out.
Implementation priority: first write the forecast receipt and loss protocol, then recruit independently selected episodes; avoid another large synthetic enumeration.

## Paper B editorial decision

Preserve the v45 core title and thesis: **The Axioms We Never Declared: Mapping the Conditions of Software Design Advice.**
New proposed contribution status: a *falsifiable prospective evaluation of the costs and outcomes of reasoning about revised warrants*; NOT a certified independent atlas calculus.
Add a subsection after v51 §7 identifying the predictions, feasible outcomes, abstention, and strong-ADR comparator. Do not present future experiments as completed.
