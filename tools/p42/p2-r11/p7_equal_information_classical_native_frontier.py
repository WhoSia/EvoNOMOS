#!/usr/bin/env python3
"""Source-aware *classical* equal-information rival + HARC repair-feasibility audit.
Scored on native original Chi/Gorilla files. Not a mechanized CCR2/Iris proof.
"""
from __future__ import annotations
import json,re,statistics
from pathlib import Path
root=Path("out/p42-r11-p7")
def parse_observations(repo):
    s=(root/f"{repo}-p7-native.log").read_text()
    needle=f"R11_P7_REAL_{repo.upper()}_ORIGINAL_SOURCE_AND_CONTEXT_REPAIR_PASS"
    line=next((v for v in s.splitlines() if needle in v),None)
    if not line:
        raise AssertionError("Native original source assertion missing: "+repo)
    hit=re.search(r"raw=\{(.*?)\}\s+repaired=\{(.*?)\}",line)
    if not hit:
        raise AssertionError("Wrong native result schema "+repo)
    def record(v):
        tokens=[q.split(":",1) for q in v.split(" ") if ":" in q]
        return dict(tokens)
    return {"raw":record(hit[1]),"repaired":record(hit[2])}
result={repo:parse_observations(repo) for repo in ["chi","gorilla"]}
# Baseline uses ONLY previously inspected original source-level facts:
# chi mux.go calls setPathValue, not setPattern; gorilla mux.go exposes
# Vars/CurrentRoute but neither PathValue/Pattern is exported automatically;
# both research handler adapters copy existing request-local route data.
# The *same source facts are available to HARC*, CCR-style refinement
# and this ordinary classical rule system. We do not starve the rival.
classical={}
errors=[]
for repo,phases in result.items():
    for mode,x in phases.items():
        expected={
           "oldCode":"200","oldBody":"OLD","oldCalls":"1",
           "pathCode":"200","sourceValue":"Ada",
           "pathValue":("Ada" if repo=="chi" or mode=="repaired" else ""),
           "pattern":("/users/{userID}" if mode=="repaired" else ""),
           "err":""
        }
        key=repo+":"+mode
        valid=all(x.get(k)==v for k,v in expected.items())
        classical[key]={"source_aware_prediction":expected,"original_native_observation":x,"matches_all_8_observer_fields":valid}
        if not valid:
            errors.append(key)
assert not errors,errors

# Exact finite route-adapter grammar: raw -> adapter, only when research-user
# permits adding a wrapper to the client surface. Actual GitHub maintainer
# institutional permission for hypothetical upstream changes remains UNKNOWN.
def demand_valid(obs,goal):
    return obs["oldCode"]=="200" and obs["oldBody"]=="OLD" and obs["oldCalls"]=="1" and all([
        not goal.get("pathvalue") or obs["pathValue"]=="Ada",
        not goal.get("pattern") or obs["pattern"]=="/users/{userID}"
    ])
goals={
    "old-only":{},
    "independent-985-pathvalue":{"pathvalue":True},
    "independent-986-pattern":{"pattern":True},
    "both-future-apis":{"pathvalue":True,"pattern":True}
}
front={}
for repo in result:
    front[repo]={}
    for name,goal in goals.items():
        distances={}
        for effective_grammar_rights in ["client_adapter_permitted","client_adapter_denied"]:
            options=[]
            if demand_valid(result[repo]["raw"],goal):options.append({"edits":0,"endpoint":"original"})
            if effective_grammar_rights=="client_adapter_permitted" and demand_valid(result[repo]["repaired"],goal):
                options.append({"edits":1,"endpoint":"research_client_adapter"})
            mn=min([x["edits"] for x in options],default=None)
            distances[effective_grammar_rights]=mn
        front[repo][name]=distances
assert front["chi"]["independent-985-pathvalue"]["client_adapter_permitted"]==0
assert front["gorilla"]["independent-985-pathvalue"]["client_adapter_permitted"]==1
assert front["chi"]["independent-986-pattern"]["client_adapter_permitted"]==1
assert front["gorilla"]["independent-986-pattern"]["client_adapter_permitted"]==1
assert front["chi"]["both-future-apis"]["client_adapter_permitted"]==1
assert front["gorilla"]["both-future-apis"]["client_adapter_permitted"]==1
assert front["chi"]["both-future-apis"]["client_adapter_denied"] is None
assert front["gorilla"]["both-future-apis"]["client_adapter_denied"] is None

cost={}
for repo in ["chi","gorilla"]:
    t=(root/f"p7-bench-{repo}.log").read_text()
    points=[tuple(map(float,m.groups())) for m in re.finditer(
        r"BenchmarkR11P7\w+-\d+\s+\d+\s+([\d.]+) ns/op\s+(\d+) B/op\s+(\d+) allocs/op",t
    )]
    assert len(points)==6,(repo,points)
    cost[repo]={
        "ns_median":statistics.median(x[0] for x in points),
        "ns_observations":[x[0] for x in points],
        "bytes_per_op":int(statistics.median(x[1] for x in points)),
        "allocs_per_op":int(statistics.median(x[2] for x in points))
    }
assert cost["chi"]["ns_median"]<cost["gorilla"]["ns_median"]
assert cost["chi"]["bytes_per_op"]<cost["gorilla"]["bytes_per_op"]
assert cost["chi"]["allocs_per_op"]<cost["gorilla"]["allocs_per_op"]

# Finite, exact fragment of classical Myhill-Nerode / labeled action bisimulation:
# the two source states have the same old-only projection, yet differ in
# pathvalue-demand edit frontier. Omitting hidden per-request state loses
# capacity/feature forecast. No new general mathematical theorem.
assert result["chi"]["raw"]["oldBody"]==result["gorilla"]["raw"]["oldBody"]
assert front["chi"]["independent-985-pathvalue"]!=front["gorilla"]["independent-985-pathvalue"]
out={
 "verdict":"R11_P7_REAL_TWO_CORES_POST_REVEAL_PRE_NATIVE_MATRIX_PASSED__EQUAL_INFORMATION_CLASSICAL_PREDICTS_ALL__PHASE_A_ABSTAIN",
 "phase_a_demand_discovery":"ABSTAIN; selected PR 985 and 986 not in frozen classifier; NOT a successful blind demand-sign forecast",
 "phase_b":"Original two core source-level behavior matrix separately frozen AFTER reading PRs and BEFORE native Go test; 4/4 original/restored states, 8 observer fields each, all matched",
 "classical_equal_input":classical,
 "conditional_repair_source_edit_distance_one_adapter_grammar":front,
 "source_core_real_github_rights":"UNKNOWN, don't infer permissions from a past merge; research user grants editing project-authored test adapter only",
 "matched_post_repair_runtime_descriptive_cost_vector":cost,
 "source_provenance":{
   "chi":"67be7d9cafdaeb4e04e887ff78d09e030ee43b00, mux.go blob 6dc1904d9b6b99ab5e5f36c376cf777f512063f6",
   "gorilla":"b4617d0b9670ad14039b2739167fd35a60f557c5, mux.go blob 1e089906fad5715477ba0c785562a43f0d987a8a, route.go blob e8f11df221f089306926ac23775906a4a50cde62",
   "heldout_maintainer_prs":"go-chi/chi #985, #986; actual source feature development tracked in original merge PRs; no claim independent consumer deployments"
 },
 "scope":"One pattern and one static old handler, appending research-only handler wrapper, time/bytes on one CI runner under a specific Go benchmark. Not globally minimal repair, real maintainer authorized upstream patch, causal source architecture advantage, or unique HARC proof power.",
 "rivals":"equal information source-aware classical router semantics/refinement is perfect; CCR 2.0, Iris, DimSum, Simuliris not separately mechanized; information cut known from Parnas, real options Sullivan, automata partition refinement classical"
}
root.mkdir(parents=True,exist_ok=True)
(root/"p7-classical-equal-info-repair-frontiers-costs.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(out["verdict"])
print("repair edit step frontiers:",json.dumps(front,sort_keys=True))
print("matched native cost vectors:",json.dumps(cost,sort_keys=True))
