# External maintenance requirement court — Chi issue #825

Pre-execution source/task seal 2026-11-04, BEFORE new issue-specific Go code or test; publicly reported issue https://github.com/go-chi/chi/issues/825 "Duplicate Request ID if Use middleware several times" (opened 2023-06-08, open when read 2026-11-04). Reporter states nested RequestID middleware regenerates IDs in one request; proposed context check or header propagation. **This is independent external task motivation, but the reported outcome is known to the investigator and this is NOT a blinded predictive challenge.**

Pinned original source: github.com/go-chi/chi/v5@v5.1.0, maintained middleware/request_id.go blob SHA 4903ecc2144e186a74a25a3a4552cf9a74098ed6. Unmodified source generates an ID when request header X-Request-Id is absent; it does not consult an existing value in context. Two nested calls may therefore overwrite ID. Existing RequestIDHeader is read, not changed.

Baseline contract: with explicit X-Request-Id="user-7", intermediate observer and final handler must both see "user-7". Future external requirement: with header absent, when RequestID is applied twice, the ID observed after first middleware must equal the ID observed by final handler, not be regenerated. Check on both Chi.NewRouter and stdlib ServeMux under same original middleware composition, no upstream modifications.

Authorized app-only repair candidate: bridge middleware between duplicate RequestID calls; if request's context already contains a nonempty upstream RequestID, clone the request and its Header and populate the forwarded X-Request-Id, then invoke the second unmodified middleware. Preserve the request header contract for explicitly supplied ID. This is one named synthetic repair unit, not human maintenance time.

PREDICTIONS (not blind): under absent header, nested original middleware yields two nonempty differing IDs; under explicit header both equal user-7; with bridge under absent header IDs agree; both routers behave identically under the same middleware chain. Negative control: deliberately omit bridge. Tested response observer reads intermediate X-Outer-Request-ID and final returned body, not arbitrary randomness exact values. The source-local classic context+header dataflow analysis should make the same prediction; no EAC novelty.

Fail/stop if original source behaves differently. Do not treat a fixture as actual httplog implementation; do not claim the external issue is fixed upstream, or that we measured production costs.
