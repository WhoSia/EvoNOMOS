# P44 F17 — correcting the distinction between runtime actions and source patches

Date 2026-11-05. Research director BACKWARD AUDIT and executable repair unit.

## Fatal terminology hazard detected during BFS

In F16 the cost 2 (aliased: `SplitFuture` and `WriteFuture`) versus cost 1 (disjoint: `WriteFuture`) was measured in **declared runtime/structural operations**. Although these were labelled edit actions in a finite experiment, the `WriteFuture(c,"new")` step is a **runtime heap mutation**, NOT automatically a source code patch. It is methodologically incorrect to present F16's 2-vs-1 as a measured or formally derived minimal number of Go source patches. Earlier dated records remain and now receive this correction rather than being overwritten.

## F17 actual source patch

F17 sourcealias analyzer accepts a fixed, single-file, typed, comment-free Go language fragment with exactly the Cell/Clients struct types, Build constructor and Write method. It distinguishes whether Build returns two client pointers to the same `&Cell{Value:"stable"}` allocation or two distinct allocations, using AST pointer allocation origins and go/types.

`DetachFutureSource` is a REAL original Go AST transformation:
1. requires all closed-grammar, typechecked source conditions (unknown constructs fail closed);
2. for shared Build, inserts a new allocation `q := &Cell{Value:"stable"}`;
3. rewrites `Clients{Legacy:p,Future:p}` as `Clients{Legacy:p,Future:q}`;
4. formats/reparses and independently rechecks supported syntax, intended old-client value and derived disjointness;
5. compiler/runtime tests execute the repaired Go source and verify `Legacy.Value == "stable"` and `Future.Value == "new"` AFTER invoking the unchanged Write function.

Define a different **declared source patch metric**: one `DetachFutureSource` source transformation costs exactly one unit, and a no-op when already disjoint costs zero. A later call to `Write(c)` is a runtime action, not another source patch. For the narrow demand “after invoking Write, old Legacy remains stable and Future becomes new,” the shared initial program requires one permitted source patch and the already disjoint program requires zero. Both have equal initial client values but different structural readiness.

This cost metric is relative ONLY to the explicitly declared patch grammar. It is neither a measured developer effort, a minimal syntactic token-count, nor a full-source minimum across arbitrary Go modifications; alternate allowed source patches could change the optimum.

## The strong classical competitor

Simple exact points-to/alias analysis of Build's two allocation origins plus an obvious compiler-verified refactoring yields the same result. Likewise a classical finite edit graph search on the declared patch grammar yields the 1/0 source patch minimum. **Classical TIE, not new source law.**

## Research relevance and next frontier

F17 addresses one actual gap from F16: source syntax now yields the alias fact and an actual source refactor, and both original and transformed Go versions can be executed by native compiler. But the full permitted source-edit universe is still user/researcher-declared. An actual maintenance cohort needs authenticated permission rights, full client contexts and independent release histories.

The novelty-sensitive next problem is whether a small, separately checkable **source-backed footprint certificate** transports across source revisions more efficiently than conventional points-to analysis and separation logic, not whether aliasing exists.

Original CI of the repaired source experiment must be separately read and linked before marking PASS. F16's original results remain true for its runtime operation metric. F12/F13 source/trace completeness and G1–G7 remain OPEN; LAW-R2 HOLD.
