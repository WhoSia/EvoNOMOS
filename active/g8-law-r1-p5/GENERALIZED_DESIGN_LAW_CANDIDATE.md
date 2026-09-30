# LAW-R1-P5 — Generalized Design-Law Candidate (Pre-Outcome)

**Status:** HYPOTHESIS / NOT YET PROMOTED

## Candidate object

A software-design law is not a maxim. It is a revocable partial decision rule over structural interventions.

Define a candidate law as the tuple

[
mathcal{L} = (mathcal{X}, mathcal{A}, mathbf{Y}, M, F, Pi, U)
]

where:

- (mathcal{X}): observable context and moderator space;
- (mathcal{A}): admissible rival structural interventions, always including `ABSTAIN`;
- (mathbf{Y}): non-collapsed lifecycle outcome vector;
- (M): bounded mechanism predictions linking interventions to outcome channels;
- (F): falsifiers, reversal surfaces, and applicability boundaries;
- (Pi): prospective decision policy that maps evidence to an intervention test or `ABSTAIN`;
- (U): authority-update rule after world contact.

The policy is **partial**, not total:

[
Pi(x,e) in {a_1,dots,a_k,mathrm{ABSTAIN}}
]

and may be undefined or abstaining when evidence does not identify a warranted rival.

No scalar utility function is required. Outcomes may remain Pareto-incomparable.

## SOLID as lower-level generators

Under this candidate, SOLID is not rejected. Its components are demoted from authority to reusable generators/constraints:

- **SRP** → proposes responsibility/authority partition interventions when change causes are separable.
- **OCP** → proposes extension-boundary interventions when variant arrival recurs behind stable core semantics.
- **LSP** → supplies a substitutability/admissibility constraint on candidate subtype interventions rather than a universal refactoring command.
- **ISP** → proposes capability/interface partition interventions when client demand leaves truthful extraneous conformance burden.
- **DIP** → proposes dependency-direction / policy-boundary interventions when implementation volatility is high behind comparatively stable policy semantics.

Each generator can yield `TEST`, a rival action, or `ABSTAIN` depending on moderators.

## Relation to prior art

This candidate deliberately absorbs rather than competes with:

- Parnas: volatility-sensitive information hiding;
- ATAM: scenario- and quality-attribute-sensitive tradeoffs;
- CBAM: economic comparison of architecture alternatives;
- Baldwin–Clark / Sullivan: option value and DSM-based modularity;
- architectural tactics / ADD: quality-driven structural tactics;
- fitness functions: executable architectural constraints;
- technical-debt economics: horizon- and uncertainty-dependent costs.

The surviving additional structure is the **empirical authority loop**:

[
	ext{moderators}
ightarrow
	ext{rival intervention}
ightarrow
mathbf{Y}
ightarrow
	ext{mechanism/falsifier adjudication}
ightarrow
	ext{support/reversal/abstention}
ightarrow
	ext{authority update}
]

plus direct measurement of whether named principles distort LLM design choice relative to moderator evidence.

## Strong falsifier

This candidate loses much of its reason to exist if prior work is found that already jointly provides:

1. named principle/tactic demotion to rival generators rather than fixed authority;
2. moderator-conditioned action selection;
3. multi-objective observed lifecycle effects;
4. empirical sign reversal/failure boundaries;
5. explicit abstention;
6. prospective world-contact updating/revocation;
7. operational use as a design-decision policy.

P5 does not claim this conjunction is novel until the literature court is deeper than the current sweep.

## P5 bridge prediction

If named-principle priming increases unsupported principle-congruent action on REVERSE/ABSTAIN cells while evidence-conditioned framing restores the precommitted rival/abstention choice, that is evidence for separating:

**principle recognition competence** from **principle authority**.

If no such effect appears across the frozen interfaces, the LLM-maxim-prior branch is weakened, but the generalized conditional-law candidate may still stand on non-LLM software-design grounds.
