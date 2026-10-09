# P34-P5 Precommit

We will compare a direct and component-based Go storage adapter under one identical new requirement. Keep the original Restic interface and prior test results unchanged. Count real changed source lines and verify matching behavior. Existing historical P12 remains a non-result.

## Frozen requirement and measurement

On `Save` of a Restic `KeyFile`, reject any input longer than 8 bytes with a stable `P34_KEYFILE_LIMIT_EXCEEDED` error. An 8-byte value remains valid, and a rejected overwrite preserves earlier data. This is a synthetic, not an upstream, maintenance demand.

DIRECT changes its public `Save` implementation. COMPOSED changes its internal write-capability `save` implementation. Each is a separate source variant using the original P4 storage engine. Keep the full existing P4 tests. An unmodified baseline must fail the new requirement. For each variant report changed production source lines, physical files, touched methods, and test results; exclude generated tests and tooling from maintenance measurements. This does not measure engineering hours or future regression frequency.
