# F20 transparent selection rule & leakage audit

**Metadata-only selection**: For the user-specified desire to leave toy fixtures, query GitHub public commit history for exactly `go-chi/chi:mux.go`, `julienschmidt/httprouter:router.go`, `gin-gonic/gin:tree.go` as of `2025-06-30T23:59:59Z`, first 8 commits per repository, choose the newest commit with subject explicitly starting with or containing fix and a router-behavior claim. The three candidates and parents are sealed in 00 registry before viewing patches. Because researcher chose the repositories and source paths, selection is **convenience/coverage**, not preregistered independent random sampling.

Leakage: subjects `Mux.Find nested routes`, `HandleOPTIONS`, `wildcard panic` and modification filenames were visible during selection. Do not assert pre-demand prediction. No pre-change oracle has been frozen by an external third party. Need an independently archived time-sliced issue/disclosure event to assess nonanticipatory future demands.

Keep selection policy fixed after source patch inspection; if any candidate fails baseline reproducibility, report exclusion with original receipt rather than silently swapping it. Full Go build tests and old-client scope may be unknown.

## Research authority and evidence limits
- These are **historical published commits**, not blinded future events. The commit SUBJECTS and changed filenames already disclose some outcome information before any source patch read.
- The selected code is owned by external upstream maintainers; our permission to build a public copy is not authenticated authorization to edit their canonical repository or to represent their policy.
- A Git commit SHA identifies a repository object; full source byte verification and self-contained executable baseline receipts remain separate obligations.
- A researcher-selected cohort, not statistically random or independently blind. No outcome prediction, causal novelty, G1–G7 closure or law promotion from metadata alone.
