# P34-P0 — Source-Pinned Graph Projection Versus Contract Information

**Status:** P34-P0 METHOD PASS / M1 NOT BEATEN / LAW-R2 NOT_AUTHORIZED.

## Real source and scientific scope

Frozen Uptime Kuma commit `398482d590daaac0d44e288c9be3bc6f6667f8b8`. Actual `server/model/monitor.js` blob `2ad572e53ed051825425f8783c91195cbd243d77`. Test `tools/law-r1-p34-source-projection.mjs` extracts the real certificate-notification method and executes the unmodified two-argument version versus one experimental edit forwarding structured `monitorJSON` as a third argument. Both emit the same existing certificate message and call the same `Notification.send` method. The tool deliberately projects **only source owner and static call target**, not full imports, typed argument dataflow or other dependencies. That weak projection is equal.

**Old demand:** legacy message preserved in both arms. **Extended demand:** downstream must distinguish name and URL even where their legacy text encoding collides. Across 64 deliberately constructed name/URL collision pairs, actual extracted JS method executions under bounded mocks confirm same legacy message; original sends two arguments with no context, edited arm sends three and distinct structured context. This is the known issue #7639 source world, not new prospective defect discovery or full production Q.

Read-only [hosted run 37885239006](https://github.com/WhoSia/EvoNOMOS/actions/runs/37885239006) SUCCESS; artifact `11595434333` SHA256 `2d6d21523d7dcdcc26c0d5f3d743c49be348cf757a0284b646aaea63180e7d49`.

## Conditional mathematics and strong competitors

If weak graph projection pi(a)=pi(b) but actual contract-channel target F(a,d)!=F(b,d), no exact predictor can express F only through pi on the two source arms. This is the **classical factorization obstruction** already known from P33. M0 graph-call-target sufficiency is falsified for this *chosen narrow target*. However **M1 call-arity-aware/dataflow** easily sees 2 versus 3 arguments, so M2 does not beat a strong static rival. M2 helps explain the relevance of information-loss to a demand; this is an interpretive source case, not a new predictor.

**Prior original literature (all Drive HELD, consulted):** [Fortuna et al. 2011](https://drive.google.com/file/d/1UHNPPeV7e8OEx7o4W0HPvei-T4H0fmib/view) package-install success, [Zanetti & Schweitzer 2012](https://drive.google.com/file/d/1J8s3H7K_NzusAypu6o8gB2hJciZW3z9q/view) module/package graph coherence, [Schäfer et al. 2022](https://drive.google.com/file/d/1aKUdZlBlTNz7FOVFWo0mkoKlQXpqnc44/view) physical Braess. EvoNOMOS Harvest XVI F28–F32 retained in [Cross-Shelf Harvest](https://app.notion.com/p/3f3ef561cf9281819a9fd930746e5ca5). This code result provides no future-maintenance cost, source contract ownership, general temporal LSP, or software Braess proof.

**Next:** source-dependency/ownership extraction and actual temporal refinement under declared client traces. P11 WIDE/SEGREGATED evidence requires independent original readback.

**Verdict:** `P34_P0_CLOSED_METHOD_PASS__M0_WEAK_SUMMARY_INSUFFICIENT__M1_NOT_BEATEN__LAW_R2_HOLD`.
