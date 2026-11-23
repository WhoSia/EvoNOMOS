# P44-F21 Unit B — Adjudication and Equal-Information Competition, PRE-OUTCOME PROTOCOL
2026-11-05. This is a research protocol and two local-Go-tested support routines, NOT a prospective study, no future issues assessed, and NO original remote GitHub CI run verified. The 2024 F20 cases remain historical C3.

## Primary question
For a fixed original source tree S at t0, permissible actor edit relation E_pi, frozen old-client observer contexts C, and demand d disclosed at t1>t0, can the precommitted structural model predict (i) existence of a finite authorized prefix-safe repair, (ii) which edit families remain viable, and (iii) the minimal cost frontier, when compared with conventional source-aware baselines that receive exactly the same information?

Do not conflate existence of a repair AFTER disclosure with selection of an irreversible edit BEFORE disclosure. Neither historical title leakage nor source readback proves predictive nonanticipation.

## Three-valued repair truth
1. SAFE_REPAIR_WITNESSED requires the exact legal edit sequence, source tree SHA at each version, successful build, and protected old-client tests/observers at each intermediate stage. It proves ONLY the witness within frozen contexts.
2. IMPOSSIBILITY_CERTIFIED requires complete admissible edit grammar or independently sound lower-bound/impossibility proof, not an unsuccessful search or time-limit.
3. UNRESOLVED when neither side is certified. This must be reported separately. A witness in a bounded grammar is not a claim about all possible Go source repairs.

The scorer counts evaluated successes and errors ONLY in certified adjudicated rows. Denominator choices and abstention rate must be stated; unresolved outcomes do not magically count as incorrect impossibility predictions.

## Equal-information rivals
- EAC research predictor: source-aware structural assumptions, declared observer and rights scope, certificate generation + verification.
- Classic A: unmodified original Go tests and issue-independent static metrics, with explicitly fixed test selection.
- Classic B: AST/type/call/alias/dependency analysis; no source or rights features withheld from this rival.
- Classic C: explicit cost-labelled source-edit graph search / CEGAR or model-checking on the SAME edit grammar and observer set.
- Classic D: footprint/separation logic / bi-abductive obligations where source grammar supports it.
- Conventional caching as a baseline when evidence reuse across revisions is the question.

For all arms freeze model implementation, tuning, corpus selection, CPU/memory budget, edit opportunities, worker permissions, and abstention rules BEFORE demand disclosure. Record CPU, wall, peak RAM, toolchain, source read footprint, and separately measured human maintenance effort; synthetic edit count is NOT developer-hours.

## Precommitted score book
Outcomes: false-safe on impossibility-certified rows, false-impossible on witnessed-safe rows, accuracy on adjudicated non-abstentions, adjudicated abstention fraction, unresolved fraction, cohort inclusion counts and reasons, computational and human cost. False-safe rate's denominator must be SAFE predictions on adjudicated cases. Never report a proportion with denominator zero. Compare same cases and disclose whether competing methods abstain.

## Gates and stop criteria
- All external historical events already publicly documented are BACKTEST/C3, not LIVE.
- The selector and timestamp must be independently authenticated, not merely boolean flags in a Go struct.
- A real downstream safe repair witness must remain separate from proof that the full edit language is complete.
- No LAW-R2 promotion if results tie classical baselines or predictive cohort is absent.
- Keep all negative controls, early failed oracles, and source version IDs.
- GitHub PR #12/#13 Draft and main untouched, human author+committer only.

## Verified boundary
The previous gate's first version incorrectly treated missing independent/rights/build evidence as C4 BACKTEST and did not reject all malformed chronological relations. New HOLD_UNVERIFIED_PROSPECTIVE classification plus 15 tests repair this (local Go 1.23.2 tests/vet/race PASS). The scoring implementation adds five local test cases that refuse to equate NOT_FOUND with impossibility; total local 20 tests PASS. GitHub branch content commits must not be equated with a remote CI result; fresh CI and Notion receipt are independent tasks.

Verdict: F21 AUDIT AND EVALUATION INFRASTRUCTURE / ACTUAL LIVE CASES ZERO / CLASSICAL COMPETITION NOT RUN / G1–G7 OPEN / LAW-R2 HOLD.
