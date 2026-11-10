# EvoNOMOS — P35 Historical Repair-Gate Decision Risk: Consequence of the Early Maintainer Audit

**2026-11-10 KST | original P35-P5 aggregate evidence repricing | 6 native Python CI tests PASS | NO new prospective empirical observation or source architecture causal effect**

## A. Why this is a genuine move after the origin review

Archived EvoNOMOS 0.1–0.4 establishes that architecture effects are conditioned on **maintainer, policy information and evaluator**, that raw edit similarity does not estimate maintenance labor, and that principled source-localization hints can help or hurt depending on search/inspection costs. The already-completed [P35-P5 actual original Chi Git history audit](../../../../g8-law-r1-p35/P35_P5_GO_HISTORICAL_PREDICTION_AND_COCHANGE_BOUNDARY.md) supplied an especially important adverse dataset: three tools could rank likely neighboring files but **all automatically produced a false extra-file warning for all 34 actually single-file edits**. A risk-aware choice may be better served by not triggering the repair action at all.

This is exactly the two-stage causal decision that many recently published F33/Viper test passes did not inspect:
- Gate G: should the maintainer inspect/edit any other file?
- Rank R: *conditional on G*, which location?
- Execute M: can a permitted maintainer patch a truly required location within the allotted observation/repair budget?

Current P35 aggregate evidence allows a reanalysis of G/R selection, NOT a fresh result on M.

## B. Verified original P35 data and limitations

Original sealed Go Chi P35-P5 holdout 2020–2024 had **40 distinct qualifying production commits**, generating **47 seed-file queries** (not independent). Of those queries, **13** had at least one other edited file, **34** were singletons, and historical B0+/B1 source/commit top-one ranking hit 9/13, B2 Parnas-like qualitative ranking 8/13; **every source baseline alerted on every singleton**. A top-one hit is not a proof the edit was necessary: actual source Git co-edits are observational labels, not a semantic repair oracle.

The following model does NOT use the unavailable per-event original cost, actual human labor, task labels, runtime CI patch outcomes or a recalibrated classifier. It simply recomputes **bounded expected decision loss from known aggregate counts**.

## C. Cost-sensitive comparator changes the recommendation

Let alpha≥0 be cost of a false extra-file alert, beta≥0 the cost of failing to alert on a real multi-file change, gamma≥0 the *additional* cost of pointing to the wrong extra-file location. P35 B0/B1 has 9 true top-one hits, four positive misses and 34 false alerts.

For the policy A = "always recommend an extra-file site using B0/B1":
\[
L_A=34\alpha+4(\beta+\gamma).
\]
For the policy N = "do not alert":
\[
L_N=13\beta.
\]
At fixed beta>0 the alert policy is better iff:
\[
\boxed{\frac{\alpha}{\beta}<\frac{9}{34}-\frac{4}{34}\frac{\gamma}{\beta}.}
\]
- If gamma=0: the break-even false-alert/miss cost ratio is **9/34≈26.47%**.
- If gamma=beta: threshold is **5/34≈14.71%**.
- If alpha=beta=1,gamma=0: always-alert loss **38** while abstain **13**.
- If alpha=0.1,beta=gamma=1: always-alert loss **11.4** versus abstain **13**: **cost preference reverses**.

B2 with 8 correct source locations has threshold (gamma=beta) **3/34≈8.82%** under the *same* scoring convention. This is ordinary weighted classification with abstention, not a novel information-theoretic or causal result.

**WARNING:** The "never alert" comparator is not a strategy for meeting unknown production requirements; it has 13 misses in this dataset. The cost model is deliberately explicit, and actual costs/uncertainty are not inferred. Also conditional rank and gating quality are separate: improving rank without reducing all-singleton false alerts can be worse than a less accurate but selective system. Strong classic selective classifiers are not evaluated here. Label independence cannot be assumed because multiple seed queries come from one commit.

## D. Native computation / exact provenance

[Source evidence](../../../../g8-law-r1-p35/P35_P5_GO_HISTORICAL_PREDICTION_AND_COCHANGE_BOUNDARY.md) supplies only the counts (13 positives/34 negatives/9,9,8 top-one hits/34 false alerts each). [Executable unit](selective_repair_decision.py) uses Python standard-library exact \`Fraction\`, [six unit tests](test_selective_repair_decision.py). [GitHub CI #42755166798 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/42755166798): checkout, pinned Python 3.12, all six tests, code compilation, runnable arithmetic. This CI does **not** run the original Go Git-history extraction, new Go patch actors, or independent maintenance tasks. No additional behavioral source evidence claimed.

## E. Return to the actual original 0.3 goal — not an extra proxy report

A next independent trial must jointly freeze:
- Paired equally currently functional Go architectures from a real source project and valid structural-atom transformation, against an internal helper baseline;
- Source/old-client contract and later independent real demand before implementation outcomes;
- At least two **actually executed** maintainer processes, equal executable source and observation budget but different explicit search policies; label any patch-location manifest separately as privileged **oracle**;
- Gating (should edit?) **and** ranking (where?) and end-to-end patch old/new client passes, actual search/tool/timing/changed symbols; record all failures and abort;
- Cost vector and declared distribution of design-context variables. Stratify task/repository, avoid clone pseudoreplication and source or reward leakage; distinguish permission from physical source editability;
- Equal-information conventional source dataflow, full-graph impact, established repair/training practices, and a classical learned selective gate. A "no alert" negative baseline and failure-to-complete are mandatory.

Potential first task source already registered in [CHI_D11 original maintained Go source task](../../../../tools/p35-b1/TASK_CHI_D11.md), a *researcher-authored* unsolved CSV-style quoted-header extension over original Chi v5.1.0. It can serve as an instrument, but NOT a real independently issued future demand. Archive reports indicate execution/evaluation of P35 B1 elsewhere; do **not** pretend it is a never-seen task. A genuinely new external issue or a time-split heldout task must be selected for confirmation.

**Scientific verdict:** the sign of policy *operating loss* reverses with false-alarm cost by elementary arithmetic; this is no discovery of architecture treatment effect. More importantly, the founding maintainer×architecture experiment supplies the **correct explanatory variable class** that our source-only tests omitted. No new real coding-agent trial, no novelty advance, LAW-R2 HOLD.
