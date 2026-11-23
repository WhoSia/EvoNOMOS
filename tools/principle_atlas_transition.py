"""Context transitions for a *toy* typed-principle atlas.

This module classifies whether an explicitly stated premise matches a context
before and after a change. A matching premise is NOT proof of the recommendation. It does not infer causal design quality, validate real SOLID claims,
or replace existing contract/specification verification.
No third-party dependencies.
"""
from dataclasses import dataclass
from typing import FrozenSet, Mapping, Tuple


@dataclass(frozen=True)
class Context:
    demand: str
    contract: str
    policy: str
    objective: str


@dataclass(frozen=True)
class Warrant:
    name: str
    kind: str
    premises: Tuple[Tuple[str, str], ...]
    evidence: FrozenSet[str]

    def __post_init__(self):
        if self.kind not in {"heuristic", "behavior_contract", "authorized_policy"}:
            raise ValueError("unknown warrant kind")
        fields = {"demand", "contract", "policy", "objective"}
        if len({field for field, _ in self.premises}) != len(self.premises):
            raise ValueError("duplicate premise")
        if any(field not in fields for field, _ in self.premises):
            raise ValueError("unknown context field")
        if not self.evidence:
            raise ValueError("warrant must name its evidence source")


def applies(warrant: Warrant, context: Context) -> bool:
    return all(getattr(context, field) == value for field, value in warrant.premises)


@dataclass(frozen=True)
class Transition:
    kept: FrozenSet[str]
    withdrawn: FrozenSet[str]
    newly_applicable: FrozenSet[str]
    not_applicable_either: FrozenSet[str]


def compare(before: Context, after: Context,
            warrants: Tuple[Warrant, ...]) -> Transition:
    names = [w.name for w in warrants]
    if len(names) != len(set(names)):
        raise ValueError("duplicate warrant name")
    kept = set()
    withdrawn = set()
    newly = set()
    neither = set()
    for warrant in warrants:
        old = applies(warrant, before)
        new = applies(warrant, after)
        if old and new:
            kept.add(warrant.name)
        elif old:
            withdrawn.add(warrant.name)
        elif new:
            newly.add(warrant.name)
        else:
            neither.add(warrant.name)
    return Transition(frozenset(kept), frozenset(withdrawn),
                      frozenset(newly), frozenset(neither))


def tests() -> dict:
    before = Context(demand="many_variants", contract="same_http",
                     policy="no_requirement", objective="lifecycle_cost")
    after = Context(demand="no_extensions", contract="same_http",
                    policy="no_requirement", objective="lifecycle_cost")
    warrants = (
        Warrant("extension_payoff", "heuristic",
                (("demand", "many_variants"), ("objective", "lifecycle_cost")),
                frozenset({"toy_cost_assumption"})),
        Warrant("preserve_http", "behavior_contract",
                (("contract", "same_http"),), frozenset({"frozen_contract"})),
        Warrant("keep_simple", "heuristic",
                (("demand", "no_extensions"),), frozenset({"changed_plan"})),
        Warrant("explicit_team_rule", "authorized_policy",
                (("policy", "require_extension_seam"),),
                frozenset({"team_policy_document"})),
    )
    result = compare(before, after, warrants)
    assert result.kept == {"preserve_http"}
    assert result.withdrawn == {"extension_payoff"}
    assert result.newly_applicable == {"keep_simple"}
    assert result.not_applicable_either == {"explicit_team_rule"}
    assert compare(before, before, warrants).withdrawn == set()
    assert compare(before, before, warrants).newly_applicable == set()
    assert compare(before, before, warrants).kept == {"extension_payoff", "preserve_http"}
    assert compare(after, before, warrants).newly_applicable == {"extension_payoff"}
    objective_only = Context(demand="many_variants", contract="same_http",
                             policy="no_requirement", objective="initial_cost")
    assert compare(before, objective_only, warrants).withdrawn == {"extension_payoff"}
    policy_change = Context(demand="many_variants", contract="same_http",
                            policy="require_extension_seam",
                            objective="lifecycle_cost")
    assert compare(before, policy_change, warrants).newly_applicable == {
        "explicit_team_rule"
    }
    contract_change = Context(demand="many_variants", contract="changed_http",
                              policy="no_requirement", objective="lifecycle_cost")
    assert compare(before, contract_change, warrants).withdrawn == {"preserve_http"}
    for bad in [
        lambda: Warrant("invalid", "untyped", (), frozenset({"source"})),
        lambda: Warrant("no_src", "heuristic", (), frozenset()),
        lambda: Warrant("dup", "heuristic",
                        (("demand", "a"), ("demand", "b")), frozenset({"source"})),
        lambda: Warrant("unknown", "heuristic",
                        (("foo", "bar"),), frozenset({"source"})),
        lambda: compare(before, after, (warrants[0], warrants[0])),
    ]:
        try:
            bad()
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input was accepted")
    return {"cases": 10, "transition": result}


if __name__ == "__main__":
    print(tests())
