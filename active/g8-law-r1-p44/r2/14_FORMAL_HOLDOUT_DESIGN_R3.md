# Prospective R3 design gate, no evidence claimed

Objective: test whether a source-checkable repair simulation certificate can predict *unseen* old-client-safe modifications in a source pair with nontrivial shared-state or middleware dependencies. Benchmark against a classical source-aware edit search.

Required conditions:
- externally motivated maintenance tasks or fixed chronological PR cohort chosen independently of source differences;
- immutable source SHA and client observation family before seeing outcomes;
- independently implemented source-aware rival with same input source, rights, evidence and CPU budget;
- dynamic execution receipts for every intermediate patch and a negative-control old-client regression;
- no source program family selected solely because the expected EAC advantage is already known;
- record failures and human-context covariates where applicable.

Prefer actual upstream or user-owned application repositories with verifiable licensing/rights. R3 is an experiment proposal, not a result or a commitment to a new theorem.

Promotion off-ramp: if classical source analysis already captures all path feasibility and costs, record equality and search for compression/transport/verification efficiency, not a new law label.
