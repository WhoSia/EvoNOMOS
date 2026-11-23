# F20 B — chi original source patch audit (AFTER prepatch seal)

Historical original commit: https://github.com/go-chi/chi/commit/6ceb498b221efa11f559602beb2463b8b52c2161 ; parent 882c15e6462ce0630529d04c330e84942ebd059d. Source-level diff read AFTER unit A's eleven selection/custody commits.

Core issue: `Mux.Find` receives nested route context; before change its subrouter lookup returns only the descendant pattern and it does not compose the outer prefix correctly. The patch introduces the prior route pattern, handles leaf endpoints directly, returns blank on failed descendant, strips outer wildcard suffix then joins the found subpattern. The original post source also revises existing TestMuxFind and adds deeply nested route cases. New source path and parent/post SHA are pinned.

The retrospective oracle `oracles/chi_nested_find_test.go` constructs nested `/api/groups/v2` and POST `/{id}`, calls `Find(ctx,"POST","/api/groups/v2/17")`, expects full `/api/groups/v2/{id}` (not merely `/{id}`). This oracle was formulated AFTER seeing original diff, hence cannot be called a blind future prediction; the native parent is expected to FAIL at test assertion, post to PASS under same fixture.

**Hidden retrospective lesson:** Original parent TestMuxFind used equal comparison `==` where subsequent source changes it to `!=` for correct positive test; therefore relying on parent green original upstream tests would hide an oracle defect. This is an observed historic test weakness, not evidence of a novel repair law. Full customer contract outside explicitly tested Mux.Find remains UNKNOWN.
