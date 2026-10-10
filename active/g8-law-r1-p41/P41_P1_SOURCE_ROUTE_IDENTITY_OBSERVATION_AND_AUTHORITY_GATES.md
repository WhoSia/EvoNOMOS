# EvoNOMOS G8 LAW-R1-P41-P1 — Source-Realized Route-Identity Observation and Independent Rights/Dependency Evidence Gates

**P41-P1 first subcourt · 2026-10-11 KST · P41 RUNNING · prior P41-P0 bounded semantics complete · P41-P1 PARTIAL / OPEN · LAW-R2 NOT_AUTHORIZED.**

## 0. Research claim and true boundary

P41's typed semantic model in [P0](P41_P0_TYPED_SEMANTIC_PREMISES_AND_INDEPENDENT_EVIDENCE_COURT.md) proves, in an unconstrained synthetic product, that a reduced scalar response readout need not determine a program's selected handler/route identity. This P1 subcourt tests whether **an actual maintained, pinned source router realizes the same observation loss** with native Go execution.

It does not claim a full general object-oriented law, a Go-to-Lean simulation, an independent authority record, or full empirical A–F axiom independence. It also does not claim that an observer allowed to introspect `Context.Path` cannot distinguish the programs: the point is precisely that the readout must be declared and route provenance included whenever route identity is part of the contract.

## 1. Source-realized pair, and observation projection

Source: original **labstack/echo v5** pinned at commit `3882266a3641a36fc2111b48cd597adab1c1ecea`; original source unchanged. This test is based on the previously noted publicly open [Echo issue #2619](https://github.com/labstack/echo/issues/2619) and earlier P40-P5/P6 native countertraces. It is **not** a blind unsighted issue forecast, but an intentional source-realizability probe of a separately specified mathematical abstraction.

Two independently generated Echo router worlds:
- **W0** registers only `GET /v2/*/tags/list` and returns HTTP status 200 with body `SAME_RESPONSE`; the handler identity and `Context.Path` report tags.
- **W1** registers `GET /v2/*/tags/list` and `GET /v2/*/blobs/uploads/:ref`; BOTH handlers, if selected, return the exact same status and body, but store their own handler-ID and `Context.Path` in an independent test probe.
- Both independently preserve identical `GET /old` status and body.
- The evaluation sends the **same literal URL** `GET /v2/foo/bar/tags/list` to both worlds.

Predeclared readout: `q(W)=(requestMethod, requestURL, oldClientStatus, oldClientBody, probeStatus, probeBody)`, with source registration admitted in both. This readout **does not include** route registration metadata, selected handler identity or dynamic `Context.Path`.

If the original native router evaluates both worlds with identical `q` and different `selectedHandler`, then no total function on `q` can recover handler identity for all worlds in this explicit source ecology. This is classical nonfactorization, not a new theorem; [P41-P0 Lean no-response-only-route-identity lemma](../../tools/p41/lean/P41SemanticP0.lean) supplies the schematic logic.

## 2. Source and CI

[Standalone native Echo original-Go test source](../../tools/p41/p1-native-echo/route_identity_projection_test.go) · [read-only original-Go workflow](../../.github/workflows/g8-p41-p1-route-identity.yml). Exact original upstream SHA is asserted by CI, together with tested EvoNOMOS code HEAD and artifact SHA. **Do not claim source-realization PASS until independently reading the hosted Go result and logs.**

If successful, this makes the missing route-identity evidence concrete **for category D** and clarifies why P41-P3 scoped behavioral subtyping has to name an appropriate observer/context set rather than equating scalar HTTP responses with full semantics. It does NOT source-realize category C (authentic authority) or category F (provider capability).

## 3. P41-P1 authority and dependency hard gates

**C — Authority:** require a versioned authorization fact about a real edit and a legitimate principal, with reliable provenance such as authenticated protected-branch rules, explicit review/approval roles or owner-granted capabilities that were *actually in force at the edit revision*. Mere CODEOWNERS text, repository visibility, a git commit author line or the ability to clone source is not a proof that a person had institutionally valid authorization for arbitrary code edits. Current evidence: **SYNTHETIC_ONLY**.

**F — Dependency capability:** require source-resolved import/provider type signatures and a version-indexed target graph; then a countermodel where the same client request and route identity have different admissible provider ports. A link to `go.mod` alone is not a fully independently measured capability contract. Current evidence: **SYNTHETIC_ONLY**.

**P41-P1 acceptance target:** separate actual source tests for route identity and context frames; independent C/F provenance before promoting them beyond the typed product; genuine source-boundary conditional simulation on a specified grammar, ideally verified with an independent Lean checker. Keep classical CSP/constraint satisfaction, contextual refinement and frame logic as live alternatives.

**P41-P1 remains OPEN until these gates are satisfied.** P41 is officially RUNNING. LAW-R2 NOT_AUTHORIZED.
