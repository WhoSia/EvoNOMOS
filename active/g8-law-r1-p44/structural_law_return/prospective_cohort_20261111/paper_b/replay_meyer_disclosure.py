"""Replay verdicts for every disclosure of the fixed-patch demand and contract."""

import json
from itertools import product
from pathlib import Path

RESULTS = Path(__file__).with_name("meyer_judgment_pair_results.json")


def delivered_verdict(rows, demand=None, contract=None):
    matching = (
        row["acceptable"]
        for row in rows
        if (demand is None or row["demand"] == demand)
        and (contract is None or row["contract"] == contract)
    )
    outcomes = set(matching)
    if not outcomes:
        raise ValueError("No admissible specification matches the disclosure")
    if outcomes == {True}:
        return "accept"
    if outcomes == {False}:
        return "reject"
    return "defer"


def main():
    rows = json.loads(RESULTS.read_text(encoding="utf-8"))["fixed_patch_judgments"]
    demands = list(dict.fromkeys(row["demand"] for row in rows))
    contracts = list(dict.fromkeys(row["contract"] for row in rows))
    print("demand,contract,verdict")
    for demand, contract in product([*demands, None], [*contracts, None]):
        print(f"{demand or 'withheld'},{contract or 'withheld'},"
              f"{delivered_verdict(rows, demand, contract)}")


if __name__ == "__main__":
    main()
