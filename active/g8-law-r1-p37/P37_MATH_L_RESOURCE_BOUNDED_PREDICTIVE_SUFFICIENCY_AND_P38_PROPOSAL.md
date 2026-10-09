# P37-MATH-L — Resource-Bounded Predictive Sufficiency, Owner–Obligation Information Geometry & Prospective Structural-Law Separability

**EvoNOMOS Generation VIII LAW-R1-P37 · 2026-10-10 KST · THEORY-FIRST / BOUNDED CLASSICAL AUDIT.**

**Authority:** P37 OPEN · MATH-L finite classical results · DIP49 IDENTIFICATION HOLD · LAW-R2 NOT_AUTHORIZED. **P38 proposed after this phase, NOT opened or authorized here.**

Lineage: [MATH-J contextual minimality](P37_MATH_J_COMPOSITIONAL_MINIMALITY_CONTEXT_CLOSURE_AND_AUTHORITY_PARTITION_RECONFIGURATION.md) → [MATH-K strong-classical non-separation](P37_MATH_K_CLASSICAL_EXPRESSIVITY_BARRIER_AND_OWNER_OBLIGATION_IDENTIFIABILITY_COURT.md) → this distinct **budgeted-identifiability** court.

## Research question, precommitted models, and observational contracts

MATH-K showed that complete correct classical reachability and any complete correct new reachability law cannot disagree on exactly the same fully given transition model. MATH-L attacks the **resource-limited source-evidence problem** rather than claiming an expressivity breakthrough. Fix before predicting:

- Source/evidence: existing pinned upstream Gorilla CookieStore + SCS APIs; **only the existing P37-E4 researcher-authored finite repair graph** is queried for outcome labels. The independently evolved upstream code and original-Go CI have already been audited; they are **not** rerun here.
- Valid-start selection: original G issuer + original G-only reader + historical G-cookie obligation, with G decoder authority **known true**. This eliminates misleading comparisons whose starting invariant already fails. The future goal is S issuer + S-only reader + historical duty expired.
- Hidden three-bit context: \(x=(k_S,b,e)\). \(k_S\) is authorized access to **the matching** SCS store; \(b\) grants owner B the dual-reader edit; \(e\) permits an **external legal expiration** of old-history obligation. All \(2^3=8\) configurations are admitted as *synthetic* distinct contexts within the fixed E4 graph.
- Outcome: \(\;Y(x)=\operatorname{May}_{\Gamma(x),I}(s_0,g)\in\{0,1\}\). E4 graph reachability agrees with \(Y(x)=k_S\land b\land e\) for these 8 contexts. That formula depends on this **bounded** grammar and fixed goal; different original-source edit authority, atomic deployment, or legacy policy changes the result.
- Information oracle \(\mathcal O_i\): one query reveals exactly **one** hidden coordinate \(x_i\); direct inspection of the other coordinates is prohibited by experiment definition. The structural Boolean formula, source API facts, prior, and feature identities are **available to all competitors**.
- Information budget \(B_I\): at most \(B_I\) distinct oracle queries, no backdoor access. Computation budget \(B_C\): at most \(B_C\) successor expansions in a different specified **discovered-handle graph oracle**. These are **different units**; neither measures elapsed CPU seconds, Go patch count, bytes of real source read, nor natural maintainer effort.
- Fair full-information classic \(B_*\): knows exact \(\Gamma(x),I,G\) and solves classical reachability without further state uncertainty. Fair *budgeted* classic \(B_{I,C}\): knows the SAME source structure, AND formula, cost model and oracle/budgets as \(H\); it may choose adaptively and abstain. A strawman with less information is only a restricted ablation, not \(B_*\).

No new real-world holdout or fresh human ownership evidence is supplied. This is mathematical court, **not** empirical causal effect identification.

## L1 — Exact source-tethered information certificates, including abstention

Assume the three hidden bits are logically independent across the eight **admitted worlds** and the oracle exposes only bit answers. A partial observation is an assignment \(u\) to some coordinates. Its completion fiber \(F(u)\subseteq\{0,1\}^3\) contains every world consistent with the queries.

A **sound exact certificate** is an observed \(u\) with \(Y\) constant on \(F(u)\); then and only then can a uniform zero-error evaluator decide without further information. This is exactly the kernel/fiber factorization principle already established by MATH-I/K, not a new proof idea.

For conjunction \(Y=k_S\land b\land e\):
- a **negative** certificate is any one observed false bit;
- a **positive** certificate requires all three observed true;
- on the all-true world any algorithm with \(B_I<3\) leaves a last unobserved coordinate, and the world with that coordinate false is observationally indistinguishable. **Every deterministic or randomized uniformly zero-error evaluator therefore needs worst-case 3 bit queries.**
- with three queries it can short-circuit on false and conclude on all-true. Hence exact deterministic worst-case query complexity is **3**.

Under an **explicitly hypothetical uniform distribution on the eight valid-start worlds**, and for any fixed permutation of the three distinct bit queries, the fraction of worlds still unresolved at budgets 0,1,2,3 is respectively \(8/8,4/8,2/8,0/8\). Both a sound evaluator and the strongest budgeted classical decision tree predict the same abstention counts; selective prediction must distinguish abstention from an incorrect answer.

**Hard classification paradox (negative control):** For every \(B_I<3\), the lowest possible uniform zero-one misclassification count is **1 out of 8** (the lone all-true positive can always be paired with an opposite-label completion; predicting always false achieves the bound). Accordingly raw accuracy 7/8 with **zero queries** is possible without having identified positive repair. This is why an apparently good static accuracy percentage is not evidence for any design law.

**Scope and failure boundary:** If the prior/contract implies any hidden bit from another, if one query leaks multiple bits, if only a restricted subset of worlds is admissible, or if the evaluator accesses full original deployment records for free, the complexity and certificates may change. No empirical distribution is inferred.

## L2 — Stochastic cost-aware query ordering is classical

Let \(p_i=P(x_i=1)\), \(0<p_i<1\), and positive query costs \(c_i\). Under an expressly *synthetic independent product prior*, an exact strategy evaluating conjunction queries bits until a false bit is seen. For order \(\pi\),

\[
\mathbb E C_\pi
=\sum_{j=1}^{3}c_{\pi(j)}\prod_{r<j}p_{\pi(r)}.
\]

An adjacent exchange shows \(i\) precedes \(j\) iff \(c_i(1-p_j)\le c_j(1-p_i)\), or equivalently the classical nondecreasing ratio \(c_i/(1-p_i)\). This is standard sequential testing / Stochastic Boolean Function Evaluation, **not** a new structure theory.

For a **deliberately hypothetical**, not measured, prior and expense table:

| Named source/authority feature | \(P(x_i=1)\) | Query cost (arbitrary units) |
| --- | ---: | ---: |
| matching SCS store \(k_S\) | \(3/4\) | 4 |
| owner B dual-reader authorization \(b\) | \(1/2\) | 1 |
| historical duty expiry permission \(e\) | \(1/4\) | 2 |

Optimal order \(b\to e\to k_S\) has \(\mathbb E C=5/2\); naive order \(k_S\to b\to e\) costs \(11/2\). The verifier exhaustively evaluates **all 3! permutations**, and the strongest informed classical evaluator chooses **the same optimal order**. These are numerical illustrations, **not measurements of source-maintenance costs, not evidence that EvoNOMOS improves over the prior art**, and not a statement that expiry is legally controllable in an actual deployment.

## L3 — Computational (successor-expansion) budget obstruction: different oracle, different claim

The finite E4 graph contains only 12 abstract typed deployment states; given its **whole explicit adjacency list**, ordinary reachability runs in \(O(|S|+|\Gamma|)\) time. The E4 model does **not** justify a new computational hardness claim.

Instead, as a separate **synthetic discovered-handle successor-oracle family**, for any integer expansion budget \(B_C\ge0\), construct two chain graphs with identical first \(B_C\) successor replies and identical visible prefix. At the next newly discovered node, graph \(G_+\) supplies an edge to an accepting goal while \(G_-\) dead-ends. An algorithm can query only a previously discovered node handle; it does not know the complete adjacency table, cannot guess an undiscovered handle or use a separate goal-reachability oracle.

Any algorithm limited to \(B_C\) successor probes receives the **same transcript** in the two graphs and therefore cannot decide reachability correctly in both. The \((B_C+1)\)-st probe separates them. The checker confirms witnesses for \(B_C=0,\ldots,8\) (18 graph-world executions). This establishes a **relative graph-oracle information lower bound**, *not* a generic CPU runtime lower bound, PSPACE-hardness, or a factual claim about actual original-Go source changes. Under a fully disclosed finite graph the obstruction disappears.

The two budgets therefore cannot be collapsed into one score: the information gap is missing context-bit authority/obligation values; the computational gap is restricted access to successor information. Modeling full graph input or direct source inspection changes the oracle and the result.

## L4 — Equal-budget strongest-rival falsification

The actual matched rival is **adaptive** and knows the source-derived conjunction exactly. It may query the same hidden bits, short-circuit negatives, compute the optimal classical stochastic order under the same priors/costs, and abstain when necessary. It achieves **identical zero-error certificates and costs** to the proposed owner/obligation-guided model in this court.

| Contract | Structural candidate \(H\) | Strong exact / budgeted classic \(B_*\) |
| --- | --- | --- |
| All three true, under budget 2 | abstain | abstain |
| Any discovered false bit | certify no May | certify no May |
| All three true, under budget 3 | certify May | certify May |
| Equal synthetic independent p/c | query \(b,e,k_S\), expected \(5/2\) | **same** |
| Discovered-handle graph, limited expansions | may remain unable to certify | **same** |

Therefore **prospectively distinct outcome signature on the current court = 0**. A source/authority-aware description remains potentially valuable for practitioners but is not mathematically or predictively superior to a well-specified classical baseline. Parnas's information hiding and option-sensitive structural design already contest generic claims that SOLID metrics ignore future changes.

## Executable and reproducibility contracts

[Independent Python checker](../../tools/p37-math-l/resource_identifiability.py) invokes the *unchanged* E4 restricted graph as an outcome oracle for valid-start contexts; verifies all **8** labels, computes classical minimum decision-tree depth, checks **6 query orders × 4 budgets × 8 worlds = 192** evaluations, their decision/abstention obligations, exact expected costs for **6** orders via \`fractions.Fraction\`, and **18** synthetic graph-oracle transcript cases. These are exhaustive within the stated finite configurations, not 192 independent original code runs. [Read-only workflow](../../.github/workflows/g8-p37-math-l.yml) must report success before hosted execution is claimed.

Prohibit proof through fabricated changes to the E4 original code or post hoc oracle. Do not treat Python assertions as Lean kernel proof or randomized population transport.

## Literature priority and novelty boundary

**Drive primary-source passages checked:** [Parnas (1972), *On the Criteria To Be Used in Decomposing Systems into Modules*](https://drive.google.com/file/d/1EcQRy3iehx4lUN7uGsZ1BFXU33HggcEQ/view) explicitly compares modular work assignments whose executable representation can coincide; design for change is not invented here. [Sullivan, Griswold, Cai & Hallen (2001), *The Structure and Value of Modularity in Software Design*](https://drive.google.com/file/d/1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr/view) already develops design-structure and option-value analyses with cost-dependent modular choice.

**Explicit further prior art, not asserted to be in Drive:** [Deshpande, Hellerstein & Kletenik (2013), *Approximation Algorithms for Stochastic Boolean Function Evaluation and Stochastic Submodular Set Cover*](https://arxiv.org/abs/1303.0726). Stochastic function evaluation treats unknown Boolean coordinates, test costs, and adaptive evaluation; deterministic query complexity is classical. No novelty is claimed for the ratio rule, certificate complexity, partition factorization or adversarial oracle argument.

## P37 closure gate and **P38 proposal only**

**MATH-L verdict:** finite mathematical/bounded E4/source-tethered oracle checks, strongest classical equal-budget model undefeated. No resource-realistic software predictive law or new cross-project owner-graph empirical result established. No further third-party Go test justified by this court.

**Recommended next version name (not OPEN yet):**

**EvoNOMOS Generation VIII LAW-R1-P38 — Prospective Structural-Law Identification under Information and Compute Budgets: Minimal Repair Certificates, Owner–Obligation Observability & Equal-Resource Rival Falsification**

*Why a flowing P38 transition would make sense:* P37 has extracted the local future-sufficient kernels, contextual criteria, authority-vs-invariant obstructions, and exact budgeted **non-identification** boundaries. P38 would own the distinct scientific question of building a **source-derived, prospective, resource-realistic, rival-discriminating conditional software design predictor**, not another finite graph proof or library replication. Its opening requires owner authorization; it inherits DIP49 HOLD, non-universal SOLID status, actual source-grammar limits, and the failure of strong-classical separation.

A prospective P38 stage should register **before fresh outcomes** a matched evidence-access + time/graph-query budget, real independent upstream maintenance demand, actual—not invented—edit owners/capabilities and invariant, cost oracle and measurement contract, full strong baseline/ablations, and explicit **discordant predictions**. If the strongest fair rival agrees, preserve NO_SEPARATION and do not open an external native trial. If H only wins by seeing extra inputs, classify information advantage, not beyond-classical identification.

**Final scientific state:** P37 OPEN · MATH-L finite classical identification bounds · DIP49 IDENTIFICATION HOLD · LAW-R2 NOT_AUTHORIZED · P38 NAME PROPOSED ONLY.
