"""Compare two maintenance requests and two client contracts on one fixed patch."""

import json

from meyer_library_case import (
    BASE_SOURCES,
    BOOK_OVERRIDE,
    EXPECTED_LEGACY,
    EXPECTED_REPORT,
    LEGACY_REQUESTS,
    NEW_REQUEST,
    PROVIDER_EXTENSION,
    check_equal,
    observe_sources,
)

REQUESTS = LEGACY_REQUESTS | {
    "technical_report": NEW_REQUEST,
    "erratum": ("erratum", "Modules", "Section 2"),
}
EXPECTED_NEW = {
    "technical_report": EXPECTED_REPORT,
    "erratum": ("rendered", "[library] erratum: Modules (Section 2)"),
}
REQUIREMENTS = {
    "report": ("technical_report",),
    "report_and_erratum": ("technical_report", "erratum"),
}
CONTRACTS = {
    "journal_proceedings_unknown": ("journal", "proceedings", "unknown"),
    "plus_book": ("journal", "proceedings", "unknown", "book"),
}
ERRATUM_EXTENSION = '''        if kind == "erratum":
            return f"erratum: {title} ({detail})"
'''


def compare(observations):
    cells = []
    for demand, required in REQUIREMENTS.items():
        demand_met = all(observations[key] == EXPECTED_NEW[key] for key in required)
        for contract, protected in CONTRACTS.items():
            contract_preserved = all(
                observations[key] == EXPECTED_LEGACY[key] for key in protected
            )
            cells.append({
                "demand": demand,
                "contract": contract,
                "demand_met": demand_met,
                "contract_preserved": contract_preserved,
                "acceptable": demand_met and contract_preserved,
            })
    return cells


def main():
    baseline = observe_sources(BASE_SOURCES, REQUESTS)
    for kind in EXPECTED_NEW:
        check_equal(
            baseline[kind], ("ValueError", f"unsupported publication kind: {kind}"),
            f"baseline rejects {kind}",
        )
    fixed = BASE_SOURCES | {
        "reports.py": PROVIDER_EXTENSION.replace("<book_override>", BOOK_OVERRIDE)
    }
    witness = BASE_SOURCES | {
        "reports.py": PROVIDER_EXTENSION.replace("<book_override>", ERRATUM_EXTENSION)
    }
    observed = observe_sources(fixed, REQUESTS)
    cells = compare(observed)
    check_equal(
        [(cell["demand_met"], cell["contract_preserved"]) for cell in cells],
        [(True, True), (True, False), (False, True), (False, False)],
        "independent outcomes on identical code",
    )
    witness_cells = compare(observe_sources(witness, REQUESTS))
    check_equal(all(cell["acceptable"] for cell in witness_cells), True, "joint feasibility")
    for sources in (fixed, witness):
        check_equal(
            {path: sources[path] for path in BASE_SOURCES}, BASE_SOURCES,
            "existing source frozen",
        )
    print(json.dumps({
        "fixed_patch_observations": observed,
        "fixed_patch_judgments": cells,
        "one_additive_witness_satisfies_all_four": True,
    }, indent=2))


if __name__ == "__main__":
    main()
