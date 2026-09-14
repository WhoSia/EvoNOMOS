# EvoNOMOS repository policy

EvoNOMOS uses GitHub as the compact executable evidence layer for the current research lineage, not as a branch-per-stage archive.

## Main-first workflow

`main` is the canonical working branch. Routine research updates should go directly to `main` unless a genuinely risky refactor or destructive migration requires a temporary branch.

Do not create one branch per DIP stage, world-contact gate, provider check, experiment snapshot, or historical checkpoint. Temporary branches must be merged or discarded promptly.

Scientific freezes should be identified by commit SHA and, when useful, an immutable tag. Branches are not archival snapshots.

## Repository hygiene

Continuously remove superseded experiment harnesses, migration receipts, provider-specific gate branches, and historical execution scaffolding that are no longer required to replay or interpret the current active lineage.

Historical continuity belongs in Notion + Google Drive + Git history/tags. External repositories such as `WhoSia/Kodo-web` are world-contact substrates only and must not be used as EvoNOMOS archival branches.

Practical rule:

> If an old branch or artifact can be deleted without blocking reproduction or interpretation of the current EvoNOMOS lineage, retire it.

Audit branch and artifact hygiene at every generation or major phase transition.
