# LAW-R1-P30 Phase II-E — Cross-Runtime Behavioral Transport Court

## Status and authority
Prospective transport protocol for CPython 3.12.12 and Node 22.16.0, frozen before cross-runtime joined verdict. The CPython one-pair and 30×64 census predictions have already been proposed and are **not independently discovered again** here. The Node input family and one-pair outcome were also selected in advance. This audit tests implementation-level transport within the *same UTF-8 specification*, not an independent law or ontology.

## Shared abstract decoder
Use abstract state \(\pi(s)=(\ell,b)\) where \(\ell\) is the length of pending decoder input and \(b\) is the recorded prefix byte (a prospectively valid input-history coordinate). The **coarse** abstraction forgets \(b\): \(W_0(s)=\ell\). The **fine** abstraction retains \(b\): \(W_1(s)=(\ell,b)\).

CPython's route \(R_{\rm CPython}\) and Node's \(R_{\rm Node}\) are source-specific. They **must not be compared for syntactic equality**. Establish a correspondence only after applying explicit cross-runtime projection \(\pi\).

For each predeclared prefix \(p\in\{\texttt{C2},\dots,\texttt{DF}\}\) and suffix \(a\in\{\texttt{80},\dots,\texttt{BF}\}\), define paired observations:

\[
\mathcal T_{\mathrm{Py}}(p,a)=(O_{\mathrm{Py}}^{0}(p),O_{\mathrm{Py}}^{1}(p,a)),
\quad
\mathcal T_{\mathrm{Node}}(p,a)=(O_{\mathrm{Node}}^{0}(p),O_{\mathrm{Node}}^{1}(p,a)).
\]

The transport witness on this finite language is

\[
\forall(p,a):\quad \mathcal T_{\mathrm{Py}}(p,a)=\mathcal T_{\mathrm{Node}}(p,a),
\]

after normalizing both public outputs into exact UTF-8 bytes, and after confirming the input-history projection, initial empty output, and one-step finalization contract.

The result is *bounded trace correspondence*, not full bisimulation, not universal language equivalence, and not a proof that the source internals share the same minimal ontology.

## Execution discipline
1. Read the CPython raw census and independently reconstruct expected input-grid membership, decoder state, and outputs using its frozen Court.
2. Read the Node raw census and independently reconstruct expected input-grid membership and outputs using its frozen Court.
3. The joined transport Court reads both complete raw artifacts and compares all 1,920 rows, not summaries.
4. Preserve source and runtime versions, signed/precommitted GitHub commit references, and output artifact SHA-256.
5. Failure to establish exact version, immutable sources, or matching public output is a HOLD. Never silently drop mismatched rows.
6. A synthetic joined fixture may test Court robustness but may not count as implementation transport.
7. A single continuous hosted run on a pinned source compiler and Node v22.16.0 is preferred over joining unverified run IDs.

## Claim ceiling
Successful bounded transport would confirm preservation of the same coarse-state predictive collision and the admissible pending-byte rescue under two independent **runtime implementations** of a common UTF-8 behavior. It would not establish transport between different semantic contracts or a mechanism-independent necessity theorem. P30 remains OPEN unless separate termination criteria are satisfied. LAW-R2, macro law, SOLID and manuscript authority remain NOT_AUTHORIZED.
