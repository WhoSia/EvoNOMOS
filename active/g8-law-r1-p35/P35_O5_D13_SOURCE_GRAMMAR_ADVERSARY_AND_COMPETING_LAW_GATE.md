# P35-O5 — D13 Parser-Alternative Adversary and the Next Law-Pair Identification Gate

**Date 2026-10-10 KST.** Parent `P35 OPEN`, `LAW-R2 NOT_AUTHORIZED`. This is an extension of original P35-O3/D11 and P35-O4/D12, NOT a new general law. Prior to any O5 original Chi execution, we inspected existing O3 CSV and independent scanner source, and ran an exploratory *local* Go `encoding/csv` probe. That local probe showed that `"ping"   ` raises a CSV parse error. **Therefore the native D13 classification below is NOT outcome-blind with respect to parser mechanism; its predeclared test is a source-level adversarial audit, not an independently discovered law.**

## Historical source and contract ambiguity

[Original chat 15](https://drive.google.com/file/d/1zQ9j6GmfFaijbfz024-CQ2sJpj_SnpJV/view) and [DIP-49](https://app.notion.com/p/3ccef561cf92818484a4d55302715e84) / [DIP-50](https://app.notion.com/p/3ccef561cf92811291b4c56437bc5b4b) demand prospective pair separation and faithful source realization. [O3 D11 seal](P35_O3_D11_INDEPENDENT_GO_RIVAL_PREIMPLEMENTATION_SEAL.md) describes CSV-like quoted tokens and 'trim surrounding spaces', but the finite D11 Go acceptance does not expressly test trailing whitespace after a closing quote. Do not silently interpret its unspecified edge grammar as definitively settled. The old O3 seven-job PASS remains a valid bounded test result, but **is not parser equivalence on all inputs**.

## D13 clarified future requirement (for prospective source treatments only)

On synthetic research header `X-EvoNOMOS-Mode` only, leading and trailing ASCII space/tab outside a fully quoted token, including after the closing `"` and before the list separator or end-of-field, are permitted and stripped. Double quotes inside quote-delimited tokens must still be doubled. Malformed non-whitespace text after a closing quote invalidates that physical field, while other physical fields remain available. Existing D0/D8/D9/D10/D11 tested behaviors, header registration priority and LIVE/SNAPSHOT temporal contracts must remain intact.

Declare exact original Go sources: `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00` overlaid with O3 actual `live-csv` and `live-scanner` source, unchanged. Frozen independent Go test `tools/p35-o5/tests/chi/p35_o5_d13_test.go` is created before a D13 repair source is written. The run checks old frozen original D0-D11 Go/race/vet tests first and then separately classifies D13. Expected source results *known from exploratory inspection* are **CSV D13 negative** and **scanner D13 positive**. No D13 source repair, no edited grammar after outcomes.

## Strong classical competition: source-aware, not a strawman

- **B2 syntax/abstraction prior (strong baseline):** standard `encoding/csv` strictness and an independently written tolerant quote parser can differ even while both satisfy the tested D11 subset. This already predicts that a D13 field-space grammar may require a CSV-only source change; neither edit locality nor two correct patches establishes beyond-SOLID law novelty.
- **B0 source-aware prediction:** the code and test grammar together identify the parse boundary. A changed router representation (LIVE vs SNAPSHOT) does not, by itself, settle quoted-token parsing. If observed parser outputs differ, the simplest mechanism is local grammar treatment, not a new structural architecture law.
- **Prospective H-opt (not yet discriminated):** after choosing two *semantically D13-equivalent actual Go repairs*, future opt-in changes might make some patch families easier to extend. Unless H-opt's precise pairwise signature differs from strongest classical information hiding/repair-refinement predictions, flag `DIP49_IDENTIFIABILITY_HOLD`, NOT a newly discovered law.

## Next actual conditional-law tournament to freeze separately before its outcomes

Build genuinely different **original Go** implementations of the SAME mutable route-registration contract (not the old opposed D-LIVE vs D-FROZEN), then compare source- and workload-conditional effects under identical `Register/Serve` behavior. Explicitly compare **eager publication** (compile after each registry update) against **dirty-epoch lazy publication** (compile on the first subsequent read). Both must supply consistent route semantics, including sequential post-update visibility, legacy routing, concurrent synchronization/race safety and independently specified acceptance. The candidate mechanistic signature for a demand sequence `w` is:
- `U(w)`: number of completed registry updates;
- `C(w)`: number of maximal nonempty update bursts that are followed by a request before the next update burst.
- EAGER predicts rebuild calls proportional to `U(w)` for the frozen exact implementation; LAZY predicts calls proportional to `C(w)`. At fixed counts of updates and requests, `UURR` and `URUR` give `U=2` for each but `C=1` and `C=2`, respectively, for LAZY. These are **conditional architecture-specific hypotheses**, not claims about all repairs. Their expected workload-order effect is already understood by classical caching, incremental computation and dependency invalidation. It is **not** a law-vs-classical disagreement.

### Prospectively fixed structural workload signature (planning only, NOT native execution)

To avoid reducing the next trial to method counts or arbitrary patch-count ranking, freeze TWO operationally distinct implementations **before** outcomes: `EAGER` compiles each completed registered update under a synchronizing publication operation; `LAZY` marks the registered state dirty under the same synchronization and compiles at most once on the next request after that nonempty update burst. Each request must see all previously completed updates. Both arms clone the exact same baseline code and pass the same complete dispatch oracle. Public `HeaderRouter map` exposes direct writes that cannot be intercepted; the concurrent-safety claim MUST be restricted to a newly declared synchronized registration API, not to arbitrary unsynchronized external map mutations. Otherwise mark `REALIZATION_HOLD`.

Two deterministic test sequences, held at 16 successful route updates and 16 route-dispatch requests each, with the same initial 32-entry registry, are:

| Query | Exact word | U | R | EAGER rebuilds | LAZY rebuilds |
| --- | --- | ---: | ---: | ---: | ---: |
| Q-burst | `U^16 R^16` | 16 | 16 | 16 | 1 |
| Q-interleaved | `(UR)^16` | 16 | 16 | 16 | 16 |

`U` and `R` represent successful API-level operations, not background cache pollution or unverified scheduling. Count rebuilds **after the initial handler construction**. The predicted rebuild numbers are testable implementational mechanisms (falsified by different counts on exact sources), not a causal architecture law by themselves. The primary outcome vector additionally contains correct dispatch, registry revision visibility, race/linearizability checks, update latency, request latency and allocated bytes; never silently collapse it to one scalar score. Prior classical eager/lazy caching mechanisms predict these patterns; the prospective EvoNOMOS theory has **not yet supplied a conflicting explanation**.

To claim repair-option survival, seal a syntactically and semantically explicit allowed repair grammar `Γ` and compare sets of *observed witnesses*; when arbitrary source rewrites are permitted, initial architecture labels alone cannot logically fix universal repair reachability. Preserve one-run `MAY` versus all-repairs `MUST`. Do not pretend selected arms enumerate `R_d^Γ(A)`.

**Identification gate:** Before allowing the separate structural experiment to earn novel-law credit, freeze an actual strong B2/caching competitor and EvoNOMOS H* with *different predictions on one shared prospective query* `q=(c,w,Q)`, plus proof of DIP-50 semantic prefix/observation factorization. If the B2 and H* signatures coincide, report `MODEL_PAIR_NOT_SEPARATED` and do not claim novelty regardless of native CI outcomes. Runtime performance, update latency, reader tail latency, memory use and correct dispatch remain different outcome dimensions. No single SOLID score.

## Negative-aware final eligibility

D13 is **source-adversarial, calibrated with prior local parser knowledge**, not a blind theory-identification experiment. `P35_OPEN / D12_LIVE_CSV_NATIVE_PASS / D13_NATIVE_PENDING / DIP49_MODEL_PAIR_IDENTIFICATION_HOLD / LAW_R2_NOT_AUTHORIZED`.