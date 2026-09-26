#!/usr/bin/env python3
"""Seal one arm's exploratory lifecycle vector without printing its values."""
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

def churn(repo:Path, base:str, head:str, paths:list[str])->int:
    cp=subprocess.run(
        ["git","-C",str(repo),"diff","--numstat",base,head,"--",*paths],
        check=True,text=True,capture_output=True,
    )
    total=0
    for line in cp.stdout.splitlines():
        parts=line.split("\t")
        if len(parts)<3 or parts[0]=="-" or parts[1]=="-":
            continue
        total+=int(parts[0])+int(parts[1])
    return total

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--arm",required=True)
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--base",required=True)
    ap.add_argument("--p2-head",required=True)
    ap.add_argument("--p3-head",required=True)
    ap.add_argument("--exposure",type=Path,required=True)
    ap.add_argument("--q0",type=int,choices=[0,1],required=True)
    ap.add_argument("--q1",type=int,choices=[0,1],required=True)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()

    exp=json.loads(args.exposure.read_text(encoding="utf-8"))
    model=exp["authority_site_model"][args.arm]
    paths=exp["product_files"]
    out={
      "stage":"EvoNOMOS Generation VIII ORIGIN-R1-P10-P3",
      "arm":args.arm,
      "authority":"EXPLORATORY_ONLY",
      "vector":{
        "S0":len(model["phase0"]),
        "L0":churn(args.repo,args.base,args.p2_head,paths),
        "Q0":args.q0,
        "S1":len(model["phase1"]),
        "L1":churn(args.repo,args.p2_head,args.p3_head,paths),
        "Q1":args.q1,
      },
      "values_disclosed_in_arm_job":False,
      "winner":None,
    }
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("P10_P3_ARM_MEASUREMENT_SEALED=PASS")

if __name__=="__main__":
    main()
