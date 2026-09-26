# EvoNOMOS LawKit — Rust Kernel

This crate is the current canonical deterministic kernel implementation for the language-neutral EvoNOMOS LawKit protocol.

It does **not** make Rust canonical to EvoNOMOS and it does **not** encode SOLID/DIP/OCP as commandments.

Current commands:

```bash
cargo run --release --manifest-path crates/evonomos-law/Cargo.toml -- \
  inspect <moderator-envelope.json>

cargo run --release --manifest-path crates/evonomos-law/Cargo.toml -- \
  adjudicate <moderator-envelope.json> <lifecycle.json> <authority-firewall.json>
```

- `inspect`: pre-outcome CIL-C1 mechanism inspection; decision authority must abstain.
- `adjudicate`: post-outcome coordinate/reversal classification under an explicit authority ceiling.

Independent semantics live in Python under `lawkit/reference/`; independent output/authority verifiers live in Node.js under `tools/`. GitHub Actions checks cross-language concordance.

The scientific contract lives under `lawkit/protocol/`. The protocol, not this crate, is the durable interface.
