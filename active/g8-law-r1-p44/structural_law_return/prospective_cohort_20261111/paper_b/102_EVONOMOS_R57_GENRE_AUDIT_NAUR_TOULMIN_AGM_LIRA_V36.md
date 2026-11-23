# EvoNOMOS R57 — Genre Audit, Naur–Toulmin–AGM Bridge, and a Genuine LIRA Challenge to v36

**2026-11-23 · SOURCE-BOUND PRIMARY-READ REVIEW, not independent peer review.** Reopened actual [v36](PAPER_B_BILINGUAL_POSITION_36_20261123.md), [LIRA 0.1 Notion method](https://app.notion.com/p/420ef561cf928159986dc36b3c6464f8), exact original Drive PDFs of Naur(1985), Toulmin(1958, 2003 updated edition), and Alchourrón–Gärdenfors–Makinson(1985). Compared with dated [R54 ten-PDF accession](99_EVONOMOS_R54_20261123_TEN_PDF_ACQUISITION_SOURCE_AND_DUPLICATE_AUDIT.md). **Scores below are subjective phrasing-retention recommendations, not truth/novelty probabilities.**

## A. Did a non-paper get misfiled as a paper?

The ten migrated items were rechecked against source-borne title, journal masthead, abstract, methods and publication notes in R54. They are all **research-related scholarly manuscripts**, but peer-review/publication status is heterogeneous:
- Journal-published scholarly works: Baldwin 2023 in *Industrial and Corporate Change*; Fu 2012 *International Journal of Project Management*; Mishra 2026 *PLOS ONE*; Räihä 2010 *Computer Science Review*; Zhan 2025 *IEEE Transactions on Software Engineering*. Cai 2025 presents an original large-scale industrial architectural study with a conference/article PDF; do not claim a journal venue without direct venue verification.
- Terra et al. 2016 is an original empirical **conference-style research paper** with abstract, methods, evaluation and references, not a blog. Exact proceedings metadata remains to be formally normalized.
- Song et al. 2016 is the *Journal of Systems and Software* **accepted manuscript** explicitly labeled as such, not guaranteed identical to final typeset issue.
- LaMantia et al. 2007 is **Harvard Business School Working Paper 07-081** and explicitly says distributed for comment and discussion (not proof of journal peer review).
- Germanos et al. 2023 **SSRN preprint** explicitly prints “This preprint research paper has not been peer reviewed.” It is not the same epistemic status as a final published version; do not cite it as peer-reviewed 2024 without the separate final article.
- Non-scholarly Vista CNET article (2006), ScienceDirect/Cloudflare `init.html`, relevant-but-not-software RNA-Seq Yadetie(2018), duplicate unreadable Parnas scan were ALL **left in 00**, not moved into 10 as design research papers. CNET is useful **historical journalism**, not a scholarly study. The Yadetie file *is* a genuine scientific paper, merely irrelevant to this project's software paper corpus.
- A review/survey is scholarly literature but it is not an original controlled experiment: Räihä 2010 must be labeled SURVEY, not presented as a new maintenance benchmark.

**Result:** NO observed non-paper erroneously entered 10 among the ten migrated PDFs. **Correction required** in metadata interpretation: “academic research PDF” does not imply “peer-reviewed journal article.” No destructive file moves needed; paper types can be represented in reading notes.

## B. Three actually owned intellectual predecessors newly reopened

### Peter Naur (1985), *Programming as Theory Building*
[Authenticated owned PDF](https://drive.google.com/file/d/1h6omxTHbuPYrKe_hjf0U_BtYCs1s8OgC/view) in *Microprocessing and Microprogramming* 15:253–261 (invited address 1984). Read the original extracted paper text. Naur argues that programming includes building the **developer's theory** of how the relevant world problem is handled by program execution; code and documentation may fail to transmit the tacit understanding needed to modify the program. He explicitly contrasts this with treating programming as mere production of code/text. **Conceptual connection (ours, not Naur's stated SOLID result):** a remembered mnemonic or static compliance score cannot by itself replace the situational theory needed to decide whether a change is apt. Naur does NOT present a mathematical atlas of SOLID, nor proof that AI believes principles.

### Stephen Toulmin (original 1958, updated 2003), *The Uses of Argument*
[Authenticated owned revised book](https://drive.google.com/file/d/1gP-zJtB9YRYrbfwWwKwXl2GMWsobMizO/view). The original introductory framing explicitly distinguishes **field-invariant structural elements of argument** from **field-dependent criteria of assessing warrants/validity**. Directly relevant to the prospect that named coding principles are arguments requiring **scope, grounds and rebuttal**, not deductive axioms for all tasks. This is a historical philosophical precursor of contextual justification, not newly invented by EvoNOMOS. Book was inspected for relevant sections and extracts rather than every 680k characters independently evaluated.

### Alchourrón, Gärdenfors & Makinson (1985), partial-meet belief revision
[Authenticated original JSL 50(2):510–530 PDF](https://drive.google.com/file/d/1nCMd4zfQcbr28HJkmFqRvHFsGWh8QabQ/view), abstract and key passages read. Established operations for **contraction and revision of logically closed beliefs**. Applying them mechanically to heuristic design norms requires semantic care: a project policy is not a propositional belief, and a principle is not necessarily a closed theory. The theoretical connection is to *rational revisability*, not existing mathematical proof of a universal design principle system.

### Cross-check: rules and design fit
[Parnas 1972](https://drive.google.com/file/d/1EcQRy3iehx4lUN7uGsZ1BFXU33HggcEQ/view) and [Parnas 1979](https://drive.google.com/file/d/1XGzB9hq_6wk6aXeVojMo1IeKoKCg704j/view) offer change/uses-relations without calling modern SOLID a universal axiomatic system. [Suh axiomatic design abstract](https://academic.oup.com/book/52792/chapter-abstract/421881976) is a contrast for a **deliberately postulated engineering axiom**, whereas [LaMantia et al. 2007](https://drive.google.com/file/d/11YpfmJ4EJ1blHIVQRy1yWFJqkS2BJgn9/view) uses design rule theory for stable architectural dependencies. These terminological types must not collapse.

## C. LIRA v36 cold reread (selective original expressions)

| Unit | Exact passage from the loaded v36 | Editorial retain score | Grounding | Decision |
| --- | --- | ---: | --- | --- |
| K01 | “하지만 한때 좋은 판단을 돕기 위해 만들어진 조언이 언제부터 코드의 합격과 불합격을 결정하는 법칙이 되었을까?” | 0.88 | QUESTION/QUALIFIED; implied history not established | Favor conditional ‘어떤 순간’ instead of claiming there was a single transition |
| K02 | “공리로 선언한 것과 오랫동안 쓰여서 공리처럼 취급되는 것의 차이” | 0.99 | CORE/EVIDENCED contrast Suh vs heuristics; prevalence unverified | Preserve |
| K03 | “SOLID의 다섯 원칙, 중복을 줄이라는 DRY, 불필요한 구현을 미루라는 YAGNI…” | 0.91 | IDEA/QUALIFIED, principles heterogeneous | Keep examples but avoid pretending all are the same logical kind |
| K04 | “각 원칙의 **관할 범위**가 다를 수 있다는 생각” | 0.98 | CORE/CONJECTURE | Preserve |
| K05 | “수학에서는 하나의 대상을 여러 국소 좌표계로 다루기도 한다.” | 0.66 | METAPHOR/QUALIFIED; invites unsupported manifold claim | Retain as marked metaphor only or replace with sober ‘부분적 지도’ |
| K06 | “게임이론은 왜 한 설계 관습이 협업의 균형으로 오래 유지되는지…” | 0.77 | BRIDGE/UNTESTED causal uptake | Avoid using game theory as proof of actual SOLID adoption; relocate catalogue to research appendix |
| K07 | “평가 함수도 누군가 선택한 기준” | 0.96 | SUPPORT/EVIDENCED as a choice; Räihä | Protect as conceptual extension |
| K08 | “누가 설계 원칙에 공리 같은 권위를 주었으며” | 0.67 | CORE/QUALIFIED; ‘누가’ presumes assignable historical agent | Refine to ‘어떤 과정에서, 어떤 근거로’ |
| K09 | “하나의 상위 구조가 없다는 결론이 나와도 괜찮다.” | 0.97 | RHYTHM/HYPOTHESIS | Preserve: scientifically open |
| E01 | “How often that happens remains a historical and empirical question.” | 0.96 | HONESTY/QUALIFIED | Preserve |
| E02 | “We propose this as a starting analogy for design principles” | 0.77 | ANALOGY/QUALIFIED | Fine but do not keep extending charts into a mathematical assertion |
| E03 | “Optimizing that score does not, by itself, establish a law of design.” | 0.99 | CORE/EVIDENCED as conceptual logical distinction | Protect |
| E04 | “Who gave design principles their near-axiomatic authority” | 0.67 | QUESTION/QUALIFIED; presumes deliberate grant | Replace with question of source and justification |
| E05 | “Even finding several irreducible structures would teach us more…” | 0.94 | CONCLUSION/CONJECTURE | Keep open plurality |

## D. Strongest adversarial critique of v36

**Conceptual critic**: At the moment the draft claims a local-map analogy, it risks confusing a metaphor with an alleged common structure of all rules. The core conceptual work should show **which questions differ** (formal correctness, team authorization, contextual heuristic) before introducing speculative category theory.

**History reviewer**: The word ‘axiom’ spans formal postulates, codified engineering design principles, and social constraints. A historical argument must not invent a conspiracy or straightforward transition. Unlike an overgeneralization of SOLID, some team code guidelines *are deliberately binding*, and some contract rules are correctness-critical.

**Philosophy reviewer**: Naur and Toulmin are VERY close antecedents to ‘situational judgment exceeds codified rules’—bring them to the front and give credit. Their existence makes the synthesis more substantial, not valueless.

**Writing editor**: Repeated ‘not X but Y’ rebuttals and five named theories in one breath flatten the voice. A concrete “OCP 위반” code review decision, then Naur/Toulmin as one well-selected historical bridge, then plural atlas as a question, is much more persuasive and shorter.

**Evidence boundary**: Neither the newly acquired sources nor the previous 35 synthetic models show the **frequency** of quasi-axiomatic automated decisions. “SOLID behaves as an axiom” remains a researchable possibility, NOT established prevalence.

## Editorial gate

A substantive v37 can be justified by this new Naur–Toulmin source grounding and by replacing accidental assumptions of historical change with a conditional decision mechanism. Preserve the beautiful Korean title, the named **EvoNOMOS Principle Atlas Hypothesis** as a project label, and open plurality of upper structures. Keep the main essay short; broader game/lattice/AGM formalization should remain in R52/R55 research notes. **Do not promote stylistic retain scores to novelty probabilities.**
