# Original six-paper Research OS intake and source reading (2026-11-04)

## Custody / version control

Six newly uploaded PDF originals from Research OS 00_INTAKE — Literature Radar (folder ID 1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16) were renamed from opaque originals to Author (Year) — Title — Venue filenames and **moved in place** to 10_PAPERS — Canonical Literature Commons (folder ID 1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP). No bytes were replaced, no files deleted. Six individual Drive metadata readbacks confirm both new titles and only the new canonical folder parent. The two CEGAR versions are DIFFERENT publications, not duplicate PDFs; keep both. Original PDF hashes / precise image formula verification NOT done, and text extraction has some corrupted symbols. The review below reflects actual connector-readable original text, named theorem statements and sections, not complete page-rendered formal proof audit.

1. [Reynolds (2002), Separation Logic: A Logic for Shared Mutable Data Structures, LICS 2002](https://drive.google.com/file/d/1lct1uFqvvOq1iSaQYodJipso_sOiDjHh/view). Separating conjunction P*Q encodes **disjoint** pieces of the heap and the frame rule permits extending local Hoare triples by an unaffected frame. The source explicitly requires free variables of frame r not to be modified by command c. Ordinary non-separating constancy fails when pointers alias. P44: a no-overlap source claim needs proof, not a name or pattern.

2. [Yang & O'Hearn (2002), A Semantic Basis for Local Reasoning, FoSSaCS 2002 LNCS 2303](https://drive.google.com/file/d/1ECH2Ken1wR-y7Y5H0ZeuGv1NW1Y6EhZX/view). Theorem 1: frame rule soundness for partial and total correctness under safety monotonicity, frame property, modifies side condition and termination monotonicity where relevant. Theorem 2: a carefully framed completeness property for consequence and frame-rule specification inference relative to a modifies set and local predicate-transformer semantics; NOT completeness of source program verification. The article explicitly notes the delicate role of nondeterministic cons allocation. P44: must freeze heap/allocator semantics before importing local reasoning.

3. [Calcagno, Distefano, O'Hearn & Yang (2009), Compositional Shape Analysis by Means of Bi-Abduction, POPL 2009](https://drive.google.com/file/d/1pO5rUHggdq1FFBzU_bOkFokK7E2WvNuA/view). Procedure-local analysis infers missing preconditions M (anti-frame) and unmodified leftover footprint F (frame), with source Theorem 5: when BiAbd(Delta,H)=(M,F), Delta * M entails H * F. The authors distinguish soundness from quality/minimality: trivially sound but useless solutions are possible. P44: discovering a permissible repair precondition is not synonymous with proving the cheapest repair.

4. [Flanagan & Godefroid (2005), Dynamic Partial-Order Reduction for Model Checking Software, POPL 2005](https://drive.google.com/file/d/1MwWcM8m_pQj-2AKJBS8gWp0SOY1FFCTz/view). Definition 1 makes event independence require enabledness invariance and commutation. Theorem 1's guarantee regarding persistent sets is stated in an **acyclic state space** and under the specified search algorithm, enabling safety/deadlock detection. P44's R3 deterministic barrier was one chosen interleaving, not DPOR-level schedule coverage.

5. [Clarke, Grumberg, Jha, Lu & Veith (2000), Counterexample-Guided Abstraction Refinement, CAV 2000 LNCS 1855](https://drive.google.com/file/d/1UcYLstqgxKnIzQHId469gEB61C_ersTc/view). Existential abstraction is an overapproximation; an abstract positive property in the specified ACTL fragment transports to concrete, while abstract counterexamples may be spurious. The source describes splitting the failure abstract state along the shortest nonrealizable prefix, with complexity and property-language restrictions. P44: use an abstract cheap repair as tentative lower bound, never as a concrete solution until checked.

6. [Clarke, Grumberg, Jha, Lu & Veith (2003), Counterexample-Guided Abstraction Refinement for Symbolic Model Checking, JACM 50(5), 752–794](https://drive.google.com/file/d/1UxXFDnQk7kZT4CLoYy7X-k3qG9Tbdc7J/view). Full journal treatment extends the 2000 CAV article with formal framework, symbolic refinement, complexity and experiments. It explicitly restricts completeness to a stated temporal-logic/counterexample family; smallest/coarsest abstraction refinement can be computationally difficult. P44: abstract-model success is NOT automatic authorization to claim all-Go edit-search completeness.

## The source-derived research contribution to investigate

CEGAR + source-repair rights + stagewise old-client contract + local heap footprints suggest a **cost interval certificate** L<=K<=U. A source-checked concrete repair proves U; a provably sound overapproximation of *admissible* source repair paths supplies L. Spurious cheaper abstract repairs can be ruled out by refinement to raise L. A legitimate bound equality L=U would certify a minimum **relative to complete frozen edit grammar and full declared observer semantics**. The inequality is a CLASSICAL formal consequence, not newly discovered mathematics. Developing a practically checkable, source-sound path abstraction and a genuinely useful proof compression remains open.

## Stop / authority ceilings

- Each paper reviewed via readable full-text extraction and targeted original definitions/theorems, not verified total visual transcription of every page or precise formula.
- None of the six was moved into 11_BOOKS; all are academic research papers.
- Remaining old intake HOLDs and user book drafts were not touched.
- No duplicate files discarded or overwritten.
- G1–G7 general source completeness OPEN, LAW-R2 HOLD.
