# Generation VIII LAW-R1-P5

**State:** CLOSED / PASS

## Canonical scientific authority

- repaired corpus head: `378cb1cfe3a9506d2f7aefa5ea5eb2effd7a7d45`
- corpus constitution CI: `36677116768` — SUCCESS
- execution host: `WhoSia/EPISTEME` (provider secrets / calls only)
- canonical provider field: `36677191280` — SUCCESS
- provider-host head: `f9f61ad94af5e2543bf4ef1e829eca8d36043ad5`
- artifact: `11080830212`
- digest: `sha256:59cd0b5fd11146dabe9ddb50a8d7af9bf637235a5e156e5f6dbed436c81ccc6b`

Historical run `36676553417` is explicitly **NONAUTHORITATIVE_ACTION_ALIASING_BUG**. Its ABSTAIN cells contained semantically overlapping status-quo choices. Run `36677159816` failed preflight before scientific calls.

## Result

The strong hypothesis

> naming a familiar SOLID-style principle systematically pushes LLM design advice toward that principle even when moderator evidence says REVERSE or ABSTAIN

is **not supported across the frozen interfaces**.

### Gemini 3.5 Flash Lite

All three arms reached 100% precommitted alignment. Named-principle priming caused zero unsupported maxim choices.

### GPT-OSS 120B

- context-only alignment: 91.7%
- named-principle alignment: 100%
- evidence-conditioned alignment: 97.2%
- named-principle unsupported maxim rate on non-APPLY cells: 0%

Notably, the named ISP prime recovered the CBL APPLY cell that context-only missed without creating errors on the CBL ABSTAIN cell.

### GPT-OSS 20B

- context-only alignment: 97.2%
- named-principle alignment: 91.7%
- evidence-conditioned alignment: 94.4%
- named-principle unsupported maxim rate on non-APPLY cells: 16.7%

The named-prime errors were concentrated in:
- DIP_REVERSE: 2/3
- OCP_REVERSE: 1/3

This is a **model-conditional priming signal**, not an LLM-wide maxim-prior result.

## Theoretical consequence

P5 does **not** justify “SOLID is harmful” or “LLMs blindly follow SOLID.”

A better surviving interpretation is:

> Named principles can be useful compressed **candidate-action generators**, but their names do not carry scientific authority. Authority comes from context, moderators, rival interventions, observed lifecycle vectors, falsifiers and world contact.

The promoted candidate kernel is:

`L = (X, A, Y, M, F, Π, U)`

where:
- `X` = context / moderators
- `A` = admissible rival interventions + semantically distinct `ABSTAIN`
- `Y` = non-collapsed lifecycle outcome vector
- `M` = bounded mechanism predictions
- `F` = falsifiers / reversal / applicability boundaries
- `Π` = prospective partial decision policy
- `U` = authority-update / revocation rule

SOLID components become lower-level generators or constraints inside this kernel, not axioms.

## Prior-art ceiling

The kernel deliberately absorbs rather than reclaims:
- Parnas information hiding / volatility sensitivity
- ATAM / CBAM tradeoff and economic decision analysis
- Baldwin–Clark / Sullivan real-options modularity
- architectural tactics / Attribute-Driven Design
- fitness functions
- technical-debt economics
- evidence-based software architecture

P5 novelty, if it survives a deeper review, lies only in the **joint operational structure**: named-principle demotion + moderator-conditioned rival choice + vector outcomes + sign reversal/failure boundary + explicit abstention + empirical authority update/revocation.

No SOLID true/false verdict, LLM-population claim, universal replacement claim or scalar architecture winner is authorized.
