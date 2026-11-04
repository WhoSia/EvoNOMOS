# Previously pending R24 native source evidence — independently recovered

Run: https://github.com/WhoSia/EvoNOMOS/actions/runs/41754193313
Pinned source code commit: d4f1f6d94745b0c26c494c8afbe9173ce8059d0a
Job ID 126326296279, status completed, conclusion success.
Go: go1.23.2 linux/amd64.
Module: github.com/go-chi/chi/v5 v5.1.0
Sum h1:acVI1TYaD+hhedDJ3r54HyA6sExp3HfXq7QWEEY/xMw=
GoModSum h1:DslCQbL2OYiznFReuXYUmQ2hGd1aDpCnlMNITLSKoi8=

Raw GET-only Chi vs standard Go:
- HEAD /items/alpha: standard 200; Chi 405 Allow GET.
- POST /items/alpha: both 405; stdlib Allow GET, HEAD / body Method Not Allowed; Chi Allow GET / empty body.
- OPTIONS same 405 status but Allow/body mismatch.
- GET /items/a%2Fb: stdlib body a/b; Chi body a%2Fb.
- GET /items/%61lpha: stdlib alpha; Chi %61lpha.
- HEAD /items/a%2Fb: stdlib 200; Chi 405.
- GET /items/%2e%2e: stdlib ..; Chi %2e%2e.

All 3 tests passed:
TestRawChiHEADCounterexample, TestDeclaredSixProbeMatchedBaseline, TestStagewiseSafeSameRightsTie.
The latter reports stage0=0, stage1=1, stage2=2 synthetic app-route additions in both systems *after matching six protected probes*. Initial Chi HEAD adapter is a nonzero excluded normalization expense. This motivates P44.
