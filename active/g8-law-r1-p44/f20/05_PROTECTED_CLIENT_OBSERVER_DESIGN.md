# F20 protected-client observer contract design

We cannot infer full client behavior from a commit title. Candidate interfaces to reproduce at parent and post revision: chi Mux.Find nested route reporting; httprouter OPTIONS response and allowed method handling; gin conflict panic text for invalid wildcard path. These are DIFFERENT observable types (route match, HTTP headers/status, panic message), so a pooled scalar correctness score would be unsound.

For each: define request/path or invalid route input before test; record output status/header/body/panic under original native Go; distinguish new desired behavior from pre-existing protected clients; repeat unaffected regression suite. For regression claims provide EXACT named test and original source commit. Negative result may be a compile mismatch, not a semantic failure.

Source design assumption: no proof of ALL clients or all interleavings. Test observations are underapproximations; unknown complete clients mean UNKNOWN for universally safe edit. F13 trace-completeness rules apply, not a blanket PASS.

## Research authority and evidence limits
- These are **historical published commits**, not blinded future events. The commit SUBJECTS and changed filenames already disclose some outcome information before any source patch read.
- The selected code is owned by external upstream maintainers; our permission to build a public copy is not authenticated authorization to edit their canonical repository or to represent their policy.
- A Git commit SHA identifies a repository object; full source byte verification and self-contained executable baseline receipts remain separate obligations.
- A researcher-selected cohort, not statistically random or independently blind. No outcome prediction, causal novelty, G1–G7 closure or law promotion from metadata alone.
