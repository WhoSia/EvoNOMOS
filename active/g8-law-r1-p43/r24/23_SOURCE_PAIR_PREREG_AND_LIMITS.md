# H24 source pair execution registration and disclosure limits

Pre-source-execution hypothesis: pinned Chi v5.1.0, registering GET only on /items/{id}, will not accept HEAD /items/alpha like stdlib ServeMux's GET route.

The basis was known from earlier R23 source-reading and subsequent GitHub blob readback; therefore the claim is *pre-execution* not blind to source semantics.

Raw candidate: Stdlib GET /items/{id}; Chi GET /items/{id} with corresponding URLParam. Controlled intervention: add a Chi HEAD /items/{id} route using application-owned adapter rights; do not modify upstream library bytes.

Broad diagnostic oracle: twelve GET/HEAD/POST/OPTIONS/PUT and percent-encoded path probes, logged individually. Matched oracle: six GET/HEAD and missing-path probes. In both use wire-level status/body/Allow/Location.

Observed native source result: NOT YET available (branch code and workflow are not substitutes for a SUCCESS execution receipt).
