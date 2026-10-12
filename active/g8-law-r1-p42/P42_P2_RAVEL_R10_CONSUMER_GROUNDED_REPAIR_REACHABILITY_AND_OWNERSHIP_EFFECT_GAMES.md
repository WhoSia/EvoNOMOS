# EvoNOMOS LAW-R1-P42-P2-R10 — Consumer-Grounded Repair Reachability & Ownership-Effect Games

**2026-10-12 KST · User-authorized official title · genuine 2024 in-repository grpc-go consumer source pinned · pretest manifest sealed · source-edit materialization/hosted native CI submitted but NOT independently verified at this document's initial creation · P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**

## 0. Why test this?

A compiler can prove an adapter implements \`Get(int) *[]byte\` and \`Put(*[]byte)\`. It cannot by itself prove that two outstanding messages are backed by independent memory. Nor can a simple type checker select where to apply the repair: the provider's allocation strategy, an adapter plus composition-root change, or a root-level substitution with an original no-op pool. Those options can have different rights, costs, and migration obligations. R10 asks which **source-realizable** paths remain under each demand and declared local edit grammar. The scientific object is safe future repair capability, **not** a manufactured gRPC production defect or a new SOLID axiom.

## 1. Historical consumer provenance: original 2024 grpc-go, not an authored imitation of mem.Copy

Upstream frozen exact source commit: [grpc/grpc-go 9ab8b62505c85a5e03be1ae97949e960e24b6d4f](https://github.com/grpc/grpc-go/tree/9ab8b62505c85a5e03be1ae97949e960e24b6d4f).

- [mem/buffer_pool.go](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/mem/buffer_pool.go), blob \`c37c58c0233ec0f468563463a8726fcfcc9c5d31\`: the 2024 interface \`Get(length int) *[]byte; Put(*[]byte)\`, original \`NopBufferPool\`, pool-size tiering, and default pool.
- [mem/buffers.go](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/mem/buffers.go), blob \`975ceb71853da3445d1cba07053ab0b3484773fe\`: genuine production \`mem.Copy(data, pool)\` invokes \`pool.Get(len(data))\`, copies bytes, creates an original \`mem.Buffer\`, and \`Free()\` returns its buffer to the pool on the last reference. Small buffers at or below the **1024-byte threshold** are a separate \`SliceBuffer\` path; the frozen test intentionally uses 2048 bytes to cross the branch.
- [internal/transport/http2_client.go](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/internal/transport/http2_client.go), blob \`ff84a3216922e10e492f8d137d5d5f042efc0f2d\`: original HTTP/2 client frame-data receive path passes \`f.Data()\` to \`mem.Copy(f.Data(), pool)\`.
- [internal/transport/http2_server.go](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/internal/transport/http2_server.go), blob \`9a42644787a6420f87fd4fdf9d38f682fcb9feb9\`: analogous original server call path.

These are **historically contemporaneous source call sites inside upstream grpc-go**, unlike the 2026 Heroku/Cortex snapshots mistakenly eligible for 2024 contemporaneity in earlier exploratory stages. However, R10 has **not** found or certified a separately maintained third-party 2024 client using this precise two-outstanding-buffer pattern. The test stimulus and replacement providers are researcher-authored. Presence of original call sites is not proof that the exact two-copy schedule was encountered in production.

## 2. Preregistered fault domain and provenance

[Frozen pre-experiment manifest](../../tools/p42/p2-r10/frozen_historical_grpc_consumer_and_repair_graph.json) committed **before** the [new R10 source generator](../../tools/p42/p2-r10-native/make_source_variants.py), standalone Go module, or [read-only native workflow](../../.github/workflows/g8-p42-r10-original-grpc.yml) existed.

- Preseal immutable EvoNOMOS commit: [c8d8199d63e9c2f4e2e4e7fd2f1435fccd3e5079](https://github.com/WhoSia/EvoNOMOS/commit/c8d8199d63e9c2f4e2e4e7fd2f1435fccd3e5079).
- Original 2024 gRPC upstream source is read-only. The workflow checks exact Git HEAD and four original Git blob SHAs; freeze ancestry and byte identity; and nonexistence of the R10 native fixture at freeze time.
- \`make_source_variants.py\` creates four physically different Go source trees. It rejects an unexpected repair source-file footprint and generates an audit receipt. The actual Go tests import original \`google.golang.org/grpc/mem\` from the pinned original repository, not a local reimplementation of \`mem.Copy\`.
- This is a **researcher's declared edit grammar**, not a survey of all possible Go patches, nor a statement about historical upstream modification rights.

## 3. Four source edits under two client contracts

The preregistered selected observation first constructs and retains \`mem.Copy(2048 × 0x41, selectedPool)\`, then \`mem.Copy(2048 × 0x42, selectedPool)\`, checks the first original \`mem.Buffer.ReadOnlyData()[0]\`, and only then calls \`Free()\` on both. All \`ReadOnlyData()\` calls are reads. The fault arises from the shared provider's source-level aliasing via \`Get\`, not from mutation of a returned read-only view by the test.

A second *research-declared migration contract*, **not universal gRPC producer obligations**, checks whether the selected authored provider or its legacy backend records two \`Put\` operations after both original \`Buffer.Free\` operations.

| Source-realized candidate grammar | Files changed relative to authored shared baseline | Preregistered first byte | Isolation contract | Research return-accounting |
|---|---|---:|---|---|
| \`base_shared\` | 0 | \`0x42\` | FAIL | PASS |
| \`provider_repair\` | \`provider.go\` (1 source path) | \`0x41\` | PASS | PASS |
| \`adapter_repair\` | \`adapter.go\` added + \`root.go\` changed (2 paths) | \`0x41\` | PASS | PASS |
| \`nop_repair\` | \`root.go\` changed (1 path) | \`0x41\` | PASS | FAIL (no designated backend) |

**These are frozen predictions until the original-Go hosted receipt is independently inspected.** A file-path edit count is not engineer hours, LOC, patch byte size, minimum possible program or realized runtime overhead.

Two independent valid routes toward the selected isolation contract are of special interest: owner-local provider allocation repair and root substitution with the existing original gRPC no-op provider. They have different impact on the migration return-accounting contract. A third route adds a new legacy adapter and changes root assembly, again under a particular user-declared source grammar.

## 4. Conditional reachability: what is actually mathematical?

Let \`E\` be exactly these proposed source-edit options; \`D_iso\` the observed two-outstanding-copy memory independence requirement, and \`D_return\` the explicit research migration accounting condition. The pre-registered candidate-prediction table entails the following **conditional anticipated acceptance families**, pending native test:

\[
\begin{aligned}
\mathcal{F}_E(D_{\mathrm{iso}})&=\{P,A,N\},\\
\mathcal{F}_E(D_{\mathrm{iso}}\wedge D_{\mathrm{return}})&=\{P,A\}.
\end{aligned}
\]

With \`P\` provider-local repair, \`A\` add adapter/change root, \`N\` root change to original Nop:

- If provider source is frozen but new adapter/root writes are permitted, \`P\` is unavailable; under both demands \`A\` survives.
- If root edits and new adapter addition are denied but owner-local provider edit is allowed, \`P\` is the only declared alternative under both demands.
- If only root edits are permitted, \`N\` can meet isolation but **cannot** meet the designated old-backend Put accounting contract.
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
