# Source and module custody

Native CI should execute with Go 1.23.2 Linux amd64; require exact go-chi/chi/v5 v5.1.0 module. Prior independently verified P44-R1 Go module checksum:
h1:acVI1TYaD+hhedDJ3r54HyA6sExp3HfXq7QWEEY/xMw=
go.mod checksum:
h1:DslCQbL2OYiznFReuXYUmQ2hGd1aDpCnlMNITLSKoi8=.

New P44-R2 module verifies the same dependency through `go mod download -json`, `go mod verify`, `go list -m -json all` during its own workflow. Prior checksums are expected values, not replacement evidence of new CI.

Main research outcome requires original pinned source execution receipts, including stdout per stage, exact HEAD/method/body semantics, source code revision and GitHub job ID. No new source test is called PASS before successful independent CI readback.
