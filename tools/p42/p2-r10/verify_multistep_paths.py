#!/usr/bin/env python3
"""P42 R10-P3 finite, source-grounded, equal-information transition court.

Observations from 2024 native Go are checked against predictions derived from
the old source and each generated Go patch. The path acceptance decision uses
*every intermediate source state*, not endpoint-only adequacy.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from source_region_classical_audit import parse_real_grpc_library,predict

FROZEN=HERE/"frozen_p3_multistep_source_repair_paths.json"
SOURCE=HERE.parent/"p2-r10-native"/"paths"

def old_obs(result:dict,size:int)->bool:
    if size==1024:return result["first"]==65 and result["puts"]==0
    if size==2048:return result["puts"]==2
    raise AssertionError("unexpected size")

def content_files(node:dict)->dict[str,str]:
    basedir=SOURCE/("states" if node["compile"] else "invalid")/node["id"]
    return {f.name:f.read_text() for f in basedir.glob("*.go") if f.name!="checkpoint_test.go"}

def main()->None:
    if len(sys.argv)!=5:raise SystemExit("usage: verify_paths.py ORIGINAL_GRPC GO_LOG NEGATIVE_COMPILE_LOG OUT_JSON")
    grpc,logfile,badfile,outfile=map(Path,sys.argv[1:])
    manifest=json.loads(FROZEN.read_text())
    assert manifest["protocol"]=="EVONOMOS_P42_P2_R10_P3_SOURCE_LIFETIME_PATH_COMPOSITION_PRESEAL_V1"
    threshold=parse_real_grpc_library(grpc)
    assert threshold==1024
    lines=logfile.read_text()
    re_state=re.compile(r"R10_P3_STATE id=([a-z_]+) small=(\d+) small_puts=(\d+) large=(\d+) large_puts=(\d+)")
    native={m[1]:{"small":[int(m[2]),int(m[3])],"large":[int(m[4]),int(m[5])]}
            for m in re_state.finditer(lines)}
    negative=badfile.read_text()
    if "undefined: legacyPool" not in negative and "undefined: legacyAdapter" not in negative:
        raise AssertionError("expected original-Go compiler rejection of wrong edit order not found")
    nodes={}
    generated={}
    for n in manifest["nodes"]:
        ident=n["id"]
        files=content_files(n)
        generated[ident]=files
        if n["compile"]:
            directory=SOURCE/"states"/ident
            actual={"small":predict(grpc,directory,threshold,1024),
                    "large":predict(grpc,directory,threshold,2048)}
            pred={"small":[actual["small"]["first"],actual["small"]["puts"]],
                  "large":[actual["large"]["first"],actual["large"]["puts"]]}
            if pred!=n["expected"] or native.get(ident)!=pred:
                raise AssertionError("preseal/source/native disagreement for "+ident+":"+str(pred)+"/"+str(native.get(ident)))
            observed_old=old_obs(actual["small"],1024) and old_obs(actual["large"],2048)
            observed_future=actual["large"]["first"]==65
            if (observed_old,observed_future)!=(n["old"],n["future"]):
                raise AssertionError("bad predeclared per-state invariant "+ident)
        else:
            if ident in native:raise AssertionError("negative expected-to-fail source unexpectedly appeared in native successes")
            observed_old=False;observed_future=False
        nodes[ident]={"compiles":n["compile"],"old":observed_old,"future":observed_future}
        print(f"R10_P3_NODE id={ident} compiles={str(n['compile']).lower()} old={str(observed_old).lower()} future={str(observed_future).lower()}")

    receipts=[]
    for route in manifest["paths"]:
        names=route["nodes"]
        steps=[]
        for a,b in zip(names,names[1:]):
            delta=sorted(p for p in set(generated[a])|set(generated[b]) if generated[a].get(p)!=generated[b].get(p))
            if len(delta)!=1:raise AssertionError(f"route {route['id']} non-atomic source edit {a} -> {b}: {delta}")
            steps.append({"from":a,"to":b,"edited_authored_source_path":delta[0]})
        old_preserved=all(nodes[n]["compiles"] and nodes[n]["old"] for n in names)
        endpoint=nodes[names[-1]]["compiles"] and nodes[names[-1]]["future"]
        safe_path=old_preserved and endpoint
        if (safe_path,endpoint)!=(route["valid"],route["endpoint"]):
            raise AssertionError("path prereg/source/native disagree for "+route["id"])
        receipt={"id":route["id"],"path":names,"edges":steps,
                 "compiles_and_preserves_original_at_every_step":old_preserved,
                 "terminal_future_demand":endpoint,"safe_repair_path":safe_path}
        receipts.append(receipt)
        print(f"R10_P3_PATH id={route['id']} valid={str(safe_path).lower()} endpoint={str(endpoint).lower()} steps={len(steps)}")
    a=next(x for x in receipts if x["id"]=="adapter_first_valid")
    b=next(x for x in receipts if x["id"]=="nop_detour_endpoint_same")
    c=next(x for x in receipts if x["id"]=="root_first_compile_break")
    if not(a["safe_repair_path"] and not b["safe_repair_path"] and not c["safe_repair_path"]):
        raise AssertionError("path-sensitive differential counterexamples not recovered")
    if a["path"][-1]!=b["path"][-1] or a["path"][-1]!=c["path"][-1]:
        raise AssertionError("endpoint same-source counterexample lost")
    output={"result":"P42_P2_R10_P3_BOUNDED_SEMANTIC_PATH_COURT_PASS",
            "original_grpc_sha":manifest["original_grpc_sha"],
            "go_valid_node_observations":len(native),"preregistered_paths":len(receipts),
            "valid_paths":sum(x["safe_repair_path"] for x in receipts),
            "identical_endpoint_but_different_admissibility":True,
            "nonclaims":["Classical finite transition-system logic suffices","Not full-Go semantic composition theorem","Not historical multi-commit replay","No actual historical owner authority"],
            "nodes":nodes,"paths":receipts}
    outfile.write_text(json.dumps(output,indent=2)+"\n")
    print("R10_P3_SIX_PATHS_SAME_ENDPOINT_DIFFERENT_PREFIX_SAFETY_CLASSICAL_PASS")

if __name__=="__main__":main()
