#!/usr/bin/env python3
"""R11-P1 bounded byte-exact provenance, original-Go native, and edit-path audit."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P=ROOT/"frozen_p1_independent_milvus_provider_typed_source_paths.json"
N=ROOT.parent/"p2-r11-native"
def main():
    if len(sys.argv)!=5:raise SystemExit("usage: verify_p1.py ORIGINAL_MILVUS_SOURCE NATIVE_LOG NEGATIVE_COMPILE_LOG OUT_JSON")
    origin,logs,invalid,out=map(Path,sys.argv[1:])
    p=json.loads(P.read_text())
    names={x["name"]:x for x in p["milestones"]}
    actual={m.group(1):(m.group(2)=="true") for m in re.finditer(r"R11_P1_STATE id=(\w+) old=true future=(true|false)",logs.read_text())}
    if set(actual)!={"direct","guard_prepared","guard_selected"}:raise ValueError("Native Go missing a presealed old/future source state "+str(actual))
    if "R11_P1_EXTERNAL_MILVUS_ORIGINAL_SOURCE_WITH_GRPC_2024_PASS" not in logs.read_text():
        raise ValueError("missing native original grpc Milvus proof")
    if "undefined: writeZeroed" not in invalid.read_text():
        raise ValueError("expected root-first wrong-order compile rejection missing")
    status={}
    paths=[]
    byname={}
    for k,v in names.items():
        folder=N/("states" if v["build"] else "invalid")/k
        f={q.name:q.read_bytes() for q in folder.glob("*.go") if q.name!="checkpoint_test.go"}
        if f["codec_buffer_pool.go"]!=origin.read_bytes():
            raise ValueError("Milvus original source modified at "+k)
        if v["build"] and actual[k]!=v["new"]:
            raise ValueError("new contract preregistered prediction mismatch "+k)
        status[k]={"build":v["build"],"old":v["old"],"future":v["new"]}
        byname[k]=f
    for r in p["paths"]:
        diffs=[]
        for before,after in zip(r["states"],r["states"][1:]):
            a,b=byname[before],byname[after]
            touched=sorted(k for k in set(a)|set(b) if a.get(k)!=b.get(k))
            if len(touched)!=1 or touched[0]=="codec_buffer_pool.go":
                raise ValueError("source edited outside synthetic one-file right "+r["name"]+" "+str(touched))
            diffs.append(touched[0])
        okay=all(names[s]["build"] and names[s]["old"] for s in r["states"]) and names[r["states"][-1]]["new"]
        if okay!=r["safe"]:raise ValueError("route safe outcome mismatch "+r["name"])
        paths.append({"name":r["name"],"safe":okay,"source_edits":diffs,"endpoint_new":names[r["states"][-1]]["new"]})
        print(f"R11_P1_PATH name={r['name']} safe={str(okay).lower()} edits={','.join(diffs)}")
    out.write_text(json.dumps({"verdict":"R11_P1_BOUNDED_EXTERNAL_MILVUS_SOURCE_GO_NATIVE_PASS","caveat":"External real provider byte-exact; consumer oracles and disjoint-path authority are researcher-authored; no independently compiled maintained client or new general theorem","states":status,"paths":paths},indent=2)+"\n")
    print("R11_P1_THREE_EXTERNAL_PROVIDER_GO_STATES_ONE_COMPILER_NEGATIVE_AND_TYPED_PATHS_PASS")
if __name__=="__main__":main()
