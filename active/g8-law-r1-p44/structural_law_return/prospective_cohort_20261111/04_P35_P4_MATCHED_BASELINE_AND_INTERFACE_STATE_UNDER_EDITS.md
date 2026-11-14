# P44 — Interface State Required by Future Edits

2026-11-13 KST. Matched Chi pilot and finite theorem. LAW-R2 HOLD.

## Native matched baseline

The source treatment at 4a619db738e6bba36edbd47379e4e183419afb28 fixes the empty-header check at the consumer that needs it. Shared AllowContentType rejects an empty Content-Type after its zero-length body bypass. ContentCharset retains its ability to accept a missing charset when configured with an empty option. The original arms remain available for reproducing the divergence. The policy is an explicit experimental baseline chosen to match Independent, with real downstream reliance on the historical divergence still unknown.

[Go CI 43416391326](https://github.com/WhoSia/EvoNOMOS/actions/runs/43416391326/job/131855256254) ran on Linux amd64, Go 1.23.12 and Chi 67be7d9cafdaeb4e04e887ff78d09e030ee43b00. Independent and normalized Shared each passed 16 historical and 10 added cases, go test -count=1 ./..., and middleware race tests. The unpatched Shared negative control returned 204 and called downstream once where the common contract required 415 and zero calls. The new tests cover absent, explicitly empty and whitespace-only headers, a nonzero or unknown content length, zero-length bypass, valid and malformed media types, and absent/quoted charset behavior. These are finite response and downstream-invocation probes. The patch is setup for the comparison, and its cost belongs in a full lifecycle accounting. Maintainer effort and independent future tasks remain unobserved.

## Mathematical object

Let S be finite. At the interface, a partial observation o is defined on D ⊆ S. Each defined value is a protected answer. Undefined means no answer is specified for that state, and a decoder may return any value there. Let a family of total deterministic edits act on S. W is the set of finite words of edits, including the empty word. Write ws for the result of applying w to s. A finite representation q:S→Q is onto. Its width is |Q|, the number of distinct interface states. Runtime cost and human effort are different quantities.

Three tasks impose progressively stronger requirements:

1. Present: o(s) can be decoded from q(s) whenever s ∈ D.
2. Word supplied at query time: o(ws) can be decoded from (q(s),w) whenever ws ∈ D. The representation need not compute the state after an edit.
3. Autonomous update: present decoding holds and, for each edit a, there is a deterministic F_a with q(as)=F_a(q(s)). The updater receives the representation and the edit label. Iterating this identity gives the second requirement.

For the second task draw an edge between s and t if some word w makes both observations defined and unequal. A feasible q is a proper coloring. Necessity follows by giving the same decoder input (q(s),w) to both states. For sufficiency, for each color and word all the defined answers agree, so choose that common answer when present and any answer otherwise. The minimum width is the graph's chromatic number.

For the third task the fibers of q must additionally be an edit-invariant partition. Conversely, any conflict-free invariant partition induces deterministic updates and a decoder. With partial observations there can be multiple incomparable valid coarsenings. For instance, with identity edits and only 0 and 1 observed as distinct, an unobserved state can be merged with either; a partition coarser than both would merge 0 and 1.

## Regular group actions

If the edits generate a finite group G acting on itself by left multiplication, the updateable partitions are precisely the partitions into left cosets xH of a subgroup H≤G. For an invariant equivalence let H be the class of the identity. If h,k∈H then translating h~k by h^-1 gives e~h^-1k, so H is a subgroup. Translating x~y by x^-1 gives x^-1y∈H. Conversely left multiplication preserves xH equivalence. For a conflicting pair (x,y), q must separate them, so the minimum updateable width is

    min { [G:H] : H≤G and x^-1 y∉H for every conflicting pair (x,y) }.

Finite reversible edits make a kernel test possible with a group action. This formula does not characterize arbitrary partial edits, observable authorization, or updaters that can inspect the original state.

## An arbitrarily large separation

Let S = Z/nZ for n≥3 and let the sole edit be a(x)=x+1 modulo n. Observe only 0 and 1 and give them distinct answers. The present width is 2. A pair conflicts after some number of edits exactly when it is adjacent in the cycle C_n. The word-supplied width is 2 for even n and 3 for odd n. For autonomous update, a is a finite permutation; any admissible partition is into residues modulo a divisor d of n, by the subgroup argument. The observations require d>1, so the minimum width is the smallest prime divisor of n. For odd primes p this is the strict separation (2,3,p), and p is unbounded. The two observations and the edit generator remain fixed in number as n grows.

Independent computational check enumerated every partition for n=3 through 10 (142414 partitions). For each partition it tested present decoding, conflicts generated by all n rotations, and whether each color has a unique successor. The triples were (2,3,3), (2,2,2), (2,3,5), (2,2,2), (2,3,7), (2,2,2), (2,3,3), (2,2,2). The proof covers all n. The check is not Go source evidence.

## What can replace parts of SOLID?

P40's typed reduct, F22's sequential residual and F32's costed lifting already give a research program about preserving source-edit opportunities. The new axis here is representation width under two different interfaces for those opportunities. In this restricted model, LSP-like preservation means a decoder can recover the protected observations; ISP-like compression means minimizing the representation for the selected observers; an OCP-like requirement under the named edits means a quotient admits the same edit updates. The cycle proves that satisfying the first two under query-time decoding can hide an unbounded obstruction to the third. This is a formal interaction among explicit proxies. SRP and DIP still require independently defined ownership, composition and dependency relations.

Classical ingredients include [Parnas's decomposition criteria](https://doi.org/10.1145/361598.361623), [behavioral subtyping](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf), [one-shot zero-error confusability and coloring](https://www.cs.tau.ac.il/~nogaa/PDFS/witsen.pdf), [incompletely specified machine minimization via closed compatible covers](https://www.cecs.uci.edu/~papers/compendium94-03/papers/1994/dac94/pdffiles/42_2.pdf), and [invariant block systems of group actions](https://webspace.maths.qmul.ac.uk/r.a.wilson/FSG/lect1.pdf). No priority is asserted for graph coloring, group congruence, or the cyclic separation. A practical synthesis that permits several abstract representatives for one concrete state must be compared to classical closed covers as well as partition quotients.

## Research decision

Test when an interface can hide concrete implementation state yet still support a future contract-preserving edit in isolation. Before a task outcome is known, specify which concrete state the actor or tool may inspect, which edit acts on it, what outputs are protected, and where an adapter is permitted. An empirical comparison should pair aligned source arms, use independent common versus consumer-specific changes and include a baseline given the same source access and edit rights. The theory is falsifiable as a model of the pilot. If the actor can reread the original header or use a local adapter, the restricted autonomous updater may be the wrong model. The parser pilot establishes the need for baseline alignment and scoped observation. It does not realize the cyclic example.

A paper contribution would require a source-checkable mapping from real edit and contract constraints to a prediction or lower bound that changes a design decision, tested under matched information against ordinary slicing, repair search and classical minimization. The finite theorem supplies an exact diagnostic and a boundary for the claim. The measured sign of the engineering effect remains unidentified.
