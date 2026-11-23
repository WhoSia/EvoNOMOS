# Actual maintained upstream source and permitted app interventions

Original source: github.com/go-chi/chi/v5@v5.1.0, file middleware/request_id.go, Git blob SHA 4903ecc2144e186a74a25a3a4552cf9a74098ed6 (read-only fetch 2026-11-04). Its middleware.RequestID uses context.WithValue(RequestIDKey,string) and r.WithContext(ctx), reading X-Request-Id when supplied and otherwise generating a process ID using atomic increment. Its GetReqID reads the string from context. We explicitly send the supplied X-Request-Id and do not modify the upstream mutable RequestIDHeader global.

The same original middleware.RequestID wraps both original standard ServeMux (Go 1.23.2) and chi.NewRouter. The state store, Capture middleware and handlers are the app-owned test fixture, not upstream Chi maintenance changes or previously published external patches.

Source provenance in GitHub module sum for Chi v5.1.0 expected h1:acVI1TYaD+hhedDJ3r54HyA6sExp3HfXq7QWEEY/xMw=. Native CI must independently confirm module hash, origin commit and Go version.
