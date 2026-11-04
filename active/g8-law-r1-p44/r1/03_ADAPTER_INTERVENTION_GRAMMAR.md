# Three application-owned adapter edits, bounded grammar

H: register Chi HEAD /items/{id} with the same app handler as GET.
D: apply URL path unescaping to the Chi route parameter before returning it.
M: replace the default Chi MethodNotAllowed response for this app router with a reply matching the stdlib observed Allow/body on the declared requests.

Permissions: application registration and handler behavior; no upstream source patch. Each H, D, M has unit synthetic cost 1 and can be independently enabled. Each subset is represented by a three-bit mask 000..111.

Hypothesis: Only mask 111 matches the twelve named probes; removing H yields a HEAD failure, removing D yields an encoded-ID failure, removing M yields a 405 Allow/body failure. The test enumerates all eight masks and prints mismatch counts.

This is exact minimum for the **eight configurations of this named grammar**, not a lower bound on every possible application program or compiler rewrite. A different single patch could implement multiple repairs; no universal minimum-edit claim is permitted.
