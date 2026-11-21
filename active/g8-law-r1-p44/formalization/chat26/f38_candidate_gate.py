"""Metadata-only prescreen of proposed F38 original-source maintenance trials.

The gate never judges source code correctness or maintainer permissions from
metadata alone. Fail-closed: missing source facts cannot authorize a LAW claim.
"""
from dataclasses import dataclass
from enum import Enum


class Gate(str, Enum):
    INSUFFICIENT_PROVENANCE = "INSUFFICIENT_PROVENANCE"
    SHARED_UPSTREAM_OUT_OF_SCOPE = "SHARED_UPSTREAM_OUT_OF_SCOPE"
    NONBLIND_EXPLORATORY = "NONBLIND_EXPLORATORY"
    CONTRACT_OR_RIGHTS_UNVERIFIED = "CONTRACT_OR_RIGHTS_UNVERIFIED"
    UNSEALED_FORECAST = "UNSEALED_FORECAST"
    NOT_EXECUTED = "NOT_EXECUTED"
    EXECUTED_UNVERIFIED = "EXECUTED_UNVERIFIED"
    EXECUTED_EVIDENCE_OPEN = "EXECUTED_EVIDENCE_OPEN"


@dataclass(frozen=True)
class Candidate:
    external_url: str
    source_author_independent: bool
    selected_without_arm_cost_inspection: bool
    edit_locus_app_owned: bool
    declared_old_contract: bool
    equivalent_edit_rights: bool
    forecast_presealed: bool
    original_source_test_executed: bool
    source_verdict_independently_checked: bool


def classify(c: Candidate) -> Gate:
    # Order matters: never call a shared-upstream-only issue a source-arm result.
    if not c.external_url.startswith("https://github.com/") or not c.source_author_independent:
        return Gate.INSUFFICIENT_PROVENANCE
    if not c.edit_locus_app_owned:
        return Gate.SHARED_UPSTREAM_OUT_OF_SCOPE
    if not c.selected_without_arm_cost_inspection:
        return Gate.NONBLIND_EXPLORATORY
    if not (c.declared_old_contract and c.equivalent_edit_rights):
        return Gate.CONTRACT_OR_RIGHTS_UNVERIFIED
    if not c.forecast_presealed:
        return Gate.UNSEALED_FORECAST
    if not c.original_source_test_executed:
        return Gate.NOT_EXECUTED
    if not c.source_verdict_independently_checked:
        return Gate.EXECUTED_UNVERIFIED
    return Gate.EXECUTED_EVIDENCE_OPEN


HISTORICAL_TRIAGE = {
    # All are post hoc selections by this research session, not blind trial IDs.
    # #995's offending singleton middleware is app-authored in the issue body;
    # editing that application middleware may be feasible without Chi rights.
    # #1035's surviving 405 concern has an app-owned explicit static PUT
    # workaround reproduced on pinned Chi; this is NOT an upstream fix.
    # #1263 still lacks matched app-owned workaround and rights evidence.
    "chi-995": Candidate("https://github.com/go-chi/chi/issues/995",
                          True, False, True, False, False, False, False, False),
    "chi-1035": Candidate("https://github.com/go-chi/chi/issues/1035",
                           True, False, True, False, False, False, False, False),
    "chi-1263": Candidate("https://github.com/go-chi/chi/issues/1263",
                           True, False, False, False, False, False, False, False),
}
