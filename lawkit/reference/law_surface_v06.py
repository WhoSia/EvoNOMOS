#!/usr/bin/env python3
import json,sys
from pathlib import Path

def frac(s):
    a,b=s.split("/",1); a=int(a.strip()); b=int(b.strip())
    if b==0 or a>b: raise ValueError("invalid shared_mechanism_fraction")
    return a,b

def world(env,wid):
    for w in env["evidence"]:
        if w["world_id"]==wid: return w
    raise ValueError("missing evidence world "+wid)

def validate(env):
    p10=world(env,"P10_MIKROTIK")
    o=p10["observed"]
    if not (p10["evidence_class"]=="EXPLORATORY_ONLY" and o["outcomes_opened"] and o["surface_reversal"] is True and o["churn_reversal"] is False):
        raise ValueError("P10 evidence contract mismatch")
    p11=world(env,"P11_TRUEFORGE")
    o=p11["observed"]
    if not (p11["evidence_class"]=="REAL_TWO_DEMAND" and o["outcomes_opened"] and o["surface_discrimination"] is False and o["churn_reversal"] is True and o["capability_burden_reduction"] is True):
        raise ValueError("P11 evidence contract mismatch")
    p12=world(env,"P12_RESTIC")
    if p12["evidence_class"]!="TERMINAL_NONRESULT" or p12["observed"]["outcomes_opened"]:
        raise ValueError("P12 must remain terminal non-result with outcomes closed")

def project(env):
    if env.get("protocol_version")!="0.6": raise ValueError("protocol_version must be 0.6")
    validate(env)
    c=env["prospective_context"]; sn,sd=frac(c["shared_mechanism_fraction"])
    boundary=set(c["boundary_capabilities"]); demand=set(c["demanded_capabilities"])
    extra=sorted(boundary-demand); missing=sorted(demand-boundary)
    if c["existing_boundary"]=="ABSENT" and c["membership_fanout"]>1 and sn>0 and sd>1:
        mp="PRESENT"
    elif c["existing_boundary"]!="ABSENT":
        mp="BOUNDED_BY_EXISTING_BOUNDARY"
    else:
        mp="LIMITED"
    if extra: bm="PRESENT"
    elif boundary and not missing and boundary==demand: bm="ABSENT_FULL_COREQUIREMENT"
    else: bm="ABSENT_OR_NOT_APPLICABLE"
    tests=[]
    if mp=="PRESENT": tests.append("TEST_MEMBERSHIP_CENTRALIZATION_VS_DIRECT")
    if bm=="PRESENT": tests.append("TEST_CAPABILITY_SEGREGATION_VS_BUNDLE_REUSE")
    abst=["NO_ARCHITECTURE_RECOMMENDATION_WITHOUT_PAIRED_LIFECYCLE_EVIDENCE"]
    if c["existing_boundary"]!="ABSENT": abst.append("CIL_C1_MEMBERSHIP_SAVING_NOT_INFERRED_WITH_EXISTING_BOUNDARY")
    if bm=="ABSENT_FULL_COREQUIREMENT": abst.append("CBL_C1_FULL_COREQUIREMENT_CELL_UNRESOLVED")
    if c["future_same_family_demand"]=="UNKNOWN": abst.append("FUTURE_SAME_FAMILY_DEMAND_UNKNOWN")
    if missing: abst.append("CURRENT_BOUNDARY_DOES_NOT_COVER_FROZEN_DEMAND")
    authority="ABSTAIN_INVALID_CAPABILITY_COVERAGE" if missing else ("ABSTAIN_NO_MATCHED_MECHANISM" if not tests else "SELECT_PROSPECTIVE_RIVAL_TESTS_ONLY")
    return {
      "protocol_version":"0.6",
      "authority":"LAW_R1_P0_CONSTITUTION_ONLY",
      "cil_c1_evidence":"EXPLORATORY_MECHANISM_PLUS_BOUNDARY_EVIDENCE__NO_GENERAL_RECOMMENDATION",
      "cbl_c1_evidence":"NARROW_MECHANISM_SUPPORT__FULL_COREQUIREMENT_FALSIFIER_UNRESOLVED",
      "coordinate_noncollapse":True,
      "p12_full_corequirement_cell":"UNRESOLVED_TERMINAL_NONRESULT",
      "context_id":c["context_id"],
      "membership_propagation_pressure":mp,
      "capability_bundle_mismatch":bm,
      "mismatch_width":len(extra),
      "uncovered_demand_capabilities":missing,
      "candidate_tests":tests,
      "abstention_reasons":abst,
      "decision_authority":authority,
      "scalarization":False,
      "winner":None,
      "cil_c1_falsifiers":[
        "PREEXISTING_BOUNDARY_COLLAPSES_MEMBERSHIP_SURFACE_DIFFERENCE",
        "LOW_OR_LOCAL_MEMBERSHIP_FANOUT",
        "NO_REPEATED_SAME_FAMILY_MEMBERSHIP_CHANGE"
      ],
      "cbl_c1_falsifiers":[
        "DEMAND_COREQUIRES_FULL_BOUNDARY_BUNDLE",
        "SEGREGATION_BIRTH_TAX_DOMINATES_LIFECYCLE",
        "NO_TRUTHFUL_DEMAND_EXTRANEOUS_CONFORMANCE_OBLIGATION"
      ],
      "prohibited_inference":[
        "SOLID_IS_VALIDATED",
        "DIP_IS_UNIVERSALLY_BETTER",
        "ISP_IS_UNIVERSALLY_BETTER",
        "ONE_MAINTAINABILITY_SCALAR_SUBSTITUTES_FOR_S_L_C_A",
        "P12_NONRESULT_COUNTS_AS_CBL_C1_FALSIFICATION"
      ]
    }

if __name__=="__main__":
    print(json.dumps(project(json.loads(Path(sys.argv[1]).read_text())),indent=2,sort_keys=True))
