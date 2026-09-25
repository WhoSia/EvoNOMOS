# Outcome-Silent Engineering Protocol

The development environment is part of the measurement apparatus.

Before the measurement firewall is released, the operator may observe only named state tokens needed to continue execution, such as:

- `SOURCE_OK`
- `MATERIALIZE_OK` / `MATERIALIZE_FAIL`
- `BUILD_OK` / `BUILD_FAIL`
- individual frozen contract check names with PASS/FAIL
- `ORACLE_EQUIVALENT` / `ORACLE_DIVERGED`
- `COMPARABLE` / `NONCOMPARABLE`

The following are sealed and must not be printed to stdout/stderr, step summaries, commit UI, or ordinary artifacts before comparability passes:

- additions/deletions and churn
- LOC
- number of changed/touched files
- binary/object/archive sizes
- build or test duration
- complexity or dependency-count proxies
- arm-specific test-count differences
- any ranking or winner-like summary

Raw command output must be redirected into arm-local sealed logs. Sealed logs must not be uploaded under a name or metadata surface that leaks a comparative proxy.

Git operations used during treatment construction must avoid `--stat`, `--shortstat`, `--numstat`, diff summaries, or commit output that reports file/change counts. A commit SHA may be emitted only after the arm is fully materialized and the harness has verified that the command's visible channel is proxy-free.

Pair comparability is semantic, not metric. It checks same frozen source, same contract, same shared scaffold, same oracle, same user-visible behavior, no extra feature advantage, no donor borrowing, and bounded unrelated edits.

If this protocol is breached, terminate the wave as `HOLD_OUTCOME_BLINDNESS_BREACH` with no same-wave rescue.
