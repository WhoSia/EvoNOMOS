# P44 R7 — Same New Application Policy, Both Frozen F37 Go Arms

**Prospective within this author's own fixture, not a genuine independent F38 external task.** This is a *classical equal-information rival*, inspired by the prior Chi #1035 static/param path ambiguity but NOT claimed to reproduce that original Chi issue in the F37 routes.

## Prediction before writing test

Both previously frozen independently developed arms implement `GET /item/{id}` or `GET /item/:id` and `GET /legacy`; neither defines reserved policy for GET `/item/me`.

New *researcher-authored* requirement: GET `/item/me` must fail with 403 (reserved identifier), while existing GET `/item/a` and GET `/legacy` retain their exact outputs. App-owned **outer HTTP filter** wrapping each arm can satisfy this without changing either arm's code. Implement the filter identically as a function receiving `http.Handler`, compare 8 input requests including unknown-provider errors and two versions, and retain original plain-arm baseline where /item/me still works.

**Prediction:** a shared ordinary HTTP wrapper meets this requirement for **both** Handler and callback arms; neither has an intrinsic structural edge for this scoped demand. No blind unseen demand, no measured human engineer cost, no library-level path-precedence repair, and no claim that this is a general semantic solution to reserved route names.

CI: Go mod verify, vet, full original test, race; source arms untouched; failure retained. Distinct from the previous typed-adapter marker test.
