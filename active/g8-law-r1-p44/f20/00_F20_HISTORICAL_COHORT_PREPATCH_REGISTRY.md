# F20 original maintainer cohort, prepatch registry, 2026-11-05

**Gate:** historical cohort selected using public `commits?path=...&until=2025-06-30T23:59:59Z` metadata and commit parent receipts. Exactly three external Go router repositories. Selected *fix* event for each from the first eight returned commits at cutoff, prior to reading patch bodies. Selection is a modest reproducibility rule for this candidate set, not blinded randomization. Parent and post SHA recorded below.

- chi: `go-chi/chi` parent `882c15e6462ce0630529d04c330e84942ebd059d` → post `6ceb498b221efa11f559602beb2463b8b52c2161` at 2024-09-26T17:44:06Z, `mux.go`, PR #954; metadata subject: Fix `Mux.Find` not correctly handling nested routes (#954)
- httprouter: `julienschmidt/httprouter` parent `ef8578da8d8e1217ea44313b23edf46154b198ab` → post `484018016424d215c0b87c42f4c9b57d980fbd00` at 2024-01-30T10:56:56Z, `router.go`, PR #360; metadata subject: fix: only append MethodOptions as allowed method if HandleOPTIONS is true (#360)
- gin: `gin-gonic/gin` parent `9d11234efec1e5517b2887a6e7dfbc9c017bc52c` → post `ea53388e6ee4a6a0a1647b390c56eeed780e7e56` at 2024-10-26T00:28:59Z, `tree.go`, PR #4077; metadata subject: fix(tree): Keep panic infos consistent when wildcard type build faild (#4077)

Do not claim that user-approved editor rights, complete old-client observability or prospective demand timing are known. Source patch reading is allowed AFTER this registry is committed; historical subject-level leakage cannot be undone.

## Research authority and evidence limits
- These are **historical published commits**, not blinded future events. The commit SUBJECTS and changed filenames already disclose some outcome information before any source patch read.
- The selected code is owned by external upstream maintainers; our permission to build a public copy is not authenticated authorization to edit their canonical repository or to represent their policy.
- A Git commit SHA identifies a repository object; full source byte verification and self-contained executable baseline receipts remain separate obligations.
- A researcher-selected cohort, not statistically random or independently blind. No outcome prediction, causal novelty, G1–G7 closure or law promotion from metadata alone.
