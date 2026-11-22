# Paper B R26 — A Minimal Falsifiable Experiment for the Named-Principle Effect

**2026-11-23 · prospective design only — NOT a preregistered or executed experiment.** This research question is sharpened after newly examining close 2026 prior art and the Martin/Parnas primary sources.

## What must remain unclaimed
- **Not novel as a general problem:** instruction-file precedence over code, agent rule effects, behavioral standards such as DRY/loose coupling and LLM reviewer overcorrection are already studied (Xu & Wu 2026; Gloaguen et al. 2026; Dong et al. 2026; guardrails 2026; ASE code-review overcorrection 2026).
- **Possible narrower novelty:** Does a *recognizable historical software-design principle name* itself induce an additional patch-disposition effect, even with equivalent authorized advice and source/contract evidence? This is a **candidate experimental contrast**, not a proved distinct mechanism or worldwide-first invention.
- **No source-supported inference:** SOLID authors intended universal axioms, models have internal dogmatic beliefs, name-effect exists, four-arm experiment was performed, tokens/energy were saved.

## Source-to-motivation correspondence
| Primary/adjacent source | Proven observation/argument | What Paper B must not take as new |
| --- | --- | --- |
| Parnas 1972/1979 | hide likely-changing design decisions; design program families for variable demands | contextual change, modularization or extension as an original AI-epoch concept |
| Meyer 1988 partial pp.22–25 | stable client description and technical-report variant | exact project library patch's fabricated erratum/book string as Meyer text |
| Martin 1996 pp.6,11–13 | strategic closure; exceptions to public member variable / RTTI heuristics | claim that his rule is uniformly unqualified or that he himself said SOLID are formal axioms |
| Dong et al. CHI EA 2026 | 91 developer rule sets including general software-engineering philosophy labels and agent behaviors | novelty of agent design-principle instruction content |
| Xu & Wu 2026 | experimentally observed conflicting stale instructions overriding existing code, corrected by instruction-priority sentence | novelty of instruction-vs-code conflicts or a general obedience mechanism |
| Gloaguen, 2026 rule studies | coding-agent exploration/performance varies with repository guidance | novelty of prompting agents with rules |
| Pehlivan et al. 2025 | classification of SOLID violations | patch acceptability cannot be read off classification benchmark alone |
| LLM code review overcorrection, 2026 | correct code can be called defective, executable counterfactual validation | novelty of wrong-refusal measurement |

## Proposed small factorial experiment (distinct from P35-B1)

**Source unit:** realistic frozen maintenance task, old callers, requirements/test oracle; the ground truth must be adjudicated by people blind to instruction labels. Include at least one valid nontraditional implementation and one case where a principle-conforming design is demonstrably preferred.

**Factor A — label:** identical authorized advice paragraph, either `OCP / Open–Closed Principle` named or identical behavioral instructions without the historical label. Preserve position, emphasis, length as closely as possible; generate **several separately reviewed matched paraphrases**. No imperative strength changes. A single one-word perturbation is insufficient proof of semantic identity.

**Factor B — admissible counterevidence:** authentic specification and client-contract facts shown either during initial evaluation or during a second phase, controlled for information budget; before-evidence decisions need an explicit **Defer** category, not an unjustified hidden-truth correctness grade.

**Outcomes:** authenticated `Accept / Reject / Defer`, final patch correctness on independent tests, actual source diffs, preserved legacy clients, coded rationales, explicit acknowledgement of rule/source conflict and correction after phase B. Separate wording-only changes from actual edits. Blind evaluate labels and contract oracle.

**Hypothesized pattern:** a named design principle selectively makes an otherwise acceptable patch more likely to be rejected, or reduces warranted revision after rebuttal. This pattern is informative **only** after ruling out instruction-priority and semantic-paraphrase differences. A name × evidence-stage effect does not establish a distinct cognitive psychology: framing/attention/authority cues remain competitors.

**Negative controls and rival arms:** unbranded advice, an equally prestigious non-SOLID guideline with matched relevance, *irrelevant* named principle under neutral task; ordinary source-aware requirements reviewer with equal facts. The additional neutral authority cue is necessary because a named principle could merely be more salient.

**Falsifiers:** no agent behavior change; only explanatory vocabulary changes; named label improves correctness/contract preservation; expert neutral semantics mismatch accounts for differences; existing instruction precedence fully explains differences; agent appropriately defers in missing contract cases.

**Do not merge protocols:** the earlier pre-sealed `NONE / HARD_SOLID / SCOPED_SOLID / EVIDENCE_CONDITIONAL` intervention tests content of advice under four explicit conditions; the new A-label comparison tests branding at held semantic advice. Run and analyze each independently. Neither has yet yielded an independent agent repair observation.

## Decision and next research threshold
The above is specific enough for a modest collaboration invitation, but not a completed experimental protocol. Before trial, freeze exact cases and positive/negative strata, treatment text, reviewer adjudication rules, independently protected tests, model/harness order and task assignments, outcomes and statistical analysis plan. A successful feasibility run would still only support that tested setting; other principle names/languages/tasks must replicate.

**Editorial status:** v29 gives the narrow proposal; no extra unsupported empirical result was added. Scholarly originality remains uncertain (internal subjective 0.51), even though experimental identifiability is more concrete (internal subjective 0.72).
