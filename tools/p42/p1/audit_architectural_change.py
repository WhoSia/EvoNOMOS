#!/usr/bin/env python3
"""P42-P1 actual router-code maintenance event fingerprint.
Source changed-file provenance, NOT a historical authorization certificate or
a behavioral regression test of the merged commit."""
import copy,hashlib,json,sys
from pathlib import Path

def verify(lock,pr,files,merge_commit):
  ref=lock["original_source"]
  if pr.get("number")!=ref["pull_number"] or not pr.get("merged"):
    raise ValueError("PR event does not match")
  if pr.get("title")!=ref["pull_title"]:
    raise ValueError("actual source change title disagrees")
  if pr.get("head",{}).get("sha")!=ref["pull_head_sha"]:
    raise ValueError("source patch head changed")
  if pr.get("merge_commit_sha")!=ref["merge_commit_sha"]:
    raise ValueError("merge source commit changed")
  if merge_commit.get("sha")!=ref["historical_postmerge_source_sha"]:
    raise ValueError("actual postmerge Git commit source changed")
  parents=merge_commit.get("parents",[])
  if len(parents)!=ref["merge_commit_parent_count"]:
    raise ValueError("historical merge commit parent count changed")
  if parents[0].get("sha")!=ref["historical_premerge_first_parent_sha"]:
    raise ValueError("actual historical premerge source SHA changed")

  if pr.get("base",{}).get("ref")!=ref["base_branch"]:
    raise ValueError("base branch changed")
  actual={f["filename"] for f in files}
  assert isinstance(files,list)
  if len(actual)!=ref["changed_files_count"] or len(files)!=len(actual):
    raise ValueError("source changed file count or uniqueness changed")
  if actual!=set(ref["changed_files"]):
    raise ValueError("actual changed source set does not match")
  if not {"route_path.go","router.go"}.issubset(actual):
    raise ValueError("no real router implementation source")
  return sorted(actual)

def main():
  if len(sys.argv)!=6:
    raise SystemExit("usage: audit_architectural_change.py lock.json pr.json files.json merged-commit.json receipt.json")
  lockp,prp,filesp,commitp,out=map(Path,sys.argv[1:])
  lock=json.loads(lockp.read_text())
  pr=json.loads(prp.read_text())
  files=json.loads(filesp.read_text())
  merge_commit=json.loads(commitp.read_text())
  assert lock["status"]=="DISCOVERY_LOCKED_BEFORE_INDEPENDENT_REPLAY"
  actual=verify(lock,pr,files,merge_commit)
  checks=[]
  for kind in ["source_head", "source_file_path", "base_branch", "wrong_historical_parent"]:
    p,f,cm=copy.deepcopy(pr),copy.deepcopy(files),copy.deepcopy(merge_commit)
    if kind=="source_head":p["head"]["sha"]="0"*40
    elif kind=="source_file_path":f[0]["filename"]="fake_router.go"
    elif kind=="base_branch":p["base"]["ref"]="main"
    else:cm["parents"][0]["sha"]="1"*40
    rejected=False
    try:verify(lock,p,f,cm)
    except ValueError:rejected=True
    if not rejected:raise AssertionError("source alteration not rejected: "+kind)
    checks.append(kind)
  receipt={
   "protocol":"P42_P1_REAL_ARCHITECTURAL_PARENT_CHILD_AND_FOUR_MUTANTS_PASS",
   "pull_title":lock["original_source"]["pull_title"],
   "head_sha":lock["original_source"]["pull_head_sha"],
   "merge_sha":lock["original_source"]["merge_commit_sha"],
   "actual_historical_premerge_parent_sha":lock["original_source"]["historical_premerge_first_parent_sha"],
   "actual_historical_postmerge_source_sha":lock["original_source"]["historical_postmerge_source_sha"],
   "source_paths":actual,
   "pr_sha256":hashlib.sha256(prp.read_bytes()).hexdigest(),
   "changed_files_source_sha256":hashlib.sha256(filesp.read_bytes()).hexdigest(),
   "actual_merge_commit_json_sha256":hashlib.sha256(commitp.read_bytes()).hexdigest(),
   "adversarial_controls_rejected":checks,
   "actual_source_maintenance_event":True,
   "before_after_runtime_behavior_executed_by_P42_P1":False,
   "historical_complete_change_authority_proven":False,
   "new_fundamental_OO_law_proven":False
  }
  out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
  print("P42_P1_ORIGINAL_ROUTER_PATCH_FOUR_FILES_AND_THREE_NEGATIVE_CONTROLS_PASS")

if __name__=="__main__":main()
