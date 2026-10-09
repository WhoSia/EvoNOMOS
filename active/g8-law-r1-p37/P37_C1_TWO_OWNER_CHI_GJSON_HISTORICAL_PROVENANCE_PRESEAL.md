# P37-C1 PRESEAL — Two-Owner Composed Software, Historical Provenance, and SOLID-Controlled Repair Reachability

**2026-10-10 KST · CONTRACT FROZEN BEFORE SOURCE IMPLEMENTATION · P37 OPEN.**

### Original real software and what is project-authored

Actual independently evolved source dependencies: `go-chi/chi/v5@67be7d9cafdaeb4e04e887ff78d09e030ee43b00` (HTTP router), `tidwall/gjson@690362d6edf4bcbde1e9f54d552d3814f1cd5bcb` (JSON key parser); both pinned Go modules must compile in one project-authored **composite** Go application. The glue and owner modules `ingress` and `archive` are written by EvoNOMOS and are **not** an independently evolved real production application. This integration uses genuine third-party software APIs while serving as a controlled structural experiment.

### Module ownership and ports

- Owner A **ingress**: handles HTTP via actual `chi.NewRouter`, converts an event's JSON semantic id with Go's standard `encoding/json`, and forwards to a typed `Store` interface (DIP-style high-level-to-port dependence).
- Owner B **archive**: implements `Store`, stores semantic `id` plus revision and, when supplied, a defensive copy of original JSON bytes, then may answer historical exact-key-lexeme demands using actual `gjson.Result.ForEach/Raw`.
- Original clients invoke `POST /events` and `GET /state`, receiving a stable status and JSON semantic state. Current observer cannot query raw source.
- The sole treatment on initial ingress is one **policy choice**: `forwardOriginal=true` forwards raw event bytes; `false` forwards nil, losing historical lexeme. Two input worlds `{"id":7}` and `{"i\\u0064":7}` have the same current semantic state; bytes differ.

### Fixed identical baseline contract Q0

All 4 combinations of two ingress forwarding policies × two source lexical spellings must produce `POST /events→204` and `GET /state→{"id":7,"revision":1}`, with no raw bytes exposed at that endpoint. Store operates independently of client raw view. No source mutation during reads, concurrent read-only handling race-free. The new `archive` implementation must preserve old legacy API.

### Future requirement D_hist — exact old source lexeme after input has vanished

A future client asks owner B's new `OriginalKeyAt(0)` **for the already processed event**, to output exact original quoted JSON key spelling `"id"` or `"i\\u0064"`. No replay, caller prompt of old spelling, upstream audit log, network retriever or hidden event store; no wild guessing based on which test case is running. `Γ_B` allows changing ONLY archive implementation and reader; ingress and historical persisted bytes cannot be rewritten or recovered by oracle. A single deterministic repair must answer correctly for *both* hidden histories, not a history-specific hardcoded value.
- Forward-original history: stored original bytes are available, and owner B should be able to parse and satisfy D_hist.
- Lossy history: both inputs collapse to same semantic historical stored state, so the uniform repair cannot reconstruct both different source lexemes under Γ_B. This is an information-theoretic no-go **for hidden-history-uniform future repairs**, not a proof of pointwise failure when input history is known externally.
- Extending `Γ` to allow owner A to begin forwarding raw bytes will enable exact future-event provenance, but **does not retroactively recover the old event**. If replay is permitted, conclusion changes.

### Explicit SOLID comparison

The two ingress treatments have the **same** module dependency direction `ingress→Store interface←archive`, ownership split, client-specific interface, and old behavioral observations. The project *does not certify all five canonical SOLID principles* merely from this diagram; it shows that these static predicates/heuristics alone do not decide historical provenance survival. An intentionally concrete-coupled counterexample with raw retained can satisfy D_hist despite a declared DIP violation. This establishes neither SOLID universal inferiority nor a new universal law. Mathematical [MATH-C](P37_MATH_C_SOLID_RESTRICTED_EMBEDDING_AND_PROVENANCE_COUNTERTHEOREMS.md) proves a **restricted preservation embedding**, not an unconditional derivation of all SOLID principles from EvoNOMOS.

### Native gate and rival

Run real Go modules, `go test -race -count=1 ./...`, `go vet ./...`, exact module pin and source digest receipt. Provide a **positive** end-to-end historical raw recovery in both input histories under forwarding policy and a **negative** indistinguishable historical snapshot in lossy policy. Strong classical opponents (information preservation/sufficient statistics, type/context semantics, SOLID source/interface heuristics) predict these results; DIP49 remains HOLD. DO NOT reinterpret a correct no-go as evidence that a legacy failing test has been repaired.

**FROZEN:** `P37_C1_COMPOSITE_ORIGINAL_CHI_GJSON_PROSPECTIVE__OWNER_A_B_AND_GAMMA_FIXED__MATH_C_SOLID_RESTRICTED_EMBEDDING_NOT_LAW__NATIVE_PENDING`.
