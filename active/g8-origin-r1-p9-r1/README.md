# EvoNOMOS Generation VIII ORIGIN-R1-P9-R1

**Clean-Wave Dual-Arm Reconstitution, Outcome-Silent Build/Commit Harness, Shared-Oracle Equivalence & Pre-Measurement Pair Comparability Adjudication**

Status: `PRESEAL_READY / EXECUTION_PENDING / OUTCOMES_CLOSED`

This is a new wave, not a repair of P9. The contaminated P9 DIRECT implementation and its diff are excluded from treatment-construction input.

## Inheritance

- Frozen source: `sumatrapdfreader/sumatrapdf@7061d827d0a31e3e623811991b5eb8ebda8b82ec`
- Frozen P9 treatment contract SHA-256: `4C99A9002BF37F27DEB2F580B9F4F74312B69BB37E5854AB8A6FCE35CA2EB58B`
- Frozen Rust fake-CLI behavior is inherited as an oracle specification only.
- P9 terminal state `HOLD_OUTCOME_BLINDNESS_BREACH` is historical evidence, not a construction donor.

## Clean-wave constitution

Both arms start from the same frozen SumatraPDF commit in isolated workspaces. Neither arm may inspect the other arm's patch, build output, artifact metadata, implementation, or sealed logs.

`DIRECT_DEDICATED` adds a dedicated C++ `AIChatProvider` for AIChat-NG.

`INVERT_SPEC` adds a reusable typed external-CLI provider mechanism and instantiates AIChat-NG as a specification value.

Existing Claude/Grok/Codex semantics are frozen.

## Shared neutral scaffold

Frozen-source inspection shows that the common functional contract requires neutral process/stream plumbing that is not itself the structural treatment: EOF remainder delivery, NUL-invalid-output detection, and non-zero child-exit surfacing. Any such changes must be byte-identical across both arms and sealed before arm-specific treatment bytes are admitted.

## Outcome-silent rule

Before pair comparability passes, no operator-visible command or CI surface may emit LOC, churn, additions/deletions, touched-file counts, binary sizes, timings, complexity, or any other downstream comparative proxy. Raw logs may exist only in sealed artifacts that are not inspected before firewall release.

Mandatory order:

`BUILD_ADMISSIBILITY -> CONTRACT_SATISFACTION -> SHARED_ORACLE_EQUIVALENCE -> PAIR_COMPARABILITY -> FIREWALL_RELEASE_ELIGIBILITY`

This phase ends at pre-measurement comparability adjudication. It does not authorize lifecycle measurement, a winner, or a design recommendation.
