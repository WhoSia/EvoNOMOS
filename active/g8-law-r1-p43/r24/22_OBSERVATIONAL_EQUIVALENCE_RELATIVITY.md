# Equivalence is relative to observer and execution layer

For programs A and B, A ~_O B iff every observation in declared O is identical. If O is restricted to GET /items/alpha, this does not imply equality on HEAD, POST, URL escaping, redirects, dynamic content, concurrent interleavings, or client-visible bytes.

Further distinguish:
1. handler-level httptest.ResponseRecorder reports application writes;
2. real client-visible HTTP behavior under httptest.NewServer may elide HEAD response body;
3. timing/concurrency and middleware history are not in either finite oracle by default.

Original Chi v5.1.0 tree.go has distinct mGET/mHEAD method bits. Its mux.go routeHTTP uses methodMap and FindRoute; an unmatched method can yield a method-not-allowed handler. This is source-reading evidence, pending original Chi native test.

R24 paired code preserves broad exploratory probes as log-only, while the proposed matched baseline is just six explicitly listed GET/HEAD and missing-path probes. This is a scoped equivalence hypothesis until CI runs; never call it all-HTTP observational equivalence.
