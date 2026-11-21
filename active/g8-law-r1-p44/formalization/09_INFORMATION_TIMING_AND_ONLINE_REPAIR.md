# P44 mathematical research: prospective repair games and information timing

Date: 2026-11-05. **Classical finite game/online-algorithm formalism adapted to software edits; not a new theorem or source-level claim.** Predecessors: P44 F0–F9, restricted finite repair cost K, stagewise demand disclosure and protected old-client requirements.

## G0: Why offline K is not evolutionary adaptability

The original definition K(p,d) = inf over admissible source edit paths assumes future demand d is known before selecting all edit decisions. Actual maintenance often requires a release commitment under currently disclosed d1, and only later reveals d2. The order matters: a clairvoyant offline repair may choose a different first release for each later demand, while a real developer cannot condition that past release on an unseen request.

Let finite S be source release states, E_pi authorized edit transitions, C0 the protected old-client contract, C1=C0 ∧ d1 the first-stage accepted contract, H1 a set of eligible stage-one release checkpoints, and D2 a set of possible second-stage demands. For each s∈H1∩C1, let Reach_C1(s,d) mean a path from s that is authorized and preserves C1 at every subsequent edit/checkpoint, ending at a state satisfying d.

Define:
  OfflineCover = forall d∈D2, exists s_d∈H1∩C1: Reach_C1(s_d,d).
  OnlineCommitWin = exists s∈H1∩C1, forall d∈D2: Reach_C1(s,d).

Under this FINITE two-round perfect-observation game with deterministic authorized edit semantics, the online condition precisely characterizes the existence of a single stage-one commitment followed by a demand-contingent stage-two plan. Nonanticipation means s is chosen without knowledge of d; the subsequent second-stage path may depend on d.

## G1: Quantifier lemma (classical)

OnlineCommitWin implies OfflineCover by choosing the same s for every d. The converse fails. Let:
  s0→a and s0→b be safe authorized first-stage paths.
  Both a,b satisfy accepted d1; only a,b are allowed first-stage checkpoints.
  a→ax realizes x and b→by realizes y; all a,b,ax,by preserve C1, all costs nonnegative.
  Cross paths a→by and b→ax are absent or unauthorized.
Then for x choose a, for y choose b, so OfflineCover holds; neither a nor b supports both demands, so OnlineCommitWin fails.

This lemma is elementary quantifier non-commutation and known reactive-synthesis/game theory; **not proprietary P44 novelty**. It requires an actual commitment before reveal. If the decision maker may wait to learn d2 before committing, the online requirement collapses to the offline one for this game. If rollback or replanning is allowed, include those in E_pi/costs and recompute the result; never infer permanent impossibility from one restricted grammar.

## G2: Multi-round version

At round k, environment discloses d_k from an allowed set D_k(history), actor uses only observed history to select a finite permitted edit path to a release checkpoint preserving C0 and every earlier accepted demand. An online policy σ maps observed histories to edits; it cannot depend on hidden future requirements. Define Winning(σ) iff for every legal adversary demand sequence all relevant releases and intermediate protected stages remain safe and each disclosed demand is eventually realized before the next forced checkpoint. Model check with alternating quantifiers or a finite turn-based safety/reachability game; specify whether zero-edit release, rollback and environment fairness are allowed.

Cost comparison should use demand sequence d, online policy σ and a specified adversary or probability distribution:
  Regret(σ,d)=Cost(σ,d)-OPT_offline(d).
  Competitive ratio Cost(σ,d)/OPT_offline(d) is undefined when OPT=0 unless convention/additive constant is fixed.
  Existence of feasible offline paths for every sequence does not imply a single online winning policy.
  A vector or unknown human-effort cost makes scalar ratio inappropriate.

## Source certification open gate

Source-level G1–G7 must build the game with verified release checkpoints, sound semantics for app-source edits, stagewise observational contracts, demand disclosure timing, rollback rights and a verified simulation/certificate checker. A finite abstract game that invents nonexistent cross-route edits can spuriously report a winning policy; omitting a real edit can spuriously report failure. Simply running a Go test for the finite game is not a proof about all permitted real source edits.

## Scholarly precedence

- Pnueli & Rosner (1989), *On the Synthesis of a Reactive Module*, POPL, DOI 10.1145/75277.75293: environment/system strategy synthesis from temporal specifications. Public abstract and metadata reviewed, not full mathematical proof.
- Borodin & El-Yaniv (1998), *Online Computation and Competitive Analysis*, CUP: decisions without future inputs and comparison to clairvoyant offline optimum. Public bibliographic material reviewed, not monograph text.
- Evolving Feature Model Configurations in Software Product Lines (2014), JSS DOI 10.1016/j.jss.2013.10.010: published multi-step configuration modeling and cost optimization; abstract reviewed, not full paper.
Google Drive title searches for Pnueli, Rosner, Borodin, and these exact titles returned no matches as of 2026-11-05. This is a **filename search**, not proof of missing bytes. These are candidate missing sources for the Research OS intake list.

## Experimental status

Finite Go control tests at formalization/online/ represent the above graph and prove the conditional example mechanically if CI passes. No standalone P44 new LAW-R2 and no general source soundness asserted.
