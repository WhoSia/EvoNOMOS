# EvoNOMOS G8 LAW-R1-P35-P4/P4B — An Independent Real-Repository Two-Demand Change-Cost Tournament

**Date:** 2026-10-09. **Official current status:** `P35_P4_AND_P4B_BOUNDED_NATIVE_PASS__PROSPECTIVE_INCREMENTAL_EDIT_SIGN_REVERSAL__B0PLUS_B2_NOT_DEFEATED__B1_HISTORY_UNDER_SUPPORTED__P35_OVERALL_OPEN__LAW_R2_NOT_AUTHORIZED`.

## 1. Actual historical substrate and pre-outcome governance

This is the **first real external repository experiment after the P35 synthetic Restic engines**. Upstream is the genuinely evolving public Go HTTP router [go-chi/chi](https://github.com/go-chi/chi) **tag v5.1.0**, frozen original commit `67be7d9cafdaeb4e04e887ff78d09e030ee43b00` (2024-06-28). The frozen target is two existing middleware functions implemented in *separate real Go files*:

- `middleware/content_charset.go::contentEncoding` used by `ContentCharset`.
- `middleware/content_type.go::AllowContentType` used by the body-aware media-type allowlist.

The new demands were **researcher-authored synthetic maintenance requests executed on genuine original source, historical git commits and full Go repository tests**, **not** a replayed upstream fix or a claim that upstream issued these specific demands. We did not open later solution diffs. Avoid inferring historical real-world effort or industry prevalence.

**Chain of custody and timing:**

1. [**D4 PRESEAL commit 5d31ade**](https://github.com/WhoSia/EvoNOMOS/commit/5d31ade7711e382450e62083a4dc831a31e665fe): original SHA, original source, fixed HTTP acceptance tests (16 cases), R0 negative, R-IND and R-SHARED alternatives, B0+/B1/B2 predictions and stopping rule **before either source implementation**.
2. [**D4 source-treatment commit 0045c07**](https://github.com/WhoSia/EvoNOMOS/commit/0045c078e8e09b1a2c108a912af19c7fc8b23a18), author and committer `WhoSia`; read-only original-source [Actions **#37899279543**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37899279543) **SUCCESS**.
3. [**D5 second-demand PRE-OUTCOME SEAL 880cdc6**](https://github.com/WhoSia/EvoNOMOS/commit/880cdc6660374d7b7e34f186f6c5e10d0aa93920) signed **before the assistant accessed D4 hosted results but 62 seconds after CI had completed; outcome-unavailable preregistration NOT MET**, holding 128-byte boundary tests, architecture-fixed incremental edit predictions, no posthoc outcome metric changes.
4. [**D5 treatment commit fdf510f**](https://github.com/WhoSia/EvoNOMOS/commit/fdf510feb72887cc2bfdaa6b86290e1b4883778a). First D5 runner #37899871990 **FAIL** on Bash syntax **before** Go testing (non-scientific harness failure). Only the shell guard syntax was corrected in human `WhoSia` [commit 0104e1e](https://github.com/WhoSia/EvoNOMOS/commit/0104e1e9cafaef2133c1885561a60728868beeb0); frozen D4/D5 tests and Go source arms were not changed.
5. Read-only original-source [Actions **#37899998083**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37899998083) **SUCCESS**. No Actions-authored commit, no bot contributor and no repository-writing workflow permission.

### Timestamp and information-leakage audit (mandatory limitation)

The first original [D4 CI #37899279543](https://github.com/WhoSia/EvoNOMOS/actions/runs/37899279543) **completed at 2026-10-09T07:31:47Z**. The D5 [pre-implementation seal](https://github.com/WhoSia/EvoNOMOS/commit/880cdc6660374d7b7e34f186f6c5e10d0aa93920) was committed **at 07:32:49Z, 62 seconds AFTER D4 CI completion**. In this conversation the assistant had not yet queried or interpreted that run's result when it wrote and committed D5, but GitHub already made the outcome available. Therefore:

- D5 requirements and the 2-site versus 1-site prediction are **genuinely sealed before D5 implementation and D5 testing/outcome**.
- D5 was **not** sealed before the D4 result existed. Claims of a strictly **pre-D4-outcome** seal or independently blinded outcome selection are **NOT CERTIFIED**. Conversation chronology supports *analyst-unreviewed* selection, which is a weaker evidentiary tier than outcome-unavailable preregistration.
- The actual Go native behavior result and D4→D5 incremental edit-direction change are unaffected; the **predictive evidence strength** of the second-demand choice is narrower. A subsequent fresh trial must register *all demand sequences before any arm-run is started* to restore the strictest prospective claim.

## 2. Demand specification and execution

**D4: canonical media-type parameter interpretation.** Both original guards must handle quoted charset, unrelated quoted fields with embedded semicolon, reordered parameters, case folding; malformed and duplicate/conflicting charset values must return 415 on nonempty bodies. Preserve legacy empty-body content-type bypass and optional missing charset only when explicitly listed. Original R0 fails selected new cases as expected. Independent stdlib `mime.ParseMediaType` calls in both guards (**R-IND**) and a newly created shared `parseCanonicalContentType` helper (**R-SHARED**) both pass all 16 frozen cases, `go test -race -count=1 ./middleware` and `go test -count=1 ./...` on original pinned upstream.

**D5: new bounded raw Content-Type length.** For requests with a nonempty body and otherwise legal header, each guard must reject a header of **129 bytes**, admit a syntactically legal header of **exactly 128 bytes** and preserve D4 rules and the ContentType bodyless bypass. This number is a reproducibility parameter, not a product-security standard. The old successful D4 versions each fail the *new*, separately presealed D5 acceptance test for the expected long-header reason. Modified D5 arms both pass D4 **and** D5, whole original Go `go test ./...`, and middleware race tests.

**Proof receipts:**

| Native run | Verdict | Evidence artifact | SHA-256 |
| --- | --- | --- | --- |
| [D4 #37899279543](https://github.com/WhoSia/EvoNOMOS/actions/runs/37899279543) | SUCCESS | 11601623479 | `aeffe3aaad4c6e4aa3fd0db71d5b74acded398ed93bd2436699dce73a342fc23` |
| [D5 #37899998083](https://github.com/WhoSia/EvoNOMOS/actions/runs/37899998083) | SUCCESS | 11601912362 | `cb1c392648927c6a13e42dcc26728a3bf1b63f7630b848f49d12635a809d5168` |

All source arms, frozen public acceptance tests, native runners, AST symbol auditor, source SHA manifests, CI logs and expected negative-control logs are human-account-authored browser-readable repository files in [`tools/p35-p4/`](../../tools/p35-p4/arms/independent/content_charset.go) and [`tools/p35-p4b/`](../../tools/p35-p4b/arms/shared/content_media_parse.go). CI has `contents: read`; the cloned upstream Go checkout is ephemeral. This is not an actual production deployment, a real downstream customer trial or full concurrency proof beyond performed tests.

## 3. Two sequential source-edit cost measurements

**Measurement:** changed *Go production files* and individually gofmt-normalized AST fingerprints of *changed existing functions*, against the exact previous stage source. New helper/file addition is a separate cost; raw +/- lines reside in immutable CI JSON artifacts. The same baseline and oracle are supplied to both arms, with the chosen architecture held constant within D5.

| Dimension | Independently parsed R-IND | Shared parse R-SHARED |
| --- | ---: | ---: |
| D4 modified/added production files | **2** | **3** (includes new helper) |
| D4 changed existing middleware functions | 2 | 2 (plus a **new** helper) |
| D5 **incremental** modified production files | **2** | **1** |
| D5 **incremental** changed existing functions | 2 (`contentEncoding`, `AllowContentType`) | 1 (`parseCanonicalContentType`) |
| Sum of file edit *visits* across D4 and D5 | **4** | **4** |
| D4 native acceptance/full Go/race | PASS | PASS |
| D5 inherited D4 + new acceptance/full Go/race | PASS | PASS |

**Empirical sign change:** R-IND has lower **D4 file edit footprint** (2 vs 3), while R-SHARED has lower **D5 incremental footprint** (1 vs 2). That direction change was fixed **before D5 treatment and D5 CI outcomes**, and before this analyst reviewed D4 logs; however D4 completion preceded the D5 seal, so it is **not** a fully result-unavailable prospective choice. It does **not** prove total design dominance or a universal SRP/OCP/DIP law: adding a helper carries continuing costs, changed-file visits are not effort, and this is one researcher-selected demand sequence in one source repo.

A transparent equal-cost thought model after `k` *further demands of the same kind* is `E_IND(k)=2+2k`, `E_SHARED(k)=3+k`. For `k=1`, totals tie at 4 file visits; `k>1` would favor shared if every further demand truly has the same scope and unit per-file cost. The future cases and nonuniform prices were **not tested**, and this elementary linear equation is not a novel pure-mathematical theorem. We cannot substitute it for observations.

## 4. Competitor tournament and actual limitations

**B0+ source-aware static impact:** D4 preseal identifies the two existing key source functions and adds a plausible but unnecessary wrapper `ContentCharset` candidate; its predeclared candidate set has **recall 1** and **precision 2/3** on the observed function edits. At D5, B0+ sees source ownership and expects independent two locations vs shared one centralized helper. This rivals and explains the sign change; no blind B0+ failure was demonstrated.

**B1 historical cochange:** Factual original history before baseline yielded **one** production commit touching the charset file, **five** touching content-type, and **no verified joint production-file edit**. A 2021 release sweep changed *test files* but is excluded from a causal production cochange target. A history-only predictor therefore has `INSUFFICIENT_HISTORY_TO_PREDICT_PAIR`, rather than an invented bad performance. True comparative B1 demands a history-rich real source.

**B2 Parnas / modularity / design rules:** Parnas (1972) already predicts that a representation reused across modules may be a hidden design decision; Sullivan et al. (2001) already models the cost/value tradeoff of modular interface centralization and evolvability. Both can explain why R-IND avoids one initial helper while R-SHARED localizes a later parser policy edit. **We did not run a full CSDG/Design Rule Spaces or trained CoChangeFinder implementation**, and cannot claim superiority over them.

**H candidate:** Preserving a distinction between raw quotes and valid MIME parameter semantics across two clients was a demand-relative information sufficiency condition. This is a direct classical information-hidden decision observation, **not a new algorithm outperforming Parnas/B0+**. The prospective edit-direction reversal is bounded **world contact**, not novel theoretical generality.

Original scholarship already in canonical Google Drive and inspected: [Parnas (1972)](https://drive.google.com/file/d/1EcQRy3iehx4lUN7uGsZ1BFXU33HggcEQ/view), [Sullivan et al. (2001)](https://drive.google.com/file/d/1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr/view), [Hong et al. (2024) cochange](https://drive.google.com/file/d/1ZL0atP6tINZJW8a3BZ-kzermZ6nhioe6/view). No external literature is credited as automatically correct.

## 5. Terminal bounded judgment and next independent world

`P35-P4 / P35-P4B` can be **CLOSED as bounded real-source/native-code PASS with prospectively measured D4→D5 incremental edit-sign reversal**. The result supports treating the design's stage-specific source edit cost as dependent on future demand distribution. It does **not** close P35 overall, infer general long-horizon costs, establish a full architecture Pareto winner, train a fair B1 model, or authorize LAW-R2.

**Next gate, with a stronger historical comparator:** Preselect a genuinely churned code region before constructing a new change demand. In the same independently evolving chi repo, the prebaseline history inquiry returned at least **100** commits touching `mux.go`, 75 touching `tree.go`, and 46 touching `context.go`. These are *raw path commit counts*, not already verified production cochange/training samples. Or select a second completely independent repository if it offers cleaner historical labels. Freeze the actual prior-commit training/test split, predictions from B0+/B1/B2 with equal inputs, a naturally motivated maintenance demand and an untouched source-only oracle **before** patch outcomes. Continue with patience without self-sealing the same D4/D5 example.

**Constitution:** `BOT_CONTRIBUTION_ZERO`; all EvoNOMOS source commits authenticated `WhoSia`, Actions read-only; original ORIGIN-R1-P12 remains TERMINAL_NONRESULT; no automatic generation transition.
