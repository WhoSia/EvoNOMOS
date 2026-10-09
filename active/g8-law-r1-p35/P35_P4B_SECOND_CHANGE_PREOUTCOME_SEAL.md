# EvoNOMOS P35-P4B — Prospective Second Change for Real Chi Maintenance, PRE-OUTCOME SEAL

**2026-10-09. This document and independent second-demand acceptance oracle were authored before reading P35-P4 R-IND/R-SHARED CI outcomes.** P35 remains OPEN; LAW-R2 NOT_AUTHORIZED.

## Inheritance

Exact original Go module: `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. The existing [P35-P4 D4 preseal](P35_P4_REAL_CHI_PREDEMAND_SEAL.md) freezes D4 syntax/charset behavior, two intervention arms, prior Git history and B0+/B1/B2 source-informed baselines. The new D5 change applies **only after both D4 arms pass the already frozen oracle**; no D4 failure may be hidden to make D5 favorable.

## Independent second demand D5: bounded Content-Type header observation

For a nonempty request body, `ContentCharset` and `AllowContentType` shall refuse any raw HTTP `Content-Type` value exceeding **128 bytes**, even if it is otherwise a syntactically valid media type with accepted charset and media subtype. Exact 128-byte legal header must remain admitted. When the body is empty, `AllowContentType` preserves its previously promised bypass. A shorter well-formed Content-Type continues to be evaluated by D4 rules, and malformed syntax still returns 415. No public Go signatures change.

The limit is intentionally **a synthetic maintenance demand**, not a historical security issue attributed to chi, and not an assertion that 128 bytes is an appropriate production limit. The test boundary is what enables a falsifiable comparison of versioned change propagation.

## Frozen prospective source prediction

**R-IND architecture freeze:** each of `contentEncoding` and `AllowContentType` directly performs independent `mime.ParseMediaType`. No introducing a shared parser in D5 treatment; doing so would be a **migration**, not a fixed-arm incremental repair. Predicted **2 previously existing functions modified**, in 2 production files.

**R-SHARED architecture freeze:** `parseCanonicalContentType` remains the shared parser and is still called by `contentEncoding` and `AllowContentType`. The byte upper bound belongs in the shared parser. Predicted **1 existing function modified** in 1 production file; no caller edit necessary.

**Bounded sign-reversal prediction:** initial D4 cost is R-IND 2 modified production files vs R-SHARED 3; D5 incremental cost is R-IND 2 changed existing functions/files vs R-SHARED 1. This is a **different cost coordinate and time stage**; no unconditional winner, no total lifecycle or human work ranking. Demand probabilities and per-file/module overhead remain external parameters. The comparison can falsify the prediction if other sites are required.

**B0+ / B2 / B1:** Source-aware impact and Parnas's information hiding already predict the conditional centralization benefit. B1 cochange is still sparsely supported and cannot be called inferior from zero observations. EvoNOMOS H claims no novel predictive superiority over these informed rivals.

## Frozen tests, admissibility, and truth tiers

The sealed test `tools/p35-p4b/tests/second_demand_test.go` independently tests exact 128 bytes, 129 bytes, both combined/individual middleware modes, a short valid header, and bodyless AllowContentType bypass. The unchanged D4 arms **must fail the D5 test for the expected long-header reason**; independently patched D5 versions must pass D4 and D5 suites, `go test -race ./middleware` and upstream original `go test ./...`.

Primary scientific outcome: actual production file/function method-diff support via Go AST normalized declaration comparison, plus raw +/− lines and new helper burden. **Do not change D5 acceptance after outcome inspection.** Whole-system cost, long-run human review effort, strong CSDG implementation and general SOLID law remain unmeasured.

This is the exact next-demand continuation of the same first independent real codebase; it is not yet a second independent repository or a randomized maintenance trial. 
