"""R77: source-receipt-aware P35 experimental case register.

This is an archive/contract integrity check, NOT a new Go/Chi execution, not
an independent truth adjudication, and not a comparative ATLAS result.
The observed statuses are historical claims from the pinned P35-P7 report.
"""
from dataclasses import dataclass
from collections import defaultdict
from itertools import product
import json

COMMON_BLOB = "81f8123d6e24eb92c1ce9529f170be36191dd1c1"
D8_BLOB = "ed13ceb8f78ccc923f58ea12584a366cd3080d37"
SOURCE_REPORT = "https://app.notion.com/p/421ef561cf9281358f3acf42af65a5f3"
NATIVE_RECEIPT = "https://github.com/WhoSia/EvoNOMOS/actions/runs/37908914089"
OBSERVATION_KIND = "HISTORICAL_NATIVE_CI_REPORTED_NOT_RERUN"


@dataclass(frozen=True)
class Observation:
    scenario: str
    arm: str
    outcome: str
    contract_id: str
    receipt_url: str
    origin: str = OBSERVATION_KIND

    def __post_init__(self):
        if self.arm not in {"LIVE", "SNAPSHOT"}:
            raise ValueError("unrecognized treatment")
        if self.outcome not in {"PASS", "FAIL"}:
            raise ValueError("non-Boolean archival result")
        if self.scenario not in {"D0", "D-LIVE", "D-FROZEN"}:
            raise ValueError("unfrozen scenario")
        if not self.contract_id or not self.receipt_url.startswith("https://"):
            raise ValueError("provenance and specific contract required")
        if self.origin != OBSERVATION_KIND:
            raise ValueError("archival evidence cannot be relabeled as fresh execution")


ARCHIVE = (
    Observation("D0", "LIVE", "PASS", "COMMON_D0", NATIVE_RECEIPT),
    Observation("D0", "SNAPSHOT", "PASS", "COMMON_D0", NATIVE_RECEIPT),
    Observation("D-LIVE", "LIVE", "PASS", "POST_CONSTRUCTION_UPDATES_VISIBLE", NATIVE_RECEIPT),
    Observation("D-LIVE", "SNAPSHOT", "FAIL", "POST_CONSTRUCTION_UPDATES_VISIBLE", NATIVE_RECEIPT),
    Observation("D-FROZEN", "LIVE", "FAIL", "POST_CONSTRUCTION_UPDATES_HIDDEN", NATIVE_RECEIPT),
    Observation("D-FROZEN", "SNAPSHOT", "PASS", "POST_CONSTRUCTION_UPDATES_HIDDEN", NATIVE_RECEIPT),
)


def inspect(records=ARCHIVE):
    index = {}
    for item in records:
        key = (item.scenario, item.arm)
        if key in index:
            raise ValueError("duplicate scenario-arm record")
        index[key] = item
    expected = {(scenario, arm) for scenario, arm in
                product(("D0", "D-LIVE", "D-FROZEN"), ("LIVE", "SNAPSHOT"))}
    if set(index) != expected:
        raise ValueError("archive has missing or extra cases")
    contracts = defaultdict(set)
    for item in records:
        contracts[item.scenario].add(item.contract_id)
    if any(len(ids) != 1 for ids in contracts.values()):
        raise ValueError("contract mismatch within a scenario")
    if contracts["D-LIVE"] == contracts["D-FROZEN"]:
        raise ValueError("different future contracts collapsed into one")
    if {index[("D0", arm)].outcome for arm in ("LIVE", "SNAPSHOT")} != {"PASS"}:
        raise ValueError("historical D0 conditions changed")
    if not (index[("D-LIVE", "LIVE")].outcome == "PASS"
            and index[("D-LIVE", "SNAPSHOT")].outcome == "FAIL"
            and index[("D-FROZEN", "LIVE")].outcome == "FAIL"
            and index[("D-FROZEN", "SNAPSHOT")].outcome == "PASS"):
        raise ValueError("P35 historical outcomes altered")
    return {
        "receipt_class": OBSERVATION_KIND,
        "rows": len(index),
        "original_go_rerun": False,
        "source_hashes": {"common_test_git_blob": COMMON_BLOB,
                          "d8_test_git_blob": D8_BLOB},
        "D0": "TIE",
        "post_construction": "CONTEXT_DEPENDENT_OPPOSITE_OUTCOMES",
        "same_contract_global_winner": "NOT_IDENTIFIED",
        "d8_reported_new_frozen_test": "NOT_EXECUTED_IN_THIS_COURT",
        "novel_ATLAS_advantage": "NOT_EVALUATED",
    }


def test():
    state = inspect()
    assert state["rows"] == 6 and state["original_go_rerun"] is False
    assert state["same_contract_global_winner"] == "NOT_IDENTIFIED"
    bad = [
        ARCHIVE[:-1],
        ARCHIVE + (ARCHIVE[0],),
        tuple(Observation(x.scenario, x.arm, x.outcome,
                          "SAME_CONTRACT" if x.scenario != "D0" else x.contract_id,
                          x.receipt_url) for x in ARCHIVE),
        tuple(Observation(x.scenario, x.arm,
                          "FAIL" if x.scenario == "D0" and x.arm == "LIVE" else x.outcome,
                          x.contract_id, x.receipt_url) for x in ARCHIVE),
        tuple(Observation(x.scenario, x.arm, x.outcome,
                          "OTHER" if x.scenario == "D-LIVE" and x.arm == "LIVE"
                          else x.contract_id, x.receipt_url) for x in ARCHIVE),
    ]
    for altered in bad:
        try:
            inspect(altered)
        except ValueError:
            continue
        raise AssertionError("inconsistent historical archive accepted")
    try:
        Observation("D-LIVE", "LIVE", "PASS",
                    "POST_CONSTRUCTION_UPDATES_VISIBLE", NATIVE_RECEIPT,
                    origin="FRESH_GOLANG_RUN")
    except ValueError:
        pass
    else:
        raise AssertionError("archival result falsely promoted to new Go run")
    return state | {"negative_controls": len(bad) + 1,
                    "result": "PASS_ARCHIVAL_PROVENANCE_GATES"}


if __name__ == "__main__":
    print(json.dumps(test(), sort_keys=True))
