# Paper B — Director's source-to-claim audit (2026-11-17)

## Scope and version history

The authoring hub is [Paper B workshop](https://app.notion.com/p/41bef561cf9281fa91bcf17a2a45fd8b). Notion integrated copies [01](https://app.notion.com/p/41bef561cf9281c2b45dee94b4744969), [02](https://app.notion.com/p/41bef561cf92819fa364da217c66be0f), [03](https://app.notion.com/p/41bef561cf9281968d9adaf0d0a5ffef), [04](https://app.notion.com/p/41bef561cf9281338542d18745ef9f9e), [05](https://app.notion.com/p/41bef561cf928187b1b7fc100f9a0995), [06](https://app.notion.com/p/41bef561cf92816d8046c0412661621c) and [07](https://app.notion.com/p/41bef561cf9281cbaf29c9a9b5daba1e) remain distinct. Version 07 is archived in GitHub as `PAPER_B_BILINGUAL_INTEGRATED_07_20261117.md`; previous GitHub v0.1/v0.2 remain separate.

## The argument that must survive every prose edit

The claim is not that OCP is invalid, not that SOLID and OOP are synonyms, and not that the acronym has been shown to cause bad decisions. It is this narrower problem: a principle argued for with specified changes and obligations may be re-used as a self-sufficient violation label. Before such a label licenses rejection of a particular edit, the reviewer needs an identifiable change request, protected caller commitments and, for judgments of implementation feasibility, an available call route. This distinction between classification and action is the paper's center of gravity.

## Claims, evidence, and ceilings

| Part | Evidence currently in the manuscript | Claim allowed | Claim withheld |
|---|---|---|---|
| §1–2, Meyer → Martin | Explicit Martin 1996 citation of Meyer 1988, conditional sorting and shape cases | The cited texts reason about specified changes and interfaces | Continuous causal genealogy of all five SOLID rules |
| §2, reception | 1995 comp.lang.c++ debate; public SOLID circulation by 2007; 2009 internal-vs-public API controversy | Early and later debate documents conditional application | First use of SOLID; that the acronym itself removed context |
| §3–4, classification | 48 reference pairs, 768 saved responses, 24 distinct exact strings of code-masked prompts; zero textual matches with both sides of reference pairs | What the saved prompt artifacts and source comparison actually show | 768 independent codebases; model saw the distinct reference pair 37; absence of all contextual cues anywhere |
| §4, prior art | Bräuer 2018, Cabral 2024, Zhu 2026 read in the filed editions | Different instruments evaluate coverage, participant perceptions, functional/structural criteria | They tested an identical intervention or measured one OCP causal treatment |
| §5, fixed patch | Four declared demand × caller-contract combinations, all executable; disclosed-information grid | Same patch may warrant different acceptance verdicts in the authored fixture | Measured prevalence of erroneous human/AI rejections |
| §6, architectures | Add-shape vs add-operation; one batch requirement under two placement rules; optional bracketed rendering under different entrypoint/hook baselines | Existing-file edit counts of implemented candidates depend on requirement, placement and reachable entry path | Globally minimal edit count, maintainer effort, or effect of an existing hook without its initial cost |
| §7, hypothesis | Information sufficiency and worked example | A research program for change/contract/authority/path representations | New general law, mathematical axiomatization or LAW-R2 authorization |

## Reader sequence / directed transitions

1. A concrete OCP argument in Martin 1996 leads to a missing sorting obligation. The 'over-axiomatization' phrase is a risk with a specific definition, not a demonstrated universal episode.
2. The 1988/1995/1996/2007/2009 sources demonstrate citation, debate and circulation without constructing an invented inevitable narrative.
3. The archive methods (§3) precede classification findings (§4) to prevent source conflation. The 37th reference pair is not identified as a saved model input.
4. The catalogue case (§5) asks whether a **given patch** meets a **given specification**; it does not optimize an architecture.
5. The drawing cases (§6) ask how the candidate can be implemented and reached. Keep the two batch requirements distinct: the first handles lists and brackets each result; the third offers an opt-in option on single renders.
6. The ending states a falsifiable prospective program while explicitly retaining the evidence ceiling.

## Remaining line-edit and layout debt

- Relocate citation-link clusters from the ends of prose paragraphs into a structured bibliography or evidence appendix; keep their original URLs and precise locators.
- Develop the relation to Parnas's 1979 specification-dependency account and the expression problem without implying direct influence. This is important prior art to the proposed mathematical structure.
- Supply a consolidated bibliography, with source editions and DOI, and name the source-specific unit for each quantitative claim.
- Read the English text against the Korean argument in §2 and §4 after any citation or section relocation, not merely by matching words.
- Distinguish the three §6 interventions visually: changing demand; changing placement permissions; changing reachable entry path and baseline.
- Keep the main text's use of 'acceptance' as an authored study criterion, not a report about real-world merge decisions.
- Test any future comparative architecture prediction against independently authored requirements. No such test is documented in this editorial pass.
- No new experiments, source-file moves, or historical discoveries were claimed by the editing pass itself.

## Manuscript writing stance

Prefer concrete causal agents, actors and objects over parallel outlines. Avoid repeated 'first/next/finally' recitations after the introduction. Check the transition between every two paragraphs: the second paragraph should answer a question raised in the first, or make explicit why the subject changes. Do not add a hypothetical example to cover a missing source claim without marking it as hypothetical.

## Source notes

[1995 debate](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ) · [Martin 1996](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf) · [Bräuer 2018 DOI](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral 2024 DOI](https://doi.org/10.1145/3644815.3644957) · [Zhu 2026](https://arxiv.org/abs/2603.27745) · [Reproduction](./PAPER_B_REPRODUCTION.md) · [Acquisition ledger](./16_CURRENT_ACQUISITION_LIST.md).
