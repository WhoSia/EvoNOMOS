# LAW-R1-P6 — Generalized Conditional Design-Law Kernel Result

## Core result

P6 rejects the idea that the five SOLID items should occupy one logical layer.

The candidate kernel remains:

[
\mathcal L=(\mathcal X,\mathcal A,\mathbf Y,M,F,\Pi,U)
]

but the principle library now has heterogeneous roles.

### Generator principles
SRP, OCP, ISP and DIP primarily nominate candidate structural interventions.

### Constraint principles
LSP primarily constrains which candidate subtype/shared-base relations are admissible.

This yields a two-step architecture:

[
\text{principle vocabulary}
\rightarrow
\text{candidate actions / admissibility constraints}
\rightarrow
\text{empirical authority layer}
]

The authority layer, not the named principle, decides whether to TEST, REVERSE, ABSTAIN, REVOKE or remain UNRESOLVED.

## Four non-equivalent terminal states

1. **APPLY / TEST** — evidence warrants testing or retaining a structural intervention.
2. **ABSTAIN** — no structural intervention currently earns authority.
3. **REVOKE** — a previously declared structural extension/abstraction relation loses authority.
4. **UNRESOLVED** — evidence does not yet adjudicate the boundary.

P6 shows that collapsing these states loses scientific information.

## Cross-principle interpretation

- SRP supplies partition candidates, but further splitting can be locally unwarranted.
- OCP supplies extension candidates, but dead extension surfaces can be revoked.
- ISP supplies capability partitions, but full-corequirement worlds may remain unresolved.
- DIP supplies dependency-boundary candidates whose benefit can reverse across lifecycle phase.
- LSP supplies admissibility tests over subtype/base relations.

## Method role

LLM execution is demoted to a local instrument:
- classify or surface candidate distinctions,
- stress-test wording or representation,
- never stand in for repository history or lifecycle evidence.

The scientific object is the changing authority of structural actions in software worlds.

## Novelty status

P6 does not establish a new universal theory of software design.

The current surviving candidate is a **cross-principle empirical authority layer** that integrates existing ideas from architecture decision research, evidence-based architecture, modularity economics and self-adaptation while making named software-design principles explicitly revocable, role-dependent and evidence-governed.

Status: **candidate synthesis / operational kernel; novelty not yet established**.
