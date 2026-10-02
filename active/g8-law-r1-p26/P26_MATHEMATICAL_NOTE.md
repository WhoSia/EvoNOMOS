# P26 Mathematical Note — Interventional Architecture Separation

Status: **PRE-FRESH / BINDING**

## 1. Two architecture classes

### U0 — Unified restricted architecture

For mechanism \(m\),

\[
S_m \xrightarrow{T_m} Z_m \xrightarrow{Q} q\in\{0,1\},
\]

with independent local gate \(g\in\{0,1\}\) and

\[
y=q\land g.
\]

The word **unified** does not mean that all concrete state spaces are identical. It means that the admitted typed intervention family induces the same quotient-level action and the same local decision grammar without mechanism ID.

### U1 — Shared-interface superclass

Each mechanism may have its own upstream transport law. Only the binary \(q\) interface and local AND rule are shared.

Thus:

\[
U0\subset U1.
\]

## 2. Theorem A — Positive-data nonidentifiability

If \(U1\) contains every realization of \(U0\), then no finite packet \(E\) satisfying \(U0\) can logically exclude \(U1\).

### Proof

Let \(M_0\in U0\) generate \(E\). Since \(U0\subset U1\), \(M_0\in U1\). Hence \(E\) is also realizable under \(U1\).

Therefore positive survival of U0 cannot establish uniqueness against unrestricted U1.

## 3. Theorem B — Complete mediation signature

For an upstream-only intervention \(\tau\) that leaves \(g\) fixed,

\[
y_\tau=Q(\tau(s))\land g.
\]

Therefore:

\[
\Delta y =
\begin{cases}
0,&g=0\\
\Delta q,&g=1.
\end{cases}
\]

## 4. Theorem C — Gate invariance

If \(\tau\) is genuinely upstream-only in the frozen typing, then

\[
g(\tau(s))=g(s).
\]

A measured gate change under \(\tau\) counts as U0 failure under the frozen experiment.

## 5. Theorem D — Quotient naturality

Let \(\tau_m:S_m\to S_m\) realize one typed intervention family.

U0 requires one mechanism-independent quotient action

\[
\bar\tau:\{0,1\}\to\{0,1\}
\]

such that

\[
Q\circ\tau_m=\bar\tau\circ Q
\]

for every admitted mechanism \(m\).

Frozen drop/restore actions:

\[
\bar D(1)=0,\qquad \bar R(0)=1.
\]

## 6. Theorem E — Interventional equivalence class

If two internal architectures induce identical kernels over every frozen tuple

\[
(\tau,q,g,y),
\]

P26 cannot distinguish them.

The identified object is therefore an equivalence class

\[
[A]_{\mathcal I},
\]

not a unique internal graph.

## 7. Separating strategy

U0 fails if any frozen extra invariant fails:

1. same typed intervention induces incompatible quotient actions across mechanisms;
2. upstream-only perturbation changes \(g\);
3. action changes while both \(Q\) and \(g\) stay fixed;
4. \(Q\) changes at \(g=1\) but action does not follow AND;
5. mechanism ID is required to state the transport rule.

## 8. Required packet

| intervention | q | g | y |
|---|---:|---:|---:|
| baseline-present | 1 | 0 | 0 |
| baseline-present | 1 | 1 | 1 |
| drop | 0 | 0 | 0 |
| drop | 0 | 1 | 0 |
| restore | 1 | 0 | 0 |
| restore | 1 | 1 | 1 |

## 9. Architecture claim ceiling

If the packet passes:

\[
\text{U0 SURVIVES under }\mathcal I.
\]

Not:

\[
\text{U0 is uniquely true}.
\]
