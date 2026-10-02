#!/usr/bin/env python3
from __future__ import annotations
import json, os, urllib.request
from pathlib import Path

PRS=[
 {"id":"B_PARK_10","repo":"G9MaGiC/park","pr":10,"merge":"51f6c2cf91cf1288f7e836c485fec90603387790","must":["audit event inside the existing database transaction","emails only after the transaction commits"]},
 {"id":"B_PARK_34","repo":"G9MaGiC/park","pr":34,"merge":"4b2f73846372dd4f3eeeec6dd22f42e802333e69","must":["one transaction","lead matching and attribution after the database transaction commits"]},
 {"id":"B_PHARMACY_38","repo":"Jcrad006/pharmacy1os","pr":38,"merge":"cd5a9ecfaf687815792c3d782307a9acdb11a2e9","must":["atomically publishes only complete backup sets","rollback copy"]},
 {"id":"C_CONTROL_TOWER_2006","repo":"linuxarena/control-tower","pr":2006,"merge":"cebca3e0732f9ad84b49f821b544e366f1d18f9a","must":["blast radius","only the instance","keep an unconditional read"]}
]
STACKS_COMMITS={
 "idempotency":"d9bd2ac58b19597a6feffde07b99cf2493628ee1",
 "audit_txn":"41fb37f6bc536e73bd5fcd1a24ac3d0767079e1b",
}

def gh(url):
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"EvoNOMOS-P8","X-GitHub-Api-Version":"2022-11-28"})
    tok=os.environ.get("GITHUB_TOKEN")
    if tok: req.add_header("Authorization",f"Bearer {tok}")
    with urllib.request.urlopen(req,timeout=60) as r:return json.load(r)

def verify_pr(s):
    p=gh(f"https://api.github.com/repos/{s['repo']}/pulls/{s['pr']}")
    assert p.get("merged") is True,s["id"]
    assert p.get("merge_commit_sha")==s["merge"],(s["id"],p.get("merge_commit_sha"))
    body=(p.get("body") or "").lower()
    missing=[m for m in s["must"] if m.lower() not in body]
    assert not missing,(s["id"],missing)
    return {"id":s["id"],"repo":s["repo"],"pr":s["pr"],"merge_commit":s["merge"],"merged_at":p.get("merged_at")}

def main():
    rows=[verify_pr(s) for s in PRS]

    comments=gh("https://api.github.com/repos/stacksjs/stacks/issues/1876/comments")
    text="\n".join((x.get("body") or "") for x in comments).lower()
    assert "stripe idempotency keys" in text
    assert "transactionality opt-in" in text
    for name,sha in STACKS_COMMITS.items():
        c=gh(f"https://api.github.com/repos/stacksjs/stacks/commits/{sha}")
        assert c["sha"]==sha,(name,c.get("sha"))
    stacks={
      "issue":1876,
      "precommit":"ae8523124191f72d4dfd604b8d1a49c7c47d45e6",
      "idempotency_commit":STACKS_COMMITS["idempotency"],
      "audit_transaction_commit":STACKS_COMMITS["audit_txn"],
      "discriminator":"SUPPORTED_SUBSTRATE_SPLIT",
      "blindness":"WEAKLY_BLINDED"
    }

    hermes=gh("https://api.github.com/repos/NousResearch/hermes-agent/issues/108671")
    hbody=(hermes.get("body") or "").lower()
    assert hermes.get("state")=="open"
    for phrase in ["shared canonical credential authority","least-privilege access","not a request to remove all sharing"]:
        assert phrase in hbody,phrase
    hermes_out={
      "issue":108671,
      "state":"OPEN",
      "role":"UNRESOLVED_COMPOSITION_WORLD",
      "evidence":"shared canonical credential authority plus profile-selected capability restrictions"
    }

    p7=json.loads(Path("active/g8-law-r1-p7/P7_TERMINAL_SEAL.json").read_text())
    assert p7["generator"]["status"]=="ABSORB_EXISTING_FAMILY__CONDITIONAL_SCOPE_REFINED"

    out={
      "schema_version":"law-r1-p8-ecology-v1",
      "stage":"EvoNOMOS Generation VIII LAW-R1-P8",
      "motif_A":{
        "source":"P7",
        "name":"SEMANTIC_AUTHORITY_CONVERGENCE",
        "status":p7["generator"]["status"],
        "axis":"SEMANTIC_AUTHORITY_CARDINALITY"
      },
      "motif_B":{
        "name":"INVARIANT_CLOSURE_BY_SUBSTRATE",
        "worlds":[x for x in rows if x["id"].startswith("B_")],
        "stacks_discriminator":stacks,
        "negative_controls":[
          "Park emails and lead attribution remain after commit",
          "Stacks audit transactionality is strict opt-in while legacy best-effort remains",
          "Stripe remote boundary uses idempotency rather than pretending to share a DB transaction"
        ],
        "axis":"FAILURE_CLOSURE_BOUNDARY"
      },
      "motif_C":{
        "name":"OPERATIONAL_AUTHORITY_SCOPE_PARTITIONING",
        "worlds":[x for x in rows if x["id"].startswith("C_")],
        "hermes":hermes_out,
        "negative_controls":[
          "control-tower intentionally keeps documented Docker-org parameters shared",
          "Hermes explicitly preserves a shared canonical credential authority where required"
        ],
        "axis":"OPERATIONAL_AUTHORITY_SCOPE"
      },
      "verdict":"PASS_MULTI_MOTIF_WORLD_CUSTODY"
    }
    Path("out").mkdir(exist_ok=True)
    Path("out/p8-ecology.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("LAW_R1_P8_ECOLOGY=PASS")
    print(json.dumps({
      "A":out["motif_A"]["status"],
      "B":out["motif_B"]["stacks_discriminator"]["discriminator"],
      "C":out["motif_C"]["hermes"]["role"]
    },sort_keys=True))
if __name__=="__main__":main()
