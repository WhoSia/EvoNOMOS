"""Three-valued premise scope crossed with four-valued evidence.

This is an intentionally small reference checker. It makes no claim about
engineering optimality, real behavioral contract satisfaction, or novelty.
A missing context field is unknown, NOT a known mismatch.
"""
from dataclasses import dataclass
from enum import Enum
from itertools import product

from principle_atlas_transition import Warrant
from principle_atlas_evidence import Evidence


class Scope(str, Enum):
    APPLICABLE = "APPLICABLE"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    UNDETERMINED_SCOPE = "UNDETERMINED_SCOPE"


@dataclass(frozen=True)
class PartialContext:
    demand: str | None
    contract: str | None
    policy: str | None
    objective: str | None


@dataclass(frozen=True)
class Assessment:
    kind: str
    scope: Scope
    evidence_status: str


def scope_of(warrant: Warrant, context: PartialContext) -> Scope:
    """Conjunction: known-false dominates unknown; all true means applicable."""
    unknown = False
    for field, required in warrant.premises:
        actual = getattr(context, field)
        if actual is None:
            unknown = True
        elif actual != required:
            return Scope.OUT_OF_SCOPE
    return Scope.UNDETERMINED_SCOPE if unknown else Scope.APPLICABLE


def assess(warrant: Warrant, context: PartialContext,
           evidence: Evidence) -> Assessment:
    """Keep normative kind, applicability, and evidence independent.

    FAVOUR is intentionally not returned here: positive evidence alone
    cannot imply that a policy is authorized or a contract is satisfied.
    """
    return Assessment(warrant.kind, scope_of(warrant, context),
                      evidence.status)


def test() -> dict:
    w = Warrant("extension_payoff", "heuristic",
                (("demand", "many"), ("objective", "lifecycle")),
                frozenset({"toy_source"}))
    policy = Warrant("local_rule", "authorized_policy",
                     (("policy", "approved"),),
                     frozenset({"policy_document"}))
    contract = Warrant("preserve", "behavior_contract",
                       (("contract", "same_http"),),
                       frozenset({"contract_definition"}))
    options = (None, "many", "no_extensions")
    objective_options = (None, "lifecycle", "initial")
    evidence_states = [Evidence(*x) for x in product((False, True), repeat=2)]
    checked = 0
    for demand, objective, ev in product(options, objective_options,
                                          evidence_states):
        c = PartialContext(demand, "same_http", "approved", objective)
        scope = scope_of(w, c)
        if demand == "no_extensions" or objective == "initial":
            assert scope is Scope.OUT_OF_SCOPE
        elif demand is None or objective is None:
            assert scope is Scope.UNDETERMINED_SCOPE
        else:
            assert scope is Scope.APPLICABLE
        a = assess(w, c, ev)
        assert a.kind == "heuristic"
        assert a.scope == scope
        assert a.evidence_status == ev.status
        assert assess(policy, c, ev).scope is Scope.APPLICABLE
        assert assess(contract, c, ev).scope is Scope.APPLICABLE
        checked += 1

    # This is the precise failing case for the earlier binary matcher:
    # unknown demand is not the same as a known lack of demand.
    unknown = PartialContext(None, "same_http", "approved", "lifecycle")
    absent = PartialContext("no_extensions", "same_http", "approved", "lifecycle")
    assert scope_of(w, unknown) is Scope.UNDETERMINED_SCOPE
    assert scope_of(w, absent) is Scope.OUT_OF_SCOPE

    # Evidence accumulation can create a conflict without changing scope.
    original = assess(w, PartialContext("many", None, None, "lifecycle"),
                      Evidence(True, False))
    changed = assess(w, PartialContext("many", None, None, "lifecycle"),
                     Evidence(True, True))
    assert original.scope is changed.scope is Scope.APPLICABLE
    assert original.evidence_status == "SUPPORT_ONLY"
    assert changed.evidence_status == "BOTH"

    # A premise-free warrant matches all contexts, but has not been proven.
    trivial = Warrant("unconditional", "heuristic", (),
                      frozenset({"a_claim"}))
    assert scope_of(trivial, PartialContext(None, None, None, None)) is Scope.APPLICABLE
    assert assess(trivial, PartialContext(None, None, None, None),
                  Evidence()).evidence_status == "NEITHER"
    return {"exhaustive_scope_evidence_combinations": checked,
            "unknown_vs_false_distinguished": True,
            "evidence_separated_from_authority": True}


if __name__ == "__main__":
    print(test())
