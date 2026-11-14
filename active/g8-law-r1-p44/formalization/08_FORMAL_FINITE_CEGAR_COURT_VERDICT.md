# P44 formalization cost-bounds court — verified finite reference result

Date 2026-11-04. This is **a classical finite mathematical control**, not original-source repair minimum certification.

## Immutable GitHub execution custody
Original [GitHub Actions run #41781081380](https://github.com/WhoSia/EvoNOMOS/actions/runs/41781081380) executed at commit `071cc77c519239ef8a970e360974214cadec0df2`, job ID `126412528950`, Go `go1.23.2 linux/amd64`. Job steps, test/vet/race and **raw logs** independently inspected: SUCCESS. Four finite test cases PASS, no bot commit action:
- TestClassicalCEGARRepairCostSandwich
- TestUnsoundAbstractionDetected
- TestOldClientAndRightViolationsRejectUpperBound
- TestEmptyAbstractSetNotClaimedConcreteFeasible.

## Actual finite log
CLASSICAL_BOUND level=0 lower=1 upper=4;
CLASSICAL_BOUND level=1 lower=2 upper=4;
CLASSICAL_BOUND level=2 lower=4 upper=4.
Sound cost projected map and concrete witness produce L<=K<=U only under frozen source-edit and observer assumptions; each soundly pruned abstract fake path raises lower bound without erasing the concrete image. At L=U=4, the declared **toy** finite optimum is certified. Removing the only concrete image or assigning an abstract image higher cost correctly fails a test. An unvalidated right or stagewise unsafe witness is not accepted.

## Explicit mathematical limitations
The Go test knows all concrete safe paths because **the finite fixture supplies them**. It does not implement a sound source-complete abstraction of arbitrary Go source, does not prove a global minimum source patch cost, and does not show novelty over abstract interpretation/CEGAR.

The real P44 research target is to extract and validate the cost-nonincreasing path abstraction from actual maintained source under complete declared edit rights and joint client trace observers, then compare certificate precision/size/CPU with equal-information classical CEGAR, separation logic/bi-abduction and exact finite search. No G1–G7 source-wide closure and no LAW-R2.

## Related literature entered and normalized
Original Reynolds (2002), Yang/O'Hearn (2002), Calcagno et al. (2009), Flanagan/Godefroid (2005), Clarke et al. (2000 CAV) and Clarke et al. (2003 JACM) were verified, renamed in place and transferred into Drive 10_PAPERS; [six-source reading and custody ledger](07_SIX_ORIGINAL_PAPERS_INGESTION_READING_20261104.md).
