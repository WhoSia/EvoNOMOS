# Chat 26 — F37 HandlerFunc Adapter Original-Go CI Verdict (2026-11-21)

**BOUND SOURCE-NATIVE PASS / CLASSICAL SEMANTIC EXPLANATION / F38 OPEN / P44 RUNNING / LAW-R2 HOLD / G1–G7 OPEN.**

## Exact execution custody

- [Predictions and negative controls frozen before code](14_F37_ADAPTER_EQUIVALENCE_GO_PREEXECUTION_SEAL.md), commit `1697de910d352345b6f23de8b562d87c147f24a3`.
- [New independent supplementary test source](../../f34_original_router_capability/chat26_adapter_semantics_test.go), commit `24d9dc9ed5cc34ddd3484d81981d3f6746dbc978`.
- [Read-only Go CI workflow](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/.github/workflows/chat26-f37-adapter-court.yml) created at `ae9b6171515a564a8e7d6bfd29108e6888dd981d`.
- **Native GitHub CI [#44912007022](https://github.com/WhoSia/EvoNOMOS/actions/runs/44912007022), exact tested source SHA `ae9b6171515a564a8e7d6bfd29108e6888dd981d`, job `136869602878`, completed SUCCESS.** Decoded raw job log read back and step verdicts checked: Go 1.23.2 setup, go mod verify, go vet -mod=readonly ./..., go test -mod=readonly -count=1 -v ./..., go test -mod=readonly -race -count=1 ./... all SUCCESS.
- No GitHub Actions bot commit; existing sealed F37 arm source packages and upstream original pinned Chi/httprouter were not changed.

## What was actually tested

1. **Adapter forwarding parity:** 8 named source-arm response cases with `http.HandlerFunc(left.ServeHTTP)` and `http.HandlerFunc(right)` agree with independently supplied expected body and status. The original F37 ten-probe test and read-only concurrent request test still pass.
2. **Method-set negative control:** original custom Handler exposes a custom Marker method; after wrapping its ServeHTTP in `http.HandlerFunc`, the Marker interface is no longer implemented, despite same HTTP response. So finite wire-output equality is NOT type/contextual equivalence.
3. **Typed-nil negative control:** typed nil pointer in an interface and nil function wrapped as HandlerFunc both create non-nil Handler interface values. Neither was called. This tests semantic representation boundaries only.
4. **Regression evidence:** previous F34, F35, F36, F37 named tests, module vet and race all succeeded in the new CI receipt.

## Claim ceiling and scientific decision

A function and `http.Handler` can be exchanged at ordinary HTTP call sites by standard Go adaptation, so a generic source-signature representational superiority claim is unsupported. Conversely, custom method-set inspection and nilness can distinguish wrapped values. Neither result says which architecture is better for actual future maintenance; no edit of those architectures under an independently authored F38 requirement was performed.

The standard Go interface and closure semantics explain all results. **CLASSICAL TIE / NO NOVEL LAW; F38 STILL OPEN.** A future comparison must explicitly define observers beyond wire-level HTTP if type inspection matters, provide equal source edit permissions, independent requirements and measured repair costs.
