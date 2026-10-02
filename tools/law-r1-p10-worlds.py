#!/usr/bin/env python3
from __future__ import annotations
import json, os, urllib.request
from pathlib import Path

PRS=[
 {"id":"MESON_FRESH","repo":"mesonbuild/meson-python","pr":914,"merge":"49a633f0cac62bf2fe21ea6c15d00450a22bd5e2","must":["absolute paths","external dependencies","relative paths"],"role":"FRESH"},
 {"id":"FFXI_SHIM","repo":"sarthax/FFXI-Mission-Toolkit","pr":269,"merge":"7d313401524a8dc003d6c1d061b3d3e664aff41e","must":["compatibility cli/import shim"],"role":"DEVELOPMENT"},
 {"id":"OPENCHIA_BREAK","repo":"chian/OpenChia","pr":10,"merge":"4adb2a1b2de8d9b5c2bc133c32fa47e150ad7647","must":["intentional hard namespace break"],"role":"DEVELOPMENT"},
 {"id":"OPENPENCIL_EXPORT","repo":"open-pencil/open-pencil","pr":612,"merge":"5689eccc0ca4556ea6f17fddc22933f3d9c06792","must":["remove published bun export conditions"],"role":"DEVELOPMENT"},
 {"id":"S7_ALIAS","repo":"RConsortium/S7","pr":734,"merge":"245aaf46355a48403ad580b366b817a9c4191851","must":["new_external_class() now resolves aliases"],"role":"DEVELOPMENT"}
]
COMMIT={"repo":"open-pencil/open-pencil","sha":"88c1077071328b8df68f282543f16e20e97930b4"}

def gh(url):
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"EvoNOMOS-P10","X-GitHub-Api-Version":"2022-11-28"})
    tok=os.environ.get("GITHUB_TOKEN")
    if tok:req.add_header("Authorization",f"Bearer {tok}")
    with urllib.request.urlopen(req,timeout=60) as r:return json.load(r)

def main():
    rows=[]
    for s in PRS:
        p=gh(f"https://api.github.com/repos/{s['repo']}/pulls/{s['pr']}")
        assert p.get("merged") is True,s["id"]
        assert p.get("merge_commit_sha")==s["merge"],(s["id"],p.get("merge_commit_sha"))
        body=(p.get("body") or "").lower()
        miss=[m for m in s["must"] if m.lower() not in body]
        assert not miss,(s["id"],miss)
        rows.append({"id":s["id"],"repo":s["repo"],"pr":s["pr"],"merge_commit":s["merge"],"role":s["role"]})

    c=gh(f"https://api.github.com/repos/{COMMIT['repo']}/commits/{COMMIT['sha']}")
    assert c.get("sha")==COMMIT["sha"]

    pre=json.loads(Path("active/g8-law-r1-p10/P10_MESON912_PRECOMMIT.json").read_text())
    res=json.loads(Path("active/g8-law-r1-p10/P10_MESON912_RESULT.json").read_text())
    assert pre["precommit"]=="MATCHED_GEOMETRY_CONTEXT_HOLDOUT_MESONPY_912"
    assert res["resolution"]["result"]=="BRANCH_A_SUPPORTED"
    assert res["adjudication"]["matched_geometry_context_effect"]=="SUPPORTED"
    assert res["adjudication"]["state_aliasing"]=="NOT_OBSERVED_ONCE_X_IS_INCLUDED"
    assert res["adjudication"]["r2"]=="NOT_AUTHORIZED"

    out={
      "stage":"EvoNOMOS Generation VIII LAW-R1-P10",
      "worlds":rows,
      "fresh_holdout":{
        "world":"mesonbuild/meson-python#912",
        "precommit":"1de10661787a6e433da6855948ebbbe3531732e2",
        "resolution_merge":"49a633f0cac62bf2fe21ea6c15d00450a22bd5e2",
        "result":"MATCHED_GEOMETRY_CONTEXT_EFFECT_SUPPORTED"
      },
      "tests":{
        "matched_geometry_reversal":"SUPPORTED_BOUNDED",
        "matched_context_discrimination":"SUPPORTED_DEVELOPMENT",
        "interaction_nonseparability":"SUPPORTED_BOUNDED",
        "same_X_G_E_distinct_action":"NOT_OBSERVED",
        "transport":"BOUNDED_MULTI_PROJECT"
      },
      "verdict":"PASS_P10_WORLD_CUSTODY"
    }
    Path("out-p10").mkdir(exist_ok=True)
    Path("out-p10/p10-worlds.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("LAW_R1_P10_WORLD_CUSTODY=PASS")
    print(json.dumps(out["tests"],sort_keys=True))

if __name__=="__main__":main()
