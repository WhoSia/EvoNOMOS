# P33 — First Pinned Source-Support Barrier: A Bounded Historical Witness

**Hosted run:** [37807536786](https://github.com/WhoSia/EvoNOMOS/actions/runs/37807536786), SUCCESS, immutable Uptime Kuma source `398482d590daaac0d44e288c9be3bc6f6667f8b8`, historical P2 materializer, P3 reconstitution and original P3 terminal vector seal. **Artifact:** `11563706254`, SHA-256 `ce5724b5f4084b2d550e330a9936714899a277e76744206c12ed9d320a92bac0`.

## Exact bounded result
For fixed real demand #7316 (phase0), the set of physical source files modified from the identical birth source is:
- **DISPERSED**: 5 files — `server/notification-providers/issue-tracker.js`, `server/notification.js`, `src/components/NotificationDialog.vue`, `src/components/notifications/IssueTracker.vue`, `src/components/notifications/index.js`.
- **DUAL**: the same 5 **plus** `server/notification-providers/law-r1-p2-membership-registry.js`, `src/components/notifications/law-r1-p2-membership-registry.js` = **7 files**.

Therefore `Supp(DISPERSED phase0)` is a *proper subset* of `Supp(DUAL phase0)`. This comparison is based on SHA256 of actual reconstructed before/after file bytes, not lexical count, class count, or P2 frozen S site metadata. Tool: `tools/law-r1-p33-repair-support.py`.

P3 historical bounded-no-network functional oracle supports both source treatments for the tested requirements but does not certify production-equivalence or exhaust legal implementations. Historical P3 lifecycle vectors:
```text
              phase0 S L C A Q     phase1 S L C A Q
DISPERSED       5 22 0 0 1         5 80 0 0 1
DUAL            2 36 0 3 1         2 75 0 0 1
```
The arm with a physical **superset** of changed first-demand source files has a lower **follow-up** handwritten L (75 rather than 80) under the sealed second demand #7559. Thus initial physical support inclusion does **not** imply lower cost on a *different later demand* under these bounded world/metrics.

**Do not overinterpret**: cumulative L for these two particular demands is DISPERSED `22+80=102`, DUAL `36+75=111`. The DUAL arm does not dominate total L here; P3's no-winner verdict still applies. A hypothetical repeated -5 benefit is not measured. Changed physical files are not the P3 S semantic membership edit-site metric and not the number of logical declaration types. The two treatments are **candidate implementations from a frozen two-arm grammar**, NOT the complete set of all admissible/minimal program repairs.

## Formal implication — standard and bounded
Consider two source-compatible implementation policies from a single starting source, yielding configurations a' and b', with `Support(a→a') ⊂ Support(a→b')`. It is **not valid** to infer
`Cost(a'→d_next) ≤ Cost(b'→d_next)`
without a monotonicity assumption linking *future* transition cost to *past* physical edit-support inclusion. The two coordinates even live on different transitions. The P3 source witness refutes that unjustified dominance inference in its bounded empirical setting; it is not a new general mathematical theorem. A support-minimizing search would discard DUAL under simple subset pruning, yet its observed next-demand L is lower. Optimization over a finite *trajectory* should retain conditional continuation values, not just first-step minimal repairs.

## P33 science requirement
Move beyond this historical witness: construct a **new source-pinned, independent same-demand alternative-repair family**, verify each candidate's *complete* functional oracle, compute source supports and source-grounded typed obligation descriptions **before** outcome exposure, and force a genuinely distinct forecast between H and strong B0+/B1/B2 at matched information. If no such candidate exists, report HOLD rather than a fabricated conditional OO law.

**Verdict:** `P33_HISTORICAL_SUPPORT_DOMINANCE_BARRIER_PASS__NO_NEW_PROSPECTIVE_DISCRIMINATION__LAW_R2_NOT_AUTHORIZED`.
