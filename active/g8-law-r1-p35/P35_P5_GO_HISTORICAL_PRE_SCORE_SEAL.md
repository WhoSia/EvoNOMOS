# EvoNOMOS G8 LAW-R1-P35-P5 — Go-Native Historical Change Prediction, Pre-Score Seal

**Status: P35-P5 TRAIN-ONLY OPEN. No holdout joint-change labels have been examined.** Scientific parent P35 OPEN; LAW-R2 NOT_AUTHORIZED.

## Priority: Go, software structure, and explanatory mechanisms

**Go is the main experimental language and the native original-source substrate.** Execute `go/ast`, Go history adapters, native Go tests, Go build and independent reproducibility audits first. Rust remains a justified option for throughput on tasks needing it; Python is ancillary, not a default simulation language. **This is a software architecture/change-prediction study, NOT an econometrics or valuation project.** The main object is coupling under real source evolution: AST symbol contacts, historical co-edits and information-hiding/contract responsibilities. Counts, recall and false alerts are evidence audits; dollars, discounted cash flows and scalar SOLID scores are **not** the goal.

## Original source and frozen cohort

Original independently developed **go-chi/chi**, native Go, `v5.1.0` commit `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. Fixed targets: `mux.go`, `tree.go`, `context.go` (root package). Cutoff **2020-01-01T00:00:00Z**. Training: nonmerge Git commits before cutoff. Holdout: nonmerge Git commits from cutoff to 2024-06-28T14:29:28Z, never commits after the pinned original upstream ref. Unit is a **Git commit changing any fixed target file**. Every changed target within the commit is a seed; correct other-target completions are other files from the same commit. A positive has 2+ target files in the same commit. Includes one-file events as negative prediction opportunities. No per-test newly invented source repair.

**Selection bias:** candidates were selected after public per-path activity scouting, including aggregate holdout counts and a few postcutoff commit titles. Thus this is **NOT a pristine untouched holdout**. No postcutoff joint cochange labels were queried before the model seal. Avoid strict blind claims. Cutoff 2020 selected to prevent extremely sparse 2022–2024 `tree.go` support; do not tune afterward.

## Precommitted rival algorithms

- **B0+ AST static:** inspect exact *training-cutoff* Go source. For each pair of files, count identifiers in either file that match package-level declarations from the other; score symmetric pair sum. Top-1 competing file, lexical tie-break. This is a Go-native syntactic impact model, **not full go/types, SSA, source-aware CSDG or DRSpaces**. That stronger baseline remains undefeated.
- **B1 historical cochange:** in training nonmerge real Git commits, count conditional pair cochange frequency `n(seed,target)/n(seed)`. Predict top 1 candidate, lexical tie break; abstain if seed observed fewer than **5** times or top pair empirical frequency below **0.10**. The same seed can have multiple valid completions; no artificial forced winner when abstaining.
- **B2 classical information-hiding role judgment:** frozen, simple domain mapping: `mux.go→tree.go` (routing dispatch→matcher), `tree.go→context.go` (match process→request-state contact), `context.go→mux.go` (request routing state→dispatch). This is an **explicit qualitative Parnas-style competitor, not full Design Rule Spaces/CSDG**; it may be wrong and is not marketed as an implementation of those models.
- **EvoNOMOS H:** no special fourth model is promoted. First establish whether actually different predeclared rivals disagree on historical changed files. A structural law must explain **why** they differ and predict independently unseen maintenance events better than fair prior art, not retrospectively rebrand file cochanges.

## Firewall: train receipt before scoring

1. Human-authored commit the entire Go predictor, cohort, cutoff, B2 mapping, scoring and this protocol. **Train-only CI must not compute or print any holdout joint-change truth.**
2. Read original Git history only before 2020, emit a deterministic JSON **sealed model** with B0, B1, B2 top-1 predictions and training support; commit the byte-identical JSON to EvoNOMOS by authenticated `WhoSia`, before launching evaluation.
3. A separate evaluation CI must recompute the training model from the same pinned original source and demand **exact JSON equality** with the committed seal *before* reading holdout cochange labels. Only then compute the heldout scoreboard.
4. Evaluate top-1 hits on positive cochange queries, false alerts on singleton commits, abstentions, class imbalance and all-model disagreement. No predictive winner if no positive holdout events or unresolved support. Do not conflate edits in a commit with a necessary edit for a user demand. Review actual heldout patches *after scoring* only for mechanistic case studies.
5. Preserve original commits, code SHA, exact Go version, train/holdout counts and complete Go-generated evidence JSON in read-only Actions artifact. No GitHub bot author/committer, no CI pushes.

**Known limitations:** commit != isolated causal change, training cutoff source may differ from evaluated later structure, AST lexical overlap is not symbol resolution, historical cochange is not necessarily required coupling, merge commits excluded, triad intentionally narrow and selected with some metadata preview. No econometric effect estimation or general SOLID law from one cohort.

**Stop condition:** Once the sealed train model is frozen, run the heldout evaluation once and record positive and negative outcomes. If no disagreement or no positive signal, state nonidentifiability; transition to another source region selected before outcome instead of trying new scores until preferred conclusions appear.
