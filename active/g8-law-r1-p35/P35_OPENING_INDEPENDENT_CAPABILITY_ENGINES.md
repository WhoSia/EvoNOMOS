# EvoNOMOS Generation VIII LAW-R1-P35 — Independent Capability Engines, Cross-Operation Change Propagation, Source-Edit Locality & Demand-Conditioned SOLID Cost Geometry

**P35 OPEN.** Existing EvoNOMOS Lab; no LAW-R2 authorization.

P34 confirmed a source-backed negative result: DIRECT and COMPOSED, sharing one storage kernel, each required the same one-method Go edit for the same new rule. Their extra internal dispatch differed, but maintenance source locality did not. The next question is whether **genuinely independent capability engines** differ under changes crossing public operations, rather than under a cosmetic delegation layer.

P35 first gate: build two Restic-compatible Go backends under an identical behavioral oracle. One has a unified private engine; the other independently implements write/read/index/remove engines and an explicit consistency mechanism. Reject implementations that merely forward to the same common storage kernel.

Retain P34's null control, then preregister one capability-local requirement and one cross-operation representation change. Measure actual code edit sets, changed methods and source lines, regression failures and public traces. Compare strong source-aware dependency and repair baselines. Do not infer developer time from dispatch counts.

The original ORIGIN-P12 still has no adjudicated comparative result. Avoid policy/risk-administration drift and bot-authored commits. Next work is Go source and tests.

[Previous P34 terminal](../g8-law-r1-p34/P34_TERMINAL_SOURCE_EDITS_AND_P35_HANDOFF.md).

## P35-P0 technical interface and discriminating tests

**Source requirements:** original Restic `restic.Backend` has 12 public methods; test six core operations against a deterministic history with callback, absent-file, cancellation, partial-load and list consistency checks. Unlike P34, the two engines must not both invoke the same vault implementation.

**U source structure:** unified private `map[Handle]Record{stored,logicalLength}` with Save/Load/Stat/List and Delete over one authoritative representation.

**C source structure:** a distinct writable payload store, independent read decoder, metadata index and removal coordinator, connected only by explicit typed APIs/consistency updates. Merely adding delegates to the same shared map fails P35's independence criterion.

**P35 contrast:** compare a KeyFile-only Save bound (P34 null control) with an encoded-storage change that must preserve Save, Load, Stat and List together. Source change supports must be measured from real Go diffs under matching public tests. An existing source-aware static dependency baseline must be allowed to predict the changed sites; no novelty claim from a known factorization argument alone.
