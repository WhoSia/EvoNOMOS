#!/usr/bin/env python3
"""R11 P8 historical proposal census and *classical* costed repair-product theorem finite witness.
No samples imputed; no source-to-Coq claim and no probability estimator from purposive strata.
"""
from pathlib import Path
import json
from itertools import product

src=Path("tools/p42/p2-r11/p8_actual_merged_unmerged_pr_census_and_repair_genealogy.json")
x=json.loads(src.read_text())
cases=x["sample"]
assert len(cases)==6
assert len([z for z in cases if z["state"]=="MERGED"])==2
assert len([z for z in cases if z["state"]=="CLOSED_UNMERGED"])==4
assert len([z for z in cases if z["known_pre_P8"]])==2
assert len({z["cluster"] for z in cases})==5
assert len([z for z in cases if z["source_kind"]=="PRODUCTION_SOURCE"])==4
assert len([z for z in cases if z["source_kind"]=="PRODUCTION_SOURCE" and z["state"]=="MERGED"])==1
assert len([z for z in cases if z["source_kind"]=="PRODUCTION_SOURCE" and z["state"]=="CLOSED_UNMERGED"])==3
assert {z["pr"] for z in cases if not z["known_pre_P8"]}=={1026,1028,782,801}
assert set((z["pr"],z["repo"]) for z in cases)=={
    (985,"go-chi/chi"),(986,"go-chi/chi"),
    (1026,"go-chi/chi"),(1028,"go-chi/chi"),
    (782,"gorilla/mux"),(801,"gorilla/mux")}
extra=x["post_selection_actual_repair_genealogy"]["not_sampled_but_linked"]
assert [z["pr"] for z in extra]==[1033,1157]
assert extra[0]["state"]=="CLOSED_UNMERGED" and extra[1]["state"]=="MERGED"
assert 1028 in extra[1]["closes"] and 1033 in extra[1]["closes"]
assert extra[1]["merge_sha"]=="15767233591fd4267ae99d05299fa3807c375cdd"
assert next(z for z in cases if z["pr"]==782)["approval_observed"] is True

# A *strict and predeclared* one-client-handler adapter grammar cannot address
# documentation wording, shared request-context lifetime or query-separator
# routing-policy changes. These 4 newly read external proposals must not be
# retroactively relabeled as successfully blind-predicted features.
unread=[z for z in cases if not z["known_pre_P8"]]
eligible=[z for z in unread if z["cluster"] in {
    "pathvalue_docs","pattern","registration_chronology","disjoint_route"}]
assert eligible==[]
rank_verdict="NOT_ESTIMABLE_OOD_0_OF_4_UNREAD_CASES"
assert len(unread)==4

# A small finite proof witness for the *classical* independent-product cost
# frontier formula, not a claim of source extraction for Go or JS.
def front(vectors):
    vs=set(tuple(v) for v in vectors)
    return sorted(v for v in vs if not any(
        all(u[j]<=v[j] for j in range(len(v))) and
        any(u[j]<v[j] for j in range(len(v)))
        for u in vs if u!=v
    ))
a=front([(1,2),(2,0)])
b=front([(0,2),(2,0)])
cart=front(tuple(u+v for u,v in zip(pa,pb)) for pa,pb in product(a,b))
assert a==[(1,2),(2,0)]
assert b==[(0,2),(2,0)]
assert cart==[(1,4),(2,2),(4,0)],cart

# A shared one-approval *total* budget is a countermodel to taking the product
# of local cost/reachability frontiers: each separate action is legal under
# local budget 1, combined compulsory pair costs 2 and is illegal.
assert 1<=1 and 1+1>1

out={
    "status":"R11_P8_SELECTED_PUBLIC_PR_SURVIVORSHIP_GENEALOGY_AND_CLASSICAL_REPAIR_PRODUCT_FINITE_PASS",
    "real_purposive_sample":{
        "all_selected_prs":len(cases),"observed_merged":2,
        "closed_unmerged":4,"previously_known_merged":2,
        "newly_unread_closed_unmerged":len(unread),
        "novel_phase_a_eligible":len(eligible),
        "unique_demand_clusters":len({z["cluster"] for z in cases}),
        "production_change_attempts":{"merged":1,"closed_unmerged":3},
        "important_counterexample":"#782 APPROVED by one reviewer but unmerged; #1028 and #1033 closed-unmerged yet same demand integrated in actual merged #1157.",
        "do_not_infer":"Purposive GitHub search not a probability sample. 'closed unmerged' is not a binary failure oracle; proposal lifecycle and technical source repair independent.",
        "pre_reveal_global_rank":rank_verdict,
    },
    "classic_product_frontier":{"module_A_local_pareto":a,"module_B_local_pareto":b,
      "full_independent_repair_pareto":cart,
      "shared_single_owner_approval_budget":"countermodel; local feasibility does not imply both legal"},
    "scholarship":"Known finite set-valued costed transition systems, Minkowski sum + Pareto pruning, separation logic/CCR/Iris strong rivals. No universal new mathematics.",
}
dst=Path("out/p42-r11-p8-structural")
dst.mkdir(parents=True,exist_ok=True)
(dst/"pr-survivorship-and-owner-product-court.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
print(out["status"])
print(json.dumps(out["real_purposive_sample"],sort_keys=True,ensure_ascii=False))
print(json.dumps(out["classic_product_frontier"],sort_keys=True,ensure_ascii=False))
