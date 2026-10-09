# P35-MATH-3 O2 — Post-Conflict Sequential Second-Demand Source-Edit Protocol

**Status:** selected exploratory repair completion, after observing O1 Git's eight textual conflicts and its successful classification CI #37931146034. This is **NOT outcome-blinded** relative to the O1 conflict surface. The paper-A source-world argument may use it only for **existence of tested O2 paths in the specified small grammar**, not statistical generality or law-theoretic noncommutation.

Each program starts from a frozen previously verified D9-only or D10-only `go-chi/chi v5.1.0` source under LIVE/SNAPSHOT and INLINE/HELPER. We now implement the **other demand by the fewest directly explainable semantic edits**, rather than 3-way automatic text merging or transplanting the earlier BOTH source file.

Frozen semantic patch operations for each first-demand family:
- `D9 → D10` INLINE: retain `r.Header.Values(header)`; extend the existing per-value matching loop by splitting each raw value at unquoted commas, trimming space and lowercasing each token before `p35P7MatchStrength`.
- `D10 → D9` INLINE: retain the already implemented comma split; replace its single `Header.Get` source with all `Header.Values` values.
- `D9 → D10` HELPER: retain `Header.Values`; enable comma-token matching in existing `p35Math2BestMatch(rule,values,true)`.
- `D10 → D9` HELPER: retain the already implemented `p35Math2BestMatch(...,true)`; replace single `Header.Get` with all `Header.Values`.

Every case uses *only its own first-demand source file as mutation input*. Previously authored final BOTH files are **neither templates nor pasted patches**; matching resulting file hashes may be reported, but not as independent discoveries. Eight traceable second edits are frozen in Git as new full source files. The completed programs must pass D0/D8/D9/D10 and the independent 720-case per-arm reference grid (where available) on the pinned upstream Go module; retain per-path source SHA, source diff first→second, full go test/vet/middleware race. No unrun path or failing path is counted as SUCCESS. No inference of `R_D9 ∘ R_D10 = R_D10 ∘ R_D9` over **all** valid repairs from these chosen witnesses.

Our source edits are deliberately simple and post-conflict. The O2 result answers **whether the textual conflict genuinely prevented feasible second-demand implementation in this narrow grammar**; it does NOT by itself rank SOLID or prove a new mathematical software principle.
