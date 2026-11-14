# EvoNOMOS P44-R3 — Source-Certified Repair Simulation under Stateful Middleware and Alias-Sensitive Change

Frozen 2026-11-04, **before new R3 implementation or native test**. Commit provenance is the GitHub commit that created this file. This is an investigator-designed protocol, **not an external customer demand or independent historical maintenance PR**. Scientific target is a substantive alias/prefix-safety example; claims of external validity or superiority are prohibited.

Original maintained code dependency: go-chi/chi/v5 v5.1.0 middleware.RequestID; official source middleware/request_id.go blob SHA 4903ecc2144e186a74a25a3a4552cf9a74098ed6. Same middleware applied to two original route implementations: standard net/http ServeMux and chi.NewRouter. Middleware RequestID uses context.WithValue and HTTP request WithContext; public GetReqID returns the value, with atomic generated IDs if no supplied request ID. The experiment supplies a stable explicit X-Request-Id to avoid random ID nondeterminism.

Application-owned shared state: a record pointer with mutex-protected mutable string field. One middleware captures an apparent request view before the handler; the update handler changes the same record while a GET request is paused after the capture and before its read. The two implementations of captured view are (A) live alias to the mutable record and (B) value snapshot copied at middleware entry. A deterministic barrier fixes happens-before without a wall-clock timing assertion.

Initial old-client behavior O0 (sequential): GET /items/alpha with explicit reqid returns v1|req-A; POST /policy/alpha with new label v2 returns updated:v2; subsequent GET returns v2|req-B. Both alias and copy methods must match sequentially on both routers. No claim of full HTTP equivalence for HEAD, OPTIONS, encodings or arbitrary paths.

New future demand D1: if GET A enters request middleware and captures the version v1 before an authorized POST B commits v2, the GET A response must still represent v1|req-A; later GET C must return v2|req-C. The old sequential behavior must be preserved. This is per-request snapshot isolation for this bounded source protocol, not general database snapshot isolation.

Fixed edit rights: application-owned middleware snapshot capture method and safe request-level adapter only; cannot patch upstream Chi RequestID source, Go runtime or mutate global middleware RequestIDHeader. Scalar synthetic repair cost = one change from pointer capture to value copy. Do NOT infer actual engineering time. Two original route engines have equal app edit rights.

Pre-outcome predictions:
P0: Both routers satisfy O0 in pointer-alias and value-copy modes.
P1: Both routers violate D1 under pointer-alias mode, despite mutex/race freedom.
P2: Both routers satisfy D1 under value-copy mode.
P3: Classical alias/happens-before analysis predicts P0–P2 exactly; EAC has no demonstrated explanatory advantage here.
P4: Synthetic repair edit cost is one on either framework, no architecture ranking.

Detection: negative control is a live alias returning v2 to a GET that captured before POST; ensure a race detector does not diagnose the logically wrong but synchronization-safe outcome as a data race. Stagewise old-client regression and source-controlled barrier tests, 2 goroutine roles, actual HTTP server.

Evidence: local pure Go reference plus native GitHub Actions pinned original Chi module; log raw statuses, body, RequestID and observed start/update/resume sequence; go test -race. Stop/publish if any forecast fails. Avoid selecting positive cases after outcome. G1–G7 remain open, LAW-R2 HOLD.
