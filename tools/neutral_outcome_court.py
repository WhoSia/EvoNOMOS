"""Independent observable-outcome protocol court for design-rationale methods.

Golden labels derive ONLY from observable client tests and authoritative policy
records, not from ATLAS scope, Belnap evidence, or the researcher's design choice.
This is a synthetic preflight/checker, NOT an empirical human study.
"""
from dataclasses import dataclass
from itertools import product
from typing import Optional
import json


@dataclass(frozen=True)
class Observation:
    event_id: str
    obligation_active: Optional[bool]
    observed_before: Optional[str]
    observed_after: Optional[str]
    policy_active: Optional[bool]
    permission_granted: Optional[bool]

    def __post_init__(self):
        if not self.event_id.strip():
            raise ValueError('empty independent event ID')


def external_oracle(o: Observation) -> frozenset[str]:
    """Outcome truth from observable behavior and signed authority; not design labels."""
    issues = set()
    if o.obligation_active is None:
        issues.add('VERIFY_OBLIGATION')
    elif o.obligation_active:
        if o.observed_before is None or o.observed_after is None:
            issues.add('RUN_CLIENT_TEST')
        elif o.observed_before != o.observed_after:
            issues.add('CLIENT_REGRESSION')
    if o.policy_active is None:
        issues.add('VERIFY_POLICY')
    elif o.policy_active:
        if o.permission_granted is None:
            issues.add('CHECK_APPROVAL')
        elif not o.permission_granted:
            issues.add('POLICY_NONCOMPLIANCE')
    return frozenset(issues)


def independent_spec(o: Observation) -> frozenset[str]:
    """A truth-table implementation different from the imperative oracle."""
    predicates = (
        ('VERIFY_OBLIGATION', o.obligation_active is None),
        ('RUN_CLIENT_TEST', o.obligation_active is True and
         (o.observed_before is None or o.observed_after is None)),
        ('CLIENT_REGRESSION', o.obligation_active is True and
         o.observed_before is not None and o.observed_after is not None and
         o.observed_before != o.observed_after),
        ('VERIFY_POLICY', o.policy_active is None),
        ('CHECK_APPROVAL', o.policy_active is True and o.permission_granted is None),
        ('POLICY_NONCOMPLIANCE', o.policy_active is True and
         o.permission_granted is False),
    )
    return frozenset(key for key, yes in predicates if yes)


@dataclass(frozen=True)
class MethodReport:
    method: str
    event_id: str
    predicted_actions: frozenset[str]
    evidence_ids: frozenset[str]


def score(report: MethodReport, observation: Observation) -> dict:
    if report.event_id != observation.event_id:
        raise ValueError('event identity mismatch')
    if not report.evidence_ids:
        raise ValueError('no provenance for evaluated report')
    valid = external_oracle(observation)
    predicted = report.predicted_actions
    if predicted - ACTIONS:
        raise ValueError('unsupported observable-action label')
    return {'tp': len(predicted & valid), 'fp': len(predicted - valid),
            'fn': len(valid - predicted), 'tn': len(ACTIONS - valid - predicted)}


ACTIONS = frozenset(('VERIFY_OBLIGATION', 'RUN_CLIENT_TEST', 'CLIENT_REGRESSION',
                     'VERIFY_POLICY', 'CHECK_APPROVAL', 'POLICY_NONCOMPLIANCE'))


def compare_reports(adr: MethodReport, atlas: MethodReport,
                    observation: Observation):
    """No asymmetric information or schema-preferred reward."""
    if adr.method != 'ADR_STRONG' or atlas.method != 'ATLAS':
        raise ValueError('unrecognized comparison arms')
    if adr.evidence_ids != atlas.evidence_ids:
        raise ValueError('unequal evidence access')
    return {'adr': score(adr, observation), 'atlas': score(atlas, observation)}


def test():
    states = (None, False, True)
    before_after = (None, 'HTTP 200', 'HTTP 404')
    tested = 0
    coverage = set()
    for (obligation, before, after, policy, approval) in product(
            states, before_after, before_after, states, states):
        o = Observation('event', obligation, before, after, policy, approval)
        assert external_oracle(o) == independent_spec(o)
        coverage.update(external_oracle(o))
        same = external_oracle(o)
        adr = MethodReport('ADR_STRONG', 'event', same, frozenset({'source-1'}))
        atlas = MethodReport('ATLAS', 'event', same, frozenset({'source-1'}))
        assert compare_reports(adr, atlas, o)['adr'] == compare_reports(adr, atlas, o)['atlas']
        assert compare_reports(adr, atlas, o)['adr']['fp'] == 0
        assert compare_reports(adr, atlas, o)['adr']['fn'] == 0
        tested += 1
    assert tested == 3 ** 5 == 243
    assert coverage == ACTIONS
    regression = Observation('r1', True, 'HTTP 200', 'HTTP 404', False, False)
    assert external_oracle(regression) == {'CLIENT_REGRESSION'}
    inactive = Observation('r2', False, 'HTTP 200', 'HTTP 404', False, False)
    assert not external_oracle(inactive)
    unauthorized = Observation('r3', True, 'HTTP 200', 'HTTP 200', True, False)
    assert external_oracle(unauthorized) == {'POLICY_NONCOMPLIANCE'}
    unknown = Observation('r4', None, None, None, None, None)
    assert external_oracle(unknown) == {'VERIFY_OBLIGATION', 'VERIFY_POLICY'}
    not_proven = MethodReport('ATLAS', 'r1', frozenset(), frozenset({'source-1'}))
    assert score(not_proven, regression)['fn'] == 1
    for invalid in (
        lambda: compare_reports(MethodReport('ADR_STRONG', 'r1', frozenset(), frozenset({'a'})),
                                MethodReport('ATLAS', 'r1', frozenset(), frozenset({'b'})), regression),
        lambda: score(MethodReport('ATLAS', 'wrong', frozenset(), frozenset({'a'})), regression),
        lambda: score(MethodReport('ATLAS', 'r1', frozenset(), frozenset()), regression),
        lambda: score(MethodReport('ATLAS', 'r1', frozenset({'OUT_OF_SCOPE'}), frozenset({'a'})), regression),
        lambda: Observation('', True, 'HTTP 200', 'HTTP 200', False, False),
    ):
        try:
            invalid()
        except ValueError:
            continue
        raise AssertionError('invalid comparison did not fail closed')
    return {'independent_synthetic_states': tested, 'actions': sorted(ACTIONS),
            'equal_information_equal_output': 'TIE',
            'fact_oracle': 'EXTERNAL_OBSERVATIONS_AND_AUTHORITY',
            'real_go_source_executed': False, 'human_study_executed': False,
            'pre_registered_human_ground_truth': False,
            'result': 'PASS_SYNTHETIC_PROTOCOL_ONLY'}


if __name__ == '__main__':
    print(json.dumps(test(), sort_keys=True))
