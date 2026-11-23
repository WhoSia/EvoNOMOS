"""Four-arm Paper B evidence-receipt gate. No model is called by this module.

Do not mistake text/manifest validity for code review quality, causal identification,
semantic equivalence, or a completed agent experiment.
"""
from __future__ import annotations
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ARMS = ("NONE", "HARD_SOLID", "SCOPED_SOLID", "EVIDENCE_CONDITIONAL")
STATUS = ("completed", "abstained", "failed", "tool_error")
REVIEW = ("ADMISSIBLE", "INADMISSIBLE", "UNRESOLVED")
SHA40 = re.compile(r"^[a-f0-9]{40}$")
SHA64 = re.compile(r"^[a-f0-9]{64}$")
TERMS = re.compile(r"\b(?:SOLID|SRP|OCP|LSP|ISP|DIP|open.closed|single.responsibility)\b", re.I)
FIELDS = (
    "trial_id", "study_kind", "task_id", "model_id", "source_commit",
    "task_spec_sha256", "tool_budget_id", "arm", "invocation_id",
    "fresh_context", "run_status", "code_patch_sha256", "patch_files",
    "explanation", "go_results", "contract_review",
)

def errors_for_receipt(r):
    errors=[]
    if not isinstance(r, dict):
        return ["not_object"]
    for key in FIELDS:
        if key not in r:
            errors.append("missing:"+key)
    if errors:
        return errors
    for key in ("trial_id", "task_id", "model_id", "tool_budget_id", "invocation_id"):
        if not isinstance(r[key], str) or not r[key].strip():
            errors.append("nonempty:"+key)
    if r["study_kind"] not in ("synthetic_test", "observed"):
        errors.append("study_kind")
    if r["arm"] not in ARMS:
        errors.append("arm")
    if r["run_status"] not in STATUS:
        errors.append("status")
    if not isinstance(r["fresh_context"], bool) or not r["fresh_context"]:
        errors.append("fresh_context")
    if not isinstance(r["source_commit"], str) or not SHA40.fullmatch(r["source_commit"]):
        errors.append("source_commit")
    if not isinstance(r["task_spec_sha256"], str) or not SHA64.fullmatch(r["task_spec_sha256"]):
        errors.append("task_spec_sha256")
    patch = r["code_patch_sha256"]
    if patch is not None and (not isinstance(patch,str) or not SHA64.fullmatch(patch)):
        errors.append("code_patch_sha256")
    if not isinstance(r["patch_files"], list) or not all(isinstance(x,str) and x.strip() for x in r["patch_files"]):
        errors.append("patch_files")
    if r["run_status"]=="completed" and (patch is None or not r["patch_files"]):
        errors.append("completed_missing_patch")
    if r["run_status"] in ("abstained", "tool_error") and (patch is not None or r["patch_files"]):
        errors.append("no_patch_status_inconsistent")
    if not isinstance(r["explanation"],str):
        errors.append("explanation")
    x=r["go_results"]
    if not isinstance(x,dict) or set(x)!= {"baseline_pass","new_requirement_pass","race_pass"}:
        errors.append("go_results")
    elif any(x[v] is not None and type(x[v]) is not bool for v in x):
        errors.append("go_results_type")
    c=r["contract_review"]
    if not isinstance(c,dict) or set(c)!={"verdict","reviewer_id","evidence_refs"}:
        errors.append("contract_review")
    else:
        if c["verdict"] not in REVIEW:
            errors.append("review_verdict")
        if not isinstance(c["reviewer_id"],str) or not c["reviewer_id"].strip():
            errors.append("reviewer_id")
        if not isinstance(c["evidence_refs"],list) or not all(isinstance(z,str) and z.strip() for z in c["evidence_refs"]):
            errors.append("evidence_refs")
        if c["verdict"] in ("ADMISSIBLE","INADMISSIBLE") and not c["evidence_refs"]:
            errors.append("decisive_review_without_evidence")
    return errors

def study_errors(receipts):
    errors=[]
    if not isinstance(receipts,list):
        return ["not_list"]
    seen=set()
    within_block={}
    for i,r in enumerate(receipts):
        e=errors_for_receipt(r)
        errors += [f"record_{i}:{x}" for x in e]
        if e:
            continue
        key=(r["task_id"],r["model_id"])
        invariant=(r["source_commit"],r["task_spec_sha256"],r["tool_budget_id"])
        if key in within_block and within_block[key]!=invariant:
            errors.append(f"record_{i}:treatment_information_confounded")
        within_block.setdefault(key,invariant)
        if r["invocation_id"] in seen:
            errors.append(f"record_{i}:reused_invocation_id")
        seen.add(r["invocation_id"])
    return errors

def manuscript_metrics(receipts):
    """Safe descriptive bookkeeping; never a causal estimate."""
    issues=study_errors(receipts)
    if issues:
        raise ValueError("; ".join(issues))
    synthetic=sum(r["study_kind"]=="synthetic_test" for r in receipts)
    observed=[r for r in receipts if r["study_kind"]=="observed"]
    # No empirical metrics from a fixture-only dataset.
    return {
        "receipts_total":len(receipts),
        "synthetic_receipts_excluded":synthetic,
        "observed_agent_invocations":len(observed),
        "observed_by_arm":dict(Counter(r["arm"] for r in observed)),
        "principle_mentions_in_observed_explanations":
            sum(len(TERMS.findall(r["explanation"])) for r in observed),
        "observed_completed_patches":
            sum(r["run_status"]=="completed" for r in observed),
        "agent_effect_estimate":"NOT_IDENTIFIED",  # no random assignment proof by this receipt layer
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",type=Path,required=True)
    args=p.parse_args()
    data=json.loads(args.input.read_text(encoding="utf8"))
    print(json.dumps(manuscript_metrics(data),ensure_ascii=False,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
