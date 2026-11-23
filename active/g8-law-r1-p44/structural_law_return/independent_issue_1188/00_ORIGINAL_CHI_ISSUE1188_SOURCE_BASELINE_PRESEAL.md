# EvoNOMOS — Original Chi #1188 Semantics Preseal, before native source baseline test

**2026-11-10 KST · independently reported external issue, issue text READ before test; NOT solution-blind design selection or independent future forecast.**

## Genuine outside request and fixed source
Original reporter of [go-chi/chi issue #1188](https://github.com/go-chi/chi/issues/1188), filed **2026-09-23**, observed that route `/re/{name:[^.]+}.json` accepts `/re/a/b.json` with parameter `a/b`, contrary to the old documented path-segment expectation. Other route expressions `/bare/{name:[^.]+}` and `/plain/{name}.json` refuse that same embedded slash. Issue report includes reproduction and expected behavior; **no solution diff, implementing PR, or patch is examined at this stage**.

Use **externally maintained original go-chi/chi v5.1.0 exact Git commit `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`**. This is an older source than the reporter used (v5.3.2/current), so **reproduction must be independently checked**. If old source behaves differently, mark OUT_OF_SCOPE SOURCE BASE, do not silently change tag or report source bug confirmed. Go v1.23.2 native tests on original production source with only research-authored app test file copied to disposable original checkout.

## Contract named before first original source execution
- Old necessary client: GET /re/a.json → HTTP 200 and name=a; GET /bare/a → HTTP 200 and name=a; GET /plain/a.json → 200 and name=a. Other source-native tests must be preserved.
- New issue contract: GET /re/a/b.json → HTTP 404; GET /bare/a/b → HTTP 404; GET /plain/a/b.json → HTTP 404; all three reject matching a slash within one path parameter.
- Positive multiple-segment routing control: GET /re/a.json GET /re/b.json must succeed; otherwise a trivial all-404 implementation could seem fixed.
- New test oracle should first run as expected-negative customer requirement on upstream v5.1.0, separately from old-client all-PASS tests. Native current failing output must NOT be labelled CI infrastructure failure; assert a known-fail baseline test with an explicit inverted expectation or manual test logs.

## Early architecture × maintainer policy entry — NOT an executed factorial
The old P35-B1 [original 4 guidance arms and Latin square](../../../../tools/p35-b1/assignment_manifest.json) were found. `agentRuns=0`, model/version, attempt budget, tool access and executor remain null. Reusing that as an executed cohort without controlling input budgets is forbidden. This independent issue can be one potential external-demand candidate, but agent source snapshots and old-client tests must be fixed, isolated across conditions, and a **separate unseen downstream follow-up task** is required before claiming temporal generalization.

No universal Go path matching, no complete regex semantics for arbitrary pattern grammars, no outside maintainer patch-time evidence, no new causal architecture law, LAW-R2 HOLD.
