# P44-F37 R4 — Go Typed Adapter Counter-Rival Pre-Execution Seal (2026-11-22)

**Purpose:** challenge an overly strong interpretation of the previous original-Go negative control: wrapping a handler in the *standard* HandlerFunc loses extra methods, but it does not follow that callback-centered application source can never expose those methods. Source arms are left unchanged. This is a classical Go adapter demonstration, not an external F38 maintenance request.

## Before writing test code
- Both F37 packages are independently written application-owned implementations using Chi v5.1.0 and httprouter v1.3.0; left returns `http.Handler`, right returns a function. They meet a fixed old oracle, but this does not measure edit cost.
- Build the **same researcher-authored explicit typed adapter** around both callbacks:
  a Go struct containing `func(http.ResponseWriter,*http.Request)` and a marker token; implement `ServeHTTP` forwarding to the function and a separate `Marker()`.
- Test identical eight HTTP request/status/body expectations for each independently constructed arm after typed wrapping, and type-assert the marker on both wrappers.
- Negative control: ordinary `http.HandlerFunc` wrapping the same callback lacks the marker; standard Go type semantics predict this difference. In other words marker retention is a wrapper design option, not an intrinsic ability only available to interface-selection apps.
- Include handler/callback versions and four concurrent read-only parallel requests to ensure no accidental global rewriting.
- Abort or report failures if original F34–F37 regression/race tests fail. Do not edit F37 arm code or upstream library.

## Predictions
1. Both typed wrappers produce same HTTP outputs and expose the marker method.
2. Both plain HandlerFunc wrappers produce same HTTP outputs but do **not** expose marker.
3. Original frozen F37 tests stay green; no packages change outside an added test.
4. Standard Go adapter theory explains all results: **CLASSICAL TIE**, F38 OPEN, LAW-R2 HOLD.

Run in separate read-only GitHub CI: Go 1.23.2, go mod verify, go vet -mod=readonly, go test -mod=readonly -count=1 -v ./..., go test -race -mod=readonly -count=1 ./..., capture exact SHA and raw job logs. Failure is preserved, not rewritten as passing.
