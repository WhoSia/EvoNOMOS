# Newly exposed observer boundary — 2026-11-04

A second execution gate found that handler-level httptest.ResponseRecorder is **not interchangeable** with the HTTP client-observed wire semantics, especially for HEAD body behavior.

In the local standard ServeMux fixture, the application handler writes a body to the recorder even on HEAD while an actual net/http client receives zero response-body bytes. Both yield status 200.

A new WireObserve function uses httptest.NewServer, a real http.Client, redirects disabled, and reads the transmitted response. New negative/positive tests assert the difference and verify GET, HEAD, POST and encoded slash status/body.

All local go test, vet and race checks passed after the change. This is a *more precise observer distinction*, not a Chi native source-pair result.

Scientific implication: freeze the layer of observation (handler invocation vs protocol client) before claiming contextual equivalence. HTTP client baseline must use the wire oracle; handler-side effects can be an explicitly separate probe.
