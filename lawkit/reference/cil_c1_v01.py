#!/usr/bin/env python3
"""Independent LawKit v0.1 reference evaluator.

This is deliberately small and dependency-free. It does not import or call the
Rust kernel. Cross-implementation concordance is checked in GitHub Actions.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

PROHIBITED = [
    "SOLID_IS_TRUE",
    "DIP_IS_UNIVERSALLY_BETTER",
    "INVERT_IS_RECOMMENDED_WITHOUT_LIFECYCLE_EVIDENCE",
    "SAME_SIGN_REPLICATION_IS_SUFFICIENT_AUTHORITY",
]

def parse_fraction(value: str) -> tuple[int, int]:
    parts=value.split("/")
    if len(parts)!=2:
        raise ValueError("fraction must be N/D")
    n,d=(int(x.strip()) for x in parts)
    if d<=0 or n<0 or n>d:
        raise ValueError("invalid fraction")
    return n,d

def inspect(envelope: dict) -> dict:
    v=envelope["vector"]
    n,d=parse_fraction(v["shared_transport_fraction"]["value"])
    fanout="PRESENT" if int(v["canonical_provider_membership_surface_fanout"])>1 else "LIMITED"
    shared="PRESENT" if n>0 and d>1 else "LIMITED"
    redundancy="PRESENT" if bool(v["existing_polymorphic_provider_boundary"]) else "ABSENT"
    heterogeneity=(
        f'payload={v["payload_heterogeneity"]};'
        f'auth={v["authentication_heterogeneity"]};'
        f'config={v["configuration_heterogeneity"]}'
    )
    return {
        "law_candidate":"CIL-C1",
        "authority":"HYPOTHESIS_ONLY_PRE_OUTCOME",
        "observations":{
            "provider_family_cardinality":int(v["existing_provider_family_cardinality"]),
            "membership_surface_fanout":int(v["canonical_provider_membership_surface_fanout"]),
            "shared_transport_fraction":v["shared_transport_fraction"]["value"],
            "payload_heterogeneity":v["payload_heterogeneity"],
            "authentication_heterogeneity":v["authentication_heterogeneity"],
            "configuration_heterogeneity":v["configuration_heterogeneity"],
            "existing_polymorphic_boundary":bool(v["existing_polymorphic_provider_boundary"]),
        },
        "mechanism_channels":{
            "membership_propagation_opportunity":fanout,
            "shared_mechanism_opportunity":shared,
            "heterogeneity_resistance":heterogeneity,
            "boundary_redundancy_pressure":redundancy,
            "future_same_family_demand":"UNOBSERVED",
            "decision_authority":"ABSTAIN_PRE_OUTCOME",
        },
        "prohibited_inference":PROHIBITED,
    }

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("input",type=Path)
    args=ap.parse_args()
    out=inspect(json.loads(args.input.read_text(encoding="utf-8")))
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
