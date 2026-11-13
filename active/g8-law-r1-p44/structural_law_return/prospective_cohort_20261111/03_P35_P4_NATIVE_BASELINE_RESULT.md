# P44 P35-P4 native baseline result

2026-11-13 KST. [CI 43394030867](https://github.com/WhoSia/EvoNOMOS/actions/runs/43394030867/job/131780510148) succeeded at bbb2578dce4857b775ad558e2e230f8ed892864f with Go 1.23.12, linux/amd64, pinned Chi 67be7d9cafdaeb4e04e887ff78d09e030ee43b00.

The unmodified upstream gave the expected negative-control failure. Independent and Shared both passed the frozen 16-case suite, whole-module tests and middleware race tests. The separate diagnostic returned 415 on Independent at 08:34:56.303Z and 204 on Shared at 08:34:56.715Z. A 204 means the sentinel downstream handler ran. The regression requires a nonempty body, an absent Content-Type and an allowlist that includes an entry normalizing to the empty string. The original 16 cases remain the scoped historical contract.

For a future paired experiment, exclude this input only when the documented client contract excludes the empty allowlist entry. Otherwise, a candidate normalization is to reject an empty header locally in Shared AllowContentType after the existing bodyless bypass. That location leaves the shared parser's missing-charset representation available to ContentCharset. This candidate has not been applied or tested. Preserve and rerun the divergence diagnostic on the historical arms and require matching responses on the normalized arms before measuring later changes.

The contrast is shared source policy versus independently placed policy, with two stdlib parse calls on the successful nonempty path through both guards. A parse-once design would require a separate treatment. No independent maintenance task or actor outcome was observed. LAW-R2 HOLD.
