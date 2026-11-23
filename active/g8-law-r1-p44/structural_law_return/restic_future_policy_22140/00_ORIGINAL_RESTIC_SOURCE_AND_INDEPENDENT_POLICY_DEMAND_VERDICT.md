# EvoNOMOS — Independent Restic Future Demand, Policy–Mechanism Source Boundary and Decision-Reversal Counterexample

**2026-11-10 KST · SOURCE-CUSTODY NATIVE CHECK PASS / INDEPENDENT USER'S ARCHITECTURAL DEMAND / CLASSICAL POLICY CONTEXT WITNESS / NO SOURCE REPAIR OR NOVEL LAW / LAW-R2 HOLD**

## 1. Demand universe: restore the denominator first, not a handpicked positive

The 2026-10-09 P35 Restic U(nified)/C(omposed) source experiments predated recent public restic issues. Instead of choosing one "interesting" issue and pretending the rest never happened, queried ALL issue states in the fixed Oct-10 through Nov-10 interval. The observed GitHub issue query surfaced **23** distinct reports, title list frozen at [commit 8b13ba1c](../experimental_gate_20261110/01_RESTIC_ISSUE_TITLE_ONLY_PREBODY_CENSUS.json) BEFORE opening new issue bodies. Classification and strict source-eligibility criteria frozen at [commit 3ae16eec](../experimental_gate_20261110/02_RESTIC_SOURCE_SCOPE_CLASSIFICATION_PREBODY.md). Each individual issue body was read afterward; [23-item verified issue-date and author-requirement annotation](../experimental_gate_20261110/03_RESTIC_23_ISSUE_POSTBODY_SOURCE_SCOPE.json) explicitly preserves **all** cases and source-component uncertainty.

Post-body subjective first-label counts: 8 features, 8 bug reports, 3 CI/release-related, 2 security/release, 1 architecture/policy proposal, 1 test infrastructure. **These are one researcher's categorizations and NOT independently adjudicated official GitHub types.** High-recall storage-related shortlist of six: #22116, #22120, #22140, #22150, #22164, #22168; no equality of this heuristic with P35 source-arm eligibility is asserted.

Most important scientific limitation: P35 U/C are TWO RESEARCH-OWNED bounded backend-like implementations compiled against a genuine original \`restic.Backend\` API. They do **not** replace the independently maintained full Restic application, and no issue in this 23-case stream has yet demonstrated a **matched, old-contract-preserving U/C source repair**. Thus zero *demonstrated directly eligible* tasks does NOT mean the 23 issues are harmless or U/C cannot be modified. It means **the support needed to identify P35 U/C architecture-specific real-world maintenance effects was not supplied by this cohort**. Do not call 0/23 a population law, nonzero-effect upper bound, p-value or a new causal result. Chi's 2-issue cohort and this one must not be pooled as independent statistically representative change processes.

## 2. Independent outside user's architectural request #22140

[Restic issue #22140](https://github.com/restic/restic/issues/22140), written by an independent user on **2026-10-24**, requests a structural separation of cold-storage billing/retention policy from prune's mechanical pack rewrite. They propose first exposing pack candidates as JSON, then accepting a user-selected allowlist, then an optional persistent external policy-engine process via pipes, so policies such as time until storage commitments expire can evolve outside core Restic. This is a truly OUTSIDE independently authored **architecture-level change demand**, not a researcher-generated MIME/parser bug. It is, however, a proposal, NOT an accepted upstream maintainer task or an already merged fix.

The user illustrates a pack with **5% unused** data under **12-month storage commitments with 11 months remaining**, and observes that rewriting the retained 95% can lead to overlapping costs. Their 195% figure is interpreted here as original retained/billed capacity (100%) plus newly rewritten (95%) under a simplified billing model; this is **not** an audited actual invoice.

## 3. Original Restic 2024 source examined / exact bytes checked

Use the genuinely maintained pre-issue Restic Git source \`495982232cf1af184eac0a97871ef8161e8708ee\`, pinned from original P35. Actual original file identities:
- [\`cmd/restic/cmd_prune.go\` original](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/cmd/restic/cmd_prune.go#L44-L79), Git blob \`638a0de5e1fc191c765da9d64b74a261fafaa792\`: \`PruneOptions\` exposes \`MaxUnused\`, \`MaxRepackSize\`, \`RepackCachableOnly\`, etc., with no explicit billing, committed retention term, or storage price member in that struct.
- [\`planPrune\` 2024](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/cmd/restic/cmd_prune.go#L269-L311) calls \`decidePackAction\`.
- [\`decidePackAction\` original](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/cmd/restic/cmd_prune.go#L465-L662) obtains pack accounting from \`repo.List\`, blob usage, format/version and configured allowed-unused, then selects keep/repack/remove sets. This is the actual source locus of pack **choice** in that original version.
- [\`restic.Backend\` original](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/internal/restic/backend.go#L16-L70), Git blob \`df3281641d743d3777a440485e79d1ccc0f3af52\`: backend Save/Load/Stat/List/Remove (and other administrative operations) represent **storage mechanism**. It is **not** equivalent to full \`prune\` economic policy.
- [\`repository.Repack\` original](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/internal/repository/repack.go#L21-L50), Git blob \`c82e63f28aa613b6e9aa834490fe1575c8422d31\`: rewrites selected pack content. Not the appropriate sole locus for pricing-policy decision.

[Read-only original-source CI #42792672435 PASS](https://github.com/WhoSia/EvoNOMOS/actions/runs/42792672435): fetch EXACT original repository commit and three exact Git source file blobs, inspect key source entry points with [source-custody audit](check_original_restic_source.py), no upstream Git diff. This is a **source-structural inspection**, not execution of new Restic \`prune\` feature, no full upstream tests or user pack data.

Crucial constraint: saying the 2024 \`PruneOptions\` source has no explicit price field is NOT a whole-program proof that no client can provide price information via other channels. All program-level impossibility claims must name a restricted observation/input grammar and the frozen original commit.

## 4. A concrete conditional *decision* counterexample, NOT novel mathematics

Let a pack have unused share \`u=0.05\`, residual horizon \`h=11\` months, normalized monthly full-pack storage price 1 **pack-month per month**, and hypothetical one-off rewrite cost \`r=0.01\` pack-month. Keep the SAME pack usage, age/horizon and original path/context in two worlds. Only the backend **billing contract**, not explicit in the selected old PruneOptions fields, differs:

- **LOCKED/PREPAID**: deleting the old pack does not refund its already committed residual cost; rewriting the used share incurs **new** storage fees for \`(1-u)h\` pack-months. Incremental rewrite cost (versus keep): \`ΔC_locked=(1-u)h+r=0.95×11+0.01=+10.46\`. Correct scoped decision: **KEEP**.
- **METERED/PAY-AS-YOU-GO**: replacing a pack immediately stops future charges for unused capacity; copying the retained 95% yields \`u h\` savings, with rewrite cost \`r\`. Incremental rewrite cost: \`ΔC_metered=r-u h=0.01-0.55=−0.54\`. Correct scoped decision: **REPACK**.

Two cost environments with the same data-proportion observation require different actions. The exact [Python \`Fraction\` model](cold_storage_policy.py) and [4 actual passing local tests](test_cold_storage_policy.py), independently rerun by hosted [CI #42792672435](https://github.com/WhoSia/EvoNOMOS/actions/runs/42792672435), confirm opposite signs; invalid cost/horizon rejected. **Every actual price, horizon billing rule and one-time rewrite cost outside the independent issue's illustrative 5% and 11 months is a stated researcher assumption.** This is an ordinary information-sufficiency/expected-cost counterexample, not an unanticipated EvoNOMOS law or evidence Restic took a wrong action on an actual repository. The first source may already permit a user to set a coarse \`--max-unused\` value, which is not the same as programmatically expressing a per-pack contract-specific decision.

The scenario also explains the qualitative 195% original user illustration: total concurrently billed pack capacity under locked/no-credit assumptions = 1 + 0.95 = **1.95 original pack units**; it does not derive actual dollars.

## 5. Strong classical implementation rivals

The independent requester proposed a progression, not just "introduce a new interface":
- **R0**: existing static \`--max-unused\` and coarse options. Low new implementation/operation burden, but does not natively encode per-pack backend billing-commitment context.
- **R1**: expose read-only pack planning JSON and accept a vetted explicit allowlist of allowed pack actions, optionally generated by separate offline policy script. This can supply *the needed per-pack decisions* without a long-lived subprocess. Must define how plans become stale and how authorization/safety are checked.
- **R2**: single long-lived policy-engine process with versioned request/response protocol and explicit fail-closed or retry semantics. Supports frequent/external policies and avoids per-pack process spawning, but incurs IPC, protocol evolution, lifecycle, compatibility, and failure costs.

If only one-off manual planning is needed, R1 may be a strong simpler rival. For frequently changing customer/provider rules, R2 may be useful. No code for these variants or realistic labor/risk costs was produced; **they must be tested on the actual Restic \`prune\` source and independently chosen task streams before making a structural design claim**. The P35 U/C payload representation cannot be substituted as equivalent to R0/R1/R2: changing the representation of Save/Load metadata does not, by itself, implement external cost-policy query and action authorization.

## 6. Decision

**Keep** independent #22140 as a meaningful future *architectural demand* and strong candidate to study policy–mechanism boundaries, and preserve ALL 23 issues in the denominator. **Reject** the temptation to declare P35 U/C favored, a low-CI "real future change sign reversal," or a new law. **Retire** repeated Chi syntax demos and narrow Restic U/C as a proxy for all of Restic. **Advance when possible** by treating the live \`prune\` decision code, its actual external API, and observed maintenance effort as the research substrate, with a controlled source-matched R0/R1/R2 arm comparison, independent agent implementation, the same safety and old/new customer contract, and strong existing source-model rivals.

**LAW-R2 HOLD; no owner-approved production prune change, no real coding agent repair, no source-native feature implementation claimed.**
