# EvoNOMOS — Competing Source-Boundary Design Protocol (Viper provenance)

**2026-11-10 KST · PRE-IMPLEMENTATION FREEZE · NO CLAIM OF INDEPENDENT BLIND FUTURE TASK**

## Scope and substrate
Actual independently maintained original `github.com/spf13/viper@v1.21.0`, underlying pinned release commit `394040caccbdf5821fa6839386a35f0fb1b1ee9e`. Current old client: `Read` obtains effective `service.token` as `same-token`; the YAML config stores `same-token`; `APP_SERVICE_TOKEN` can be absent or set to the same value. App-owned boundaries, not upstream patch.

Independent externally issued [Viper issue #2161](https://github.com/spf13/viper/issues/2161) motivates effective-origin information. The following delayed forensic query is RESEARCHER-AUTHORED after reading #2161, not an externally unforeseeable issue or C5 prospective test.

## Actual competing architecture choices, ALL currently correct
- **L: lazy-value**: `Read` returns effective value and never records source, and `OriginNow` checks the current known env variable.
- **S: source-snapshot**: `Read` returns value plus effective-source label at read time; later observations can refer to this immutable snapshot.
- **J: journal-rival**: `Read` writes the effective source to an append-only app-owned observation log keyed by stable record ID; returned record has value and ID but no direct provenance field. This is a STRONG rival that preserves exactly the necessary bit in a different representation. No claim that S alone has the ability.

Frozen W0: at t0 `APP_SERVICE_TOKEN` absent, read value `same-token`; at t1 env variable set to `same-token`.
Frozen W1: at t0 env variable set to `same-token`, read same value; at t1 variable removed. The same old value and selected Viper `GetString/IsSet/InConfig/AllSettings` should be identical at t0 between W0/W1 as previously source-verified.

**Demand A (historical audit):** a later client needs source as it was at read time t0. Expect L without a record to report present environment, thus WRONG in both switch worlds. S and J preserve old historical source. Under a fixed L design a proper repair requires logging a provenance bit at t0, which cannot be retroactively recovered if no original environment-state log is available.

**Demand B (live refresh):** later client needs source **now** at t1, not original t0. Expect fresh env inspection works for L; snapshot S and journal J must also expose a separate explicitly live lookup and NOT be mistakenly used as live. An app that confuses historical source with live source fails. This is API semantics, NOT a claim that snapshot architecture is inherently unable to handle live refresh.

**Strong source-aware classical competitor**: known-name `os.LookupEnv` at t0 with a timestamped audit event preserves the same bit as S/J. Any added advantage from a fancy record type or interface vanishes against a same-information recording comparator.

## Formal interpretation
Let `H_0` be the env presence bit at read time and `H_1` the bit at later query. Historical audit goal `d_A=H_0`; live goal `d_B=H_1`. If storage state contains only `value` and fresh `H_1`, the pair `(H_0,H_1)` cannot be reconstructed when two initial worlds have the same value but differing `H_0`, despite opposite `H_1` transition paths unless history is encoded somewhere. This is a classical irreversible-information-loss argument; not a new result and not about arbitrary Viper source precedence.

A later expected-cost policy threshold may be expressed as `c_capture < P(d_A) L_missing` for stylized one-time capture cost and missed-audit penalty, but its cost/probability inputs are NOT measured. No real design superiority from this inequality alone.

## Outcome and falsification
- Native original pinned Viper module in app Go tests; old functional equality, two switched world observations, D_A, D_B, journal rival, classic direct timestamp audit, source current-vs-historical distinction. Tests that assert EXPECTED L failure yield green results; they do not certify L meets D_A.
- Structural cost measured only as Go production code lines, optional allocations/benchmark if stable, not developer hours or system economics.
- If original source semantics differ, fail tests rather than adjust claims. Do NOT assert C5, full original Viper SourceOf semantics, or independent future-demand prediction.
- New scientific insight only if genuinely out-of-sample conditional architecture policy beats strong same-information, same-decision-time rivals. Otherwise classify as useful information-timing mechanism with classical tie.
