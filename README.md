# EvoNOMOS

Canonical repository for executable conditional software-design law research.

## Current scientific head

**EvoNOMOS Generation VIII ORIGIN-R1-P11-P1 — Wide-Boundary Reuse↔Capability-Segregated Rival Constitution, Exa/Tavily Dual-Real-Demand Contract Freeze, Search/Fetch Exposure Oracle & Outcome-Blind Dual-Arm Materialization Preseal**

- Active evidence surface: `active/g8-origin-r1-p11-p1/`
- Exact world: `truefoundry/trueforge@dd421b79216c9b42eefd7b0191e546919f8be3f1`.
- Real demand pair remains frozen: #852 Exa search → #853 Tavily search.
- Rival constitution is now sealed:
  - `WIDE_BOUNDARY_REUSE`: preserve mandatory search+fetch boundary and truthful two-tool exposure.
  - `CAPABILITY_SEGREGATED`: minimally separate search/fetch capabilities; preserve Parallel search+fetch; Exa/Tavily search-only.
- Frozen two-phase lifecycle vector: `S/L/C/A/Q`.
- Independent Go provider-surface oracle validates Exa/Tavily search plus the conformance-only fetch/extract surfaces.
- GitHub Actions preseal run `36231088031` PASS.
- Treatment bytes: zero. Measurement firewall: closed. Outcomes: unopened. Winner: none.

## LawKit

`lawkit/` + `crates/evonomos-law/` form the executable theory and developer-tool layer.

Current protocol/tool surfaces:
- v0.1 — pre-outcome moderator inspection;
- v0.2 — authority-preserving lifecycle adjudication;
- v0.3 — fresh-world admission;
- exact-source GitHub provider-family adapter;
- provider-surface oracle v0.1 — deterministic Go mock HTTP oracle with demand-required vs conformance-only request classes.

LawKit does **not** encode SOLID, DIP, OCP, ISP or another design principle as an axiom. The protocol is canonical; implementation language is not.

## GitHub Actions policy

Actions is the read-only experimental substrate.

- workflows use `contents: read`;
- Actions may clone exact worlds, build, execute, reconstruct, audit, measure and upload artifacts;
- Actions does not commit experimental results back to this repository;
- raw logs are part of the measurement instrument and obey blindness/firewall rules;
- canonical code/theory changes are researcher-authored, not `github-actions[bot]`.

## Repository workflow

`main` is canonical. Keep only the live scientific lineage under `active/`; retired stages remain in Git history and Research OS.

The research target remains:

> under which observable architecture, demand and capability conditions does a design intervention change the sign of later engineering cost, conformance burden or validity?
