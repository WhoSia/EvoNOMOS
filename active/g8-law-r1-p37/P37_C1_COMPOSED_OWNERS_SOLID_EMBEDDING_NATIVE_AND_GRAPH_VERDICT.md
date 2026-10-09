# P37-C1/C1D — Actual Two-Owner Chi + GJSON Original-Go Composition and Scoped SOLID Negative-Control Verdict

**2026-10-10 KST · AFTER ORIGINAL NATIVE CI READBACK · P37 OPEN · DIP49 IDENTIFICATION HOLD**

## What was actually built

The components **Chi core HTTP router** and **gjson JSON key parser** are genuine independently evolved external Go libraries, requested by exact source commit IDs. The composition, the two owner modules, the interface and all tests are research-authored; this is **not** a naturally occurring independently evolved composite production repository.

- Chi original pin `go-chi/chi/v5@67be7d9cafdaeb4e04e887ff78d09e030ee43b00` (GitHub Actions Go module receipt resolves version `v5.1.0`).
- gjson original pin `tidwall/gjson@690362d6edf4bcbde1e9f54d552d3814f1cd5bcb` (Go module receipt resolves `v1.20.0`).
- Source A `tools/p37-c1/ingress/ingress.go`: actual `chi.NewRouter` HTTP POST /events and GET /state, reads input and delegates to *interface* `StorePort`, optionally forwards a defensive copy of the raw event bytes to owner B.
- Source B `tools/p37-c1/archive/archive.go`: project-authored archive `AppendSemantic(id,raw)`, `State()` and future `OriginalKeyAt(n)`, using actual `gjson.ParseBytes` and `Result.Raw` to select original JSON quoted key.
- The explicit alternate concrete-owned source `tools/p37-c1/concreteingress/concrete.go` uses a **direct compile-time dependency** on `*archive.Store` in its high-level constructor; it is the separate C1D static-DIP violation negative control, introduced after the first C1 native result and separately presealed.

The original actual external library source was not modified. A `go get @exactCommit` workflow records resolved module versions. Only the project-owned integration source changed.

## Preregistered four-world source contracts

[Prospective original source C1 preseal](P37_C1_TWO_OWNER_CHI_GJSON_HISTORICAL_PROVENANCE_PRESEAL.md) before source implementation, plus [C1D new negative-control preregistration](P37_C1D_CONCRETE_DEPENDENCY_NEGATIVE_CONTROL_PRESEAL.md) after first C1 outcome but before the concrete source. Four initial worlds vary raw lexical history `{"id":7}` vs `{"i\\u0064":7}` and original forwarding policy `forwardOriginal=true/false`.

Q0 original externally visible `POST /events` returns 204 and `GET /state` returns semantic `id=7,revision=1`. **All four** match current output. Uniform historical future demand `OriginalKeyAt(0)` after the original input has disappeared must return the **exact original quoted key spelling**; no source replay, hidden log or caller-supplied answer.

- **Owner A forwards retained bytes**: B still has a distinguishing observable input and its additive future reader returns correct `"id"` vs `"i\\u0064"` (both native tested).
- **Owner A discards bytes**: both hidden histories yield identical B-accessible historical state; B-only deterministic future reader cannot satisfy both historically different outputs uniformly. This is **not** a no-go for a reader that knows the hidden world from an external oracle. The actual source tests confirm identical stored state and explicitly signaled lack of original information.
- **A becomes permissive only later**: a later event can preserve original key, yet the earlier lossy event stays unavailable without replay; native source test PASS.
- **Direct high-level-to-concrete dependent owner A, but forwards raw**: C1D test returns exact historical keys in both worlds. A narrow static DIP condition (policy owner must depend only on abstraction rather than concrete archive package) fails, yet this future repair succeeds. No claim every interpretation of SOLID is refuted.

## Original native CI receipts

**Original source composition** [C1 #37983103065](https://github.com/WhoSia/EvoNOMOS/actions/runs/37983103065) final SUCCESS, Go `1.23.12 linux/amd64`, actual chi and gjson versions from `go list -m all`, `go vet ./...` PASS and **`go test -race -count=1 ./...` PASS**. All five component tests passed:
1. `TestP37C1SameLegacyObservationAcrossFourWorlds`
2. `TestP37C1OwnerBRepairCanRecoverWhenIngressRetainedRaw`
3. `TestP37C1OwnerBLossyHistoricalWorldsIndistinguishable`
4. `TestP37C1IngressPolicyChangeProtectsFutureNotHistory`
5. `TestP37C1ConcurrentReadersPreserveLegacyContract`

Original C1 ZIP artifact **11642216730**, sha256 `d9e9e530e4889d1cfc8715a0cfe6249c88d9bbaa8897c9787842a62fb05b8a12`. Archived source SHA: ingress `19f3309aad461de1b31e805540e77be6bf8251547c8350ab5232cea684ed187c`, archive `295f433b13aff99dca06f6ca990576fc15c6695187bb54cca20e0bcfcd74c25b`, original Q0/Future/race test `348cfc7574e725da3a57c98acdf2f1e2c484428526fc25bc185ca8c62420219f`.

**Direct-concrete-dependency separate native** [C1D #37983448468](https://github.com/WhoSia/EvoNOMOS/actions/runs/37983448468) SUCCESS, full previous suite plus `TestP37C1DConcreteOwnerDependencyAndHistoricalRecovery` under race and vet PASS; source-level grep proves high-level `concreteingress` directly imports `archive` and publicly requires `*archive.Store`; original `ingress` remains interface-port only. Artifact id **11642725667**, digest `sha256:f2c60afd36b26de5c92f55db8a8e6e1798a1b80d515c7f589747e67eb4696147`. This is post-first-result intentionally scoped negative control, not prospective blinded holdout.

**P37-MATH-C finite formalized SOLID model** [#37983210716](https://github.com/WhoSia/EvoNOMOS/actions/runs/37983210716) SUCCESS, exact 16 finite two-state transition-graph configurations checked for an **exact-copy conservative embedding**, plus exhaustive 2-lexeme uniform reader existence distinction between lossy and retained state. ZIP artifact id **11641407249**, digest `sha256:54847e82b067cdb07dd9efa2ae2ad8bf05ed312ec546f09fcdf3c45086d7fadb`. This is bounded model checking of classical representation reasoning, not an arbitrary-language machine-checked theorem.

**Owner graph source-linked model** [#37983647370](https://github.com/WhoSia/EvoNOMOS/actions/runs/37983647370) SUCCESS, explicit [four-world owner-typed graph](../../tools/p37-c1/model/owner_repair_graph.json) plus [checker](../../tools/p37-c1/model/check_owner_graph.py); same Q0 observation, retained archive state separates the two lexical histories, lossy archive state merges them; deterministic archive-only uniform reader has no solution for the lossy class. Artifact id **11641922778**, digest `sha256:3d17710d5173864cd8aa205b4b4933b9d03d9826fa27c3533c7a12ec3af4bf9b`. This model is manually source-linked, NOT an exhaustively AST-derived authorized Go source edit graph.

**Technical provenance caution:** An intermediate re-triggered C1 workflow [#37983394844](https://github.com/WhoSia/EvoNOMOS/actions/runs/37983394844) failed during `go mod tidy` while transient sibling module imports were being indexed after separate commits; it did not enter source functional/race tests. Original preceding #37983103065 and subsequent source C1/C1D native CI succeeded. Preserve this as environment/code-publication chronology, not a scientific negative world.

## Scoped mathematical interpretation

[MATH-C restricted SOLID embedding](P37_MATH_C_SOLID_RESTRICTED_EMBEDDING_AND_PROVENANCE_COUNTERTHEOREMS.md) proves that **finite formally specified OO source states, clients, nominal subtypes, interfaces and authorized edits** can be injected into a more general typed source/repair/context graph while preserving exactly mapped finite observation and authorized edit paths; a declared formal SRP/OCP/LSP/ISP/DIP constraint family defines a **restricted subdomain**. This is the precise mathematical sense of "SOLID as a special case". It does NOT derive the five informal engineering heuristics from unknown general axioms or establish beyond-classical novelty.

[MATH-D authority–provenance cut](P37_MATH_D_AUTHORITY_PROVENANCE_CUT_AND_HISTORICAL_REPAIR_OBSTRUCTION.md) states the conditional theorem: **if all accessible histories pass through a channel collapsing h1,h2 and no alternate B-readable log/side channel exists**, B-only deterministic repair cannot output historically different raw key strings uniformly. Source actual native worlds witness this premise. Having preserved input removes this information obstacle, but does not automatically guarantee a legal edit path.

**Strong classical rivals** data provenance, noninjective sufficient-statistics and contextual equivalence already explain the result. Neither a new beyond-SOLID structural law nor DIP49 identification is obtained just by completing this formalization and test.

**Final:** `P37_C1_OWNERS_CHI_GJSON_NATIVE_PASS__C1D_DIRECT_DEPENDENCY_NEGATIVE_NATIVE_PASS__MATH_C_FINITE_EMBEDDING_PASS__SOURCE_LINKED_OWNER_GRAPH_PASS__SOLID_A_SCOPED_SUBDOMAIN_NOT_STRONGER_NEW_LAW__DIP49_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
