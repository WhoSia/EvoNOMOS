# LAW-R1-P7 — Prior-art convergence kill for the first beyond-SOLID motif

## Discovery motif

The first cross-world motif emerged without SOLID labels:

- Kyverno #17769 — two loaders independently encoded supported PolicyException versions; drift caused valid inputs to be skipped; repair reused one shared semantic definition.
- ComfyUI_frontend #18700 — remote CRDT changes used a store-first mutation path plus reconciliation layers separate from the graph API used by humans/extensions; repair routed mutations through the graph API and deleted reconciliation machinery.
- TER #48 — scoring/pricing semantics lived in calculator implementation and hard-coded prices; repair moved scoring to a pure domain and price authority to versioned data behind a port.

Temporary motif name: AUTHORITY_PATH_CONVERGENCE_MOTIF.

Provisional shape:

> When multiple independently editable paths encode or mutate the same domain-semantic authority, drift or reconciliation burden can arise. A candidate intervention is to converge decisions/mutations onto one canonical behavioral authority while preserving legitimately distinct semantics outside that authority.

## Fresh out-of-stream challenge

CrewAI #7304 was frozen after the motif was formed and before reading the actual merged implementation.

Prediction precommit: active/g8-law-r1-p7/P7_OUT_OF_STREAM_CHALLENGE_1_PRECOMMIT.json

Actual merged repair: CrewAI #7796, merge a6e6d0f9d85a72dd03bc041b8ea4648f211b6d9e.

Observed:
- shared context-window definitions and resolver;
- native and LiteLLM paths migrated to the resolver;
- cross-path parity tests;
- provider-specific catalogs and Bedrock regional semantics retained rather than erased.

The holdout therefore supports the conditional motif.

## Novelty kill

The generic motif is not new.

Relevant prior families already own major parts of it:

1. Single-source-of-truth architecture explicitly treats duplicated semantic authority as a drift/inconsistency risk and derives secondary representations from an authoritative source.
2. Code-clone evolution literature shows the crucial boundary: duplicated code is not automatically harmful. Clones may be consistently propagated or may intentionally evolve independently.
3. Empirical release-level clone studies report that only a small minority of clone genealogies introduce defects, reinforcing that deduplicate-everything is not a valid general law.

Therefore the surviving candidate is narrower than SSOT:

> First determine whether two paths truly encode the same semantic authority. Convergence is a candidate intervention only when duplicated edit authority is causal to drift/reconciliation burden. Distinct semantics, intentionally independent evolution, derived read-only representations, and synchronization with a mechanical invariant are explicit falsifiers.

## P7 ruling candidate

- generic SSOT novelty: RETIRE
- deduplicate-all-semantic-copies: REJECT
- conditional semantic-authority convergence generator: ABSORB / REFINE
- generalized kernel: remains viable if it can discover a motif, challenge it out-of-stream, and then downgrade novelty when prior art owns it

This is a test of the discovery-and-authority-update loop, not a claim that EvoNOMOS invented SSOT.
