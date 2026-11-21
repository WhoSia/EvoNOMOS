# Paper B R10 — Instruction Authority Layers and a Discriminating Follow-Up Study (2026-11-22)

**Conceptual expansion, NOT a measured coding-agent result.** Current official sources reopened 2026-11-22:
- [OpenAI Codex AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md); [Codex customization guide](https://learn.chatgpt.com/docs/customization/overview) — repository/project instructions can be supplied via `AGENTS.md`.
- [Anthropic, Steering Claude Code (2026)](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more) — distinguishes `CLAUDE.md` project context, rules, skills, hooks and subagents.
- [Original October 9 Paper B hypothesis](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_SOLID_OBJECT_ORIENTATION_AND_AI_QUASI_AXIOMATIZATION_PAPER_B.md) states that such **instruction channels** do NOT demonstrate the model learned SOLID as axioms from pretraining.

## New research distinction: advice's location vs its claimed authority

Four separate locations may feed a principle into agent work:

1. **Model prior / unknown pretraining.** No accessible source-level access or verified intervention here; cannot identify specific SOLID training examples.
2. **Session or repository instructions.** `AGENTS.md`, `CLAUDE.md`, explicit local project configuration: documented, inspectable *instruction sources*. Their priority and interactions are product-dependent, so do not claim that one provider's file carries the same authority as another's.
3. **Task and source context.** Actual requirement, old caller, files, test failures, existing code comments. These describe *the problem* and may conflict with a general rule.
4. **Review and execution outcome.** Agent-produced code, explanation, tests and accept/reject recommendation. Even a matching output cannot alone reveal where the preference was learned.

**Hypothesis A: location effect.** Same wording may produce different behavior as a persistent project instruction vs an ordinary task-level advisory paragraph (we have NOT measured this). Under provider-specific instruction precedence, such a finding might reflect tool delivery rather than SOLID semantics. This is separate from the existing four-arm **wording intervention**, and should be a *later* study with tool controls, not covertly introduced into P35-B1's only-differing-paragraph design.

**Hypothesis B: norm conflict susceptibility.** Provide a legitimate old-API contract disconfirming a canonical refactor. Conditional advice should permit exception; HARD_SOLID might stubbornly reject or propose intrusive rewrites—but **no effect sign assumed**, and task-oracle dominance may collapse all groups to equivalent results.

**Hypothesis C: persuasion without code change (lexical rival).** Count principle references in agent output separately from code patch and tests. A strong vocabulary shift accompanied by no source behavior shift supports a lexical explanation, not operational quasi-axiomatization.

**Hypothesis D: valid strict doctrine.** Some actual change distributions justify hard separation; hard wording can improve implementation under those conditions. We must deliberately source such cases so the study isn't set up to show only harmful adherence.

## Experiment discipline and study outputs

First P35-B1 study: exactly four existing instruction arms, *one channel, one source*, same task and budget. No file-scoped AGENTS.md vs CLAUDE.md crossover until that first comparison is stable. Record actual injection content and path in **every fresh invocation**; runner behavior is not inferred from the name of a file. Keep source SHA and test oracle fixed before any assignment. Include failures and abstentions. Contract truth needs a separate source-bearing reviewer; do not use an agent's explanation or only a passing test as the independent contract oracle.

The [v23 receipt schema](agent_4arm_20261122/evidence_receipt_gate.py) deliberately records task source SHA, a SHA of the common task, tool budget, fresh invocation identity, code-patch digest, Go pass/fail and independent contract-review judgment **separately**. It does not contain a fabricated treatment effect or the results of the promised four-arm experiment.

This is an **idea-priority addendum**: define *where* authority can enter a system, *what* it causally changes, and *what observation* would disconfirm the asserted mechanism. Neither its four layers nor these hypotheses are claimed to be wholly unprecedented.
