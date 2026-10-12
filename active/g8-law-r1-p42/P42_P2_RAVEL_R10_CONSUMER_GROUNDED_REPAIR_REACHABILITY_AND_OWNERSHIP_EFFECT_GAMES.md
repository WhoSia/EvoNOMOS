# EvoNOMOS LAW-R1-P42-P2-R10 — Consumer-Grounded Repair Reachability & Ownership-Effect Games

**2026-10-12 KST · User-authorized official title · genuine 2024 in-repository grpc-go consumer source pinned · pretest manifest sealed · source-edit materialization/hosted native CI submitted but NOT independently verified at this document's initial creation · P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**

## 0. Why test this?

A compiler can prove an adapter implements `Get(int) *[]byte` and `Put(*[]byte)`. It cannot by itself prove that two outstanding messages are backed by independent memory. Nor can a simple type checker select where to apply the repair: the provider's allocation strategy, an adapter plus composition-root change, or a root-level substitution with an original no-op pool. Those options can have different rights, costs, and migration obligations. R10 asks which **source-realizable** paths remain under each demand and declared local edit grammar. The scientific object is safe future repair capability, **not** a manufactured gRPC production defect or a new SOLID axiom.

## 1. Historical consumer provenance: original 2024 grpc-go, not an authored imitation of mem.Copy

Upstream frozen exact source commit: [grpc/grpc-go 9ab8b62505c85a5e03be1ae97949e960e24b6d4f](https://github.com/grpc/grpc-go/tree/9ab8b62505c85a5e03be1ae97949e960e24b6d4f).

- [mem/buffer_pool.go](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/mem/buffer_pool.go), blob `c37c58c0233ec0f468563463a8726fcfcc9c5d31`: the 2024 interface `Get(length int) *[]byte; Put(*[]byte)`, original `NopBufferPool`, pool-size tiering, and default pool.
- [mem/buffers.go](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/mem/buffers.go), blob `975ceb71853da3445d1cba07053ab0b3484773fe`: genuine production `mem.Copy(data, pool)` invokes `pool.Get(len(data))`, copies bytes, creates an original `mem.Buffer`, and `Free()` returns its buffer to the pool on the last reference. Small buffers at or below the **1024-byte threshold** are a separate `SliceBuffer` path; the frozen test intentionally uses 2048 bytes to cross the branch.
- [internal/transport/http2_client.go](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/internal/transport/http2_client.go), blob `ff84a3216922e10e492f8d137d5d5f042efc0f2d`: original HTTP/2 client frame-data receive path passes `f.Data()` to `mem.Copy(f.Data(), pool)`.
- [internal/transport/http2_server.go](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/internal/transport/http2_server.go), blob `9a42644787a6420f87fd4fdf9d38f682fcb9feb9`: analogous original server call path.

These are **historically contemporaneous source call sites inside upstream grpc-go**, unlike the 2026 Heroku/Cortex snapshots mistakenly eligible for 2024 contemporaneity in earlier exploratory stages. However, R10 has **not** found or certified a separately maintained third-party 2024 client using this precise two-outstanding-buffer pattern. The test stimulus and replacement providers are researcher-authored. Presence of original call sites is not proof that the exact two-copy schedule was encountered in production.

## 2. Preregistered fault domain and provenance

[Frozen pre-experiment manifest](../../tools/p42/p2-r10/frozen_historical_grpc_consumer_and_repair_graph.json) committed **before** the [new R10 source generator](../../tools/p42/p2-r10-native/make_source_variants.py), standalone Go module, or [read-only native workflow](../../.github/workflows/g8-p42-r10-original-grpc.yml) existed.

- Preseal immutable EvoNOMOS commit: [c8d8199d63e9c2f4e2e4e7fd2f1435fccd3e5079](https://github.com/WhoSia/EvoNOMOS/commit/c8d8199d63e9c2f4e2e4e7fd2f1435fccd3e5079).
- Original 2024 gRPC upstream source is read-only. The workflow checks exact Git HEAD and four original Git blob SHAs; freeze ancestry and byte identity; and nonexistence of the R10 native fixture at freeze time.
- `make_source_variants.py` creates four physically different Go source trees. It rejects an unexpected repair source-file footprint and generates an audit receipt. The actual Go tests import original `google.golang.org/grpc/mem` from the pinned original repository, not a local reimplementation of `mem.Copy`.
- This is a **researcher's declared edit grammar**, not a survey of all possible Go patches, nor a statement about historical upstream modification rights.

## 3. Four source edits under two client contracts

The preregistered selected observation first constructs and retains `mem.Copy(2048 × 0x41, selectedPool)`, then `mem.Copy(2048 × 0x42, selectedPool)`, checks the first original `mem.Buffer.ReadOnlyData()[0]`, and only then calls `Free()` on both. All `ReadOnlyData()` calls are reads. The fault arises from the shared provider's source-level aliasing via `Get`, not from mutation of a returned read-only view by the test.

A second *research-declared migration contract*, **not universal gRPC producer obligations**, checks whether the selected authored provider or its legacy backend records two `Put` operations after both original `Buffer.Free` operations.

| Source-realized candidate grammar | Files changed relative to authored shared baseline | Preregistered first byte | Isolation contract | Research return-accounting |
|---|---|---:|---|---|
| `base_shared` | 0 | `0x42` | FAIL | PASS |
| `provider_repair` | `provider.go` (1 source path) | `0x41` | PASS | PASS |
| `adapter_repair` | `adapter.go` added + `root.go` changed (2 paths) | `0x41` | PASS | PASS |
| `nop_repair` | `root.go` changed (1 path) | `0x41` | PASS | FAIL (no designated backend) |

**These are frozen predictions until the original-Go hosted receipt is independently inspected.** A file-path edit count is not engineer hours, LOC, patch byte size, minimum possible program or realized runtime overhead.

Two independent valid routes toward the selected isolation contract are of special interest: owner-local provider allocation repair and root substitution with the existing original gRPC no-op provider. They have different impact on the migration return-accounting contract. A third route adds a new legacy adapter and changes root assembly, again under a particular user-declared source grammar.

## 4. Conditional reachability: what is actually mathematical?

Let `E` be exactly these proposed source-edit options; `D_iso` the observed two-outstanding-copy memory independence requirement, and `D_return` the explicit research migration accounting condition. The pre-registered candidate-prediction table entails the following **conditional anticipated acceptance families**, pending native test:

\[
\begin{aligned}
\mathcal{F}_E(D_{\mathrm{iso}})&=\{P,A,N\},\\
\mathcal{F}_E(D_{\mathrm{iso}}\wedge D_{\mathrm{return}})&=\{P,A\}.
\end{aligned}
\]

With `P` provider-local repair, `A` add adapter/change root, `N` root change to original Nop:

- If provider source is frozen but new adapter/root writes are permitted, `P` is unavailable; under both demands `A` survives.
- If root edits and new adapter addition are denied but owner-local provider edit is allowed, `P` is the only declared alternative under both demands.
- If only root edits are permitted, `N` can meet isolation but **cannot** meet the designated old-backend Put accounting contract.
- These are *hypothetical local edit-policy regimes*. No historical gRPC maintainer's permissions have been proven.

**Mathematical positioning:** Behavioral context refinement cuts down the type-conforming universe. A source-edit graph records which candidate transformations are permitted. Ordinary separation/alias analysis plus constrained shortest paths/hitting sets predicts the same bounded outcomes when it sees the same source and behavior requirements. There is no novel law in a finite acceptance table or a file-name edit count.

Potential meaningful future theorem: establish sufficient—and where possible necessary—conditions on provider region separation and lifetime disjointness that make a repair pathway compositional under real client call sequences. But an assertion for all Go clients, all pool implementations and all concurrency schedules is not justified by this case.

## 5. What this court does not establish

1. **No shipped gRPC bug:** the shared-backing faulty provider is research code; upstream gRPC is unmodified.
2. **No production historical external client cohort:** only original historical in-repo client source has been grounded.
3. **No universal alias safety:** a selected sequential two-copy test is not a concurrency/race freedom proof.
4. **No global minimal Go patch:** candidate and edit grammar were explicitly bounded.
5. **No actual governance permission:** repository source and local research permission are not historical upstream maintainer authority.
6. **No competitive win:** an equal-source classical method-set + ownership/alias analysis model appears fully capable of reproducing this example. Independent implementation and equal-cost testing remain open.
7. **No new P43 or LAW-R2 authority.**

## 6. Evidence status & continuation

- Original historical consumer paths and 2024 blob identities: **GitHub source inspection completed**.
- Frozen predictions and WhoSia-authored immutable preseal: **VERIFIED**.
- Research-authored Go patch fixture and read-only hosted workflow: **COMMITTED**; Go outcome **PENDING external CI result readback** at initial report creation.
- Next scientific gate: a historically genuine independently maintained 2024 consumer; source-to-ownership/lifetime model with actual checked simulation or falsifying trace; independent equal-information classical analyzer; demand sequences that produce non-nested repair option sets or real cost-vector preference reversals.

**Canonical owner: P42 RUNNING. R10 is an evidence-building work unit, not a general TCS theorem. P43 HOLD. LAW-R2 NOT_AUTHORIZED.**

---

## 7. Hosted original-Go receipts: R10 R1 is SUCCESS

[First hosted original-gRPC Actions #38223510662 — SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38223510662); tested EvoNOMOS commit 8f780a1d252a1bc1881cd892370e46e631956d8d, job 114725264857, artifact 11735457125, artifact ZIP SHA-256 93b8c920a23d3b813003f669679b57229f900605172a63d3d9890e5cbef2b10d.

GitHub job logs confirm original upstream commit/file identities, registration of both genuine HTTP/2 mem.Copy call sites, frozen pretest ancestry, and actual Go tests for all four distinct researcher-authored candidate source trees.

| Source candidate | Two live 2048B copies: first observed byte | Authored backend return count | Changed authored source files |
| --- | ---: | ---: | --- |
| base_shared | 0x42 | 2 | none |
| provider_repair | 0x41 | 2 | provider.go |
| adapter_repair | 0x41 | 2 | adapter.go + root.go |
| nop_repair | 0x41 | 0 | root.go |

The shared provider's isolation FAIL is an intended, correctly detected negative-control observation, **not** an upstream gRPC defect or GitHub Actions failure. No patch-cost minimality is established outside the declared edit grammar.

## 8. R10-P2: frozen pooling threshold and original-Go contextual discontinuity

[Second sealed hypothesis manifest](../../tools/p42/p2-r10/frozen_threshold_region_and_classical_rival.json) was committed at 226c431cef0bef41ab33add883397d1a67955849, **after** first R10 Go PASS and **before** authoring the new threshold tests and independent source-region model. The second workflow verifies that antecedent ordering and the unchanged freeze bytes.

[Original-Go and equal-input classical validation #38323501620 — SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38323501620). Exact tested HEAD 00cc93dd9064db0c8aa79b89660c1005c5cb6077, job 115056746384, artifact 11779622864, ZIP SHA-256 1a66585e161c1eb4d16f0368e626f43f622c85d479328b9ab838766861e50f2d.

Pinned grpc-go has pooling threshold **1024 bytes**. The original mem.Copy function returns a separately copied SliceBuffer at sizes <= 1024; at sizes > 1024 it calls the supplied pool.Get, copies into that region, and returns a reference-counted Buffer whose eventual Free calls pool.Put. The following are actual Go runtime observations:

| Candidate | 1024B: first byte / returns | 1025B: first byte / returns | 2048B: first byte / returns |
| --- | --- | --- | --- |
| base_shared | 0x41 / 0 | 0x42 / 2 | 0x42 / 2 |
| provider_repair | 0x41 / 0 | 0x41 / 2 | 0x41 / 2 |
| adapter_repair | 0x41 / 0 | 0x41 / 2 | 0x41 / 2 |
| nop_repair | 0x41 / 0 | 0x41 / 0 | 0x41 / 0 |

**Restricted semantic claim:** for these two still-outstanding mem.Copy operations and fixed 0x41/0x42 payloads, the shared-backed provider destroys independence only on the original pooled branch; if pooling is bypassed or the selected provider allocates a fresh region for each outstanding acquisition, the selected first-byte interference vanishes. This is a precise case-specific explanation derived from 2024 source, not a general alias-safety theorem for all Go programs, goroutines, release orders, or schedules.

## 9. Equal-information classical competitor: full finite adequacy, not originality

[Classical source-region and lifetime audit](../../tools/p42/p2-r10/source_region_classical_audit.py) reads exactly the pinned original 2024 grpc source (Copy, NewBuffer, Free, Nop Get, pooling threshold) and the same Go source trees for the provider, adapter, and composition-root edits. It extracts only a **declared restricted syntax grammar**, deriving regions named slice-copy, shared or fresh; it predicts first bytes and return counts **before** comparing with runtime log lines.

**12 of 12** source-state × size predictions exactly matched both frozen expectations and independent original Go runtime outputs. Four adversarial controls passed: changing shared Get into a fresh allocation changes the predicted outcome; changing root selection to original Nop changes accounting; an unrecognized provider statement causes abstention; and tampering with the original Copy pool.Get link causes abstention.

It is not a general-purpose classical Go points-to solver nor a formally proved abstraction theorem. Nevertheless, even this bounded **classical allocation-region / alias / lifetime mechanism explains all observed distinctions** without new EvoNOMOS-specific axioms. Strong classical adequacy survives; novel theory superiority is NOT proven.

## 10. Scope-relative repair graph and rights boundary

Fix the declared one-step source-repair grammar: P = change provider Get (one authored source file), A = add legacy adapter + modify root (two files), N = choose original Nop at root (one file). For the selected 1024B isolation-only requirement, the baseline itself already passes; **zero edits** are necessary. For a 1025B isolation-only requirement, P, A, and N satisfy the selected observation while the baseline does not. For 1025B isolation plus the **research-only migrated-legacy-backend return-count requirement**, P and A survive but N does not.

Under hypothetical local fixture editing rights, provider-only rights leave P; root-only rights leave N for isolation and no candidate for both demands; root+new-file rights leave A for both demands even when original provider source is not writable. These are source-edit grammar scenarios, **not verified 2024 gRPC maintainers' authorization history**.

No global shortest patch, runtime or labor cost result, full source-to-Lean simulation, independent externally maintained contemporaneous 2024 consumer cohort, or empirical architecture-preference reversal follows from these observations.

**Scientific verdict:** R10 original gRPC four-source Go PASS; R10-P2 12/12 original-Go/classical cross-check PASS; four fail-closed source mutation controls PASS; **classical theory sufficient for all observations**. P42 RUNNING, P43 HOLD, LAW-R2 NOT_AUTHORIZED.
