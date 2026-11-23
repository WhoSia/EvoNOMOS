# Client contract — temporal versus sequential

O0 old-client observations:
- GET /items/alpha with X-Request-Id:req-A -> status 200 body v1|req-A.
- POST /policy/alpha?label=v2 with req-B -> 200 body updated:v2.
- Following GET with req-C -> 200 body v2|req-C.
Both live-alias and frozen-copy modes must satisfy O0 in both routers. This is a narrower client oracle than prior P44-R2's twelve HTTP probes, not silently claimed as equivalent.

D1 new temporal contract: GET A captures the value v1 at middleware entry. While GET A is paused, concurrent POST B commits v2. GET A must still return v1|req-A; a later GET C must return v2|req-C. The barrier channels enforce capture(A) happens-before update(B) happens-before read(A) without relying on timing guesses.

The contract says nothing about arbitrary request IDs, snapshot guarantees outside this small application protocol, middleware chains not in the fixture, HTTP HEAD, or arbitrary client concurrency.
