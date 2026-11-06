# P44 finite graph certificate precision, scientific limitations and next measurements

Date 2026-11-05. The new edgecert checker accepts a supplied finite concrete source-edit graph, a finite abstract graph and a safe-state mapping. It checks permitted edit rights labels, same-stage index, protected-state flags, goal reflection and cost-nonincreasing edge simulation. The same finite reference tests execute an exact classical shortest-path algorithm and independent concrete path witness.

**Result relative to declared finite graph:** All authorized protected same-stage paths map to abstract admissible paths at no greater cost if all mapped edge checks pass. Therefore the abstract minimum is a lower bound and an independently verified concrete path gives an upper bound; equality proves the finite graph optimum.

**No source-level proof:** The checker does NOT extract a graph from Go source, prove that every actually permitted source edit has been represented, validate runtime contract truth of supplied Safe/Goal flags, authenticate actor/ownership rights, or prove all joint client observations across arbitrary schedules. One newly discovered permitted edit of cost 1 changes a supposedly exact K=4 to K=1. The verifier correctly rejects the prior mapping after the missing edge is inserted. Without independent graph-completeness proof, accepting the initial certificate says nothing about all real patches.

**No empirical superiority:** The example maps three concrete safe states to three abstract safe states; it does not compress the state graph. There is no observed certificate size/speed/transport gain over classical finite graph search. Record classical TIE rather than inventing novelty.

**Next measured comparison:** Concrete and abstract |V|/|E|, number of rights and observers, certificate bytes and checker time/CPU, source extraction coverage, false exclusions, L/U width, closed-grammar exact classical reference, revision-to-revision proof transport, independent actual maintainer tasks. Neither this finite test nor its CI establishes G1–G7 closure.
