# LAW-R1-P9 — Temporal/Evolution Prior-Art Kill and Geometry Sufficiency Ruling

## Attack target

P8 promoted a bounded structural representation:

`G = (S, P, F)`

- S = semantic-authority cardinality
- P = operational-authority scope
- F = invariant/failure closure

P9 asks whether G is a sufficient decision state, not merely whether it is a useful structural projection.

## Development evidence

### Version / release-state donors

- farming-labs/farm.js#1625 — tightly coupled packages at mismatched versions fail; repair aligns the package epoch.
- linuxarena/control-tower#1924 — a released runner talking to a moving latest sidecar fails after protocol evolution; repair pins the sidecar to the submitting release.
- openclaw/openclaw#163087 — a co-shipped UI/Gateway contract permits obsolete compatibility fallbacks to be removed.
- Armadillon44/shotAI#106 — staggered rollout / rollback across builds requires preserving unknown schema state rather than destroying it.

These worlds can have similar S/P/F structure while requiring different compatibility actions because release coupling and coexistence horizon differ.

### Ordering / replay donors

- vanyastaff/nebula#1136 — correctness depends on happens-before, concurrency, iteration frontier and replay position.
- rishu605/bulk-price-editor#897 — a delayed ACTIVE event cannot be classified from payload order alone; the repair asks the provider for current authoritative active state before replacing local state.

These are temporal, but they are not reducible to the same intervention as version alignment.

## Fresh holdout

home-assistant/core#181879 was frozen before resolution was revealed.

Precommit:
`active/g8-law-r1-p9/P9_HOLDOUT_HA181879_PRECOMMIT.json`

Observed resolution:
- the integration genuinely requires the newer public API;
- the minimum version remains;
- the affected console was in a broken package-repository state;
- once updated to a supported version, the integration worked again.

This supports the branch where capability/version state is decisive without any S/P/F structural change.

## Prior-art collision

The temporal/evolution family is not novel.

Existing research already owns major components:

1. API evolution and deprecation research studies compatibility-preserving migration and how clients react to evolving APIs.
2. Component-compatibility work explicitly models configurations containing multiple active component versions.
3. Empirical microservice API-evolution research identifies backward compatibility, versioning, collaboration, consumer lock-in and outdated-version dependence as central evolution problems.
4. Version-skew work for partial rollouts treats mixed-version compatibility as a first-class distributed-systems correctness problem.
5. Temporal-rule mining and replay/order research already treats event order and temporal invariants as program semantics.

Therefore P9 may not claim invention of a temporal design axis.

## Representation ruling candidate

P9 currently distinguishes two questions that P8 left implicit:

### Structural geometry
`G = (S,P,F)`

What structural coordinate does an intervention alter?

### Decision context
`X`

Under what environment, lifecycle, compatibility, ordering and capability state should that intervention be selected?

Temporal/evolution variables belong in a moderator family:

`X_T = (release_coupling, version_coexistence_horizon, mixed_version_overlap, capability_epoch, event_order_contract, replay/current-state relation)`

The evidence does **not** justify collapsing X_T into one fourth structural axis.

## Alias result

A co-shipped system can safely retire obsolete compatibility support while a staggered/rollback-coexistent system may need unknown-state preservation, even when their S/P/F structural geometry is materially similar.

Thus:

`same G != same action`

unless relevant context X is also supplied.

This falsifies **G as a sufficient policy state**, not G as a bounded structural coordinate system.

## Ontology consequence

Candidate update:

`Pi : (X, G, E) -> {TEST(a), ABSTAIN, REVOKE, UNRESOLVED}`

where E is the available empirical evidence/world-contact state.

No fourth structural axis is promoted.

Status candidate:

`THREE_AXIS_STRUCTURAL_GEOMETRY_SURVIVES__POLICY_STATE_INSUFFICIENT__TEMPORAL_MODERATOR_FAMILY_PROMOTED__ONTOLOGY_AXIS_EXPANSION_WITHHELD`
