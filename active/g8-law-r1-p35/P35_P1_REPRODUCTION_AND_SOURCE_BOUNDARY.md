# P35-P1 — Authentic Restic Validation and Source-Claim Boundary

**2026-10-09. Updated status:** `PINNED_UPSTREAM_RESTIC_P35_PACKAGE_PASS__EIGHT_WORLDS__BASELINE_NEGATIVE_CONTROLS_PASS__FULL_RESTIC_SUITE_NOT_RUN__LAW_R2_NOT_AUTHORIZED`. Prior local DNS failure remains a historical environment attempt, superseded by [Actions #37895607800](https://github.com/WhoSia/EvoNOMOS/actions/runs/37895607800).

## Why this document exists

The research assistant produced a local **P35-P0/P1 Go source and evidence bundle** separately from GitHub. That bundle's `fixture/internal/restic/restic.go` is a deliberately synthetic API shim; its module path merely permits testing imports of `github.com/restic/restic/internal/restic`. Local compilation does **not** prove that the exact upstream Restic source accepted these adapters.

The upstream target is official `restic/restic` at commit `495982232cf1af184eac0a97871ef8161e8708ee`, interface `internal/restic/backend.go` (12 public methods). P34's independent hosted confirmation does not automatically validate P35.

## Executable original-source protocol

Use a machine or read-only CI runner with Go and a real network. Do **not** run GitHub Actions as a repository writer.

```bash
set -euo pipefail
git clone https://github.com/restic/restic.git restic-p35-upstream
cd restic-p35-upstream
git checkout 495982232cf1af184eac0a97871ef8161e8708ee
test "$(git rev-parse HEAD)" = "495982232cf1af184eac0a97871ef8161e8708ee"
mkdir -p internal/p35pair
# From the independently retained P35-P1 source bundle:
cp /path/to/P35-BUNDLE/sources/baseline/*.go internal/p35pair/
# Repeat for each source world; replace all .go files on every iteration.
go test -race -count=1 ./internal/p35pair
go vet ./internal/p35pair
```

Run all source worlds: `baseline`, `u-local`, `c-local`, `u-encoded`, `c-encoded`, `c-encoded-tagged`. Each needs the same `go test` command but the new-demand negative controls must be selected separately: unchanged baseline **must fail** `LocalKeyFile` and `VersionedStorage`; modified worlds should only be declared PASS for the demand actually implemented. Ordinary tests and the 18-call public history must pass. Test callbacks, context cancellation, missing object, partial read, List ordering, replacement, physical separation and legacy bytes beginning with the new encoding prefix. The decoder must not infer version from untrusted payload prefix alone.

Capture in artifacts: pinned SHA, `go version`, dependency resolution, `go test -race`, `go vet`, suite output, process exit codes, exact source patches against immutable P0, source-method AST diff and byte hashes. If Go version changes or upstream Restic source differs, call it a different replication.

## Current bounded evidence

- **Local** Go 1.23.2 portable shim runner: baseline ordinary tests PASS; five local edited implementations PASS their selected demands; untouched baseline two expected negative requirements FAIL.
- **P34 behavior replay:** 18 public action history for original semantics. Unlike P34, adapter-to-unit dispatch counts are not compared because the architectures no longer share that topology.
- **Actual source patches:** local-only `KeyFile` demand: one modified method in each arm. Encoded-storage demand: 2 modified existing methods in U; 6 in C with separate version map, 5 in C with tagged payload, and 4 in C when the payload store decodes tagged values internally. All are realized patches, **not inclusion-minimal admissible repair families**.
- **Actual native upstream:** [Actions #37895607800](https://github.com/WhoSia/EvoNOMOS/actions/runs/37895607800) **SUCCESS** at original pinned Restic commit, Go 1.23.12, all eight source worlds package `go vet` and `go test -race` PASS; 18/18 P34 public history each; both negative controls expected-fail. Artifact **11599942843**, SHA-256 **49d38c9c60a7415c9b9395cb7c52db5e33cdf25e55297de6888d5f52fa89f85b**. Earlier local `git clone` exit-40 DNS block is a preserved historical attempt, not a current hosted blocker. Full upstream Restic suite not tested.

## Source-aware rival / identification

A Go-AST field/selector/call conservative reachability baseline proposed 6 U methods and 12 C methods for the encoded change and covered the observed edits in both arms. This is an imperfect **B0+ candidate set**, not a mature CSDG or whole-program change impact analysis. Comparison at equal oracle/source information gives coverage, not a win for a bespoke EvoNOMOS hypothesis. B1 historical co-change needs real history, not synthetic local patches. B2 Parnas/Design Rule Spaces/CSDG and conventional program-repair workflows are substantive existing alternatives.

Let `R_A(d;T,G)` be admissible repairs under architecture A, requirement d, behavior oracle T and allowed patch grammar G. An observed patch `r ∈ R_A` has change support `S_A(r)`. The 6→5 C-method reduction after changing version placement proves that **single-witness edit support is representation- and strategy-dependent**; it is no proof that `min |S_U| < min |S_C|` across all legal repair strategies.

For old arbitrary bytes `S_0(x)=x` and new format `S_1(y)=E(y)`, overlapping ranges with `x≠y` cannot be decoded correctly by a single function that receives only the bytes. Version distinguishing information or a strict state restriction is necessary. Classical factorization/information sufficiency, **not** a novel theorem.

## Verdict discipline

`P35-P1 LOCAL TEST PASS` and bounded `P35-P2 PINNED RESTIC PACKAGE PASS` are now valid. `P35 CLOSED`, `LAW-R2`, a whole-upstream Restic suite success, architecture-wide Pareto rank, minimal global repair family and predictive superiority over B0+/B1/B2 remain **HOLD**. If competing repair grammars cannot be distinguished using the required evidence, record nonidentifiability and move to a genuinely new demand/world. Do not introduce another governance theory to rescue the phase.

Authorship: no workflow may commit to the repository, including with `GITHUB_TOKEN`. Human-account-author and committer evidence is required for promoting this text or executable source.
