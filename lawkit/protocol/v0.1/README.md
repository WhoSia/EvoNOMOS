# EvoNOMOS LawKit Protocol v0.1

LawKit is **not a Rust product**. Rust is the current canonical kernel implementation because it is convenient for a small deterministic executable. The scientific contract is the JSON protocol in this directory.

Any implementation language is admissible if it:

1. consumes the same moderator envelope;
2. emits the same semantic inspection object;
3. preserves authority ceilings and explicit abstention;
4. passes cross-implementation concordance fixtures;
5. never converts CIL-C1 into a scalar design score or universal SOLID/DIP/OCP recommendation.

Current implementations:

- Rust: `crates/evonomos-law`
- Python: `lawkit/reference/cil_c1_v01.py`
- Node.js: independent output verifier in `tools/lawkit-verify.mjs`

Future implementations may use Haskell, Scala, Kotlin, C++, OCaml, Prolog, D, Ada, R, or another language when that language supplies a useful independent semantics or execution property.

The protocol, not any implementation language, is canonical.
