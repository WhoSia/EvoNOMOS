"""Conservative evidence-stage classifier; NOT a cryptographic or causal certificate."""
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class Grade(str, Enum):
    INVALID = "INVALID"
    HISTORICAL = "HISTORICAL_REPLAY"
    PROTOCOL = "PREREGISTERED_ONLY"
    REVEALED = "PRE_REVEAL_SEAL_VERIFIED"
    EXECUTED = "MATCHED_SOURCE_EXECUTED"
    CAUSAL_CANDIDATE = "CAUSAL_CANDIDATE_NEEDS_REPLICATION"

@dataclass(frozen=True)
class Evidence:
    prereg_hash: str = ""
    prereg_time: Optional[int] = None
    reveal_time: Optional[int] = None
    manifest_hash_before_reveal: bool = False
    independent_demand_author: bool = False
    matched_source_arms: bool = False
    equivalent_permissions: bool = False
    protected_old_contracts: bool = False
    executed_source_tests: bool = False
    actor_assignment_predeclared: bool = False
    observed_outcomes: bool = False
    baseline_same_information: bool = False
    leakage_or_postselection: bool = False
    historical_demand: bool = False

def classify(e: Evidence) -> Grade:
    """Fail closed. Flags MUST be audited from independent evidence."""
    if e.leakage_or_postselection:
        return Grade.INVALID
    if e.historical_demand:
        return Grade.HISTORICAL
    if not e.prereg_hash or e.prereg_time is None:
        return Grade.INVALID
    if e.reveal_time is None:
        return Grade.PROTOCOL
    if e.prereg_time >= e.reveal_time or not e.manifest_hash_before_reveal or not e.independent_demand_author:
        return Grade.INVALID
    if not (e.matched_source_arms and e.equivalent_permissions and e.protected_old_contracts and e.executed_source_tests):
        return Grade.REVEALED
    if not (e.actor_assignment_predeclared and e.observed_outcomes and e.baseline_same_information):
        return Grade.EXECUTED
    return Grade.CAUSAL_CANDIDATE
