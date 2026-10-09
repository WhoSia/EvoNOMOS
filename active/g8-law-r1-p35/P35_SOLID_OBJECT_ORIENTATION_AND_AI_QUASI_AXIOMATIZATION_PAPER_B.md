# EvoNOMOS — From Object Orientation to the Operational Quasi-Axiomatization of SOLID

**Status (2026-10-09): historical-critical research programme / PAPER B NOT SUBMITTED.** This is a source-grounded interpretive thesis with open empirical tests, NOT a historical fact that LLM model training has caused SOLID dogmatism.

## Initial insight was already in the early primary conversation

[Archive 1.md, 2026-07-29](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view), EvoNOMOS 0.5: owner distinguishes principles from rules, and questions whether tools like Codex and Claude Code and repositories' conventions have turned SOLID from revisable advice into commands that *operate as though they were axioms*. The same chat developed **operational quasi-axiomatization**, an Open Principle Ledger and a tentative Axiomatization Pressure Index. Those were **earlier project proposals, not facts about model weights or actual corporate training corpora**. [Archive 5.md, DIP-18/19](https://drive.google.com/file/d/1L_YfIOq0RxVmLP8a0Nhs7h8O3RPutQUl/view) explicitly reopens the founding question and treats the five SOLID components as logically heterogeneous; [Archive 6.md](https://drive.google.com/file/d/1pTybpiZID2obS-0CzNnoWQfmZ73qlgu-/view) asks why design principles acquire the authority of aphorisms instead of scoped theorems or empirically limited policies. [Archive 14.md](https://drive.google.com/file/d/1TuweqOEc1KY14ddEJVoPbBJAiT-i3thP/view) further corrects the author's tendency to demand a wholly new theorem: a historically candid reconstruction of SOLID using established mathematics can itself be scholarly work. Missing archive **7.md excluded**; no imaginary contents.

## History with distinct authority and correct chronology

| Historical locus | What can be documented | What must NOT be inferred |
| --- | --- | --- |
| Simula I / Simula 67 (1960s) | Dahl and Nygaard used object/class concepts emerging from simulation; the 1967 general-purpose language added elements that became central to OO | That SOLID already existed, or that OO began as a closed package of SOLID obligations |
| Smalltalk (1970s–1980s), Alan Kay's retrospective (1993) | Different motivations centered on interactive systems, encapsulation and message-based objects; OO has divergent schools | That Smalltalk equals one modern dependency-inversion recipe |
| Parnas, 1972 | Information-hiding/modularization as an explicit design criterion linked to change and comprehensibility | That Martin invented modularity or that all criteria imply one unique layout |
| Liskov and Wing, 1994 | Behavioral subtyping is a precise semantic/contract concern | That LSP is a comparable scalar guideline interchangeable with SRP |
| Martin, *Design Principles and Design Patterns* (copyright 2000) | Architectures' rigidity, fragility, immobility, viscosity, changing demands; author states scope is limited; principles framed as design argument | That Martin formally asserted five unconditional mathematical axioms |
| Five-principle mnemonic known as SOLID (popularized in 2000s) | Consolidation into memorable professional guideline cluster (exact timeline needs archival sources beyond secondary summaries) | That there is a single precise 2000 date for the full acronym; **Michael Feathers 2004 attribution requires primary corroboration** |
| LLM coding-agent era (2020s) | Systems can ingest persistent local instructions; code generation and architecture decision support are consequential | That any specific provider hard-coded SOLID into foundation-model training, or that an industry-scale causal increase in dogmatism is already measured |

**Verified historical sources:**

1. Andrew P. Black (2013), authoritative historical account: "Object-oriented programming: Some history, and challenges for the next fifty years," *Information and Computation* 231 (2013), doi:10.1016/j.ic.2013.08.002, https://arxiv.org/abs/1303.0427
2. Alan C. Kay (1993), "The Early History of Smalltalk", ACM SIGPLAN Notices 28(3), DOI 10.1145/155360.155364, https://doi.org/10.1145/155360.155364
3. D. L. Parnas (1972), "On the criteria to be used in decomposing systems into modules", CACM 15(12), DOI 10.1145/361598.361623, https://doi.org/10.1145/361598.361623
4. B. Liskov and J. Wing (1994), "A Behavioral Notion of Subtyping", ACM TOPLAS 16(6), DOI 10.1145/197320.197383, https://www.cs.cmu.edu/~svc/papers/view-publications-lw94.html
5. Robert C. Martin (2000), "Design Principles and Design Patterns", primary 34-page text, https://www.fil.univ-lille.fr/~routier/enseignement/licence/coo/cours/Principles_and_Patterns.pdf — **p.1 says this treatment is limited**; pp.2–3 specify concrete deterioration symptoms, and p.3 explicitly recognizes multiple ways of implementing a change. This is strong evidence AGAINST caricaturing the primary author as claiming a universal axiom system.

## Distinguish four distinct meanings of 'axiomatization'

**Logical axiomatization:** formal premises and proven consequences, with an explicit domain; intellectually legitimate. **Professional canonization:** mnemonic pedagogical simplification and repeated expert teaching; historical process requiring evidence. **Operational quasi-axiomatization:** an agent or evaluation loop refuses otherwise admissible designs due to a hard SOLID instruction *even after relevant negative evidence*, despite no validated universal scope. **Normative legitimacy:** whether such refusal is justified in a given project, a separate judgment.

Hypothesis H-history-1: the packaging of heterogeneous design advice as a small mandatory bundle increases unconditional/exception-free prescriptive wording in teaching and repository guidelines. Hypothesis H-agent-1: a hard SOLID file injected into a coding agent increases SOLID-conforming design selection, independent of source behavior. H-agent-2: this may **reduce or improve** correctness/maintainability depending on demand and alternative architecture; there is no preselected effect sign. H-feedback: generated text may recursively influence future advice, but **training-data, amplification rate and industry effect are UNIDENTIFIED**.

## AI claims: grounded mechanisms versus unproven causal narrative

- OpenAI's public model-development policy states broad classes of information used in development, not verifiable inclusion/counts of SOLID primary documents in particular training runs: https://openai.com/policies/how-chatgpt-and-our-foundation-models-are-developed/
- OpenAI Codex documents repository-scoped AGENTS.md injection; this **shows an instruction channel**, not an axiom in model weights: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- Anthropic documents CLAUDE.md persistence/read at each project session; again a user/team instruction layer, not proof of pretraining: https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts
- Gloaguen et al. (2026), "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" https://www.sri.inf.ethz.ch/publications/gloaguen2026agentsmd: agents respect context-file instructions, and this can add inference costs without improving task success. **Crucially NOT a test of hard SOLID prompts**, so not direct evidence of 'SOLID amplification'.
- A multivocal review of GenAI for software architecture (JSS 231, 112607, 2026), https://doi.org/10.1016/j.jss.2025.112607 reports use for architectural decision support but does not establish historical SOLID dogmatization.

**Avoid causal leaps:** widespread source availability ≠ exposure in a specific training sample ≠ trained preference ≠ prompted adherence ≠ developer acceptance ≠ industry norm transformation. Never infer specific proprietary-model corpora from public web availability. Do not write "LLMs were trained on SOLID and therefore made it axiomatic" as settled history.

## Independent paper-B falsifiable research design

1. **Dated texts / historiography:** pre-LLM (e.g. 2000–2021) and agent-era (2022–2026) matched design-advice documents from comparable source types; record publish dates, revision history, audience and genre; **no post-hoc selection by strong prescriptive wording**. Classify original advice and explanatory prose rather than conflating blog posts with official standards.
2. **Axiomatization *operational* coding rubric:** imperative absolutism ('must/always'), source and scope omission, exception/negative case suppression, rejection of a semantically valid non-SOLID alternative, presence of explicit reversal/abstention. Audit annotator disagreements; do not label every assertive guideline as dogma.
3. **Agent factorial on authentic Go tasks:** same pinned task and source; randomized counterbalanced conditions `NONE`, `HARD_SOLID`, `SCOPED_SOLID`, `EVIDENCE_CONDITIONAL`. Use fresh agent contexts, fixed versions/temperatures/budgets and an architecture-neutral full Go test oracle. Outcomes: real correctness, code structure, explicit scope/exception reasoning, counterexample response, reversibility after supplied contradictory evidence. Report per-case paired and cross-agent outcomes; do not assert a statistical population effect from one small case.
4. **Moderation and alternative explanations:** programmer education and OO-language ecosystem, training corpus unknowns, project-specific conventions, test pressure, static analysis tooling, post-training instruction policies. Rival hypotheses include 'agents mirror local instructions' and 'principle vocabulary improves explanation without changing code'. Include agent-and-human baselines only if independent reviewers available.
5. **Causal identification limit:** even a clean randomized user-prompt/context experiment identifies the impact of **present instructions on the tested agents**, NOT a proprietary training-weight mechanism, nor long-run historical adoption. A historical rise in imperative wording cannot alone identify an LLM effect.

## Paper B synopsis (working English abstract — not submitted)

*"Software design guidelines are often presented as if their authority were independent of the changing systems they were meant to improve. We trace the historically heterogeneous development of object orientation and SOLID, distinguishing formal axioms from professional canons and instructions that operate as hard design constraints in coding agents. Using primary historical documents, prospective coding of developer-facing guidance, and controlled coding-agent interventions on pinned Go maintenance tasks, we propose to test whether architectural guidance can harden into a context-insensitive prescription. We do not assume that particular foundation-model training datasets included SOLID or that language models caused historical dogmatization. The broader goal is an empirically revisable account of when established design advice is justified, superseded or best left conditional."*

**Publication gate:** must add source-coded archival corpus with transparent sampling and at least one actual agent prompt comparison; this historical outline alone is a **proposal**, not journal-ready evidence. Potential genres: a historical-critical software-engineering essay (if empirical claims restrained) and empirical coding-agent guideline study (if prereg and replicated).


## Standing unresolved historical-source acquisition

The [cross-checked A/B bibliography audit](P35_PAPERS_A_B_MISSING_FROM_DRIVE_LITERATURE_AUDIT.md) identifies four highest-priority primary/empirical texts not found by title/author in accessible Drive metadata: **Kay (1993) Smalltalk**, **Black (2013) OO historiography**, **Martin (2000) original design principles**, and **Gloaguen et al. (2026) AGENTS.md naturalistic study**. Additional **Esposito et al. (2026) GenAI for software architecture** is also not found. Not-found-by-filename is not conclusive absence. Original paper rather than paraphrase is necessary before historical claims graduate; non-OA access restriction is a legitimate HOLD, not a reason to erase prior art. Martin (1996) DIP and Liskov–Wing (1994) are already verified in Drive.
