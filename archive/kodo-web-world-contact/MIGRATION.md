# Migrated branch: agent/evonomos-dip65-common

Source repository: `WhoSia/Kodo-web`
Source base: `bd47de6f07250bb6c5cd9fd3ade99b911eda1596`
Source head: `301f6c4b7b71903b390de5726a264410d5500847`
Purpose: historical DIP-65 WC1 common scaffold. This is an inert provenance snapshot; Kodo-web remains external substrate only.

Changed research files relative to Kodo-web main:
- `.github/workflows/site-check.yml`
- `evonomos-media-contract.json`
- `tests/media-catalog.test.cjs`

## Contract snapshot
```json
{
  "alternate_label": "preview",
  "retired_label": null
}
```

## Historical workflow snapshot
```yaml
name: Site checks
on:
  push:
  pull_request:
jobs:
  validate:
    strategy:
      fail-fast: false
      matrix:
        node: ['20', '22']
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install beautifulsoup4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: node --check script.js && node --check media-manifest.js
      - run: python tools/check_site.py
      - run: node tests/media-catalog.test.cjs
```

The exact historical test source remains recoverable from source head `301f6c4b...0847`; the canonical preregistration has been migrated to EvoNOMOS issue #1.