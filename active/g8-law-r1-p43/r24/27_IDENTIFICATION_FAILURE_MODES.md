# Identification failure conditions

- Non-comparable initial contracts: raw GET-only Chi vs stdlib GET handler disagree on HEAD.
- Different ownership: one side can edit an upstream router while the other cannot.
- Different adapter burden: adding a Chi-specific HEAD adapter is real maintenance work.
- Postselection: selecting demands after observing source differences violates a clean blind prospective test.
- False proof completeness: passing a finite request set cannot certify every HTTP request or middleware context.
- Metric collapse: lines-of-code, number of edits and actual time are not equivalent.
- Reviewer selection: an unmerged PR is not evidence a source change was technically impossible.
- Historical overreach: earlier P42 source results cannot automatically certify new R24 cases.
- CI provenance: workflow creation is not workflow success.

Each failed gate has an off-ramp: report a scoped counterexample, a classical tie or a source-access limitation, instead of forcing a new named law.
