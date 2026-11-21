"""Retrospective source-impact calibration, with known previously measured Go results.

Runs exact AST tool against all original P35-P7 source variants and the five
previously frozen Go patch operators. No new customer fixture or oracle.
"""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from sys import path as py_path

OPS=("none","constructor","route_both","remove_lookup_lower","match_lower")
EXPECTED_BLOBS={
 "live":"ad9a2fbc0a30a39475f746068e74e2d3e6c93999",
 "snapshot":"e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75"
}
CHANGED={
 "none":[],
 "constructor":["NewPattern"],
 "route_both":["HeaderRouter.Route","HeaderRouter.RouteAny"],
 "remove_lookup_lower":["HeaderRouter.Handler"],
 "match_lower":["Pattern.Match"],
}
# Based on ORIGINAL native Go public direct-legacy oracle #42932257551,
# NOT independently blinded outcome data.
PREVIOUS_NATIVE_DIRECT_CHANGED={"constructor":True,"match_lower":True,
                                 "none":False,"route_both":False,
                                 "remove_lookup_lower":False}
def call(args,**kw):
    p=subprocess.run(args,capture_output=True,text=True,check=True,**kw)
    return p.stdout.strip()
def run(repo,analyzer):
    patch_dir=repo/"active/g8-law-r1-p44/structural_law_return/source_to_repair_20261111"
    import sys
    sys.path.insert(0,str(patch_dir))
    from mutate import apply
    evidence=[]
    for arm in ("live","snapshot"):
        original=repo/"tools/p35-p7/arms"/arm/"route_headers.go"
        blob=call(["git","hash-object",str(original)])
        assert blob==EXPECTED_BLOBS[arm], (arm,blob)
        for op in OPS:
            with tempfile.TemporaryDirectory(prefix="evonomos_footprint_") as td:
                root=Path(td)
                (root/"middleware").mkdir()
                target=root/"middleware/route_headers.go"
                shutil.copyfile(original,target)
                outcome=apply(root,op)
                data=json.loads(call([str(analyzer),"--before",str(original),"--after",str(target)]))
                if data["changed_functions"]!=CHANGED[op]:
                    raise AssertionError((arm,op,data["changed_functions"],CHANGED[op]))
                if data["changed_types"]:
                    raise AssertionError("unexpected type change: "+repr(data["changed_types"]))
                if not data["direct_declared_calls_purity_approved"]:
                    raise AssertionError("direct microclient not in safe subset")
                expected=PREVIOUS_NATIVE_DIRECT_CHANGED[op]
                if data["direct_microclient_may_affect"]!=expected:
                    raise AssertionError("AST impact inconsistent with known Go evidence")
                evidence.append({
                  "arm":arm,"operation":op,
                  "sites":outcome["sites"],
                  "source_blob":blob,
                  "static":data,
                  "known_native_direct_legacy_behavior_changed":expected,
                  "known_native_evidence_run":"https://github.com/WhoSia/EvoNOMOS/actions/runs/42932257551"
                })
                print("SOURCE_FOOTPRINT",arm,op,
                      "file",data["file_baseline_may_affect"],
                      "direct_may",data["direct_microclient_may_affect"],
                      "direct_preserved",data["direct_microclient_definitely_preserved"],
                      flush=True)
    assert len(evidence)==10
    flags=sum(1 for x in evidence if x["static"]["file_baseline_may_affect"])
    bound=sum(1 for x in evidence if x["static"]["direct_microclient_may_affect"])
    observed=sum(1 for x in evidence if x["known_native_direct_legacy_behavior_changed"])
    assert (flags,bound,observed)==(8,4,4)
    return {
      "schema":"evonomos-restricted-go-ast-client-preservation-v1",
      "model":"explicit researcher-specified microclient NewPattern(...).Match(...); no automatic client discovery",
      "known_outcome_reuse":True,
      "blinded_external_future_test":False,
      "original_source_git_blobs_verified":True,
      "candidate_count":10,
      "file_level_may_affect":flags,
      "ast_direct_may_affect":bound,
      "native_direct_cases_with_behavioral_change":observed,
      "limited_direct_preservation_certificates":10-bound,
      "claims_excluded":["general program semantic equivalence","runtime Router behavior preservation",
        "actual owner permissions","novel static slicing technique","out-of-sample prediction",
        "independent actor maintenance costs"],
      "evidence":evidence
    }
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo-root",type=Path,required=True)
    parser.add_argument("--analyzer",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    a=parser.parse_args()
    result=run(a.repo_root.resolve(),a.analyzer.resolve())
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("RESULT:",result["candidate_count"],result["file_level_may_affect"],
          result["ast_direct_may_affect"],result["limited_direct_preservation_certificates"])
