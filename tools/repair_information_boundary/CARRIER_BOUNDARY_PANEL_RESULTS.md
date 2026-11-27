# Carrier-boundary panel: source inspection, not a prevalence survey

Panel frozen at 0cdaede495fa87975a7f658d6595c10be47902ef. Production paths returned by the bounded GitHub searches, reviewed in search order; CLI/auth-only and documentation/stub hits excluded. Search ranking uncontrolled. No substitute for unresolved Betamax; no count of all dynamic invocations, no independent maintenance demand.

| Repo, pinned commit | File and blob | Source observation |
|---|---|---|
| requests-cache/requests-cache b6dedd798c231aecd5f13e1010a9373cea81528a | requests_cache/models/response.py 9fe8c3375fe9e74fb67e977ffedb165b7bb1d445 | 62–70 in-place class wrapper; 129–152 copies Response.__attrs__ into CachedResponse, existing CachedResponse uses attr.evolve; 217–224 direct pickle uses dict |
| same | requests_cache/models/raw_response.py e895e551ecf44854043038427d92b612565c244d | 49–63 raw reconstruction via explicit attrs fields |
| same | requests_cache/session.py 6dc27d3b73c3d0be26f2ba88651a8542cfcd0d3e | 224–268 conditional cache hit vs resend, 281–302 super send and wrapping; dispatch hook |
| psf/cachecontrol 661a198159bf5280030cef2b97d8c63a0ef1acbf | cachecontrol/adapter.py d23d74a66ea120d142b1b3144f78a9dc51b557ee | 71 cache-hit build_response; 97–125 heuristics/304 substitution; 156–167 constructs Response via parent |
| same | cachecontrol/serialize.py 5a911ea688460f84cc08260b8048787c9242a1e2 | 20–63 named raw HTTPResponse fields -> msgpack; 88–151 restores urllib3.HTTPResponse |
| same | cachecontrol/heuristics.py d95e78a9d2df0f9e75346c110b55f757d1c379fa | 48–57 raw HTTPResponse header update then return; not necessarily original receive-time header |
| requests/toolbelt bcd5f7be229e14089052be7e3b527ebcea0ae7b8 | requests_toolbelt/utils/dump.py dec0e376648287ca0a331e5f8d60f2ca73970030 | 88–110 dumps selected HTTP response data; output is not promised to recreate a Response |
| same | requests_toolbelt/threaded/pool.py a15e38b090770116a18b4654d6edb7bfc2e060b4 | 121–141 queue result wrapper, 153–184 proxy forwards attrs to original Response |
| same | requests_toolbelt/threaded/thread.py 542813c1fdb7de6fa1bedc55c0601a35c5f44abf | 28–34 passes (kwargs,response) in response queue |
| jamielennox/requests-mock 9742d02a8cad17276dbeba7b300b6d27ae1b6fb1 | requests_mock/response.py 92032623bc065b425c179a2b3aba2d866b306b01 | 140–207 synthetic urllib3.HTTPResponse -> HTTPAdapter.build_response, encoding and cookie modification |
| same | requests_mock/adapter.py b6f00529eedcab2f0a2c846ea85f6f39965fc1f1 | 213–228 matcher calls get_response; 240 onward adapter sends matching result |
| same | requests_mock/mocker.py 3a7be3788065fdfd9645141c8357c9e221b16e7f | 155 onward patches Session.send; dynamic dispatch unresolved without runtime scenario |
| sigmavirus24/betamax | no search hits for Response, serialize, send | UNKNOWN, not evidence of absence |

These are heterogeneous path observations, not a random sample of dependents, and a file count cannot become a boundary-crossing frequency. In particular same-object proxying does not establish carrier survival through every later boundary. Dumping HTTP bytes is an observation transformation, not a compatibility failure. CacheControl's raw-header heuristics precede Requests construction: a capture in HTTPAdapter.build_response is not necessarily the unmodified wire declaration.

## Native experiment on exact released package files

Requests 2.32.5 pins from run.py; requests-cache 1.3.2 v1.3.2 release blobs independently matched installed core files: response 57b7ce20c57f18c28471cdbcc50af4a0046cf39e, raw response e895e551ecf44854043038427d92b612565c244d, cattrs a791cd690498ed1f3963255272fd7e402e84e1a1, preconf 523599c639a20ba7b7c113502d7c06a77ac23efe. urllib3 2.7.0, attrs 26.1.0, cattrs 26.1.0. Do not identify default-branch response.py with released response.py.

Reproduce from tools/requests_header_policy with Python and pinned dependencies:
- python cache_carrier.py NEW_DIR
- python cache_schema.py NEW_DIR

First runner: 3 histories x 7 boundaries x 2 arms = 42 synthetic input-boundary checks. Internal snapshot survives in-place wrap, first conversion and direct pickle (9/9); attr.evolve and actual pickle/JSON/dict pipelines lose it (12/12 mismatch). Explicit caller-owned envelope preserves 21/21; not the same interface/protocol. The initial oracle-fed sidecar run was rejected, and corrected actual capture + envelope rerun retained. Existing body/encoding/text all match. No live request or full upstream suite.

Second runner: extends only requests_cache/models/response.py with typed Optional[Tuple[str, Optional[str]]] field and Tuple import, on top of prior Requests snapshot. Exact experimental blob ba9019a5fd920ba7a0c2286edc35c066c1d15878. Three histories x three native pipelines x three cycles: unchanged cache schema 27/27 mismatch, extended 0/27 mismatch; all legacy body/encoding/text preserved. Four writer-reader schema combinations x three histories x three pipelines = 36 read checks. Old->new correctly unknown, new->new exact, new->old silently loses new field but existing legacy observable preserved. Old->old unknown. Not complete compatibility, not repair of historical payloads and not real owner grant. All payloads locally generated and read only in experiment. No empirical labor. This is a stronger classical schema-evolution explanation, not new LSP law.

Decision: a carrier must survive the composed actual boundary transformations, not merely be located inside the library object. Scope the guarantee to declared chain, serializer schema and rights. Actual deployment/owner approvals and dynamic caller prevalence remain OPEN. Strong alternative sidecar can avoid editing cache schema but changes caller-owned envelope. No generic superiority claim.