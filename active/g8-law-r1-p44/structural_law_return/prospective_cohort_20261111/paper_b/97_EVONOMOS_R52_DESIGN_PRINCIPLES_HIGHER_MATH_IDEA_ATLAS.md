# EvoNOMOS R52 — Mathematical Bridges Above Design Principles: Idea Atlas

**2026-11-23 KST · idea-first, source-sensitive research note; hypotheses, NOT proven universal laws.**

## Why this note exists

The original [2026-07-29 EvoNOMOS archive](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view) contains the user's exact fundamental concern: **원칙 ≠ 규칙 ≠ 공리**. No one formally designated SOLID a universal mathematical axiom; repeated education/peer review/AI coding practices can *appear* to confer quasi-axiomatic authority. The same original research sought conditional principles, epistemic autonomy and discovery of better principles.

In the user's [2026-10-09 archive](https://drive.google.com/file/d/1TuweqOEc1KY14ddEJVoPbBJAiT-i3thP/view), the user explicitly rejected the assistant's insistence on globally unprecedented theorems: reinterpretation of already known mathematics *through SOLID's quasi-axiomatization* and an honest bibliography can itself be a worthwhile cross-field position thesis. This is a **conceptual inquiry first**. Actual source-level efficacy testing may follow but is not a prerequisite for writing the position paper.

**Two hypotheses should not be merged**:
- *Epistemic/social hypothesis:* a defeasible, domain-specific design guideline may function as an unquestioned convention or command. The historical prevalence and AI behavior effect are NOT yet established.
- *Structural/metamathematical hypothesis:* heterogeneous rules including SOLID, DRY, KISS, YAGNI, information hiding or selected patterns might each be **partial readings/projections of deeper mathematical structures**, perhaps more than one. The existence of a single unifying law is entirely open.

### Seven cross-disciplinary idea tracks

| Rank | Bridge | New question proposed for EvoNOMOS | What existing mathematics ALREADY supplies | Strict limit |
| --- | --- | --- | --- | --- |
| A | **Coordination games and institutional equilibria** | Can adherence to a principle spread because shared vocabulary is an effective equilibrium, even where another conditional design is technically preferable? | Monderer & Shapley 1996, potential games; strategic incentives; coordination games. | An equilibrium is not evidence that SOLID is actually suboptimal, historically coercive, or that a codebase game is a potential game. |
| A | **Defeasible reasoning and belief revision** | Can a design principle be an *overridable argument* rather than a theorem, and can evidence of context trigger legitimate withdrawal? | Dung 1995 attack/defense argument semantics; AGM 1985 and Darwiche–Pearl 1997 iterative belief revision. | These are existing logics, not mathematical systems invented here; a team-approved norm can still be binding. |
| A | **Formal concept lattices/Galois connections** | Can relationships between *contexts in which design interventions are warranted* and *principles they support* generate a nontrivial lattice of scopes, rather than five universal yes/no commandments? | Wille, Ganter & Wille 1999 formal concept analysis: concept lattices from context–attribute incidence. | Defining a lattice requires a justified incidence/evidence relation; unknown and context-dependent outcomes cannot honestly be silently made binary. |
| B | **Category-theoretic compositionality** | Are interface boundaries and change/behavior preservation instances of compositional structures, with OOP mnemonics only local views? | Fong & Spivak 2018/2019, compositional wiring diagrams; Ghani et al. 2018 open games; Goguen & Burstall specification institutions. | Category theory already models many software constructions. There may be incompatible semantic axes and no universal functor over SOLID. |
| B | **Abstract interpretation and information loss** | Does a static rule such as “violates OCP” operate as an abstraction that forgets protected contracts and expected changes, and is an automatic patch rejection an unsound *normative* lift from that coarse abstraction? | Cousot & Cousot 1977 abstract interpretation uses ordered abstract domains and sound approximation for specified properties. | Soundness of a formal abstraction for one property is NOT the legitimacy of a design command; one must specify what is being approximated. |
| B | **Mechanism design + principal/agent roles** | When a maintainer, reviewer and coding agent optimize different objectives, could a principle work as a governance convention rather than a universally optimal code invariant? | Mechanism design, principal–agent problems, team incentives. | Empirical institution/authority data needed. Normative policy and technical correctness are not interchangeable. |
| C | **Local-to-global compatibility (sheaves/constraint gluing)** | Can local good design decisions be mutually incompatible globally, even though each locally satisfies a rule? | Existing sheaf and distributed consistency formalisms describe local-to-global gluing problems. | Highly speculative bridge; a mathematical sheaf must be actually constructed, not adopted as decoration. |

**Scores in this note are *ordinal research priority A/B/C*, not scientific novelty probabilities.** We intentionally avoid pseudo-calibrated claims such as “0.95 unique” before a systematic search.

## Concrete game-theoretic thought experiment (invented, not a user observation)

Suppose two maintainers choose a shared conventional architectural rule **S** or a situation-specific alternative **F**.

| Maintainer 1 / maintainer 2 | S | F |
| --- | --- | --- |
| **S** | (3,3) | (0,0) |
| **F** | (0,0) | (4,4) |

Both (S,S) and (F,F) are Nash equilibria. The (F,F) equilibrium yields higher payoff **under this invented scenario**, yet (S,S) can persist because a single person deviating from the shared convention loses coordination benefit. Thus *a rule can be stable without being a universal technical optimum*. Other cost structures can favor S; the example does not establish SOLID's actual payoff or prevalence. This is a research **metaphor with exact mathematics**, not an empirical claim.

A useful higher-level question is **how a principle gains social authority**, not merely whether the principle improves raw maintenance speed. The theory belongs at the interface of design practice, multi-agent coordination and conceptual history.

## Concrete formal-concept sketch (interpretation, no new theorem)

Let C be a finite set of software contexts and P a set of candidate design heuristics. Define E ⊆ C × P only when **independent, contract-respecting evidence** warrants using principle p in context c. For X ⊆ C define X↑ = {p ∈ P : all c ∈ X support p}; for Y ⊆ P define Y↓ = {c ∈ C : all p ∈ Y are supported in c}. In classical formal concept analysis, these operators yield a Galois connection and a concept lattice, a rigorous way to discuss **families of contexts and principles**.

Potential EvoNOMOS interpretation: “SOLID”, “DRY” and “YAGNI” might occur in different regions of a context–principle lattice, so apparent conflicts can mark a boundary between contexts, not a contradiction in one universal deductive system. This is *not* a discovery of a novel lattice, and a ternary evidence relation (supported/refuted/unknown) needs additional theory. The first interesting result would be a nontrivial, source-grounded map of scoped design judgments.

## Original practical core: three levels of authority

1. **Formal semantic obligation:** public contracts and invariant preservation (some forms of LSP); enforced because the project must remain correct under an agreed specification.
2. **Authorized local policy:** a team has deliberately chosen a coding standard; obedience is warranted by governance within its scope, not by a timeless theorem.
3. **Defeasible design heuristic:** OCP, DRY, KISS, etc. as contextual advice with alternatives and counterexamples. A structural pattern/word alone is not a grant of universal rejection authority.

The very same principle *name* can participate in different levels. The program's goal is to expose that transition and make it discussable, not to say strict rules are inherently wrong.

## Three particularly promising novelty *interpretations*

- **Why does a rule become unquestioned?** The coordination game supplies a possible sociology of apparent axioms; software history is still unobserved.
- **What lies above named rules?** The lattice/abstraction/composition family could represent context and structure from which named principles emerge as fragments, without presupposing one magical scalar.
- **Can we tell when a name is unjustified?** Argumentation and belief revision allow defeaters/withdrawals; not a brand-new logical system, but a conceptually sharp remedy to the epistemological issue.

This is a **position agenda**. No reason to postpone a short conceptual paper until every interpretation has been experimentally verified. The hypothesis and precedent attribution must be honest.

## Anchoring prior literature (verified public references / original Drive holdings)

- [Monderer & Shapley (1996), Potential Games](https://doi.org/10.1006/game.1996.0044) — published theory; public abstract verified.
- [Dung (1995), argumentation/nonmonotonic reasoning/n-person games, owned original PDF](https://drive.google.com/file/d/1QFpaDCwOINWeak1cXSXyvcN6Vrin3lkR/view) — original PDF text freshly reopened and read.
- [Darwiche & Pearl (1997), iterated belief revision, owned original PDF](https://drive.google.com/file/d/1fMpdbYg_ewS5Cwyh_jWRDx1AfDo0R6Fi/view) — original PDF text freshly reopened and read.
- [Ganter & Wille (1999), Formal Concept Analysis: Mathematical Foundations](https://link.springer.com/book/10.1007/978-3-642-59830-2); [TU Dresden introduction to FCA](https://iccl.inf.tu-dresden.de/w/images/4/49/IntroFCA-RW2019.pdf) — formal-concept literature metadata and definition verified online; **not** directly acquired as a connected Drive PDF.
- [Fong & Spivak (2018/2019), Seven Sketches in Compositionality](https://arxiv.org/abs/1803.05316), [MIT OCW course](https://ocw.mit.edu/courses/18-s097-applied-category-theory-january-iap-2019/pages/lecture-videos-and-readings/) — public description verified; not read full PDF here.
- [Ghani et al. (2018), Compositional Game Theory](https://arxiv.org/abs/1603.04641) — published/open-game formalism; abstract verified, full text not read here.
- [Goguen & Burstall (1992), Institutions: Abstract Model Theory for Specification and Programming](https://www.lfcs.inf.ed.ac.uk/reports/90/ECS-LFCS-90-106/) — formal logic "institution", NOT a claim about sociological institutions.
- [Cousot & Cousot (1977), Abstract Interpretation, owned original PDF](https://drive.google.com/file/d/1hZfipMMYFSwpOVx4ZuhAIvkzt4jDptIl/view) — original PDF text freshly reopened and read.
- [AGM belief-revision overview](https://plato.stanford.edu/entries/logic-belief-revision/), [Stanford Encyclopedia: defeasible reasoning](https://plato.stanford.edu/entries/reasoning-defeasible/) — secondary conceptual references.
- [Baldwin & Clark (2000), Design Rules, owned PDF](https://drive.google.com/file/d/1yQWVWQSVQRoRNaeH_SHDITdV1oDWr46K/view) and [Sullivan et al. (2001), environment-sensitive modularity, owned PDF](https://drive.google.com/file/d/1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr/view) — the latter already read and audited in R47; not claimed as new.
- [Previous EvoNOMOS R36 speculative higher-order structure](81_EVONOMOS_R36_HIGHER_ORDER_STRUCTURE_INDEPENDENT_CONJECTURES.md) — not erased; this note broadens *mathematical interpretation* beyond utility/forecast metrics.

**Research disposition:** CROSS-FIELD IDEA MAP STAKED AS A VERSIONED ARTIFACT; EXISTING MATHEMATICS CITED; MAIN THESIS SEPARATED FROM UNPROVEN REFINEMENTS; NO NEW UNIVERSAL DESIGN THEOREM OR REAL AGENT EFFECT CLAIMED.