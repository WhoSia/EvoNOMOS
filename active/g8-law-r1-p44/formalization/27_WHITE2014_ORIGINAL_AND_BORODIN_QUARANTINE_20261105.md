# P44 original evidence custody — formerly missing White 2014 and Borodin/El-Yaniv 1998

2026-11-05. **Both files detected in Research OS 00_INTAKE after the previous missing table**, but their verified scientific usability differs.

## A: White et al. (2014) — original academic article acquired and canonicalized

[Drive PDF](https://drive.google.com/file/d/1n4vr5-CR7P-_HHBzpkmHmoNzFqzmghDp/view), file ID `1n4vr5-CR7P-_HHBzpkmHmoNzFqzmghDp`, 2,250,352 bytes by Drive metadata. Original source verified from cover and readable body: Jules White, José A. Galindo, Tripti Saxena, Brian Dougherty, David Benavides, Douglas C. Schmidt, *Evolving feature model configurations in software product lines*, Journal of Systems and Software 87 (2014), 119–136; DOI 10.1016/j.jss.2013.10.010. Moved **in place** from 00_INTAKE ID 1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16 to canonical 10_PAPERS ID 1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP, renamed `White, Galindo, Saxena, Dougherty, Benavides & Schmidt (2014) — Evolving Feature Model Configurations in Software Product Lines — JSS 87 119-136.pdf`. Exact final name/sole parent/size independently read back; no byte overwrite or deletion.

**Direct original-text reading**, not abstract-only:
- §3.1 explicitly defines multi-step configuration as a **6-tuple**, involving edge constraints E, point configuration constraints PC, change cost between successive configurations, maximum step count K, start constraints and endpoint constraints.
- §§3.2–3.3 treat point and edge constraints, including bounded change budget; multi-step validity and cost are already formalized here.
- §2.5 treats changes in the feature-model itself (model drift) as a different process from selecting new feature configurations.
- Introduction says MUSCLES maps these multi-step tasks into CSPs and optimizes total properties of the evolution path. It builds on authors' prior 2009 work.
- §6.4 explicitly acknowledges randomly generated feature model populations, ecological validity, constraint complexity and limited transport to real engineering tasks as threats to empirical generalization.

**Severe novelty verdict:** P44 cannot claim to be the first model of stagewise valid software evolution, constrained adaptation paths, future changes, feature-drift or cumulative optimization. What remains potentially distinctive must be **source-level edit authority, verified runtime joint client traces, a machine-checkable two-axis completeness certificate and measured evidence of compactness or efficiency over equal-information MUSCLES/CSP, separation logic and model checking**. This is a research target, not a proven difference.

No full visual proof/page formula transcription; text extraction affects precise symbolic display. Source-level assertions are restricted to directly read passages.

## B: Borodin & El-Yaniv (1998) — candidate book file present but PDF damaged

[Drive file](https://drive.google.com/file/d/11AdbiQ9bvF0bi-74k8sLRVP09Sqpw7Ax/view), file ID `11AdbiQ9bvF0bi-74k8sLRVP09Sqpw7Ax`, 21,483,785 bytes. Filename indicates Allan Borodin and Ran El-Yaniv, *Online Computation and Competitive Analysis* (1998). Raw file fetched intact from authenticated Drive to local container for integrity/readability inspection.

Local PDF inspectors report 217 pages but **invalid deflate/zlib compressed streams**: pdfinfo/pdftotext report illegal character, Bad FCHECK; PyMuPDF repeatedly reports incorrect header checks. No machine-extracted readable text, and first page render is blank. Therefore do NOT claim book original text read or edition/contents verified. It may be a corrupt scan, partial or mislabeled file; metadata alone does not settle content identity.

Safely renamed IN PLACE to `BORODIN & EL-YANIV (1998) — Online Computation and Competitive Analysis — PDF STREAM CORRUPTION — INTAKE HOLD.pdf`; remains in 00_INTAKE rather than being promoted to 11_BOOKS. Final parent and size read back. Never delete, overwrite or certify full ownership/edition until a sound, readable replacement is obtained.

## Current acquisition status

White 2014: OWNED, READ AT TARGETED ORIGINAL SECTIONS, CANONICAL 10_PAPERS.
Borodin/El-Yaniv 1998: **BYTES PRESENT, CORRUPT/HOLD, NOT READABLE CANONICAL**, keep in intake for a verified replacement. This is NOT an entirely missing title, but a missing usable original source.
