# EvoNOMOS Generation VIII ORIGIN-R1-P12-P2

**OCI Phase-0 Independent Full-Backend Reuse↔Capability-Composed Dual-Arm Materialization, Mandatory-Capability Oracle, Exact-Custody & Pre-Reveal Comparability Gate**

Status: `EXECUTION_ACTIVE / OCI_PHASE0_ONLY / OUTCOMES_CLOSED`

Inherited authority:
- Restic exact donor: `495982232cf1af184eac0a97871ef8161e8708ee`
- OCI real demand: restic/restic#4517
- OneDrive follow-up: restic/restic#5301 — frozen, unopened
- public `restic.Backend` invariant
- mandatory core: `Save / Load / Stat / List / Remove / Delete`
- lifecycle vector `Y=(S,L,C,A,Q)` remains sealed

P2 is allowed to materialize and execute the OCI phase-0 pair, but it is **not** allowed to compute, print, rank, or infer S/L/C/A/Q coordinates.

Rivals:
- `FULL_BACKEND_REUSE`: one complete OCI backend owns all mandatory operations.
- `CAPABILITY_COMPOSED_BACKEND`: the same public Backend is implemented by an adapter whose mandatory operations are internally owned by separate capability objects.

Both arms use the same pre-demand OCI Go SDK version `v65.50.0` (released before the donor and demand), the same SDK-typed client seam, the same config/layout semantics, and the same byte-identical no-network oracle.
