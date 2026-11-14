# P44-F17 — source-derived alias footprint and typed closed-source proof boundary

Research date 2026-11-05. This work is a deliberately limited extension of F16, motivated by the KSGT-like DFS/BFS research loop.

## The exact gap from F16

F16 executed real Go pointer aliasing, but the independent edit-cost graph was initialized with a manually chosen alias bit. It did not derive this bit from actual Go syntax. Thus it demonstrated classical effect semantics but not source-based identification of the mechanism.

F17 attempts one narrow source-extraction task with a **closed, typed AST grammar**:
- Exactly one comment-free Go file `package fixture`.
- Exactly two type declarations, `Cell struct{ Value string }` and `Clients struct{ Legacy,Future *Cell }`, with no other fields.
- Exactly `Build() Clients`, allocating one shared or two separate `&Cell{Value:"stable"}` cells and returning a keyed `Clients{Legacy:p,Future:p/q}` literal. No other allocations or statements.
- Exactly `Write(c Clients)`, whose only statement is `c.Future.Value="new"`.
- No imports, comments, build directives, closures, callbacks, concurrency, reflection or hidden state; the standard `go/types` checker must accept the file.

Under those conditions the source-local `Build` SSA-style allocation-origin dataflow (not full SSA library) is exact: identical returned pointer origin means aliased, distinct origins mean disjoint. Since there are no intervening mutators or escapes, a `Write` through Future has legacy-visible effect exactly when the origins coincide.

The resulting single-pass recognizer obtains the alias/disjoint fact **from source text**, rather than a manually labelled graph. Source constructors under test are compiled/executed independently using native Go compiler/runtime and compared with the derived legacy-after-write and future-after-write values.

## What a PASS proves if CI passes

A bounded source parser/AST recognizer for EXACT supported syntax agrees with Go runtime behavior for the two tested instances; outside syntax produces UNKNOWN/REJECT instead of false confidence. The F16 safe cost relation in the declared two-operation grammar is then determined by this derived alias fact:
- shared, Legacy==stable: write alone unsafe, split+write synthetic cost 2;
- separated, Legacy==stable: direct write synthetic cost 1.

This does NOT automatically prove source code edit authorizations, the completeness of all Go patches, source code equivalence under different modules/build tags, or any global Go memory model theorem. It does not derive `SplitFuture` and `WriteFuture` as all permitted source modifications from typed source.

## Classical rival / expected result

A standard exact points-to/alias analysis for this no-escape fragment and simple separation-logic ownership reasoning predicts the same effects with the same input. This is explicitly an **equal-information classical TIE**, not an EvoNOMOS mathematical novelty.

Important countercontrols: extra functions, Go build directives, writes through Legacy instead of Future, extra side effects, illegal pointer references, changed initial contents and return-expression constructs the analyzer cannot model must be REJECTED. Small-source recognition can be sound by being narrow; it cannot claim to cover the rejected source programs.

## BFS decision checkpoint

Question again: can structure relevant to future safe repair be extracted from real source and transported with an independently checkable certificate to a new revision, at smaller effort than classical analysis? A closed AST recognizer shows one mechanism but does not measure this transfer. The next meaningful branch should focus on **proof-carrying effect footprint or independent held-out source modifications**, not repeat the same pointer example with new names.

Keep F17 report pending original CI verification; raw source CI failure must be retained with exact causal description. G1–G7 OPEN, LAW-R2 HOLD.
