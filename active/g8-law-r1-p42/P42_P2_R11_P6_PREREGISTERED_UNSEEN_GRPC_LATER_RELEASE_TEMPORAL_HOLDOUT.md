# EvoNOMOS P42-P2-R11-P6 — Preregistered Unseen Later grpc-go Release, Actual Source-Byte Holdout & Temporal Repair-Mechanism Transfer

**VERDICT:** GENUINELY UNREAD LATER SOURCE AT FREEZE · FROZEN SPECIFIC PROPERTY PREDICTIONS ALL PASS ON NATIVE GO. **Not** a preregistered architecture cost comparison; **not** a discovery of new soundness theory or proof of full transport to unrelated software.

## 1. Training/holdout split and source custody

The only source histories used to formulate the frozen predictions were the previously inspected authentic 2024 grpc-go original commits: [2024-10-24 f8e5d8f7](https://github.com/grpc/grpc-go/commit/f8e5d8f704180341e3f1034bc503a324d05d91dc) (large slice capacity vs short length pooling repair; PapaCharlie), [2024-11-18 ee3fb298](https://github.com/grpc/grpc-go/commit/ee3fb2982c88000782b36591c81bf7067ac1f2c0) (no-pool direct SliceBuffer cleanup; ash2k). The previous earlier transport writer commit 3c2a44dc (raghav-stripe) was historical context, not the mechanics of the held-out predicate.

**Before examining holdout implementation**, target was fixed as grpc/grpc-go **v1.78.0**, and four precise predictions with a failure rule were frozen in [frozen R11-P6 contract](../../tools/p42/p2-r11/frozen_p6_unseen_grpc_release_temporal_holdout.json) at WhoSia commit [b118c55cbc21037129a774ee2996c74dc9708957](https://github.com/WhoSia/EvoNOMOS/commit/b118c55cbc21037129a774ee2996c74dc9708957). At freezing, the target tag's actual source files, diff, commit SHA and resource/codec implementation had **not been inspected**. Only *after* freezing did we verify the target tag existence and go.mod version, then check out original source in a hosted workflow.

Later original release ref [grpc-go v1.78.0](https://github.com/grpc/grpc-go/tree/v1.78.0) resolved to **9df039ef2c921978514b600c9d5c6bf25cce54f6**; Git timestamp **2025-12-23**. Original source blobs copied into the hosted run, without modifying the implementation: **mem/buffers.go ecbf0b9a73ea39f3b7a299ba2b060f02beef47d3** and **codec.go 959c2f99d4a735e1990a351eab99880485e273e5**. Test-only fixtures from the already-existing R11-P4 source audit were copied into the checked-out repo, so the tests were not rewritten to fit the later code.

## 2. Frozen predictions and complete observed results

With original Go source and hosted Go toolchain satisfying target go.mod 1.24.0:

| Frozen prediction from 2024 only | Original v1.78.0 native outcome |
| --- | --- |
| len 512, cap 2048, threshold 1024, nonnil pool: NewBuffer(...).Free invokes pool.Put exactly once | **PASS**: observed puts=1 |
| len 512, cap 512, threshold 1024, nonnil pool: no pool return | **PASS**: observed puts=0 |
| With no pool, NewBuffer(&data,nil) and SliceBuffer(data) preserve same tested bytes/Len/Free behavior | **PASS** |
| Original legacy codecV0Bridge remains executable for a compatible Codec and marshals/unmarshals the same test string | **PASS** |

[Actual hosted run #38339315021 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38339315021). Job 115106510769, artifact 11785841859, ZIP SHA256 e134de89d5c61a95fd94d98073754aac4b5d7a33a88f9755dd4d81be17e4d87a. The artifact contains the original commit/author, original blob IDs, frozen specification, and full native Go test output.

## 3. What has been scientifically learned — and what has not

**Supported temporal transfer:** An identified 2024 resource-ownership repair mechanism (distinguishing *logical slice length* from *underlying allocation capacity* for pooling) retained its predicted observable property at the independently unrevealed later 2025 tag. The nil-pool and legacy-bridge observations also transported. This is a properly frozen **temporal holdout of individual source-level invariants**, not just after-the-fact reading of another patch.

**Not demonstrated:** This does NOT establish that the later implementation is internally identical to the 2024 implementation, that all historical buffer usage is safe, that no later source regressions exist, or that the HARC abstraction gives predictive advantage over a straightforward test of grpc-go's existing contract. We did not compare architecturally distinct real implementations' maintenance costs on independently sampled 2025 requirements. Because the target release/version is fixed by the analyst rather than drawn at random from a publication population, it is a **single bounded out-of-time validation**, not statistical generalization.

**Theoretical relation:** HARC's [T1 observation-complete port repair theorem, T2 promise-set antitonicity and five operational SOLID restricted corollaries](P42_P2_R11_P5_HARC_HISTORY_CONDITIONED_REPAIR_CALCULUS_SOLID_AS_CONDITIONAL_FRAGMENTS.md) remain conditional. This temporal success gives evidence for one source-extracted resource predicate, not novel TCS composition logic. CCR 2.0, Iris, Simuliris and DimSum remain live equal-information competitors.

## 4. Decisive next test (R11-P7 candidate)

Do **not** merely repeat this kind of invariance check across more tags. The next genuinely discriminating falsifier is to freeze prospective competing architecture repair routes **before reading target demands** and compare against the strongest classical tools with exactly the same permitted source, history, rights and resource observations. Require:
- two genuinely alternative architectures that were maintained as actual source variants (not cosmetically authored stand-ins);
- a nontrivial future demand whose author/implementation and eligible interface obligations are independent of the desired outcome;
- versioned old-client contract warrant and empirical approval/merge rights as distinct predicates;
- intermediate source/build/resource safety, counterexample witnesses and Pareto multidimensional edit/proof cost;
- conditional structural reversal and explicit failure when an external demand exceeds the verified interface separator;
- OO/Ruby and non-OO/Go first, then independently verify an FP, data-oriented or event-based actual project.

Any novel mathematical-logic superiority claim must survive CCR 2.0 enhanced vertical composition and Iris/DimSum/Simuliris under equal assumptions. Disproof or classical explanatory adequacy is a scientific result, not permission to repurpose a familiar theorem as new law.

**P42 RUNNING · R11-P6 TEMPORAL ORIGINAL SOURCE HELDOUT PASS · HARC CONDITIONAL FRAMEWORK OPEN · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**
