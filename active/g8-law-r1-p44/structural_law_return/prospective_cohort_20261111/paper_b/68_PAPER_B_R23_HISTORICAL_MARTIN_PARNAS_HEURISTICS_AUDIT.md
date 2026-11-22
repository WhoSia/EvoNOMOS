# Paper B R23 — Historical Reassessment: The Original Sources Already Limited the Rules
**2026-11-23 · newly inspected public sources and inherited local source notes · no new experiment.**

## Source custody and verification level

1. **Meyer 1988, Object-Oriented Software Construction, first edition**, primary passage originally recovered in project file [13](13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) from pp.22–25 of a **partial repaired PDF**, not the complete book. Passage account: closure via stable client-facing description and extension via types, with library case. We did not newly inspect the actual full first edition in this iteration.
2. **D. L. Parnas 1972**, "On the Criteria To Be Used in Decomposing Systems into Modules," CACM, DOI [10.1145/361598.361623](https://doi.org/10.1145/361598.361623), present in author/publisher and mirrored material. Important prior concept: modularization should follow *difficult decisions and decisions likely to change*, not a mechanical execution flow. The central context-aware design insight predates SOLID.
3. **D. L. Parnas 1979**, "Designing Software for Ease of Extension and Contraction," IEEE TSE 5(2), pp.128–138, primary reproduction [MIT course source PDF](https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/1c68d0f98909a126ec5eb6a0ff358ec7_parnas_ease.pdf). Direct text and first-page visual screenshot examined in this iteration. Parnas discusses programs as **families**, and differing user requirements / input-output formats / changes to modular relations. Extension is not solely "add a derived class"; contraction and variation also motivate the design. This adds a strong *rival classical antecedent* rather than supporting claims of our discovery.
4. **R. C. Martin 1996**, "The Open-Closed Principle," first Engineering Notebook for The C++ Report, [public faculty-hosted PDF](https://www.cs.utexas.edu/~fares/papers/OCP.pdf) plus secondary PDF reproduction [collected source](https://dan.socaciu.com/wp-content/uploads/2018/02/Martin_Paper_Software_Principles.pdf), textual pages internally numbered 6–13 inspected. The university-hosted PDF screenshot endpoint failed but direct PDF text lines were retrieved; original public PDF reproduction and figures' textual content consulted. Martin explicitly writes that no significant program is 100% closed; the developer chooses closure **for expected probable changes**. More distinctive: when discussing public member variables, he differentiates **bad style** from **bad design** depending on whether closure is violated (p.11–12); for RTTI he shows a counterexample where `dynamic_cast` is safe under OCP (p.12–13). His original account itself opposes treating every slogan-like prohibition as unconditional. DO NOT claim Robert Martin flatly rejected all such rules or argued OCP never binds. Full source contains emphatic strong OCP language, too.
5. **GoF 1994**, Erich Gamma et al., *Design Patterns: Elements of Reusable Object-Oriented Software*, [publisher listing](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610), originally published October 31 1994 and enumerates 23 patterns. The catalog precedes the later SOLID mnemonic; overlapping practices do not mean that GoF "was derived from the five SOLID axioms." Not core to a short B, but keep historical chronology correct.

## Why the new source detail matters

**V28's sentence** "Meyer's original open–closed account and Martin's strategic closure both involve stable client obligations and anticipated kinds of change" is directionally correct, but *unusually weak* compared to the source. A stronger historically grounded contrast is that in Martin's **own** 1996 discussion, several apparently absolute bans are later assessed as context-dependent heuristics. This is the direct historical counterweight to a straw-man theory that "the SOLID authors always told us to follow five inviolable axioms."

This does **not** establish historical transmission (that prompt rules are a causal descendant of 1996 statements). We can ask whether the *qualifiers* are retained in contemporary guidance, rather than assert they have disappeared from it.

## Publisher/source-grounded passage claims (paraphrased, not extensive verbatim quotes)
- Martin's section **Strategic Closure**, p.6 of his original article: complete closure unattainable; prioritize change classes based on their likelihood.
- Martin's **Heuristics and Conventions**, pp.11–13: public state, globals and RTTI conventions have exceptions, with explicit OCP arguments.
- Parnas 1972: select module boundaries by hidden likely-to-change design decisions.
- Parnas 1979: a product *family* and the possibility of adding/removing optional capabilities matter to extensibility and cost; "family" concept is not an AI-epoch invention.
- Meyer first edition is only passage-reviewed: the library witness reused in Paper B is **modified author research** (errata and book prefix) and not literal Meyer text.

## How much of this belongs in the short position paper?
One or two sentences only, e.g.:
> Martin himself did not treat every design prohibition as absolute: his 1996 account distinguished strategic closure from universal closure and even separated a practice's poor style from its actual design consequences.

Parnas family-of-programs is an excellent **citation and counter-tradition**, but a long digression would bury the agent study. Historicity earns its space only if it sharpens the one question: "why should a named principle override a code-grounded obligation?"

## Honest new result
We **did** perform new web-primary-source inspection and found a stronger original-source claim about *style versus design*; **we did not** perform a complete systematic history of SOLID's public uptake, and we have **no source-supported causal statement** that today's AI agents trained on a simplified slogan. Historical evidence supports the **conceptual possibility and need for qualified judgment**, not agent error prevalence.
