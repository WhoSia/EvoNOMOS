"""Synthesize strict finite source-repair options from real native Go receipts.

Only accepts a complete 5 x 2 result table. Does NOT claim global editability,
actual developer costs, user-authorized source access or semantic proof.
"""
from collections import defaultdict
from pathlib import Path
import argparse
import json
from mutate import OPS

def classify(receipt):
    rs=receipt["results"]
    required={(arm,op) for arm in ("live","snapshot") for op in OPS}
    keys=[(r["arm"],r["operation"]) for r in rs]
    if len(keys)!=len(required) or set(keys)!=required:
        raise ValueError("incomplete or duplicated source action coverage")
    out={}
    for arm in ("live","snapshot"):
        rows=[r for r in rs if r["arm"]==arm]
        # Distinguish verified finite successful patch from undeclared other repairs.
        admissible=[r for r in rows if r["accepted"]]
        failing=[r for r in rows if not r["accepted"]]
        out[arm]={
            "candidate_count":len(rows),
            "native_oracle_accepted_operators":sorted(r["operation"] for r in admissible),
            "native_oracle_rejected_operators":sorted(r["operation"] for r in failing),
            "fewest_source_edit_sites_among_accepted":min(
                (r["repair"]["sites"] for r in admissible),default=None),
            "fewest_site_operators":sorted(
                r["operation"] for r in admissible if
                r["repair"]["sites"]==min((q["repair"]["sites"] for q in admissible),default=None)),
            "old_contract_broken":sorted(r["operation"] for r in rows
                if not(r["p35_d0"]["success"] and r["issue_old"]["success"])),
            "new_requirement_failed":sorted(r["operation"] for r in rows
                if not r["issue_new"]["success"]),
        }
    l=set(out["live"]["native_oracle_accepted_operators"])
    s=set(out["snapshot"]["native_oracle_accepted_operators"])
    return {
        "scope":"exact selected Go source file candidate grammar and finite test oracle",
        "strictly_incomplete_action_universe":True,
        "full_source_semantic_equivalence_claim":False,
        "source_owner_authorization_verified":False,
        "maintainer_labor_measured":False,
        "per_arm":out,
        "accepted_in_both":sorted(l&s),
        "accepted_exclusively_live":sorted(l-s),
        "accepted_exclusively_snapshot":sorted(s-l),
        "claim":"No universal repair or best architecture follows even if observed accepted sets tie."
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("receipt",type=Path)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    v=classify(json.loads(a.receipt.read_text()))
    out=json.dumps(v,indent=2,sort_keys=True)+"\n"
    print(out)
    if a.output:a.output.write_text(out)
