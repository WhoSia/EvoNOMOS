# P44 mathematical research decision — source sublanguage completeness before more full-Go rhetoric

## Decision

Previous F12 and F13 reference checkers accepted externally supplied graphs and trace universes. They were logically valid finite toys, but did not prove source extraction. Following the newly verified White et al. 2014 MUSCLES formalism, mere multi-step costs, feature drift and path constraints are ALREADY known. Stop claiming those concepts might be independently new.

The smallest defensible next research unit should derive BOTH artifacts from one actual parsed Go program in a tiny closed fragment:

- a fixed Go source file in a strict AST grammar: `package fixture` and exactly two zero-argument functions, `Legacy() string` and `Future() string`, each returning exactly one string literal;
- a fully enumerated finite edit policy `Future` constant-literal replacement, with allowed literal domain declared in advance, and no other actor rights;
- a finite observer over both legacy and future outputs, whose meaning is **defined** in this pure no-input source subset by AST literal extraction, with no concurrency, reflection, middleware, IO or runtime scheduler;
- derivation of every source edit edge by explicit membership in the policy domain, preserving legacy client return value, and resulting after-source AST parse;
- exact full enumerative oracle and an independent abstract certificate checker with lower/upper cost.

The restriction to a finite **declared** language/rights domain is an advantage for mathematical rigor, not evidence that arbitrary Go source can be comprehensively enumerated.

## Formal completion obligations

1. Specify the lexical and AST grammar, reject any code outside it (no silently ignored declarations).
2. Prove the extractor is complete relative to the declared edit policy for that grammar; do not equate that with full Go source.
3. Joint-observer C consists of exactly the two function results under that pure interpretation. The `Legacy` result is preserved at each path state.
4. Check new future demand (e.g. `Future()` returns selected target literal), rights, source parsing, and a consistent nonnegative synthetic cost (one literal replacement).
5. Compare source-derived exact enumeration to a classical BFS/Dijkstra oracle, and measure certificate bytes/graph sizes before any benefit claim.
6. Verify test and static checks in actual original Go CI, and leave all broad G1–G7 / LAW-R2 source assertions open.

## Classical competition

White et al. (2014) already solve abstract stage configuration constraints and path cost with CSP. For this restricted source language, an equal-information exact classical state-graph search is likely sufficient and may be faster than an elaborate certificate. Record TIE where appropriate. Source-derived proof obligation and true observer semantics are the only present reason for this controlled experiment.
