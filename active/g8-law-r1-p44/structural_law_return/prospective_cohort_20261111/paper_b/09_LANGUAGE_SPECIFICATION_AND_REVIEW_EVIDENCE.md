# Paper B — Specification, Rationale, and Evidence Available to a Reviewer

Three deposited PDFs were identified from their first pages and moved by metadata only. The QOC scan had no extractable text in Drive; title and bibliographic details were verified by OCR of the first two pages, and the public article was used for close reading. The original and post-move downloads were compared byte-for-byte, with equal SHA-256, and the IDs, sizes, names, and destination parents were read back.

| File | Destination | Bytes | SHA-256 |
|---|---|---:|---|
| [Dahl, Myhrhaug & Nygaard (1970) — SIMULA 67 Common Base Language — NCC S-22 Revised Edition.pdf](https://drive.google.com/file/d/1Q5IvxnxgT3l8u77JM0CtGUukU3fC4ab_/view) | 11_SOURCES | 3366070 | `a1ad7d8fc4fc2d453b8a7964d350f9e84450624bb3f62a617daf9bf4a6959d39` |
| [MacLean, Young, Bellotti & Moran (1991) — Questions, Options, and Criteria - Elements of Design Space Analysis.pdf](https://drive.google.com/file/d/1qzj5Cmz88ZP9jseFVJcUHCtey0ewUCZP/view) | 10_PAPERS | 2515375 | `f3f72e6863e185bdd2208c996b945d6cb567b0ddf3a89dbbbe490ad945c61ffe` |
| [Perry & Wolf (1992) — Foundations for the Study of Software Architecture.pdf](https://drive.google.com/file/d/1MUO6uBCPwQ44jSBNMHidAKF8DyBKTwaP/view) | 10_PAPERS | 1267855 | `46ca00f2f4d8c68a2bf5ba465db28382e84a0d109a430ae9550734bedfbdf6ce` |

## Specification and implementation

SIMULA 67 Common Base Language is NCC S-22, October 1970, revised from S-2. The 1968 preface is reproduced inside it. In §15.1, printed p. 131, the statement about referencing externally compiled procedures and classes is conditional on the implementation permitting user-defined declarations to be separately compiled. The external declaration is given semantics in terms of the identified declaration. This qualifies our earlier comparison to the December 1968 conference demonstration. A facility illustrated in a paper, a provision in a language reference, and support in a particular compiler are different evidence. This reading neither substitutes the 1970 text for S-2 nor attributes it verbatim to the October 1968 Garmisch submission.

## Design rationale and recorded practice

Perry and Wolf (1992, §3, Rationale) locate the reasons for architectural choices in system constraints, often derived from requirements. MacLean et al. (1991, abstract and §2) use Questions, Options, and Criteria to compare alternatives and explicitly distinguish the constructed rationale from a record of the design process. Parnas's IFIP 1971 paper, printed in 1972, argues against broadcasting all internal system information. This supplies a counterpoint to treating missing context as a demand to disclose everything. The task is to find the premises that materially determine a particular verdict.

## A test for the automated-review claim

For each OCP item, record the criterion and candidate demand in the scenario/label documentation, the corresponding available evidence in the actual serialized request, and the reported scoring action. If only pipeline source is available, mark a reconstructed request separately. Record the protected boundary or legacy contract, even when only inferable, and state the evidence for the inference. Apply a paired test with the same source and protected boundary and two different demands. A verdict should change only where the criterion entails a change; when both demands leave the answer the same, this provides a control. QOC supplies the comparison of design alternatives. The audit tests what reached the evaluator. No new model runs or ASE row-level claims are made.

AreWeSOLID.zip is user-confirmed held and remains outside the missing list. Connected location and byte/row verification remain pending. LAW-R2 HOLD.

Public readings: [SIMULA 1970](https://softwarepreservation.computerhistory.org/ALGOL/manual/Simula-CommonBaseLanguage.pdf) · [QOC](https://doi.org/10.1080/07370024.1991.9667168) · [Perry–Wolf](https://www.cs.unibo.it/cianca/wwwpages/readings/perrywolf.pdf) · [Parnas IFIP](https://cseweb.ucsd.edu/~wgg/CSE218/Parnas-IFIP71-information-distribution.PDF).
