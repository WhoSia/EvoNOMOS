# P34-P1 — Pinned Source Imports and the Contract Authority Boundary

**Status:** P1 bounded CommonJS import-audit METHOD PASS; ownership attribution HOLD. P34 OPEN / LAW-R2_NOT_AUTHORIZED.

Actual Uptime Kuma birth commit `398482d590daaac0d44e288c9be3bc6f6667f8b8` was checked. Blob `server/model/monitor.js` equals `2ad572e53ed051825425f8783c91195cbd243d77`, and `server/notification.js` equals `b1a42d003a92e3760f6d33a4be59784a9cb4dbf2`.

[Read-only hosted run 37885549293](https://github.com/WhoSia/EvoNOMOS/actions/runs/37885549293) SUCCESS, artifact `11595953305`, SHA256 `546dc5c5c0e0b7943e3d96217853c5b96ae48c03d8667089bcb6db0892b23019`. Code: [bounded source import audit](../../tools/law-r1-p34-source-import-audit.mjs) and [contract-channel separator](../../tools/law-r1-p34-source-projection.mjs).

**Source-anchored witnesses:**
- `monitor.js` line 48 has `const { Notification } = require("../notification");`, resolving to `server/notification.js` as a literal CommonJS edge.
- `sendCertNotificationByTargetDays` line 1596 calls `Notification.send` in this pinned source.
- `notification.js` statically requires multiple `./notification-providers/*` modules. Exact import counts and first provider references are emitted to the hosted JSON artifact.
- P34-P0's weak call-target projection is the same between the original and the context-forwarding single-site change. Call argument count differs 2 versus 3 and **rich static baseline M1 could distinguish** the worlds.

**Epistemic boundary:** syntax only proves the import and call relation for these two CommonJS files. It does not establish social ownership, the right to evolve the contract, all runtime edges, or whether dependency inversion is institutionally appropriate. Distinguish `observed_source_edge` from `inferred_contract_authority`, whose status is `NOT_IDENTIFIABLE_FROM_IMPORT_SYNTAX`. This is the P33 mathematical DIP interpretation faithfully restricted to executable evidence.

**Historical P11 labels must not collide:** archive 10.md's **ORIGIN-R1-P11** studies TrueForge WIDE_BOUNDARY_REUSE versus CAPABILITY_SEGREGATED and Exa/Tavily real demand pair. Archive 12.md and repository `active/g8-law-r1-p11/P11_TERMINAL_SEAL.json` describe **LAW-R1-P11** `Pi(X,G,E)` policy state-sufficiency/transport. These are distinct protocols with different authority. P34-P2 should restore ORIGIN-P11 receipts as originally frozen, not misapply LAW-P11 action-result cells as the WIDE/SEGREGATED cost vectors.

**Next:** P2 reconstruct original valid ORIGIN-P11 outcomes and trace contracts with matched requirements; if source authority or full oracle is unavailable, record a bounded hold rather than fabricate equivalence. No Braess mechanism claim without endogenous implementation-choice effects.

**Verdict:** `P34_P1_SOURCE_DEPENDENCY_PROVEN__CONTRACT_CHANGE_AUTHORITY_NOT_IDENTIFIED__NEXT_P11_RECONSTITUTION`.
