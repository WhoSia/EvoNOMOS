# Paper B R34 — Two Newly Ingested PDFs: Full-Text Reading and Source-Custody Ledger

**2026-11-23 KST · Connected Google Drive source review; verified metadata-only move.** These are the two newest PDFs in Research OS's `00_INTAKE — Literature Radar`, whose direct IDs and file bytes were preserved. A third older `2512.19466v1.pdf` was not requested in the two-item intake and remains in 00.

## File acquisition and custody
| Original intake name | Source Drive ID | New title (verified) | Destination |
| --- | --- | --- | --- |
| `2610.38244v1.pdf` | `1mk1MmGh5QfFUPmT_CTe9srLTDEZjU784` | **Zhu et al. (2026) — Precedent or Intent - What Coding Agents Follow When Evolving Existing Code — arXiv 2610.38244v1.pdf** | [10_PAPERS](https://drive.google.com/drive/folders/1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP) |
| `2610.33201v1.pdf` | `1E-alGOnlpVPoE8IHSF1USVyRWhMVQHrv` | **Laddha, Pradhan & Srivastava (2026) — Position, Role or Label - A Controlled Study of Instruction Conflicts in LLM Agents — arXiv 2610.33201v1.pdf** | same |

Source parent: `1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16`; both PDF files originally uploaded on **2026-11-22 ~19:30 UTC (2026-11-23 ~04:30 KST)**, metadata shows later than the third 2025 paper. Target `1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP` is the Research OS canonical 10_PAPERS commons. Drive `update_file` with `addParents` and `removeParents` succeeded for each; **post-write `get_file_metadata` independently reconfirmed both titles, same IDs, both parent IDs exactly `10_PAPERS`, and original sizes 387141/872920 bytes**. No PDF content was overwritten. Duplicate checks by both arXiv IDs returned no prior matching files. The third `2512.19466v1.pdf` remains in intake unchanged.

### Original PDF links
- [Zhu et al. 2026 — Precedent or Intent?](https://drive.google.com/file/d/1mk1MmGh5QfFUPmT_CTe9srLTDEZjU784/view)
- [Laddha et al. 2026 — Position, Role or Label?](https://drive.google.com/file/d/1E-alGOnlpVPoE8IHSF1USVyRWhMVQHrv/view)

## PDF 1 · Zhu, Xu, Yang, Wang & Zhang (2026)

*Precedent or Intent? What Coding Agents Follow When Evolving Existing Code*. ArXiv `2610.38244v1`; source PDF first page is dated October 26 and arXiv version banner October 28. Text in the user's uploaded PDF was extracted/read across Abstract, §1–§7 (including Methods §§3.1–3.6, evaluation §§4.1–4.6, §5 Threats to Validity, §6 Related Work, §7 Conclusion). Full accessible text ~69.5k raw characters. The following are **the authors' empirical findings**, not experiments performed by EvoNOMOS.

**Question:** When several implementations meet the same functional task specification, which choices do coding agents make based on (a) default implementation preferences, (b) existing code precedent, or (c) written current task instructions?

**Identification design:** Three stages. Stage 1 suppresses nearby endpoint examples to elicit model/harness defaults. Stage 2 manipulates support count and placement of examples in local versus sibling-resource code, keeping functional hidden tests constant. Stage 3 makes existing six endpoints follow the opposite choice to a requested new implementation and compares no guidance, a written rule, a code example, and both. Trial is an independent agent session on a fresh repository instance. Agents: Claude Sonnet-4-6, Claude Opus-4-8, gpt-5.6-sol and gpt-6-sol paired to their respective harnesses.

**Reported evidence:** 5,625 trials, 4 agents, 6 implementation pairs and validation in 4 public repositories (Python/Go/TypeScript). With one local source precedent, agents depart from defaults in 359/360 corresponding cases; across increasing local support, alternative adoption at 0,1,2,3 out of three local files is 0/360,74/359,175/360,347/360 (~0%,21%,49%,96%). Strong sibling precedent alone is much less influential: 13/360 adoptions with three sibling files (~4%) versus 347/360 local. In selected explicit-conflict trials, 59/60 joint successes with written rule versus 38/60 with example, 0/60 no guidance, 60/60 with both. Open-source native instruction file comparison: 117/120 joint successes with rule versus 0/120 without for the authors' envelope case. These percentages characterize controlled choices under their specifications, not **general code quality** or all AI agents.

**Crucial limitations admitted by authors:** location and task-relatedness vary together in some contrasts; examples controlled as available not necessarily attended; 15 repetitions per cell and controlled Flask API family limit generalization; different model/harness combinations cannot be attributed to weights alone; classifiers track implementation **choice**, not maintainability or quality; the rule-loaded-by-harness test does not show spontaneous discovery. Their "functional equivalence" is defined by pair-specific hidden tests, not full semantic equivalence of all clients.

**Implication for Paper B:** The general effects of existing convention and task rules in real coding-agent edits **are no longer a novelty claim** for us. The prior study does not inspect OCP/SOLID language, the difference between a *principle* and a *binding rule*, the normative verbs `violation/should/must/always`, or the possibility that a common **higher-order conditional structural criterion** explains the principle. In the article's substantive sections (prior to conclusion), `SOLID`, `OCP`, `design principle`, `axiom` have no exact text mentions. That count is a bounded search in extracted text, NOT proof that no synonyms or relevant ideas exist.

**Further adversarial note:** Since the authors already manipulate instruction text and repository placement, our experimental proposals must supply a distinct outcome grounded in *the authority attached to principle terminology and the conditions of application*. Label-only manipulation by itself is not unique.

## PDF 2 · Laddha, Pradhan & Srivastava (2026)

*Position, Role or Label? A Controlled Study of Instruction Conflicts in LLM Agents*. ArXiv `2610.33201v1`; dated October 23. Original PDF text ~213k raw characters and 55 pages with extensive methods and appendices; main body Abstract–§5 and key appendix study-design headings were examined.

**Question:** When instructions conflict, how does the winner depend on location/order (position), actual chat role, and a text label that purports to name an instruction source? Note that `label` here denotes the **claimed instruction source seat** such as operator/repository/user/tool/memory, *not* the recognized name of a historical software-design principle like OCP.

**Design:** WHOWINS with 1,080 code-scored scenarios of five task types (tool call, file write, format, action order, gated refusal), up to five mutually incompatible instructions, and 7 controlled variations in how instructions are presented. Five "seats": operator, repository config, user, tool output, memory. Fourteen open-weight models, twenty-six model/mode combinations and 1,887,356 scored replies. This is **instruction conflict adjudication**, not whole-repository maintenance correctness. They measure behavior without relying on LLM adjudicators for their code-scored outcomes.

**Reported findings:** Inside one message, the first of two conflicting instructions wins ~72.42–94.66% of decided replies, but across messages the first has lower share (~22.95–62.65%). With real system/developer roles, outcomes depend on the model family; in **tool and file-write tasks**, an earlier operator instruction in the actual system/developer role wins **6.41–48.75 percentage points less often** than the same labelled text placed in a user message across studied model-modes. Thinking increases some Qwen models' obedience to declared numerical tiers, but does not guarantee it; at most 2.92% of decided pair replies visibly flag/hedge an instruction conflict under their keyword extraction. Their experiments isolate source/role/label position effects; they **do not identify independent design-axiom canonization**.

**Important scope caveat:** Real system/developer message layouts may contain tool definitions, whereas the fake-labelled user message does not; authors themselves note this can confound role and tool-definition proximity. Scenarios include artificial mutually exclusive values and are not a sample of historical design principle advice. Results are from the tested model families and message formats, not proof about all assistants. Long PDF appendix includes many literal prompts; those are study artifacts, not instructions to follow during research.

**Implication for Paper B:** "Different labels change agent behavior" is a known research theme. Its **`source-label`** is not the same construct as our **`normative design vocabulary`** or **`principle name/violation wording`**, but merely observing a name effect would still be too weak. Our more defensible research object is whether historically conditional design *advice* is linguistically reclassified as a binding rule or a violation verdict, and what happens to actual patch choices under independently established contracts and legitimate instructions. No matching study in this paper specifically of OCP/SOLID was identified; that alone does NOT prove we are first.

## Comparative "not our result" table

| Dimension | Zhu et al. | Laddha et al. | Proposed Paper B |
| --- | --- | --- | --- |
| Research object | local code precedent vs explicit task intent | conflicting instruction source/role/text label | historical design-principle term and its conditional application authority |
| Unit | repository code modification trial | code-scored agent response | historical prose + agent patch disposition, eventual source-grounded audit |
| Intervention | example location/count and task priority rule | instruction position/role/source label | *normative lexical force* (`principle`, `violation`, `must`, `always`) within clear scopes; named vs unnamed as secondary |
| Outcome | functional tests + chosen implementation | chosen conflicting instruction | documentation of lost qualifiers, actual patch behavior and justified revision, if observed |
| Strong alternative | code-locality and task semantics | ordinary instruction hierarchy and message order | ordinary contracts, approved policies and lexical framing; no automatic dogmatism |
| Relationship to higher-order structure | not a study of SOLID reduction | not a study of SOLID reduction | future, separate research axis; **no reduction yet discovered** |

## Decision / future citation
1. Both original PDFs now curated and verified under 10_PAPERS; retain their exact version suffix `v1`.
2. In Paper B cite each once as powerful neighboring work, not a lengthy "related work" section; put full technical method numbers here.
3. Keep user-specified title and intellectual priority: **conditional SOLID principle → linguistically hardened rule → potential machine-enforced verdict**; this is a hypothesis, **not an empirically established historical causal trajectory**.
4. Any follow-up agent experiment needs a source-verified, contract-sensitive verdict and an authorized instruction hierarchy. A name-only contrast cannot by itself identify special normativity.
5. Treat exploration of a common higher-order architecture law as its own structural research programme, not as a theorem smuggled into a position paper.

**Research disposition:** `SOURCE PDFs READ · TWO FILES RENAMED/MOVED/VERIFIED · GENERAL RULE EFFECT PRIOR-ART CLEAR · SOLID NORMATIVE VOCABULARY HYPOTHESIS OPEN · AGENT TRIALS UNRUN`.
