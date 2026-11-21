# F20 unit C — machine-checkable historical-evidence claim gate

Dated 2026-11-05. This is a narrow research-operations tool, not a new Go program verification theorem. It follows:
1. a metadata-only A cohort (11 separate research commits, parent/post SHA selected from path history before patch viewing);
2. a B original code-diff and native CI cohort (posthoc oracles, actual external parent/post source trees and original native Go test logs);
3. the important Gin initial non-discriminator discovered by executing actual source rather than relying on issue titles.

## Why a typed evidence model is necessary

A clean historical before/after reproduction can look like a successful future prediction if the provenance clock is erased. Here the issue titles and code diffs were public before custom oracle tests were written; for each of the three selected cases `SubjectDisclosedBeforeOracle=true`. The strongest valid grade is C3 HISTORICAL ORIGINAL REPLAY, not C5 prospective prediction. `Grade` requires all future seals and a non-disclosed demand; the current cases cannot satisfy it, even if an adversarial caller supplies an impressive but fabricated future prediction token.

`OriginalCase.Validate` enforces full-length commit identifiers, distinct parent/post, original job receipt, UTC timestamps, distinct observed outputs and typed observer scope. It does not itself cryptographically query GitHub or prove the claimed logs, which were separately read in the actual GitHub tool.

## Three original receipt rows

- chi: [original GitHub job 127137439627](https://github.com/WhoSia/EvoNOMOS/actions/runs/41995425112), parent `/{id}`, post `/api/groups/v2/{id}`, `Mux.Find` exported; **one input** only, NOT full public API equivalence.
- httprouter: original job 127137439769, parent GET, OPTIONS vs post GET when HandleOPTIONS=false; direct `Router.allowed` unexported helper, so NOT an independently verified HTTP wire `Allow` header contract.
- Gin: original job 127137439315, parent runtime bounds-error vs post descriptive panic, injected `node.insertChild("*all")` internal helper; NOT a supported end-user Gin router path contract.

`CanSupport` accepts exactly tested client input as evidence and rejects claims to ALL exported public API or ALL client contexts for every case. This makes explicit an observability deficit central to P44's G4/G5 gate.

## Ethical methodological boundary

- These code-derived observations are retrospective diagnostics based on already known upstream fixes. Matching them is **not** novel causal inference, prospective cost prediction, or a proof of all safe future edits.
- Our test harness builds upstream versions on GitHub Actions only. Actual edit rights in the upstream canonical repositories are NOT granted by source-code visibility or open-source licensing.
- A GitHub commit SHA identifies a revision; it does not by itself authenticate complete build dependencies, protected customer coverage, maintainers' effort or future demand timing.
- The evidence model itself is a manually curated receipt table; the typed Go tests protect against accidental misclassification, not against an intentionally falsified tool output.
- Preserve failed initial Gin oracle (original test not distinguishing parent/post) and later successful internal negative-index boundary; never silently relabel this as a user-facing panic guarantee.

## What should be falsified next

The really difficult P44 claim asks if structural facts in a maintained program predict viable safe *future* repair in an unknown later demand. Unit A–C do not prove that. A candidate F21 would need a sealed pre-reveal issue stream or an actually new independent task unknown at inference time, matched source-aware classical rivals, customer contract oracle and rights. The user requested BFS re-entry, so resist continuing with incrementally larger toy patches solely to inflate F numbers.

Original evidence-gate CI must be checked and linked separately before claiming its tests PASS. F20 historical source-run evidence resides in GitHub original [run #41995425112](https://github.com/WhoSia/EvoNOMOS/actions/runs/41995425112), whose three independent jobs all SUCCESS.
