"""Check source preservation and caller behavior in a fixed OCP example."""

import json
import platform


BASE_CATALOG = '''def describe(publication):
    kind, title, detail = publication
    if kind in {"book", "journal", "proceedings"}:
        return f"{kind}: {title} ({detail})"
    raise ValueError(f"unsupported publication kind: {kind}")
'''

BASE_CLIENT = '''def render(publication, describe):
    return f"[library] {describe(publication)}"
'''

DISPATCH_EXTENSION = '''    if kind == "technical_report":
        return f"report: {title} (institution: {detail})"
'''

PROVIDER_EXTENSION = '''def extend(previous_describe):
    def describe(publication):
        kind, title, detail = publication
        if kind == "technical_report":
            return f"report: {title} (institution: {detail})"
<book_override>        return previous_describe(publication)
    return describe
'''

BOOK_OVERRIDE = '''        if kind == "book":
            return f"BOOK: {title} ({detail})"
'''

BASE_SOURCES = {"catalog.py": BASE_CATALOG, "client.py": BASE_CLIENT}
LEGACY_REQUESTS = {
    "book": ("book", "Algebra", "North Press"),
    "journal": ("journal", "Computing", "Vol. 3"),
    "proceedings": ("proceedings", "Design", "1988"),
    "unknown": ("unknown", "Unclassified", "—"),
}
NEW_REQUEST = ("technical_report", "Modules", "Research Lab")
EXPECTED_LEGACY = {
    "book": ("rendered", "[library] book: Algebra (North Press)"),
    "journal": ("rendered", "[library] journal: Computing (Vol. 3)"),
    "proceedings": ("rendered", "[library] proceedings: Design (1988)"),
    "unknown": ("ValueError", "unsupported publication kind: unknown"),
}
EXPECTED_REPORT = ("rendered", "[library] report: Modules (institution: Research Lab)")


def load_fixed_source(path, source):
    namespace = {}
    exec(compile(source, path, "exec"), namespace)
    return namespace


def observe_sources(sources, requests):
    catalog = load_fixed_source("catalog.py", sources["catalog.py"])
    client = load_fixed_source("client.py", sources["client.py"])
    provider = catalog["describe"]
    if "reports.py" in sources:
        extension = load_fixed_source("reports.py", sources["reports.py"])
        provider = extension["extend"](provider)

    def observe(publication):
        try:
            return ("rendered", client["render"](publication, provider))
        except ValueError as error:
            return ("ValueError", str(error))

    return {key: observe(value) for key, value in requests.items()}


def evaluate(sources):
    observed = observe_sources(sources, LEGACY_REQUESTS | {"technical_report": NEW_REQUEST})
    return {key: observed[key] for key in LEGACY_REQUESTS}, observed["technical_report"]


def check_equal(actual, expected, description):
    if actual != expected:
        raise AssertionError(f"{description}: expected {expected!r}, got {actual!r}")


def main():
    legacy, report = evaluate(BASE_SOURCES)
    check_equal(legacy, EXPECTED_LEGACY, "baseline legacy")
    check_equal(
        report,
        ("ValueError", "unsupported publication kind: technical_report"),
        "baseline rejects the new kind",
    )

    extended_catalog = BASE_CATALOG.replace(
        '    raise ValueError', DISPATCH_EXTENSION + '    raise ValueError'
    )
    drifting_catalog = extended_catalog.replace(
        '        return f"{kind}: {title} ({detail})"',
        '        label = "BOOK" if kind == "book" else kind\n'
        '        return f"{label}: {title} ({detail})"',
    )
    cases = [
        (
            "additive_extension",
            {"reports.py": PROVIDER_EXTENSION.replace("<book_override>", "")},
            [],
            [],
        ),
        ("compatible_dispatch_edit", {"catalog.py": extended_catalog}, ["catalog.py"], []),
        (
            "behavior_drift_without_edit",
            {"reports.py": PROVIDER_EXTENSION.replace("<book_override>", BOOK_OVERRIDE)},
            [],
            ["book"],
        ),
        (
            "behavior_drift_with_edit",
            {"catalog.py": drifting_catalog},
            ["catalog.py"],
            ["book"],
        ),
    ]

    results = []
    for name, changes, expected_edits, expected_drift in cases:
        sources = BASE_SOURCES | changes
        observed_legacy, observed_report = evaluate(sources)
        edits = [path for path, text in BASE_SOURCES.items() if sources[path] != text]
        drift = [key for key, result in legacy.items() if observed_legacy[key] != result]
        check_equal(observed_report, EXPECTED_REPORT, f"{name} report behavior")
        check_equal(edits, expected_edits, f"{name} existing source edits")
        check_equal(drift, expected_drift, f"{name} legacy behavior drift")
        results.append({
            "case": name,
            "added_source_files": sorted(sources.keys() - BASE_SOURCES.keys()),
            "edited_existing_sources": edits,
            "existing_sources_preserved": not edits,
            "client_source_unchanged": "client.py" not in edits,
            "legacy_contract_preserved": not drift,
            "changed_legacy_requests": drift,
            "new_report_supported": True,
        })

    print(json.dumps({
        "python": platform.python_version(),
        "legacy_cases": list(LEGACY_REQUESTS),
        "baseline_rejects_new_report": True,
        "cases": results,
    }, indent=2))


if __name__ == "__main__":
    main()
