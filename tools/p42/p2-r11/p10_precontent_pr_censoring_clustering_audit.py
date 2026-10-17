#!/usr/bin/env python3
"""Read-only P42 R11-P10 truly precontent PR-ID court; classify only after reveal."""
import json
from collections import Counter
from pathlib import Path

base=Path("tools/p42/p2-r11")
pre=json.loads((base/"frozen_p10_gin_echo_independent_source_precontent_pr_court.json").read_text())
post=json.loads((base/"p10_actual_gin_echo_16_PR_precontent_holdout_reveal_and_clustering.json").read_text())
assert post["seal_sha"]=="35a3c8980206d38b4f65c508650336a453ecfbdd"
expected={(q["repo"],i) for q in pre["repositories"] for i in q["sample"]}
rows=post["records"]
actual={(r["repo"],r["pr"]) for r in rows}
assert len(rows)==16 and len(actual)==16 and expected==actual
assert len({r["repo"] for r in rows})==2
assert len([r for r in rows if r["repo"]=="gin-gonic/gin"])==8
assert len([r for r in rows if r["repo"]=="labstack/echo"])==8
counts=Counter(r["status_as_of_2026_10_17"] for r in rows)
assert counts=={"MERGED":5,"OPEN":5,"CLOSED_UNMERGED":6},counts
classes=Counter(r["frozen_taxonomy_domain"] for r in rows)
allowed={"runtime_protocol","resource_or_lifetime","API_semantic","concurrency","documentation","CI_or_metadata","other"}
assert set(classes)<=allowed
runtime=[r for r in rows if r["frozen_taxonomy_domain"] not in ("documentation","CI_or_metadata","other")]
clusters={(r["repo"],r["demand_cluster"]) for r in runtime}
assert len(runtime)==12 and len(clusters)==9,(len(runtime),len(clusters))
assert classes["documentation"]==2 and classes["CI_or_metadata"]==1 and classes["other"]==1
assert all(not r["admissible_for_original_pre_PR_GinEcho_Flush_rank"] for r in rows)
assert post["certified_cross_framework_matched_native_comparisons_from_unseen_PRs"]==0
assert post["certified_pre_exposure_cross_framework_rank_eligibility"]==0
out={"cohort_ids_sealed":16,"runtime_or_api_or_resource_PRs":12,
     "independent_within_project_runtime_demand_clusters":9,
     "certified_pre_exposure_cross_framework_rank_eligible":0,
     "merge_censored_labels":dict(counts),"domains":dict(classes),
     "interpretation":"ABSTAIN; do not compute selective accuracy, no positive ranking coverage",
     "scientific_priority":"CLASSICAL_ADEQUATE; P43 HOLD LAW-R2 NOT_AUTHORIZED"}
path=Path("out/p42-r11-p10/pr-censoring-court.json")
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2)+"\n")
print("P10_PRECONTENT_PR_COHORT_AND_CENSORING_AUDIT_PASS")
print(json.dumps(out,sort_keys=True))
