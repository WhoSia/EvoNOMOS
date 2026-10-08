# G8 LAW-R1-P30 Phase II-G Outcome Audit — Intervention Fidelity Failure (Local, Not Hosted)

## Chronology and status
- Prospective candidate precommit: commit \`0c5535651343473d704bed128facbc6850d83b29\`, before inspecting any results for the sequence-equalization intervention.
- Runtime of this preliminary audit: Python sqlite3 linked to SQLite **3.46.1**, not yet the independently built exact Git mirror commit.
- Intended manipulation: \`INSERT OR REPLACE INTO sqlite_sequence(name,seq) VALUES('events', 0 or 7)\`.
- **Verdict: HOLD_INTERVENTION_FIDELITY_FAILURE__NO_CAUSAL_RESCUE_VERDICT__LAW_R2_NOT_AUTHORIZED.**
- The original P30 Phase II-F observational candidate and its precommit are unchanged.

## Observed local contrasts
For a fresh table (no prior insert/delete), setting \`0\` produced measured \`H=0\` and future ID \`1\`; setting \`7\` produced \`H=7\` and future ID \`8\`.

For a table with one prior insert followed by deletion, attempts to set \`0\` or \`7\` left the first matching \`sqlite_sequence\` row at \`seq=1\`; both futures returned ID \`2\`. In a diagnostic test after attempting to set \`7\`, the history arm contained **two rows**:
\`(rowid=1,name='events',seq=1)\` and \`(rowid=2,name='events',seq=7)\`.

\`PRAGMA table_info(sqlite_sequence)\` confirmed that neither \`name\` nor \`seq\` is declared UNIQUE or PRIMARY KEY. Thus SQLite's \`OR REPLACE\` conflict action had no uniqueness conflict to resolve.

## Causal interpretation
The precommitted intervention intended to equalize latent allocator state across histories; it failed to do so. Comparing different futures after this manipulation does **not** falsify the scientific hypothesis that actual \`sqlite_sequence\` equalization can rescue prediction: treatment was not delivered. This is a **manipulation-fidelity failure**, not a positive or negative rescue result.

Never silently change the original treatment definition, edit the old precommit after seeing the result, or treat this as fresh independent mechanism evidence.

## Next prospective repair experiment
A new, separately precommitted candidate may use:
1. \`UPDATE sqlite_sequence SET seq=t WHERE name='events'\` for an existing row;
2. \`INSERT INTO sqlite_sequence(name,seq) VALUES('events',t)\` **only if the row does not exist**;
3. strictly verify exactly one relevant row with \`seq=t\` before observing the future output;
4. reject the intervention as non-delivered if that verification fails.

Such a protocol tests a **different intervention**, is confirmatory only for data collected after its own prospective precommit, and must preserve the current claim ceiling: bounded causal sufficiency for one SQLite allocator behavior, no persistent ontology failure, no LAW-R2, no P30 closure.
