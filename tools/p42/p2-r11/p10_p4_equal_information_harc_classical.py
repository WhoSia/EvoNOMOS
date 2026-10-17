#!/usr/bin/env python3
"""P10-P4 fair information-matched HARC versus classical edit LTS.

Both arms receive the SAME (1) parsed pinned source evidence, (2) old
and one-handler-repair native tests, (3) research-owned handler edit
grammar, (4) synthetic cost vector. Do not promote a 2-case tie into
mathematical novelty or a proof of correctness for unobserved clients.
"""
import argparse
import json
from pathlib import Path

TARGETS = {"gin-gonic/gin": "NO_PANIC", "labstack/echo": "PANIC"}
GOALS = ("NO_PANIC", "PANIC")
BASELINES = {
    "gin-gonic/gin": "GIN_P10_NATIVE: oldGET=200/old, noFlush=NO_PANIC, flushSupported=NO_PANIC",
    "labstack/echo": "ECHO_P10_NATIVE: oldGET=200/old, noFlush=PANIC, flushSupported=NO_PANIC",
}
REPAIRS = {
    "gin-gonic/gin": "P10_GIN_ONE_HANDLER_REPAIR oldGET200 failFastNoFlusher=true withFlusher=PASS",
    "labstack/echo": "P10_ECHO_ONE_HANDLER_REPAIR oldGET200 gracefulNoFlusher=true withFlusher=PASS",
}

def static_forecast(source):
    """Syntax-only hypothesis: never a proof about underlying operation."""
    gin = (source["flush_ast_type_assert_http_flusher"]
           and not source["flush_ast_calls_http_new_response_controller"]
           and not source["flush_ast_has_panic_call"])
    echo = (not source["flush_ast_type_assert_http_flusher"]
            and source["flush_ast_calls_http_new_response_controller"]
            and source["flush_ast_has_panic_call"])
    if gin:
        return "NO_PANIC"
    if echo:
        return "PANIC"
    return "ABSTAIN"

def harc_quotient(inputs, demanded):
    if not inputs["native_verified"] or not inputs["research_handler_right"]:
        return "ABSTAIN"
    baseline = inputs["baseline"]
    repaired = inputs["repair"]
    if baseline == demanded:
        return [[0, 0]]
    if repaired != demanded:
        return []
    return [[1, 1]]

def classical_costed_lts(inputs, demanded):
    if not inputs["native_verified"] or not inputs["research_handler_right"]:
        return "ABSTAIN"
    # Exact same state/rights/observed contracts as HARC: no hidden data.
    # Explicit graph reachability instead of the HARC quotient shortcut.
    nodes = {"original": inputs["baseline"], "one_owned_handler_edit": inputs["repair"]}
    outgoing = {"original": [("one_owned_handler_edit", (1,1))],
                "one_owned_handler_edit": []}
    found = []
    stack = [("original", (0,0), frozenset(["original"]))]
    while stack:
        state, cost, visited = stack.pop()
        if nodes[state] == demanded:
            found.append(cost)
        for successor,delta in outgoing[state]:
            if successor not in visited:
                stack.append((successor, tuple(a+b for a,b in zip(cost,delta)),
                              visited | {successor}))
    if not found:
        return []
    return [list(v) for v in sorted(set(found)) if not any(
        all(o<=w for o,w in zip(other,v)) and any(o<w for o,w in zip(other,v))
        for other in found)]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--evidence", required=True)
    p.add_argument("--gin-baseline", required=True)
    p.add_argument("--echo-baseline", required=True)
    p.add_argument("--gin-repair", required=True)
    p.add_argument("--echo-repair", required=True)
    p.add_argument("--out", required=True)
    a = p.parse_args()
    manifest = json.loads(Path(a.evidence).read_text())
    sources = {x["repository"]:x for x in manifest["sources"]}
    assert set(sources)==set(TARGETS)
    logs = {
        "gin-gonic/gin":(Path(a.gin_baseline).read_text(), Path(a.gin_repair).read_text()),
        "labstack/echo":(Path(a.echo_baseline).read_text(), Path(a.echo_repair).read_text())
    }
    cases = []
    for repo in sorted(TARGETS):
        src = sources[repo]
        assert src["old_client_semantics"] == "UNKNOWN_UNTIL_INDEPENDENT_NATIVE_TEST"
        assert src["upstream_source_edit_authority"] == "UNKNOWN"
        assert src["human_edit_cost"] == "UNKNOWN"
        assert src["declares_flush"] and src["declares_unwrap"]
        syntactic_prediction = static_forecast(src)
        assert syntactic_prediction == TARGETS[repo], ("static syntax mismatch", repo)
        original_log, repair_log = logs[repo]
        assert BASELINES[repo] in original_log and "--- PASS: TestEvoNOMOS" in original_log
        assert REPAIRS[repo] in repair_log and "--- PASS: TestEvoNOMOS" in repair_log
        inputs = {"baseline": syntactic_prediction,
                  "repair": "PANIC" if syntactic_prediction=="NO_PANIC" else "NO_PANIC",
                  "native_verified": True, "research_handler_right": True,
                  "human_cost_observed": False}
        for demanded in GOALS:
            h=harc_quotient(inputs,demanded)
            c=classical_costed_lts(inputs,demanded)
            assert h==c,(repo,demanded,h,c)
            cases.append({"repository":repo,"demand":demanded,"harc_cost_frontier":h,
                          "classical_cost_frontier":c,"equal_information":True,
                          "cost_units":"research-authored handler change count, synthetic review unit"})
        no_right=dict(inputs,research_handler_right=False)
        for d in GOALS:
            assert harc_quotient(no_right,d)=="ABSTAIN"
            assert classical_costed_lts(no_right,d)=="ABSTAIN"
    assert len(cases)==4
    output={
      "status":"PASS_INFORMATION_MATCHED_TIE_BOUNDED_FOUR_SOURCE_CONTRACT_CASES",
      "cases":cases,"n_cases":len(cases),"both_correct_against_tested_native_cases":True,
      "harc_unique_wins":0,"classic_unique_wins":0,"ties":len(cases),
      "original_source_authority":"UNKNOWN; NOT ASSUMED BY EITHER ARM",
      "research_owned_handler_authority":"declared only for authored experiment",
      "human_cost":"UNOBSERVED","all_old_clients_certified":False,
      "source_evidence_strength":"AST static syntax plus named original Go source native tests; no general compiler-derived source semantics proof",
      "pr_future_holdout_ranking":"NOT EVALUATED BY THIS COURT",
      "novel_design_law":"NOT_PROVEN",
      "gates":"P42 RUNNING; R11-P10-P4; P43 HOLD; LAW-R2 NOT_AUTHORIZED"
    }
    out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n")
    print(output["status"])
    print("HARC_CLASSICAL_TIE_4_OF_4__SOURCE_RIGHTS_UNKNOWN_OUTSIDE_LAB")
    print(json.dumps(cases,sort_keys=True))

if __name__=="__main__":
    main()
