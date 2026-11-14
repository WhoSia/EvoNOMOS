# Zerolog actual historical context-state repair, source-informative replay

This fixture does NOT predict an unseen future PR. The research source has already been inspected. It tests real maintained original source exactly before and after merged upstream PR #811 (2026-09-28), while keeping PR #769's unmerged context-capture path distinct.

- Real upstream pre-fix parent: `5eb5f3a76c09eeadc1f2464baf4a4e3f1037c830`
- Real upstream merged one-line fix: `56591163bce358abdb860d3dad599d3ab440621a`
- External historical issue: [PR #811](https://github.com/rs/zerolog/pull/811)
- Separate unmerged historical proposal: [PR #769](https://github.com/rs/zerolog/pull/769)
- [Predictions frozen before source CI](00_HISTORICAL_SOURCE_PREDICTIONS_BEFORE_TEST.md)

The workflow `p44-source-law-zerolog-history.yml` shallow-checks out both exact commit objects independently, uses unchanged original files apart from copying this research-owned external test into the ephemeral original-source checkout, asserts exact commit SHA, then runs `go vet`, five selected native source tests and race tests under Go 1.23.2. No permanent upstream modification or maintainer rights claimed.

Classical field-copy/dataflow and explicit `Event.Ctx` provide a completely adequate rival. This is an independent maintainer-originating repair record, but a retrospective *outcome-aware* replay, not an independent future task forecast, design-law causal study or proof of universal contract preservation. No promotion to LAW-R2.
