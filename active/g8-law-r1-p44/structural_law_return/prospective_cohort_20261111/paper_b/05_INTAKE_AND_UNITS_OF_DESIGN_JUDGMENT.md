# Paper B — Intake and Three Units of Design Judgment

Six deposits were moved by metadata only. IDs, sizes, names and destination parents were checked after the move.

| Deposit | Shelf | Bytes |
|---|---|---:|
| [Huvila & Sköld (2026) — A Fieldwork Manual as a Regulatory Device - Instructing, Prescribing and Describing Documentation Work — Online First 2023.pdf](https://drive.google.com/file/d/1hEdJy5o0Lq_swtcpcQ6V1O9M9-_1griz/view) | 10_PAPERS | 222920 |
| [Wadler (1998) — The Expression Problem — Java Genericity Mailing List.txt](https://drive.google.com/file/d/10qZ9I27xzS8Wcs2euZQkN2B8asFL6n-b/view) | 20_NON_PAPER_SOURCES | 13185 |
| [Fowler (2015) — Yagni — Web Capture.pdf](https://drive.google.com/file/d/19EdKtYX9-so-JuyQeskYKs48nK5j_yEi/view) | 20_NON_PAPER_SOURCES | 412376 |
| [Atwood (2009) — The Ferengi Programmer — Web Capture.pdf](https://drive.google.com/file/d/16gSDghZiUphyi2I4sum4vWfalVeDgEdz/view) | 20_NON_PAPER_SOURCES | 3549761 |
| [Parnas & Clements (1986) — A Rational Design Process - How and Why to Fake It.pdf](https://drive.google.com/file/d/11PVdBdKG1gqjU4o1cEXJ0XWpjuGuHFbw/view) | 10_PAPERS | 151959 |
| [Kroll et al. (2017) — Accountable Algorithms.pdf](https://drive.google.com/file/d/1REloIJNv6T6gZknCdN3jo341b2UX3zEB/view) | 10_PAPERS | 560797 |

The file originally named sultan2021.pdf identifies itself as Massimo Cacciari, Nomes de Lugar: Confim (2005), pp. 13–22, JSTOR 26459823. It has the same byte length (691,260) and identical extracted text as [the shelved copy](https://drive.google.com/file/d/1G7oFZpAeXLZgGUCSD2yDt1DDV2cHMCBb/view). [The candidate](https://drive.google.com/file/d/1sH_bDqmDMWntg8gY4VLlYAenKo7qH6j0/view) was labeled in 00. No independent checksum comparison or deletion was performed. The traffic items remain in the shared intake.

## 1. Language capability and local architecture

Wadler's November 12, 1998 message requires both new cases and new operations, separate compilation of existing code, and static type safety. The Python review fixture borrows the two extension directions and measures edits to protected files. Separate compilation and static type safety are additional criteria. Dahl and Nygaard's historical SIMULA account reports simulation workloads and a later move toward general-purpose language features. This is a source comparison for what problem a language mechanism was designed to solve, not a claim that its authors anticipated SOLID. [Wadler](https://homepages.inf.ed.ac.uk/wadler/topics/gj.html) · [SIMULA history](https://www.cs.tufts.edu/comp/150FP/archive/kristen-nygaard/hopl-simula.pdf)

## 2. Structural feasibility and whether to prepare

Martin's strategic closure asks which changes should be anticipated. Fowler's Yagni adds the cost of carrying capability before demand materializes, while treating refactoring that preserves ease of change as enabling incremental design. A one-horizon illustrative model makes the difference explicit. Let k be up-front preparation plus carry, p the chance of a specified demand in the horizon, f the conditional cost of doing it after deferral, and e the conditional implementation cost after preparation. With risk-neutral expected cost, no discounting, and equal eventual outcomes, prepare if k + p e < p f. If f > e the threshold is p > k/(f-e). At k=3, f=10, e=2, checked examples p=.1 and p=.6 reverse the decision, while the local structure comparison stays fixed. At p=.1 costs are 3.2 vs 1; at p=.6 they are 4.2 vs 6. Inputs are constructed, not estimates. No independent software demand or lifecycle cost has been observed. [Martin](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf) · [Fowler](https://martinfowler.com/bliki/Yagni.html)

## 3. Consistent evaluation and justified evaluation

Huvila and Sköld study what manuals prescribe and how they structure the available workspace, distinguishing the manual from evidence of work as performed. Kroll et al. give a cross-domain comparison through procedural regularity, in which an announced rule is applied consistently. For EvoNOMOS this raises two independently inspectable questions: which rule and input did the reviewer actually use, and were those sufficient to decide this design question? Atwood's 2009 post offers an especially useful reception artifact because it reproduces short principle formulations and argues against blindly extending them into a detailed ruleset in the same document. Concision alone does not show dogmatic reception. Parnas and Clements provide the counterexample of useful idealized documentation when later maintainers can recover the relevant requirements. [Huvila–Sköld](https://doi.org/10.1177/01655515231203506) · [Kroll et al.](https://pennlawreview.com/2017/02/23/accountable-algorithms/) · [Atwood](https://blog.codinghorror.com/the-ferengi-programmer/) · [Parnas–Clements](https://www.laputan.org/pub/papers/Fake.pdf)
