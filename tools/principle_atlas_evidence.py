"""Toy counterexample suite: premise applicability is not evidential support.

The four evidence states are already standard (Belnap-Dunn); this is not a
novel logic, a source-code semantics, or a validation of design guidelines.
"""
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Evidence:
    positive: bool = False
    negative: bool = False

    @property
    def status(self):
        return {
            (False, False): "NEITHER",
            (True, False): "SUPPORT_ONLY",
            (False, True): "DEFEAT_ONLY",
            (True, True): "BOTH",
        }[(self.positive, self.negative)]

    def accumulate(self, other: "Evidence") -> "Evidence":
        return Evidence(self.positive or other.positive,
                        self.negative or other.negative)


def recommendation(premises_match: bool, evidence: Evidence) -> str:
    """Illustrative conservative policy, not an engineering quality rule."""
    if not premises_match:
        return "OUT_OF_SCOPE"
    return {
        "NEITHER": "ABSTAIN",
        "SUPPORT_ONLY": "FAVOUR",
        "DEFEAT_ONLY": "OPPOSE",
        "BOTH": "CONFLICT",
    }[evidence.status]


def test() -> dict:
    states = [Evidence(*p) for p in product((False, True), repeat=2)]
    assert {s.status for s in states} == {
        "NEITHER", "SUPPORT_ONLY", "DEFEAT_ONLY", "BOTH"
    }
    for a, b, c in product(states, repeat=3):
        assert a.accumulate(b) == b.accumulate(a)
        assert a.accumulate(a) == a
        assert a.accumulate(b.accumulate(c)) == a.accumulate(b).accumulate(c)
        assert (not a.positive or a.accumulate(b).positive)
        assert (not a.negative or a.accumulate(b).negative)
    base = Evidence(positive=True)
    new = base.accumulate(Evidence(negative=True))
    assert base.status == "SUPPORT_ONLY"
    assert new.status == "BOTH"
    assert recommendation(True, base) == "FAVOUR"
    assert recommendation(True, new) == "CONFLICT"
    assert recommendation(False, base) == "OUT_OF_SCOPE"
    assert recommendation(True, Evidence()) == "ABSTAIN"
    assert recommendation(True, Evidence(negative=True)) == "OPPOSE"
    return {"triple_cases": len(states) ** 3,
            "information_monotone": True,
            "recommendation_not_monotone": True,
            "unknown_distinct_from_out_of_scope": True}


if __name__ == "__main__":
    print(test())
