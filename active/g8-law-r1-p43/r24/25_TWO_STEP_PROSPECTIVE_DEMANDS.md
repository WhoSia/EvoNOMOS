# Two-stage future-demand court — intentionally strong tie candidate

Both applications initially protect six GET/HEAD and missing-path observations.

At t1 both are granted app-route insertion and asked to serve GET /lookup/alpha -> lookup:alpha.
At t2 both are granted another app-route insertion and asked to serve GET /lookup/alpha/meta -> meta:alpha.
Each stage must preserve all six old observations; at t2 the stage-one result must also remain correct.

No upstream library edits are permitted. Synthetic expense: one new authorized endpoint insertion at each demand (0,1,2 cumulative for each candidate). This is NOT human engineering-time measurement.

Strong classical baseline predicts both succeed: each router supports the required route insertions. Thus even if native paired CI succeeds, the outcome is a predicted tie, useful as a positive control, NOT a new architecture superiority or LAW-R2 promotion.

Next experiment must use independently motivated, time-sealed demands capable of separating outcomes while preserving equal rights and baseline. Neither of these convenient additions does so.
