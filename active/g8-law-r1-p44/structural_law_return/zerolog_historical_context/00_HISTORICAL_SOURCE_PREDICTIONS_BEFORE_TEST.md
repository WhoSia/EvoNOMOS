# Pre-execution, source-informed historical replay — zerolog Output Go-context preservation

Date 2026-11-09 KST. **Not blinded future demand prediction:** author/research assistant has already read PR #811's complete public diff and #769's description. Thus this is a historical native Go source verification and a structural-mechanism comparison, not C5.

## Source ancestry
Independent upstream `rs/zerolog` original parent at **`5eb5f3a76c09eeadc1f2464baf4a4e3f1037c830`**, merged original contributor fix **`56591163bce358abdb860d3dad599d3ab440621a`**, PR #811 merged 2026-09-28. Exact parent→child Git history. Current user has no authenticated write rights to this upstream; run read-only original sources, placing only a disposable app-owned external regression oracle into the ephemeral CI checkout.

PR #769 from 2026-05-13 proposed attaching Go context when using `Logger.WithContext`; closed unmerged on 2026-05-14. This is a separate missing propagation path; no assumption that PR #769 was accepted as correct.

## Source-derived predictions (before CI)
- OLD: `New(w).Hook(h).With().Ctx(ctx).Logger().Info().Msg(...)` exposes trace ID to `Event.GetCtx` in both versions.
- NEW requirement from actual externally authored PR #811: same logger after `logger.Output(writer2)` must preserve Go context in hooks; PRE fails by losing trace, POST passes. `Output(Output(logger))` likewise.
- STRONG FIX WITHOUT UPSTREAM SOURCE CHANGE: directly adding `.Ctx(ctx)` on the emitted event must preserve trace in both versions. That is a standard explicit client repair, but requires updating every affected call site and is a **real alternative**.
- DIFFERENT HISTORY PATH: `log.WithContext(ctx); Ctx(attached).Info()` is predicted not to set logger's internal `ctx` in either original version, so event hook sees no trace; merging PR #811 alone does not fix PR #769's separate path.
- OLD writer output payload and field `service: api` are preserved in PRE and POST.

## Falsification
Run identical fixture in exactly the parent and merge commit checkout; compare expected observations by version, no test relaxation. Original repo `go.mod` pins Go 1.23, native Go test and race, check `git rev-parse HEAD`; local fixture may be copied into ephemeral checkout but cannot edit upstream original source or claim fork code edits. External PR's actual maintenance demand was independently authored in 2026-09, but the analyst has already read it, so no result-blind forecasting.

This is deliberately a more genuinely different source mechanism than pflag/global names: **identity and source state propagation across an object-copy boundary, plus noninterchangeable context capture operators**. Nevertheless ordinary source-aware def/use dataflow and Go structure-field copy analysis completely predict it, so no beyond-classical law is anticipated. The scientific value is quantifying precisely where current client behavior ceases to imply future repair behavior, and demonstrating multiple possible repair interventions.

Decision stop: if native predictions match classical inference, archive as a real historical source comparison; DO NOT claim a new principle or open unlimited related PR tests. LAW-R2 HOLD.
