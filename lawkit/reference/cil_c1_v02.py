#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

def direction(d:int,i:int)->str:
    return "EQUAL" if d==i else ("DIRECT_HIGHER" if d>i else "INVERT_HIGHER")

def pattern(p0:str,p1:str)->str:
    if p0=="INVERT_HIGHER" and p1=="DIRECT_HIGHER":
        return "INITIAL_INVERSION_TAX_THEN_PROPAGATION_SAVING"
    if p0=="DIRECT_HIGHER" and p1=="INVERT_HIGHER":
        return "INITIAL_DIRECT_TAX_THEN_INVERSION_FOLLOWUP_TAX"
    if p0==p1:
        return "NO_SIGN_REVERSAL"
    return "MIXED_OR_EQUAL"

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("moderator",type=Path)
    ap.add_argument("lifecycle",type=Path)
    ap.add_argument("firewall",type=Path)
    a=ap.parse_args()
    mod=json.loads(a.moderator.read_text())
    life=json.loads(a.lifecycle.read_text())
    fw=json.loads(a.firewall.read_text())
    d=life["vectors"]["DIRECT_DEDICATED"]
    i=life["vectors"]["INVERT_CHANNEL_ADAPTER"]
    s0,s1=direction(d["S0"],i["S0"]),direction(d["S1"],i["S1"])
    l0,l1=direction(d["L0"],i["L0"]),direction(d["L1"],i["L1"])
    out={
      "law_candidate":"CIL-C1",
      "authority":fw["lawkit_required_authority"],
      "evidence_class":"EXPLORATORY_ONLY",
      "phasewise_direction":{
        "surface":{"phase0":s0,"phase1":s1},
        "churn":{"phase0":l0,"phase1":l1},
      },
      "reversal":{
        "surface":s0!="EQUAL" and s1!="EQUAL" and s0!=s1,
        "churn":l0!="EQUAL" and l1!="EQUAL" and l0!=l1,
      },
      "lifecycle_pattern":{"surface":pattern(s0,s1),"churn":pattern(l0,l1)},
      "moderator_context":{
        "membership_surface_fanout":mod["vector"]["canonical_provider_membership_surface_fanout"],
        "shared_transport_fraction":mod["vector"]["shared_transport_fraction"]["value"],
        "payload_heterogeneity":mod["vector"]["payload_heterogeneity"],
        "authentication_heterogeneity":mod["vector"]["authentication_heterogeneity"],
        "configuration_heterogeneity":mod["vector"]["configuration_heterogeneity"],
        "existing_polymorphic_boundary":mod["vector"]["existing_polymorphic_provider_boundary"],
      },
      "cil_c1_update":"FORBIDDEN_CONFIRMATORY_UPDATE",
      "decision_authority":"ABSTAIN",
      "prohibited_inference":fw["forbidden"],
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
