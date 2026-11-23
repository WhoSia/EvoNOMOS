# Paper B v17 — Primary-Source / Claim Pre-Edit Seal (2026-11-21)

**BEFORE v17 manuscript source creation.** Preserve v16 byte-for-byte; create v17 as a new file and keep 7 Korean + 7 English sections and Appendix A.

## Verified source anchors

- v16 source: `PAPER_B_BILINGUAL_INTEGRATED_16_20261121.md` (blob SHA `a78a05ffbee3c8a7f7d1eff407a2ac5b8394029c`); based on archived OCP submissions 768 saved records / 48 distinct submitted codes / 24 scaffolds / 64 model-strategy-language cells. Do not reinterpret the records as independently reviewed patches.
- Jin & Chen (2026), *Are LLMs Reliable Code Reviewers? Systematic Overcorrection in Requirement Conformance Judgement*, held arXiv:2603.00539v1 PDF [Drive](https://drive.google.com/file/d/1fWCLu97RGa1TvRt0RxuziolpRSh8rLW4/view). Directly read abstract and Introduction: natural-language requirement conformity judged on canonical and buggy solutions across three benchmarks, three prompt modes and five models; false rejection of correct code and mitigation by fix-guided verification. **Not** a demonstration that OCP label in Pehlivan triggers an industry patch rejection.
- Widyasari, Zhang, Bouraffa, Maalej & Lo (2025), *Explaining Explanations*, TOSEM 34(6), Article 177, [DOI](https://doi.org/10.1145/3708518), [held original PDF](https://drive.google.com/file/d/1POjBSQkxLKYmTXPzb4Z6wYBpjJgItIQA/view). Direct abstract: 793 manually coded Gerrit review comments; 42% suggestion-only; seven explanation types including rule/principle. ChatGPT type-specified explanation judged correct for 88/90 examples. **Explanation presence is not a certificate of correct patch rejection.**
- Papotti, Paramitha & Massacci (2024), *On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools*, ESE 29:132, [DOI](https://doi.org/10.1007/s10664-024-10506-z), [held original PDF](https://drive.google.com/file/d/1Fmrm1uQIOTgevCYo6rQrkqaiaANpEvE4/view). Direct abstract: 72 Master students; APR security patch accept/reject experiments, tool-origin cue alters decisions. **Different sample and setting from Paper B authored 2x2.**
- Ling, Zou & Liu (2026), *Negotiating Completion in Agentic Software Work*, Systems 14:1312 [DOI](https://doi.org/10.3390/systems14101312), [held PDF](https://drive.google.com/file/d/10IrIflqxO0BtWAOJ3cEutu3glU2CogwN/view). Direct abstract: qualitative 30 diagnostic PRs from 22 repos in a larger 1782-contribution frame; completed/merged/requirements satisfied are distinct. This *empirically challenges any claim that Paper B first identified conditional acceptance*.

## Requested edits and strict boundaries

1. Strengthen §4 interpretation: insert a named direct rival comparison anchored in primary sources; classification, human review explanation, measured reviewer adoption and LLM conformance must remain four different dependent variables.
2. Strengthen §5: two minimal rejection certificates, one joint acceptance certificate, explicit ambiguous-world witness, nonempty admissible set, source provenance of requirements. Record Chat26 CI only as bounded Boolean/exact enumeration.
3. Strengthen §6/§7 bridge without claiming historical OCP misuse prevalence or architectural cost measurements.
4. Improve abstract's relation to “over-axiomatization” with **one** compact conceptual claim, not inflated results.
5. Correct v16 Appendix A's stale “14판” reference and keep 12th v figures fully preserved.
6. Cite source read scope; text/abstract/intro reading ≠ every table/appendix reverified.
7. New bilingual v17, comparison note, version audit and separately recorded actual CI success. No overwriting past Notion manuscript pages.
