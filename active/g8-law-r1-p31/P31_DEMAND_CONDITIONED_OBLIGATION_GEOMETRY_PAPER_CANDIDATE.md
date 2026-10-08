# P31 — Paper Thesis Court: Demand-Conditioned Obligation Geometry

## Purpose and authority
SCIENTIFIC HYPOTHESIS / NO NEW EMPIRICAL WORLD RESULT. P31 remains OPEN and structural-law MAINLINE HOLD. The original EvoNOMOS aim is a deeper causal account of object-oriented organization from which some SOLID guidelines can arise *conditionally*, not SOLID axiomatization. No LAW-R2 or manuscript acceptance claim.

## Literature threat refreshed 2026-10-08
- Parnas, CACM 1972, DOI 10.1145/361598.361623: information hiding by likely change is established.
- Geipel & Schweitzer, IEEE TSE 2012, *The Link between Dependency and Cochange*: structural dependencies alone badly approximate co-change; design evaluation needs both structure and change properties.
- Ajienka, Capiluppi & Counsell, EMSE 2018, DOI 10.1007/s10664-017-9569-2: semantic coupling and co-change strength are not simply interchangeable.
- Large co-change-pattern studies and contextual pattern maintenance experiments already cover many explanatory claims.
Consequently **'meaning matters', 'co-change matters', 'boundaries should reflect variation', 'simple coupling metrics fail' and 'SOLID is contextual' are prior art**, NOT EvoNOMOS novelty.

## Best creative candidate: Demand-Conditioned Obligation Geometry (DCOG)
Focus on a *requirement* and a *realization contract*, not simply a class name or static dependency edge.

Let U be externally observable user obligations and C the concrete implementer/client set. A demanded change d induces a relation R_d⊆C×U: (c,u) means realization c must implement, authorize, preserve, or adapt obligation u for d to be correctly implemented under the chosen architecture. Distinguish:
- positive **co-requirement**: same semantic update required by multiple clients;
- negative **noninterference**: an obligation must affect one client but must NOT leak to another;
- **capability burden**: interface conformance forces an implementer to supply a capability unused for the demand;
- **realization tax**: adapting a shared boundary, adapter, tests, rollout or an additional interface.
These are a **hypothesized useful vocabulary**, not an established minimal ontology or novel construct in its own right.

Candidate mechanism: architectural intervention a changes the allocation R_d and the extra coordination edges required to honor its constraints. Measured lifecycle effect vector V(a,d,history)=(S,L,C,A,Q) may depend on both topology and which obligation relations d actually activates.

## Required discriminator, not decorative counterexample
Construct a 2×2 crossed contrast:
- architecture: a_D independent client-owned realization; a_S shared-boundary realization;
- independently justified demand: d_J both consumers must apply identical rule; d_X one consumer must apply a different rule and the other must remain unaffected.
Hold baseline code semantics, initial capability correctness and acceptable interfaces fixed. Collect V and Q for each cell.
Before the run, freeze:
B0: structural edge / degree / file-count / interface-method-count model.
B1: a strong baseline using historical co-change, identifier/semantic coupling and requirement trace where available.
H: demand-conditioned obligation+noninterference graph.
**Admit only a contrast for which B0 and B1 demonstrably give a different prospective sign/Pareto prediction from H**, or a precise calibrated abstention gap. If B1 can encode the distinctions and predict equally well, H has no incremental contribution; reject stronger novelty.
B2: full-system source mutation footprint and initial implementation tax, preventing moved-code cost sleight of hand.

## What would make this paper worthwhile
- Empirical generation and verification of distinct predicted change effects across *independently sourced* real OO cases, not naming a law.
- A principled link between ability/obligation allocation and actual lifecycle consequences, with correctness held equal.
- Out-of-sample selection or abstention better calibrated than state-of-art stronger baselines (including semantic and historical change coupling). Not just a static-degree comparator.
- Recover SRP/DIP/ISP-like choices under explicit demand constraints; demonstrate a real condition in which their recommendation is dominated or non-comparable. Keep LSP contractual substitutability apart from optimization advice.
- Report negative cells, construction/adapter overhead, failures, and S/L/C/A/Q noncollapse.

## What would kill it
1. An enhanced historical co-change/semantic coupling model predicts the held-out demands just as well.
2. The two implementations do not meet the same complete external requirement.
3. The 'hidden obligation' variable is coded from observed future outcomes (leakage).
4. A reversal follows only from hand-coded arbitrary test helpers, or a deliberately uneven code base.
5. One unique source repository or one narrowly scoped test repeated many times masquerades as replication.
6. Any unsupported universal derivation of SOLID or collapse of Q to a performance score.

## Immediate paper positioning
Provisional research question: **Can demand-conditioned obligation allocation predict the signed lifecycle effect of OO boundary interventions beyond static architecture and historical co-change/semantic models?**

Provisional possible title (NOT a submitted paper): **When Should Object-Oriented Boundaries Be Shared or Split? A Demand-Conditioned Study of Implementation Obligations and Change Effects**.

The strongest scientific result today is a sharp *novelty and falsifiability criterion*, not a proved theory. P31 should spend its next limited budget on designing a single baseline-disagreeing contrast with real complete functionality, not on more world contacts or ceremonial receipts. Scientific status: `P31_DCOG_CANDIDATE_HYPOTHESIS__NO_INCREMENTAL_PREDICTION_DEMONSTRATED`.
