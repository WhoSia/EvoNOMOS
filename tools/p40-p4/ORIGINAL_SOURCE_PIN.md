# Original dependency pin for independent source-level trial

- Maintained repo: https://github.com/go-chi/chi
- Complete exact source commit: `167e1e3bd039d060696b99c8da4e876ae04f42c1` (2026-09-29)
- Inspected at this SHA: `chi.go` (`Router` embeds `http.Handler`, `Routes`; `Mount`, `Use`), `mux.go` (`Mux.Mount` duplicate mount detection; `Mux.Use` before-route guard), `tree.go` (route matching), `go.mod` (Go 1.24 requirement)
- Go test harness operates with `go.mod` local replacement `./original-chi`, checked out by CI from exact SHA; there is no copied or locally modified third-party source in EvoNOMOS.
- Proof scope: particular static mount namespaces `/service/a,b,c`, old request `/old`, child `/item`, and middleware call order. This is not exhaustive proof of all Go chi patterns/middleware/client contexts.
- No claims of maintainer permissions, deployment regressions, PR viability, CVE, or source patch acceptance. Original modules held read-only.
