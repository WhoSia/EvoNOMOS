# Paper B / Claude independent review adjudication and archive audit (2026-11-21)

## Status, decision, and limits

**Recommendation, not an authorized rewrite of the existing manuscript:** adopt a focused Plan B-prime for the next separately versioned draft. Keep the *reason-giving conditions for a patch rejection* in Paper B; move operation-by-shape placement, existing-file edit counts, and the existing Figure 1 / Table 3 to a preserved Paper C research appendix. Retain one short *reachable entrypoint* counterexample in B, because a requirement to support the original calling path is part of patch acceptance, not a general claim that one layout is better.

The source manuscript [Notion 12](https://app.notion.com/p/41bef561cf9281e1864afb74a3bbb4ce), the [Claude referee report](https://app.notion.com/p/41fef561cf92818d9ebdde67fffe0799), and the [Claude B-prime proposal](https://app.notion.com/p/41fef561cf9281108fc2da223d1394ab) remain untouched. This record adjudicates the proposal and independently reads the pinned archived ZIP.

## Archive acquisition and immutable identifier

Drive source: [AreWeSOLID.zip](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view).
SHA-256 computed from its raw bytes in the working container:
`d2cfbe50dd12d189c0ee2b561a842757fa7483251df9025b602c498b753f0353`.
This matches `are_we_solid_inventory.json`. The archive was inspected read-only through Python `zipfile`; archive members were not executed or extracted.

### Independent recount of OCP records

- OCP reference pairs: **48** (two sides each).
- Saved `output_test.jsonl` files: **16**, with **48 rows each** = **768 records**.
- Unique submitted code strings: **48**; each code string occurs **16 times** (4 models × 4 strategies).
- Unique prompt scaffolds after exact replacement of the submitted code: **24**.
- **64** (strategy, language, model) triples. Within each triple, all **12** submitted code snippets have an identical masked scaffold. This is the exact stratification needed to make an invariance claim.
- The 24 scaffolds are **not** a function of strategy and language alone. For DEFAULT and SMELL there is 1 scaffold per language (4 each); for ENSEMBLE and EXAMPLE there are 2 per language (8 each): `gpt-4o-mini` uses a distinct scaffold from the three other saved models. Counts are 4/8/8/4 by strategy.
- Within every scaffold there are **12 distinct code strings**; thus each scaffold is reused across programs. No scaffolds overlap across strategies.

The precise statement is: **conditional on model, strategy and language, the masked instruction text is invariant across the 12 code examples that were submitted to that combination.** The observed absence of a separately supplied per-case maintenance demand or protected contract in the masked instruction is a separate interpretive finding. *Do not claim the model had no contextual information*: the source itself can convey names, comments, invariants and behavior; the model can infer possible obligations.

### Source comments/docstrings and reference alignment

- Code comments detected in **208/768 saved rows**, representing **13/48 distinct submitted codes**. This count includes possible lexical false positives in C-like code (e.g. comment syntax inside regex/string literals). Python docstring extraction found **0** records. No scanned comment/docstring contained the specific audit keywords `requirement|requires|must|should|preserve|backward|compatib|client|contract|maintain|support|request|TODO` as standalone words. This **does not establish** absence of implied requirements or broader natural-language meaning.
- Submitted code vs either side of all 48 reference pairs: **0/768** matches for raw text, trimmed ends, all-whitespace-stripped, or per-line trimming/deleting blank lines.
- Python only: 24 reference-side Python sources parsed and all 192 Python submitted-row sources parsed. **0/192** saved Python rows matched any reference-side Python source under `ast.dump(ast.parse(...),include_attributes=False)`. The AST comparison is more formatting-insensitive but does **not** prove semantic non-equivalence, provenance independence, or absence of common concepts.
- Conclusion: the saved submissions and the reference examples are **not textually or Python-AST identical under the tested normalizations**. Do not infer that reference pair 37 was presented to a model, or that no saved response relates conceptually to that reference example.

## What to accept / revise from Claude's review

1. **Accept** the caution about criterion circularity. The 2×2 truth table follows the authored acceptance criterion and authored demand/contract grid. The execution establishes the candidate's observations. The contribution is a *reproducible witness and explicit review protocol*, not an observed empirical approval reversal.
2. **Accept** the focus on partial disclosure, but avoid novelty inflation: unanimity over a set of compatible specifications is elementary logic. Potential novelty lies in the OCP label-to-acceptance distinction, an evidence-backed map of obligations, and a reproducible way to articulate the next **decision-relevant question**.
3. **Accept** the term *over-axiomatization* only as a **named risk in applying** conditional design advice to a patch verdict without sufficient premises, not as proven historical causal drift or measured reviewer behavior.
4. **Accept with qualification** splitting §6. Reachability through an existing entry point is a legitimate contract/demand observation in Paper B; edit-count architecture comparison is not the same estimand and belongs in Paper C. No changes to existing Paper B or Paper C files were made here.
5. **Qualify** Claude's proposed benchmark claim. The observed 24 templates vary also with the model. Only after conditioning on (strategy, language, model) do we see a constant masked scaffold across cases. The archival 768 rows are repeated inputs, not 768 independent cases.
6. **Qualify** Claude's actual-repo example proposal. The CPython `assertNoLogs` change is a promising trace from an external feature request to an independently documented existing API contract, *if original commits and docs are verified*. A deliberately modified counterfactual version is not a real flawed merged patch and cannot be described as one.
7. **Reject** any unconditional claim of paper novelty against Design by Contract, requirements engineering, behavioral subtyping, oracle adequacy or epistemic uncertainty before comparing those literatures. The manuscript should articulate *the gap in what a design-principle label licenses as an action*, not claim to have invented contract checking.

## Versioned writing decision

Suggested compact manuscript:
- Abstract: one concrete question, short definition of over-axiomatization, one benchmark input fact, one finite-witness result, review-protocol implication. No code-layout counts.
- §1: Martin's sorting example → caller obligation → risk of unconditional verdict.
- §2: Meyer 1988/ Martin 1996 historical context and existing competing concepts. Historical causality deliberately left open.
- §3: archive units, mask/exact grouping by (model, strategy, language), submission/reference alignment limits; fixed-patch inputs, protected observations, acceptance rule, partial disclosure protocol.
- §4: archive observations and appropriate limits on the label's intended use.
- §5: the executable fixed-patch witness and its 2×2 / partial disclosure table; optionally a verified CPython trace, clearly marked as supporting provenance rather than evidence of historical rejection.
- §6: Discussion, consequences for evidence-based review and one existing-entrypoint counterexample; reserve implementation-placement comparisons for Paper C.
- §7: conclusion and one falsifiable question about finding actual obligations from issues, docs, clients and tests.

### Priority gates before writing a claimed new result

P0 completed: raw archive SHA check, grouping and model effect, extended formatting and Python AST comparison, rough comment/docstring scan.

P1: confirm CPython version-pinned source change/commit, issue and pre-change documentation; distinguish actually merged behavior from authored counterfactual.

P2: source-critical literature: requirements/contract theory and how label classification claims differ from an action justification. Avoid misrepresenting Pehlivan's classification task as a patch-decision benchmark.

P3: independently authored change requests and blinded reviewer questions; only then consider frequency or reviewer-performance claims.

**No new real-world reviewer experiment, true source lineage between saved and reference code, or generalized causal law is claimed here.**
