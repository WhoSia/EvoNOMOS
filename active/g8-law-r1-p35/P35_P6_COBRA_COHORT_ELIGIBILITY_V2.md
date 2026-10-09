# P35-P6 — Cohort Eligibility Repair v2: Frozen Train-Source Existence

**2026-10-09; new v2 protocol addendum BEFORE ANY P6 train model was computed or heldout joint-file truth opened.** The [original P6 preregistration](P35_P6_COBRA_OPERATOR_NONE_PREHISTORY_SEAL.md) is historically preserved, not rewritten. This eligibility repair supersedes **only the triad and corresponding B2 owner mapping** in that v1 preseal.

## Exact observed P6-v1 technical failure

[Read-only train CI #37904355177](https://github.com/WhoSia/EvoNOMOS/actions/runs/37904355177) stopped before producing a sealed model. Frozen pre-cutoff Go source SHA **`a4ab3fa09e3d6c4ac3fb7deece97a910957305ab`** (2020-12-31 history revision) does **not contain** `completions.go`. `git show a4ab3...:completions.go` failed with path-not-in-tree during `staticGraph()`. No B1 training/model output and **no P6 heldout joint-change labels** existed at this point. Treat v1 as `TECHNICAL_ELIGIBILITY_HOLD`, never a negative performance observation.

The pre-cutoff original Git blob existence audit (not future cochange history) confirmed: `command.go`, `args.go`, `cobra.go` **all exist** at revision `a4ab3...`. This is an explicit source availability criterion: each candidate predictor file must have a real, byte-identifiable pre-cutoff AST. No imaginary empty stub or future-Go-source backfill.

## V2 frozen eligible cohort and models

- Original public upstream remains **`spf13/cobra@e94f6d0dd9a5e5738dca6bce03c4b1207ffbc0ec`** (v1.8.1), language **Go**.
- Training cutoff stays **2021-01-01T00:00:00Z**; evaluation through tag `2024-06-01T10:31:12Z`.
- Triad v2 exactly: `command.go` (dispatch/command), `args.go` (argument validation), `cobra.go` (root command helper and CLI globals). Same original Go package but different responsibility.
- B0+ and B1 algorithms **unchanged**. B2 predeclared at this point: `command.go→args.go`, `args.go→command.go`, `cobra.go→command.go` on `TYPE_SHAPE` only, else `NONE`. This role map is an openly simplified qualitative rival.
- Operators, `NONE`, `ABSTAIN`, train minimum 5, B1 incidence threshold 0.5, score and fair input rules are **byte-for-byte unchanged** from v1's executable Go algorithm except the triad/B2 literal names.
- V1 failure log, v1 commit and CI stay in history. No P6 training outcome was used to choose new files. **Caveat:** checking cutoff file existence after technical failure is a researcher-mediated eligibility decision; do not claim randomized project/file selection.

**Gate:** human `WhoSia` authors this v2 preseal and Go literal correction before rerunning training-only. Train must not read heldout cochange data; frozen human commit must precede heldout scorer.
