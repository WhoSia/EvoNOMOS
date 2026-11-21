# P44-F35 R3 — Original Go CI Raw-Log Readback, Claim Ceiling (2026-11-21)

Prior research: [F35 preseal](./85_F35_INDEPENDENT_CALLBACK_RIVAL_PREEXECUTION_SEAL.md) · [native verdict](./86_F35_INDEPENDENT_CALLBACK_RIVAL_NATIVE_CI_VERDICT.md).

## Exact CI receipt

- Workflow: [P44 F34 Original Router Capability Comparison #44903866312](https://github.com/WhoSia/EvoNOMOS/actions/runs/44903866312), SUCCESS.
- GitHub job ID `136845215392` / `native-original-routers`, SUCCESS.
- Executed source commit: `75c6994999cba9bdd20236c40181395cc084d09e`.
- Job log explicitly contains `=== RUN TestF35IndependentCallbackRivalAgainstPinnedOriginalRouters`, `--- PASS` for the F35 top-level test and **eight explicitly named F35 request subtests**: chi/legacy, httprouter/legacy, chi/item/a, httprouter/item/a, CHI/item/abc, httprouter/item/abc, missing/item/a, empty-header/legacy.
- The same log explicitly lists original **six F34 top-level tests** as PASS: old-client, independent-version coexistence, request-based router switching, original self-forwarding callback comparison (retained for audit), concurrency and unknown-router rejection.
- Test code additionally executes one intentionally faulty callback that must **not** match the correct result, and 32 concurrent callback requests. These are checks inside the one F35 top-level test, NOT separate named CI test records.
- Module verification, `go vet -mod=readonly ./...`, native `go test -mod=readonly -count=1 -v ./...` and `go test -mod=readonly -race -count=1 ./...` were all recorded as successful job steps.

## Evidentiary constraints

The new test is a genuine independent **application dispatch** implementation, not an independent upstream router or one with no `http.Handler` abstraction. A bounded eight-request equivalence result and negative-control detection do not imply contextual equivalence, owner-authorized source repair, measured developer costs, blind task prediction or conditional SOLID superiority. These unknowns remain open and **LAW-R2 HOLD** continues. No upstream source modifications or bot commits occurred.

This note corrects the earlier R2 statement that only job step verdicts were inspected: raw job logs were subsequently read and the named F35 test passes enumerated above were checked.
