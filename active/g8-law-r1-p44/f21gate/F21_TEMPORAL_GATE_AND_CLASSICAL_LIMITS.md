# P44-F21 — Temporal Claim Gate, Classical Competition, and Nonanticipation Boundary

2026-11-05. Research-only audit after F20. No independent future demand has been observed, predicted, or scored here. G1–G7 OPEN; LAW-R2 HOLD; PR #12/#13 draft; no main merge.

## Unit A: type-check the claim chronology
The Go package `f21gate` separates C3 historical reproduction, C4 chronological backtest, and C5 prospective *eligibility only*. Thirteen local Go tests (Go 1.23.2, GO111MODULE=off) and go vet passed before remote insertion. Its positive test uses **synthetic future timestamps**, not an observed future issue; the gate does NOT certify timestamps, GitHub service provenance, prediction correctness, completeness of rights, or immutability of the receipt. A genuine C5 experiment must independently authenticate all these facts.

The original F20 three repositories remain C3: public commit metadata disclosed subjects and changed files before custom tests. They can never be promoted retroactively to C5 by moving timestamps or generating new predictions.

Two authored code commits on PR #13 branch: `1c5e7ecc` (gate); `d7e177c5` (13 tests). A proposed new GitHub Actions workflow write was blocked by tool safety validation; original remote CI is **NOT VERIFIED**. No bot-authored commit was requested or made by this change.

## Unit B: simple nonanticipation impossibility bound — classical
Let H be source information visible at prediction time, and R a later undisclosed repair demand. Suppose worlds w1 and w2 induce exactly the same available H but require incompatible safe first irreversible edits. Any deterministic predictor f(H) must issue the same edit in both worlds; thus it cannot succeed in both. A randomized predictor that picks one of these two exclusive edits has worst-case success probability at most 1/2 if the adversary chooses the harder world; this bound applies only to this symmetric, two-action zero-sum construction, NOT all repair problems. A legitimate option-preserving edit or abstention may avoid the forced-choice premise. This is standard information-set / online decision reasoning, not a new EvoNOMOS theorem.

Therefore a forecast must specify whether it predicts existence of *some* later edit after disclosure, or recommends an irreversible edit *before* disclosure. Treating them as equivalent creates an information-timing error.

## Unit C: evaluation contract before unknown future issues
Before any issue data or patch arrives, freeze: (1) executable baseline tree and full build dependency source; (2) authorized edit region and actor; (3) old-client observers and coverage limits; (4) exact demand family, which is not the unknown realized demand; (5) outputs SAFE/UNSAFE/ABSTAIN and edit-family estimates; (6) classical source-aware call/dependency analysis, existing tests, ordinary dependency cache, and applicable footprint/bi-abductive methods with identical source and compute budgets; (7) accuracy, false-safe rate, abstention, total wall-clock/CPU/memory, plus human labor separately where legitimately measured; (8) stopping rules and invalidity categories.

Do NOT count prospective prediction accuracy until a genuinely independent later issue passes nonanticipation and source/rights checks. For historical data use `BACKTEST` with immutable chronology and explicit information-leak assessment. The F20 original Go three-repository retrospective replay remains a source-execution sanity control only.

## Verdict
LOCAL F21 EVIDENCE GATE PASS; REMOTE WORKFLOW WRITE BLOCKED; F21 PROSPECTIVE COHORT NONE; CLASSICAL NONANTICIPATION PRINCIPLE; NO ADDITIONAL SOFTWARE EVOLUTION LAW; G1–G7 OPEN; LAW-R2 HOLD.
