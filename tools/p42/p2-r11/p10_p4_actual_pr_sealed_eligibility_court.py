#!/usr/bin/env python3
"""P10-P4: genuine unread-ID lock and honest dual-theory eligibility court.

Records after reveal do NOT constitute prospective demand-type predictions.
Zero admissible rank predictions is not zero predictive accuracy. Classifier
requires the same executable old/new client contract for both maintained
original Gin/Echo producers and a source-authorized edit grammar.
"""
import json
from collections import Counter
from pathlib import Path

base=Path("tools/p42/p2-r11")
frozen=json.loads((base/"frozen_p10_p4_source_ast_equal_information_rival_and_unread_prs.json").read_text())
reveal=json.loads((base/"p10_p4_actual_chi_mux_16_unread_pr_reveal_and_eligibility.json").read_text())
assert reveal["sealed_prior_to_reading"]=="f2c663787d13c55dfcdbbdf3934de6a8d0426d2b"
ids={(z["repo"],i) for z in frozen["cohort"]["selected"] for i in z["ids"]}
rows=reveal["records"]
observed={(r["repo"],r["pr"]) for r in rows}
assert len(rows)==16 and len(observed)==16 and observed==ids
status=Counter(r["status_as_of_2026_10_17"] for r in rows)
assert status=={"OPEN":11,"CLOSED_UNMERGED":4,"MERGED":1},status
clusters={(r["repo"],r["post_reveal_demand_cluster"]) for r in rows}
assert len(clusters)==15,len(clusters)
known=[r for r in rows if r["related_problem_theme_known_from_preexisting_P9_or_P9Q"]]
assert set((r["repo"],r["pr"]) for r in known)=={
 ("go-chi/chi",1181),("gorilla/mux",815),
 ("gorilla/mux",816),("gorilla/mux",818),("gorilla/mux",820)}
assert any((r["repo"],r["pr"])==("go-chi/chi",1185)
           and r["post_reveal_demand_cluster"]=="chi_discard_flush_effect" for r in rows)
assert all(r["pre_registered_gin_echo_dual_architecture_optional_interface_goal_certified"] is False for r in rows)
# The same source/rights observations and blind-admission grammar are given
# to both our version of HARC and standard classical costed transition systems.
for arm in ("HARC_RC","CLASSICAL_CTLS"):
    assert frozen["judge_models"][arm]["inputs"].startswith("exact same")
admitted=[r for r in rows if r["pre_registered_gin_echo_dual_architecture_optional_interface_goal_certified"]]
assert not admitted
out={
 "protocol":"P10_P4_SEALED_UNREAD_PR_CENSORED_CLASSICAL_EQUAL_INFORMATION",
 "status":"PASS_WITH_ABSTENTION",
 "locked":16,"retrieved":len(rows),"distinct_post_reveal_clusters":len(clusters),
 "known_previously_exposed_problem_theme_PRs":len(known),
 "status_counts":dict(status),
 "rank_eligible":0,"forecasts_graded":0,
 "HARC_RC":"ABSTAIN","CLASSICAL_CTLS":"ABSTAIN",
 "selective_accuracy":"UNDEFINED_NO_ADMISSIBLE_FORECASTS",
 "cross_repo_contract_and_owner_rights":"NOT_CERTIFIED",
 "original_previous_R11_P9_0_of_6":"PRESERVED_UNCHANGED",
 "law_claim":"NONE",
 "note":"PR #1185 contains genuine effect obligations under Discard; Flusher method presence alone is not a complete event trace."
}
path=Path("out/p42-r11-p10-p4/heldout-pr-eligibility.json")
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print("P10_P4_SEALED_CHI_MUX_16_PR_CENSORING_AND_DUAL_ABSTENTION_PASS")
print(json.dumps(out,ensure_ascii=False,sort_keys=True))
