"""Equal-information ATLAS vs strong ADR+rationale-link finite *representation* court.

Both arms receive exactly the same explicit evidence, four context fields,
source IDs and decision/warrant links. Strong ADR is allowed rationale IDs,
reverse references and revision history. Outputs are *review flags*, NOT
engineering recommendations or verified contract satisfaction.

A tie demonstrates that the stated tasks alone cannot establish an ATLAS
advantage. No human times, real change impacts, or independent validation.
Run: python tools/principle_atlas_rival_court.py
"""
from dataclasses import dataclass
from itertools import combinations, product
import json

from principle_atlas_evidence import Evidence
from principle_atlas_epistemic import PartialContext, Scope, assess
from principle_atlas_transition import Warrant

FIELDS = ("demand", "contract", "policy", "objective")
VALUES = (None, "yes", "no")
KINDS = ("heuristic", "behavior_contract", "authorized_policy")


@dataclass(frozen=True)
class Decision:
    id: str
    warrants: tuple[str, ...]


class StrongADR:
    """Independent conventional evaluator; indexed rationale is allowed."""

    def __init__(self, warrants: tuple[Warrant, ...], decisions: tuple[Decision, ...]):
        names = {w.name for w in warrants}
        if len(names) != len(warrants):
            raise ValueError("duplicate rationale identifier")
        if len({d.id for d in decisions}) != len(decisions):
            raise ValueError("duplicate decision identifier")
        if any(len(set(d.warrants)) != len(d.warrants) or
               any(w not in names for w in d.warrants) for d in decisions):
            raise ValueError("broken or duplicated rationale link")
        self.warrants = {w.name: w for w in warrants}
        self.reverse_index = {name: frozenset(d.id for d in decisions
                                              if name in d.warrants)
                              for name in names}

    def status(self, name: str, context: PartialContext, evidence: Evidence):
        w = self.warrants[name]
        mismatch = False
        unknown = False
        for field, required in w.premises:
            actual = getattr(context, field)
            mismatch |= actual is not None and actual != required
            unknown |= actual is None
        scope = ("OUT_OF_SCOPE" if mismatch else
                 "UNDETERMINED_SCOPE" if unknown else "APPLICABLE")
        # The evaluator must not infer mandate, contract satisfaction or benefit.
        evidence_label = (("BOTH" if evidence.negative else "SUPPORT_ONLY")
                          if evidence.positive else
                          ("DEFEAT_ONLY" if evidence.negative else "NEITHER"))
        return (w.kind, scope, evidence_label)

    def affected(self, changed_fields: frozenset[str],
                 changed_evidence: frozenset[str]):
        selected = {name for name, w in self.warrants.items()
                    if name in changed_evidence or
                    any(field in changed_fields for field, _ in w.premises)}
        return frozenset().union(*(self.reverse_index[n] for n in selected))


def atlas_affected(warrants: tuple[Warrant, ...],
                   decisions: tuple[Decision, ...],
                   changed_fields: frozenset[str],
                   changed_evidence: frozenset[str]):
    """Reference ATLAS index; same permissions as the strong ADR baseline."""
    impacted = {w.name for w in warrants if w.name in changed_evidence or
                any(field in changed_fields for field, _ in w.premises)}
    return frozenset(d.id for d in decisions if impacted.intersection(d.warrants))


def test():
    # Every four-field partial context, every subset of required fields,
    # each normative label and all four evidence states: 15,552 comparisons.
    states = tuple(Evidence(*bits) for bits in product((False, True), repeat=2))
    comparisons = 0
    counts = {scope.value: 0 for scope in Scope}
    for size in range(5):
        for subset in combinations(FIELDS, size):
            premise = tuple((name, "yes") for name in subset)
            for kind in KINDS:
                warrant = Warrant("shared", kind, premise, frozenset({"declared_source"}))
                adr = StrongADR((warrant,), (Decision("D1", ("shared",)),))
                for values in product(VALUES, repeat=4):
                    ctx = PartialContext(*values)
                    for e in states:
                        expected = assess(warrant, ctx, e)
                        actual = adr.status("shared", ctx, e)
                        assert actual == (expected.kind, expected.scope.value,
                                          expected.evidence_status), (warrant, ctx, e)
                        counts[expected.scope.value] += 1
                        comparisons += 1
    assert comparisons == 16 * 3 * 81 * 4 == 15552

    # Cross-decision shared warrant and independent binding conditions.
    warrants = (
        Warrant("extension_payoff", "heuristic", (("demand", "yes"),),
                frozenset({"versioned_forecast"})),
        Warrant("preserve_http", "behavior_contract", (("contract", "yes"),),
                frozenset({"contract_definition"})),
        Warrant("team_extension_policy", "authorized_policy", (("policy", "yes"),),
                frozenset({"team_record"})),
        Warrant("cost_comparison", "heuristic", (("objective", "yes"),),
                frozenset({"cost_data"})),
    )
    decisions = (
        Decision("D1", ("extension_payoff", "preserve_http")),
        Decision("D2", ("extension_payoff", "team_extension_policy")),
        Decision("D3", ("cost_comparison",)),
    )
    adr = StrongADR(warrants, decisions)
    cases = (
        (frozenset({"demand"}), frozenset(), frozenset({"D1", "D2"})),
        (frozenset(), frozenset({"extension_payoff"}), frozenset({"D1", "D2"})),
        (frozenset({"contract"}), frozenset(), frozenset({"D1"})),
        (frozenset({"policy"}), frozenset(), frozenset({"D2"})),
        (frozenset({"objective"}), frozenset(), frozenset({"D3"})),
        (frozenset(), frozenset(), frozenset()),
    )
    for changes, evidence_changes, expected in cases:
        assert adr.affected(changes, evidence_changes) == expected
        assert atlas_affected(warrants, decisions, changes, evidence_changes) == expected

    # Strong-baseline fairness: known unknowns, opposite evidence, authority
    # and behavioral contract labels are preserved without automatic decisions.
    all_unknown = PartialContext(None, None, None, None)
    for w in warrants:
        for evidence in states:
            status = adr.status(w.name, all_unknown, evidence)
            assert status == (w.kind, "UNDETERMINED_SCOPE", evidence.status)
    assert adr.status("team_extension_policy", PartialContext(None, None, "yes", None),
                      Evidence(False, True)) == (
                          "authorized_policy", "APPLICABLE", "DEFEAT_ONLY")
    assert adr.status("preserve_http", PartialContext(None, "yes", None, None),
                      Evidence()) == ("behavior_contract", "APPLICABLE", "NEITHER")
    # No source identity may mean no record: fail closed on missing provenance.
    for invalid in (
        lambda: Warrant("no_source", "heuristic", (), frozenset()),
        lambda: StrongADR(warrants, (Decision("bad", ("missing",)),)),
        lambda: StrongADR(warrants, (Decision("bad", ("preserve_http", "preserve_http")),)),
        lambda: StrongADR(warrants, (Decision("same", ()), Decision("same", ()))),
    ):
        try:
            invalid()
        except ValueError:
            pass
        else:
            raise AssertionError("invalid record unexpectedly accepted")
    return {
        "finite_equal_information_comparisons": comparisons,
        "finite_scope_counts": counts,
        "matched_dependency_change_cases": len(cases),
        "matched_dependency_change_cases_passed": len(cases),
        "conclusion": "TIE_ON_DECLARED_REPRESENTATION_TASKS",
        "human_accuracy": "NOT_MEASURED",
        "reviewer_cost": "NOT_MEASURED",
        "source_contract_validation": "NOT_PERFORMED",
        "external_novelty": "NOT_ESTABLISHED",
    }


if __name__ == "__main__":
    print(json.dumps(test(), ensure_ascii=False, sort_keys=True))
