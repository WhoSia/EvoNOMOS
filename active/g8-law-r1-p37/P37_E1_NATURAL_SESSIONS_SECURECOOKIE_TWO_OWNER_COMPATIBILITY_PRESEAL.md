# P37-E1 PRESEAL — Naturally Integrated Original Gorilla Sessions × Securecookie: Ownership-Split Compatibility and Invariant-Preserving Version Transitions

**2026-10-10 KST · frozen BEFORE E1 test file and native outcomes · P37 OPEN.**

## Why this target is stronger than project-authored composition

Two separately released, naturally integrated upstream Go repositories with original source:
- `gorilla/sessions@bb4cd60c952a9ce48ea0dc6cc7b282ff79c38263`: original `store.go` **already imports and invokes** securecookie to persist and read cookie-based sessions. Original `CookieStore.New` calls `securecookie.DecodeMulti`, and original `CookieStore.Save` calls `securecookie.EncodeMulti`.
- `gorilla/securecookie@eae3c1840ec4adda88a4af683ad0f60bb690e7c2`: original `securecookie.go` includes `CodecsFromPairs`, `EncodeMulti` (tries codecs in priority order) and `DecodeMulti` (tries all codecs for compatibility).
Both are Gorilla organizational ecosystem; they are **separate repositories and naturally integrated sources**, not evidence of totally independent maintainers or externally different organizational ownership.

This is a **configuration/release authority** experiment on unmodified original production source. Owner A controls the currently emitting `CookieStore` instance in one deployed service; owner B controls the consuming `CookieStore` instance in another deployment. These are *hypothetical deployment owners/roles over genuine library APIs*, NOT documented separate human maintainers of the upstream modules. Original software-level structural transfer is verified via real Go execution.

## Identical frozen functional observables and invariants

Toy fixture uses two arbitrary different in-test authentication keys, no production secrets, no live service and no security assurance claim. `W0/W1` = current cookie issue using old/new key only. `R0/R1` = read using old/new key only. `R*` = read with both new and old keys using correct original API `NewCookieStore(newKey,nil,oldKey,nil)`. Note: `CodecsFromPairs` consumes (hash, optional block) pairs, so `NewCookieStore(newKey,oldKey)` would mean **one codec**, not two; forbid this as an incorrect control.

Use the original session API to issue a cookie through `store.New(...)`, `Session.Values`, `store.Save(...)`, and verify decode via `reader.New(...)`, session value and `IsNew`.

Two scoped invariants:
- `I_live(W,R)`: decoder R accepts a fresh legitimate cookie from current writer W (same session name and payload), not a claim about attacker-created/tampered cookies.
- `I_legacy(W,R)`: during the declared migration window R also accepts a previously issued unexpired old-key cookie `oldCookie`.
For current-stage maintenance require BOTH. Starting W0/R0 satisfies both; R1 alone cannot decode old cookie; W1 with R0 cannot decode new cookie; W1/R* must decode both. Target of declared **legacy-preserving migration** is W1/R*, not W1/R1 while legacy window remains active.

Frozen matrix:
| writer | reader | I_live | I_legacy | checkpoint |
| W0 | R0 | true | true | initial |
| W1 | R0 | false | true | forbidden A-first |
| W0 | R1 | false | false | forbidden direct B-only switch |
| W0 | R* | true | true | permissible B expansion |
| W1 | R* | true | true | permissible A switch |
| W1 | R1 | true | false | only permitted after explicit legacy obligation expiry |

Pre-registered sequential paths:
- NO BRIDGE, edits W0→W1 or R0→R1, both checkpoint obligations enforced: all paths to W1/R1 encounter forbidden intermediate and final violates legacy; even when legacy later expires, no safe binary path.
- WITH B expansion `R0→R*`, then A change `W0→W1`: all checkpoints satisfy both obligations. A final contraction `R*→R1` cannot be declared safe until old-cookie obligation is explicitly lifted and tested.
- A single jointly authorized atomic W/R change bypasses intermediate but is a different Γ, not evidence one-owner rollout is possible.

Native gate: checkout two exact original source commits to separate trees, optional local `go mod replace` only for test routing to pinned securecookie tree, record source SHA and module version, add **one frozen test file only** to original sessions module. Go vet, full original Go race suite for sessions and securecookie, frozen experiment tests PASS; archive native receipts. If the actual native result differs from this preseal, preserve it and diagnose, **do not amend the frozen expected semantics**.

## Strong prior that predicts this

Original source already advertises multi-codec key rotation and strong classical expand-and-contract/version-skew theory predicts a compatibility bridge; the result cannot identify a new law. In particular, SREcon 2026 *Escaping Version Skew: Formalizing Compatibility in a World of Partial Rollouts* is a relevant classical competitor, not novelty evidence.

**PRESEAL:** `P37_E1_ORIGINAL_NATURAL_TWO_REPO_COMPATIBILITY_TEST_FROZEN__LOCAL_BOTH_POSSIBLE_GLOBAL_NO_BRIDGE_PATH_BLOCKED__DUAL_READER_BRIDGE_PREDICTED__DIP49_IDENTIFICATION_HOLD`.
