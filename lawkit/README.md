# EvoNOMOS LawKit

LawKit is the executable theory/tool layer of EvoNOMOS.

Its purpose is not to encode SOLID, DIP, OCP, DRY, or another software-design maxim as a commandment. It turns **observable architecture conditions + prospective lifecycle evidence + authority constraints** into bounded conditional-law statements, falsifiers, and abstentions.

## Product thesis

Traditional design guidance often starts from named rules:

`principle → implementation advice`

LawKit is intended to support the opposite workflow:

`world evidence → moderator envelope → candidate mechanism → prospective intervention → lifecycle evidence → bounded law / reversal / abstention`

That makes it usable during actual software development without pretending that a rule is universally correct.

## Commands today

The canonical Rust implementation currently exposes:

```bash
evonomos-law inspect <moderator-envelope.json>
evonomos-law adjudicate <moderator-envelope.json> <lifecycle.json> <authority-firewall.json>
```

- `inspect` is pre-outcome: it may expose mechanism opportunities and resistance but must abstain from choosing a design.
- `adjudicate` is post-outcome: it may classify coordinatewise directions and reversals but must preserve the supplied authority ceiling.

## Language policy

**The protocol is canonical; implementation language is not.**

Current independent implementations:

- Rust — deterministic typed kernel
- Python — independent reference semantics
- Node.js — independent authority/output verifier

Future components may use TypeScript, C++, Haskell, Scala, Kotlin, OCaml, Prolog, Ada, D, R, or another language when that language supplies a useful property: IDE integration, static analysis, graph inference, solver semantics, compilation guarantees, interactive UI, or independent replay.

Choosing a language is an engineering decision inside the experiment, not a scientific axiom.

## Current law candidate

`CIL-C1 — Conditional Inversion / Membership-Propagation Law Candidate`

P10 produced an exploratory coordinate split:

- semantic membership surfaces: initial inversion tax, then lower follow-up propagation;
- handwritten source churn: no sign reversal within one follow-up;
- overall winner: forbidden;
- confirmatory authority: held.

This is precisely the sort of result LawKit is built to preserve without collapsing into “use DIP” or “do not use DIP.”

## Development direction

LawKit should grow as a real developer-facing harness:

1. source adapters extract moderator envelopes from repositories;
2. protocol schemas define observable conditions and authority ceilings;
3. independent kernels evaluate candidate conditional laws;
4. CI executes prospective interventions and lifecycle probes;
5. editor/CLI surfaces explain **why authority is bounded**;
6. future law families compete, fail, fork, or retire.

Tool quality is an important engineering axis, but a better tool is not automatically new scientific evidence. EvoNOMOS mainline progress still requires fresh world contact and discriminating observations.
