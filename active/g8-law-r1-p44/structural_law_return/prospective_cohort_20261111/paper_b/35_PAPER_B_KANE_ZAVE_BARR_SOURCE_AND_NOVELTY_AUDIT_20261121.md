# Paper B v15 evidence memorandum — Three newly acquired originals, inference-to-use and requirements-oracle boundaries
**2026-11-21 | Source-close-reading note, not an experiment.** Prior manuscript: [bilingual v14](./PAPER_B_BILINGUAL_INTEGRATED_14_20261121.md). This note corrects the active *missing* status of three originals; other projects must not relocate these files without current parent verification.

## Source receipts

| Original | Drive raw file, current at first read | SHA-256 of fetched PDF | PDF pages | What was inspected |
|---|---|---|---|---|
| Michael T. Kane (2013), *Validating the Interpretations and Uses of Test Scores*, JEM 50(1):1–73 | [kane2013.pdf](https://drive.google.com/file/d/1nbQUgK4kFkjKS4X9Op_q2e5H-Vgm8epM/view) | `13adced4ea89c2b13bc930572021692e5cac88c05f6461c1105959d40caa092b` | 73 | First-page official volume, abstract, interpretation/use argument sections and concluding points; not a full close reading of every page |
| Pamela Zave & Michael Jackson (1997), *Four Dark Corners of Requirements Engineering*, ACM TOSEM 6(1):1–30 | [dark-corners-re-zave-jackson.pdf](https://drive.google.com/file/d/1PwUeINSkW6vhhuUvYEh9YvGQFBWlWlav/view) | `382e5f7723ee15c5ebe67c1056540bc57ee9098f1bd3144a887ee02665425dca` | 30 | Abstract, introductory four conclusions, control of actions, §requirements-versus-specification and completion conditions |
| Earl T. Barr et al. (2015), *The Oracle Problem in Software Testing: A Survey*, IEEE TSE | [06963470.pdf](https://drive.google.com/file/d/1GvLHYntPcmuPdjuFmKZdenmBHeAy0SxY/view) | `0572def3bfd4baaadb2041a098f12a0bac261427962e46cef084efff60fd3a36` | 19 | Abstract, introduction, partial oracles, specification-driven and derived oracles. PDF internal title verified, page extent is PDF pages, not asserted journal pagination |

The three were present in the globally shared `00_INTAKE` in the first 2026-11-21 scan; their exact PDF bodies were accessed through connected Drive, raw fetched, locally SHA-256 checked. Parent locations may change in parallel sessions. Do not infer move completion from this note.

## 1. Kane (2013) is a substantive novelty challenge, not an OCP empirical result

Kane distinguishes an observable test performance, an interpretation of a score, and the *use* of that interpretation to guide a consequential decision. He explicitly rejects assuming that a validated score interpretation validates a proposed score use, and calls for spelling out the inferences, assumptions and consequences of the use. This is precisely the general **evidence-to-decision transfer** issue that Paper B otherwise risks presenting as new. But Kane does not audit SOLID labels, code review or patch acceptance. We should explicitly credit the *general distinction*, retaining our narrower OCP source audit and controlled patch illustration as a domain-specific application.

**Argument boundary:** an OCP label `L` can be accurate under its benchmark rubric; without evidence that the requirements `D`, protected calls `C` and scope `S` authorize rejecting *the particular patch*, `L` does not entail that use. Our study has not measured consequential use in real software reviews and should not claim Kane's validity theory experimentally tested in software engineering.

## 2. Zave & Jackson (1997) put the source of requirements, actors and obligations at the center

The 1997 paper distinguishes:
- requirements for desired *environmental* effects,
- machine specifications at the machine/environment interface,
- domain knowledge `K` about indicative facts in the environment,
- proof that `S, K ⊢ R` (the original PDF's entailment symbol is imperfectly extracted) and consistency of `S` with `K`.

Crucially, it requires making explicit which shared actions are controlled by the machine and which by the environment. This is directly applicable to Martin's drawing case: sorting may be a *caller-controlled precondition* or a *callee-guaranteed output requirement*. It is not enough to inspect an unsorted output or a code-pattern label. The exact environment/machine partition matters. The catalog's book contract is **author-stipulated**, not discovered by applying Zave–Jackson to a real repository.

We must not claim to introduce requirements/environment separation, assumption/guarantee composition or clarification questions generally. Paper B's distinctive object is **using an OCP label as a rejection warrant for one proposed patch**, with an explicit abstention/next-question policy.

## 3. Barr et al. (2015) limits what our fixture tests prove

The survey defines an oracle as the means of determining correct vs faulty observed behavior. Without formal complete specifications, the testing literature already has *partial* oracles from invariants, contracts, documentation, prior versions, metamorphic relations and human judgment. A test result in our catalog establishes the stated observed output or exception on the specified input; **whether that is a contract violation depends on a separately authenticated expected behavior**. None of the v14 tests exhaustively establishes all client obligations, and a source method declaration's deletion need not prove contract breach.

This is a closer software-engineering novelty rival than Kane. Use the phrase 'selected authored test observations', not 'proof of full contract preservation' or 'verified real-world rejection'.

## 4. New reviewer-facing prior art identified by public search, acquisition not yet verified

- Haolin Jin & Huaming Chen (2026), *Are LLMs Reliable Code Reviewers? Systematic Overcorrection in Requirement Conformance Judgement*, [doi 10.1007/s10515-026-00638-5](https://doi.org/10.1007/s10515-026-00638-5), [arXiv:2603.00539](https://arxiv.org/abs/2603.00539): model false-rejection and unsupported rationales on requirements conformance, experimental rather than OCP classification. Public article checked for bibliographic/abstract only, not whole PDF.
- Widyasari et al. (2025), *Explaining Explanations: An Empirical Study of Explanations in Code Reviews*, [doi 10.1145/3708518](https://doi.org/10.1145/3708518), [author-hosted PDF](https://researchmgt.monash.edu/ws/portalfiles/portal/736501150/736500695-oa.pdf): a real code review taxonomy including rule/principle explanation. Abstract and article metadata only; original full PDF not located in present Drive search.
- Papotti, Paramitha & Massacci (2024), *On the Acceptance by Code Reviewers of Candidate Security Patches Suggested by Automated Program Repair Tools*, [doi 10.1007/s10664-024-10506-z](https://doi.org/10.1007/s10664-024-10506-z): controlled real reviewer accept/reject research, but cybersecurity patch domain and no OCP frequency measurement here.
- *Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements* (2026), [doi 10.3390/systems14101312](https://doi.org/10.3390/systems14101312): source-based account of negotiated acceptance/deferral, potentially close. Public article metadata inspected, full close read outstanding; do not assert direct originality without reading.

These works should be checked against an actual Paper B claims matrix before submission, not automatically added to §4 as a literature dump. A missing-only, copyright-respecting acquisition list is preserved separately.

## 5. Editorial decision for v15 (requested short, question-driven Paper B)

1. The abstract should **not** say Kane or Zave proved OCP over-axiomatization exists. Retain name 'over-axiomatization' for *a risk in misusing a design label* and a question about warranted use.
2. In §3 explicitly separate empirical data, source interpretation, authored norm/criterion, and observed fixture outputs; 768 rows / 64 conditions / 24 templates are not independent reviewer verdicts.
3. In §4 append 2 short paragraphs: Kane transfer-to-use distinction; Zave/requirements-control + Barr/partial oracles. Describe their boundaries, do not overclaim novelty.
4. In §5 preserve the decision diagram's status: authored definitions imply 1 accept/3 reject and 1/5/3 under partial disclosure. Add **evidence provenance** for each axis: actual change request, external API/source docs, test witness, edit authority, route. In the constructed case those axes were explicitly stipulated.
5. With zero compatible candidate specifications, return *inconsistent premises*, never 'accept' through vacuous unanimity. Any unknown real requirements outside enumerated choices may invalidate the procedure's scope.

**Research director verdict:** intellectual contribution is currently a compact methodology/application with falsifiable boundaries; no novelty as general logic of validation/requirements/oracles is supported. Source audit and patch construction are distinguishable; the move from a classification rubric to a real rejection judgment remains prospective.
