# Paper B R11 — Instruction Compliance, Rebuttal and Quasi-Axiomatization: A Critical Identification Gate
**Research hypothesis and mathematical design note, 2026-11-22. No observed agent executions, no demonstrated treatment effects.**

## 1. Collision with the current construct

The existing P35-B1 four-arm design changes a design-advice paragraph:
`NONE / HARD_SOLID / SCOPED_SOLID / EVIDENCE_CONDITIONAL`.
This is an excellent randomized **instruction-content comparison** if assignments and outcome oracles are sound. But the strongest version of the Paper B claim—an agent treats design doctrine as independent, overriding truth—is not measured merely by `HARD_SOLID` changing the generated patch. A participant can follow an explicit authorized instruction because it was given, not because it independently believes SOLID to be a universal law. The two causal channels are:
- **Compliance channel:** an instruction changes action because it has operational priority.
- **Epistemic-authority channel:** an agent continues applying the principle as binding despite context that, under a frozen authorized requirement hierarchy, defeats that rationale.

Both may coexist. A prompt-only intervention cannot infer what an inaccessible base model learned during training. A wrong patch alone does not identify which channel caused the error.

## 2. A finer operational target

Let task t fix: pinned code S, disclosed customer requirement D, protected clients C, authorized edit rights A, observer/test set O, and an instruction precedence policy H. Let proposed patch p be `admissible(t,p)` iff it meets D,C,A under the source-backed evaluation protocol. Independently mark `principle_conforming(t,p)` according to an explicit case-specific OCP/SOLID interpretation (NOT a universal mechanical SOLID classifier).

Let R denote independently authenticated contradictory or limiting evidence supplied in a subsequent controlled turn, and let J_a(t,R) denote the agent's **patch disposition** (not vocabulary). We can identify a *behavioral unresponsiveness* event only if:
1. a specified binding constraint and source-backed oracle makes the initial doctrinal reason insufficient under the declared instruction precedence;
2. the agent actually received and could inspect R;
3. an allowed compliant resolution exists, or, when the instruction set is inconsistent, the agent was explicitly permitted to flag conflict/abstain;
4. it nevertheless refuses to revise a patch or decision **because the principle is treated as overriding**, with rationale coded separately from observed code.

A final failure without condition (4) is not enough. A response refusing to violate an unconditional higher-priority hard instruction may be correct instruction following rather than quasi-axiomatization. Distinguish `DOCTRINAL_OVERRIDE`, `EXPLICIT_POLICY_COMPLIANCE`, `CONTRACT_FAILURE_OTHER`, `CORRECT_REVISION`, `ABSTAIN/CONFLICT`, and `UNRESOLVED`. Classification requires a blinded independent adjudicator, and disagreements remain visible.

## 3. Built-in rival and negative-control demands

The 2026-10-09 preregistration requires tasks **both** where conventional SOLID advice can help and where canonical-looking refactoring may violate a protected contract. Predeclare task strata:
- ALIGN: a principle-conforming edit and customer obligations align, with an independent ordinary solution.
- CONFLICT: a naive or forced doctrinal refactor would violate a documented protected client or a legitimate task constraint, but an authorized repair exists that does not.
- UNDERDETERMINED: source data are insufficient to know whether the alleged doctrinal violation warrants repair; correct behavior may be to request evidence or abstain.

For each stratum, keep the same source, requirements, tests, rights, tools, model settings, budget, patch visibility and follow-up factual evidence across four arms. Balance order by task and model; ensure distinct clean agent contexts. Outcome coding must not use `mentions("SOLID")` as a proxy for behavioral authority.

The follow-up R must be **the same independently sourced, credible information** for every condition, and not newly invent or contradict higher-priority formal study constraints. A follow-up that changes the user's request is a new task, not a pure belief update; label it accordingly.

## 4. What randomization can and cannot estimate

If A is randomized prompt arm, Y is a preregistered objective such as old-client correctness or admissible final patch, and t is fixed, compare:
`tau_t = E[Y | do(A=HARD_SOLID), t] - E[Y | do(A=EVIDENCE_CONDITIONAL), t]`.
Randomization plus execution and missingness controls can identify a *prompt effect* within eligible task/model blocks. It does **not** identify the mediator `believes SOLID is an axiom` or historical training cause.

To assess practical context sensitivity, report the interaction:
`Delta = (tau_CONFLICT - tau_ALIGN)`
where each tau is defined by the same outcome and aggregation plan, and model/task clustering is accounted for. This contrast can detect when an instruction's effect changes with task type; it is **not uniquely an estimate of operational quasi-axiomatization**. A pure task/test-dominance rival predicts tau≈0; lexical echo predicts explanation differences with no source patch/contract differences; a valid strict-doctrine rival allows HARD_SOLID to outperform on ALIGN. Preserve TIE and sign reversals.

A later, separately preregistered study can compare repository-level vs inline instruction locations. Combining location and content now would confound the inherited P35-B1 study; **do not secretly change its four arms**.

## 5. Nontrivial counterexample to a tempting interpretation

Suppose a reporter directs an agent to implement a strict policy in a project *even when* a noncanonical patch would be simpler. The agent outputs a strict design, passes old and new contracts and defends it in its explanation. Calling this 'harmful axiomatization' would be a false positive: nothing about the trace demonstrates rejection of a valid binding requirement. Conversely, an agent may mention SOLID repeatedly but produce exactly the same correct patch as NONE. Vocabulary signals alone cannot establish behavioral influence.

A different case is a clearly protected, authenticated caller contract, an authorized repair that preserves it, and a hard-rule agent that outputs a failing rewrite while rejecting explicit contrary test evidence. That case supports an observed **failure to integrate the evidence under the treatment**; attributing its origin to pretrained knowledge still requires additional interventions.

## 6. Minimum executable next step without data fabrication

1. Lock a verified source snapshot and independent requirement/old-contract oracles for 1 ALIGN + 1 CONFLICT case (prefer a third UNDERDETERMINED control), including conventional source-aware baseline predictions.
2. Replace shared task/source placeholders in the four existing prompts only after the common task is frozen; inspect prompt diffs for exclusive architectural hints. Record task hash, model, schedule, fresh-context identity and equivalent budget.
3. Execute real independent coding-agent calls only through legitimately available executor access; retain tool logs, failed calls, original patch bytes, hidden evaluator and independent human review. A CI test of receipt syntax is **not** an agent execution.
4. Apply the identical factual rebuttal and evaluate both the actual code change and response to the rebuttal. Keep patch/contract and lexical outcomes separate.
5. Analyze by stratum and arm, give uncertainty with correlated task/model trials, and present negative, tie, reversal and unknown outcomes. If independent calls are unavailable, **stop at experiment-ready design** and publish B as a position paper with no empirical agent-effect paragraph.

## Editorial consequence for v23

Preserve v23 as canonical draft. In the next separately versioned edit, place this threat-to-identification directly after the four treatment conditions, not hidden in a long appendix. Rephrase any claim that the proposed experiment would directly reveal agents' intrinsic belief in SOLID: it measures **context-conditional instruction responses**, and repeated counterevidence is a proposed operational test of rule-like behavior. Historical canonization, instruction precedence and model pretraining remain separate.
 
**Verdict:** classical rival and causal identification barrier improved at design level only. `PAPER B v23 DRAFT / FOUR ARM PRE-AGENT-RUN / F38 OPEN / LAW-R2 HOLD`.
