# EvoNOMOS Generation VIII ORIGIN-R1-P8

**Capability-Absence Certified Fresh-Holdout Reconstitution, Unsatisfied-Demand Proof, Cross-Topology Pairability Screen & Prospective Treatment-Birth Gate**

Status: `PRESEAL_PASS / TREATMENT_NOT_BORN / OUTCOMES_CLOSED`

## Directionality lock

P8 returns to the founding object: real structural choices under real maintenance demand. It does not authorize comparative outcomes, winner claims, or a new methodology-only branch.

## Admission algebra

For candidate `c`, define the prospective gate vector

`G(c) = (E, A, T, P, O)`

where:

- `E`: independently arising/exogenous demand exists before EvoNOMOS treatment design.
- `A`: requested capability is absent at the source snapshot used for admission.
- `T`: problem source does not prescribe the internal structural treatment strongly enough to contaminate the comparison.
- `P`: two minimal, functionally equivalent structural realizations can be defined without deleting or manufacturing the demand.
- `O`: both realizations can be judged by one common functional oracle.

Admission requires `Π G_i(c) = 1`. A missing coordinate is a hard stop, not a score penalty.

## Candidate screen

### RETIRE — Aider #5308

Inherited from P7. Exact v0.86.2 source already contains MAIN/WEAK/EDITOR routing and therefore `A=0`; no repeated new demand exists and `k*` is undefined.

### RETIRE — UI-TARS Desktop #279 / GPT-4o request

The demand is real and capability absence is user-visible, but the pre-demand source already exposes a generic model configuration surface (`baseURL`, `apiKey`, `model`) and the unsupported part is model/action-protocol semantics rather than a clean missing routing abstraction. A DIRECT↔INVERT pair would confound architecture with model semantic compatibility. `P=0`.

### RETIRE — aichat-url-maker #3

The issue itself proposes a provider configuration map and a concrete provider-record representation. It is useful as a discovery donor but fails low-treatment-contamination authority. `T=0`.

### PROMOTE — SumatraPDF discussion #5906 / AIChat-NG CLI backend

Problem source: a user asks for AIChat-NG/aichat as a CLI backend for the newly introduced document-chat feature. The request specifies the desired external capability but not the internal C++ architecture.

Conservative pre-demand source anchor: `sumatrapdfreader/sumatrapdf@7061d827d0a31e3e623811991b5eb8ebda8b82ec` (2026-08-06 23:59:37 UTC). At this snapshot `AIChatBackend` contains exactly `Claude`, `Grok`, and `Codex`, and `kAIChatProviderCount = 3`; no AIChat-NG/aichat backend exists. The source already has an `AIChatProvider` polymorphic boundary, so the new structural contrast is intentionally one level lower than the old 'provider abstraction vs no abstraction' question.

Frozen rival treatments for the next construction gate:

- `DIRECT_DEDICATED`: add one dedicated `AIChatProvider` implementation for AIChat-NG, with provider-specific executable discovery, command construction, stream parsing, session/history handling, and settings accessors.
- `INVERT_SPEC`: add one reusable external-CLI provider mechanism whose executable/arguments/session/stream behavior is supplied by a typed backend specification, then instantiate AIChat-NG through that mechanism. Existing Claude/Grok/Codex behavior must remain untouched at birth.

The pair is admissible only if both arms can satisfy the same AIChat-NG behavior contract without changing the demand or using downstream implementation bytes.

## Common oracle preseal

P9 may materialize a deterministic fake `aichat` executable/fixture and one shared oracle that checks, at minimum:

1. executable discovery;
2. document path + user prompt transmission;
3. model selection transmission when configured;
4. streamed assistant text recovery;
5. non-zero/invalid output becomes an error rather than silent success;
6. session identity/history behavior is either equivalently supported by both arms or explicitly excluded from both arms before construction.

The oracle must be byte-identical across arms. Real AIChat-NG network/model calls are unnecessary for construction equivalence and are forbidden until the pair passes the offline oracle.

## P8 verdict

`SUMATRA_AICHATNG = ADMITTED_TO_TREATMENT_BIRTH_GATE`

This is **not** a treatment result. No DIRECT or INVERT bytes have been constructed, no lifecycle vector has been measured, and no design recommendation exists.

Next authorized stage: **EvoNOMOS Generation VIII ORIGIN-R1-P9 — SumatraPDF AIChat-NG Exact Pre-Birth Source Freeze, Dedicated-vs-Spec Treatment Contract, Shared Fake-CLI Oracle Materialization & Zero-Outcome Pair Construction Gate**.
