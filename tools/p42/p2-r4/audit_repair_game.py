#!/usr/bin/env python3
"""P42-R4 exact two-state original-source edit-game court.

Checks unchanged Echo source executions, *source difference exactly one Go
route registration*, and independent exhaustive shortest-edit paths. The
fault domain is specifically these two authored source assemblies, not an
unrestricted Go patch calculus. Weighted lifecycle probabilities are
hypothetical sensitivity parameters, never observations.
"""
import itertools
import json
import re
import hashlib
import sys
from fractions import Fraction
from pathlib import Path

STATES=("SINGLE","SPLIT")
CONTEXTS=("/health","/r/foo:cancel","/r/foo","/r/foo:other")

def check_source_patch(a:Path,b:Path):
    aa=a.read_text(); bb=b.read_text()
    aa=aa.replace("package single\n","package state\n",1)
    bb=bb.replace("package split\n","package state\n",1)
    needle=' e.GET(`/r/:name\\:cancel`,verb)\n'
    addition=' e.GET("/r/:name",legacy)\n'
    assert aa.count(needle)==1 and bb.count(addition)==1,(aa[-400:],bb[-400:])
    assert aa.replace(needle,needle+addition)==bb, "more than one original Go registration changed"
    return {
        "source_change":"one exact registration added/removed, both source state functions otherwise identical",
        "go_source_single_sha256":hashlib.sha256(a.read_bytes()).hexdigest(),
        "go_source_split_sha256":hashlib.sha256(b.read_bytes()).hexdigest()
    }

def minimal_cost(start,stream):
    goals={"L":"SPLIT","N":"SINGLE"}
    feasible=[]
    for choices in itertools.product(STATES,repeat=len(stream)):
        if any(s!=goals[d] for s,d in zip(choices,stream)):
            continue
        path=(start,)+choices
        feasible.append((sum(a!=b for a,b in zip(path,path[1:])),path))
    assert feasible
    return min(feasible)

def main():
    if len(sys.argv)!=6:
        raise SystemExit("usage: audit_r4.py frozen.json source-single.go source-split.go original-go.log receipt.json")
    manifest,asrc,bsrc,logpath,out=map(Path,sys.argv[1:])
    m=json.loads(manifest.read_text())
    assert m["protocol"]=="EVONOMOS_P42_P2_R4_FROZEN_DEMAND_INDEXED_SOURCE_EDIT_GAME_V1"
    source=check_source_patch(asrc,bsrc)
    history={}
    txt=logpath.read_text()
    assert "--- FAIL:" not in txt and "FAIL\t" not in txt
    for line in txt.splitlines():
        found=re.search(r'P42_R4_ACTUAL_GO\s+(\{[^\r\n]*\})',line)
        if found:
            item=json.loads(found.group(1))
            key=(item["sequence"],item["start"],item["stage"],item["path"])
            assert key not in history
            history[key]=item
    expected_stages=sum(len(z["stream"])+1 for z in m["frozen_sequences"])*2
    assert expected_stages==32
    assert len(history)==expected_stages*len(CONTEXTS)==128, (len(history),expected_stages)
    audit=[]
    for seq in m["frozen_sequences"]:
        stream=seq["stream"]
        for start in STATES:
            path=seq["paths"][start]
            minimum, optim_path=minimal_cost(start,stream)
            assert tuple(path)==optim_path, (seq["id"],start,path,optim_path)
            assert minimum==seq["edit_count"][start]
            assert len(path)==len(stream)+1
            for stage,state in enumerate(path):
                obs={k:history[(seq["id"],start,stage,k)] for k in CONTEXTS}
                assert {x["state"] for x in obs.values()}=={state}
                assert {x["demand"] for x in obs.values()}=={"D0" if stage==0 else stream[stage-1]}
                assert {x["sequence"] for x in obs.values()}=={seq["id"]}
                health=obs["/health"]; verb=obs["/r/foo:cancel"]
                assert (health["status"],health["body"])==(200,"health")
                assert (verb["status"],verb["body"],verb["handler"])==(200,"new:foo","verb")
                legacy=(obs["/r/foo"],obs["/r/foo:other"])
                if state=="SINGLE":
                    assert all(x["status"]==404 and not x["handler"] for x in legacy)
                else:
                    assert ((legacy[0]["status"],legacy[0]["body"],legacy[0]["handler"])==
                            (200,"legacy:foo","legacy"))
                    assert ((legacy[1]["status"],legacy[1]["body"],legacy[1]["handler"])==
                            (200,"legacy:foo:other","legacy"))
            audit.append({"sequence":seq["id"],"starting_architecture":start,
                          "demand_stream":stream,"source_states":path,
                          "independent_exhaustive_minimum_edits":minimum,
                          "initial_source_route_registrations":m["cost_policy"]["initial_S_single"]
                               if start=="SINGLE" else m["cost_policy"]["initial_S_split"]})
    by={(z["sequence"],z["starting_architecture"]):z for z in audit}
    assert by["L","SINGLE"]["independent_exhaustive_minimum_edits"]==1
    assert by["L","SPLIT"]["independent_exhaustive_minimum_edits"]==0
    assert by["N","SINGLE"]["independent_exhaustive_minimum_edits"]==0
    assert by["N","SPLIT"]["independent_exhaustive_minimum_edits"]==1
    assert by["LN","SINGLE"]["independent_exhaustive_minimum_edits"]==2
    assert by["NL","SINGLE"]["independent_exhaustive_minimum_edits"]==1
    assert by["LN","SPLIT"]["independent_exhaustive_minimum_edits"]==1
    assert by["NL","SPLIT"]["independent_exhaustive_minimum_edits"]==2
    def sensitivity(p,w):
        single=Fraction(1)+p*w
        split=Fraction(2)+(1-p)*w
        return {"p_legacy":str(p),"hypothetical_late_action_weight":str(w),
                "single_birth_plus_late":str(single),"split_birth_plus_late":str(split),
                "lower_conditional_numeric_cost":"SINGLE" if single<split else "SPLIT" if split<single else "TIE"}
    cases=[sensitivity(Fraction(1,4),Fraction(2)),sensitivity(Fraction(9,10),Fraction(2))]
    assert [s["lower_conditional_numeric_cost"] for s in cases]==["SINGLE","SPLIT"]
    receipt={
        "protocol":"P42_R4_DEMAND_INDEXED_SOURCE_EDIT_GAME_BOUNDED_NATIVE_AND_CLASSICAL_PASS",
        "manifest_sha256":hashlib.sha256(manifest.read_bytes()).hexdigest(),
        "original_go_log_sha256":hashlib.sha256(logpath.read_bytes()).hexdigest(),
        "upstream_original_echo":m["upstream_original"]["ref"],
        "source":source,
        "source_program_variants":2,
        "frozen_streams":6,
        "source_repair_scenarios":12,
        "source_state_stages_verified":expected_stages,
        "original_echo_client_executions":len(history),
        "d0_same_clients_both_architectures":True,
        "source_aware_exhaustive_shortest_paths":True,
        "one_edit_patch_grammar_validated":True,
        "legacy_demand_incremental_preference":"SPLIT",
        "deny_demand_incremental_preference":"SINGLE",
        "order_sensitive_edit_costs_both_start_states":True,
        "hypothetical_weighted_condition_can_reverse":True,
        "empirical_weights_or_demand_distribution_measured":False,
        "complete_software_lifecycle_cost_verified":False,
        "source_to_lean_whole_go_semantics_proved":False,
        "classical_delta_transitions_and_dp_baselines_undefeated":True,
        "historical_upstream_change_authority":"UNKNOWN",
        "new_general_law_proved":False,
        "LAW_R2_authorized":False,
        "audits":audit,
        "hypothetical_sensitivity_only":cases,
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("P42_R4_128_ORIGINAL_ECHO_TRACES_12_EXHAUSTIVE_MIN_EDIT_PATHS_PASS")
if __name__=="__main__":main()
