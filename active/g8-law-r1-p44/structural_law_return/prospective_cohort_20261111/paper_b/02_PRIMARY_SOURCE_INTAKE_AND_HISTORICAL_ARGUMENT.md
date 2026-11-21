# Paper B — Primary Source Intake and the History of Design Judgment

2026-11-14 KST. Ten newly deposited PDFs identified from their own title pages or text, renamed, and moved. All ten file IDs, byte sizes, names and destination parents were read back from Drive. Changes were metadata only. Independent file hashes were not available from that readback.

| File | Copy | Shelf | Bytes |
|---|---|---|---:|
| [Velasco et al. (2026) — A Causal Perspective on Measuring, Explaining and Mitigating Smells in LLM-Generated Code — arXiv 2511.15817v7](https://drive.google.com/file/d/1noZZ3zqOXyK1wv_JtsOERV-SYPNpNKOk/view) | arXiv v7 | 10_PAPERS | 1515474 |
| [Shaw (1990) — Prospects for an Engineering Discipline of Software — CMU-SEI-90-TR-020](https://drive.google.com/file/d/1CLi8xbQo6DYgERqLC0knsWpuuvXNmGYD/view) | SEI technical report | 11_SOURCES | 1581219 |
| [Ghosh Paul, Zhu & Bayley (2025) — Investigating the Smells of LLM-Generated Code — arXiv 2510.03029v2](https://drive.google.com/file/d/1kVNg1rHIEu6GnZB4Ii2pDZ6I9DNdZAUs/view) | arXiv v2 | 10_PAPERS | 783479 |
| [Tantithamthavorn et al. (2026) — RovoDev Code Reviewer - A Large-Scale Online Evaluation of LLM-Based Code Review Automation at Atlassian — arXiv 2601.01129v2](https://drive.google.com/file/d/1KEGjUrcl9HLJxWDNHyT4h3VwMaHK8HMl/view) | arXiv v2 | 10_PAPERS | 2226302 |
| [McMillan (2026) — Instruction Adherence in Coding Agent Configuration Files - A Factorial Study of Four File-Structure Variables — arXiv 2605.10039v1](https://drive.google.com/file/d/1M2CIk_yJV_swII6C8S3o8jXi_iwX1TT-/view) | arXiv v1 | 10_PAPERS | 1392622 |
| [Spolsky (2009) — From Podcast 38 — Joel on Software Transcript Excerpt](https://drive.google.com/file/d/16P3vVEJYSz_fRF6WmAqVYzTIMVOJGG5P/view) | Web transcript excerpt | 20_NON_PAPER_SOURCES | 454146 |
| [Naur & Randell eds. (1969) — Software Engineering - NATO Garmisch Conference 1968 — OCR Reprint](https://drive.google.com/file/d/1XE3E8MGUtSVtKvgdBe5V4qxaFZ-4YDLr/view) | OCR and reformatted reprint | 20_NON_PAPER_SOURCES | 2315016 |
| [Yanakiev, Lazar & Capiluppi (2025) — Applying SOLID Principles for the Refactoring of Legacy Code - An Experience Report](https://drive.google.com/file/d/1AgrvMjuayztaJ9yp6JtYbzeRyOOcGCG3/view) | JSS version of record | 10_PAPERS | 2349131 |
| [Pehlivan et al. (2025) — Are We SOLID Yet - An Empirical Study on Prompting LLMs to Detect Design Principle Violations — arXiv 2509.03093v1](https://drive.google.com/file/d/1kSIAwqyLhcNWbwEuuL4uFqZ917Evyz1f/view) | arXiv v1 | 10_PAPERS | 1130865 |
| [Martin (1996) — The Open-Closed Principle — C++ Report](https://drive.google.com/file/d/1DlBeE1kdwARRKyK2gEsKwp3wNa0ZbBQG/view) | Trade-press article | 20_NON_PAPER_SOURCES | 70775 |

## The history worth correcting

- Garmisch, October 1968, reported January 1969. The editors say the conference name was chosen to provoke an engineering aspiration. The design section explicitly reports disputes about the design/production distinction, which the editors kept as an organizing device. The report also explains how notes and recordings became edited excerpts. Our file is an OCR and reformatted reprint with original page numbers indicated, not a facsimile. Compare introduction, design/production discussion, and the later discussion of the software crisis. [Report](https://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF)
- Shaw, September 1990, CMU/SEI-90-TR-020, §2 and Figure 1. Shaw describes an engineer asking where to find demonstrably good designs and methods for choosing between them. Craft, commercialization, supporting science and professional practice are parts of a historical model she proposes. Treat the sequence as her model, not a periodization already established for all software. [SEI](https://www.sei.cmu.edu/library/prospects-for-an-engineering-discipline-of-software/)
- Martin, 1996, pp. 1 and 6. He asks where OO heuristics get their validity and whether they always hold. He explicitly calls his wording a paraphrase of Meyer 1988, p. 23. Strategic closure is a choice of changes to anticipate. The 1997 Meyer text provides a second-edition comparison, not evidence for verbatim first-edition wording. The narrow historical question is what was being fixed, who could depend on it, and which changes were contemplated. [Martin](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)
- Spolsky, 2009, first-person transcript excerpt beginning 42:28. Compare his objection to applying interface conventions to small internal classes with his acceptance of strong contracts for plugin APIs. The historical artifact is a blog excerpt, not the full recording. [Post](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)
- Mahoney's historical work already asks what counts as the object of a history of software engineering. Our proposed contribution is a narrower account of how the premises of individual design judgments travel across publication, professional debate, automated review and scoring. [Mahoney 2004](https://doi.org/10.1109/MAHC.2004.1278847)

## What the later instruments measure

Yanakiev et al. report selected industrial refactoring work, centered on dependency inversion and applied across over 5,000 files, with limited available metrics. Pehlivan et al. turn violation detection into a synthetic labeled benchmark and manually review 1,431 of 3,840 outputs where the parsing/classification procedure needed human handling. McMillan's target is an AST-detectable annotation, not a judgment about architectural merit. RovoDev reports a 38.70% code-resolution rate using its observational definition, alongside reports of incorrect or non-actionable comments in unknown context. Ghosh Paul et al. count smells in generated Java against reference solutions. Velasco et al. use a model-probability metric for smell propensity. These observations have distinct units and outcomes. Compare which contract, change, or dependent client each procedure can actually see.

## Pending evidence

Meyer 1988 p. 23 and the audio of Hanselminutes #145/#150 remain outstanding. DOI and direct Zenodo API access did not resolve the replication package in this pass. The paper is held, but no raw OCP rows or annotation criteria were audited from the package. No new model run or maintenance outcome is claimed. LAW-R2 HOLD.
