# G8 LAW-R1-P31 — Predictive State Versus Decision-Sufficient State

## Status
P31 mathematical framing and prospective restricted decision class, written after the P30 terminal Court and before any P31 source-pinned action-grid outcome. This is not a closure or LAW-R2 authorization.

## 1. The target
P30 demonstrated that matching visible present observations need not predict a common future action response, and that an admissible historical coordinate can restore local predictions. P31 now asks a different question: when **two structural interventions** have different correctness and lifecycle cost, how much historical information is necessary to **select** the right intervention?

Source-grounded first calibration uses SQLite \`events(id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT NOT NULL)\`. Current public rows are empty in every arm, while a pre-treatment allocator sequence value \`h\` is directly audited. Environment \`e\` supplies the legitimate requirement \`next_id >= m\`. The requirement is **not** a hidden state variable.

Two actions, selected before a future outcome, are:
- \`A0 = NOOP\`: do not perform an additional high-water reservation transaction.
- \`A1 = RESERVE\`: explicitly insert a row with ID \`m-1\` and remove that row in one transaction, preserving the public row set but advancing a low high-water mark.

The same prospective \`INSERT INTO events(note) VALUES ('next') RETURNING id;\` follows both actions. These actions are legitimate **only** in fresh disposable test databases with empty public rows and a proven schema. They are not instructions to manipulate user or production databases.

## 2. Four distinct notions of sufficiency

**Present-output sufficiency:** \`W(s)=W(t)\` implies the same current visible output.

**Predictive sufficiency:** \`W(s)=W(t)\` implies the same public trace for every prospectively declared intervention word.

**Outcome-vector sufficiency for a fixed action:** \`W(s)=W(t)\` implies the same consequential outcome vector under a given structural action and demand.

**Decision sufficiency:** a state representation \`D(s,e)\` is sufficient for the policy problem when all states sharing \`D\` (and demand \`e\`) admit the same action under the prospectively frozen feasibility-first, nonredundancy-second decision rule. This is not equivalent to predictive sufficiency.

The predictive quotient may be much finer than the quotient needed to make one engineering decision.

## 3. Prospective mechanical hypothesis (NOT yet an observation)
Let \`h\` be the exact high-water row in \`sqlite_sequence\` before the action, and \`m\` the frozen minimum acceptable next ID. Conditional on the tested SQLite semantics, the rival structural predictions are

\[
Y_{\rm id}(h,m,A_0)=h+1,\quad
Y_{\rm id}(h,m,A_1)=\max(h,m-1)+1 .
\]

Define the **one-bit decision coordinate**

\[
B(h,m)=\mathbf 1\{h+1<m\}.
\]

Then the prospective minimal-action policy is

\[
\pi_B(h,m)=
\begin{cases}
A_1 & B(h,m)=1,\\
A_0 & B(h,m)=0.
\end{cases}
\]

The policy's normative ordering is lexicographic over **violation count first**, then additional mutation transactions (no weighted scalar objective). The full outcome vector stays visible, with file size and time descriptive only.

## 4. Restricted minimality theorem

Fix a requirement \`m\` and a support containing at least one audited \`h_- < m-1\` and at least one audited \`h_+ >= m-1\`. Assume the two prospective mechanical hypotheses above are borne out and that A1 consumes exactly one extra write transaction while A0 consumes none.

- Any policy relying solely on common visible state \`W\` and fixed environment \`m\` must select the **same** action for both states.
- Choosing A0 violates the requirement at \`h_-\`.
- Choosing A1 is correct but incurs an avoidable extra transaction at \`h_+\`.
- In contrast \`B(h,m)\` supports \`A1\` precisely at \`h_-\` and \`A0\` at \`h_+\`.

Therefore a **zero-bit history feature** is insufficient for zero violations and zero redundant reservations over this frozen state support, while the **one-bit feature B** suffices. This is a decision-feature lower bound **only for the prospectively fixed action set, demand family, support and lexicographic priority**, not a universal complexity lower bound or a proof of exact-ID prediction from one bit.

The full high-water value \`h\` may remain necessary to predict the exact next identifier, but it is overcomplete for selecting the action.

## 5. Causal and comparison protocol

Prospectively freeze \`h in {0,3,7,11}\`, \`m in {5,9}\`, actions \`{A0,A1}\`, and three fresh file-backed SQLite databases for each matched cell: 4 × 2 × 2 × 3 = **48 trajectories**.

Every trajectory starts with the same declared schema, identical empty rows, matching source/build and PRAGMAs, and direct observation of \`h\` **before** structural intervention. Implement both actions independently from a fresh initial state; forbid action carryover from one arm to another. Require public rows to remain empty after A1, record H after the action, and apply the same final SQL oracle.

Prespecify \`Y=(requirement_violation,public_row_integrity,extra_write_transaction,extra_mutation_statements,exact_future_id,file_size_delta,elapsed_ns)\`. The last two are secondary descriptive quantities: no claim about general runtime dominance is admissible without a paired noise/stability audit.

The outcome-based action policy is computed *after* both action arms are measured, but the policy \`pi_B\` itself is defined prospectively and is not chosen to fit a revealed outcome. Judge each arm's direct future output, not a synthetic predictor alone.

## 6. Claim and novelty boundaries

This is an exact-source testbed exercising a real database implementation under a **synthetic engineering requirement**, not an independent fresh maintainer demand and not a claim that the SQLite AUTOINCREMENT specification was newly discovered. The scientific target is the new *state-aware design policy contrast* and the narrower **decision-state sufficiency** distinction.

The evidence ceiling is bounded policy correctness and nonredundant structural action on the frozen demand grid. Do not infer cross-mechanism transport or state ontology irreducibility until a different implementation with a real engineering decision and prospective correspondence has been tested. LAW-R2, macro law, SOLID derivation and manuscript authority remain NOT_AUTHORIZED.

## 7. Explicit disqualifiers

Hold if source provenance, pre-action state, visible-state matching, schema, treatment delivery, action isolation, post-action empty rows, common final oracle, future-ID type or unmodified demand are not established. A failed action-comparison gate is not evidence for a policy or ontology claim.
