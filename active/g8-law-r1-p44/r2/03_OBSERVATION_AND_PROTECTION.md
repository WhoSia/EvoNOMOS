# Protected observer family and layering

The protected initial contract consists of the same twelve (HTTP method, URL path) probes used by P44-R1, including GET, HEAD, POST/OPTIONS, encoded slash and letter, missing or trailing path. The projection is (status, whitespace-trimmed body, first Allow value, Location). The test uses httptest.NewServer plus an actual HTTP client and disables automatic redirect following.

The protector is intentionally finite and already known. This is not complete contextual equivalence for arbitrary clients; body trimming is lossy, HTTP headers besides Allow/Location omitted, temporal effects, races, middleware and arbitrary Unicode not fully observed.

Demand-specific observer: GET /ledger/alpha/revisions, /ledger/alpha/audit, /ledger/alpha/summary each returns 200 and the exact named text. Old protected observations remain checked at every future stage.
