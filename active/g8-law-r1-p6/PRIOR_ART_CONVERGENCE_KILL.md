# LAW-R1-P6 — Prior-Art Convergence / Novelty Kill

## Stronger collisions discovered in P6

### Ros & Sangwan (WICSA 2011): evidence-based architecture discovery

This is a direct collision with any weak EvoNOMOS claim that "SOLID decisions should be revised when future evidence contradicts them."

Their method:
- organizes architectural decisions in a semi-formal reasoning framework;
- explicitly uses SOLID as the taxonomy;
- treats decisions already made as context for future decisions;
- treats future decisions as evidence about the robustness of earlier decisions;
- challenges and adjusts earlier decisions when conformance is no longer possible.

**Killed claim:** EvoNOMOS is novel merely because SOLID is evidence-tested and revisable over time.

### Zimmermann et al. (JSS 2009): architectural decision models

This work formalizes:
- decision issues,
- candidate alternatives,
- outcomes,
- logical incompatibility,
- forces/triggers/dependencies,
- reusable production rules,
- pruning of alternatives and not-applicable outcome states.

**Killed claim:** EvoNOMOS is novel merely because it models competing alternatives, applicability, incompatibility or rule-based decision guidance.

### Self-learning self-adaptive systems / MAPE-K

Self-learning adaptation frameworks already:
- observe current context/state,
- choose adaptation actions,
- evaluate effects,
- learn or revise adaptation rules,
- verify adaptation logic in the current context.

Policy-learning approaches additionally update a state→action policy from trajectories and rewards.

**Killed claim:** EvoNOMOS is novel because it has a context→action→effect→policy-update feedback loop.

### ATAM / CBAM / architecture-decision research

Prior work already owns:
- multi-quality tradeoffs,
- cost/benefit/risk analysis,
- alternative comparison,
- decision rationale,
- architecture decision knowledge reuse,
- empirical study of architecture decision making.

**Killed claim:** EvoNOMOS is novel because it uses nonfunctional outcomes, alternatives, economics, or empirical architecture decisions.

## Surviving research object after P6 kill

The remaining candidate is narrower:

> A cross-principle empirical authority layer for software-design maxims, grounded in real maintenance interventions, where named principles generate candidate structural actions but gain, lose, reverse, or abstain from authority only through observed context-conditioned lifecycle evidence.

Its strongest current distinguishing commitments are the conjunction:

1. named design principles are demoted to action generators / admissibility constraints;
2. structural rivals are tied to explicit pre-treatment moderators;
3. authority is based on observed lifecycle vectors rather than principle conformance;
4. sign/Pareto reversal is first-class rather than treated as noise;
5. ABSTAIN means no structural intervention is currently authorized;
6. REVOKE allows a previously declared extension/abstraction relation to lose authority;
7. rules are updated from real maintenance-world contact across independent repositories;
8. different SOLID items may occupy different logical roles (generator vs admissibility constraint).

This conjunction remains a **candidate novelty**, not a novelty verdict.

## P6 falsifier

If prior work is found that already jointly operationalizes all eight commitments above for software-design principles over real maintenance histories, EvoNOMOS must absorb that framework rather than claim a new kernel.
