# Paper B R13 — Paradigm Transfer Without a Second Thesis
**2026-11-22 · analytic note · no new native-Go experiment / no agent observations**

## Question raised in the discussion
If an application is refactored globally in Go using function values, callbacks, closures and small interfaces, how should its design quality be compared with a class-based Java/C# implementation? Is 'OCP violation' as a syntactic label transportable across these idioms?

## Source-corrected premises
- [Go specification](https://go.dev/ref/spec) permits functions as values, function types, closures, methods attached to non-interface types, interface method sets, multiple return values and `defer`. These features do not classify Go as a *pure functional language*. [Official Go FAQ](https://go.dev/doc/faq) explicitly discusses object-oriented programming in Go despite the absence of classes/type hierarchies.
- Java/C# are not exclusively class-subtyping languages, and Go is not exclusively callback-based. Each supports several composition styles; a contrast between **particular architectures** should not be mistaken for a randomized contrast between paradigms or languages.
- The presence of `defer` or multiple-value return is not direct evidence about FP, architectural maintainability or SOLID validity. C# supports tuple returns/deconstruction ([Microsoft C# tuples](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/tuples)); C++ supports tuple-return/structured binding ([Microsoft C++ functions](https://learn.microsoft.com/en-us/cpp/cpp/functions-cpp?view=msvc-170)).

## Formal identification problem
Define a comparison unit as `(source, clients, requirement sequence, edit rights, full observation set, change budget)`. Suppose `A` is a design where a named dispatch interface accepts an extension and `B` a design where function-valued callback parameters select behavior. Both can accept a new handler with **zero changes to an existing dispatch function**. In that admissible pair, syntactic OOP/FP status does not determine protected-client behavior or required edits.

The stronger observation is conditional:
- If requirement `d` merely supplies a new handler, both architectures may be open to the requested extension.
- If `d` requires changing the callback protocol, a callback-based design may require updating many callers.
- If `d` adds a new capability outside the existing interface, interface implementations may need coordinated edits; a class-based design can also be affected.
- For either architecture, source-visible opportunities and permitted repairs depend on the pinned project state and client contract, not language branding.

This is a **conceptual possibility claim** with familiar classical explanations (parametricity, modularity, interface/functional composition), not an observed comparison of repair costs and not a new theorem. It makes the following inference invalid:

`(uses-classes(s) or uses-callbacks(s)) -> uniquely determined OCP-patch disposition`.

## Three candidate explanations for a reviewer refusing a function-composition patch
1. A legitimate task-specific requirement explicitly mandates an interface / stable extension point; refusal can be warranted.
2. Reviewer preferences are conditioned by familiar OOP vocabulary; the label may affect explanation but not source acceptance.
3. Reviewer erroneously treats 'all functionality should be open by class extension' as an unconditional norm, overriding a source-backed acceptable callback implementation.

The evidence to distinguish (2) from (3) is **actual patch disposition with equal contract information**, not token frequency. Distinguishing (1) from (3) requires source-backed authority and instruction-precedence review. All these interpretations remain open in the absence of real agent observations.

## Manuscript ruling
**Do not introduce a new section called 'OOP vs FP' into Paper B.** Add a short paragraph at the end of the Section 3 proposal, as a *possible arena of application*, with an explicit Go-is-not-pure-FP caveat. This demonstrates why the intended question is about operational authority rather than a class-based style war. Place broad performance/repair-cost comparison into Paper C/F38. Preserve PAPER B v24; a v25 editorial revision may fold this one paragraph into both languages.

## Falsifier/negative control
If equal-information reviewers approve source-equivalent callback and interface candidates and justify their decisions with the same protected-client constraints, there is no evidence of a class-centric authority problem in those cases. If they diverge, investigate task/caller/rights differences before claiming doctrinal influence.

**Outcome:** theoretical counterexample pattern and writing constraint only; no new Go source pair was executed and no behavior rate was measured. `PAPER B v24 / AGENT PRE-RUN / F38 OPEN / LAW-R2 HOLD`.
