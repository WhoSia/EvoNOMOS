# EvoNOMOS R55 — Fitness Functions as Hidden Axioms: Mathematical Idea Seeds from New Sources

**2026-11-23 · an idea proposal grounded in freshly opened Baldwin (2023), LaMantia et al. (2007), Räihä (2010), Fu et al. (2012), Song et al. (2016), Parnas (1979).** None of the novel analogies below are attributed to those authors as their established results. This note broadens the [R52 cross-field atlas](97_EVONOMOS_R52_DESIGN_PRINCIPLES_HIGHER_MATH_IDEA_ATLAS.md) and complements the short [v36](PAPER_B_BILINGUAL_POSITION_36_20261123.md).

## The newly sharpened idea: the metric can become an invisible axiom

Räihä (2010) surveys search-based software design and emphasizes the choice of **representation and fitness function** as a crucial design decision. [Full original](https://drive.google.com/file/d/1BdFL0tU7Nna7jqQM0oPK6Ds1wdtyZS8S/view). An optimizer can be mathematically correct at maximizing a designer-defined score and still implement a poor architectural policy if that score inadequately represents the system's true obligations. This is elementary optimization logic; not a new result.

**EvoNOMOS interpretation:** the same quasi-axiomatization concern applies not only to *SOLID as named doctrine*, but to *cohesion, coupling, propagation cost, decoupling level, code-review scores, complexity thresholds and AI-agent reward models*. A scoring formula or algorithm may quietly move from “a chosen abstraction” to “the design law” when its unexpressed purpose and scope are forgotten. A **fitness function is a policy of attention**, not an objective truth of design.

The conceptual project should distinguish **what a representation can describe**, **which values an objective function rewards**, and **who legitimately authorizes a binding verdict**. Treating those three as equivalent is the same philosophical category confusion exposed by an over-authoritative principle name, at a higher level.

## A possible formal signature: conditional relations, not universal scalar equations

For a context c, a set of architectures A(c), protected contracts K(c) and candidate design advice p, posit:
- A feasibility predicate F(a,c) ∈ {valid,invalid,unknown} subject to evidence and verified contracts.
- A family of partially ordered quality criteria Q_c on **feasible** architectures, where cost, understandability, change propagation, risk and coordination may conflict.
- A principle's *defeasible recommendation relation* R_p(c) ⊆ A(c)×A(c), sometimes undefined if no evidence or the principle has no scope.
- An authorized project policy G_c that may legitimately require one approach even if other technical criteria remain disputed.

**Higher-order atlas candidate:** instead of asking whether “OCP is always true,” ask for the domain of c over which R_OCP(c) has defensible support, how R_OCP and R_YAGNI overlap, and whether different recommendations can be generated from a common context-dependent composition of structure/constraints/governance.

This signature is a **researcher's proposal**, not a formal discovered mathematical object. Even if built, it might instantiate preexisting multi-criteria decision theory, formal concept analysis or classical design spaces. One could view it as a typed formalism that prevents mixing **technical statement**, **normative authorization**, and **empirical outcome**.

## Game-theory extension: the rule and its score can coevolve

A simple coordination game can give two developers reasons to adopt the same standard, even if the conventional standard is not the global technical optimum for the project. Add a reviewer or code-bot that automatically enforces the convention: the optimization score acquires **institutional enforcement**. This suggests a three-stage *hypothesis*:

1. A technical heuristic is introduced as an economical description of design tradeoffs.
2. Developers coordinate through its vocabulary, and tools expose compliance scores as salient signals.
3. The score becomes a de facto veto unless its scope, protected behavior and governance are revisited.

The sequence is *not established history*. Alternative mechanisms include formally authorized team rules, genuine technical superiority in the tested domain, teaching simplifications and plain review mistakes. Test history separately if empirical claims are needed.

## Relation to new source lineage

- **Parnas (1979)**, [owned readable canonical PDF](https://drive.google.com/file/d/1XGzB9hq_6wk6aXeVojMo1IeKoKCg704j/view) emphasizes “uses” dependencies and minimum extensions/subsets to support expansion/contraction. Good *structural basis*, not a declaration of all SOLID axioms.
- **LaMantia, Cai, MacCormack & Rusnak (2007)**, [original working paper](https://drive.google.com/file/d/11YpfmJ4EJ1blHIVQRy1yWFJqkS2BJgn9/view) explicitly notes informal information-hiding criteria and attempts to model design rules/replaceable modules with DSM and options theory. Crucial: **Baldwin/Clark architectural “design rules” are stable specification/interface constraints, which differ from the social imperative to follow SOLID**.
- **Baldwin (2023)**, [original retrospective](https://drive.google.com/file/d/14QDJGv1bN_42BY-d15gnX2svKDXkE04Q/view) openly discusses limits of her own prior modularity options theory and the inability to give credible probabilities for incomparable new technologies. This is an elegant case of a design theory's own epistemic revision.
- **Fu, Li & Chen (2012)**, [original paper](https://drive.google.com/file/d/16Snv86b2rVuaeGaakbswwJHD9lkGZxrK/view) already supplies probabilistic change propagation and DSM-based architecture comparisons. Any future mathematical framework must credit its existing domain and claims.
- **Song et al. (2016)**, [original accepted manuscript](https://drive.google.com/file/d/1sekVIZ1TI_SgcCt28lLDi8BfezwHBV2f/view) learns how to choose project **process models** from context but admits that successful historical projects can use bad models. This is an adjacent warning: learning observed conventions is not necessarily identifying optimum architecture.
- **Cai et al. (2025)**, [original 1,252-project paper](https://drive.google.com/file/d/1cYBfoR0LQEwK2x5cMMLTaLZizEtQeoga/view) relates architectural complexity to maintenance burdens, not proof that a scalar metric is a universal design norm.
- **Mishra et al. (2026)**, [original two-platform leakage paper](https://drive.google.com/file/d/1vX1nxs44EVg6nTPC85CNaMoNU7fO9A0A/view) shows data leakage can inflate an accurate-seeming model in another software task. Experimental caution belongs in follow-on papers, not the headline of the short theoretical idea.

## Four research candidates generated now (priority = idea interest, not uniqueness certificate)

| Code | Candidate interpretive question | Most helpful existing field | Status |
| --- | --- | --- | --- |
| **F-AX** | What makes a chosen **fitness function** look like an unquestionable design axiom after automation? | Optimization, Goodhart/Campbell measurement effects, governance | Concept seed; actual trend unmeasured |
| **P-ATLAS** | Can named design principles be context-dependent partial relations with meaningful overlaps, rather than universal total orders? | Formal concept analysis, order theory, categorical composition | Formalism sketch; partial mapping unbuilt |
| **D-RULE** | How do *binding architectural interface constraints* differ from *general design heuristics* and *mathematical postulates*, despite all being called “rules”? | Programming-language semantics, design rule theory, epistemology | Historically source-grounded distinction; new interpretation |
| **G-NORM** | Can shared review norms become stable equilibria and be enforced by agents even when other conventions would be technically adequate? | Game theory, mechanism design, coordination games | Demonstration possible in constructed payoff game; real coding history untested |

### User-facing editorial decision

The short Paper B **should not** become an explanation of all four research programs. Keep the founding two-line thesis. Baldwin's 2023 author-retrospective and Räihä's design-fitness caution warrant at most **one added illustrative sentence** and a source link in each language. Details remain here for independent work. No need to force a new v37 while v36's question remains alive.

**Status:** CONCEPTUAL CROSS-FIELD SYNTHESIS DEVELOPED / 10 NEW PAPER PDF SOURCES CURATED IN R54 / NO NEW GENERAL MATH THEOREM OR AGENT-SPECIFIC BEHAVIOR OBSERVED.
