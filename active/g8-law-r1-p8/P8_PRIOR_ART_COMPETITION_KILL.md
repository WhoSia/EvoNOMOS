# LAW-R1-P8 — Multi-Motif Prior-Art Competition Kill

## Motif A — semantic-authority convergence

Inherited from P7.

Observed shape:
multiple independently editable paths encode or mutate the same semantic fact, producing drift or reconciliation burden.

Prior-art collision:
single-source-of-truth and clone-maintenance literature already own the generic idea that duplicated semantic authority can drift, while clone evolution also blocks a universal deduplicate-everything rule.

P8 status:
**ABSORBED / NOT NOVEL.**

## Motif B — invariant closure across failure

Discovery worlds:
- G9MaGiC/park#10
- G9MaGiC/park#34
- Jcrad006/pharmacy1os#38

Fresh discriminator:
- stacksjs/stacks#1876
- exact implementation commits:
  - d9bd2ac58b19597a6feffde07b99cf2493628ee1 — Stripe idempotency keys
  - 41fb37f6bc536e73bd5fcd1a24ac3d0767079e1b — transactional audit opt-in

Observed moderator geometry:
- when invariant-coupled durable facts share one transactional substrate, use one commit/rollback boundary;
- when a remote effect cannot share the transaction, preserve closure through retry-safe/idempotent/compensating/reconciliation mechanisms instead of pretending the remote effect is atomic with the database;
- adjacent effects that are not part of the validity invariant stay outside the closure boundary.

Prior-art collision:
ACID atomicity, transactional outbox, saga, idempotent consumer/operation, and distributed consistency patterns already own these mechanisms and their substrate dependence.

P8 status:
**ABSORB_EXISTING_FAMILY__SUBSTRATE_MODERATOR_EXPLICIT.**

## Motif C — operational-authority scope partitioning

Discovery world:
- linuxarena/control-tower#2006

Negative/limit evidence inside the same world:
- per-instance fleet secrets are narrowed to the instance;
- documented Docker-org parameters remain intentionally shared.

Fresh unresolved composition world:
- NousResearch/hermes-agent#108671

The Hermes RFC explicitly separates:
1. credential authority — local vs canonical shared store;
2. inheritance permission;
3. selected pool capability.

It asks for one shared canonical credential truth where necessary, while restricting which profiles may read, refresh, select or mutate entries.

Prior-art collision:
NIST least privilege, AWS IAM least-privilege guidance, and the bulkhead/fault-isolation pattern already own generic scope minimization and failure-domain isolation.

P8 status:
**ABSORB_EXISTING_FAMILY__FAILURE_DOMAIN_MODERATOR_EXPLICIT.**

## Competition result

The three motifs are not true alternatives over one variable.

They manipulate different coordinates:

- **S — semantic-authority cardinality:** how many independently editable owners exist for one semantic fact?
- **P — operational-authority scope:** which principals/failure domains may exercise a capability or access an authority?
- **F — invariant-closure boundary:** which state/effect transitions must settle together, and by what substrate-specific mechanism?

Apparent contradictions such as "centralize vs partition" arise when S and P are conflated.

A system may validly:
- centralize semantic truth (low S),
- partition operational capability by principal/failure domain (narrow P),
- and close invariant-coupled effects atomically or compensatorily (F determined by substrate).

Hermes #108671 is a direct composition demand: shared canonical credential authority plus profile-scoped access.

## Novelty ceiling

The component generators are not novel.

The only remaining EvoNOMOS candidate is the **empirical moderator geometry and authority-update process** that decides which coordinate a structural intervention is actually changing, then permits APPLY / ABSTAIN / REVOKE / UNRESOLVED without collapsing the coordinates into a universal maxim.

Status:
**COMPOSITION_REPRESENTATION_CANDIDATE__NOVELTY_WITHHELD.**
