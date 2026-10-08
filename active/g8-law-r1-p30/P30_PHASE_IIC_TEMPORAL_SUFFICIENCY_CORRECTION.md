# LAW-R1-P30 Phase II-C — Temporal Sufficiency and Intervention-Signature Correction

## Status
This is a prospective mathematical correction for future candidates. It does not change the precommitted zlib Phase I verdict, observations, or raw evidence. Earlier Phase II theoretical prose is retained as a historical source, not silently rewritten.

## 1. The vacuity trap
Set \(\Phi_{Z,\mathcal I}(s)=(Z(I(s)))_{I\in\mathcal I}\) with \(\mathrm{id}\in\mathcal I\). Then
\[
\Phi_{Z,\mathcal I}(s)=\Phi_{Z,\mathcal I}(t)\implies Z(s)=Z(t).
\]
Thus \(\Phi_Z(s)=\Phi_Z(t)\) and \(Y(s)\ne Y(t)\) is a **subset** of ordinary passive \(Z\)-collisions, but it is not automatically a stronger scientific claim about predicting outcomes under interventions. In particular, if \(Y(s)\ne Y(t)\) already at time zero, the interventional responses are irrelevant to falsifying static factorization.

**Correction:** The Tier-2 test must require a prospective coordinate \(W=(Z,H_S)\) which already repairs *passive current outcomes* on the candidate support, followed by a precommitted intervention word that reveals an outcome difference not predicted by the current \(W\). It is not enough to show an extra equality of \(Z\)-response signatures.

## 2. Predictive sufficiency
Fix a deterministic transition system \((S,\mathcal A,T,O)\), a common public-output contract and a prospective intervention language \(\mathcal L\subseteq\mathcal A^*\).

For a word \(w\), define \(\operatorname{trace}(s,w)\) as the complete public output trace generated from state \(s\) while applying \(w\), including output timing where timing belongs to the public contract.

A representation \(W:S\to\mathcal W\) is **\(\mathcal L\)-predictively sufficient** iff
\[
W(s)=W(t)\implies
\operatorname{trace}(s,w)=\operatorname{trace}(t,w)
\quad\text{for all }w\in\mathcal L.
\]
It is **passively sufficient** iff \(W(s)=W(t)\implies O(s)=O(t)\).

### Theorem 5 — Temporal failure with passive rescue
It is possible that \(W\) is passively sufficient on a support while being predictively insufficient on the same support: choose \(s,t\) with \(W(s)=W(t)\) and \(O(s)=O(t)\), and one frozen word \(w\) for which \(\operatorname{trace}(s,w)\ne\operatorname{trace}(t,w)\).

This is a valid Tier-2 future-behavioral counterexample. It does not refute passive factorization because current outputs are the same.

## 3. Intervention response mismatch versus action mismatch
Define two separately recorded objects:
\[
\Phi^Z_{\mathcal I}(s)=(Z(T_w(s)))_{w\in\mathcal I},\qquad
\Psi^Y_{\mathcal I}(s)=(\operatorname{trace}(s,w))_{w\in\mathcal I}.
\]
Never substitute equality of \(\Phi^Z\) for equality of \(\Psi^Y\).
A strong predictive collision for a *frozen* \(W\) is \(W(s)=W(t)\) and \(\Psi^Y_{\mathcal I}(s)\ne\Psi^Y_{\mathcal I}(t)\).
If even \(\Phi^W_{\mathcal I}(s)=\Phi^W_{\mathcal I}(t)\) persists, record it as a stronger **observational-aliasing persistence** property, not as a necessary ingredient of predictive failure.

## 4. Horizon and distinguishing depth
For \(\mathcal I_L=\{w:|w|\le L\}\), let
\[
d_W(s,t)=\min\{|w|:\operatorname{trace}(s,w)\ne\operatorname{trace}(t,w)\}
\]
over matched \(W\)-states, and record \(\min d_W\) in a candidate with a measured witness; never infer unbounded indistinguishability from finite search.

## 5. Admissible repair and cost
Freeze a finite candidate observable family \(\mathcal A_0\) before the decisive future-output contrast. An \(H\) is an admissible predictive rescue only when \(W'=(W,H)\) is sufficient for the frozen intervention words *on the adjudicated support*. It is deletion-necessary only if removing it restores a measured counterexample. Local support sufficiency alone is not transportability.

## 6. Constructive NP-hardness caveat
The finite collision-edge cover representation is valid. NP-hardness needs an explicit input-class reduction, not a declaration that the algorithm resembles set cover. For SET COVER instance \((U,\{S_j\})\), create for each \(u\in U\) two states \(a_u,b_u\) with a unique shared \(Z\)-label \(u\), public outputs \(Y(a_u)=0,Y(b_u)=1\). Define outcome-independent prospective \(H_j(a_u)=0\) and \(H_j(b_u)=\mathbf 1[u\in S_j]\). The only collision edge in each \(Z\)-fiber is \(\{a_u,b_u\}\), and \(H_j\) separates it exactly when \(u\in S_j\). Thus a repair with \(k\) observables exists iff the set cover has size \(k\). This proves NP-hardness for the unconstrained finite observable-table class. It does **not** prove hardness for every restricted source-realizable or mechanistically admissible class.

## 7. Bounded finite-automaton convergence
For a fully specified deterministic finite Moore machine with \(n\) states, successive partition refinement by current outputs and transition successors stabilizes after at most \(n-1\) strict refinements. Hence a finite structural bound can certify behavioral equivalence, provided the action alphabet and transition semantics are complete and the machine is truly closed and finite. P30 source-level probes normally do not satisfy that exhaustive premise.

## 8. Tier-2 candidate gate (future-only)
- Match \(W=(Q,R,G,H_S)\) directly, without using the public future Y to define \(W\).
- Require same current public observation and passive sufficiency on the candidate support.
- Freeze a nonempty admissible intervention word family before comparing future traces.
- Obtain different future public traces from the matched \(W\)-states under at least one matched word.
- Audit nondeterminism, time, environment, oracle, route, and any structured gate omitted at precommit.
- Classify the result as **failure of predictive sufficiency of W at the frozen horizon and support**, not universal ontology impossibility.
- Any new rescue must come from a separately prospective admissible family. Post-outcome hypothesis generation remains non-confirmatory.
- P30 still cannot authorize LAW-R2, macro law, SOLID, manuscript authority, or nonexistence of finite state.

## 9. Existing authority retained
P29 is CLOSED/PASS; Phase I zlib is exact same-Z/different-current-Y with prospective dictionary-state separation; the Phase II initial set-cover/finite-state boundaries remain useful subject to this correction. No P30 terminal Court is claimed by this document.
