# P36-O3 — Original Chi D14/D15 Repair-Option Survival: Retain vs Erase

**2026-10-10 KST · HUMAN PRE-SOURCE SEAL · P36 active · P35 closed.** This is a deliberately source-grounded, **classically explained information-retention** calibration, not a DIP-49 strong-law separation. Strong prior: multiple plausible software patches can pass existing tests yet behave differently under independent future requirements (Qi et al., ISSTA 2015; APR overfitting literature); retention and erasure limitations also follow classical information theory.

## Source and fixed demand

Exact original `go-chi/chi v5.1.0@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`, augmented with the already native-PASS *EAGER* synchronized [P35-O6 source](../../tools/p35-o6/arms/eager/p35_epoch_router.go). No upstream edits, global library replacement, arbitrary reflection, external historical log, or caller-supplied middleware used during restore.

**D14**, new independent mutable-route demand: `DisableRoute(header, match string) bool` hides the **earliest currently enabled, exact-match, lower-case ASCII route** for the specified header and match, while keeping all other routes and original first-registration priority. A successful change increments the revision and publishes a new immutable snapshot before returning. Missing route is a false no-op without revision increment. Its scope explicitly **excludes wildcards, RouteAny membership and cross-header winner ranking** to avoid modifying historical Chi experiments. Existing registration, RouteAny, default fallback, initial 16U/16R trace and concurrency API must remain intact. D14 defines observable *serving behavior only*, not a future restore requirement.

Freeze **TWO legal, genuinely different D14 source treatments** under the explicit two-candidate finite grammar `Γ_obs={RETAIN,ERASE}`:
1. RETAIN: remove the route from the published enabled list but retain the original `HeaderRoute` middleware closure plus insertion index in a synchronized private disabled-rule store.
2. ERASE: physically remove the exact route from the registry and do **not** retain the old closure, insertion index or any copy/history under the authorized wrapper state. Its new disable method may only use current registry, no external log.

The two source files must have **different SHA**, preserve identical D14 output tests and original Chi full/race/vet. Their code is written *after* this seal and after BOTH D14 and D15 frozen independent tests.

## D15 future demand, sealed before either D14 source treatment

Under the same exact dynamic API, `EnableRoute(header,match string) bool` must recover the disabled **same original middleware closure** at its original priority **without requiring caller to re-register or supply that closure**, even if requests have already been served after Disable. As part of the D14 candidate grammar, both versions declare `EnableRoute` but D14 itself does not require it to do anything. Thus the D15 oracle is **not** part of D14’s pass contract; only the frozen, separate future-demand test probes it.

Predicted:
- RETAIN will pass D14 and D15 (an existing saved middleware closure is enough, assuming correct reinsertion and synchronized revision updates).
- ERASE will pass D14 but fail the independent D15 `EnableRoute` acceptance; a no-log/no-input deterministic continuation cannot recreate arbitrary lost closure identity across two different closure histories whose current retained state is the same.

**Negative control:** Two initial worlds use distinct middleware tags `alpha` vs `beta`, identical remaining duplicate route and baseline. After ERASE+served request, their current authorized states are identical (modulo discarded historical ephemeral pointers); demanded Restore returns different original tags. This is classic indistinguishable-state non-invertibility. It does **not** establish that all software architectures must retain every deleted route: authorized event sourcing/persistence/re-registration semantics can restore information through external channels; they must be explicitly permitted as a different Γ and policy.

## Exact mathematical reading

Let `R_{14}^{Γ}(A)` be the set of two *observed* valid source patches (when CI confirms). Let `P_{15}(B)` mean B passes D15 without further Go source edit: `Surv_0(B,D15)`. Under both native outcomes as expected, `May_{R14}(P15)` holds and `Must_{R14}(P15)` fails **only for the enumerated two-member Γ_obs**, not for every legal real-Go D14 patch. The D15 requirement is a **new outcome oracle predeclared here** and separated from D14, not a retroactively reinterpreted old test. D15 native negative for ERASE is an expected **scientific negative**, not technical CI failure. If both pass, revise the conceptual mechanism and preserve observation; never silently modify tests.

Additional gated future experiment: permit an external append-only authenticated registration history `Γ_log`, and compare whether ERASE can regain future D15 through explicit log replay at memory/latency cost; this alters capabilities and must not be attributed to the original Γ_obs.

## Real-world semantic limits and strong priors

Predeclare the current observer `O14` as HTTP response tag, return status of DisableRoute, and revision count; `O15` additionally tests re-enable output from original closure. The symbolic projection `ψ` maps actual original Go HTTP responses to identical labels and route-visibility states. The test is a narrow local **DIP-50 prefix bridge**, not all-context factorization.

Strong classical opponent: **information loss + APR patch overfitting** already predicts possible future extension divergence. Therefore success cannot claim a new mathematical law. The scientific value is an authentic source-level nontrivial difference between two behaviorally matched current repairs under an independently frozen later capability demand, and a potential instrument for testing future strong structural-law competitors. If the two selected treatments are insufficient to discriminate strong H* from classical B, retain `DIP49_IDENTIFICATION_HOLD`.

## Execution contract

- Human preseal → human D14 and D15 test commits → two distinct source commits → read-only original Chi CI.
- Native original Go full module, race `go test -race -count=1 ./middleware`, vet; old P35 O6 exact trace test, separate D14 test; D15 test run separately with RETAIN expected pass / ERASE expected negative.
- No changes to frozen D14/D15 test to force desired outcomes.
- Proof-tier distinction: analytic two-history impossibility under stated no-input restrictions; native source negative control; universal software law still unestablished.
- Source author/committer `WhoSia`, no bot writes.

**Pre-source verdict:** `P36_O3_FROZEN__NO_SOURCE_TREATMENT_YET__DIP49_LAW_PAIR_HOLD__LAW_R2_NOT_AUTHORIZED`.
