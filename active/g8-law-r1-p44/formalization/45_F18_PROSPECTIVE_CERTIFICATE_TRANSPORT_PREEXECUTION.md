# P44-F18 — Pre-execution protocol: source-backed alias footprint certificate transport

FROZEN PLAN issued 2026-11-05 AFTER F17 final CI and BEFORE any F18 tests. This is NOT a claim of completed research, preregistered third-party blind data or future source robustness.

## Founding question and falsifier

Can a bounded, independently verifiable source alias/footprint certificate created for one Go release be reused after later source edits, and does reuse reduce verification work compared to strong ordinary classical points-to/source analysis without losing correctness or rejecting valid harmless changes?

Null hypothesis H0: conventional go/types + exact closed-grammar AST alias analysis on each source revision matches certificate precision and has comparable or lower total workload. Alternative H1 requires provable correctness, no false safety, and an actual measured gain on a meaningful diverse independent source cohort. Simple renaming of pointer variables does not by itself constitute novel certificate transport.

## Evidence and scope

1. Preserve exact baseline source commit `29b298ac33adf21951c27cb785fe758488e77b38` for F17 tested Go source fixtures. F17 supports precisely two typed Go constructors and a known runtime write; it does not cover ordinary repository source edits.
2. Develop a source-backed certificate containing source-content digest, named allocation sites, observed client boundary and read/write footprint plus a small checker. Explicitly decide whether exact byte SHA invalidates harmless renames or whether sound source AST canonicalization is proved.
3. Independent source revisions should include: harmless renaming/format changes (should preserve certificate meaning), repaired pointer split (must change safety classification), previously unmodeled pointer writes/escapes (must be REJECT/UNKNOWN), and a syntactically accepted but semantically dependent case if one can be legally constructed in an expanded grammar. Do not silently alter F17 closed grammar to admit these cases.
4. Compare two branches on the same code revisions and compute budget: A=certificate generation+verification/transport, B=classical `go/types` and full exact bounded alias analysis. Record bytes, parser/typechecking CPU, cache invalidations, false accept/reject and correctness.
5. If certification re-verifies all AST with the same cost as classical analysis, label CLASSICAL TIE; do not claim performance from counting only checker time while omitting certificate generation and invalidation.
6. Use source/raw CI SHA and immutability of tests. Reviewer-selected fixtures are NOT independent third-party blind data. Holdout from external maintained source requires a separately pinned unbiased selection protocol.
7. Preserve negative outcomes in the README/Notion and do not graduate to LAW-R2 on one finite state graph or synthetic task.

## BFS return gate

Regardless of F18 outcome, ask whether it improved the fundamental problem of predicting future safe edits in real software with authenticated owner rights, complete customer observations, independent task cohorts, human labor and equal-information classical comparison. A failed certificate transport may be the informative result.

**Status: protocol only; F18 implementation and results NOT yet started.**
