# Observation protocol — preregistered relative to P44 execution, not earlier R24 observations

Every wire observation is (status code, body after whitespace trim, first Allow header value, Location header). The request identifier is (method, path including encoded spelling). Tests use an actual httptest.NewServer plus http.Client and disable automatic redirects. They do not assert universal HTTP semantic equivalence or middleware/concurrency behavior.

The first six protected probes originate from the earlier R24 predeclared narrow set; the six additional probes were *exploratory and already observed in R24*. Therefore the combined twelve are **not a blinded independent holdout**. Their purpose is a reproducible remediation exercise.

A new independent test family must be preregistered in a later R1 stage and chosen without tuning to this pair's observed divergences. Keep old six and new six provenance distinct.

Whitespace trimming is a lossy projection; exact byte-for-byte response identity is not established.
