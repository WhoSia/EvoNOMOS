# F20 external source validity threats

- Selection on visible commit titles creates issue-description leakage; no meaningful 'unknown future' test yet.
- Public source commits may be merges with parent state affected by unrelated changes; pin complete parent and post tree.
- Router libraries differ in Go toolchain and dependency ecosystem; forcing a uniform Go version can cause spurious failure.
- A commit can include tests or CI changes; execution at post tree may not be comparable with parent if tests are new.
- HTTP status, response headers, redirects and panic messages are distinct client contracts; never replace with one artificial scalar.
- CI runners can use cached dependencies/network; successful build without module manifest and checksums is incomplete reproducibility.
- Changed-file count, number of edit actions, measured time and actual developer labor are different units.
- Historical commit diff sizes are not a causal estimate of the minimal authorized fix.
- Only three convenience examples; no statistical transport or general law.

## Research authority and evidence limits
- These are **historical published commits**, not blinded future events. The commit SUBJECTS and changed filenames already disclose some outcome information before any source patch read.
- The selected code is owned by external upstream maintainers; our permission to build a public copy is not authenticated authorization to edit their canonical repository or to represent their policy.
- A Git commit SHA identifies a repository object; full source byte verification and self-contained executable baseline receipts remain separate obligations.
- A researcher-selected cohort, not statistically random or independently blind. No outcome prediction, causal novelty, G1–G7 closure or law promotion from metadata alone.
