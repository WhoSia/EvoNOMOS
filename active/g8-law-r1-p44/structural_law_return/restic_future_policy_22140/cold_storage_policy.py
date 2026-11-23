"""Restic issue #22140 — bounded, researcher-defined cost counterexample.

NOT a Restic fix, billing estimate, upstream source modification or new law.
Unit: one full pack's monthly storage price (pack-month).
"""
from dataclasses import dataclass
from fractions import Fraction

@dataclass(frozen=True)
class PackObservation:
    unused_fraction: Fraction
    remaining_months: int

    def __post_init__(self):
        if not 0 <= self.unused_fraction < 1:
            raise ValueError("unused_fraction must be within [0,1)")
        if self.remaining_months <= 0:
            raise ValueError("remaining months must be positive")

@dataclass(frozen=True)
class BillingEnvironment:
    # pay_as_you_go: deleting old storage stops future monthly charges
    # prepaid_locked: original pack cost is already committed/nonrefundable
    plan: str
    rewrite_operation_cost: Fraction = Fraction(1, 100)

    def __post_init__(self):
        if self.plan not in ("pay_as_you_go", "prepaid_locked"):
            raise ValueError("unsupported illustrative plan")
        if self.rewrite_operation_cost < 0:
            raise ValueError("negative costs disallowed")

def incremental_cost_of_repack(obs: PackObservation, env: BillingEnvironment) -> Fraction:
    """C(repack)-C(keep) over the fixed remaining time horizon.

    If prepaid: sunk old storage + new charges on (1-u) rewritten fraction.
    If pay-as-you-go: save u fraction over n months + one-time rewrite.
    Transfers, thawing, transaction fees, partial billing are excluded.
    """
    u, n = obs.unused_fraction, obs.remaining_months
    if env.plan == "prepaid_locked":
        return (1 - u) * n + env.rewrite_operation_cost
    return -u * n + env.rewrite_operation_cost

def optimal_action(obs: PackObservation, env: BillingEnvironment) -> str:
    return "repack" if incremental_cost_of_repack(obs, env) < 0 else "keep"

if __name__ == "__main__":
    obs = PackObservation(Fraction(5, 100), 11)
    for plan in ("prepaid_locked", "pay_as_you_go"):
        env = BillingEnvironment(plan)
        print(plan, "delta_pack_months", incremental_cost_of_repack(obs, env),
              "preferred", optimal_action(obs, env))
