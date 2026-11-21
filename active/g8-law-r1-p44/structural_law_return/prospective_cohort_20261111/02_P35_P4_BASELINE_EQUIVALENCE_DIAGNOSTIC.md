# P44 P35-P4 baseline equivalence diagnostic

2026-11-13 KST. Source audit, with a separate Go diagnostic. LAW-R2 HOLD.

The five arm blobs and the original acceptance test were fetched at d34890f1ca88c089e710304fb1374696cedf18f6. All six returned byte sequences reproduced their Git blob IDs locally. The original [D4 CI job](https://github.com/WhoSia/EvoNOMOS/actions/runs/37899279543/job/113717793482) recorded both arms passing the historical acceptance, whole-module, and race checks with Go 1.23.12. That receipt pertains to the October run.

In Shared, AllowContentType and ContentCharset each invoke parseCanonicalContentType. For a valid nonempty header and a nonempty body, when both guards run and allow the request, each arm invokes mime.ParseMediaType twice. Shared centralizes the source of the parsing policy. Runtime reuse would be a separate treatment.

The historical acceptance suite uses AllowContentType("application/json"). Its optional empty charset is configured on ContentCharset. It misses the following case. Give AllowContentType("") a POST with a nonempty body and no Content-Type. Independent passes the empty header to Go's mime.ParseMediaType, whose checkMediaTypeDisposition rejects the empty token. It returns 415. Shared's helper returns ("", "", true), the lookup succeeds on the empty entry and the next handler runs. The dedicated diagnostic uses 204 as the downstream sentinel. This is a baseline observational difference on the exported API. Its relevance to real customers remains unmeasured. Keep the historical tests and the separate diagnostic, and match this behavior explicitly before assigning a maintenance task that exercises it.

The cutoff search for go-chi/chi issues created on or after 2026-11-12 UTC returned zero results. The direct issues listing filtered on creation time also returned zero matching issues. These are bounded observations from one repository. No independent task, real maintainer outcome, or causal estimate enters this result.
