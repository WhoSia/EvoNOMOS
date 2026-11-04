# Observer contract v0

Projection: (method, request target, status code, response body after whitespace trimming, Allow header, Location header). The whitespace trimming is an explicit limitation and must be removed if exact bytes matter.

Probes include GET, HEAD, POST, OPTIONS, PUT; encoded slash and encoded ordinary letter; trailing slash; empty identifier; HEAD on encoded slash; encoded dot-segment candidate.

Not measured: full response header map, streaming/flush, cancellation, request context lifecycle, timing, concurrency, panic propagation, raw network behavior, status differences outside the finite input set.

Only assert observational agreement *on the named finite probes*.
