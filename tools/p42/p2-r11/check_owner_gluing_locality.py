#!/usr/bin/env python3
"""Finite model falsification court for R11-P1 source-ownership composition claims.

No Go semantics are being "proved" here. This exhaustively checks specified
finite labelled transition systems and minimal countermodels to endpoint-only
and module-local safety; paper proof is by induction under lift/frame closure.
"""
import itertools,json
from pathlib import Path
V=[(0,0),(1,0),(0,1),(1,1)]
moves={(0,0):[(1,0),(0,1)],(1,0):[(1,1)],(0,1):[(1,1)],(1,1):[]}
routes=[[(0,0),(1,0),(1,1)],[(0,0),(0,1),(1,1)]]
cases=0; full=0; one_good_one_bad=0; bad_endpoint_contexts=0
examples=[]
for compatmask in range(16):
  C={p:bool(compatmask>>i&1) for i,p in enumerate(V)}
  for safemask in range(16):
    S={p:bool(safemask>>i&1) for i,p in enumerate(V)}
    cases+=1
    if not C[(0,0)] or not S[(0,0)]: continue
    admissible=lambda p:C[p] and S[p]
    route_ok=[all(admissible(p) for p in route) for route in routes]
    # Assume/guarantee lifting condition for any source state reached by
    # any *locally enabled* edit in this declared 2 x 2 design grammar.
    full_frame=all(admissible(p) for p in V)
    if full_frame:
      full+=1
      if not all(route_ok):raise AssertionError("frame-lift closure not sufficient")
    if sum(route_ok)==1:
      one_good_one_bad+=1
      if len(examples)<4: examples.append({"J":compatmask,"I":safemask,"routes":route_ok})
    # Same final state (1,1) and new-d outcome, but path can be unsafe.
    if admissible((1,1)) and not all(route_ok):
      bad_endpoint_contexts+=1
if not one_good_one_bad or not bad_endpoint_contexts:raise AssertionError("missing negative")
# Standard k-locality obstruction: the only difference is at graph distance k+1
# from the edited region. Thus any function of the radius-k marked rooted graph
# must map them to same summary although global future repair feasibility differs.
radius_witnesses=[]
for k in range(1,33):
  nodes=list(range(k+2))
  G0={"edges":[(i,i+1) for i in range(k+1)],"reserved":set()}
  G1={"edges":[(i,i+1) for i in range(k+1)],"reserved":{k+1}}
  visible=lambda g:tuple((v,v in g["reserved"]) for v in range(k+1))
  assert visible(G0)==visible(G1)
  future=lambda g:(k+1 not in g["reserved"])
  assert future(G0)!=future(G1)
  radius_witnesses.append(k)
summary={
 "result":"R11_P1_FINITE_GLUING_AND_LOCALITY_COUNTERMODELS_PASS",
 "scope":"256 four-state two-owner compatibility/safety valuations, 32 explicit k-locality witnesses; finite checking NOT new proof of general Go composition theorem",
 "valuations_total":cases,
 "full_frame_closed_models":full,
 "one_safe_one_unsafe_same_endpoint":one_good_one_bad,
 "final_compiles_but_forbidden_prefix_contexts":bad_endpoint_contexts,
 "locality_radius_witnesses":len(radius_witnesses),
 "first_counterexamples":examples,
 "theory":"Inductive all-path lifting under frame closure, and k-neighborhood insufficient to decide arbitrary unbounded global shared-boundary requirement; fully classical contextual/congruence and graph locality phenomena"
}
Path("out/p42-r11/p1-finite-mathematical-court.json").write_text(json.dumps(summary,indent=2)+"\n")
print("R11_P1_256_TWO_OWNER_MODELS_32_LOCALITY_WITNESSES_PASS")
print(json.dumps({k:v for k,v in summary.items() if k not in ("first_counterexamples","theory","scope")}))
