# EvoNOMOS P42 R11-P10-P8 — History-Residual Factorization and the Finite-Monitor Boundary of Future Source Repair

**Research-question / proof first. Authored 2026-10-17 before any P8 checker. P42 RUNNING. P43 HOLD. LAW-R2 NOT_AUTHORIZED.**

## 0. Why P8, rather than another source parser?

P7's published 32→9 finite deterministic right-receipt calculation correctly minimizes **future action receipts from a fully specified current world** in its frozen grammar. It does not answer whether a concrete source snapshot and externally certified present permissions are *sufficient* to decide client demands about what happened on the path **before the current snapshot**. The four actual original PDFs in [F131](P42_P2_R11_P10_P7_F131_FOUR_ORIGINAL_STRONG_PRESERVATION_TRACE_GPT_READING.md) force us to declare that query language first. In particular Ranzato–Tapparo 2004 Proposition 4.9 warns not to restrict all abstract domains to partitions; Ranzato–Tapparo TACAS 2005 Theorem 4.3 requires assumptions before GPT correctness; Giacobazzi–Ranzato cs/0404048v2 Theorems 3.1, 3.2 and 3.21 exhibit *language-specific* trace/state complete-shell obstructions, NOT an automatic theorem about our repair machine.

This P8 is an **originally chosen research application** of classical Myhill–Nerode derivatives, deterministic monitoring and abstract-interpretation language-relative preservation. No claim that residual languages, regularity or automata minimization were invented here.

## 1. Precise query-scoped semantics

Let E be a finite alphabet of source edit labels. S is a set of current **certified worlds**: source configuration, protected existing-client observation, and externally *verified* current edit authority. A deterministic partial transition \(\delta:S\times E\rightharpoonup S\) accepts an edit only when it is source-realizable, authorized and preserves the declared old client contract *at the step*. Each accepted transition carries an exact finite event plus nonnegative exact vector-cost receipt \(\lambda:S\times E\rightharpoonup O\times\mathbb N^d\). We distinguish a past edit history h, a suffix v and a terminal new-client acceptance language \(K\subseteq E^*\), potentially requiring ordered history. Feasible histories are H; let \(s_h=\delta^*(s_0,h)\).

The valid future completion language at an eligible past h is
\[
D_h^H(K)=\{v\in E^*: hv\in H\cap K\}.
\]
This is a continuation language **from the past h**; do not silently replace it by an endpoint reachability predicate. An \(L_{reach}\) query tests a final goal/available cost frontier from \(s_h\) (with **suffix-relative** cost, not prehistory total). An \(L_{trace}\) query may additionally test a predicate over the old history, stagewise emitted effects and the entire extended history hv, e.g. 'capability A was granted before capability B'. A query language is a selected class of such terminal or temporal client formulae. One may choose regular or nonregular K; the choice is not merely algorithmic.

For the clean factorization theorem below, fix a *single* initial world and query K. For query families \(\mathcal K\), take the joint signature \(\big(D_h^H(K)\big)_{K\in\mathcal K}\). Retain real rights in s; if rights change with history and the current authenticated rights are *not* in s, s is not a certified current world and the theorem's premise fails.

## 2. Mathematical statements and proofs (classical residual mathematics, source-repair instantiation)

**P8-T1 — Source-only exactness iff residuals factor through certified current worlds.**
For eligible histories h,k, a single exact *source-only* future language predictor \(P:S\to\mathcal P(E^*)\) satisfying \(P(s_h)=D_h^H(K)\) for every h exists **iff**
\[
\forall h,k\in H:\quad s_h=s_k\implies D_h^H(K)=D_k^H(K).
\]
*Proof.* Forward direction by applying P to equal arguments. Reverse: define P(s) to be the common value of D on its nonempty history fibre, arbitrary for unreachable s. It is well-defined by the hypothesis. If two equal endpoints have different residuals, their symmetric difference contains a finite future word v witnessing failure of every endpoint-only predictor. The extension to a whole selected family \(\mathcal K\) uses joint residual signatures. There is NO assertion that equality of full future edit receipt transducers is necessary for a **weaker** reachability-only client query.

**P8-T2 — Finite regular history monitors suffice under declared Markov hypotheses.**
Suppose S finite; \(\delta,\lambda\) depend only on the certified current s and next edit label (the *Markov/current-rights premise*); exact future costs are aggregated over the **suffix**, and every selected history-sensitive terminal predicate K is recognized by a finite deterministic monitor \(M=(Q,q_0,u,F)\). The product state \((s_h,u^*(q_0,h))\) is a finite sufficient representation for all subsequent legal edit suffixes, step receipts and K-acceptance, with at most \(|S||Q|\) states (and optionally one rejected sink). For finitely many query predicates, take a finite monitor product.
*Proof.* Induction over suffix length: s controls admissible transitions and exact event/cost receipts; monitor q controls the residual K acceptance. Both successor components depend only on present pair and action. Equality of pairs therefore preserves all suffix receipt sequences and acceptance. This is **sufficiency**, not a claim of minimality or a general-purpose proof of Go source-to-effect fidelity. The smallest monitor of a standalone language K has \(|\{D_h(K):h\in E^*\}|\) states by Myhill–Nerode; a source-product can minimize further in the restricted feasible H and receipt alphabet.

**P8-T3 — No universal finite state-only monitor for unrestricted nonregular history demands.**
In an authored mathematical machine, let the source world be a single state \(s\), all edits a and b be authorized self-loops with equal zero costs and no protected old-client restrictions. Let the *future new-client completion contract* be
\[
K_{balanced}=\{a^n b^n:n\ge 0\}.
\]
For every distinct m,n, \(D_{a^m}(K_{balanced})\ne D_{a^n}(K_{balanced})\): the suffix \(b^n\) belongs after \(a^n\) and not after \(a^m\). Thus infinitely many pairwise distinct continuation languages occur **from the identical source world with identical current permissions**, and no finite exact future-completion monitor exists. This proves a classical language **nonregularity** boundary, not an impossibility for all event-log contracts. Source transitions are purposely self-loops; applicability to a maintained system is **not certified**.

**P8-T4 — A smallest useful finite past-order countermodel.**
Start at source \((A,B)=(0,0)\) with once-only authorized independent edits A and B. Edit A sets A=1 and consumes the A edit right, receipt (event A, cost (1,0)); B analogously sets B=1, receipt (event B, cost (0,1)). Both action orders pass stagewise old-client safety. Both histories \(h_1=AB\) and \(h_2=BA\) finish at **the same exact source, current rights, final observation (1,1) and total vector cost (1,1)**. A purely terminal-goal/remainder-cost query at their final states agrees. The future new client now demands 'A was installed before B', i.e. among feasible complete histories K={AB}. Then \(\varepsilon\in D_{AB}^H(K)\), while \(D_{BA}^H(K)=\varnothing\). By P8-T1, current source+rights is insufficient for this language. The reachable source snapshot set has four elements; adding a finite first-action-order monitor yields five reachable source×history states (ε,A,B,AB,BA), distinguishing the two source-identical terminal states. This is a **finite** past-history obstruction, unlike P8-T3's **infinite** boundary.
*Proof.* Follow the edit transition definitions on AB vs BA; each is legal and installs the same two flags, with the same rights spent and summed costs. Membership of ε in K residual differs. All five reachable histories are distinguishable by the combined terminal installed-flag atoms and K acceptance. This does not refute P7, whose original receipt language is defined on fixed present worlds and future receipts without externally selected past-time predicates.

## 3. Consequences for source-backed research and proof gates

- A **precise state sufficiency test** is now available: must the selected client's residual language be constant on the actual certified-source fibres? Answering 'no' requires only two independently source-valid histories and one admissible continuation v that distinguishes them.
- The relevant difference between \(L_{reach}\) and \(L_{trace}\) is **expressive power relative to the chosen history information**, not which is morally better or always 'more mathematical'.
- Regular contracts permit **history automata**; nonregular/unbounded counters may force infinitely many residuals. Restrictions to actual feasible paths can collapse distinctions; a standalone nonregular policy does not imply every restricted software machine needs an infinite monitor.
- The earlier Giacobazzi–Ranzato trace-shell no-go in its universal temporal abstraction **cannot be deduced solely** from P8-T3's Myhill–Nerode nonregularity. Different concrete semantic universes and different completeness notions. P8 uses that literature as a caution against unlicensed transfer.
- **Exact accumulated historical cost** and budget constraints are not implicitly suffix-relative. If a future demand asks 'have we ever spent more than k before now?', historical cost belongs in monitor state; an unbounded collection of thresholds may similarly require unbounded memory. Fixed cap budgets can be monitored finitely.
- A SOLID-style decomposition is not yet proved. Conditional commutation with independently authenticated owner rights and client trace observability remains P6's issue. Formalizing expressive user demands is logically prior to evaluating an architecture ranking.

## 4. Freeze before implementation

This file is the **P8 mathematical question and explicit predicted finite/infinite witnesses**, committed **before any P8 checker**. If an implementation is done afterwards, the predeclared verification targets are: (1) 5 vs 4 reachable history/source worlds under A/B, identical endpoint and summed cost; (2) terminal reach-only indistinguishability of AB vs BA and past-order query distinguishing; (3) distinct residual witnesses \(a^n,b^n\) for n=1..12, with the infinitude proven on paper rather than extrapolated from tests; (4) independent DFA/source-product and brute-force word-membership agreement for the finite case. The checker must refer back to this pre-code commit and produce a machine-readable receipt; any CI PASS remains **author-created mathematical fixture**, not external-source authorization or architecture forecast.

**Research status: P42 RUNNING; R11-P10-P8 THEOREM QUESTION PRESEALED; G1–G7 source effect/rights unclosed; external truly unseen PR architecture ranking ABSTAIN; P43 HOLD, LAW-R2 NOT_AUTHORIZED.**
