"""R79 P35 contract-conditioned decision court, on historical receipts only.

Strong linked-ADR and ATLAS each encode the SAME historical facts by distinct
lookup paths; their disagreement can now be detected. Contract identity must be stated before
declaring a winner. This is NOT a human study or a fresh Go execution.
"""
from itertools import product
import json

# Separately transcribed representations of the same historical CI report.
ADR_RECORDS = (
    ("D0", "LIVE", "SATISFIES"),
    ("D0", "SNAPSHOT", "SATISFIES"),
    ("D-LIVE", "LIVE", "SATISFIES"),
    ("D-LIVE", "SNAPSHOT", "VIOLATES"),
    ("D-FROZEN", "LIVE", "VIOLATES"),
    ("D-FROZEN", "SNAPSHOT", "SATISFIES"),
)
ATLAS_FACTS = {
    "LIVE": {"D0": True, "D-LIVE": True, "D-FROZEN": False},
    "SNAPSHOT": {"D0": True, "D-LIVE": False, "D-FROZEN": True},
}
RECEIPT = "https://github.com/WhoSia/EvoNOMOS/actions/runs/37908914089"
ARMS = ("LIVE", "SNAPSHOT")
CONTRACTS = frozenset(("D0", "D-LIVE", "D-FROZEN"))


def score_from_receipt(contract, candidate, method, *, atlas_facts=None):
    """Comparable factual answer, not an architectural preference."""
    if method not in ("ADR_LINKED", "ATLAS"):
        raise ValueError("unsupported method")
    if candidate not in ARMS:
        raise ValueError("unsupported arm")
    if contract is None:
        return "ABSTAIN_CONTRACT_UNSPECIFIED"
    if contract not in CONTRACTS:
        raise ValueError("unknown contract")
    if method == "ADR_LINKED":
        matched = [status for c, a, status in ADR_RECORDS
                   if c == contract and a == candidate]
        if len(matched) != 1:
            raise ValueError("missing/duplicate ADR fact")
        return matched[0]
    facts = ATLAS_FACTS if atlas_facts is None else atlas_facts
    try:
        outcome = facts[candidate][contract]
    except KeyError as exc:
        raise ValueError("missing ATLAS fact") from exc
    if type(outcome) is not bool:
        raise ValueError("ATLAS fact must be a Boolean")
    return "SATISFIES" if outcome else "VIOLATES"


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
    # A mismatched transcription must be detected, not hidden by shared code.
    mutated = {arm: dict(vals) for arm, vals in ATLAS_FACTS.items()}
    mutated["LIVE"]["D-FROZEN"] = True
    assert score_from_receipt("D-FROZEN", "LIVE", "ADR_LINKED") != (
        score_from_receipt("D-FROZEN", "LIVE", "ATLAS", atlas_facts=mutated))
    return {
        "separate_representation_paths": True,
        "transcription_mutation_detected": True,
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
