# LAW-R1-P5 — Prior-Art Novelty Kill

## Question

Is there already a framework more general than SOLID that makes EvoNOMOS LAW-R1 unnecessary?

## Strong collisions

### ATAM / CBAM

ATAM already treats architecture as a set of candidate approaches evaluated against multiple competing quality attributes and exposes sensitivity/tradeoff points. CBAM adds economic comparison among architecture alternatives under finite resources.

**Killed claim:** "EvoNOMOS is novel because it considers multiple quality outcomes or architecture tradeoffs."

References:
- Kazman et al., *The Architecture Tradeoff Analysis Method*, CMU/SEI-98-TR-008.
- Asundi, Kazman & Klein, *Using Economic Considerations to Choose Among Architecture Design Alternatives*, CMU/SEI-2001-TR-035.

### Parnas information hiding

Information hiding already says decomposition should be organized around difficult or likely-to-change design decisions rather than around a universal syntactic decomposition rule.

**Killed claim:** "EvoNOMOS is novel because abstraction/modularity should depend on volatility."

Reference:
- Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules*, CACM 1972.

### Baldwin–Clark / Sullivan real-options modularity

Design Rules / real-options work formalizes how modularity creates option value under uncertainty, future experimentation and change opportunities. Sullivan et al. explicitly transported this theory to software design and DSMs.

**Killed claim:** "EvoNOMOS is novel because modularity value depends on uncertainty or future change."

References:
- Baldwin & Clark, *Modularity-in-Design: An Analysis Based on the Theory of Real Options*.
- Sullivan et al., *The Structure and Value of Modularity in Software Design*, ESEC/FSE 2001.

### Architectural tactics / Attribute-Driven Design / fitness functions

Architectural tactics and ADD already connect quality-attribute drivers to structural tactics; evolutionary architecture fitness functions make desired architectural properties executable and continuously checked.

**Killed claim:** "EvoNOMOS is novel because design advice should be tied to quality goals and executable evidence."

### Technical-debt economics

Architecture technical-debt literature already treats design choices as temporally contingent and sometimes locally rational despite later cost. Recent real-options work explicitly makes deliberate technical debt optimal in some uncertainty regimes.

**Killed claim:** "EvoNOMOS is novel because a usually discouraged design can be locally rational."

## Older empirical warning against universal principles

Empirical software-design work predates SOLID and already found that proposed coupling rules can have context-sensitive or inconsistent effects on modifiability. Therefore "principles are not universally beneficial" is not a novelty claim.

Reference:
- Selby & Basili, *Experimental evaluation of software design principles: An investigation into the effect of module coupling on system modifiability*, JSS 1984.

## 2025–2026 LLM collision

Recent work evaluates whether LLMs can:
- apply requested architecture patterns,
- assist Attribute-Driven Design,
- generate architecture design rationale,
- perform SOLID/pattern-oriented refactoring,
- support real software-design work.

These studies mostly evaluate application quality once a pattern/method/task is specified. They do not establish that a named maxim should have been selected in the first place under changing moderator evidence.

Examples:
- Hadjichristofi et al., *An Empirical Evaluation of Large Language Models Applying Software Architectural Patterns* (2026).
- *Better Together: An LLM-assisted approach to designing software architectures using Attribute-Driven Design* (IEEE TSE, 2026).
- *Using LLMs in Generating Design Rationale for Software Architecture Decisions* (ACM TOSEM, 2026).
- Wang et al., *Using LLMs in Software Design: An Empirical Study of GitHub and A Practitioner Survey* (2026).
- *AI-assisted code refactoring: Where can it be helpful and where do humans outperform it?* (JSS, 2026).

## Surviving candidate

The surviving EvoNOMOS object is **not a new list of principles**.

It is a revocable empirical decision layer:

```
observed context/moderators
        ↓
admissible rival structural interventions
        ↓
non-collapsed outcome vector
        ↓
mechanism / birth tax / downstream effect
        ↓
support, reversal, failure boundary, or ABSTAIN
        ↓
updated law authority
```

A named principle such as SRP, OCP, ISP or DIP becomes only a **candidate action-family generator** inside this layer.

The additional P5 question is whether LLM advice exhibits a **maxim prior**: when a familiar principle name is supplied, does the model select its congruent action more often even on cells where moderator evidence calls for a rival or ABSTAIN? And does an evidence-conditioned rival representation recover the reversal?

## Novelty ceiling after kill

At P5 opening, novelty may be claimed only for the **combination** of:

1. named principles demoted to rival-action generators rather than authorities;
2. explicit moderator-conditioned apply / reverse / abstain surfaces;
3. non-collapsed lifecycle outcome vectors and installation taxes;
4. empirical updating/revocation of rule authority from real maintenance worlds;
5. direct measurement of named-principle priors versus evidence-conditioned rival choice in LLM design advice.

Any weaker novelty statement is considered killed or substantially anticipated by prior art.
