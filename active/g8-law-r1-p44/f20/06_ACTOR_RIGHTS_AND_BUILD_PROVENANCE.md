# F20 actor rights, source ownership, build manifest

Upstream OSS repos allow public reading and local testing subject to licenses; the experimental actor is a local research fork/CI process, NOT the authenticated official maintainer. Do not equate a GitHub public diff with authorization to modify production source. Model two distinctly: (1) experimental patch scope = paths modified in known historical commit (retrospective, information leakage); (2) genuine maintainer right = requires own repository rules/permissions/branch protection and review history, not established.

Baseline parent tree SHA and post tree SHA are needed, not only one file. Go module root, dependencies, vendored code, generated assets, build tags and tests must be recorded or bounded. CI action checkout SHA does not automatically prove dependency availability/version stability. Failed dependency resolution must remain an environment failure distinct from client regression.

## Research authority and evidence limits
- These are **historical published commits**, not blinded future events. The commit SUBJECTS and changed filenames already disclose some outcome information before any source patch read.
- The selected code is owned by external upstream maintainers; our permission to build a public copy is not authenticated authorization to edit their canonical repository or to represent their policy.
- A Git commit SHA identifies a repository object; full source byte verification and self-contained executable baseline receipts remain separate obligations.
- A researcher-selected cohort, not statistically random or independently blind. No outcome prediction, causal novelty, G1–G7 closure or law promotion from metadata alone.
