#!/usr/bin/env python3
"""Classical reduction on six issue-derived PRELOCKED forecasts.
Use only after pinned native Go independently confirms outcomes. These
explanatory baselines are NOT novel mathematical laws or unbiased predictions.
"""
import json,sys,hashlib
from pathlib import Path
def plain_method_literal_model(x):
    # A deliberately source-oblivious model: no optional HEAD fallback and
    # colon paths treated as ordinary literals (not parser source tokens).
    return {
      "E-HEAD-DEFAULT":"HEAD_405",
      "E-HEAD-OPTIN":"HEAD_405",
      "E-HEAD-EXPLICIT":"EXPLICIT_HEAD_PRIORITY",
      "G-VERB-BARE":"BOTH_REGISTER_AND_SERVE",
      "G-VERB-ESCAPED":"BOTH_REGISTER_AND_SERVE",
      "G-STATIC-CONTROL":"BOTH_REGISTER_AND_SERVE",
    }[x]
def classical_guarded_source_model(x):
    # From Echo's HEAD method resolution and Gin's AST wildcard grammar.
    # Re-expressible as standard guarded transition / CSP relations.
    return {
      "E-HEAD-DEFAULT":"HEAD_405",
      "E-HEAD-OPTIN":"HEAD_200_EMPTY_GET_EXECUTES",
      "E-HEAD-EXPLICIT":"EXPLICIT_HEAD_PRIORITY",
      "G-VERB-BARE":"SECOND_REGISTRATION_PANICS",
      "G-VERB-ESCAPED":"BOTH_REGISTER_AND_SERVE",
      "G-STATIC-CONTROL":"BOTH_REGISTER_AND_SERVE",
    }[x]
def main():
    if len(sys.argv)!=3:
        raise SystemExit("usage p5_classical_reduction.py prereg.json receipt.json")
    infile,outfile=map(Path,sys.argv[1:])
    m=json.loads(infile.read_text())
    assert m["contract"]=="P40_MATH_B_P5_ISSUE_DERIVED_PREREG_V1"
    decided=[x for x in m["cases"] if x["forecast"]!="ABSTAIN"]
    unknown=[x for x in m["cases"] if x["forecast"]=="ABSTAIN"]
    assert len(decided)==6 and len(unknown)==2
    scores={}
    for label,fn in [
      ("source_oblivious_method_and_literal",plain_method_literal_model),
      ("classical_implementation_aware_CSP",classical_guarded_source_model),
    ]:
        details=[{"id":x["id"],"locked":x["forecast"],"prediction":fn(x["id"]),
                  "match":x["forecast"]==fn(x["id"])} for x in decided]
        scores[label]={"correct":sum(x["match"] for x in details),"total":6,"cases":details}
    assert scores["source_oblivious_method_and_literal"]["correct"]==4
    assert scores["classical_implementation_aware_CSP"]["correct"]==6
    result={
      "protocol":"P40_P5_CLASSICAL_REDUCTION_V1",
      "frozen_manifest_sha256":hashlib.sha256(infile.read_bytes()).hexdigest(),
      "native_original_source_success_run":38052099200,
      "prospective_score_limit":"6 locked issue-derived holdouts only. 2 declared unknowns excluded.",
      "epistemic_limit":"CSP encoding repeats the same pinned source mechanisms as the successful forecast; not an independent prediction algorithm or demonstrated theoretical novelty.",
      "scores":scores,"abstentions":[x["id"] for x in unknown]
    }
    outfile.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("P40_P5_CLASSICAL_CSP_EXPLAINS_6_OF_6_ISSUE_DERIVED_OUTCOMES",[(k,v["correct"]) for k,v in scores.items()])
if __name__=="__main__":
    main()
