# P44 F36 R3 — Native Original-Router Map-Aliasing Counterexample and Snapshot Rival (2026-11-21)

**Status:** BOUNDED SOURCE-AWARE NATIVE GO CI SUCCESS / NO NEW STRUCTURAL LAW / LAW-R2 HOLD / G1–G7 OPEN.

## Independently predeclared and executed

- Hypotheses, inputs and failure conditions frozen BEFORE code at [preseal commit bbab119e](https://github.com/WhoSia/EvoNOMOS/commit/bbab119e3834c2057c7242f5380aeed288f822f8).
- Separate implementation commit [7d80c512](https://github.com/WhoSia/EvoNOMOS/commit/7d80c51210ad50917f8a57dfa74e677100ae9be5) added `f36_selector_alias_test.go` to the existing app-owned module with two unchanged pinned original Go router libraries.
- [GitHub Actions run #44906785836](https://github.com/WhoSia/EvoNOMOS/actions/runs/44906785836) at exact tested SHA `7d80c51210ad50917f8a57dfa74e677100ae9be5`: **SUCCESS**. Job `136853966921` `native-original-routers`: dependency verification, `go vet -mod=readonly ./...`, native `go test -mod=readonly -count=1 -v ./...`, and `go test -mod=readonly -race -count=1 ./...` all SUCCESS.
- Raw job logs were read back: `TestF36SelectorMapAliasingAndSnapshotRival` PASS and its **three named subtests** PASS. Existing F35's eight named request subtests and six F34 top-level tests also PASS.

## What was actually observed under controlled source code

`Pick` (interface selector) and `independentCallbackPicker` (separately implemented function selector) both close over input Go maps and access their current entry per request. A **sequential, post-construction** map entry change from v1 to v2 caused `GET /item/x` to move from `v1:x` to `v2:x` without changing the selector functions or the original pinned router libraries. In both versions, `GET /legacy` continued to report `old`, so the old-client probe was insensitive to provider selection changes.

The new `snapshotCallbackPicker` independently copies the function map at construction and returns `v1:x` after the caller changes its original input map to v2. Thus **the source configuration ownership/copying rule**, rather than interface-vs-callback dispatch alone, controls this specific post-construction stability property. Neither source code nor tests require simultaneous map mutation; **no race or security vulnerability is claimed**.

| Declared observer / candidate | Mutable input map selector before change | After v1→v2 input-map change | Holds authored frozen-routing contract? |
|---|---|---|---|
| Interface selection `Pick` | `v1:x` | `v2:x` | No |
| Independently implemented live callback selector | `v1:x` | `v2:x` | No |
| Independent snapshot callback selector | `v1:x` | `v1:x` | Yes |
| Existing `GET /legacy` observer | `old` | `old` | Insufficient probe: cannot distinguish |

The “frozen-routing contract” is a **constructed comparison requirement**. The original app did not promise it to any documented third-party client. The result is a counterexample to overgeneralizing F35's bounded dispatch parity to configuration stability, **not proof of an actual developer defect**.

## Newly acquired primary-source priority boundary

- Jones (1981) Ch.4: environment rely and program guarantee conditions and compatibility; classical. The analogy to our test is *uncontrolled environment modification*, but the experiment does not mechanically extract Jones' proof obligations.
- Brookes (2004): local ownership and precise invariants enable scoped concurrent reasoning; classical. Our test is sequential and does not validate his concurrency semantics.
- Baldwin & Clark (2000) Chs.5 and 9–13: design operators, option values and tradeoffs are already theorized; not superseded by an app-level map copy.

See [F36 intake/custody original-reading note](./89_F36_00_THREE_ORIGINALS_CUSTODY_AND_SOURCE_PRIORITY.md).

## What this changes in P44 direction

Old-client **observer scope** is a separate proof obligation: old `/legacy` alone cannot observe changed provider selection. When a contract includes stable configuration under later map edits, a source-aware checker must trace mutable map aliasing and capture semantics or HOLD. This is a standard source/heap effect question with readily available classic alternatives (copy/snapshot/rely-guarantee/alias analysis).

**No prospective independent requirement, authenticated upstream modification authority, comprehensive Go source edit grammar, human repair cost, all-client contextual equivalence, or matched full-information baseline advantage was demonstrated.** Classical TIE is acceptable. G1–G7 and LAW-R2 stay OPEN/HOLD, PR #13 stays draft.
