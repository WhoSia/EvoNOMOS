# EvoNOMOS — Three Source-Boundary Designs, Historical Information Preservation, Strong Journal Rival

**2026-11-10 KST · SOURCE-ACTUAL ORIGINAL MODULE v1.21.0 / CONTROLLED APP-OWNED TREATMENTS / NO NEW CONDITIONAL LAW / LAW-R2 HOLD**

## 1. Relevant actual history and deliberate experimental restriction

Previous [original Viper issue #2161 external-source trial](../viper_provenance/01_ORIGINAL_VIPER_PROVENANCE_DECISION_INSUFFICIENCY_RESULT.md) proved that equal final \`GetString\`, \`IsSet\`, \`InConfig\` and \`AllSettings\` may conceal whether a known env variable was actually used. User requested actual extension into competing architectures. This study acts on genuine unmodified \`github.com/spf13/viper@v1.21.0\` source as a pinned third-party Go module, with **three research-owned application architecture treatments**. It does NOT modify upstream Viper sources or implement generic \`SourceOf\`.

[Pre-implementation source-contract document](00_PREDICTION_AND_COMPETING_STRUCTURE_PROTOCOL.md) committed **67ceb345**. A real logical flaw was found BEFORE any treatment source code/testing: its initial worlds flipped the environment flag in opposite directions, yielding different late observations. **Pre-code correction commit e4ee80eb** retains that fact and defines a valid equal-late-observation history pair: H0=0→H1=1 versus H0=1→H1=1, identical current env presence and token value. The correction's timestamp matters; a study that hides such errors is not a reliable research instrument.

## 2. Treatment design and protected old contract

Every app-owned architecture calls the same pinned original Viper \`GetString("service.token")\`, reads YAML \`same-token\`, has \`AutomaticEnv\`, prefix \`APP\`, dot→underscore replacer, and the same optional \`APP_SERVICE_TOKEN\`.
- L / \`Lazy\`: return value only; later \`GuessHistorical\` consults **current** env state. No historical provenance recorded.
- S / \`Snapshot\`: return value and exact known-env presence bit when reading. Its record has a source field; separate current query remains available.
- J / \`Journal\`: return value plus stable lookup ID while app-owned map records read-time bit separately. This is a **strong, equally expressive classic event-logging competitor**; snapshot is NOT uniquely capable of historical reconstruction.

All three produce equal old user-facing values on both original source worlds. The new forensic demand (historical origin for an earlier read) is **RESEARCHER-AUTHORED**, not later issued by an independent user, and was frozen before treatment code and native tests. The external Viper issue #2161 motivates effective provenance *now*, not this delayed historical audit. The second 'live-current-source' goal is also researcher-authored to prevent confusing stale historical and actual present origin.

## 3. Native original library test results

[CI #42743131444 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/42743131444) at project head \`4d9c0b225f722abe03471068676595f2ab6d3b75\`, Go1.23.2 Linux amd64, read-only GitHub Actions, \`go mod tidy/download/verify\`, \`go vet\`, \`go test -count=1\`, \`go test -race\`. The native Go job log reports **five top-level tests PASS**, plus vet/race success. Compared against original Viper code as a dependency, not against a mocked config reader.

| Bounded fact | L value-only | S snapshot | J journal |
|---|---|---|---|
| Old client gets same token | PASS | PASS | PASS |
| H0=0→H1=1 vs H0=1→H1=1 historical source can be differentiated at t1 | **NO** | YES | YES |
| Historical H0=1→H1=0 source still available at t1 | **NO** | YES | YES |
| Live/current source H1 retrievable without treating H0 as current | YES | YES via separate query | YES via separate query |

The Go tests for L PASSED because they assert precisely the predeclared information loss. This should never be misrepresented as L passing the historical customer contract.

**Source-level logical interpretation:** for the corrected two histories, the record stored by L and current observed environment at t1 coincide, yet the historical client target differs. No deterministic function of only that available pair can reconstruct H0 for both. S and J record the differentiating bit at t0 and distinguish the histories. This is exactly classical information-theoretic sufficiency and history/state distinction, not an original theorem. In an operational environment that already records env-change events, L plus that preexisting log may also recover the history; the claimed impossibility is relative to the **declared no-history state**. An arbitrary Viper setting source including flags, overrides or aliases is outside this test.

## 4. Actual small native execution-cost measurements (not labor economics)

The pinned original source was benchmarked inside a single GitHub Actions Linux runner with \`-benchtime=2000x -count=3 -benchmem\`, serial operations, three separately run benchmark functions and same Viper GetString baseline. Raw measurements:

| Go benchmark | ns/op (three runs) | B/op (three runs) | allocs/op |
|---|---|---|---|
| L / Lazy | 830.0, 511.1, 481.2 | 224,224,224 | 10 |
| S / Snapshot | 462.5, 716.4, 525.3 | 224,224,224 | 10 |
| J / Journal | 596.6, 594.9, 477.6 | 277,277,276 | 10 |

The ranges overlap, and the trial is 2000 operations only, in non-randomized benchmark order, on one shared CI worker. Therefore **no credible speed superiority of S over L or vice versa can be inferred**. J allocated roughly 52–53 more amortized bytes/op under the specific growing-map history, but memory footprint depends on map size, lifecycle and GC; not a general long-horizon comparison. None of these benchmarks measure actual change effort, defect risk, total application runtime, or human/AI maintainer actions. Also \`go mod tidy\` was performed in the disposable CI checkout; the project repository was not written by CI.

## 5. Why this is still not an EvoNOMOS new design law

This study is **better than an unverified finite graph** because it uses true Viper code, three actually compiled source-boundary treatments under one old client oracle, a corrected identification witness and an empirical runtime/allocated-byte vector. Yet:
- Future historical task selected/researcher-authored before testing, NOT independent after a genuine live architecture decision.
- The three designs are intentionally unequal in the *information recorded*. That difference makes the new task logically possible/impossible under no-history premises; this does not isolate the economical benefit of an interface, inheritance, OCP or DIP.
- S/J differ in representation, and both are classical ways of recording one bit. No new beyond-classical structural mechanism or predictive modifier was established.
- The artificial binary historical-source label omits real Viper precedence, multi-BindEnv, aliases and arbitrary config. No production bug reduction or real maintainer effort demonstrated.
- A simple economic break-even formula of the form \`capture_cost < P(later audit)*penalty_if_missing\` is just expected value of information with *unmeasured* quantities. Do NOT claim sign reversal based on it.

## 6. Decision forcing research path

**No more Viper equal-value fixtures by default.** The actual next scientific challenge is NOT to implement larger provenance-type taxonomies. It is an original independently maintained program with a real independent requirement and TWO alternative *equally informative* bounded source architectures, preferably comparable by random or crossover assignment to agents/developers. Freeze BEFORE treatment outcomes: same old/new clients, rights to modify, toolchain, information budget, design choice time, robust source-aware classical baselines and a vector of correctness / labor / throughput / defect / cognition. Identify a structural moderator that changes the **recommended action**, not merely a hidden source bit. If no moderator survives strong baselines, record the null result and retire this candidate.

**Result: SOURCE-ACTUAL THREE-TREATMENT NATIVE PASS; HISTORICAL FIBER INFORMATION LOSS VERIFIED; JOURNAL RIVAL TIE; MICROBENCH EXPLORATORY; CONDITIONAL SOURCE DESIGN LAW OPEN; G1–G7 OPEN, PR #13 DRAFT, LAW-R2 HOLD.**
