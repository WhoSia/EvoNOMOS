# EvoNOMOS LawKit

LawKit is the executable theory/tool layer of EvoNOMOS.

Its purpose is not to encode SOLID, DIP, OCP, ISP, DRY, or another software-design maxim as a commandment. It turns **world evidence + prospectively frozen demands + architecture moderators + lifecycle evidence + authority constraints** into bounded conditional-law statements, falsifiers and abstentions.

## Product thesis

Traditional design guidance often starts from:

`principle → implementation advice`

LawKit targets:

`exact world → real demand pair → source evidence → moderator geometry → candidate mechanism → prospective intervention → lifecycle evidence → bounded law / reversal / abstention`

That makes it usable during actual development without pretending that a named rule is universally correct.

## Commands and protocol surfaces

```bash
evonomos-law inspect <moderator-envelope.json>
evonomos-law adjudicate <moderator-envelope.json> <lifecycle.json> <authority-firewall.json>
evonomos-law admit-world <world-envelope.json>
```

- `inspect` — pre-outcome mechanism inspection; no design choice.
- `adjudicate` — post-outcome coordinate/reversal classification under an explicit authority ceiling.
- `admit-world` — conjunctive fresh-world admission; no scalar repository score and no design recommendation.
- `lawkit/measurements/provider_family_lifecycle_v01.py` — exact-Git two-phase provider-family lifecycle measurement over `S/L/C/A/Q`.
- `lawkit/courts/cil_cbl_support_v01.mjs` — support-domain court for CIL-C1 and CBL-C1 with explicit no-winner semantics.

## Source adapters

`lawkit/adapters/` is the developer-facing evidence compiler.

The first adapter, `github_provider_family_v01.mjs`, checks an exact Git checkout against a frozen source-evidence specification. It verifies source identity, architecture authority sites, runtime interface evidence and pre-demand provider absence. The adapter emits evidence; it does not choose an architecture.

The protocol is canonical; implementation language is not.

## Current candidate laws

- **CIL-C1 — Conditional Inversion / Membership-Propagation Law Candidate**
- **CBL-C1 — Capability-Bundle Mismatch Law Candidate**

P11 sharpens the distinction between them: membership-surface propagation (`S`) and handwritten source churn (`L`) can dissociate across worlds, while capability-conformance burden (`C`) can remain independently measurable.

## Development direction

1. source adapters extract auditable world evidence;
2. world-admission protocols reject contaminated or non-discriminating cases;
3. rival constitutions define bounded interventions before treatment bytes;
4. Actions executes exact-world experiments under log firewalls;
5. lifecycle measurement preserves distinct coordinates instead of scalarizing them;
6. support-domain courts update candidate laws without recommending a winner;
7. law families compete, fail, split, mutate or retire.

A better LawKit is an engineering achievement. New scientific authority still requires fresh world contact.
