#!/usr/bin/env python3
"""P41 C: independently re-read PUBLIC GitHub historic PR/merge event.

Requires raw live GitHub REST JSON artifacts from Actions curl. This proves a
platform-recorded merge, NOT authorization policy, normative rights, or the
current authenticated collaborator permission snapshot.
"""
import json,sys,hashlib
from pathlib import Path
def main():
 if len(sys.argv)!=6:
  raise SystemExit("usage: script expected.json live-pr.json live-events.json live-reviews.json receipt.json")
 expected,pr_path,event_path,review_path,out=map(Path,sys.argv[1:])
 e=json.loads(expected.read_text())
 p=json.loads(pr_path.read_text())
 events=json.loads(event_path.read_text())
 reviews=json.loads(review_path.read_text())
 assert e["protocol"]=="P41_P1_C_GITHUB_HISTORICAL_MERGE_EVENT_V1"
 assert p["merged"] is True and p["number"]==3132
 assert p["base"]["repo"]["full_name"]=="labstack/echo" and p["base"]["ref"]=="v4"
 assert p["merged_by"]["login"]==e["merge_actor"]
 assert p["merged_at"]==e["merge_at_utc"]
 assert p["merge_commit_sha"]==e["merge_commit_sha"]
 assert p["html_url"]==e["pull_request"]
 matches=[v for v in events
  if v.get("event")=="merged" and v.get("actor",{}).get("login")==e["merge_actor"]
  and v.get("commit_id")==e["merge_commit_sha"]
  and v.get("created_at")==e["merge_at_utc"]]
 assert len(matches)>=1
 for expected_review in e["review_submissions"]:
  assert any(r.get("user",{}).get("login")==expected_review["author"]
   and r.get("state")==expected_review["state"]
   and r.get("submitted_at")==expected_review["submitted_at"] for r in reviews)
 assert all(x["state"]=="COMMENTED" for x in e["review_submissions"])
 receipt={
   "protocol":"P41_P1_C_PUBLIC_GITHUB_MERGE_EVENT_LIVE_VERIFIED",
   "merge_commit_sha":e["merge_commit_sha"],
   "merged_at_utc":e["merge_at_utc"],
   "merge_actor":e["merge_actor"],
   "pr_raw_sha256":hashlib.sha256(pr_path.read_bytes()).hexdigest(),
   "timeline_raw_sha256":hashlib.sha256(event_path.read_bytes()).hexdigest(),
   "reviews_raw_sha256":hashlib.sha256(review_path.read_bytes()).hexdigest(),
   "current_authenticated_admin_independently_requeried_by_this_job":False,
   "branch_protection_policy_at_merge_observed":False,
   "legal_or_institutional_rights_proven":False,
   "all_C_conditions_irredundant":False
 }
 out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
 print("P41_P1_PUBLIC_HISTORICAL_MERGE_ACTOR_AND_COMMIT_INDEPENDENT_API_PASS")
if __name__=="__main__": main()
