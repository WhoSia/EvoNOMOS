# P37-E3 — Native Cross-Organization Natural Gin/Gorilla Sessions Transport Court

**2026-10-10 KST · POST-NATIVE READBACK · P37 OPEN · DIP49 IDENTIFICATION_HOLD · LAW-R2_NOT_AUTHORIZED**

## Prospective chronology, independent ecology and source ownership

The [E3 prospective preseal](P37_E3_CROSS_ORGANIZATION_GIN_SESSIONS_INVARIANT_TRANSPORT_PRESEAL.md) committed **before** the [frozen original Gin cookie test](../../tools/p37-e3/tests/gin-contrib-cookie/p37_e3_original_transport_test.go) and CI. It froze the exact E1 six-case compatibility matrix in a different, independently authored upstream Gin middleware wrapper.

All actual original production code was sourced from:
1. **`gin-contrib/sessions@12aa9f4b814f76844894f186ace4bd23b1ff29c0`** (v1.0.4, separate Gin-contrib organization), original `cookie/cookie.go` already invokes `github.com/gorilla/sessions.NewCookieStore`, and actual `sessions.Sessions` middleware owns context/registry.
2. **`gorilla/sessions@bb4cd60c952a9ce48ea0dc6cc7b282ff79c38263`** (Gorilla).
3. **`gorilla/securecookie@eae3c1840ec4adda88a4af683ad0f60bb690e7c2`** (Gorilla).

These are **three original source repositories and natural existing import edges**; no researcher-authored production glue or upstream production source changes were used. A research-authored test was copied into the original Gin `cookie` package. Local `go.mod` temporary replacements routed Gin's actual dependency imports to exact pinned original Gorilla module checkouts, so module metadata changed **only in the CI checkout**; actual source files did not.

**Independence qualification:** Gin-contrib is a separate organization and uses its own HTTP wrapper and contexts; however, E3 and E1 deliberately share the **exact same Gorilla cookie-codec implementation**. This is **an independently developed downstream integration transport**, NOT a second independent cryptographic algorithm or fully independent mechanism. Do not count the six Gin test subcases as six independent source-ecosystem discoveries or as a statistical holdout for a new law.

## Original Gin HTTP call paths and exact independent functional result

Frozen one-file test uses original Gin `gin.New`, original Gin-contrib `sessions.Sessions` and `sessions.Default(c).Set/Get/Save`, original `gin-contrib/sessions/cookie.NewStore`, and transitively the original Gorilla `CookieStore` / Securecookie codec:
- old writer → old reader: live/legacy PASS/PASS;
- new writer → old reader: FAIL/PASS;
- old writer → new reader: FAIL/FAIL;
- old writer → dual reader: PASS/PASS;
- new writer → dual reader: PASS/PASS;
- new writer → new reader: PASS/FAIL.
Both issuance and reads pass through **actual separate Gin HTTP handlers** using `httptest`, not direct encoder stubs.

[Native original Gin cross-organization CI #37985769868](https://github.com/WhoSia/EvoNOMOS/actions/runs/37985769868) completed **SUCCESS (1/1)**, `go1.23.12 linux/amd64`. Original pinned `cookie` package frozen Go test under `-race` passed **all six** originally presealed subcases and original cookie-package `go vet` PASS. **This workflow did not run the full gin-contrib upstream multi-backend test suite or repeat Gorilla full-race suite**; original E1 already did full Go/race/vet on Gorilla sessions and securecookie modules. No claim broader Gin modules or Redis/SQL/Mongo external backends were tested.

Artifact **11643175912**, ZIP sha256 **`dc9b6d85eef7be0802887cbed79ecbcff9a0118a490aa86f8e8aff01c52e3f6c`** (verified by direct ZIP inspection); contains exact 3 original SHA pins, per-file source/test sha256, recorded module list, original Gin test-race log, vet log, and PASS verdict. The original Gin checkout only shows `go.mod` modified (CI-local replace) and the one untracked frozen research test file.

## Structural inference and strong competing theories

Three source repositories now exhibit one naturally integrated **composed compatibility contract** at different layers. Source A emission version and source B reader acceptance are not independent local safety predicates: global compatibility is **nonrectangular**, and independently permitted version changes can have no safe sequential path while a dual-version reader can provide a bridge. Whether that bridge remains permissible depends on **declared persistence of historical obligations**. The actual source APIs already advertise dual codecs / key rotation; strong classical assume–guarantee contracts and expand/contract upgrade theory predict the observed sign pattern.

Compared to E1, E3 adds **original independent Gin HTTP middleware context and different organizational provenance**—valuable transport—but not a different underlying codec algorithm and not a differing (H_*) vs strongest-classical (B_*) prediction. [MATH-E](P37_MATH_E_OWNER_PRODUCT_INVARIANT_BARRIERS_AND_BRIDGE_THEOREMS.md) and [MATH-F](P37_MATH_F_RECTANGULAR_INVARIANTS_AND_LOCAL_GLOBAL_REPAIR_FACTORIZATION.md) remain classical exact theorems.

**Verdict:** `P37_E3_CROSS_ORGANIZATION_NATURAL_ORIGINAL_GIN_GORILLA_SOURCE_RACE_VET_PASS__ALL_SIX_FROZEN_STATES_MATCH__NO_NEW_INDEPENDENT_CODEC_ALGORITHM__DIP49_NEW_LAW_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
