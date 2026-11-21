# P44 — Original-text reading log (2026-11-04)

These documents were directly retrieved from Google Drive via authenticated readable-text extraction. Source pages were not rendered for formula/symbol visual cross-check, so this is targeted concept/argument-level reading, not a full line-by-line verified mathematical transcription.

## Song et al. (2023), Conditional Contextual Refinement
Google Drive: https://drive.google.com/file/d/13Ghr7KUsITAJnkDngPoh2tT2jn5JbkMy/view
DOI https://doi.org/10.1145/3571232
Directly read front matter and introductory framework, including the claim that CCR unifies contextual refinement and separation-logic conditional pre/post specifications and allows transitive composition. Scientific threat to P44: we cannot present 'conditional compositional source-change refinement' as unprecedented. Our distinct task, if one exists, is a certificate relating **source edit authorization, dynamic future-demand arrival and stagewise old-client preservation with measured/comparable costs**.
What remains unread/proof-gated: CCR's formal judgment, model relation, exact Coq soundness and conditional transitivity proof hypotheses. Must read full formal sections before novelty claim.

## Gäher et al. (2022), Simuliris
Google Drive: https://drive.google.com/file/d/1w5g28mYNDVpmyhEaXFn1LDF0nxgTkl9s/view
DOI https://doi.org/10.1145/3498689
Front matter directly read: ownership-based simulation for transformations of concurrent programs, preservation of termination under fair scheduler and modular reasoning via Iris-style separation logic; examples with shared aliasing, data-race UB and Stacked Borrows for Rust. Scientific threat: P44 cannot claim the first ownership-sensitive simulation of concurrent source transformations. Our different target is permitted **future maintenance pathways** and comparability under change demands/rights, not compiler transformation correctness.
Proof gates: fairness, source language UB and memory model, simulation step interpretation and termination must be checked in mathematical sections before transfer to Go mutex/request semantics.

## Huang et al. (2023), A Survey on Automated Program Repair Techniques
Google Drive: https://drive.google.com/file/d/1RmEcUSQUqyzYfdWcK5m5DPu4W1vDVKIt/view
arXiv 2303.18184v3
Abstract/front matter directly read: APR grouped by search-based, constraint-based, template-based and learning-based generation; failure of patch tests to prove global correctness remains important. Reading source explicitly distinguishes patch generation from verification criteria. Scientific threat: a source repair search or template-driven fix method is not novel simply because bundled with EAC observation/rights semantics.
Proof gates: full section-level comparison to search-based/constrained repair, how patch correctness measured, and latest benchmark limitations.

## Further already-owned relevant source not fully read in this session
- Jung et al. (2018), Iris from the Ground Up.
- Song & Cho (2025), CCR 2.0.
- Smith et al. (2015), program-repair overfitting.
- Prechelt et al. (2001), design patterns vs simpler solutions.
- Parnas (1972), design modularity.
Use Drive originals and distinguish full text from partial reading.

## Priority missing by exact Drive filename lookup (not total byte audit)
Reynolds (2002) separation logic; Yang/O'Hearn (2002) semantic local reasoning; Calcagno et al. (2009) bi-abduction; Flanagan/Godefroid (2005) DPOR; Clarke et al. (2000) CEGAR; Musuvathi et al. (2007) CHESS; O'Hearn (2020) Incorrectness Logic; Sjøberg et al. (2005) controlled experiments; Jimenez et al. (2024) SWE-bench. See R3 literature audit for bibliography. Do not imply papers obtained until Drive metadata confirms.
