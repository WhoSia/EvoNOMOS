# Paper B R35 — SOLID Lexical Hardening: A Bounded, Falsifiable Linguistic Hypothesis

**2026-11-23 · Independent research lane A (lexical/historical).** This is a proposed vocabulary study, NOT a completed corpus analysis and NOT proof that SOLID has been historically axiomatized.

## Source-restored problem
The user's actual 2026-07-29 founding complaint (read directly in [EvoNOMOS Archive 1.md](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view)) distinguished **원칙** (a defeasible guideline) from **규칙** (a norm with application conditions and enforcement) and **공리** (formally accepted premise). The user emphasized that nobody had formally declared SOLID an axiom; nonetheless use by tools may *appear* axiom-like. The original concern was epistemic autonomy and the possibility of conditions or principles superior to memorized slogans. This does NOT demonstrate that industry documents or model outputs actually shifted over time.

## Distinguish five lexical and speech-act functions
| Coding | Example, **invented solely to illustrate coding rubric** | What the sentence purports to do | Missing claim that needs external proof |
| --- | --- | --- | --- |
| D — descriptive | "새 구현은 상속 계층 하나를 추가한다." | source observation | whether the description is factually correct |
| H — conditional heuristic | "새 타입이 자주 늘어날 예정이라면 OCP형 확장이 유리할 수 있다." | proposes contingent design policy | expected change distribution, boundary costs |
| V — evaluative label | "이 구현은 OCP 위반으로 분류될 수 있다." | assigns a design-quality label | classifier standard, evidence, reliability |
| N — norm / directive | "OCP 위반은 반드시 수정해야 한다." | directs behavior with asserted obligation | authorization, exceptions, priority |
| A — purported axiom | "SOLID는 예외 없는 설계 공리다." | asserts unconditional conceptual status | formal system? empirical invariance? no known warrant here |

The sequence **H→V→N→A is a possible movement in a text** and an investigable coding pattern. It is NOT assumed chronological inevitability or a completed empirical history. "Principle", "guideline", "best practice", "rule", "violation", "must", "never", "always", "axiom", "nonnegotiable" are **candidate surface markers** only; a historical occurrence may refer to a genuinely authorized requirement, an illustrative hypothetical, a negative quote, an ironic example or a condition carried in a neighboring sentence. Do not count unexamined key words as endorsement.

## The real hypothesis, modest and distinctive
**H-Lexical:** At least some contemporary design advice, review rubrics or agent-facing guidance might use *SOLID* and its named subprinciples as if they conferred unconditional patch-review obligations while omitting original expected-change and protected-client conditions. A source-grounded, human-coded corpus can test whether and when this happens. An AI-agent experiment can separately test whether a **lexical promotion** changes actual patch behavior after instruction priority and functional contracts are fixed. A hypothesis can be false.

**Rival 1: faithful shorthand.** Engineers who say "OCP violation" may already know the context and intend a scoped warning; no unwarranted authority transfer.
**Rival 2: legitimate requirement.** A team may explicitly make SOLID a project policy. The requirement is authorized and a coding agent ought to respect it, even if another design could satisfy business behavior.
**Rival 3: true structural violation.** An evaluation might correctly classify a design feature as violating one structural formulation of OCP; that doesn't settle task-level acceptability but is not inherently incorrect.
**Rival 4: ordinary prompt salience.** Phrase choice or prohibition language may change agent choices without any special SOLID epistemology.
**Rival 5: selection bias.** Policy documents containing "must" are easier to find than nuanced design conversations, making a historical hardening trend look artificial.

## A separable, executable study plan (not run)
1. Assemble a **pre-registered dated and genre-stratified corpus**: original Meyer/Martin and later SOLID exposition, text of public education/training, coding-style guides, source repository instruction files, code review and architecture decision records. Preserve legally accessible URLs/editions and dates; sample by genre/year before inspecting outcomes. Do not assume training-set membership for any AI.
2. Annotate each *complete claim+context span*, not isolated tokens. Coders record principle mentioned, speech-act D/H/V/N/A, modality, attached conditions, explicitly protected contracts, claimed speaker authority, quote/negation status, default action, and evidence sufficiency. Distinguish actual historical occurrence from synthetic author example. Inter-coder agreement and disagreement adjudication required.
3. **Negative historical control**: compare similarly popular non-SOLID software guidance, and actual legally binding security/configuration policies. A modal "must" is not categorically problematic.
4. Analyze whether modality distributions change by **time within document genre**, and whether qualifiers are included in sentence/paragraph context; no inference of individual model pretraining or causal historical transmission from corpus co-occurrence alone.
5. Separate study B: controlled coding-agent patch review where task, contract tests and authorized policy are held constant while **H vs V vs N** normative formulations vary, including a no-SOLID baseline and a semantically scoped version. Changing a statement from advice to command **also changes its semantics/authority**, so the comparison cannot be called a "pure name effect." Report whether the edit is authorized, not only whether wording changes.
6. Disconfirm: conditional qualifiers remain intact across genres; directive use is always expressly authorized/scoped; the lexical shift changes only explanations, not patches; alternative non-SOLID conventions produce indistinguishable effects.

## Specific risks to avoid
- **Axiomatization ≠ formal logic:** The phrase *quasi-axiomatization* is a metaphor naming an investigable change of epistemic *status*, not a mathematical claim.
- **No fabricated historical chain:** Parnas→Meyer→Martin→public text→AI is a possible genealogy to research, not an already demonstrated pipeline.
- **Surface token counting is insufficient:** a sentence quoting "must not" could be rejecting dogmatism. Need adjacent-sentence meaning and speaker stance.
- **Named vs unnamed is not the whole issue:** v29 overfocused on cue salience, not user’s central normative-vocabulary concern.
- **Do not expand Paper B into the entire pipeline:** main position paper should state the problem, one historical illustration, one lexicon taxonomy example, and a few falsifiable invitations. Detailed protocol lives here.
- **Do not publish a causal agent-effects conclusion:** the two newly ingested PDFs demonstrate general instruction/precedent effects, not this specific SOLID normative-hardening transition.

## Source-specific prior work separation
[Zhu et al. 2026 original PDF](https://drive.google.com/file/d/1mk1MmGh5QfFUPmT_CTe9srLTDEZjU784/view): 5,625 trials of implementation preference and repository precedent; original paper body did not name SOLID/OCP in extracted textual keyword audit.
[Laddha et al. 2026 original PDF](https://drive.google.com/file/d/1E-alGOnlpVPoE8IHSF1USVyRWhMVQHrv/view): source-*label* / position / role conflicts, not *design principle* label. Original body did not directly test SOLID or OCP.
Neither textual absence establishes worldwide literature firstness; [R34 annotated source reading](79_PAPER_B_R34_TWO_2026_PDFS_FULLTEXT_READING_AND_DRIVE_CUSTODY.md) gives full controls and limitations.

**Research status:** LEXICAL TRANSITION HYPOTHESIS SPECIFIED / HISTORICAL CORPUS NOT ASSEMBLED / INTER-CODER TEST NOT RUN / LIVE AGENT STUDY NOT RUN.
