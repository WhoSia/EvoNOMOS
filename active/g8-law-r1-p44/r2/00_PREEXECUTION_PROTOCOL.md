# EvoNOMOS P44-R2 — Pre-execution research protocol (2026-11-04)

Title: Prospective Repair-Certificate Identification under Matched Source Semantics.

IMPORTANT: This is a researcher-predeclared sequence **before new R2 source tests are written/executed**, but it is neither third-party-blind nor previously unknown to the investigator. The task family is deliberately independent of R24's observed HEAD, percent-unescape and 405 mismatch categories. Outcomes must not be retroactively relabeled as blind holdouts.

Source pair: Go 1.23.2 net/http ServeMux and pinned go-chi/chi/v5 v5.1.0; adapters inherited from P44-R1 exactly, including H,D,M. Initial fixed observer O0 is the already-disclosed 12-probe set, not full-HTTP observational equivalence.

Fixed app-maintainer rights: add or revise application-owned route handlers and their registration; cannot modify third-party router source, Go standard library, or shared Go runtime. No invisible extra permission on one side.

Demand sequence, in this exact order:
D1: GET /ledger/alpha/revisions -> status 200, body `revisions:alpha`.
D2: GET /ledger/alpha/audit -> status 200, body `audit:alpha`, while D1 must remain correct.
D3: GET /ledger/alpha/summary -> status 200, body `summary:alpha`, preserving D1 and D2.

All 12 old probes must be re-executed at initial normalized source and after each staged app edit. Preserve required response status/body; check allowance/Location under O0.

Reference classes: (i) direct original-source execution under two routers, (ii) finite authorization-labelled shortest-path LTS, (iii) same-information classical source-aware route-addition oracle. Strong classical prediction is a **TIE** for incremental route addition cost 0,1,2,3 under one synthetically priced edit per new route on both sides. From raw initial versions total cost remains Stdlib [0,1,2,3] vs Chi [3,4,5,6] due to previously measured normalization work; never confuse these numbers.

Failure outcomes must be preserved in their entirety. Refute this protocol's tie prediction if either router cannot implement an authorized stage or preserve O0 with the same edit grammar.

No developer labor measurement. No LAW-R2 promotion. No claim of novel structural law from the tie.
