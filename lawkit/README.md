# EvoNOMOS LawKit

LawKit is the executable theory/tool layer of EvoNOMOS.

Its purpose is not to encode SOLID, DIP, OCP, ISP, DRY, or another software-design maxim as a commandment. It turns **world evidence + prospectively frozen demands + architecture moderators + lifecycle evidence + authority constraints** into bounded conditional-law statements, falsifiers and abstentions.

## Product thesis

Traditional design guidance often starts from:

`principle → implementation advice`

LawKit targets:

`exact world → real demand pair → source evidence → moderator geometry → candidate mechanism → prospective intervention → lifecycle evidence → bounded law / reversal / abstention`

That makes it usable during actual development without pretending that a named rule is universally correct.

## Commands today

```bash
evonomos-law inspect <moderator-envelope.json>
evonomos-law adjudicate <moderator-envelope.json> <lifecycle.json> <authority-firewall.json>
evonomos-law admit-world <world-envelope.json>
```

- `inspect` — pre-outcome mechanism inspection; no design choice.
- `adjudicate` — post-outcome coordinate/reversal classification under an explicit authority ceiling.
- `admit-world` — conjunctive fresh-world admission; no scalar repository score and no design recommendation.

## Source adapters

`lawkit/adapters/` is the beginning of the developer-facing evidence compiler.

The first adapter, `github_provider_family_v01.mjs`, checks an exact Git checkout against a frozen source-evidence specification. It verifies source identity, architecture authority sites, runtime interface evidence and pre-demand provider absence. The adapter emits evidence; it does not choose an architecture.

Future adapters may use TypeScript, C++, Haskell, Scala, Kotlin, OCaml, Prolog, Ada, D, R or another language when useful. **The protocol is canonical; implementation language is not.**

## Current candidate laws

- **CIL-C1 — Conditional Inversion / Membership-Propagation Law Candidate**
- **CBL-C1 — Capability-Bundle Mismatch Law Candidate**

CBL-C1 asks whether reusing an existing abstraction that requires capabilities outside the real demand creates conformance burden or semantic overclaim, and when capability segregation repays its own coordination cost.

## Development direction

1. source adapters extract auditable world evidence;
2. world-admission protocols reject contaminated or non-discriminating cases;
3. rival constitutions define bounded interventions before treatment bytes;
4. Actions executes exact-world experiments under log firewalls;
5. LawKit classifies vector-valued lifecycle results without scalar winners;
6. editor/CLI surfaces explain both candidate mechanisms and why authority is bounded;
7. law families compete, fail, split, mutate or retire.

A better LawKit is an engineering achievement. New scientific authority still requires fresh world contact.
