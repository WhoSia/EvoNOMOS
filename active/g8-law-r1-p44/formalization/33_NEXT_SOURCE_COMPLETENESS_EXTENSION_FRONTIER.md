# P44 after F14: one-construct source language expansion strategy

2026-11-05. PLANNED RESEARCH, not an executed or proved source semantics result.

## Why the F14 closure matters and why it is inadequate

F14 proves enumeration completeness relative to a syntactically complete *single literal replacement* edit grammar, and a pure fixed source context with exactly two constant-return functions. Real Go compiler test witnesses match the AST observer for the three permitted source configurations. The result is deliberately small and easy: an exact classical enumeration yields same answer and a source certificate adds no demonstrated predictive power.

## Next source construct: finite input-dependent branch

A minimal meaningful challenge is to add a single boolean input for a branch in Future:
  func Future(flag bool) string {
    if flag { return "A" }
    return "B"
  }
but retain Legacy() as the protected no-arg constant. The observer is now a *joint input/output* relation for flag=false and true, not one unconditional literal. A source edit policy must explicitly enumerate which branch literals are independently editable, how branch order affects old clients, and whether new syntax/return expressions are permitted. A conservative parser must reject unmodeled control flow, comments/build directives, closure captures and nonliteral branches.

## Mathematical obligations before code

1. Define well-typed AST grammar including exactly one if statement, one trailing return and at most two string literal terminals; prevent unmodeled statements and shadowing.
2. Enumerate all `|D|^2` branch-output combinations and the corresponding authorized one-terminal edit transitions. If each terminal can be replaced by any distinct value, there are `2*|D|^2*(|D|-1)` directed labeled edits, assuming branch position is part of state identity and all states are admitted.
3. Define joint observer outcomes at both possible boolean inputs, and old-client contract C as a predicate on the **pair** (input, output), not merely separate marginal output sets. Specifically test that a change swapping return literals can preserve output sets but violate the joint input/output contract.
4. Compare source-certificate results against an exact classical product-state graph or simple CSP, with equal code/input knowledge.
5. Confirm transformed files actually compile and run and independent negative controls reject unsafe legacy modifications or hidden compiler directives.
6. Preserve F14 exact source grammar and source commit SHA as a sealed baseline; branch extension should have its own definition, tests and version notes.

## Stop criteria

If the larger sublanguage requires a heuristic completeness guess, falsifies a protected client contract, or depends on hidden build/runtime semantics, leave UNKNOWN and do not promote a law. If a classical exact product automaton handles the same task with same precision and lower cost, record classical TIE. General source rights, safety, aliasing/concurrency and human costs remain open.

## Study provenance

White et al. 2014 already cover sophisticated multi-step constraints and drift through CSP; 2009 precursor currently not located in Drive. Borodin/El-Yaniv titled 1998 scan present but corrupted. Read and compare these before proposing any new evolutionary path principle.
