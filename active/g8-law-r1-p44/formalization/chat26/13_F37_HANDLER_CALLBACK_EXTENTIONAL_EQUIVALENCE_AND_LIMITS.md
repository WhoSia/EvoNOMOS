# Chat 26 — F37 Interface/Callback Equivalence: What Can and Cannot Differ

**Based on actual pinned Go files:** f37arms/handlerarm/handlerarm.go and f37arms/callbackarm/callbackarm.go at P44-F37, maintained in separate research-authored packages. Their own source uses the same original chi v5.1.0 and httprouter v1.3.0, with the same initial routes and header selection, but different application-owned dispatch tables.

## 1. Conditional extensional equivalence (classical Go semantics)

Let H be a *non-nil* http.Handler. Define the function F(H) := H.ServeHTTP. For a non-nil function f of type func(http.ResponseWriter, *http.Request), define the handler G(f) := http.HandlerFunc(f). Then for any fixed request r and any initial ResponseWriter w, provided that invocation terminates and no extra metadata/identity inspections intervene,

G(F(H)).ServeHTTP(w,r) invokes H.ServeHTTP(w,r), and F(G(f))(w,r) invokes f(w,r).

These wrappers are *extensionally* equivalent on the same HTTP call inputs and observable writer effects, given an agreed execution/interference model. They are **not** equal as Go values, static or dynamic types, source layouts, mutation rights, method sets or resource costs.

Consequently, an interface map and a callback map that both route each kind to the same underlying handler can implement the same HTTP-level dispatch. In F37, the two programs instantiate independent but equivalent route registration logic, so the result establishes only finite observed equality at the sealed test matrix; it is not a proof of whole-source equivalence.

## 2. Conditions that break a stronger equivalence

- Dynamic interface-method inspection, e.g. the app reads whether the selected handler implements an additional interface; wrapping with HandlerFunc erases that dynamic interface metadata. Equivalent HTTP response is insufficient to preserve this observation.
- Nilness and initialization: a nil func held as HandlerFunc is a non-nil interface but panics if called. Interfaces also distinguish nil pointer in non-nil interface from nil interface.
- Mutable captured variables: closures or interface concrete values can capture and later read the same mutable map, so initial parity does not establish temporal equivalence under mutation.
- Actor edit permissions and source location: one edit may be feasible within an owned file while another needs a forbidden upstream modification or multiple app files.
- Resource metrics: heap allocation, wrapper overhead and source-change labor do not follow from HTTP extensional equivalence; only direct measurements and explicit cost models can compare these.

## 3. F38 scientific discriminator gate

A prospective task that merely adds an ordinary GET endpoint to both otherwise independent applications is unlikely to expose a fundamental difference of representational power, because both can adapt any non-nil handler to a callback and vice versa. It may still expose differing edit *cost*, but one must not preselect a task only because it favors a chosen arm.

Any alleged architectural advantage requires evidence under the actual target:
1. task is independently sourced and selection criteria are frozen;
2. old/new observer family is declared, including dynamic metadata or temporal behavior where relevant;
3. edit rights and comparable source modification power are fixed;
4. conventional adapter, function-table and source-aware competitors are given equal information;
5. predicted outcome or measured cost differs and resists matched classical explanation.

This makes a classical TIE a *positive methodological correction*, not a failed study.

## 4. Claim ceiling

The wrapper lemma is standard Go functional forwarding, not new theory; the exact real Go source is not proved contextually equivalent under every environment; original F37 CI tests only its named probes, and no F38 independent repair has yet been run. This note **does not** modify the frozen F37 source or claim LAW-R2.
