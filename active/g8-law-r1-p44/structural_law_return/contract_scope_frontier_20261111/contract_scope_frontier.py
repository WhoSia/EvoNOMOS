"""Exact rational contract-obligation threshold over SOURCE-VERIFIED action choices.

All probability, engineering cost and downstream penalty inputs are ASSUMPTIONS,
not estimates. This is classical finite expected-loss decision theory.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import json

@dataclass(frozen=True)
class Assumptions:
    shared_cost: F
    local_cost: F
    legacy_loss: F
    protection_probability_low: F
    protection_probability_high: F
    def __post_init__(self):
        if min(self.shared_cost,self.local_cost,self.legacy_loss)<0:
            raise ValueError("nonnegative costs required")
        if not (0<=self.protection_probability_low<=self.protection_probability_high<=1):
            raise ValueError("invalid unknown client obligation probability interval")

# Prior full native Go CI #42932257551, NOT inferred by cost model.
NATIVE_BOUNDED_OPTIONS={
    "route_only":frozenset({"constructor","route_both","match_lower"}),
    "route_plus_direct":frozenset({"route_both"}),
}

def evaluate(x:Assumptions,hard_protection:bool=False)->dict:
    shared_allowed=(not hard_protection) or x.protection_probability_high==0
    local_allowed=True
    difference=x.local_cost-x.shared_cost
    lower=x.protection_probability_low*x.legacy_loss-difference
    upper=x.protection_probability_high*x.legacy_loss-difference
    if hard_protection and not shared_allowed:
        verdict="LOCAL_ONLY_HARD_CLIENT_CONTRACT"
    elif lower>0:
        verdict="LOCAL_ROBUSTLY_LOWER_EXPECTED_LOSS"
    elif upper<0:
        verdict="SHARED_ROBUSTLY_LOWER_EXPECTED_LOSS"
    elif lower==upper==0:
        verdict="COST_TIE"
    else:
        verdict="ABSTAIN_SENSITIVE_TO_UNMEASURED_CLIENT_SCOPE"
    return {
        "shared_is_feasible_under_hard_contract":shared_allowed,
        "local_is_feasible_under_hard_contract":local_allowed,
        "signed_shared_minus_local_loss_range":[str(lower),str(upper)],
        "verdict":verdict,
        "assumed_values_not_measured":True,
        "native_test_oracle_actions":{k:sorted(v) for k,v in NATIVE_BOUNDED_OPTIONS.items()},
        "cannot_infer_real_maintainer_cost":True,
    }

if __name__=="__main__":
    x=Assumptions(F(1),F(2),F(4),F(1,10),F(2,5))
    print(json.dumps(evaluate(x),indent=2))
    print(json.dumps(evaluate(x,hard_protection=True),indent=2))
