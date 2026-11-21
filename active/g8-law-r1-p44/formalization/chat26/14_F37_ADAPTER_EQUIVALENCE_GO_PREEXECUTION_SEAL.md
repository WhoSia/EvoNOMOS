# Chat 26 — F37 Handler/Callback Adapter Court Pre-Execution Seal

**2026-11-21, before adapter test source.** This is a *supplementary classical equivalence/negative-control court*, not F38 independent future-demand evidence. Keep F37 baseline commit 4cc2fb302888ecbe72f6a683d97eff18378b261a unchanged.

## Target source and semantic limit

Use pinned original router module evonomos/f34-original-router-capability and the two F37 researcher-owned source-separate packages. Compare the standard Go transformations:
- Handler to function: h.ServeHTTP
- Function to handler: http.HandlerFunc(f)

No candidate will change upstream chi/httprouter source or modify either F37 arm.

## Predictions frozen before test writing

1. For finite queries on the existing F37 arms, wrapping a Handler into a callback then back with HandlerFunc preserves expected HTTP status, body and selected provider values.
2. Wrapping a callback as HandlerFunc then calling ServeHTTP similarly preserves those HTTP observations.
3. A handler implementing an *additional custom interface* loses that interface through HandlerFunc wrapping, even though HTTP outputs agree; this falsifies full contextual/type-level equivalence.
4. A typed nil pointer stored as a Handler interface can yield non-nil interface value; a nil function held as HandlerFunc can also yield non-nil Handler interface. **Do not invoke either**: the intended evidence is a type/nil boundary, not any panic.
5. The previous F37 original ten-probe baseline and Go race checks must continue to pass; a new isolated test does not alter earlier sealed predictions.
6. Strong classical Go method-set and interface semantics predict all behavior. Even success produces CLASSICAL TIE and F38 OPEN.

## Required run

Separate read-only GitHub CI with Go 1.23.2, original pinned dependencies, go mod verify, go vet and go test -race; preserve exact SHA and raw job logs. No Github Actions bot commits. Initial failure, if any, must be recorded rather than erased.
