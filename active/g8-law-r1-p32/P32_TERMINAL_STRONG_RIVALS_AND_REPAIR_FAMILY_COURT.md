# P32 Closing Court — Source-Rooted Boundaries, Strong Rivals and the Repair-Family Handoff

## Scope of closure
**P32 bounded research package CLOSED / METHOD PASS / SCIENTIFIC LAW HOLD.** Closing a research package is not a claim that the title's "Emergence" has been empirically established. P31's mathematical/bounded predecessors remain unchanged, LAW-R2 remains NOT_AUTHORIZED.

### 1. Literature custody actually performed
Two new user-uploaded PDFs were read by original page text, DOI/title/author identified, normalized **without replacing raw bytes**, and moved after verified parent checks from `00_INTAKE — Literature Radar` folder `1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16` to `10_PAPERS — Canonical Literature Commons` `1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP`.

- Angerer, Grimmer, Prähofer & Grünbacher (2019), *Change Impact Analysis for Maintenance and Evolution of Variable Software Systems*, DOI `10.1007/s10515-019-00253-7`, Drive `1eIyyfug4gQnclMakY7ZxUjgxp83oqNPc`; canonical filename `Angerer et al. (2019) — Change Impact Analysis for Maintenance and Evolution of Variable Software Systems.pdf`.
- Hong, Tantithamthavorn, Thongtanunam & Aleti (2024), *Don't Forget to Change These Functions! Recommending Co-Changed Functions in Modern Code Review*, DOI `10.1016/j.infsof.2024.107547`, Drive `1ZL0atP6tINZJW8a3BZ-kzermZ6nhioe6`; canonical filename `Hong et al. (2024) — Don't Forget to Change These Functions! Recommending Co-Changed Functions in Modern Code Review.pdf`.
- Existing Cai et al. *Design Rule Spaces* PDF had already been in 10_PAPERS; do not recollect. File punctuation: author-year/title delimiter is the em dash `—`; `Co-Changed` uses ASCII U+002D HYPHEN-MINUS. No duplicate full-title DOI match found outside intake in bounded repository search. Source files remain their same Drive IDs.

### 2. Strong baseline and forecast information contracts
**Angerer 2019** represents conditional system dependence graphs (CSDG): nodes/edges of control/data/definition-use dependence with configuration presence conditions; propagates impact conditions to determine *potentially affected* elements or variants. This is much stronger than raw coupling count. Its target is `POTENTIAL_IMPACT`, not automatically a unique required repair or implementation cost.

**Hong 2024** CoChangeFinder predicts functions co-changed after an already existing *initial patch* using past review co-change history and textual features, tested on 66 projects from OpenStack, OpenDaylight, Android, Chromium and Qt and compared to TARMAQ. Its target is `MISSING_REVIEW_COCHANGES`; input includes the initial patch. Comparing it directly against P32 pre-implementation-from-requirements cost forecasts would be a task and information-budget mismatch.

Explicit information ladder:
- `I0`: source at frozen commit + a prospective requirement text, but **no candidate patch**.
- `I1`: I0 + *proposed initial patch*, appropriate for Hong's code-review target.
- `I2`: post-implementation actual edits, tests, costs, functionality observations.
All B0+/B1/B2/H comparisons must match both information budget and target. If a predictor needs I1 when others only get I0, report NOT_COMPARABLE and do not award H victory.

Three different output objects are not interchangeable:
- `Impact(G,p,c)`: potential dependents of a proposed code change p under configuration c, often an overapproximation.
- `Repairs(a,d)`: **family of admissible source changes** satisfying a demand d and fixed oracle for design a.
- `Observed(a,d,policy)`: realized modifications, validity, and (S,L,C,A,Q) from a concrete implementation policy.
No automatic arrow from potential impact to required repair or observed lifecycle cost.

### 3. Source-pinned *negative control*, not a new prospective success
Independent post-birth Uptime Kuma issue [#7639](https://github.com/louislam/uptime-kuma/issues/7639) (2026-07-28) reports certificate-notification template context defaults. The fixed **2026-04-26** source commit `398482d590daaac0d44e288c9be3bc6f6667f8b8` shows:
1. `server/model/monitor.js::sendCertNotificationByTargetDays` invokes `Notification.send` with **two** arguments, not a monitor context.
2. `server/notification.js::Notification.send(notification,msg,monitorJSON=null,heartbeatJSON=null)` passes optional contexts to the provider.
3. `server/notification-providers/notification-provider.js::renderTemplate` uses the dummy values when `monitorJSON` is null.
4. P2 DISP/DUAL's changed membership-registry declaration placement **does not directly supply the missing contract argument**.
The exact files are verified by Git blob identity (`2ad572e...`, `b1a42d0...`, `4207917...`). `tools/law-r1-p32-contract-probe.py` checks bounded call shape, defaults and fallback; read-only hosted workflow `37806525690` and latest `37806669570` **SUCCESS**. The issue's reported symptom was observed before selection and this is SOURCE-SIGNATURE ONLY, *not* an independent blinded prediction or full behavioral oracle. A strong CSDG/SDG baseline could also identify this flow; H receives **NO NOVELTY CREDIT**.

Real issue [#7576](https://github.com/louislam/uptime-kuma/issues/7576) merely adds another provider and largely repeats the strong B0+ membership-site baseline; [#7594](https://github.com/louislam/uptime-kuma/issues/7594) voice-mode extension requires Plivo from subsequent #7584, not in the frozen birth source (file `server/notification-providers/plivo.js` is absent at birth). A clean source-comparable preregistration of this two-demand chain was NOT performed. Do not count these as independent strong-rival defeats.

### 4. Theoretical boundary and next object
Weighted fixed owner coverage `C(X)=Σ_{m∈∪_{d∈X}U_d}w_m` is a standard monotone submodular function with `I(x,y)=-Σ_{m∈Ux∩Uy}w_m≤0`. But if a policy may select among *alternative admissible architectures* after seeing a demand **set**, the lower envelope of modular costs may have positive interaction. The existing checker finds synthetic `I=+2`. Neither theorem licenses a new law.

More fundamentally, source obligations are **not a unique necessary edit set**. A demand may admit distinct subset-minimal valid repairs, e.g. `R={{a},{b,c}}`. Their intersection is empty though every legal repair has positive cost. For weights (3,1,1) the optimal repair cost is 2; for (1,3,3) it is 1. This is a standard finite set-system fact (verified by `tools/law-r1-p32-coverage-check.mjs`, hosted `37806669570` SUCCESS), and a compelling argument to treat **minimal admissible repair antichains** and strategy selection as the next modeling target. This is only an abstract toy; source-level admissibility for these alternative repairs has not been shown.

P32 commits and reproducible source:
- `tools/law-r1-p32-obligation-extract.py`: 50 pinned declaration instances/typed edges across two existing historical demands and two arms, with SHA/line/type/source; synthetic destructive-mutation PASS, hosted baseline `37800703213` SUCCESS.
- `tools/law-r1-p32-contract-probe.py`: separate pinned real source negative control, hosted `37806525690`, `37806669570` PASS.
- `tools/law-r1-p32-coverage-check.mjs`: 256 fixed-owner mask-pair standard math check, architecture selection envelope and repair antichain examples.
- Existing `P32_COVERAGE_BARRIER_POLICY_ENVELOPE_AND_RIVAL_CONTRACT.md` and source recovery are retained.
- No general AST soundness, production Q, H>B0+/B1/B2 differential, universal OO mechanism, conditional SOLID theorem or LAW-R2.

### 5. P32 → P33 scientific discontinuity
**P32 terminal ruling:** `CLOSED_METHOD_PASS__NEGATIVE_CONTROL_PASS__STRONG_RIVAL_DISCRIMINATION_HOLD__LAW_R2_NOT_AUTHORIZED`.

P33 may open to pursue **admissible repair-set semantics and prospective source-grounded choice** only after this bounded closure is read back. The new task must not score the P32 witness twice. Its falsifiers: ill-defined equivalence between repairs, implementation-policy nonidentifiability, no admissible source realization, an adequate CSDG/DRSpaces explanation, or no genuinely prospective demand. P33's job is not to relabel this negative P32 as a positive law.
