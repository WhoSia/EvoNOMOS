# F20 strong classical competitors and evaluation matrix

A0 original upstream regression test diff, plain Go test, and source-aware expected output.
A1 exact branch/path conditional reasoning on changed source with matched complete files.
A2 static points-to/call-graph/effects where state sharing affects a route; no weak 'grep' baseline only.
A3 ordinary incremental source dependency cache and source-matched Go AST/typechecker reanalysis.
A4 model checking/abstract interpretation for parameterized routes and error branches where feasible.
A5 EAC/source certificate under EXACT same inputs/time/actor scope; cannot read future patch if baseline cannot. Treat conventional route constraints and output contract as strong competitors.

Metrics separately: test success, time to build, changed files, safe/unsafe false positives, abstentions, validation walltime, proof byte size and repeated revision reuse. No single weighted index hiding critical false-safe errors. Prior F18/F19 showed exact classical cache equal or slightly faster; no free novelty credit for hashing or route-specific finite graphs.

## Research authority and evidence limits
- These are **historical published commits**, not blinded future events. The commit SUBJECTS and changed filenames already disclose some outcome information before any source patch read.
- The selected code is owned by external upstream maintainers; our permission to build a public copy is not authenticated authorization to edit their canonical repository or to represent their policy.
- A Git commit SHA identifies a repository object; full source byte verification and self-contained executable baseline receipts remain separate obligations.
- A researcher-selected cohort, not statistically random or independently blind. No outcome prediction, causal novelty, G1–G7 closure or law promotion from metadata alone.
