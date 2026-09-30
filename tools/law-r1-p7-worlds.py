#!/usr/bin/env python3
from __future__ import annotations
import json, os, urllib.request
from pathlib import Path

PRS=[
 {"id":"KYVERNO_17769","repo":"kyverno/kyverno","pr":17769,"merge":"c51c8f6fd10824a2560819553b78ac0d4f80a652","must":["root cause of drift","single source of truth"],"role":"DISCOVERY"},
 {"id":"COMFY_18700","repo":"Comfy-Org/ComfyUI_frontend","pr":18700,"merge":"888e079ea9999bbde7aadb0e58eb9c848c84590d","must":["delete every reconciliation layer","graph api"],"role":"DISCOVERY"},
 {"id":"TER_48","repo":"lgriffin/TER","pr":48,"merge":"983f0aa2af5cd188f342d5a6daf08cb46f470806","must":["pure ter 4 domain","price_book.json"],"role":"DISCOVERY"},
 {"id":"CREWAI_7796","repo":"crewAIInc/crewAI","pr":7796,"merge":"a6e6d0f9d85a72dd03bc041b8ea4648f211b6d9e","must":["centralize context-window lookup","parity"],"role":"HOLDOUT"}
]

def gh(url):
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"EvoNOMOS-P7","X-GitHub-Api-Version":"2022-11-28"})
    tok=os.environ.get("GITHUB_TOKEN")
    if tok:req.add_header("Authorization",f"Bearer {tok}")
    with urllib.request.urlopen(req,timeout=60) as r:return json.load(r)

def main():
    rows=[]
    for s in PRS:
        p=gh(f"https://api.github.com/repos/{s['repo']}/pulls/{s['pr']}")
        body=(p.get("body") or "").lower()
        assert p.get("merged") is True,s["id"]
        assert p.get("merge_commit_sha")==s["merge"],(s["id"],p.get("merge_commit_sha"))
        miss=[x for x in s["must"] if x.lower() not in body]
        assert not miss,(s["id"],miss)
        rows.append({"id":s["id"],"repo":s["repo"],"pr":s["pr"],"merge_commit":s["merge"],"merged_at":p.get("merged_at"),"role":s["role"]})
    out={
      "stage":"EvoNOMOS Generation VIII LAW-R1-P7",
      "motif":"AUTHORITY_PATH_CONVERGENCE_MOTIF",
      "discovery_worlds":[x for x in rows if x["role"]=="DISCOVERY"],
      "holdout":[x for x in rows if x["role"]=="HOLDOUT"],
      "holdout_precommit":"2354a8a0db1d747221d0699682db6d2aaa47c969",
      "holdout_result":{
        "prediction":"SUPPORTED",
        "observed":["shared definitions/resolver","native+fallback migration","cross-path parity tests","provider-specific semantics retained"]
      },
      "prior_art":{
        "generic_ssot_novelty":"KILLED",
        "clone_boundary":"DUPLICATION_NOT_AUTOMATICALLY_HARMFUL",
        "surviving_scope":"CONVERGE_ONLY_WHEN_PATHS_SHARE_SEMANTIC_AUTHORITY_AND_DUPLICATED_EDIT_AUTHORITY_CAUSES_DRIFT_OR_RECONCILIATION"
      },
      "verdict":"PASS_WORLD_CUSTODY_AND_OUT_OF_STREAM_CHALLENGE"
    }
    Path("out").mkdir(exist_ok=True)
    Path("out/p7-worlds.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("LAW_R1_P7_WORLD_CONTACT=PASS")
    print(json.dumps({"discovery":len(out["discovery_worlds"]),"holdout":len(out["holdout"]),"prediction":out["holdout_result"]["prediction"]}))
if __name__=="__main__":main()
