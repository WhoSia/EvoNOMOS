# P35-MATH-2B — Post-outcome Independent Go Differential Oracle Preseal

**Time/order:** This is a *post-MATH-2-outcome*, *pre-differential-oracle-execution* robustness extension. It cannot retroactively make MATH-2's source variants blind or establish independent replication. Parent P35 OPEN; LAW-R2 NOT_AUTHORIZED.

## Exact unmodified source treatments

Four original `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00` source replacements are fixed in `tools/p35-math2/arms/{live,snapshot}/{inline,helper}/both/route_headers.go`. No modification to these sources, prior D0/D8/D9/D10 oracles or runtime model is authorized within this robustness check.

## Evaluation oracle, frozen before execution

A new test file builds an **independent literal reference matcher** (not calling either arm's `p35P7MatchStrength` or `p35Math2BestMatch`). Its inputs are the research contract's two whitelisted header keys `X-A`, `X-B` only. A header has 0+ physical field values. Each physical value is split by unquoted comma, whitespace-trimmed and lowercased; empty tokens are ignored. For registered rules, first matching rule *per header* is chosen and then among keys the winning candidate is the strongest (`exact> wildcard`), ties break `X-A` before `X-B`; no candidate implies `fallback`. Wildcards here have only simple `prefix*` and `*suffix` syntax. No quoted-string grammar, RFC normalization or general HeaderRouter statement is admitted.

Generate all cartesian products of the following fixed physical-field arrangements on X-A and X-B:
`none; ["none"]; ["ping"]; ["pong"]; ["miss","ping"]; ["miss,ping"]; [" ping , pong "]; ["polo, miss"]; ["","ping"]; [" , , "]; ["pong","ping"]; ["miss, pong"]`.
For each pair evaluate five fixed route registrations: (i) A wildcard p*, B exact ping, (ii) A exact ping, B wildcard p*, (iii) A wildcard p* then exact ping, B wildcard p*, (iv) A RouteAny [p*,ping], B wildcard p*, and (v) A wildcard *g, B wildcard p*. This yields **12²×5 = 720 declared cases per arm**, each compared against *reference-observed handler selection* using real `httptest` and exact HeaderRouter public API. Repeat no random sampling, no program-path special-casing, no outcome-driven case removal.

Secondary metamorphic contact: field pair `["miss","ping"]` and single physical `["miss,ping"]` must give identical routing results for this restricted contract. Cases explicitly target empty and repeated values, wildcard vs exact across header keys, per-header first-registration precedence, RouteAny, no match/fallback, casefold and trim.

**Action on FAIL:** preserve failing case and native logs. Do not modify fixed four source files or this frozen reference oracle within current wave. If reference itself is demonstrably inconsistent with the prior D9/D10 intended contract, record `ORACLE_CONFLICT_HOLD` and open a separately sealed repair wave. Successful exhaustive bounded testing is not proof of universal behavior or independent law discovery.

## Meaning for DIP-49 / DIP-50

This checks a narrow faithful concrete behavioral oracle for D9+D10, but it does **not** implement DIP-49's pairwise-discriminating **competing law-hypothesis family** or all-prefix real-world symbolic query realization. Do not call a four-arm behavior agreement an identified law automaton. This wave is a robust **program-repair overfitting attack**, justified after positive source witnesses, with established multiple-plausible-patches and testing literature as strong background.

The MATH-2 formal results are classical may/must/noncommuting relations; these four actual Go patches witness `May(usable patch)` in four limited fixed worlds, not Must and not realized noncommutation of demand operators. Separate any future source-level D9;D10 vs D10;D9 tests from abstract Lean's finite noncommutation countermodel.
