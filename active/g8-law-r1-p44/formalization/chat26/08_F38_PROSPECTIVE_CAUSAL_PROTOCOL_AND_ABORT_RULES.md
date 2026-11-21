# Chat 26 — P44 F38 Prospective Two-Arm Repair Protocol (Design Only)

**Gate:** F37 paired source baseline is PASS on ten declared initial cases, original Go CI #44908134492; *no F38 source modification or independently concealed demand has been performed*. P44 RUNNING / LAW-R2 HOLD / G1–G7 OPEN.

## Unit and estimand

For task \`d\`, matched initial state \`s0\`, actor \`m\`, disclosure protocol \`I\`, and allowed edit policy \`Γ\`, consider potential outcome vectors \`Y(A,d,m,I,Γ)\` and \`Y(B,d,m,I,Γ)\`, A=handlerarm, B=callbackarm. A paired task contrast is interpretable only when the task, old-client contract, knowledge budget and edit rights are fixed. One actor solving A then B leaks learning; balanced order/counterbalanced actors or separate blinded maintainers must be used before claiming causal actor-general effects.

Outcomes must be recorded **separately**, not normalized to one arbitrary reward:
- hard constraints: old-client pass rate, new-demand satisfaction, unauthorized file edits, compile and race correctness;
- effort: changed source sites, file touches, diff size, compilation/test attempts, actual human time where available;
- verification/debt: extra adapter/setup work, new tests, reviewer questions, unresolved contracts;
- regression risk: prespecified negative controls, observed reverts and previously protected clients;
- runtime performance: only if comparable workloads and source instrumentation are predeclared.

## Sequential design

1. **Custody:** Fix F37 source SHA \`4cc2fb302888ecbe72f6a683d97eff18378b261a\` and exact dependency sums, toolchain, tests and full initial observables. Never silently compare unequal initial obligations.
2. **Sampling frame:** Freeze issue repositories, time window, inclusion and exclusion criteria before revealing arm-specific source cost. Record rejected cases and reasons. External issue != blinded task assignment.
3. **Contract:** Publish exact old and new request/response oracle, including potentially problematic headers, methods, optional paths and temporal traces. Unspecified cases remain UNKNOWN, not automatically promised.
4. **Rights:** Each actor has researcher-owned app-source edit rights only, unless separately verified. A shared-upstream defect is not fixed by claiming authorization over the upstream project.
5. **Forecast:** Each arm and classical source-aware comparator commits a pre-task prediction with version SHA: feasibility, expected affected edits, negative tests, bounded costs, abstention/uncertainty.
6. **Independent edits:** Separate source branches and maintainers/agents; same task, dependencies, time/cost budget, allowed tools, test and documentation access. Preserve failed partial diffs.
7. **Adjudication:** Build/test and inspect each edit; compare the predicted direction and measured outcome with formal lower/upper/exact/HOLD grades. Audit whether historical familiarity or different existing defects caused outcomes.
8. **Release:** Law candidate requires multiple prospectively selected independent tasks and support for generalization under documented conditions, not a source parity test or a single selected counterexample.

## Stop/abort logic

- BASELINE_UNMATCHED: any protected old-client mismatch at F37 under declared oracle.
- RIGHT_UNVERIFIED: attempted upstream-authorized edit without a valid grant.
- TASK_NONBLIND: selected after seeing edited arm costs, cannot score as independent forecast.
- SOURCE_COURT_FAIL: output mismatch/negative control or CI failure, log and preserve.
- COST_NOT_IDENTIFIED: only synthetic edit units, no factual claim about human labor.
- RIVAL_NOT_MATCHED: conventional baseline lacks the same input, rights or budget.
- INCONSISTENT_CONTRACT: available evidence yields no legitimate candidate requirement world.
- REGRESSION_UNKNOWN: untested protected clients block a broad safety claim.
- OBSERVATION_SCOPE_SWITCH: post-hoc narrowing of contract to turn failure into PASS.
- NOVELTY_TIE: conventional state-machine/alias/rely-guarantee model predicts result as well as EAC.

Hard failures forbid scientific promotion. Failure is informative; retain the reason code and raw evidence, never omit it from the denominator.
