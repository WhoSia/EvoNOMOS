# Paper B §6 — Batch rendering prediction

Baseline: the executable shape fixture in `ocp_case.py` at `f1b8e739de5a868a2526ed6256ba784c6e58ec53`. This is an author-designed prospective check. The prediction is recorded before implementing its candidates.

## Requirement and legacy contract

Add `batch.render_many(kinds)`. It returns a list of bracketed legacy rendering strings in input order, retains duplicates, returns an empty list for empty input, and raises `ValueError` if an unsupported kind occurs. Both layouts retain their original rendering outputs for circle and square. Compare the same input, output and legacy obligations under both placement rules.

## Placement rules

- **Layout-preserving ownership.** The operation-file layout can implement transformation of each item in the new operation module. In the shape-owned layout the per-shape transformation must be callable from each existing shape file. The new batch entry point can coordinate both implementations.
- **Shared adapter permitted.** Either layout can transform the result of the unchanged legacy renderer in the new operation module.

All existing baseline source files are counted equally. Only the explicit candidates are compared. A candidate is a witness of feasibility. Source counts and functional checks do not estimate human effort. The naming of the two rules records the policy change and does not characterize all uses of OCP.

| Placement rule | Operation files, existing/new | Shape files, existing/new |
| --- | --- | --- |
| Layout-preserving ownership | 0 / 1 | 2 / 1 |
| Shared adapter permitted | 0 / 1 | 0 / 1 |

The predicted advantage in existing-file edits disappears under the second rule. Reject the numerical prediction if either candidate misses its announced count, fails the feature or legacy suite, or fails the rule it is meant to obey. Preserve the old triangle and labeling fixture as a regression check.
