# Chat 26 — P35-P4 415/204 Historical Negative Control and Repaired Baseline

**Archive source:** \`25.md\` lines 937–1233; GitHub historical source/CI links recorded there. No fresh Go execution claimed in Chat 26.

Initial two structures: original pinned go-chi/chi v5.1.0, independent parser policy versus shared *policy source*. Both passed 16 old cases, but on a POST with a nonempty body, absent Content-Type, and \`AllowContentType("")\`, Independent returned HTTP 415 while Shared returned 204 (research test handler's response). These are different *current* behaviors; a subsequent differential modification cannot attribute that discrepancy to the modification.

The corrective edit was **not** to make the entire shared parser reject empty media type: a separate \`ContentCharset("")\` old-client path relied on existing behavior. Instead the shared Content-Type middleware narrowed its check. Archive reports the fixed Go original-source run #43416391326 PASS for the 16 baseline + 10 extra cases *per arm*, full Chi-module tests and middleware race tests. This is finite observer equivalence only.

**Performance correction:** Shared source definition is not shared *memoized computation*. In a request traversing two middleware components, both call media-type parsing even if both import the same shared function. Never infer CPU performance superiority from policy-source centralization.

## Consequences for F38

1. Freeze the query domain and exact wire observables *before* comparing architectures.
2. Run a blind/mutation-selected negative-control probe to expose baseline mismatch; a discovered mismatch must trigger BASELINE_FAIL or narrowed-contract disclosure, not a fabricated design advantage.
3. Count edits used solely to normalize the initial baseline as setup debt.
4. The changed policy's contract scope must not regress other clients (\`ContentCharset("")\` is the motivating example).
5. If authoring a prospective task on F37, do not import a P35 fix as “unseen customer need.”

**External validity:** 415/204 is one historical test setting, not proof that independent middleware designs are universally superior.
