#!/usr/bin/env python3
"""EvoNOMOS prospective architecture choice toy, exact enumeration.

All tasks/costs/probabilities are fabricated for methodological inspection.
Not real repository observations, live AI-agent experiments or a new design law.
Requires Python 3 standard library only. Run: python 86_EVONOMOS_R41_PROSPECTIVE_SELECTOR_TOY.py
"""
from fractions import Fraction as F
from math import comb
import json

P_LOW, P_HIGH = F(1, 4), F(3, 4)
N_SIGNAL = 6
SETUP_X = F(12)
COST_B_VAR, COST_B_SHARED = F(6), F(1)
COST_X_VAR, COST_X_SHARED = F(1), F(4)


def binom(n, k, p):
    return F(comb(n, k)) * p**k * (1-p)**(n-k)


def cost(architecture, horizon, variants):
    shared = horizon - variants
    if architecture == "B":
        return COST_B_VAR * variants + COST_B_SHARED * shared
    if architecture == "X":
        return SETUP_X + COST_X_VAR * variants + COST_X_SHARED * shared
    raise ValueError(architecture)


def forecast(signal_count):
    """Posterior predictive p under a known stationary 50/50 regime mixture."""
    low = binom(N_SIGNAL, signal_count, P_LOW)
    high = binom(N_SIGNAL, signal_count, P_HIGH)
    posterior_high = high / (low + high)
    return P_LOW * (1-posterior_high) + P_HIGH * posterior_high


def expected_cost(architecture, horizon, p):
    return sum(binom(horizon, j, p) * cost(architecture, horizon, j)
               for j in range(horizon + 1))


def choice(horizon, signal_count):
    p_hat = forecast(signal_count)
    eb = expected_cost("B", horizon, p_hat)
    ex = expected_cost("X", horizon, p_hat)
    return ("X" if ex < eb else "B", ex == eb)


def model_result(horizon, signal_shifted=False, signal_independent=False):
    # A regime is selected before both the historical signal and future work.
    # Negative control: signals come from the OPPOSITE regime, without warning.
    rows = {}
    for p in (P_LOW, P_HIGH):
        q = F(1, 2) if signal_independent else ((1-p) if signal_shifted else p)
        b = expected_cost("B", horizon, p)
        x = expected_cost("X", horizon, p)
        policy_cost, tie_flag = F(0), F(0)
        for k in range(N_SIGNAL + 1):
            action, tied = choice(horizon, k)
            prob = binom(N_SIGNAL, k, q)
            policy_cost += prob * (x if action == "X" else b)
            if tied:
                tie_flag += prob
        rows[str(p)] = dict(always_B=b, always_X=x,
                            clairvoyant_oracle=min(b, x),
                            prospective_selector=policy_cost,
                            tie_flag_rate=tie_flag)
    keys = ["always_B", "always_X", "clairvoyant_oracle",
            "prospective_selector", "tie_flag_rate"]
    result = {key: sum(rows[str(p)][key] for p in (P_LOW, P_HIGH))/2
              for key in keys}
    result["relative_gain_vs_best_constant"] = (
        min(result["always_B"], result["always_X"])
        - result["prospective_selector"])
    result["horizon"] = horizon
    result["signal_shifted"] = signal_shifted
    result["signal_independent"] = signal_independent
    return result


def display(x):
    if isinstance(x, F):
        return dict(exact=str(x), decimal=round(float(x), 6))
    return x


def main():
    assert sum(binom(N_SIGNAL, k, P_LOW) for k in range(N_SIGNAL+1)) == 1
    assert sum(binom(N_SIGNAL, k, P_HIGH) for k in range(N_SIGNAL+1)) == 1
    assert forecast(3) == F(1, 2)
    assert choice(12, 0)[0] == "B" and choice(12, 6)[0] == "X"
    assert choice(12, 3) == ("B", True)
    assert expected_cost("B", 12, F(1, 2)) == expected_cost("X", 12, F(1, 2))
    rows = [model_result(horizon, shifted, independent)
            for horizon in (6, 12, 24)
            for shifted, independent in ((False, False), (False, True), (True, False))]
    assert model_result(12)["relative_gain_vs_best_constant"] > 0
    assert model_result(12, True)["relative_gain_vs_best_constant"] < 0
    assert model_result(12, False, True)["prospective_selector"] == F(42)
    assert model_result(6)["relative_gain_vs_best_constant"] >= 0
    print(json.dumps(
        [{key: display(value) for key, value in row.items()} for row in rows],
        ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
