# EvoNOMOS Generation VIII LAW-R1-P35-P3 — Frozen Decoder Repair-Family Attack, Native Restic Tests & Strong Prior-Art Rivals

**2026-10-09. Phase verdict:** `P35_P3_NATIVE_FROZEN_REPAIR_PASS__C5_MINIMUM_CLAIM_FALSIFIED__B0PLUS_B2_NOT_DEFEATED__B1_OUT_OF_SUPPORT__LAW_R2_NOT_AUTHORIZED`.

**This phase can close as a bounded counterexample and source-rival comparison. EvoNOMOS P35 overall remains OPEN; no new universal SOLID law is claimed.**

## Original upstream contact

- [Read-only native Restic Actions #37897588100](https://github.com/WhoSia/EvoNOMOS/actions/runs/37897588100) **SUCCESS** with actual `restic/restic@495982232cf1af184eac0a97871ef8161e8708ee` and Go 1.23.12.
- Original P35 P0 Go blob `d15f47c3511c0a1dad1d8cb6793db59a19860066`; new [P35-P3 fixed-reader four-method source](../../tools/p35-p3/c-encoded-four-decoder/backend.go) is a source patch over that exact P0.
- P35-P3 dedicated tests: `go vet`, 3 repeated `go test -race` checks; original P34 public 18-event behavior contract; P35 versioned storage and legacy-prefix collision; Remove/Delete then reuse of the same Handle as legacy data; concurrent read/write snapshot and race; Go-parser-based frozen-reader guard. All pass in pinned native Restic package. **Not** a full original Restic repository integration suite.
- Counterexample mutant `c-encoded-compact`, which moves decoding to the payload store, was run against the same architecture guard and rejected for the expected explicit reason. This is an **expected failed mutant**, not a failed source test.
- Hosted evidence artifact **11600679229**, `g8-law-r1-p35-p3-frozen-decoder-rival-audit`, SHA-256 `4fc9da28ca81a814759f3cd46949ce011ac0a1b22410dc1f02edd5db50ca92a3`. Includes source-hash manifest, native logs, architecture mutant expected-failure log, and quantitative rival audit.
- Workflow [`g8-law-r1-p35-p3-repair-grammar.yml`](../../.github/workflows/g8-law-r1-p35-p3-repair-grammar.yml) is computation-only with `contents: read`. GitHub commit authored/committed by authenticated human `WhoSia`.

## Mechanism, not a cosmetic delegation layer

Same public `restic.Backend` behavior and frozen architecture:
- U has one `map[Handle]record{payload,logicalLength}`.
- C has separately authoritative payload bytes and logical metadata; a distinct read engine performs **its own decode**, with a removal coordinator preserving cross-store consistency. No common vault secretly implements both designs.
- New demand `d_E`: reversible V1 physical encoding of fresh Save outputs; legacy **arbitrary raw bytes** (including a colliding `P35:1:` prefix) must be preserved on Load; Stat/List return logical sizes; Remove/Delete and later legacy Handle reuse must not misclassify payloads.

**New C4 repair construction:** Keep the existing `payloadStore.blobs map[Handle][]byte` and original `payloadStore.get` untouched. Add a lazily allocated `payloadStore.encoded map[Handle]bool`. Four old methods change: `payloadStore.put` (encoded write + marker), `payloadStore.erase` (marker removal), `payloadStore.clear` (marker reset), `readEngine.decode` (trusted marker-aware decode). `newPayloadStore` remains semantically unchanged: nil marker map is initialized lazily, so no constructor edit. `readEngine.decode` remains the independent decoder. The encoded helper functions and one changed type are counted separately.

## Source-edit geometry: two feasible arms and multiple repairs

**Measurement:** Go AST declarations individually formatted before hashing, to prevent accidental `gofmt` alignment from masquerading as method edits. Unified-diff production Go source lines plus the identical `codec.go` addition.

| Actual repair candidate | Modified original Go methods | Added Go lines (incl. codec) | Removed Go lines | Relevant status |
| --- | ---: | ---: | ---: | --- |
| U2 encoding | 2 | 30 | 1 | Original Restic native P35-P2 PASS |
| C5 independent decoder + tagged entry | 5 | 55 | 9 | Original Restic native P35-P2 PASS |
| **C4 lazy marker + independent decoder** | **4** | **56** | **7** | **Original Restic native P35-P3 PASS** |
| Prior C4 compact decoder relocation | 4 | 50 | 7 | Public behavior PASS, frozen C architecture **INADMISSIBLE** |

The older claim that **the best observed frozen C repair changes at least five methods is empirically false**. C4 changes fewer methods than C5 but *more added lines*. These are different cost dimensions, and the observed counts are not developer effort, versioned service lifetime, repair-family minimum, or architecture-wide Pareto rank. The candidate family has not been enumerated exhaustively.

## Strong competitors, measured without rigged information asymmetry

The documented [Go AST symbol auditor](../../tools/p35-p3/source_audit.py) computes these explicit candidate methods under the **same** source-world and demand knowledge, with normalized Go AST diff and fixed P0. Both syntactic baselines contain every observed C4 changed method:

| Baseline | Candidate method set size | Matched actual edits | Precision | Recall | Proper interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| B0, prior broad static vicinity | 12 | 4 | 1/3 | 1 | Conservative syntactic envelope, not a source-change oracle |
| B0+, tighter payload owner + lifecycle | 6 | 4 | 2/3 | 1 | Stronger source-aware ownership envelope |
| B2, Parnas-style side-map ownership/lifecycle obligations | 4 | 4 | 1 | 1 | **Retrospective and conditional** on marker representation; explanatory ability, not preregistered prediction |
| B1, history/co-change | — | — | — | — | **No fair pre-demand training data** for newborn synthetic P35 implementations |

The B2 decomposition is classical **information hiding with evolution obligations**: introduce version-tag writes, preserve distinction on read, and clean tags on both deletion paths. This explains this C4 patch without a new EvoNOMOS law. But the four-element set was constructed after the observed source change and must **never** be scored as a prospective win. A real B2 comparator (Design Rule Spaces/CSDG) was **not** implemented end-to-end, and B1 cannot be pronounced inferior when there is no same-population pre-demand cochange history.

**Original Drive sources already held:** [Parnas (1972)](https://drive.google.com/file/d/1EcQRy3iehx4lUN7uGsZ1BFXU33HggcEQ/view), [Sullivan et al. (2001)](https://drive.google.com/file/d/1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr/view), and [Hong et al. (2024) CoChangeFinder](https://drive.google.com/file/d/1ZL0atP6tINZJW8a3BZ-kzermZ6nhioe6/view). Their established ideas are rivals, not mere supporting decorations.

## Mathematical interpretation and limitation

Let `R_A(d;Q,G,architecture)` denote the admissible repairs for demand d under public behavior Q, modification grammar G and explicit architecture preservation. The earlier observed C5 witness did not identify a minimum; C4 is another member of this set that falsifies any C-lower-bound `>=5` if one was inferred from enumerated witnesses. This is a classical existential counterexample, **not a new pure mathematics theorem**. Changing constraints `G` or moving the decoding owner legitimately changes the admissible set; post-hoc relabeling the new owner is not a fair fixed-architecture comparison.

The fully observed new mechanism is **extra version-mark lifecycle cleanup at independently owned storage boundary** under this particular demand. The traditional B2 information-hiding account already explains why those contacts matter. The P35 source tests certify feasibility and false-lower-bound correction; **they do not identify universal differences between SOLID architectures**, human maintenance effort, global optimization, or predictive advantage.

## Next legitimate scientific contact

P35-P3 can be marked **CLOSED / BOUNDED NEGATIVE AGAINST C>=5 / NATIVE SOURCE PASS**. P35 remains OPEN for a fresh, independently selected real maintenance change and pre-registered **B0+/B1/B2** predictions with equivalent available histories and source context. Seek a new change mechanism or real evolving codebase, not endless redefinition of this synthetic encoding test. Retain the user's long-term scientific ambition and persistence while closing falsified narrow claims. **LAW-R2 NOT_AUTHORIZED.**
