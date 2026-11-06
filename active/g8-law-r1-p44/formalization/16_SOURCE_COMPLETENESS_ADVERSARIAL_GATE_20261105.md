# P44 source graph completeness — the central remaining unsolved requirement

## A potentially fatal misinterpretation

A finite exact shortest-path result is an exact optimum for THAT graph. It is not a lower bound for all source patches when the graph omits authorized edits. The older edgecert test 'SOURCE_COMPLETENESS_VIOLATION' demonstrates an apparently certified K=4 that becomes K=1 once an overlooked authorized direct patch is added.

Precisely, if a bounded edit relation E_small is only a subset of the actual permitted E_full, then
   K_full <= K_small
under unchanged semantics, costs and observation predicates. Thus a finite minimum in a restricted grammar is at best an upper bound on a more permissive actual optimum if its exhibited patch is valid; it is **not** automatically a lower bound on the full optimum.

To transport the finite theorem to real source, require one of:
A. a genuinely complete declared domain grammar that exactly specifies the claimed benchmark's allowed patches;
B. a sound whole-source symbolic lower-bound argument showing every cheaper actual authorized patch impossible;
C. a verifiable proof-carrying source policy (e.g. signed allowed edit catalogs + trusted completeness scope) restricted to precisely stated rights.

Source ownership may be partial or unknown. Mark missing/unknown edges as **UNKNOWN**, never FALSE. A checker can prove finite-image obligations without proving the completeness of inputs.

## Source extraction obligations

1. Pin source tree SHA, package/module dependency versions and build tags.
2. Define edit operations in terms of actual parser/typechecked source transformations and provenance/actor rights, not a mere right-name string.
3. Establish sound source semantics or a carefully limited abstract runtime trace language including joint client response tuples and selected schedules.
4. Prove all relevant allowed source transformations are captured or represent missing transformations conservatively.
5. Establish execution-equivalent semantics and authorized per-step cost projection.
6. Test false positives and negatives against a strong source-aware classical verifier using the identical edit universe, customer observer and compute budget.

The research value may lie in proof compression, compositional transfer and certificate checking rather than stronger correctness than a complete classical oracle. This must remain an explicit novelty gate; LAW-R2 HOLD.
