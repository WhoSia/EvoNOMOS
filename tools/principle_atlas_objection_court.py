"""R72 adversarial review court: explicit limits of typed design rationale.

This is a finite *specification test*, not a new logic, design-quality oracle,
or an empirical advantage over ADR/AREL/defeater-based systems.

Separate forecast revision (not boolean mismatch), behavioral contract status,
policy authority/expiry, and attack targets. An undermining attack on a datum
must not silently invalidate the inference rule or negate a contract. An
unresolved claim-level rebuttal must not be auto-resolved by majority vote.

Run: python tools/principle_atlas_objection_court.py
"""
from dataclasses import dataclass
from enum import Enum
from itertools import product
import json


class Status(str, Enum):
    VERIFIED = "VERIFIED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


class Authority(str, Enum):
    IN_FORCE = "IN_FORCE"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    OUTSIDE_SCOPE = "OUTSIDE_SCOPE"
    UNKNOWN = "UNKNOWN"


class Target(str, Enum):
    CLAIM = "CLAIM_REBUTTAL"
    INFERENCE = "WARRANT_UNDERCUTTER"
    SOURCE = "DATA_UNDERMINER"


class Action(str, Enum):
    CHECK_SOURCE = "CHECK_SOURCE"
    REASSESS_INFERENCE = "REASSESS_INFERENCE"
    REASSESS_CLAIM = "REASSESS_CLAIM"
    CHECK_AUTHORITY = "CHECK_AUTHORITY"
    CHECK_CONTRACT = "CHECK_CONTRACT"
    RECALCULATE_FORECAST = "RECALCULATE_FORECAST"


@dataclass(frozen=True)
class Forecast:
    """Input estimate; a revised probability is not a known-false premise."""
    likelihood: float | None
    impact: float | None
    source_id: str

    def __post_init__(self):
        if not self.source_id.strip():
            raise ValueError("forecast must carry provenance")
        if self.likelihood is not None and not 0 <= self.likelihood <= 1:
            raise ValueError("likelihood outside [0, 1]")
        if self.impact is not None and self.impact < 0:
            raise ValueError("negative forecast impact")

    @property
    def expected_impact(self):
        return None if self.likelihood is None or self.impact is None else self.likelihood * self.impact


@dataclass(frozen=True)
class PolicyRecord:
    status: Authority
    source_id: str
    scope: str

    def __post_init__(self):
        if not self.source_id.strip() or not self.scope.strip():
            raise ValueError("policy requires provenance and jurisdiction")


@dataclass(frozen=True)
class ContractRecord:
    """Existence/binding and observed satisfaction are separate inputs."""
    binds: Status
    observed_satisfaction: Status
    source_id: str

    def __post_init__(self):
        if not self.source_id.strip():
            raise ValueError("contract requires provenance")


@dataclass(frozen=True)
class Objection:
    target: Target
    source_id: str
    subject_id: str

    def __post_init__(self):
        if not self.source_id.strip() or not self.subject_id.strip():
            raise ValueError("objection requires source and named attacked object")


@dataclass(frozen=True)
class Review:
    """Independent state axes; never a verdict to replace an architecture."""
    forecast: Forecast
    policy: PolicyRecord
    contract: ContractRecord
    objections: tuple[Objection, ...]


def review_changes(before: Review, after: Review) -> frozenset[Action]:
    """Finite, explicit event-to-review routing. Does not resolve attacks."""
    tasks = set()
    if before.forecast != after.forecast:
        tasks.add(Action.RECALCULATE_FORECAST)
    if before.policy != after.policy or after.policy.status is Authority.UNKNOWN:
        tasks.add(Action.CHECK_AUTHORITY)
    if before.contract != after.contract or after.contract.binds is Status.UNKNOWN or after.contract.observed_satisfaction is Status.UNKNOWN:
        tasks.add(Action.CHECK_CONTRACT)
    old = set(before.objections)
    new = set(after.objections)
    for objection in old.symmetric_difference(new):
        tasks.add({Target.CLAIM: Action.REASSESS_CLAIM,
                   Target.INFERENCE: Action.REASSESS_INFERENCE,
                   Target.SOURCE: Action.CHECK_SOURCE}[objection.target])
    return frozenset(tasks)


def independent_oracle(before: Review, after: Review):
    """Separately composed declarative specification for deterministic checks."""
    changed = {"forecast": before.forecast != after.forecast,
               "authority": before.policy != after.policy,
               "contract": before.contract != after.contract}
    targets = {item.target for item in set(before.objections) ^ set(after.objections)}
    return frozenset(action for condition, action in (
        (changed["forecast"], Action.RECALCULATE_FORECAST),
        (changed["authority"] or after.policy.status == Authority.UNKNOWN, Action.CHECK_AUTHORITY),
        (changed["contract"] or after.contract.binds == Status.UNKNOWN or
         after.contract.observed_satisfaction == Status.UNKNOWN, Action.CHECK_CONTRACT),
        (Target.CLAIM in targets, Action.REASSESS_CLAIM),
        (Target.INFERENCE in targets, Action.REASSESS_INFERENCE),
        (Target.SOURCE in targets, Action.CHECK_SOURCE),
    ) if condition)


def test():
    original_forecast = Forecast(.8, 100.0, "forecast-v1")
    revised_forecast = Forecast(.2, 100.0, "forecast-v2")
    unknown_forecast = Forecast(None, 100.0, "forecast-pending")
    base_policy = PolicyRecord(Authority.IN_FORCE, "policy-v1", "team X")
    policy_states = tuple(PolicyRecord(a, "policy-v1", "team X") for a in Authority)
    base_contract = ContractRecord(Status.VERIFIED, Status.VERIFIED, "contract-v1")
    contract_states = tuple(ContractRecord(a, b, "contract-v1")
                            for a, b in product(Status, repeat=2))
    base = Review(original_forecast, base_policy, base_contract, ())
    assert original_forecast.expected_impact == 80.0
    assert revised_forecast.expected_impact == 20.0
    assert unknown_forecast.expected_impact is None
    assert review_changes(base, Review(revised_forecast, base_policy, base_contract, ())) == {
        Action.RECALCULATE_FORECAST}
    assert review_changes(base, Review(unknown_forecast, base_policy, base_contract, ())) == {
        Action.RECALCULATE_FORECAST}
    assert review_changes(base, Review(original_forecast, policy_states[1], base_contract, ())) == {
        Action.CHECK_AUTHORITY}
    # A binding policy does not certify usefulness; a failed implementation
    # does not imply the contract no longer binds.
    failed_contract = ContractRecord(Status.VERIFIED, Status.FAILED, "test-failure")
    assessed = Review(original_forecast, base_policy, failed_contract, ())
    assert assessed.contract.binds is Status.VERIFIED
    assert assessed.contract.observed_satisfaction is Status.FAILED
    assert review_changes(base, assessed) == {Action.CHECK_CONTRACT}
    attacks = tuple(Objection(t, "reviewer-evidence", "specific-object") for t in Target)
    expected = {
        Target.CLAIM: Action.REASSESS_CLAIM,
        Target.INFERENCE: Action.REASSESS_INFERENCE,
        Target.SOURCE: Action.CHECK_SOURCE,
    }
    for a in attacks:
        updated = Review(original_forecast, base_policy, base_contract, (a,))
        assert review_changes(base, updated) == {expected[a.target]}
        assert review_changes(updated, base) == {expected[a.target]}
    # Full cross product: forecasts × policy states × contract states × 2^3 attacks.
    forecasts = (original_forecast, revised_forecast, unknown_forecast)
    total = 0
    tasks_seen = set()
    for f, p, c, flags in product(forecasts, policy_states, contract_states,
                                  product((False, True), repeat=3)):
        objections = tuple(o for present, o in zip(flags, attacks) if present)
        state = Review(f, p, c, objections)
        actual = review_changes(base, state)
        assert actual == independent_oracle(base, state)
        tasks_seen.update(actual)
        total += 1
    assert total == 3 * 5 * 9 * 8 == 1080
    assert tasks_seen == set(Action)
    # Fail-closed input controls (rather than converting missing provenance to truth).
    for make in (
        lambda: Forecast(-.01, 1, "x"),
        lambda: Forecast(1.01, 1, "x"),
        lambda: Forecast(.5, -1, "x"),
        lambda: Forecast(.5, 1, ""),
        lambda: PolicyRecord(Authority.IN_FORCE, "", "team X"),
        lambda: PolicyRecord(Authority.IN_FORCE, "x", ""),
        lambda: ContractRecord(Status.VERIFIED, Status.VERIFIED, ""),
        lambda: Objection(Target.CLAIM, "", "w"),
        lambda: Objection(Target.CLAIM, "x", ""),
    ):
        try:
            make()
        except ValueError:
            continue
        raise AssertionError("malformed input accepted")
    return {
        "finite_cross_product_cases": total,
        "independent_oracle": "PASS",
        "attack_type_reversibility_cases": len(attacks) * 2,
        "typed_authority_contract_axes": "DISTINCT",
        "forecast_revision_is_binary_mismatch": False,
        "recommendation_or_quality_oracle": "NOT_IMPLEMENTED",
        "strong_adr_or_arel_advantage": "NOT_ESTABLISHED",
        "real_source_ground_truth": "NOT_OBSERVED",
    }


if __name__ == "__main__":
    print(json.dumps(test(), ensure_ascii=False, sort_keys=True))
