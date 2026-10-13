# EvoNOMOS P42-P2-R11-P2 — History-Sensitive Authority, Ruby/Go Source Semantics, and Conditional Architecture Reversal

**Disposition: BOUNDED ORIGINAL-RUBY MAINTAINER SOURCE PASS; RESEARCH RUBY CONTEXT REVERSAL PASS; PRIOR GO PASSES RETAINED; GENERAL NOVELTY HOLD. P42 RUNNING / P43 HOLD / LAW-R2 NOT_AUTHORIZED.**

## 1. Four original PDF rivals: acquired, PDF-inspected, normalized into Research OS 10_PAPERS

The actual uploaded original PDF front pages, internal statements, bibliographic forms and selected sections were examined. Original PDFs were renamed and moved from 00_INTAKE to 10_PAPERS without replacing their bytes or IDs.

- **Song & Cho (2025), CCR 2.0: Refinement, Unary, and Relational Separation Logic**; arXiv 2507.04298v2; 34 pages; SHA256 06bca6494ab07224d827ac9ec3d7e85744d379e9e77959a083d0e90870be705c; [original Drive PDF](https://drive.google.com/file/d/1j5yfy4LMVwmtZevZLV_TGo_7O-AvuutH/view). Note the exact downloaded PDF title differs from the arXiv search-display alias "CCR 2.0: High-level Reasoning for Conditional Refinements." Original §4.1 establishes **Enhanced Vertical Compositionality** with composition of conditions; §4.2 develops vertical framing and separation-logic simulation; §7 gives substantive model counterexamples. Naïve frame or transitivity arguments from R11-P1 do not outdo it.
- **Gäher et al. (2022), Simuliris: A Separation Logic Framework for Verifying Concurrent Program Optimizations**; 31 pages, DOI 10.1145/3498689; SHA256 b5e95723de7164f3d775f58fbf2ada9bf84518a4049f468bf3e9f4a89dcb256c; [original Drive PDF](https://drive.google.com/file/d/1w5g28mYNDVpmyhEaXFn1LDF0nxgTkl9s/view). Owns a strong concurrency-aware relational refinement competitor (including fairness/termination), not refuted by any current Go/Ruby source fixture.
- **Jung et al. (2018), Iris from the Ground Up: A Modular Foundation for Higher-Order Concurrent Separation Logic**; 73 pages, JFP 28 e20, DOI 10.1017/S0956796818000151; SHA256 867758274a943b2173a032d60a599e35a2cb42bd2319fdb5c1fe973e10372b1f; [original Drive PDF](https://drive.google.com/file/d/15ed-nbT1uTSKIk4i_JYklUADxHXM1-8F/view). Resource algebras, ghost state and frame-preserving updates are strong prior art for representing temporal permissions; merely adding permission tokens is no mathematical novelty.
- **Sammler et al. (2023), DimSum: A Decentralized Approach to Multi-language Semantics and Verification**; 39 pages, POPL, DOI 10.1145/3571220; SHA256 db10eef3c759a3433e5ca64976e6eba9301c9acce11daf082e736461ccaa93d5; [original Drive PDF](https://drive.google.com/file/d/16-oUcYkqEL8p0dW4Py42aiTKzYcjvqHb/view). Its language-local event synchronization, Kripke relations and wrappers make it a powerful competitor to any proposed Go/Ruby joint metalanguage.

**Source honesty:** these primary-paper points come from the actually loaded full-text PDF files, not merely web abstracts; inspection of sections is not a full independent reproduction of the authors' Rocq/Coq proofs.

## 2. Real original historical Ruby source and native execution

We replayed the original Rack maintainer edit [444dc8a130663159ed490f25948b73ff9b5fbba0](https://github.com/rack/rack/commit/444dc8a130663159ed490f25948b73ff9b5fbba0) (Samuel Williams/ioquatix, 2023-07-19) on the authentic repository's lib/rack/builder.rb:

- BEFORE commit af9e278ffd9024f325e595f18bace4f9b7e931d7, original blob 80c073148e6a52bc9deeb1219b8e873f610fbe92. An old no-options Rack::Builder application returned 200 in native Ruby, and Builder lacked the new options API.
- AFTER commit 444dc8a130663159ed490f25948b73ff9b5fbba0, original blob 9faeffb7868021d17fad26118b426a6bd1819d53. The same old application returned 200, and new Builder.new(foo: :bar).options[:foo] returned :bar.
- Preseal [R11-P2 Ruby source and authority contract](../../tools/p42/p2-r11/frozen_p2_ruby_source_history_authority_preseal.json) at eb6667249c1b393be172cae405af812ab9fcca55 BEFORE test generator and workflow. Real Ruby 3.3.12 [original Rack/authorial source court #38335832818 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38335832818), original job 115095563263 and artifact 11784294919, SHA256 1e5cf23bc3d63ed20a3dd580d914fadd7abced987ad813ffd15dca4.

This is genuine maintained **one-repository source evolution**, not independently authorized cross-maintainer revisions. The observed old/new API compatibility is an expected semantic result, not a new design law.

## 3. Separate research-authored Ruby source-history falsifier

The [Ruby native court](../../tools/p42/p2-r11-native/history_sensitive_ruby_court.rb) instantiates a base Core#fetch and two modules Trim (strip then super) and Guard (reject padded input then super), using genuine Ruby Module#prepend and introspecting actual class ancestors.

| Research-authored prepend event history | Ruby runtime lookup order | Old fetch("2") | Future fetch(" 2 ") |
| --- | --- | --- | --- |
| Guard then Trim | Trim, Guard, Core | ok | ok |
| Trim then Guard | Guard, Trim, Core | ok | rejected |

The **unordered inventory of the three source-definition modules** is identical but application history changes runtime method resolution. If source identity includes all entrypoint/load events, the worlds need not be source-identical, and ordinary Ruby lookup semantics predict the result exactly. Context-specific future demand acceptance vs rejection reverses which composition is correct, with unchanged old consumer. This is **demonstrated feasibility/behavior reversal**, not a measured engineering-cost reversal in real commercial code.

The research-authored AuthorityLedger also confirmed source-level edit permission at epoch 0 and denial after revocation epoch 1. This is NOT actual GitHub ownership authority; never equate commit authorship with legal edit rights.

## 4. History-enriched state and source semantic extraction obligations

Define a research abstraction h=(B,L,Gamma,rho,O,D,tau), where B denotes code blobs/build configuration, L compiled or runtime dynamic call resolution, Gamma time-indexed *authorized source edit* policy, rho runtime/heap ownership, O grandfathered old-client contracts, D independent future demand family, and tau effective change/publication history.

An edit labelled (principal,patch) is legitimate only if all deployed intermediate linked programs build or run, its principal has valid consent/rights for that edit epoch, all relevant old clients remain within the declared trace contracts, and memory/semantic frames remain valid. **Runtime memory ownership, source-edit permission, and evidentiary authority are separate concepts**. A GitHub username/commit proves an authored modification, not authorization over another project.

## 5. History-erasure congruence theorem (standard, non-novel)

Let H be a deterministic partial labelled transition system of enriched source/runtime/history states with each action a giving a partial successor T_a. Let pi:H->Q be a proposed architecture summary. Assume for all h,h' with pi(h)=pi(h'):
1. old-client Good and every declared Goal_d agree;
2. each authorized buildable action a is enabled at h iff at h';
3. whenever T_a successors are defined, pi(T_a(h))=pi(T_a(h')).

**Theorem H:** for every finite action word w, its feasibility, prefix safety and final goal result are functions of pi(h) alone.

*Proof:* Induct on the length of w. The empty word is covered by (1). For a nonempty word, (2) determines enabledness and (3) fixes the next summary, after which apply the induction hypothesis for the remaining suffix. Hence the result and each prefix are invariant on pi-fibers. QED.

For the **full language of current predicate observations, enabledness tests and next-summary observations**, these conditions are also necessary, by zero- and one-step distinguishing contexts. For narrower test languages, coarser summaries may suffice.

**Counterexample/finite extraction:** model four states (Trim/Guard outer lookup) × (source edit grant currently active/revoked). An unordered module-source inventory cannot predict demand success or authorization. Each of lookup order and grant alone is insufficient; the pair is sufficient for this small declared observation language. The [checker](../../tools/p42/p2-r11/check_history_quotient.py) exhausts the four states, but does not mechanize Ruby or Go semantics. This is ordinary bisimulation/congruence reasoning, fully compatible with known TCS approaches.

**Source-interface certificate remains OPEN:** soundly extract runtime lookup (Ruby require/prepend/method_missing/refinements) and compiler/linker semantics (Go package, module graph, interface and aliases) plus owner rights from actual repos, then prove these projections satisfy premises (1)-(3) for specified clients and authorized actions. This is what strong CCR 2.0/DimSum/Iris attacks must test.

## 6. Conditional SOLID as non-circular interpreted fragments

The ambient model defines typed programs, source edits, old/future observable traces, resource rights, clients and objective families **without any SOLID assumptions**. Optional fragments may be *interpreted* as: SRP, demand-relative edit-support separability; OCP, authorized safe extension while preserving a declared protected core region; LSP, conditional client trace-substitution refinement; ISP, client footprint of actually needed capabilities; DIP, factoring dependencies through a stable contract for the specified evolving partners. These are not canonical or universally necessary/optimal SOLID laws. The open discovery problem is a source-derived structural theorem that makes prospective qualitative/quantitative predictions about when these fragments help, fail, and reverse under independent future conditions.

## 7. Strong classical priority and release gate

CCR 2.0 §4.1 Enhanced VC and §7 counterexamples, Iris's ghost/frames, Simuliris's concurrent refinements and DimSum's multi-language event semantics **have not been defeated**. The Rack maintained source history is genuine, but not an authorized cross-owner patch experiment. The Ruby conditional reversal is native-real but from research-authored programs; no field comparison of two genuine maintained architectures exists. No paper-ready general theorem or systematic source extractor is established.

**P42 RUNNING / R11-P2 BOUNDED RUBY + GO SOURCE HISTORY PASS / CLASSICAL ADEQUACY SURVIVES / P43 HOLD / LAW-R2 NOT_AUTHORIZED.**
