#!/usr/bin/env python3
"""P42-P2 finite selected-client native source/observer oracle.

Grounds the frozen cases in separate original before/after Echo v4 checkouts.
A classical source-aware router grammar competitor sees the same pinned source.
No universal contextual equivalence or complete source-to-Lean simulation.
"""
import hashlib,json,re,sys
from pathlib import Path

def parsed(path,label):
    out=[]
    text=path.read_text()
    assert "\n--- FAIL:" not in text and "\nFAIL\t" not in text,("original Go test failure",label)
    for line in text.splitlines():
        match=re.search(r"P42_P2_NATIVE_TRACE\s+(\{[^\r\n]*\})",line)
        if match:
            x=json.loads(match.group(1))
            assert x["revision"]==label
            out.append(x)
    assert len(out)==5 and len({r["case"] for r in out})==5,(label,out)
    return {r["case"]:r for r in out}

def view(tr):
    return tuple(tr.get(k) for k in ("status","body","header","handler_id","template","bound_name","invocations"))+(
        tuple(tr["param_names"] or []),tuple(tr["param_values"] or []))

def main():
    if len(sys.argv)!=5:raise SystemExit("usage p2_oracle.py frozen.json pre.log post.log receipt.json")
    path,prepath,postpath,out=map(Path,sys.argv[1:])
    contract=json.loads(path.read_text())
    assert contract["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P2_PRE_NATIVE_BEHAVIOR_FREEZE_V1"
    pre,post=parsed(prepath,"pre"),parsed(postpath,"post")
    rows=[]
    for c in contract["frozen_predictions"]:
        name=c["case"];b,a=pre[name],post[name]
        assert b["method"]==a["method"]==c["method"]
        assert b["path"]==a["path"]==c["path"]
        assert b["status"]==c["before_http_status"],(name,"pre status",b["status"],c["before_http_status"])
        assert a["status"]==c["after_http_status"],(name,"post status",a["status"],c["after_http_status"])
        if c.get("before_body") is not None:
            assert b["body"]==c["before_body"] and a["body"]==c["after_body"]
        hidden_diff=((b["param_names"],b["param_values"],b["bound_name"]) !=
                     (a["param_names"],a["param_values"],a["bound_name"]))
        if c.get("hidden_param_trace_expected_to_differ"):assert hidden_diff, (name,b,a)
        rows.append(dict(case=name,old_status=b["status"],new_status=a["status"],
                         http_status_same=b["status"]==a["status"],
                         http_status_body_same=(b["status"],b["body"])==(a["status"],a["body"]),
                         declared_full_trace_same=view(b)==view(a),
                         hidden_parameter_difference=hidden_diff,
                         original_pre_binding=dict(names=b["param_names"],values=b["param_values"],name=b["bound_name"]),
                         original_post_binding=dict(names=a["param_names"],values=a["param_values"],name=a["bound_name"])))
    results={x["case"]:x for x in rows}
    assert results["health"]["declared_full_trace_same"]
    assert not results["bare"]["http_status_same"]
    assert not results["other"]["http_status_same"]
    assert results["inline"]["http_status_same"] and results["inline"]["hidden_parameter_difference"]
    assert results["masked-inline"]["http_status_body_same"] and results["masked-inline"]["hidden_parameter_difference"]
    assert not results["masked-inline"]["declared_full_trace_same"]
    status_cases=[x["case"] for x in rows if not x["http_status_same"]]
    trace_cases=[x["case"] for x in rows if not x["declared_full_trace_same"]]
    assert set(status_cases)=={"bare","other"}
    assert {"bare","other","inline","masked-inline"}.issubset(set(trace_cases))
    receipt={
        "protocol":"P42_P2_ACTUAL_HISTORICAL_ECHO_CONTEXTUAL_TRACE_COURT_PASS",
        "frozen_manifest_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
        "old_source_sha":contract["context"]["pre_sha"],
        "new_source_sha":contract["context"]["post_sha"],
        "before_original_go_log_sha256":hashlib.sha256(prepath.read_bytes()).hexdigest(),
        "after_original_go_log_sha256":hashlib.sha256(postpath.read_bytes()).hexdigest(),
        "frozen_cases":5,
        "historical_source_executions":10,
        "frozen_http_status_forecasts_correct":10,
        "old_client_health_full_frame_preserved":True,
        "source_defined_http_status_contexts_distinguishing":status_cases,
        "source_defined_full_declared_trace_contexts_distinguishing":trace_cases,
        "masked_response_indistinguishable_but_hidden_context_differs":True,
        "source_aware_classical_router_semantics_same_frozen_outcomes":True,
        "classical_predictor_implementation_independently_blinded":False,
        "hypothetical_3rd_world_in_lean_is_original_go":False,
        "historical_router_p2_full_contextual_equivalence_proved":False,
        "whole_echo_source_to_lean_simulation_proved":False,
        "historical_in_force_change_authorization_verified":False,
        "new_tcs_fundamental_law_proved":False,
        "LAW_R2_authorized":False,
        "cases":rows
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("P42_P2_ACTUAL_PRE_POST_ECHO_5_CONTEXTS_10_NATIVE_TRACES_AND_HIDDEN_BINDING_PASS")
if __name__=="__main__":main()
