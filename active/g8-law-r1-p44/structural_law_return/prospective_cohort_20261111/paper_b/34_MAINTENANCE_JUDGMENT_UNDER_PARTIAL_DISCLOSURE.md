# What a maintenance decision can establish with a withheld premise

This replay uses the four executed cells in [the fixed-patch witness](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md). Run `python3 replay_meyer_disclosure.py` in this directory. The provider, existing files, permitted edit boundary, behavior and witness data are unchanged. Each of the two context fields can be revealed as one of its two recorded values or withheld. Withholding leaves both values admissible. The compatible cells form a nonempty set.

Accept if every compatible cell accepts the edit. Reject if every compatible cell rejects it. Defer if the compatible cells disagree. This gives a decision relative to the admissible set recorded for the case. A reviewer should record how those alternatives were obtained. Disclosure can narrow the set, so an already unanimous verdict is stable under further disclosure in this model. The proof is inclusion of the narrowed nonempty set in the original set.

| Disclosed demand | Disclosed contract excludes book | Disclosed contract includes book | Contract withheld |
|---|---|---|---|
| Reports | Accept | Reject | Defer |
| Reports and errata | Reject | Reject | Reject |
| Withheld | Defer | Reject | Defer |

Result: one accept, five rejects and three deferrals in the nine disclosure settings. These numbers count logical settings in one designed case. One disqualifying fact can justify rejection even when the other field remains open. Approval here requires the specific shorter demand and the contract that does not bind book formatting. This distinction raises a practical question for the manuscript: which outstanding fact can still change the decision, and who can supply it?

The comparator is a deterministic replay of executed fixture data. We have not collected model or reviewer responses to withheld information, nor measured calibration or time savings in the field. Any additional plausible demand or contract can change an answer by expanding the admissible set.
