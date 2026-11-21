# Expected controlled failure is not a test failure

LiveAlias is a **deliberately logically incorrect treatment** for new D1 and must return v2|req-A under the fixed interleaving, whereas FrozenValue must return v1|req-A. The tests PASS only if both the negative control and repaired positive behavior agree with their precommitted predictions. A failing intended negative control is a genuine refutation of the experimental mechanism.

A mutex protects the app value access; go test -race is an independent guard that should pass for both. A race detector warning would invalidate the planned 'race-free semantic regression' argument, and should be preserved rather than ignored.

The barrier is deterministic for this selected interleaving and does not exhaustively enumerate all possible scheduler interleavings, arbitrary middleware orders or source ownership changes.
