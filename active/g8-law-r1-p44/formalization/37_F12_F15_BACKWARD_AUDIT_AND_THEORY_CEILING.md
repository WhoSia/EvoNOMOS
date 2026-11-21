# P44 retrospective audit: F12 through F15, 2026-11-05

F12: weighted simulation of a supplied finite source edit graph. Its graph completeness is an assumption; missed cheap authorized edits invalidate lower bounds.

F13: separately supplied finite runtime traces. Universal client safety needs sound overapproximation of all relevant traces; concrete violation needs a realizable underapproximation witness. Both completeness flags require external source evidence.

F14: actual Go AST parsing of one protected constant function and one editable literal-return function. The bounded edit universe was exhaustively enumerated; native Go runtime verified three source releases. No whole-Go proof.

F15: one boolean conditional with independently editable literal outputs; nine source states, 36 source edit transitions. Native Go runtime verified every source state. The marginal output-set-equivalence shortcut was refuted with an input-output mapping counterexample. A previously accepted input-specific client contract was separately protected and native CI confirmed.

Strong classical rival status: White et al. 2009 established MUSCLE CSP multi-stage configurations; the authenticated Drive upload labelled JSS-2012 is a SIX-author 2012 journal-submission PREPRINT, not the FOUR-author 2009 SPLC original. Published White et al. 2014 JSS is a separate later article with feature-model drift. These works already cover multi-stage validity, budgets, configuration change costs, evolving feature models and optimization. Source-level edits, joint runtime client observations and rights provenance remain only candidate differentiators.

Current academic ceiling: F15 is a standard product-state source graph and classical contextual contract issue. Exact source-aware BFS returns the same answer as the proposed finite certificate; no speed, precision or size advantage demonstrated. Source grammar restricts every construct that could introduce aliasing, concurrency, network output or hidden semantic dependencies.

Next genuinely risky gate: add ONE shared mutable state or aliasing construct and prove source edit footprint and client observation coverage under defined schedules, comparing directly with separation logic / bi-abduction and bounded model checking. Do not infer broad law novelty from repeated safe examples. G1–G7 OPEN, LAW-R2 HOLD.

Original F15 native CI success with both stage regression and nine compiled states: https://github.com/WhoSia/EvoNOMOS/actions/runs/41962356928
