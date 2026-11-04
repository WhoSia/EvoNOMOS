# Reproduction instruction and evidence levels

Local formal test, no network or Chi dependency:
cd active/g8-law-r1-p44/r2/formal
go version
go test -count=1 -v ./...
go vet ./...
go test -count=1 -race ./...

Original source paired test (requires pinned external module):
cd active/g8-law-r1-p44/r2
go mod download -json github.com/go-chi/chi/v5@v5.1.0
go mod verify
go list -m -json all
go test -count=1 -v ./...
go vet ./...
go test -count=1 -race ./...

The original source court must capture raw module checksum, run ID, commit SHA, per-stage trace and actual exit statuses. Expected code is not a substitute for an executed CI receipt; update this file with a dated append-only verdict after inspection.

Known previous-source native P44-R1 reference CI run 41756947113 SUCCESS; it did not exercise the R2 future requirements.
