# EvoNOMOS LawKit Protocol v0.2

LawKit v0.2 adds **post-outcome authority adjudication**.

The protocol remains implementation-language neutral. Rust is the canonical
deterministic kernel for this revision; Python is an independent semantic
implementation; Node.js provides a third verifier.

Inputs:
1. a pre-treatment moderator envelope;
2. a lifecycle exposure object containing both raw arm vectors;
3. an authority firewall.

Outputs may describe phasewise direction, sign reversal and moderator
consistency. They must preserve the authority ceiling supplied by the
firewall.

For P10-P3 the mandatory ceiling is `HOLD_SELECTION_BLINDNESS`.
Therefore no implementation may:
- promote CIL-C1 confirmatorily;
- emit an overall design winner;
- recommend DIRECT or INVERT generally;
- claim SOLID/DIP/OCP validation;
- count the synthetic Pushover follow-up as an independent replication.

The protocol is canonical; implementation language is not.
