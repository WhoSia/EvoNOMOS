"""R79 P35 contract-conditioned decision court, on historical receipts only.

A strong linked-ADR baseline and candidate ATLAS receive the SAME fixed
contract and observed arm outcomes. Contract identity must be stated before
declaring a winner. This is NOT a human study or a fresh Go execution.
"""
from itertools import product
import json

RESULTS = {
    "D0": {"LIVE": True, "SNAPSHOT": True},
    "D-LIVE": {"LIVE": True, "SNAPSHOT": False},
    "D-FROZEN": {"LIVE": False, "SNAPSHOT": True},
}
RECEIPT = "https://github.com/WhoSia/EvoNOMOS/actions/runs/37908914089"
ARMS = ("LIVE", "SNAPSHOT")
CONTRACTS = frozenset(RESULTS)


def score_from_receipt(contract, candidate, method):
    """Comparable factual answer, not an architectural preference."""
    if method not in ("ADR_LINKED", "ATLAS"):
        raise ValueError("unsupported method")
    if candidate not in ARMS:
        raise ValueError("unsupported arm")
    if contract is None:
        return "ABSTAIN_CONTRACT_UNSPECIFIED"
    if contract not in CONTRACTS:
        raise ValueError("unknown contract")
    return "SATISFIES" if RESULTS[contract][candidate] else "VIOLATES"


def winner(contract, method):
    if method not in ("ADR_LINKED", "ATLAS"):
        raise ValueError("unsupported method")
    if contract is None:
        return "UNDETERMINED"
    if contract not in CONTRACTS:
        raise ValueError("unknown contract")
    fits = [a for a in ARMS if score_from_receipt(contract, a, method) == "SATISFIES"]
    return fits[0] if len(fits) == 1 else "TIE" if len(fits) == 2 else "NONE"


def test():
    cells = 0
    for c, arm in product(("D0", "D-LIVE", "D-FROZEN", None), ARMS):
        assert score_from_receipt(c, arm, "ADR_LINKED") == score_from_receipt(c, arm, "ATLAS")
        cells += 1
    for c in ("D0", "D-LIVE", "D-FROZEN", None):
        assert winner(c, "ADR_LINKED") == winner(c, "ATLAS")
    assert winner("D0", "ADR_LINKED") == "TIE"
    assert winner("D-LIVE", "ATLAS") == "LIVE"
    assert winner("D-FROZEN", "ADR_LINKED") == "SNAPSHOT"
    assert winner(None, "ATLAS") == "UNDETERMINED"
    for f in (
        lambda: score_from_receipt("OTHER", "LIVE", "ATLAS"),
        lambda: score_from_receipt("D-LIVE", "OTHER", "ATLAS"),
        lambda: score_from_receipt("D-LIVE", "LIVE", "UNKNOWN"),
        lambda: winner("OTHER", "ADR_LINKED"),
    ):
        try:
            f()
        except ValueError:
            continue
        raise AssertionError("invalid datum accepted")
    return {
        "historical_receipt": RECEIPT,
        "same_information_cells": cells,
        "same_contract_winners_checked": 4,
        "unlabeled_contract": "ABSTAIN",
        "strong_adr_atlas": "TIE",
        "negative_controls": 4,
        "new_go_run": False,
        "independent_truth_adjudication": False,
        "human_cost": "NOT_MEASURED",
        "result": "PASS_CONTRACT_CONDITIONED_NEGATIVE_RESULT",
    }


if __name__ == "__main__":
    print(json.dumps(test(), sort_keys=True))
