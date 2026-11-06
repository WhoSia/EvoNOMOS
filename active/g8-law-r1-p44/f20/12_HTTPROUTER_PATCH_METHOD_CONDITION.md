# F20 B — httprouter original source patch audit (AFTER prepatch seal)

Original https://github.com/julienschmidt/httprouter/commit/484018016424d215c0b87c42f4c9b57d980fbd00 parent ef8578da8d8e1217ea44313b23edf46154b198ab, authored 2024-01-30T10:56:56Z. Changed router.go alone, three additions / one removal.

`Router.allowed(path,reqMethod)` previously included the OPTIONS method whenever any allowed methods existed. The post patch guards that append with `r.HandleOPTIONS`, so setting HandleOPTIONS=false no longer advertises OPTIONS. This is a configuration-sensitive header/client contract, not a pointer-aliasing example. The public test suite's `TestRouterOPTIONS` exercises ordinary OPTIONS flow but does not by itself prove the disabled flag branch.

Our posthoc oracle registers GET /probe, disables HandleOPTIONS, queries `allowed("/probe",POST)`, requires GET in result but not OPTIONS. Parent is expected to fail, post to pass. An HTTP transport-level `ServeHTTP` test would be a different observer and has not been executed yet. The actor's source edit rights remain unverified.
