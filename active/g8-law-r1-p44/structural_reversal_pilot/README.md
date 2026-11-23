# F33 Structural Reversal Pilot — Strong-Rival Negative Control

This is **researcher-generated native Go source**, not independent upstream evidence or a new software design law.

## Reproduce

Requires Python 3 and Go 1.23.2:

```sh
python3 generate.py
python3 evaluate.py
```

The generator creates 12 compilable Go modules under `snapshots/`, with three architectures (duplicated DIRECT, interface PORT, private-helper DIRECT_REFACTORED), crossed with provider replacement and new `Mode()` demand switches. The evaluator runs `go test -count=1 ./...`, `go vet ./...` and `go test -race -count=1 ./...` in every module. It counts Go source line insertions/deletions and changed files against the same architecture's unchanged baseline; tests are excluded from the change-footprint metric.

| Metric | DIRECT | PORT | DIRECT_REFACTORED |
|---|---:|---:|---:|
| Initial source LOC | 5 | 13 | 6 |
| Replacement change lines (+/-) | 6 | 2 | 2 |
| Mode addition changed lines | 1 | 3 | 1 |
| Mode addition changed files | 1 | 3 | 1 |

All **12 modules / 36 Go commands passed locally** on 2026-11-09. These do not measure human time, all-client safety, independent permission, or real issue prediction.

**Important pre-registration boundary:** the initial 8 DIRECT+PORT snapshots and expected comparisons were declared before the first local execution in `preseal_initial_8.json`. DIRECT_REFACTORED is a **post-hoc** stronger rival introduced specifically because duplicated provider literals could explain the apparent PORT advantage. This rival removes the replacement advantage, so the initial attribution to DIP was confounded.

The original locally produced ZIP of the source snapshots and complete run logs was 19,303 bytes with SHA-256 `561979a701d7e1fa2f4c7474e0d01bccb0c5b344c17913cc6e75eb7a9e66a81b`. This repository stores the **byte-identical generator and evaluator** (Git blob SHA compared to their tested local files), not the generated ZIP. Re-run rather than treating old local logs as fresh CI.

Research narrative: [83_F33_STRUCTURAL_REVERSAL_STRONG_RIVAL_NEGATIVE_CONTROL](../formalization/83_F33_STRUCTURAL_REVERSAL_STRONG_RIVAL_NEGATIVE_CONTROL.md). G1-G7 OPEN / LAW-R2 HOLD.
