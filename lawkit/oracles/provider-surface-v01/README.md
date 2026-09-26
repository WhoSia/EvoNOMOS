# Provider Surface Oracle v0.1

A dependency-free Go mock server used by EvoNOMOS provider-family experiments.

It intentionally separates the **demand-required** search surface from **conformance-only** fetch/extract surfaces:

- `/exa/search` — demand-required
- `/exa/contents` — conformance-only for a wide search+fetch boundary
- `/tavily/search` — demand-required
- `/tavily/extract` — conformance-only for a wide search+fetch boundary

The server never calls vendors. It provides deterministic wire fixtures and can write a JSONL ledger marking each request as `demand-required` or `conformance-only`.

This oracle does not decide which treatment is better and does not measure source churn.
