# P37-E3 PRESEAL — Independent Gin Sessions Middleware Transports the Owner-Product Invariant Barrier

**2026-10-10 KST · prospective frozen predictions before new source test and native outcome · P37 OPEN.**

## Why this is an independent transport rather than another invented composite

Original `gin-contrib/sessions@12aa9f4b814f76844894f186ace4bd23b1ff29c0` (v1.0.4, Go 1.23) is an independently developed cross-organization middleware repository. It **already** imports `github.com/gorilla/sessions` in `cookie/cookie.go`, and its `NewStore` delegates to Gorilla's original `NewCookieStore`. Actual Gin HTTP handlers use `sessions.Sessions` middleware, `sessions.Default`, `Session.Set/Get/Save`, and the original Gorilla/securecookie chain. Exact external original `gorilla/sessions@bb4cd60c952a9ce48ea0dc6cc7b282ff79c38263` and `gorilla/securecookie@eae3c1840ec4adda88a4af683ad0f60bb690e7c2` from E1; the Gin-contrib repo has different organizational provenance, although dependencies overlap and **this is not an independent second underlying cookie-codec algorithm**.

We will CHECKOUT all three original source repositories and `go mod edit -replace` **inside temporary native CI working copies only** to bind Gin's existing imports to the E1 original pins. There are no changes to original library production source files. Frozen experiment code is ONE additional Go test file in the Gin original `cookie` package.

## Exact independent source-level transport contract

Using the ACTUAL original Gin router and Gin sessions middleware:
- issue a session cookie through `gin.New`, `sessions.Sessions`, `sessions.Default(c).Set` and `Save`;
- read via a separate Gin handler configured with the selected original `cookie.NewStore`;
- same two test-only old and new key labels, old historical cookie and new live cookie, same original plaintext semantic value `stage=kept`.

Frozen expected matrix from E1 **before native E3 result**:
```
writer old / reader old: live yes, old historical yes;
writer new / reader old: live no, historical yes;
writer old / reader new-only: live no, historical no;
writer old / reader dual(new,nil,old,nil): live yes, historical yes;
writer new / reader dual(new,nil,old,nil): live yes, historical yes;
writer new / reader new-only: live yes, historical no.
```
Read failure is an application-visible no-session result, not an exploitable rejection bypass. No production tokens or secrets involved. A single-owner staged rollout with B dual-compatible expansion first, then A writer change, is a feasible invariant-preserving path; a B contraction to new-only is NOT permitted while the old-cookie compatibility duty remains.

Record full modules' SHA, Go version, source-test SHA and native race/vet. This test is a **new application integration transport** over the same underlying codec semantics. It does NOT provide independent identification of a new mathematical law against classical multi-version deploy analysis.

Potential failure: the Gin adapter could impose extra context/registry/Set-Cookie semantics; preserve any such mismatch as an actual contextual obstruction, not patch Q23 or the pre-registered E3 expected matrix after seeing result. If it fails because of toolchain or upstream test unrelated issues, audit separately before judging E3.

**FROZEN:** `P37_E3_CROSS_ORGANIZATION_GIN_NATURAL_COMPOSITION_PRESEAL__ORIGINAL_GO_UNTESTED__P37_E1_CLASSICAL_TRANSFER_PREDICTION__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
