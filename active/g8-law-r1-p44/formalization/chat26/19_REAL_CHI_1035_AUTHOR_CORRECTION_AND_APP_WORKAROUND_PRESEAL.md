# Real Chi issue #1035 — Author-corrected scope and app-only route guard, PREEXECUTION

**NONBLIND historical researcher-selected source.** Re-read public [issue #1035](https://github.com/go-chi/chi/issues/1035) plus comments, original author bekabaz 2025-11-18. At 15:48Z the author expressly withdrew the second assertion of regex failure in nested route segments after isolated tests. Do not count regex issue as established.

Remaining reported behavior: GET static `/users/me` and PUT parameter `/users/{id}`. A `PUT /users/me` is routed to parameter handler, contrary to reporter's requested 405.

**Before writing test:** use original pinned Chi v5.1.0 (not current master); create app-owned route fixture with GET /users/me, PUT /users/{id}; check PUT /users/me actual response (expect parameter) vs app-owned explicit PUT /users/me response 405. Ensure GET static /users/me and PUT /users/123 retain expected outputs in guarded case. No upstream router modifications, no live listener, no F37 original arms modified. The explicit static route is a narrowly compatible application-owned workaround for the **selected calls** only; does not prove global static precedence, does not prove original author's proposal merged, and is not a prospective blind task.

Alternative: router-level StrictRouting option suggested by third-party commenter; not available in pinned untouched Chi v5.1.0. Mark unaudited; do not invent API.

Ruling if CI passes: **historical issue reproducer and app-owned local mitigation only**. Still no measured cross-arm structure advantage, F38 OPEN, LAW-R2 HOLD.
