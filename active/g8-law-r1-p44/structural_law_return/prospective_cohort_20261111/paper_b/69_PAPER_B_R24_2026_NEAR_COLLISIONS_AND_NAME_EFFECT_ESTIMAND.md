# Paper B R24 — Novelty Collision Audit: Existing AI Instructions and LLM Code Review
**2026-11-23 · public literature verified in this turn; record distinguishes published empirical claims from future study proposal.** This audit intentionally challenges the paper's strongest novelty claim.

## Serious neighboring results — not optional context

1. Pehlivan et al. 2025, *Are We SOLID Yet?*: five-principle LLM violation classification with 240 total examples, prompt variations, empirical model comparisons; it does NOT directly adjudicate actual edits under authenticated old-caller contracts. [ASE 2025](https://conf.researchr.org/details/ase-2025/ase-2025-nier-track/35/Are-We-SOLID-Yet-An-Empirical-Study-on-Prompting-LLMs-to-Detect-Design-Principle-Vio); [arXiv](https://arxiv.org/abs/2509.03093).
2. Gloaguen et al. 2026, *Evaluating AGENTS.md*: measured whether repository-level files affect coding-agent performance and exploration, and reports that agents tend to respect instructions. Not an SOLID-specific principle-name factor. [arXiv](https://arxiv.org/abs/2602.11988).
3. *Do Agent Rules Shape or Distort? Guardrails Beat Guidance in Coding Agents* (2026): examines 679 agent instruction files, 25,532 rules and 5,000+ agent trials, with positive versus negative rule-type findings. This **directly undermines** broad novelty claims such as "we are first to study whether design rules shape AI coding." [arXiv 2604.11088](https://arxiv.org/abs/2604.11088).
4. Xu and Wu (2026-10-22), *Stale Instruction Files Override the Code in Coding Agents: A One-Sentence Fix*: in author-reported controlled studies, agents followed stale instruction files despite code contradiction; tested source-priority wording as intervention. This is unusually close to authority-displacement story, even though the study manipulates stale repository conventions, not the semantic status of a named OCP/SOLID principle. [arXiv 2610.30571](https://arxiv.org/abs/2610.30571). Reported numbers in abstract are **their results**, not ours.
5. Mehtiyev et al. (2026-11-06), *When Instruction Files Go Stale*, reports 22 tasks, 732 trajectories comparing stale, corrected and absent instructions. This is very close on conflict, cost and evidence. [arXiv 2611.09802](https://arxiv.org/abs/2611.09802).
6. *Are LLMs Reliable Code Reviewers? Systematic Overcorrection in Requirement Conformance Judgement* (2026): analyzes LLMs marking correct code nonconforming and tests executable counterfactual validation. This is very close to any generic 'wrong patch refusal' contribution; B CANNOT claim discovery of review overcorrection or counterfactual verification as a new technique. [Springer 2026 DOI 10.1007/s10515-026-00638-5](https://doi.org/10.1007/s10515-026-00638-5).
7. Google Research CHI EA 2026, *From Correctness to Collaboration*, taxonomy of 91 sets of developer-defined coding-agent rules; includes high-level principles such as DRY and loose coupling. Already covers **named high-level design principles as developer instructions**, though the taxonomy is not itself a matched named-vs-neutral-contract-aware patch intervention. [Google Research](https://research.google/pubs/from-correctness-to-collaboration-a-human-centered-taxonomy-of-ai-agent-behavior-in-software-engineering/).
8. *Toward an Evidence-Based Template for Agent Instruction Files* (2026-11-02) reports many instruction formats and divergent guidance; its scope is adoption, consistency, maintenance and templates, not design-principle-specific patch decisions. [arXiv 2611.02383](https://arxiv.org/abs/2611.02383).

## Novelty becomes a narrow proposed interaction, not a grand discovery

Call the target **named-principle authority increment**. A conditional *experimental estimand*, not an existing effect:
- Hold the maintenance requirement, original source, old-client test oracle, authorized instruction hierarchy, tool budget, and semantic advice constant.
- Vary **only** the presence of a recognizable principle name/citation (e.g. 'Open–Closed Principle' versus the same content without branding), randomize independently of the admissibility of the patch.
- Add an **authenticated, authorized counterevidence phase**, identical across both named and neutral conditions, measuring revision, justified abstention and incorrect refusal.
- The strongest (still conditional) signal is a named-principle × admissible-counterevidence interaction on **actual disposition** after matching lexical choices and validating the source obligations. This is not evidence of dogmatic internal beliefs; it may also reflect anchoring, prestige, attention or instruction-priority misunderstanding.
- **Negative control:** equally plausible neutral design advice, or other authoritative named rules with identical instruction priority. Stronger control distinguishes recognition of specific design branding from general authority cues. Keep blind human/source-aware adjudication for actual acceptability.
- **Disconfirmations:** labels alter explanations but not code; names improve contract compliance; under matched authority no interaction; all differences explained by ordinary preference for named/authoritative instructions or source comprehension.
- **Contrast with P35 four-arm**: NONE/HARD_SOLID/SCOPED_SOLID/EVIDENCE_CONDITIONAL manipulates **instruction content**, not a pure name effect, so it is a separate foundational arm experiment. Do NOT claim these are interchangeable designs or that the new factorial is already preregistered.

The research-specific question is **not** whether rules influence LLMs, whether contracts matter, whether stale files mislead, or whether LLM code review sometimes overcorrects: those are documented topics. It is **whether named historical design-principle branding contributes additional, source-unjustified decision authority under otherwise equal authorized semantics and counterevidence**. A legitimate new label effect would still require replication across distinct principles, models, programming languages and tasks. 'First ever' is explicitly NOT established.

## Adversarial judgments
- Construct validity: name/no-name neutral paraphrase rarely preserves *exact* pragmatics, so many independent wording paraphrases and blinded human semantic-equivalence checks are necessary. Otherwise it measures phrasing, not conceptual authority. 
- Instruction hierarchy: if the named label is supplied as an authorized imperative, obeying it is not dogmatism. Make both conditions equally nonmandatory or explicitly scoped.
- Measured endpoint: actual patch disposition and retained client observations, not lexical rate or subjective persuasiveness alone.
- Framework critique: a simple named-wording effect would be reducible to well-studied framing/authority biases; Paper B can be useful as a **design-principle-specific evaluation agenda** even if no distinct cognitive mechanism exists.
- External validity: one OCP fixture is not all SOLID and an original author-constructed patch is not representative real-world maintenance.
- Scholarly defensibility: no result for a name effect exists in the project archive as verified. 
- Literature status: some articles read via public full-text or abstracts; not a systematic full corpus meta-review. Dates and numerical claims are cited to their papers, not treated as ours.

## Editor recommendation
Retain Martin's historical **style-versus-design** exceptions for texture, Parnas's **program families** for deep classical priority, and the narrow **named label vs neutral guidance** intervention as the paper's actionable research invitation. Cut any claim that naming this phenomenon itself establishes causal mechanism or first discovery.

**Gate:** novelty plausibility for v28 broad formulation was only 0.48. The narrower hypothesis is more **specific** but also faces stronger neighboring literature. Do not mechanically inflate a novelty score to 0.9 after rewriting.
