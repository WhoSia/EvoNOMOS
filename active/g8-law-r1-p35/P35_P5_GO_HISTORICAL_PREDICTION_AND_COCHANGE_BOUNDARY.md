# EvoNOMOS Generation VIII LAW-R1-P35-P5 — Go-Native Historical Prediction, Source Coupling and Non-Necessity

**2026-10-09. Bounded verdict:** `P35_P5_GO_HISTORICAL_SEALED_EVALUATION_PASS__B0_B1_TOP1_TIE__B2_NOT_BETTER__ALL_MODELS_SINGLETON_FALSE_ALERT_100PCT__COCHANGE_NOT_CAUSAL_REQUIREMENT__P35_OPEN__LAW_R2_NOT_AUTHORIZED`.

This is **real public Git history**, not a synthetic change demand and not econometrics. The subject is when software program structure, historical edits and information-hiding boundaries explain **which actual code sites will change together**. Event counts and error rates check predictions; they do not turn source design into an economic optimization model.

## A. Original independent Go software and Go-first code

[go-chi/chi](https://github.com/go-chi/chi) `v5.1.0`, fixed original SHA `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. Three Go production files: `mux.go`, `tree.go`, `context.go`; history split at **2020-01-01T00:00:00Z**. All upstream histories are nonmerge Git commits reachable from the fixed source head; a commit changing at least one triad file is an event. Each changed triad file is a potential seed; its other simultaneously changed triad members are the observed co-edit labels. No claim that these are *necessary* patches or that each seed query is statistically independent.

**Implementation language: Go.** [Go source + unit tests](../../tools/p35-p5/main.go) use `go/parser`, `go/ast`, real `git log`, `git diff-tree`, Go stdlib JSON and SHA-256. Go 1.23.12, `go vet`, `go test` and native Go binary PASS. Python, spreadsheet-based modeling and econometric identification are **not** the engine.

**[Pre-score contract](P35_P5_GO_HISTORICAL_PRE_SCORE_SEAL.md)** documents the exact train/evaluate barrier, information fairness, fixed B2 hypotheses, potential information leakage from aggregate holdout activity scouting, and the stopping rules.

## B. Chronological machine-checkable seal

1. Human `WhoSia` [commit **44aa07b**](https://github.com/WhoSia/EvoNOMOS/commit/44aa07be5a4ac1285321f7f118385fb44ea886aa) fixes **all three predictors, training/test cutoff, source universe, scoring logic and protocol before evaluation**.
2. Read-only **training-only [Actions #37902114102](https://github.com/WhoSia/EvoNOMOS/actions/runs/37902114102) SUCCESS**; source from the original pre-cutoff Go commit `7fb34524d9ab7c9e3dd0f9c17c1ec808d8c77f33`. Exactly **121 qualifying training commits**, **43 multi-file**. Training mode does not compute holdout cochange labels. Artifact **11603105240** SHA256 `64abe4f1fb69107cba20bf4e91e9258c1c892b937766686c28df833ddca98842`.
3. Human `WhoSia` [commit **d35a50b**](https://github.com/WhoSia/EvoNOMOS/commit/d35a50bd8437d89bbf554327fd901666b1e19ae4) freezes the [exact deterministic JSON predictions](../../tools/p35-p5/seals/predictions-2020.json) and updates the Go-first README. Training `model.json` SHA256 **`3c48c40a8ba8bcdacaa09d44bdfc0be34e4258b4428d44a969f105296de501c6`**.
4. Separate, human-committed [read-only evaluator](../../.github/workflows/g8-law-r1-p35-p5-evaluate.yml) run **[Actions #37902487463](https://github.com/WhoSia/EvoNOMOS/actions/runs/37902487463) SUCCESS**. **Before reading any heldout cochange event**, it recomputes the entire old training JSON and asserts byte-for-byte equality with the committed seal; mismatch is fatal. Result artifact **11602978360** SHA256 `a54682672add462daaf4d115bd966b84737ed3d0e799cb6dc41bdff093d4be56`.
5. An *additional* Go AST review **after** heldout scoring and expressly excluded from predictors is [source audit #37902868379](https://github.com/WhoSia/EvoNOMOS/actions/runs/37902868379) SUCCESS, artifact **11603615549** SHA256 `cc129f5591a22861663a55420dc04210a00a406aadde4f94ac827a269d2cdba3`. It compares syntax after Go parser without comments, not semantic necessity.

**Selection caution:** The triad and cutoff were picked after reviewing raw path-activity counts, including some holdout totals and commit titles. Thus no claim of a perfectly untouched dataset; the critical protection is that **joint labels and heldout scores were unavailable to the committed predictor/model until seal verification**. This is a bounded historical replay, **not independently randomized or strict blind model selection**.

## C. Pre-registered B0+/B1/B2 predictions

| Known seed file | B0+ Go AST lexical cross-file symbols | B1 pre-2020 cochange | B2 predeclared design responsibility |
| --- | --- | --- | --- |
| `mux.go` | `tree.go` | `tree.go` | `tree.go` |
| `tree.go` | `mux.go` | `mux.go` | **`context.go`** |
| `context.go` | `mux.go` | `mux.go` | `mux.go` |

Original B1 train counts: `mux.go` 83 seed events, max pair `tree.go` 34 (40.96%); `tree.go` 64 seed events, max pair `mux.go` 34 (53.13%); `context.go` 33 seed events, max pair `mux.go` 22 (66.67%). B1 was supposed to abstain when fewer than 5 seed events or top conditional rate below 10%; **none** of the three meets that abstention condition. This abstention rule later turns out far too permissive for single-file negative events.

B0+ is only real-Go AST declared-identifier cross-reference counting at the **training** source revision, **not** go/types-resolved call/data impact or a full Control/Design Structure dependency graph. B2's explicit Parnas-style mapping is a genuine qualitative rival but **not** a full Design Rule Spaces/CSDG implementation. No strong conventional model is defeated by relabeling this small baseline family as exhaustive prior art.

## D. Heldout result, including adverse outcomes

The 2020–2024 fixed-head historical window contains **40 distinct qualifying commits**, **6 commits editing two or more triad files**, and **47 seed-based queries**, of which **13** have at least one additional changed target and **34** are singleton negative opportunities. The B2 map disagrees with B0+/B1 on **12** seed queries. Because multi-file commits give more than one seed query, treat per-query metrics as **descriptive**, not 47 independent experiments.

| Model | Top-1 hits on 13 positive seed queries | Alerts on 34 singleton seeds | Abstentions |
| --- | ---: | ---: | ---: |
| **B0+ actual Go AST lexical** | **9 / 13** | **34 / 34** | 0 |
| **B1 actual pre-2020 Git cochange** | **9 / 13** | **34 / 34** | 0 |
| **B2 explicit information-hiding map** | **8 / 13** | **34 / 34** | 0 |

The 9/13 hits apply **only conditional on a paired change already existing**. All three methods issue unnecessary top-1 companion suggestions on **every singleton case**. It would be misleading to claim ~69% end-to-end accuracy by omitting false alerts. The answer to 'which file next?' is distinct from the gate 'does *any* other file need changing?'

Training multi-file incidence was **43/121**, heldout **6/40**. This is an observed change in sample composition, not a causal econometric effect, and it could reflect development regime, source composition, commit practices or selection.

**Verdict:** B0+ and B1 are observationally indistinguishable in this three-file top-1 experiment, B2 gets one fewer hit. No statistical winner, no universal SOLID cost ranking, and no novel predictive theory. The major falsification is the **ability to infer necessary coupling from a ranking alone**.

## E. Source-backed mechanisms opened ONLY after scoring

[Full Go AST audit](../../tools/p35-p5/sourceaudit/main.go) on the heldout source: all **six** multi-triad commits change syntax (AST shape) in at least two target Go files. **AST co-edit is stronger than path-only co-edit but still does not prove required joint behavior.** Concrete original commits:

- [**4b14b832 (2023-07-13)**](https://github.com/go-chi/chi/commit/4b14b832d53cef6c77fdcf852876a34f46bc84a2): HTTP **405 Allow header** feature changes `tree.go` to gather supported methods, `context.go` to carry that list, `mux.go` to emit it. A strong, source-observable **cross-boundary dataflow/contract requirement**: the feature's data passes through three responsibilities. Triple edits mean B0, B1 and B2 can all hit a companion, so this one event does **not** by itself distinguish them.
- [**8391bdb4 (2020-11-29)**](https://github.com/go-chi/chi/commit/8391bdb4da71e4bf0093b175c574cd42cb9e70b4) and [**721b475b (2021-02-10)**](https://github.com/go-chi/chi/commit/721b475b562335b524b47b821458b4020c3e90cc): optimization that replaces `context.WithValue` with a `directContext` representation across `context.go`/`mux.go`, **then reverts** that choice. This is real lifecycle reversal tied to representation/contract decisions, not one scalar economic cost.
- [**fb48a476 (2021-02-28)**](https://github.com/go-chi/chi/commit/fb48a47641af106c7eae2f09864e7fecd54237bf): memory/struct layout adjustments touch `tree.go` and `context.go`, though they do **not** establish a new public route contract. [**bed8648a (2021-03-07)**](https://github.com/go-chi/chi/commit/bed8648a22121634da5be6019e9223b9630a53bb) touches `mux.go`/`tree.go` and other files in another layout optimization. Different reasons produce the same cochange label.
- [**b612eb4a (2020-02-20)**](https://github.com/go-chi/chi/commit/b612eb4a0679ba65000dd57947496db7ecadb35f), titled 'Comments', actually **also deletes an unused method** from `tree.go`, so even an innocuous message label cannot safely replace AST inspection.
- [**ef31c0bf (2024-05-07)**](https://github.com/go-chi/chi/commit/ef31c0bff3f8061e6fba7085691e4970a3d1b7da) reduces only `context.go` struct size, and [**9dd8b4a7 (2023-12-20)**](https://github.com/go-chi/chi/commit/9dd8b4a7b5930c86ac2ecfdb55467112cc223518) adjusts context reuse in `context.go` alone. Connection to `mux.go` does **not** force a companion change for every local context edit.

**This is the core next research problem**: given a *specified change operator* and source contract, predict whether a potential structural connection becomes an **obligation to edit**, a **safe no-op**, or a **migration of abstraction ownership**. This is about operational software semantics and information hiding, not finance, ad hoc cost weights or another ornamental universal structure theorem. The next Go-native baseline should admit and score **NONE** as a real outcome, with source-change features frozen before new historical evaluation.

## F. Status and constraints

`P35-P5 HISTORICAL GO PREDICTION AND POST-SCORE SOURCE AUDIT CLOSED, BOUNDED`. The evidence certifies reproducible real-history conditional rankings, frozen-model readback and a false-alert failure mode. **P35 parent OPEN** and **LAW-R2 NOT_AUTHORIZED**. The next experiment must separate required co-edit from coincident historical co-edit and compare genuine B1/AST/Parnas/CSDG rivals on matched information. Keep persistence on the large software-science question without dragging it into econometric pricing or overstating novelty.
