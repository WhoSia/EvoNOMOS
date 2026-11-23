# P44 F18 bounded certificate transport — proof obligation and explicit skeptical null

## Preseal
The earlier [F18 pre-execution protocol](45_F18_PROSPECTIVE_CERTIFICATE_TRANSPORT_PREEXECUTION.md) was committed **before** any implementation. The added code only provides a conservative exact-cache form; it is not a fully compositional transported dependency proof.

## Definition
Source s must be accepted by strict, typechecked F17 two-client Go grammar. Trusted issuance gives a certificate c holding SHA-256 of its **lexical Go token sequence** (including semicolon insertion; excluding only whitespace) plus the source-derived alias facts and post-write client outcome. Certificate receipt seal h(c) must be authenticated by a trusted EXTERNAL store/issuer; a bare hash alongside a forged certificate is not proof of who issued it.

For revision s', a verifier first checks the supplied seal against trusted h(c), parses Go and rejects comments/build directives, then lexes Go into a token sequence and compares its digest against c. If match, the entire Go lexical token sequence (under the fixed single-file build context) matches original; existing source semantics and alias facts can be safely reused conditionally on the original typechecked source analysis and compiler/parser trust. No need to rerun `go/types` for the *same* token program. If mismatch, verdict INVALIDATED, never falsely assert an unsafe structure is safe. Bad/malformatted/comment-bearing Go produces UNKNOWN.

This is stronger than accepting an untrusted cached result but MUCH weaker than carrying source-dependent heap proofs across genuinely changed code. Alpha renaming, altered allocation origin, hidden side effects and even semantically harmless syntactic modifications invalidate unless separately proved. The name of the technique is ordinary canonical-token caching.

## Test demands, deliberately finite and researcher-selected
- whitespace-only source change: should reuse with full classical analysis agreeing;
- shared-to-disjoint alias structure: MUST invalidate;
- unsupported directives/malformed source: UNKNOWN;
- altered certificate facts with pinned externally trusted evidence-seal: reject;
- accepted but semantically equivalent local variable renaming: conservative invalidation (false invalidation, not false safety).

The first CI found a real issue: AST go/format printing can preserve source-layout effects, so two whitespace-variant files produced differing hashes. This FAIL verdict is retained; a separate patch replaced AST-printer hashing with exact token-sequence hashing. The retest must be verified at its exact tested source commit before any successful claim.

## Fair benchmark
A, full typed original-source `Analyze` each time; B, ordinary classical exact Go token digest cache; C, current sealed certificate verification including receipt hash. Measure A/B/C plus issuance and invalidation cost. Because B's semantics are identical to C's source identity test, C cannot claim novel incremental algorithm performance. Any runtime advantage over A is a **classical cache effect**. Benchmark time on a tiny fixture is unstable and not a transferable production gain.

F18 must leave LAW-R2 HOLD, G1–G7 OPEN. Harvest/Drive originals are prior art/rival generators and must not be interpreted as source CI.
