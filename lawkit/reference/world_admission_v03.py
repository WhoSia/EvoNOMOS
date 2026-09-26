#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

GATES=[
 "exact_source_locked",
 "independent_real_initial_demand",
 "independent_real_followup_demand",
 "pair_frozen_before_treatment",
 "discriminates_prior_world",
 "outcome_surface_frozen",
 "observability_firewall_frozen",
]

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("world",type=Path)
    a=ap.parse_args()
    w=json.loads(a.world.read_text())
    g=w["admission_gates"]
    gates={k:("PASS" if g[k] else "FAIL") for k in GATES}
    m=w["moderators"]
    mismatch=bool(m["capability_bundle_mismatch"])
    out={
      "protocol_version":"0.3",
      "world_id":w["world_id"],
      "admission":"ADMIT" if all(g[k] for k in GATES) else "HOLD",
      "gates":gates,
      "law_pressures":{
        "CIL-C1":{
          "membership_propagation_opportunity":"PRESENT" if int(m["membership_surface_fanout"])>1 else "LIMITED",
          "preexisting_boundary_pressure":"PRESENT" if bool(m["existing_runtime_interface"]) else "ABSENT"
        },
        "CBL-C1":{
          "capability_bundle_mismatch":"PRESENT" if mismatch else "ABSENT",
          "interface_capabilities":m["existing_interface_capabilities"],
          "initial_demand_capabilities":m["initial_demand_capabilities"],
          "followup_demand_capabilities":m["followup_demand_capabilities"]
        }
      },
      "authorized_next":"PRETREATMENT_RIVAL_CONSTITUTION" if all(g[k] for k in GATES) else "NONE",
      "decision_authority":"NO_DESIGN_RECOMMENDATION",
      "winner":None
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
