# P44 F13 finite trace-evidence original CI verdict — 2026-11-05

**GitHub Actions run #41956125916** https://github.com/WhoSia/EvoNOMOS/actions/runs/41956125916 completed SUCCESS at source commit 0b2cfd93bedeedeb5858d608d45e5b41af8ec807, original job 127011323909; raw job log inspected. Go1.23.2 linux/amd64; six tests, go vet and race PASS.

The finite test suite:
- TestFiniteSafeOnlyWithSoundOverapproximation: one successful reachable sample does not prove universal safety; sound overapprox enclosing all possible traces can.
- TestReachableBadTraceProvesViolation: a source-realizable bad trace proves an existential violation (under finite reference assumptions).
- TestPhantomBugWitnessRejected: underapprox containing an unrealizable bad trace is rejected.
- TestHiddenBadExecutionInvalidatesOverapproxSafety: an apparently safe overapprox that omitted a real bad execution is rejected when full finite truth is supplied.
- TestAuthorizedRepairPathNeedsAllCheckpointProofs: old-client safety needs full certified coverage at each protected release; a bad or unknown intermediate rejects universal safe path claims, and unauthorized edits are not permitted.
- TestConflictingEvidenceCannotBothProve: mutually incompatible proof flags are rejected.

Raw CI evidence includes INCORRECTNESS_WITNESS proven_unsafe=true and SOURCE_OBSERVER_COMPLETENESS missing_bad_trace_detected=true.

**Crucial scope:** The finite model is supplied the actual realizable traces by the test. In a real source analyzer that completeness is precisely what remains unproved. The proof flags UnderCertified and OverCertified are EXTERNAL ASSUMPTIONS, not authenticated by passing tests. No arbitrary Go source semantics, whole-scheduler proof or EAC novelty established.

Together with [F12 edge coverage](20_EDGE_LOCAL_CERTIFICATE_CI_VERDICT_20261105.md), this yields two INDEPENDENT assumptions for any future full safe source-repair certificate. [Two-axis conditional theorem](24_TWO_AXIS_SOURCE_CERTIFICATION_20261105.md). Classical Incorrectness Logic (O'Hearn 2020) and abstract interpretation explain the logic. LAW-R2 HOLD, G1-G7 OPEN.
