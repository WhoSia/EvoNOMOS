# P44 Structural-Law Return — Independent pflag Owner-Composition: Pre-execution Contract

**2026-11-09. PRE-TEST COMMIT; NOT prospective blind requirement prediction.** Original source has already been inspected. The purpose is to test P40's local-vs-joint observation obstruction on an independent non-router source and to challenge it with source-aware classical rivals. This is NOT F35 continuity and not a new law.

Original external library `github.com/spf13/pflag@v1.0.5`, Git tag commit `2e9d26c8c37aae03e3f9d4e90b7116f5accb7cab`; Go module go 1.12. Original source file `flag.go`: `AddFlag` panics on a duplicate normalized name, but `AddFlagSet` checks `Lookup` and silently skips a duplicate. The prediction is informed by that original source and MUST NOT be misrepresented as independently unseen future evidence.

### Frozen old-client and new demand
- Two app-owned plugin owners A and B each have separately created `pflag.FlagSet`. Initial old-client contract: parse `--tenant-a=alpha` and `--tenant-b=beta` with a combined app selector; correct independent values, and no panic. Both owner-local sets independently pass.
- New D1 collision: each owner additionally declares a local `channel` flag with independent values. The new customer requires A.channel=canary and B.channel=stable, concurrently in one app; the names and value independence are part of the semantics, NOT merely syntactic data formatting.
- Architecture S (SHARED-MERGE): combine both local owner FlagSets with `shared.AddFlagSet(a)`; `shared.AddFlagSet(b)`, parsing the combined CLI. Predicted original source behavior: A channel retained, B channel silently skipped, so local owner tests both PASS while joint D1 FAILS without an error. If the test independently observes absent shared second entry, it must show it.
- Architecture E (EXPLICIT-REGISTER): replay owner definitions with `shared.AddFlag` for every flag. Predicted D1 duplicate panic, NOT silent success. Catch panic in the test fixture for diagnosis; a production application may not safely recover.
- Architecture P (PREFIX-RENAME): construct a single app-owned `FlagSet` with distinct `a-channel` and `b-channel` names and independent storage; old and D1 PASS. This strong classical namespace adapter may fully explain the effect.
- Architecture I (OWNER-ISOLATED): retain separate owner-local FlagSets, independently parse their own arguments; both old and D1 PASS. No Go interface or SOLID norm needed.

### Falsifier and controls
1. Original source checksum/tag identity, `go.mod` and `go.sum` pinned; remote CI read-only Go1.23.2, `go mod verify`, native `go test -mod=readonly -count=1 ./...`, `go vet`, `go test -race`.
2. Old Q0 MUST pass for all four structures under old distinct names.
3. Owner-local D1 MUST pass for both owners, even if the joint shared merge fails.
4. Silent merge D1 MUST fail joint semantic equality without panic; explicit duplicate register must exhibit the original source panic. Diagnostic negative controls count as test PASS only when exactly these expected outcomes are asserted.
5. Prefix and isolated baselines must satisfy both independent values, or the science result FAILS.
6. Compare complete information rivals: basic normalized-name collision scan; explicit namespace prefixing; separated FlagSets. These **predict the outcome from original source**. If they tie, no scientific novelty upgrade.
7. App-owned integration code only. **No upstream edits, outside owner permissions, real maintainer labor, general long-horizon outcome, independent new issue or C5 inference**.

**Decision:** If predicted, classify as independent source replication of P40 local/global insufficiency plus a distinct silent-drop failure mode. Do NOT claim beyond-classical software design law. G1–G7 OPEN, LAW-R2 HOLD.
