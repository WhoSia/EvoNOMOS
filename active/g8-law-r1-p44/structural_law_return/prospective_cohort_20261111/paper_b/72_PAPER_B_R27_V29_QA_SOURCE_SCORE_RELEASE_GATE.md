# Paper B R27 — v29 Bilingual Readback, Source, Score and Release Gate

2026-11-23 KST · This is an internal textual source-quality check, not a peer review or agent experiment.

## Verified artifact state

- Original v28 and all prior 01–27 editions remain preserved, not overwritten.
- v29 manuscript: [PAPER_B_BILINGUAL_POSITION_29_20261123.md](PAPER_B_BILINGUAL_POSITION_29_20261123.md). GitHub blob `b0582e72de08641c0719637d9b4f6a2275705708`; 11,061 connector characters; original source readback confirms **6 numbered sections in Korean and 6 numbered sections in English**, plus abstracts (7 manuscript parts per language). Changes are deliberately short.
- v29 sentence editor: [R25 score audit](70_PAPER_B_R25_V29_SENTENCE_SCORES_AND_ADVERSARIAL_REVIEW.md). Every sentence in two languages receives explicit editorial role, comment, identifier and subjective retention score. Exactly **78 distinct rows**.
- [Author-review Notion page](https://app.notion.com/p/420ef561cf9281299541faf3c781a210): created in original Paper B workspace and fetched again after the score rendering correction. Notion readback contained all **78** colored score rows: **green 56 / orange 20 / red 2**. `truncated` absent, and manuscript's Martin/Parnas/independent-four-arm status survives. No Notion side panel opened; user had requested a link rather than opening.
- The initial Notion creation generated malformed color-score markup due to an extra regex capture group (displaying a colored K/E instead of numerical score and falsely zero group totals). This was **diagnosed and fully corrected in the same turn** by 79 exact Notion search-replace operations. The verified readback above is after repair. Do not cite the pre-repair artifact as the final state.

## Main methodological gain and its limit

**Gain:** differentiate a mere familiar principle *label* from the semantic content of advice and its instruction priority, then observe contract-grounded patch disposition and response to authenticated counterevidence. The previous P35-B1 4-arm design manipulates the *content* of advice; the proposed v29 design manipulates the *name attached to otherwise equivalent advice*. They are distinct prospective interventions.

**Threats:** no neutral wording truly matches every pragmatic implication of a historically famous name; multiple controlled paraphrases, blind semantic checks, authority hierarchy, randomized source tasks, conventional requirements reviewer and neutral prestige cues are needed. Even a name effect would show a **behavioral framing effect in tested agents**, not the model's inner axioms or a novel causal mechanism.

## Historical improvement verified
- David Parnas 1972 on likely-to-change decisions, 1979 on extension/contraction and families of programs. Both are pre-SOLID classical ancestors. MIT primary 1979 PDF was directly checked, including first-page screenshot.
- Robert C. Martin's 1996 OCP paper (Strategic Closure pp.6–7; Heuristics and Conventions pp.11–13) includes exceptions and explicitly distinguishes a public member's bad style from necessarily bad design; RTTI can be compatible with OCP. Avoid claim his article was a formal five-axiom declaration. University-hosted PDF textual lines checked; one screenshot endpoint failed. Public copy text also inspected.
- Meyer 1988 account limited to recovered first-edition pp.22–25 in earlier project note; cannot imply the entire 1988 book read.
- Google 2026 CHI EA primary PDF checked (first and third pages visually): enterprise developer rules already include high-level design principles such as DRY and loose coupling, supporting a stronger novelty veto.
- Xu & Wu 2026 stale instructions, Gloaguen et al. 2026, 2026 rule impact, and code-review overcorrection already cover broad claims about coding agent rule effects or unsound review.

## Unsparing current editorial judgment

| Axis | Subjective rating | Why |
| --- | ---: | --- |
| Question clarity | 0.94 | First-paragraph question can be reproduced in one line |
| Historical exactness | 0.92 | Martin's own qualifications and Parnas genealogy supplied |
| Novelty relative to confirmed neighboring studies | **0.51** | Narrow name cue under matched semantic authority may still be normal framing or known prior work |
| Causal identifiability of proposed factorial | 0.72 | Better intervention; equal meaning/priority is hard to ensure |
| Sentence rhythm / brevity | 0.86 | Compact and concrete; low scoring sentences marked |
| Agent evidence | **0.30** | Zero independent treatment observations. No effect estimate |
| Counterevidence / negative outcomes | 0.95 | Includes strict principle benefit, lexical-only effect, no effect, classical explanation |

Two red scored phrases are **K01.03** and **E01.03** (phrased as "new" or "our narrower question"). They do not prove new scholarly priority. The user-facing annotation explicitly marks them. Whether to replace them with more qualified phrasing is an author decision; no need to hide the contested lines.

## Commit and dissemination integrity
- All write commits in this iteration were authored and committed by `WhoSia`; `github-actions[bot]` absent from new writes; no new branches created.
- GitHub verified sources: [R23 history](68_PAPER_B_R23_HISTORICAL_MARTIN_PARNAS_HEURISTICS_AUDIT.md), [R24 near-prior art](69_PAPER_B_R24_2026_NEAR_COLLISIONS_AND_NAME_EFFECT_ESTIMAND.md), [v29](PAPER_B_BILINGUAL_POSITION_29_20261123.md), [R25 score audit](70_PAPER_B_R25_V29_SENTENCE_SCORES_AND_ADVERSARIAL_REVIEW.md), [R26 falsifiable prospective protocol](71_PAPER_B_R26_NAMED_PRINCIPLE_COUNTEREVIDENCE_PROTOCOL.md).
- Notion written and independently read back; next update should retain this link in main workspace navigation.
- **No** four-arm executions, named-label agent executions, new Go tests, measured token/energy benefit, external real peer review, or new universal software law.

**Decision:** Paper B v29 is a more original **proposed contrast** than broad v28 wording, but is still an unvalidated research idea. Treat the 0.51 novelty and 0.30 empirical evidence ratings as critical editorial judgments, not probabilities. `PAPER B V29 AUTHOR REVIEW · TEXT CHECK PASS · NOVELTY OPEN · PRE-AGENT-RUN · LAW-R2 HOLD`.
