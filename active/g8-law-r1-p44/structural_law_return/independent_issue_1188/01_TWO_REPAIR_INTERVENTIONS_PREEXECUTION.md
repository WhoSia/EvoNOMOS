# Source-level intervention comparison for go-chi issue 1188 — freeze before patch execution

**2026-11-10 · EXACT original bug reproduced by native hosted Go CI #42763113563 before this treatment contract.** Previous original source inspection already identified a known missing slash branch in `tree.go`. This is not a blind maintainer or predictive source discovery.

## Common, prior source
go-chi/chi v5.1.0 at immutable `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`; original Go1.23.2. Exact old client and independent issue #1188 new demand both predeclared in `00_ORIGINAL_CHI_ISSUE1188_SOURCE_BASELINE_PRESEAL.md`. Baseline tested old PASS, new FAIL specifically `/re/a/b.json` returning HTTP200 `a/b`, whole upstream suite and vet PASS.

## Two actual source repair treatments
- Arm G / inline guard: change the existing `ntParam,ntRegexp` match path so every candidate parameter substring containing slash is discarded BEFORE matching regex. Keep original regex check; do not modify unrelated source.
- Arm H / helper extraction: introduce a separate top-level `validSingleSegment` helper and call it at the same matching boundary. This adds symbol and function wiring, while enforcing the SAME slash disallowance; the client behavior under the frozen oracle is identical if both succeed. This is an ordinary minimal-helper comparator, NOT an "interface" or entire architecture reformulation.
- Both paths must preserve the complete existing original Go suite including unrelated customers; run original source `go test -race -count=1 ./...` and `go vet ./...` if feasible. Must show changed source `tree.go` only, test added ephemeral, no upstream production write.
- Record AST symbol addition, touched production files, actual source behavior, and Go workload bounded benchmark if feasible. File touched alone cannot measure maintainer effort.

## Falsification and evidence rating
If one arm fails new/old tests or whole repo, do not declare it a valid repair. If both pass, conclude only that two app-authored source patches satisfy this **bounded customer oracle**, not that helper extraction is unnecessary for all future requirements, nor that source architecture has a causal long-term advantage. No real independent coding agents, human effort, new future unseen demand or full Go semantics proof. In particular, #1188 has been public and already discussed before these patches were written.

G1–G7 OPEN, LAW-R2 HOLD.
