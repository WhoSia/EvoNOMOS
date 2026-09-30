# EvoNOMOS

Canonical repository for executable conditional software-design law research.

## Current scientific head

**EvoNOMOS Generation VIII LAW-R1-P5 — Blinded Design-Context Corpus, Principle-Prior Elicitation, LLM Maxim-Default Measurement, Evidence-Conditioned Rival Choice, Advice-Reversal Thresholds & Axiomization-to-Conditional-Law Bridge**

Current status: **CLOSED / PASS**.

P5 directly tests whether naming familiar software-design principles creates a maxim prior that overrides moderator evidence, and whether a more general evidence-conditioned decision representation can recover reversal or abstention.

### Canonical repaired field

- repaired corpus head: `378cb1cfe3a9506d2f7aefa5ea5eb2effd7a7d45`
- corpus CI: `36677116768`
- provider execution host: `WhoSia/EPISTEME`
- canonical provider run: `36677191280`
- artifact: `11080830212`
- digest: `sha256:59cd0b5fd11146dabe9ddb50a8d7af9bf637235a5e156e5f6dbed436c81ccc6b`

Historical run `36676553417` is non-authoritative because status-quo actions were semantically aliased with ABSTAIN in three cells.

### P5 result

The strong cross-model hypothesis that named SOLID-style principles systematically push LLM advice toward unsupported principle-congruent actions is **not supported** by the frozen three-interface pilot.

- Gemini 3.5 Flash Lite: 100% precommitted alignment in all three arms.
- GPT-OSS 120B: named-principle alignment 100%; unsupported named-maxim rate on non-APPLY cells 0%.
- GPT-OSS 20B: named-principle alignment 91.7%; unsupported named-maxim rate 16.7%, concentrated in DIP/OCP reversal cells.

This supports a narrower and more useful distinction:

**principle recognition / nomination ≠ principle authority**.

A familiar principle can be a useful compressed generator for a structural rival. Whether that rival deserves action must be decided from moderators, predicted outcome channels, falsifiers, world contact and update/revocation.

### Generalized candidate

`L = (X, A, Y, M, F, Π, U)`

- `X`: observable context / moderators
- `A`: genuine rival structural interventions + semantically distinct `ABSTAIN`
- `Y`: non-collapsed lifecycle outcome vector
- `M`: bounded mechanism predictions
- `F`: falsifiers / reversal / applicability boundaries
- `Π`: prospective partial decision policy
- `U`: empirical authority-update / revocation rule

SOLID is not rejected. SRP/OCP/ISP/DIP become candidate intervention generators; LSP is primarily an admissibility/substitutability constraint.

This candidate deliberately absorbs prior work on information hiding, ATAM/CBAM, real-options modularity, architectural tactics/ADD, fitness functions, technical-debt economics and evidence-based architecture. Any novelty claim weaker than the **joint operational authority loop** is withheld.

No SOLID true/false verdict, LLM-population claim, universal replacement claim or scalar architecture winner is authorized.

## Repository workflow

`main` is canonical. Current scientific surfaces live under `active/`; failed/reconstituted executions remain append-preserved as scientific provenance.
