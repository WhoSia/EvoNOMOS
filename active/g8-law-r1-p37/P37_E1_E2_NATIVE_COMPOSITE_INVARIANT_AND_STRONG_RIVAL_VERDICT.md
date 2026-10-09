# P37-E1/E2 — Post-Native Real Inter-Repository Sessions/Securecookie Invariant Court and Owner-Product Geometry

**2026-10-10 KST · POST ORIGINAL-GO SOURCE EXECUTION · P37 OPEN · DIP49 HOLD / LAW-R2 NOT_AUTHORIZED.**

## Evidence chain

1. The [E1 prospective pre-source seal](P37_E1_NATURAL_SESSIONS_SECURECOOKIE_TWO_OWNER_COMPATIBILITY_PRESEAL.md) froze source pins, six expected writer/reader compatibility cases, checkpoint invariants and target before any new test was implemented.
2. A [single frozen Q23-independent additive test file](../../tools/p37-e1/tests/sessions/p37_e1_original_cookie_compatibility_test.go) was copied into a checkout of **unaltered original** `gorilla/sessions@bb4cd60c952a9ce48ea0dc6cc7b282ff79c38263`; the upstream sessions source had already imported `gorilla/securecookie` via `NewCookieStore` → `CodecsFromPairs` and `CookieStore.Save/New` → `EncodeMulti/DecodeMulti`. Separately checked out **original** `gorilla/securecookie@eae3c1840ec4adda88a4af683ad0f60bb690e7c2`. They are naturally integrated **separate repositories of the same Gorilla ecosystem**, not independent corporate governance; no researcher-created source coupling was required.
3. Native [E1 original Go/race/vet CI #37985028491](https://github.com/WhoSia/EvoNOMOS/actions/runs/37985028491) completed **SUCCESS 1/1**. `go vet ./...` and `go test -race -count=1 ./...` completed on **both** original module checkouts, and frozen tests `TestP37E1ExactOriginalCompatibilityMatrix` (all six subcases PASS) and `TestP37E1OriginalSafeSequentialMigration` PASS. Go `go1.23.12 linux/amd64`. Checkouts pinned SHA verified before use. The ONLY original sessions working-tree changes were a copied additive test file and `go.mod/go.sum` dependency-resolution bookkeeping to point to the pinned local securecookie module. **No upstream production source file edited**.
4. E1 original GitHub Actions ZIP artifact **11642378372**, SHA256 **`a79390dcf9e2741ae5fc22fefb912ab04bd88144ce9c315acc1863ca5fd76c26`**, directly downloaded and inspected. Original raw logs confirm exact six-subcase acceptance, sessions + securecookie full race/vet and original two SHA pins. Frozen test SHA archived in ZIP.
5. Native [E2 finite model CI #37985430782](https://github.com/WhoSia/EvoNOMOS/actions/runs/37985430782) completed **SUCCESS**. [Source-linked compatibility graph](../../tools/p37-e2/owner_product_repair_graph.py) verifies:
   - Binary square 4 possible mixed-state combinations satisfy Theorem E1;
   - no unary local predicates can reproduce the actual six-pair writer/reader invariant table;
   - no safe B-reader/W-writer one-owner-only path to new-only terminal without a dual compatibility state;
   - B dual reader expansion → A switch → **explicit external legacy expiry** → B contraction gives a 4-transition safe path;
   - joint atomic change is a **different Γ** and does not prove one-owner sequencing.
   Separate [MATH-F exhaustive relational enumerator](../../tools/p37-e2/check_rectangular_theorems.py) verified **all 64** possible 2×3 compatibility relations (22 are rectangular under this finite enumeration) and **16,384** exact local-product graph/demand/invariant combinations satisfy product May factorization when its strict hypotheses hold. ZIP artifact **11642855623** digest `sha256:3e5a7d44b079fd9d0250cfe9bb005b4a5b713be5e37799b52ef1b7a9b8f90994`.

## Original source-native compatibility matrix

`W0` = old-key writer, `W1` = new-key writer; `R0/R1` old/new-only reader; `R*` = original `NewCookieStore(newKey,nil,oldKey,nil)`, which actually configures TWO codecs because the original API consumes (hash, optional block) pairs. Values below were asserted by original Go source tests. Each semantic session payload is ordinary string `stage=kept`; toy fixture keys are not production material.

| Current writer | Consumer reader | I_live new legitimate cookie | I_legacy prior old cookie | Interpretation |
| --- | --- | --- | --- | --- |
| W0 | R0 | PASS | PASS | initial |
| W1 | R0 | FAIL | PASS | owner A changes first |
| W0 | R1 | FAIL | FAIL | owner B switches directly |
| W0 | R* | PASS | PASS | owner B expands |
| W1 | R* | PASS | PASS | owner A changes after B expansion |
| W1 | R1 | PASS | FAIL | terminal new-only **requires explicitly expired** legacy obligation |

No claim this test establishes resistance to attacks, crypto security, long-running distributed network reliability, or exact production window duration. It is a **structural compatibility invariant court**.

## What is new as a research representation, vs already-known mathematics

The user-requested beyond-SOLID structural quantity is **not runtime cost**. In mathematical terms, the safety relation `I⊆S_A×S_B` is **nonrectangular**, so local-owner safety certificates cannot be simply multiplied to certify global safety. An authorized global edit path exists only if the product graph has I-preserving intermediate states. [MATH-E](P37_MATH_E_OWNER_PRODUCT_INVARIANT_BARRIERS_AND_BRIDGE_THEOREMS.md) and [MATH-F](P37_MATH_F_RECTANGULAR_INVARIANTS_AND_LOCAL_GLOBAL_REPAIR_FACTORIZATION.md) make these exact. The key conditional factorization statement:
```
When I=I_A×I_B, Γ=Γ_A ⊠ Γ_B and demands split as D_A×D_B:
 May_global((a,b),D) ⇔ May_A(a,D_A) ∧ May_B(b,D_B).
```
For nonrectangular I, this implication fails in general. This mechanism is **orthogonal to whether the implementation uses SOLID-style dependency inversion**. It reveals a useful missing axis in ordinary class diagrams but is classical product automata/assume–guarantee and staged compatibility theory.

The original API **already advertises multiple codecs for rotation**; therefore a dual decoder state is not a surprise newly predicted by EvoNOMOS. A strong classical prior explicitly predicts E1/E2. No `σ(H)≠σ(B*)` new-law separation exists. The E1 owner labels distinguish hypothetical **deployment configuration** ownership, not two proven corporate source-code custodians.

## Independent ecology transfer

[P37-E3 preregistered cross-organization natural Gin integration](P37_E3_CROSS_ORGANIZATION_GIN_SESSIONS_INVARIANT_TRANSPORT_PRESEAL.md) targets original `gin-contrib/sessions` importing Gorilla original libraries, through genuine Gin middleware HTTP round-trip, with **the same six-entry expected matrix**. E3 is a distinct upstream wrapper implementation from a different organization, but retains the same underlying Gorilla/securecookie algorithms; its result cannot count as a wholly independent new cookie algorithm.

At E1/E2 initial inscription E3 native workflow was [#37985769868](https://github.com/WhoSia/EvoNOMOS/actions/runs/37985769868), **PENDING**. Update after readback, never invent a PASS.

**Verdict:** `P37_E1_ORIGINAL_TWO_GORILLA_MODULES_FULL_RACE_VET_PASS__P37_E2_64_RELATIONS_16384_PRODUCT_CASES_PASS__OWNER_INVARIANT_NONRECTANGULAR__DUAL_BRIDGE_CONDITIONAL_NATIVE_PASS__E3_TRANSFER_PENDING__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
