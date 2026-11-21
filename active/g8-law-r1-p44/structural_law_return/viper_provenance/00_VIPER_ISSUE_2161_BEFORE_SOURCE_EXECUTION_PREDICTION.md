# Decision-information field test: independent Viper issue #2161 — pre-execution seal

**2026-11-10 KST. Original public requirement read, NOT implementation or solution.**

## Independent external demand and original source anchor
[spf13/viper issue #2161](https://github.com/spf13/viper/issues/2161), filed by `kaelnn` on 2026-10-12, still open on readback, requests effective configuration-value provenance including actual env variable name (env prefix, replacement, aliases, explicit binding, priority). This issue is not authored by EvoNOMOS and is **not** a randomly selected project sample. Issue text was inspected before choosing this experiment; the frozen expectation is therefore requirements-informed, not a blind task-selection claim. No pull-request solution or implementation diff was consulted in this work before freeze.

Source base: authentic external repository `spf13/viper` exact v1.21.0 annotated-tag COMMIT `394040caccbdf5821fa6839386a35f0fb1b1ee9e` (tag object `9d332ad291ae43150db75ef817217898eb14149c`), released 2025-09-08, before issue date. Must assert this actual Git checkout in read-only hosted Go CI.

## Paired source-worlds and static decision state
Two app-owned configurations, both read identical YAML `service.token: same-token` and use `AutomaticEnv`, `SetEnvPrefix("APP")`, `SetEnvKeyReplacer(strings.NewReplacer(".", "_"))` with same getter key `service.token`.
- W0: APP_SERVICE_TOKEN absent, effective value comes from YAML.
- W1: APP_SERVICE_TOKEN present with exactly `same-token`, so effective value comes from environment; value intentionally matches file.

Expected *public* source-independent projection `z_{{Get,IsSet,InConfig,AllSettings}}` to be identical between W0 and W1. `IsSet` and `InConfig` should be true in both worlds, and `AllSettings` map identical. If any differs, mark falsification rather than silently changing the projection.
Expected oracle provenance labels: W0=file-managed, W1=external-env-managed, obtained from **research-controlled setup facts**, not claimed upstream exposed `SourceOf`.

## Action/decision and mathematical falsifier
Actions: F=local refresh/manage token; E=respect externally owned token, never refresh. For a narrow declared use-case, correct action is F in W0 and E in W1. Binary loss J=0 if chosen correctly, J=1 otherwise. If public projection z is identical, no deterministic value-only policy can achieve worst-case zero regret: common optimal action intersection empty. A source-aware classic comparator given the actual env key can inspect `os.LookupEnv("APP_SERVICE_TOKEN")` and choose exactly, 0 regret on this restricted two-world set. Thus **do not claim EvoNOMOS defeats classical source-aware inspection or solves full issue**. Prefix/aliases and multiple explicit bindings are not covered; public `SourceOf` is NOT implemented.

Two candidate architectural policies in same user-owned application:
- V: value-only action policy, same action for every world with identical z. It must miss one world, as proved independently of source implementation.
- O: app-owned explicit provenance adapter for this bounded known variable, supplied with the actual effective environment variable name, distinguishing the worlds; should succeed both. This adds an observable; it is not a free or generic solution.
Add negative control for W1 with different env value so value projection becomes distinguishable; the impossibility pertains to equal-value cases, not all configurations.

## Execution gate
Identical actual original source checkout + app test file, no upstream source edits; Go native original `go test` and `go vet` (race if feasible), original commit asserted; interpret 2-world tests and classical rival. Record failures and any diffs in source or toolchain. Do not claim a matched architecture intervention or measured human repair cost. This is an empirical grounding test of the **decisional sufficiency** mechanism, a prerequisite rather than a new source architectural law.

**Falsifier:** W0/W1 projection differs; original source resolves priority differently; env-aware conventional rival fails despite declared environment-key knowledge; or test demands are not executable without changing assumptions. In those cases, explicitly report and revise the hypothesis rather than promote.

P37-MATH-K and 2026-11-10 multi-role audit are mathematical predecessors. No new pure theorem, no C5, no LAW-R2 promotion.
