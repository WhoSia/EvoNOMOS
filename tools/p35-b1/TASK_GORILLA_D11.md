# Task GORILLA_D11 — Go source maintenance (original pinned source supplied)

Original upstream code: gorilla/mux v1.8.1 at `b4617d0b9670ad14039b2739167fd35a60f557c5`. This task concerns `Headers` and `HeadersRegexp` as separate real matching paths, not Chi's routing API.

For only the synthetic research header `X-EvoNOMOS-Mode`, support CSV-style quoted comma tokens and doubled double quotes. For both literal `Headers` and regex `HeadersRegexp`, match a declared expression against each decoded token rather than the raw physical header string; retain existing literal/regex semantics on old plain-value cases. Ignore tokens in a malformed quoted field, but allow other physical fields. For this task use only lower-case comparison examples; do not change unrelated header case semantics. This grammar is a synthetic study requirement, not a proposed generic HTTP header standard. Preserve the public API and the complete original module tests.
