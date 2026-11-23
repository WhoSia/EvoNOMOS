# EvoNOMOS P44-F35 R2 — Independent Callback Rival Native Go CI Result (2026-11-21)

**Native original-router CI: PASS under bounded clients. LAW-R2 HOLD; G1–G7 OPEN.**

## Preseal, source and exact outcome

- Pre-implementation source-critical protocol: [85_F35_INDEPENDENT_CALLBACK_RIVAL_PREEXECUTION_SEAL.md](./85_F35_INDEPENDENT_CALLBACK_RIVAL_PREEXECUTION_SEAL.md), committed separately at [0c2617c](https://github.com/WhoSia/EvoNOMOS/commit/0c2617c873abbfadd1f16805cbe6dd4687e329a1).
- Independent rival test: `active/g8-law-r1-p44/f34_original_router_capability/f35_independent_callback_test.go`, committed at [75c6994](https://github.com/WhoSia/EvoNOMOS/commit/75c6994999cba9bdd20236c40181395cc084d09e). This implementation does NOT call `Pick`; its app-owned selector reads the header, selects a function callback from a map and handles missing/unknown keys itself.
- [GitHub Actions F34 workflow #44903866312](https://github.com/WhoSia/EvoNOMOS/actions/runs/44903866312) ran against exact head `75c6994999cba9bdd20236c40181395cc084d09e`: **SUCCESS**. Job `native-original-routers` id `136845215392` completed with successful module verification, `go vet -mod=readonly ./...`, `go test -mod=readonly -count=1 -v ./...`, and `go test -mod=readonly -race -count=1 ./...`. Read-only GitHub workflow with `contents: read`; no bot commits. We inspected completed job-step verdicts, not individual test stdout in this record.

## What the additional test checks

- Independent callback selection and the pre-existing `Pick` selector agree on eight controlled requests: chi/httprouter legacy output, new item output, uppercase normalization and missing/unsupported router header.
- Negative control: deliberately substitute an incorrect chi callback and confirm a detectable difference from the `Pick` output. The test **expects** the mismatch, so its presence is a PASS of the detector, not an upstream failure.
- Concurrent checker: thirty-two concurrent callback requests must retain provider-specific responses. CI's race test passed for the module, including this test.

## Why this matters

F34's earlier `TestCallbackRivalMatchesInterfaceSelection` bound `callback := func(...) { iface(w,r) }`, so it only wrapped the selection function it compared against. The new callback selector is implemented independently at the app-owned dispatch boundary. The original upstream `go-chi/chi@v5.1.0` and `julienschmidt/httprouter@v1.3.0` remain unchanged, with the exact same pinned `go.mod`/`go.sum` as F34.

A bounded match is evidence of tested behavioral parity for these requests; it does not demonstrate a non-interface end-to-end implementation, because the upstream router values still satisfy `http.Handler`. Nor does it show equal maintenance cost, preserved behavior for all contexts, independent future demands, maintainer permissions, or a general SOLID advantage. This repairs the evidence quality of a negative control without creating a new structural law.

**Next gate:** the researcher-owned, app-level callback and interface comparison is now independently implemented. For a real architecture contrast, freeze two matched alternative source arms with identical initial capabilities, require an independently authored future change, include genuine permission and existing-client records, and compare to source-aware classical rivals at equal information and cost. If those elements cannot be established, keep predictive identifiability HOLD.
