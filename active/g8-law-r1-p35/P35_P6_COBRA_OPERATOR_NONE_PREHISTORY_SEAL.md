# EvoNOMOS G8 LAW-R1-P35-P6 — Go Source-Operator Conditional NONE Prediction: Independent Historical Cohort Preseal

**2026-10-09 · status: PROTOCOL SEALED BEFORE ANY P6 COBRA HISTORY LABEL QUERY, Go-native training, source mutation or heldout evaluation.** Parent P35 remains OPEN; LAW-R2 NOT_AUTHORIZED.

## Scientific target, not econometrics
A static dependency or earlier co-edit tells us that a companion file *could* matter. The operational task is to predict whether a **specified source edit operator** activates a need to modify another source file, vs `NONE`: no observed companion edit. This is a study of Go declarations, contracts, information hiding, and changing module obligations. No dollar values, discounting, causal econometric claims, scalar SOLID rankings or universal structure laws.

**Important truth tier:** Historical co-edits are an OBSERVED proxy, not necessary edits under counterfactual admissible repairs. To claim genuine necessity requires separate public-contract tests and negative-file-ablation interventions. P6-A is a historical proxy classifier; P6-B will follow with actual Go original-source intervention and stronger controls.

## New upstream, deliberately independent of Chi & Restic

Actual public [spf13/cobra](https://github.com/spf13/cobra), `v1.8.1`, exact Go production source SHA `e94f6d0dd9a5e5738dca6bce03c4b1207ffbc0ec` (2024-06-01). Fixed production Go triad selected by roles from baseline source listing, *not* observed per-path Go history outcomes: `command.go` (dispatch/routing), `completions.go` (completion), `args.go` (validation). Training nonmerge original Git commits strictly before `2021-01-01T00:00:00Z`; heldout originals from that cutoff through pinned `2024-06-01T10:31:12Z`. Full-history clone only. Merge commits excluded. Each commit touching at least one triad file is an event. Each changed source file provides a **given seed patch** (`commit^:seed` → `commit:seed`); the target is whether any other triad file changes in that same commit and, if so, which one. This is a partially observed source-patch task, not prediction from commit title or future source. Do not read target-file diffs until after freezing predictions and verifying the model seal.

## Frozen deterministic Go operator extraction

Parse only the presented seed file *before and after the commit* with `go/parser`/`go/ast` excluding comments. Normalize each existing function declaration and type declaration with `go/format`. Labels:
1. `TYPE_SHAPE` when any type spec's normalized AST changes/is added/removed (struct fields, interface or aliases; this also covers noncontract type layout).
2. `FUNCTION_ONLY` when at least one function declaration changes and no type spec changes (signatures and bodies combined; explicitly coarse).
3. `NO_DECL_CHANGE` otherwise (comments, import-only, package-level values etc. can still matter).

Priority TYPE_SHAPE > FUNCTION_ONLY > NO_DECL_CHANGE. **This is not a semantic Go compiler oracle** and does not show whether a public contract changed or whether a companion edit was necessary.

## Fair registered competitor models on matched information

For each known seed, all methods receive the **same seed patch-derived operator class**, original Go source as of training cutoff and pre-2021 nonmerge training history, but **never heldout other-file changes**.

- **B0+ operator/AST:** rank the companion by pre-2021 Go AST lexical cross-file declaration links (symmetric scoring and lexical tie-break), predict that file on `TYPE_SHAPE` iff score positive; otherwise **NONE**. No history coedit used for selection.
- **B1 historical operator-conditional:** on training commits calculate per `seed×operator` multi-target incidence and pair frequencies. With at least **5** training samples and conditional multi-rate ≥ **0.5**, return most frequent other changed triad member (lexical tie-break); with at least five and smaller rate, return **NONE**; with fewer than five, **ABSTAIN**, never quietly convert uncertainty into NONE. Also compute seed-only historical baseline analog using ≥5 support and same 0.5 threshold.
- **B2 classical conditional responsibilities:** on `TYPE_SHAPE` predict `command.go→completions.go`, `completions.go→command.go`, `args.go→command.go`; otherwise **NONE**. This is a predeclared simplified Parnas role rule, NOT real full DRSpaces / CSDG. Strong B2 remains undefeated.
- **Control:** `ALWAYS_NONE`, to disclose class imbalance and cheap singleton accuracy; never declare it an architectural win.
- No EvoNOMOS proprietary H is credited with better performance by this design.

## Pre-registered scoring

First train-only CI creates native Go deterministic JSON with source revision, counts and exact B0/B1/B2 outputs by seed×operator. It SHALL NOT compute/post ANY heldout cochange truth. A human WhoSia commit freezes *byte-for-byte* those predictions. Only a distinct read-only CI may regenerate and verify the seal and then read heldout labels. Report event-level and per-seed counts separately, positive-companion recall, singleton specificity, unnecessary alert count, B1 abstentions, and any disagreement. Balanced accuracy is diagnostic, not an economic objective. In events with >2 triad files, multiple seed queries share one event; do not treat as independent replicates.

**Negative results count.** If no TYPE_SHAPE seeds or insufficient support, mark `IDENTIFIABILITY_HOLD`, not a preferred model win. If all models are degenerate, move to a fresh independently prechosen Go cohort. Do not optimize gates using heldout cases. Native Go `go test` and `go vet`, read-only GitHub Actions, immutable original source and `BOT_CONTRIBUTION_ZERO`.

## Leakage and scope

This cohort was selected because Cobra is a mature Go CLI project and its file roles are suitable; the v1.8.1 file listing and tag metadata were inspected, **but no historical coedit labels for these three Cobra files were queried before this protocol**. Strong independence is still limited by one authoring team/triad, nonmerge filtering and fact that commit bookkeeping is not causal necessity. The operator extracted from historical completed seed patch makes this a *conditional patch-completion* task, not anticipation of a natural-language demand before any patch exists.
