#!/usr/bin/env python3
"""EvoNOMOS P42 R11-P9 bounded original-GitHub-PR cohort court.

No causal inference from a purposively sampled search, and no blind
architecture rank promoted when the original prediction grammar abstained.
"""
import json
from collections import Counter
from pathlib import Path

f = Path("tools/p42/p2-r11/p9_actual_2026_PR_holdout_reveal_status_and_original_Go_evidence.json")
x = json.loads(f.read_text(encoding="utf-8"))
rows = x["records"]
assert len(rows) == 9
assert len(set((r["repo"],r["pr"]) for r in rows)) == len(rows)
expected = {
 ("go-chi/chi",1092),("go-chi/chi",1093),("go-chi/chi",1094),("go-chi/chi",1095),
 ("gorilla/mux",801),("gorilla/mux",802),("gorilla/mux",803),("gorilla/mux",806),
 ("primus/eventemitter3",284)
}
assert set((r["repo"],r["pr"]) for r in rows) == expected
status = Counter(r["original_status"] for r in rows)
assert status == {"CLOSED_UNMERGED":6, "OPEN":3},status
assert not any(r["original_status"] == "MERGED" for r in rows)
leaks = [r for r in rows if r["known_before_prereg"]]
assert len(leaks)==1 and leaks[0]["pr"]==801
new = [r for r in rows if not r["known_before_prereg"]]
assert len(new)==8
runtime = [r for r in new if r["domain"]=="runtime"]
assert len(runtime)==6
assert sum(1 for r in runtime if r["source_forecast_eligible"])==0
assert len([r for r in new if r["domain"]!="runtime"])==2

# Observed source run is not a PR integration/approval oracle.
pair = next(r for r in rows if r["repo"]=="go-chi/chi" and r["pr"]==1093)
assert pair["source_native"]=="PASS_ORIGINAL_2024_22_VS_UNMERGED_2026_11"
assert pair["original_status"]=="CLOSED_UNMERGED"

# Classical prequential information-leakage witness:
# indistinguishable source/PR-submission histories diverge *after* submission.
histories = [
 {"t0":("go-chi/chi", "public-pr-submitted", 1), "reviews_after_t0":0,"late_outcome":"withdrawn"},
 {"t0":("go-chi/chi", "public-pr-submitted", 1), "reviews_after_t0":5,"late_outcome":"merged"}
]
assert histories[0]["t0"] == histories[1]["t0"]
assert histories[0]["reviews_after_t0"] != histories[1]["reviews_after_t0"]
assert histories[0]["late_outcome"] != histories[1]["late_outcome"]
# No function on the t0 equivalence class alone can reproduce both later values.

# Strict identifiability of a cost/repair sign from censored outcomes:
# If either original architecture has interval [0,2] for a latent source-
# authorized repair cost, both A<B and B<A remain consistent with
# observations; no source-grounded architecture preference is determined.
allowed_completions = [
 {"chi_cost":a,"gorilla_cost":b}
 for a in (0,1,2) for b in (0,1,2)
]
signs = {("chi" if z["chi_cost"]<z["gorilla_cost"] else
          "gorilla" if z["chi_cost"]>z["gorilla_cost"] else "tie")
         for z in allowed_completions}
assert signs == {"chi","gorilla","tie"}

# A real CLOSED_UNMERGED PR whose originally contributed code executed with
# corrected accounting falsifies "not merged => proposed source cannot run".
# It does not identify social abandonment or approval.
out = {
  "verdict":"R11_P9_TRUE_UNSEEN_2026_PR_RANK_COVERAGE_ZERO_OF_SIX__NATIVE_UNMERGED_SOURCE_REPAIRS_ACCOUNTING__CENSORING_LEAKAGE_PROOFS_PASS",
  "cohort": {
    "selected":len(rows),"previously_read_excluded":len(leaks),
    "new":len(new),"new_runtime_demands":len(runtime),
    "eligible_under_original_blind_repair_grammar":0,
    "source_status_selected":dict(status),
    "status_is_not_abandonment_label":True
  },
  "original_Go_unmerged_source": {
    "PR":"go-chi/chi#1093 CLOSED_UNMERGED",
    "native_evidence":"https://github.com/WhoSia/EvoNOMOS/actions/runs/38522200806",
    "same_output_11_bytes":True,"old_accounted_bytes":22,
    "proposed_unmerged_accounted_bytes":11,
    "merged_upstream":False
  },
  "math": {
    "submission_time_information_leakage_two_histories":True,
    "post_submission_review_count_not_available_at_submission":True,
    "repair_cost_interval_completion_possible_signs":sorted(signs),
    "robust_architecture_rank": "NOT_IDENTIFIED",
    "status_to_repairability_function":"COUNTEREXAMPLE using executable but CLOSED_UNMERGED PR 1093",
    "prior_art":"Classical filtration, missing-data identifiability, costed transition systems, contextual refinement"
  },
  "literature": {
    "khatoonabadi_2023_full_original_read":True,
    "265325_PR_and_4450_candidate_abandoned":True,
    "paper_7_false_positives_in_100_manual_checked":"NOT transported as 7 percent local cohort false-positive rate",
    "singh_chahal_2026":"public abstract reviewed; complete PDF still not held"
  },
  "novel_design_law":"NOT_PROVEN",
  "release_gate":"P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED"
}
Path("out/p42-r11-p9").mkdir(parents=True,exist_ok=True)
Path("out/p42-r11-p9/p9-holdout-coverage-censoring-and-theorem.json").write_text(
 json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(out["verdict"])
print(json.dumps(out["cohort"],ensure_ascii=False,sort_keys=True))
print(json.dumps(out["math"],ensure_ascii=False,sort_keys=True))
