# P36-O6 — Finite Maintenance-Automaton Court: Exhaustive Action Words Against an Independent Reference Model

**2026-10-10 KST · test-program seal BEFORE running O6, AFTER O3–O5 treatment construction. P36 OPEN.**

This is **not** a blind patch treatment; the four original Chi source candidates and their earlier results are known. O6 provides a systematic independent executable reference oracle, reducing dependence on targeted source-derived D15–D17 test cases. Exhaustive claims apply **only to this finite alphabet and depth**.

## Frozen deterministic source-visible semantics

All routes share one exact-match header `X-P36-O6` with a fixed match value `test`, distinct attached middleware tags. Start with three registrations `A,B,C` in this priority order. A semantic reference model is an immutable logical *registration-order list* of entries `{tag,enabled}` and a FIFO queue of indices representing disabling events. This model does **not** invoke production Chi HeaderRouter, use either treatment's index or sorted-by-ID insertion algorithm, or inspect private fields.

Allowed action alphabet `Σ={R,D,E}`:
- `R`: register a **new** tagged exact-match route at the end of the original order.
- `D`: disable the earliest currently enabled route; if none enabled, false/no update.
- `E`: re-enable the earliest still-disabled route by **disable event FIFO**, preserving its original registration order; if none pending, false/no update.

At each prefix after each action compare: method boolean for D/E, exact `Stats` revision increment on successful register/disable/enable, published revision, and HTTP response tag of earliest enabled logical route or fallback. Compare against an independent model not sharing the SUT's disabled-record index representation. Old contracts D14/D15 are not changed.

**Finite complete input domain:** all words of lengths 0..6 over Σ (there are `Σ_{k=0}^6 3^k = 1093` words), plus verification at every intermediate prefix. Same original upstream `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`, no test fixtures changed after CI outcome. Record the first lexicographically enumerated shortest counterexample, if any; no random seeds or test selection after result.

## Old four source variants (NO new treatment source for this O6)

- [ERASE](../../tools/p36-o3/arms/chi/erase/p35_epoch_router.go): expected negative on some word containing E after D.
- [POSITION_INDEX](../../tools/p36-o3/arms/chi/retain/p35_epoch_router.go): expected negative when repeated disables and restores collapse positional records.
- [RELATIVE_REBASE](../../tools/p36-o5/arms/chi/relative-rebase/p35_epoch_router.go): expected negative on a cyclic sequence where one-sided saved-index correction is insufficient.
- [STABLE_ORDER](../../tools/p36-o4/arms/chi/stable-order/p35_epoch_router.go): expected to pass **all 1093 words and all prefixes**. If false, preserve the counterexample, repair source in a separately versioned treatment and do not hide new negative.

For each original Go source, run full upstream regression, `go vet`, race testing of existing D14+O6 functional tests, and isolated independent finite O6 model oracle. An expected finite oracle FAIL in the first three is a successful *negative-control scientific result*, not a CI tooling error. Source hash and test hash preserved in artifact.

## What this could legitimately establish

On native successes with expected negatives, the **observed finite source candidate survival** against a complete depth-six action alphabet would be:
```
May_{Γ_obs}(universal_{|w|≤6} prefix conformance) = true,
Must_{Γ_obs}(universal_{|w|≤6} prefix conformance) = false.
```
This would provide a stronger bounded **conformance surface** than hand-picked D15–D17 worlds, not a universal theorem about all histories or all Go software. A successful stable candidate does not imply stable IDs are necessary: other correct algorithms can explicitly maintain relational invariants without unique IDs.

**Strong classical rival:** automata-based conformance testing, abstract reference models, stable-order maintenance and test-suite overfitting already predict all mechanisms. No novel H-vs-B inequality yet, so `DIP49_LAW_IDENTIFICATION_HOLD` continues. Testing another independent actual source or nontrivial edit-grammar law remains mandatory before promoting generality.

**Pre-result state:** `P36_O6_FINITE_ALPHABET_1093_WORDS_PRESEALED__NO_NEW_SOURCE_TREATMENTS__ORIGINAL_GO_CI_PENDING`.
