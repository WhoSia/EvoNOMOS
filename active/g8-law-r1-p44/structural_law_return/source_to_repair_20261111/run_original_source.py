"""Enumerate whole explicitly bounded repair grammar on actual pinned upstream Go source.

All candidates produce an immutable JSON receipt. No generated patch is pushed
to go-chi/chi. Does not simulate real independently acting maintainers.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time
from mutate import OPS,apply

EXPECTED={"live":"ad9a2fbc0a30a39475f746068e74e2d3e6c93999",
          "snapshot":"e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75"}
COMMIT="67be7d9cafdaeb4e04e887ff78d09e030ee43b00"

def execute(args,cwd,timeout=180):
    try:
        p=subprocess.run(args,cwd=cwd,text=True,capture_output=True,timeout=timeout)
        return {"success":p.returncode==0,"returncode":p.returncode,
                "tail":(p.stdout+"\n"+p.stderr)[-2200:]}
    except subprocess.TimeoutExpired:
        return {"success":False,"returncode":None,"tail":"TIMEOUT"}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo-root",type=Path,required=True)
    parser.add_argument("--upstream",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    source=args.repo_root
    orig=args.upstream
    assert execute(["git","rev-parse","HEAD"],orig)["success"]
    commit=subprocess.check_output(["git","rev-parse","HEAD"],cwd=orig,text=True).strip()
    assert commit==COMMIT,(commit,COMMIT)
    results=[]
    for arm in ("live","snapshot"):
        arm_file=source/"tools/p35-p7/arms"/arm/"route_headers.go"
        assert subprocess.check_output(["git","hash-object",str(arm_file)],text=True).strip()==EXPECTED[arm]
        for op in OPS:
            target=orig/"middleware/route_headers.go"
            shutil.copyfile(arm_file,target)
            for old in ("p35_p7_common_test.go","p35_p7_modes_test.go"):
                shutil.copyfile(source/"tools/p35-p7/tests"/old,orig/"middleware"/old)
            shutil.copyfile(source/"active/g8-law-r1-p44/structural_law_return/p35_p7_future_issue1247/evo_issue1247_future_contract_test.go",
                            orig/"middleware/evo_issue1247_future_contract_test.go")
            repair=apply(orig,op)
            diff=subprocess.check_output(["git","diff","--numstat","--","middleware/route_headers.go"],cwd=orig,text=True)
            observed={"arm":arm,"operation":op,"repair":repair,
                      "production_file_changed":bool(diff.strip()),
                      "source_sha256":hashlib.sha256(target.read_bytes()).hexdigest()}
            for key,cmd in (
                ("p35_d0",["go","test","-count=1","-run","^TestP35P7(EmptyRouterExactlyOnce|StableHeaderOrderAndFallback|RouteAny|ConditionalMode)$","./middleware"]),
                ("issue_old",["go","test","-count=1","-run","^TestEvo1247OriginalOldClientContract$","./middleware"]),
                ("issue_new",["go","test","-count=1","-run","^TestEvo1247LaterIndependentDemand$","./middleware"]),
            ):
                observed[key]=execute(cmd,orig)
            if all(observed[k]["success"] for k in ("p35_d0","issue_old","issue_new")):
                observed["full_upstream"]=execute(["go","test","-count=1","./..."],orig,300)
                observed["vet"]=execute(["go","vet","./..."],orig,180)
            else:
                observed["full_upstream"]={"success":None,"reason":"not run when named contracts fail"}
                observed["vet"]={"success":None,"reason":"not run when named contracts fail"}
            observed["accepted"]=all(observed[k]["success"] is True for k in
                                     ("p35_d0","issue_old","issue_new","full_upstream","vet"))
            results.append(observed)
            print("SOURCE_REPAIR",arm,op,
                  "old",observed["issue_old"]["success"],
                  "new",observed["issue_new"]["success"],
                  "accepted",observed["accepted"],flush=True)
    out={"schema":"evonomos-native-source-finite-repair-v1",
         "upstream_commit":COMMIT,
         "declared_grammar":list(OPS),"results":results,
         "semantics":"finite executed Go test oracle, not all-program proof; patch authority is not authenticated owner rights"}
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    assert len(results)==10
    assert any(r["accepted"] for r in results)
    assert not any(r["accepted"] for r in results if r["operation"]=="none")
    print("EVIDENCE_RECEIPT",args.output)
if __name__=="__main__":main()
