# Finite real-source repair cones and conservative conflict certificates

**2026-11-11 · methods note, not a new architecture theorem · source-grammar experiment in progress**

## Mathematical move beyond hand-specified optimizer sets

Let \(\mathcal E\) be an explicitly enumerated finite grammar of Go source repairs and \(A\) a fixed original architecture with retained client contract \(Q_0\). For a later task \(d\) and its explicit customer contract \(Q_d\), define

\[
\mathcal T(A,d;\mathcal E,\Gamma)
=\{e\in\mathcal E:\ e\text{ is authorized by }\Gamma,\
 \mathrm{Semantics}(e(A))\models Q_0\land Q_d\}.
\]

This is the *truly correct bounded action cone* and is generally uncomputable from finite testing alone for arbitrary Go programs. The present experiment DOES NOT possess a real source-owner \(\Gamma\), so at this stage it enumerates syntactically applicable patches on disposable owned research checkouts only.

Instead, executing a finite customer suite \(\mathsf{Tests}(Q_0,Q_d)\) yields a **test-passing repair set**

\[
\mathcal P(A,d;\mathcal E)=\{e\in\mathcal E:
 \text{all selected native tests of }e(A)\text{ pass}\}.
\]

Assuming every actual semantically correct patch passes the deterministic tests that are faithful to the stated contract, **sound exclusion** gives

\[
\mathcal T(A,d;\mathcal E,\Gamma)
\subseteq
\mathcal P(A,d;\mathcal E)\cap\mathcal E_\Gamma.
\]

Any syntactically inapplicable operation is likewise removed. This is an elementary overapproximation, **not a claim that a passing test proves general correctness**. If an observed test is flaky, incorrectly asserts an extra rule, or has broken infrastructure, the inclusion need not hold without repair of its validity assumptions. A source patch may pass every listed test yet break arbitrary downstream clients.

For contexts \(d_i\) that are observationally indistinguishable when an action must be chosen, a **rigorously sound (relative to the bounded grammar and valid tests) incompatibility certificate** is:

\[
\bigcap_i [\mathcal P(A,d_i;\mathcal E)\cap\mathcal E_\Gamma]=\varnothing
\quad\implies\quad
\bigcap_i\mathcal T(A,d_i;\mathcal E,\Gamma)=\varnothing.
\]

The converse fails: a nonempty test-passing intersection need not contain a genuinely correct repair. Thus:
- test-failing is a sound counterexample to correctness for a valid executable contract;
- test-passing is **possible** correctness, not guaranteed correctness;
- empty *overapproximated* common action cone certifies no common repair **within the frozen grammar and rights**, not in the whole possible program universe.

This allows the earlier decision-conflict hypergraph to receive **actual executed source evidence** without pretending to have derived fully optimal actions or true engineering costs. Not novel mathematics: ordinary may/must abstraction and counterexample-based refinement.

## Original source experiment

Inputs are two original Oct9 P35-P7 LIVE and SNAPSHOT Go source files (each exact Git blob pinned), and the independently later but already known #1247 header-case issue. Five precommitted, intentionally nonexhaustive repair operators: none, constructor normalization, two caller normalization sites, remove request normalization, matcher normalization. Run actual original go-chi v5.1.0 and both old and issue-specific new Go test contracts, full upstream suite and vet for named-contract passing repairs. See [pre-execution seal](00_BOUNDED_SOURCE_REPAIR_PREEXECUTION.md) and [Go runner](run_original_source.py).

**Important:** This is a known-demand calibration experiment, not a prospective blinded forecast. The \(\Gamma\) permissions have NOT been authenticated from original maintainers. Do not infer \(\mathrm{Opt}\), labor time, update distribution, general future developer experience, or a SOLID-superordinate law from edit-site count.

## Falsifiable next bridge

A worthwhile next result would provide a sound source-level *must-correct* subset (e.g., by bounded model checking or local explicit contracts) as well as a may-correct set, under actual repository authorization and with strong source-aware classical baselines. The uncertainty band between must and may options, not the number of generated syntax trees, would then help decide whether a proposed information/ownership/interface change is justified. Observe and report *zero* true-client proof coverage when none is formally established.
