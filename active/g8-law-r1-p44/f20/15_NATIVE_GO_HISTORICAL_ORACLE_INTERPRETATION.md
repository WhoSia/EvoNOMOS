# F20 B — interpretation of parent/post native Go matrix

The research executable `run_historical_native.sh` uses immutable GitHub parent/post SHA pairs, fetches each exact revision, verifies HEAD == requested SHA, logs Go toolchain and go.mod SHA, runs an existing upstream named test, injects a one-test retrospective oracle, and records expected regression at parent followed by expected fix at post. The original source is fetched into a runner temporary directory, not replaced with an invented fixture implementation.

A **parent failing the injected new test is expected**: the runner only classifies it semantic if `--- FAIL: TestF20` is in Go test log; compile/dependency/Go incompatibility is separately marked environment failure. A parent unexpectedly passing or post failing stops the job. Test names, commit metadata and code diff were known before oracle design, so no outcome is independent blind prediction.

Failure modes: unavailable network, package dependencies, toolchain mismatch, tests depending on timing or unrelated modifications, and upstream license conditions. These must be recorded as separate named blockers. CI success would prove a specific same-input historical behavior change, NOT all old clients preserved or measured human costs.
