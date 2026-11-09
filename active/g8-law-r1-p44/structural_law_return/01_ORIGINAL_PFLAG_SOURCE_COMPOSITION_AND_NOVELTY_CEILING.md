# EvoNOMOS P44 — Structural Law Return, Independent Pflag Original-Source Replication and Research Judgment

**2026-11-09 · RESULT: source-backed composition obstruction verified; classical exact explanation survives; ORIGINAL RESEARCH LAW HOLD.**

## Direct source and temporal evidence
This study is a deliberate return to the EvoNOMOS founding target after F33/F34 repeated weaker toy examples and go-chi sources previously explored in P35/P36/P40/P42. P40-P4 had already shown on original go-chi source that two individually legal owner contributions may fail when composed over the same global namespace, despite identical local SOLID*-like views. This is a replication to an independent non-router framework, **not a new theorem**.

Repository `spf13/pflag`, original tag `v1.0.5` commit `2e9d26c8c37aae03e3f9d4e90b7116f5accb7cab`; external dependency unchanged. Original `flag.go` reveals two different composition operators:

- `FlagSet.AddFlag` panics for duplicate normalized flag names.
- `FlagSet.AddFlagSet` checks `Lookup` and **skips** already-present names silently.

The source behavior was read **before** the [prediction preseal](00_PFLAG_OWNER_COMPOSITION_PREEXECUTION_CONTRACT.md) committed as `76b73f8f9c3d0499164230414529e9aea5ac6f80`; therefore this is **SOURCE-INFORMED confirmation**, not independent blinded future-demand prediction.

## Source-native Go experiment
[Reproducible app-owned source and tests](pflag_owner_composition/) build with Go 1.23.2 and real `github.com/spf13/pflag v1.0.5`, with original Go module archive hash recorded in go.sum. Two app-owned plugin owners A and B each define independently valid old fields `tenant-a` and `tenant-b`. A new source-stage demand independently adds owner-local `channel` fields, with joint goal A.channel=`canary`, B.channel=`stable`. Both local owner flag sets separately parse successfully.

| Architecture / operator | Old Q0 | Independent owner-local new D1 | Joint D1 under this operator | Source mechanism |
|---|---|---|---|---|
| Shared `AddFlagSet` merge | PASS | PASS | FAIL silently | normalized duplicate B skipped |
| Explicit `AddFlag` registration | PASS | PASS | FAIL loudly | original source panic |
| Preflight checked merge | PASS | PASS | ABSTAIN / REFUSE | classical normalized-name collision scan |
| App-prefixed owner flags | PASS | PASS | PASS | distinct `a-channel` and `b-channel` |
| Independently scoped flagsets | PASS | PASS | PASS | no namespace composition needed |

The strong classical normalized-name scanner detects the same `channel` overlap. That rival obtains the same full namespace/source facts as the new test. Thus the effect is **not a unique analytical discovery**. In particular, the preflight checked merge is a refusal, not a constructive customer repair; separate namespaces change the public argument grammar and must not be counted as a free no-client-change rewrite. The isolated setup needs an app-owned dispatcher to preserve shared-CLI semantics; its test demonstrates two independently satisfiable local clients, not an identical global CLI user interface. These distinctions are material.

First [Go CI #42572660124](https://github.com/WhoSia/EvoNOMOS/actions/runs/42572660124) **SUCCESS**, exactly ten top-level Go tests, `go vet`, `go test -race` pass. Source `go.sum` then checked into repository; read-only dependency verification CI [#42572831334](https://github.com/WhoSia/EvoNOMOS/actions/runs/42572831334) executed at commit `467e81150434ea6610ad92e1a312aa1eefc574d7`. Check actual result separately; do not infer success from this note. No upstream source edit rights claimed, no end-to-end application CLI compatibility across all clients, no human patch-time metric, no outside future issue prediction.

## Formal interpretation: familiar math, source-grounded counterexample
Let `S_A,S_B` be independently valid owner flag registrations, and `\u2297` denote a specified merge operator. Then `Valid(S_A) \u2227 Valid(S_B)` does not imply `Valid(S_A \u2297 S_B)` for a joint contract requiring both owner-local channel values. Local SOLID*-style signatures omitting normalized global key equality cannot predict joint behavior. This was established already within P40's original-Chi source subclass, so **no nontrivial generalization theorem, new structure invariant or mathematical priority claim** follows here.

More specifically, two original source composition operators yield distinct failure modes from the same exact collision. `AddFlagSet` gives apparently successful construction but loses a customer capability; `AddFlag` refuses via panic. This is relevant to **safe-by-construction evidence grading**, but known name uniqueness and conflict detection fully explain it.

## Comparison with earlier source results (mandatory novelty collision)
- **P35-P4/P4B:** original go-chi two-demand independent/shared source changes with bounded future change-cost direction change; strongest information-hiding rival not defeated. More causally informative than this simple collision.
- **P36-O9/O10/O11:** naturally evolved go-chi vs Gorilla semantic contract reversals, plus same-Q integrated lifecycle benchmark and tested changes; classical routing priority and amortized costs explain.
- **P40-P3/P4:** Go interface enlargement, owner-source permissions, local/global composition and typed SOLID* strict local reduct; real Go and original Chi. Direct predecessor already demonstrates this impossibility of locally deciding global gluing.
- **P42-P13-R5:** original maintained Chi 1,215 registration paths and 384 composite goal costs; exact bounded option-loss frontier, classic weighted LTS tied, grammar-relative infinity.

### Research decision
This pflag replication has **ecological diversity / different silent-failure morphology**, but no compelling extra law-discovery value. **DO NOT repeat it in another package.** Retire repeated global namespace-collision experiments as a mainline discovery tactic. The objective remains identifying an independently predictive conditional source-architecture advantage that survives the strongest source-aware classical baseline on real future demands with old-client conformance, owner authorization and multiobjective costs.

Next actual discriminating work should be in a **different source mechanism** than simple normalized-key collision, and the design must name (before source execution) a structural prediction that static names, classic effect/dependency analysis and incremental design economics would *not* already predict. If a competitor has full explanatory coverage, classify a valid research negative and choose another candidate. Avoid new general formalism, theorem naming, synthetic toy extensions, and generation promotion by continuity.

**G1–G7 OPEN. C5 NOT ESTABLISHED. PR #13 DRAFT. LAW-R2 HOLD.**
