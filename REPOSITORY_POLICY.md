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

## Canonical research-document ownership (2026-11-23)

- **Notion is the canonical authoring and meaning layer** for manuscripts, paper drafts, LIRA sentence-level edit ledgers, RAVEL/COURT decisions, research interpretations, mathematical notes, and historical phase records. [EvoNOMOS workspace](https://app.notion.com/p/3c4ef561cf9281e69e1cf0dbf1239bbb) and [historical Markdown migration collection](https://app.notion.com/p/421ef561cf928167aa1fc101494d0caf) hold the material retired from `active/`.
- **Google Drive is the canonical original-byte/evidence shelf** for acquired papers, historical archives and binary research source documents.
- **GitHub is the executable/reproducible layer** for source code, CI configurations, tests, developer README files, operational protocol contracts, and references necessary to run/rebuild the experiments. Prose papers, editorial drafts and stand-alone research decisions should not be newly written into GitHub as duplicate Markdown.
- On 2026-11-23, 254 narrative `.md` files from `active/` were moved to individually verified Notion pages and removed from the `main` working tree; original Git commits remain queryable. Existing historical links to those paths in older README narratives refer to Git history, **not** live main-branch canonical files. Future updates should point to Notion pages directly.
- Never retire an executable contract, code/config asset or CI-consumed file without checking dependencies. GitHub deletions or updates must show `WhoSia` as both author and committer, never `github-actions[bot]`.
