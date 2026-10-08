# G8 LAW-R1-P30 Phase II-H — Preliminary Local Outcome, Exact-Source Court Pending

## Chronology
- II-G non-delivered \`INSERT OR REPLACE\` intervention recorded as \`HOLD_INTERVENTION_FIDELITY_FAILURE\` at commit \`8dce3f335ac4c21c85db666117de9d61aade475f\`.
- New II-H corrected intervention was independently precommitted in commit \`cc677ef3e9fce41eed3b382f52f4432322bf853f\` **before inspecting its outcomes**.
- A preliminary local test of \`UPDATE\` for existing sequence rows and \`INSERT\` for missing rows was then run against the system-linked SQLite **3.46.1** library. This test reopened the database connection between phases; it did not compile the exact pinned Git source and did not use the source-built sqlite3 CLI required by the formal hosted Court.

## Local measurements
Three fresh repeats; two history arms at each of two precommitted target sequence values:

| Rounds | Forced \`sqlite_sequence.seq\` | No past insert: future ID | Past insert-and-delete: future ID |
|---|---:|---:|---:|
| 0, 1, 2 | 0 | 1 | 1 |
| 0, 1, 2 | 7 | 8 | 8 |

All 12 arms had an empty visible \`events\` table before the future \`INSERT ... RETURNING id\`. The target sequence row was checked directly before the future action. Both corresponding history arms gave the same result in **6/6** local comparisons. With distinct target sequences the future IDs differed as expected.

## Claim ceiling
This is local **intervention-fidelity-positive evidence**, not a source-pinned official experiment, not a universal predictive-state theorem, and not an independent replication of a new mechanism. The old II-G HOLD remains unchanged; its attempted treatment cannot be silently credited to this new candidate.

The exact-source workflow \`.github/workflows/g8-law-r1-p30-sqlite-durable.yml\` is configured to:
1. check the SQLite Git commit and official Fossil UUID;
2. compile the SQLite CLI from that exact source;
3. run the precommitted II-F durable-history probe and Court;
4. run the separately precommitted II-H verified intervention and independent Court;
5. reject adversarially altered evidence and upload diagnostics even on failure.

No hosted PASS or P30 terminal closure is claimed here. LAW-R2 remains NOT_AUTHORIZED.
