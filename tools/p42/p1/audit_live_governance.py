#!/usr/bin/env python3
"""EvoNOMOS P42-P1 — independent public GitHub event/ruleset evidence court.
Verifies fields and rejection controls, NEVER infers historic rule completeness
or institutional legitimate rights from a successful platform merge.
"""
import copy
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

def read(path):
    return json.loads(Path(path).read_text())

def when(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(dt.timezone.utc)

def evidence_check(lock, pr, events, reviews, rulesets, ruleset):
    known=lock["original_source"]
    declared=lock["rule_discovery"]
    if not pr.get("merged") or pr.get("number")!=known["pull_number"]:
        raise ValueError("missing actual merge")
    if pr.get("base",{}).get("repo",{}).get("full_name")!=known["repository"]:
        raise ValueError("base repo changed")
    if pr.get("base",{}).get("ref")!=known["base_branch"]:
        raise ValueError("base branch changed")
    if pr.get("merged_by",{}).get("login")!=known["merge_actor"]:
        raise ValueError("platform merge actor changed")
    if pr.get("merged_at")!=known["merge_at_utc"] or pr.get("merge_commit_sha")!=known["merge_commit_sha"]:
        raise ValueError("merge timestamp or commit changed")
    merge_events=[v for v in events if v.get("event")=="merged"
      and v.get("actor",{}).get("login")==known["merge_actor"]
      and v.get("created_at")==known["merge_at_utc"]
      and v.get("commit_id")==known["merge_commit_sha"]]
    if not merge_events:
        raise ValueError("no independent merge timeline matching original PR")
    if len(reviews)!=len(known["reviews_recorded"]):
        raise ValueError("review count changed, refresh evidence from source")
    for row in known["reviews_recorded"]:
        if not any(r.get("user",{}).get("login")==row["author"]
          and r.get("state")==row["state"]
          and r.get("submitted_at")==row["submitted_at"] for r in reviews):
            raise ValueError("review state/actor/time changed; COMMENTED must not become APPROVED")
    if ruleset.get("id")!=declared["id"] or ruleset.get("name")!=declared["name"]:
        raise ValueError("current rule identity changed")
    if ruleset.get("source")!=declared["source_repo"] or ruleset.get("source_type")!=declared["scope"]:
        raise ValueError("source/type mismatch")
    if ruleset.get("enforcement")!=declared["enforcement"]:
        raise ValueError("present enforcement state changed")
    conditions=ruleset.get("conditions",{}).get("ref_name",{}).get("include",[])
    if not set(declared["included_refs"]).issubset(set(conditions)):
        raise ValueError("the queried current ruleset no longer covers the expected refs")
    if not isinstance(rulesets,list) or not any(row.get("id")==declared["id"] for row in rulesets):
        raise ValueError("ruleset missing from public repo listing")
    rules={r["type"]:r for r in ruleset.get("rules",[])}
    for rule in ["deletion","non_fast_forward","pull_request"]:
        if rule not in rules:
            raise ValueError("required current source rule changed: "+rule)
    count=rules["pull_request"].get("parameters",{}).get("required_approving_review_count")
    if count!=declared["current_required_approving_review_count"]:
        raise ValueError("current required review count changed")
    if when(ruleset.get("created_at"))!=when(declared["created_at"]) or when(ruleset.get("updated_at"))!=when(declared["updated_at"]):
        raise ValueError("rule metadata instant mismatch: live "+repr((ruleset.get("created_at"),ruleset.get("updated_at")))+" expected "+repr((declared["created_at"],declared["updated_at"])))
    born,updated,merged=when(ruleset["created_at"]),when(ruleset["updated_at"]),when(pr["merged_at"])
    if born>updated or updated>merged:
        raise ValueError("ruleset metadata is not ordered before the merge")
    return {
      "current_ruleset_created_before_merge":born<merged,
      "current_ruleset_updated_before_merge":updated<merged,
      "current_ruleset_applies_to_v4_now":("refs/heads/v4" in conditions),
      "current_ruleset_required_approvals":count,
      "merge_timeline_independently_agrees":True,
      "observed_reviews_all_COMMENTED":all(r["state"]=="COMMENTED" for r in reviews),
    }

def check_mutations(lock,pr,events,reviews,rulesets,ruleset):
    mutations=[]
    def negative(label, update):
        data=[copy.deepcopy(obj) for obj in [pr,events,reviews,rulesets,ruleset]]
        update(data)
        rejected=False
        try:
            evidence_check(lock,*data)
        except (ValueError,KeyError,TypeError):
            rejected=True
        if not rejected:
            raise AssertionError("fail-open rejection control: "+label)
        mutations.append({"name":label,"rejected":True})
    negative("wrong_merge_actor",lambda x:x[0].setdefault("merged_by",{}).update(login="FAKE_ACTOR"))
    negative("wrong_merge_commit_sha",lambda x:x[0].update(merge_commit_sha="f"*40))
    negative("ruleset_last_updated_after_merge",lambda x:x[4].update(updated_at="2026-10-02T00:00:00+00:00"))
    negative("ruleset_does_not_include_v4",lambda x:x[4]["conditions"]["ref_name"].update(include=["refs/heads/elsewhere"]))
    negative("fake_APPROVED_review",lambda x:x[2][0].update(state="APPROVED"))
    return mutations

def main():
    if len(sys.argv)!=10:
        raise SystemExit("usage: file.py lock pr events reviews list detail hist_status protection_status receipt")
    lockp,prp,eventsp,reviewsp,listp,detailp,histp,protectp,out=map(Path,sys.argv[1:])
    lock,pr,events,reviews,listing,detail=map(read,[lockp,prp,eventsp,reviewsp,listp,detailp])
    assert lock["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P1_DISCOVERED_GOVERNANCE_EVENT_PACKET_V1"
    assert lock["status"]=="DISCOVERY_LOCKED_BEFORE_INDEPENDENT_REPLAY"
    present=evidence_check(lock,pr,events,reviews,listing,detail)
    controls=check_mutations(lock,pr,events,reviews,listing,detail)
    status_history=int(histp.read_text().strip())
    status_protection=int(protectp.read_text().strip())
    if status_history not in (200,403,404) or status_protection not in (200,403,404):
        raise ValueError("unclassified API access response must NOT be interpreted as no policy")
    receipt={
      "protocol":"P42_P1_RAVEL_GITHUB_DISCOVERY_REPLAY_AND_NEGATIVE_CONTROLS_PASS",
      "lock_sha256":hashlib.sha256(lockp.read_bytes()).hexdigest(),
      "api_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
        for p in [prp,eventsp,reviewsp,listp,detailp]},
      "observed_public_GitHub_platform_merge":True,
      "discovered_current_ruleset_id":lock["rule_discovery"]["id"],
      "present_ruleset_temporally_compatible_with_merge":present,
      "controls":controls,
      "negative_controls_passed":len(controls),
      "ruleset_history_api_HTTP_status":status_history,
      "classic_branch_protection_api_HTTP_status":status_protection,
      "historical_policy_version_independently_authenticated":False,
      "all_applicable_policy_layers_at_merge_observed":False,
      "bypass_authority_at_merge_known":False,
      "institutionally_legitimate_edit_authority_proven":False,
      "pr_merge_platform_event_proves_edit_legitimacy":False,
      "missing_policy_means_no_policy":False,
      "new_unseen_classical_outperformance":False,
      "LAWR2_authorized":False,
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("P42_P1_LIVE_RULESET_AND_MERGE_5_NEGATIVE_CONTROLS_BOUNDED_PASS")
    print(f"HISTORY_HTTP={status_history} CLASSIC_PROTECTION_HTTP={status_protection} HISTORICAL_PERMISSIONS=UNKNOWN")

if __name__=="__main__":main()
