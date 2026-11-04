# P44 — Research OS Harvest backflow, not automated originality transfer

## Harvest material directly read 2026-11-04
1. [Research OS Harvest Citation and Provenance Audit — 2026-10-17](https://docs.google.com/document/d/1KfHbPocXjD1jo4Rb7sW_v9Mj56rwzjywUMU2DEYCnUk/edit) — citation identity, claim/page locator, passage-level authority ceiling and need to distinguish internal derivation from published source. Audit status was PARTIAL, not total certification.
2. [Harvest_LR-20260905-A.md](https://drive.google.com/file/d/1z91HQNm6RQZoqLSd7u9dTeDQpxmQmhVj/view) — Weyuker (1983) program inference and test adequacy, D. Richard Kuhn (1999) specification-based fault classes; 12 fragments with explicit pages, assumptions, counter-fragments and source ceiling.
3. [MQR-5.3 Evidence-Lineage Transport](https://docs.google.com/document/d/1rSArpBZ9GvYLkJrI5j3oEu6o-cdGobpi0xzmVj7SiH8/edit) — measurement/calibration, context-indexed observational equivalence, intervention mapping, transport error budget and nonidentifiability. This is **analogy from a distinct research domain**, not a direct software-maintenance theorem.

## Mathematical backflow that is useful, with strict boundaries

### H1: A test's adequacy is a different predicate from passing it
Weyuker program-inference adequacy distinction: source tests passing on a finite O do not establish O's capacity to detect the target family of semantic differences. In P44 specify both `Safe_C(p)` and `Adequate(O,H)` relative to a named hypothesis/fault family H. No universal Go adequacy from one synthetic suite. Any new counterexample incorporated into O consumes its independence and requires a new holdout.

### H2: Discrimination can be made claim-relative
Kuhn fault-class detection (subject to original text/symbol verification) motivates asking for a minimal separating observer set: for a finite model pair family Q, choose O* such that all behaviorally distinct relevant pairs receive a distinguishing probe. A 3-witness H/D/M suite was only complete for eight named masks, not arbitrarily source-edited code.

### H3: Host semantics and transport are separate evidence gates
MQR example: two models may agree observationally but disagree under intervention; transporting a result between environments needs a mapping of states and interventions and stability assumptions. P44 analog: comparing Chi/ServeMux requires mapping client observers, edit rights and cost units, **not** just matching GET outputs. The exact SEM intervention-transport theorem from causal abstraction is NOT directly applicable to source code without a proof of the mapping.

### H4: Proof facts, source interpretations and analogies must be separated
Harvest's record schema suggests one row per claim: SOURCE_ID, exact title/edition/DOI, canonical PDF ID, locator, claim, assumption, our formal translation, scope, strongest counterexample, conflict, confidence/evidence grade, next independent validation. No passage-level citation means claim is internally derived or a reading candidate, not established as a published theorem. A code CI does not establish theoretical priority.

### H5: Normalization and authority matter as much as an outcome
A change in observer, rights, cost scheme or scheduler creates a different formal problem. Do not transport a favorable cost inequality between them without a proof. Historical results and source files remain immutable and version-indexed.

## Practical research transfer
For P44 theorem T, create:
- original published theorem + exact original premises and proof target
- new mathematical formalization, whether it reduces to standard LTS/contextual refinement
- countermodel under one removed assumption
- executable finite witness if available
- independent maintainer-source and verification receipt
- remaining G1–G7 source gap
- verdict KNOWN / REFORMULATION / POSSIBLE_NEW / REFUTED / OPEN

**No new law declared from these cross-project analogies.**
