#!/usr/bin/env python3
from __future__ import annotations
import json, os, urllib.request
from pathlib import Path

PRS = [
  {
    "id":"SRP_APPLY_QUILL","repo":"shinycake/quill","number":194,
    "merge":"e79d0d5df9a1ebeaeaa200a4ea65b168e0724cfa",
    "must":["18,837","48 one-responsibility modules","1,219 passed"],
    "role":"SRP","cell":"APPLY","ceiling":"STRUCTURAL_WORLD_WITNESS"
  },
  {
    "id":"SRP_LOCAL_ABSTAIN_KIRO","repo":"kirodotdev/KiroCrew","number":15153,
    "merge":"6fce1827e58c8612d85e4b9da9d6eabd9ee3f9b9",
    "must":["Not a goal","AcpClient","AcpRuntime","AcpSessionHandle","stay whole"],
    "role":"SRP","cell":"LOCAL_ABSTAIN_ON_FURTHER_SPLIT","ceiling":"STRUCTURAL_WORLD_WITNESS"
  },
  {
    "id":"OCP_APPLY_BACKSTAGE","repo":"backstage/backstage","number":31225,
    "merge":"c1b94c43a4926d82540e2a607e533a9fe8243b1c",
    "must":["CustomHomepageWidgetBlueprint","CustomHomepageBlueprint","composable homepage functionality"],
    "role":"OCP","cell":"APPLY","ceiling":"STRUCTURAL_WORLD_WITNESS"
  },
  {
    "id":"OCP_REVOKE_AGNES","repo":"AgnesAI-Labs/agnes-harness","number":42,
    "merge":"adfd9bfe473a55b0e6d0779cb34fc3ffd502cac9",
    "must":["never-dispatched","not an extension point","removed"],
    "role":"OCP","cell":"REVOKE","ceiling":"STRUCTURAL_WORLD_WITNESS"
  },
  {
    "id":"LSP_REPAIR_PYRUST","repo":"ChanyaVRC/pyrust","number":2388,
    "merge":"161fe6e5607f5a489143435b0cc6fda6b93746d6",
    "must":["substitutability boundary","62-case sweep","fails 0"],
    "role":"LSP","cell":"ADMISSIBILITY_FAILURE_REPAIR","ceiling":"STRUCTURAL_PLUS_BEHAVIORAL_TEST_WITNESS"
  },
  {
    "id":"LSP_REJECT_IGNIXA","repo":"brendankowitz/ignixa-fhir","number":275,
    "merge":"c61f77bc0c64c5bab6b1afa413413115b22f143d",
    "must":["incompatible","omitted from base","per-version"],
    "role":"LSP","cell":"ADMISSIBILITY_REJECT_INCOMPATIBLE_SHARED_BASE","ceiling":"STRUCTURAL_WORLD_WITNESS"
  }
]

def gh(url):
    req=urllib.request.Request(url,headers={
      "Accept":"application/vnd.github+json",
      "User-Agent":"EvoNOMOS-LAW-R1-P6",
      "X-GitHub-Api-Version":"2022-11-28",
    })
    tok=os.environ.get("GITHUB_TOKEN")
    if tok: req.add_header("Authorization",f"Bearer {tok}")
    with urllib.request.urlopen(req,timeout=60) as r:
        return json.load(r)

def main():
    rows=[]
    for spec in PRS:
        base=f"https://api.github.com/repos/{spec['repo']}/pulls/{spec['number']}"
        pr=gh(base)
        body=pr.get("body") or ""
        assert pr.get("merged") is True, spec["id"]
        assert pr.get("merge_commit_sha")==spec["merge"], (spec["id"],pr.get("merge_commit_sha"))
        lower=body.lower()
        missing=[x for x in spec["must"] if x.lower() not in lower]
        assert not missing,(spec["id"],missing)
        files=[]
        page=1
        while True:
            batch=gh(base+f"/files?per_page=100&page={page}")
            files.extend(batch)
            if len(batch)<100: break
            page+=1
        rows.append({
          "id":spec["id"],"principle":spec["role"],"cell":spec["cell"],
          "repo":spec["repo"],"pr":spec["number"],"merge_commit":spec["merge"],
          "merged_at":pr.get("merged_at"),"changed_files":len(files),
          "additions":sum(x.get("additions",0) for x in files),
          "deletions":sum(x.get("deletions",0) for x in files),
          "authority_ceiling":spec["ceiling"],
          "required_text_evidence":spec["must"]
        })
    out={
      "schema_version":"law-r1-p6-atlas-v1",
      "fresh_worlds":rows,
      "existing_authority":{
        "ISP":{
          "apply":{
            "source":"LAW-R1-P11 TrueForge Exa→Tavily",
            "authority":"LIFECYCLE_VECTOR_WORLD_CONTACT",
            "result":"phase0 tradeoff; phase1 capability-segregated Pareto dominance; CBL-C1 narrow support"
          },
          "boundary":{
            "source":"P12 Restic",
            "authority":"TERMINAL_NON_RESULT",
            "result":"full mandatory bundle/corequirement cell; no CBL adjudication"
          }
        },
        "DIP":{
          "source":"pre-ORIGIN EvoNOMOS Kodo/homebridge world contacts",
          "authority":"LIFECYCLE_VECTOR_WORLD_CONTACT",
          "result":"DIRECT lower initial churn; INVERT lower follow-up churn; bounded tradeoff, no universal dominance"
        }
      },
      "verdict":"PASS_ATLAS_WORLD_CUSTODY"
    }
    p=Path("out/p6-atlas.json"); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("LAW_R1_P6_ATLAS=PASS")
    print(json.dumps({
      "fresh_worlds":len(rows),
      "principles":sorted(set(x["principle"] for x in rows)),
      "cells":[[x["principle"],x["cell"]] for x in rows]
    }))

if __name__=="__main__": main()
