"""Contract-scope sensitivity on real original upstream and prior Oct9 source variants.

Researcher-designed observed direct NewPattern semantics, not upstream API promise.
All 5 x 2 candidates, frozen. Independent CI receipts, no upstream writes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

from mutate import OPS,apply
from run_original_source import COMMIT,EXPECTED,execute

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repo-root",required=True,type=Path)
    p.add_argument("--upstream",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    a=p.parse_args()
    root=a.repo_root
    upstream=a.upstream
    actual=subprocess.check_output(["git","rev-parse","HEAD"],text=True,cwd=upstream).strip()
    if actual!=COMMIT:raise ValueError("original upstream source changed")
    out=[]
    for arm in ("live","snapshot"):
        f=root/"tools/p35-p7/arms"/arm/"route_headers.go"
        if subprocess.check_output(["git","hash-object",str(f)],text=True).strip()!=EXPECTED[arm]:
            raise ValueError("historical arm source changed")
        for op in OPS:
            shutil.copyfile(f,upstream/"middleware/route_headers.go")
            for name in ("p35_p7_common_test.go","p35_p7_modes_test.go"):
                shutil.copyfile(root/"tools/p35-p7/tests"/name,upstream/"middleware"/name)
            local=root/"active/g8-law-r1-p44/structural_law_return/source_to_repair_20261111"
            for name in ("evo_direct_legacy_contract_test.go",):
                shutil.copyfile(local/name,upstream/"middleware"/name)
            shutil.copyfile(root/"active/g8-law-r1-p44/structural_law_return/p35_p7_future_issue1247/evo_issue1247_future_contract_test.go",
                            upstream/"middleware/evo_issue1247_future_contract_test.go")
            shape=apply(upstream,op)
            datum={"arm":arm,"operator":op,"sites":shape["sites"],
                   "source_sha256":hashlib.sha256((upstream/"middleware/route_headers.go").read_bytes()).hexdigest()}
            for label,filter in (
                ("p35_baseline","^TestP35P7(EmptyRouterExactlyOnce|StableHeaderOrderAndFallback|RouteAny|ConditionalMode)$"),
                ("route_old","^TestEvo1247OriginalOldClientContract$"),
                ("route_new","^TestEvo1247LaterIndependentDemand$"),
                ("direct_legacy","^TestEvoP44DirectLegacyPatternContract$")
            ):
                datum[label]=execute(["go","test","-count=1","-run",filter,"./middleware"],upstream)
            if all(datum[k]["success"] for k in ("p35_baseline","route_old","route_new","direct_legacy")):
                datum["upstream"]=execute(["go","test","-count=1","./..."],upstream,300)
                datum["vet"]=execute(["go","vet","./..."],upstream,180)
            else:
                datum["upstream"]={"success":None,"reason":"not executed on failed named contract"}
                datum["vet"]={"success":None,"reason":"not executed on failed named contract"}
            datum["accepted"]=all(datum[k]["success"] is True for k in
                                  ("p35_baseline","route_old","route_new","direct_legacy","upstream","vet"))
            out.append(datum)
            print("DIRECT_SCOPE",arm,op,"route_new",datum["route_new"]["success"],
                  "direct_legacy",datum["direct_legacy"]["success"],
                  "accepted",datum["accepted"],flush=True)
    if len(out)!=10:raise AssertionError("incomplete enumeration")
    result={"schema":"evonomos-source-contract-scope-v1","original_upstream":COMMIT,
            "author_defined_direct_legacy_observational_contract":True,
            "not_upstream_documented_promise":True,"grammar":list(OPS),"results":out,
            "scope":"native Go tests within finite grammar; not complete semantic proof, not actual edit rights"}
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    for arm in ("live","snapshot"):
        accepted={x["operator"] for x in out if x["arm"]==arm and x["accepted"]}
        if accepted!={"route_both"}:
            raise AssertionError("frozen prediction falsified for "+arm+":"+repr(accepted))
if __name__=="__main__":
    main()
