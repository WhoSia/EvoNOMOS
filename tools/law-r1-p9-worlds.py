#!/usr/bin/env python3
from __future__ import annotations
import json, os, urllib.request
from pathlib import Path

PRS=[
 {"id":"FARM_VERSION_ALIGN","repo":"farming-labs/farm.js","pr":1625,"merge":"7ec4502d0261967b0ee1e4cab81f03b16e41a1e4","must":["tightly coupled preview packages resolve from different versions","workspace:*"],"family":"VERSION_COEXISTENCE"},
 {"id":"CONTROL_TOWER_EPOCH_PIN","repo":"linuxarena/control-tower","pr":1924,"merge":"67dcf28e64f7abd4aee06d4cd16f08d1bde1bbdc","must":["released runner talks to a newer server","v<version>"],"family":"VERSION_COEXISTENCE"},
 {"id":"OPENCLAW_FALLBACK_RETIRE","repo":"openclaw/openclaw","pr":163087,"merge":"0976a9abff56c55785cc8926311efd796652ac24","must":["co-shipped-gateway contract","unsupported older preview responses no longer receive compatibility handling"],"family":"VERSION_COEXISTENCE"},
 {"id":"SHOTAI_UNKNOWN_PRESERVE","repo":"Armadillon44/shotAI","pr":106,"merge":"77adda386150ee591a9b768b80128afa9b4ab2c8","must":["key written by a newer build","preserve the raw value"],"family":"VERSION_COEXISTENCE"},
 {"id":"NEBULA_ORDER_REPLAY","repo":"vanyastaff/nebula","pr":1136,"merge":"7fabc0c1c3e4740f512bd7995b1cdd6d55de4622","must":["happens-before","concurrent_with"],"family":"EVENT_ORDER_REPLAY"},
 {"id":"BULK_PRICE_CURRENT_STATE","repo":"rishu605/bulk-price-editor","pr":897,"merge":"c3f915e427c26f2a25ea61447e795df098f2004d","must":["ask shopify on receipt","delayed or replayed active"],"family":"EVENT_ORDER_REPLAY"}
]

def gh(url):
    req=urllib.request.Request(url,headers={
      "Accept":"application/vnd.github+json",
      "User-Agent":"EvoNOMOS-LAW-R1-P9",
      "X-GitHub-Api-Version":"2022-11-28"
    })
    tok=os.environ.get("GITHUB_TOKEN")
    if tok: req.add_header("Authorization",f"Bearer {tok}")
    with urllib.request.urlopen(req,timeout=60) as r:
        return json.load(r)

def verify_pr(s):
    p=gh(f"https://api.github.com/repos/{s['repo']}/pulls/{s['pr']}")
    assert p.get("merged") is True,s["id"]
    assert p.get("merge_commit_sha")==s["merge"],(s["id"],p.get("merge_commit_sha"))
    body=(p.get("body") or "").lower()
    missing=[m for m in s["must"] if m.lower() not in body]
    assert not missing,(s["id"],missing)
    return {
      "id":s["id"],"repo":s["repo"],"pr":s["pr"],"merge_commit":s["merge"],
      "merged_at":p.get("merged_at"),"family":s["family"]
    }

def main():
    rows=[verify_pr(s) for s in PRS]

    issue=gh("https://api.github.com/repos/home-assistant/core/issues/181879")
    comments=gh("https://api.github.com/repos/home-assistant/core/issues/181879/comments")
    ctext="\n".join((c.get("body") or "") for c in comments).lower()
    assert issue.get("state")=="closed"
    assert "minimum stays" in ctext
    assert "package repository state" in ctext
    assert "7.3.68" in ctext

    pre=json.loads(Path("active/g8-law-r1-p9/P9_HOLDOUT_HA181879_PRECOMMIT.json").read_text())
    result=json.loads(Path("active/g8-law-r1-p9/P9_HOLDOUT_HA181879_RESULT.json").read_text())
    assert pre["precommit"]=="FRESH_HOLDOUT_HA_UNIFIPROTECT_181879"
    assert result["result"]=="BRANCH_B_SUPPORTED"

    families={}
    for r in rows:
        families.setdefault(r["family"],[]).append(r["id"])

    out={
      "schema_version":"law-r1-p9-worlds-v1",
      "stage":"EvoNOMOS Generation VIII LAW-R1-P9",
      "development_worlds":rows,
      "temporal_families":families,
      "fresh_holdout":{
        "world":"home-assistant/core#181879",
        "precommit":"e94f2f017e31fd78df60f782ebd12807008efd58",
        "result":"BRANCH_B_SUPPORTED",
        "structural_spf_change":"NONE",
        "decisive_state":["required capability availability","reachable version state"]
      },
      "representation_tests":{
        "same_geometry_different_action":{
          "status":"BOUNDED_WITNESS",
          "contrast":[
            "co-shipped contract permits compatibility fallback retirement",
            "staggered/rollback coexistence requires unknown-state preservation"
          ]
        },
        "temporal_single_axis":{
          "status":"REJECTED_AS_PREMATURE",
          "reason":"version coexistence and event-order/current-state problems require different interventions"
        },
        "cross_axis_forced_coupling":{
          "status":"NOT_ESTABLISHED_IN_SAMPLED_WORLDS"
        }
      },
      "verdict":"PASS_P9_WORLD_CUSTODY"
    }
    Path("out").mkdir(exist_ok=True)
    Path("out/p9-worlds.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("LAW_R1_P9_WORLD_CUSTODY=PASS")
    print(json.dumps({
      "families":sorted(families),
      "holdout":out["fresh_holdout"]["result"],
      "aliasing":out["representation_tests"]["same_geometry_different_action"]["status"]
    },sort_keys=True))

if __name__=="__main__":main()
