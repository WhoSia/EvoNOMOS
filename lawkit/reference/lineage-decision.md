# LawKit Lineage Decision Gate

This gate decides whether EvoNOMOS should keep `ORIGIN-R1`, open `ORIGIN-R2`, graduate ORIGIN into a forward scientific lineage, or open a new Generation.

## Constitutional rules

1. `ORIGIN-R2` is event-counted, not age-counted. It requires a second documented post-recovery drift/return event.
2. A new Generation requires a material change in theory, ontology, data regime, measurement, Court, or authority.
3. ORIGIN graduation requires the founding explanandum to be restored in actual practice: real structural interventions, rival-policy competition, independent world contact, an observed reversal/failure boundary, and engineering-decision consequences.
4. An open experiment is never renamed midstream. A transition decision may be made, but its timing becomes `AFTER_ACTIVE_EXPERIMENT_TERMINAL`.

## Current G8 fixture

`lawkit/fixtures/g8-origin-lineage-decision.json` encodes the current constitutional state without using P12 outcomes. Its intended verdict is:

`GRADUATE_ORIGIN_TO_NEW_LINEAGE / AFTER_ACTIVE_EXPERIMENT_TERMINAL / Generation VIII LAW-R1`

This is a governance/development decision, not a scientific treatment result. It neither opens P12 outcomes nor changes the Generation VIII measurement constitution.

## Usage

```
node tools/lineage-decision.mjs --self-test
node tools/lineage-decision.mjs lawkit/fixtures/g8-origin-lineage-decision.json
```
