"""Finite regression court for the contextual-principle ATLAS toy semantics.

Only checks declared premise scope, evidence orthogonality, and typed labels.
It does NOT validate contracts against code, authorize policies, assess design
quality, benchmark ADRs, or claim a novel theorem. Standard library only.
Run: python tools/principle_atlas_regression.py
"""
from itertools import combinations, product

from principle_atlas_evidence import Evidence
from principle_atlas_epistemic import PartialContext, Scope, assess, scope_of
from principle_atlas_transition import Warrant

FIELDS = ("demand", "contract", "policy", "objective")
KINDS = ("heuristic", "behavior_contract", "authorized_policy")


def independent_oracle(premises, values):
    """Closed-form finite truth table, independent of the implementation loop."""
    observed = tuple(values[FIELDS.index(field)] for field, _ in premises)
    if "no" in observed:
        return Scope.OUT_OF_SCOPE
    if None in observed:
        return Scope.UNDETERMINED_SCOPE
    return Scope.APPLICABLE


def check():
    evidence = tuple(Evidence(*bits) for bits in product((False, True), repeat=2))
    cases = 0
    status_counts = {scope.value: 0 for scope in Scope}
    for number in range(len(FIELDS) + 1):
        for subset in combinations(FIELDS, number):
            premises = tuple((field, "yes") for field in subset)
            for values in product((None, "yes", "no"), repeat=4):
                context = PartialContext(*values)
                expected = independent_oracle(premises, values)
                for proof in evidence:
                    warrant = Warrant("candidate", "heuristic", premises,
                                      frozenset({"declared_example"}))
                    result = assess(warrant, context, proof)
                    assert result.scope == expected
                    assert scope_of(warrant, context) == expected
                    assert result.evidence_status == proof.status
                    assert result.kind == "heuristic"
                    status_counts[expected.value] += 1
                    cases += 1
    assert cases == 5184
    # A policy's authority or a contract's satisfaction is NOT inferred
    # from the presence of pro evidence or the status APPLICABLE.
    context = PartialContext("yes", None, None, None)
    typed_cases = 0
    for kind, proof in product(KINDS, evidence):
        warrant = Warrant("candidate", kind, (("demand", "yes"),),
                          frozenset({"unverified_claim"}))
        value = assess(warrant, context, proof)
        assert (value.kind, value.scope, value.evidence_status) == (
            kind, Scope.APPLICABLE, proof.status)
        typed_cases += 1
    assert typed_cases == 12
    # Information gain (positive -> both) does not authorize FAVOUR.
    same = Warrant("change", "heuristic", (("demand", "yes"),),
                   frozenset({"unverified_claim"}))
    before = assess(same, context, Evidence(True, False))
    after = assess(same, context, Evidence(True, True))
    assert before.scope == after.scope == Scope.APPLICABLE
    assert before.evidence_status == "SUPPORT_ONLY"
    assert after.evidence_status == "BOTH"
    # An unassessed premise differs from a tested and failed premise.
    assert scope_of(same, PartialContext(None, None, None, None)) == Scope.UNDETERMINED_SCOPE
    assert scope_of(same, PartialContext("no", None, None, None)) == Scope.OUT_OF_SCOPE
    # The initial *binary* matcher cannot safely be used on partial contexts.
    return {"scope_evidence_cases": cases, "typed_cases": typed_cases,
            "scope_counts": status_counts, "verdict": "PASS_TOY_FINITE_ORACLE",
            "empirical_design_advantage": "NOT_TESTED",
            "external_ADR_comparison": "NOT_TESTED"}


if __name__ == "__main__":
    print(check())
