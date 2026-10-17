#!/usr/bin/env python3
"""Real Chi #1185: certificate that the capability-only quotient is unsound.

Takes actual pinned Go run logs, not invented expected outcomes. The
mathematical nonfactorization is an ordinary witness argument; type-set
and selected HTTP-output equality is scoped to tests, not all clients.
"""
import argparse
import json
import re
from pathlib import Path

LINE=re.compile(
    r"CHI1185_NATIVE phase=(baseline|merged) discard=(true|false) "
    r"mechanism=(direct|ResponseController) wrapper=flushWriter "
    r"hasFlusher=true wrapperStatus=200 wrapperBytes=0 bodyBytes=0 "
    r"transportFlush=(true|false)"
)

def parse(path):
    text=Path(path).read_text()
    assert "--- PASS: TestEvoNOMOSP10P4QAuthenticChi1185DiscardFlushEffect" in text
    observed={}
    for match in LINE.finditer(text):
        phase,discard,mechanism,transport=match.groups()
        key=(phase,discard=="true",mechanism)
        assert key not in observed,key
        observed[key]=transport=="true"
    return observed

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--old",required=True)
    p.add_argument("--merged",required=True)
    p.add_argument("--out",required=True)
    args=p.parse_args()
    old=parse(args.old)
    merged=parse(args.merged)
    obs=dict(old)
    assert not (set(old)&set(merged))
    obs.update(merged)
    expected={(phase,discard,mechanism) for phase in ("baseline","merged")
              for discard in (False,True)
              for mechanism in ("direct","ResponseController")}
    assert set(obs)==expected,(set(obs),expected)
    witness=[]
    for mechanism in ("direct","ResponseController"):
        # The cap-only projection also includes tested status/body/count
        # and the Discard input bit; it intentionally does not include
        # source revision's flush effect.
        for discard in (False,True):
            q={"concrete_wrapper":"flushWriter","has_optional_Flusher":True,
               "discard":discard,"wrapper_status":200,
               "accounted_bytes":0,"response_body_bytes":0,
               "client_call":mechanism}
            a=obs["baseline",discard,mechanism]
            b=obs["merged",discard,mechanism]
            if discard:
                assert a and not b,("missing nonfactorization witness",mechanism)
                witness.append({"same_capability_and_selected_http_projection":q,
                                "underlying_transport_flush_before":a,
                                "underlying_transport_flush_after":b})
            else:
                assert a and b,("passthrough control failed",mechanism)
    assert len(witness)==2
    # Exhaustively derive the least observed source features necessary to
    # predict the actual native transport event, not a hand-chosen quotient.
    from itertools import combinations
    source_worlds=[]
    for (revision,discard,invocation),transport in sorted(obs.items()):
        source_worlds.append({
            "revision":revision,
            "discard":discard,
            "invocation":invocation,
            "method_has_flusher":True,
            "wrapper_status":200,
            "body_bytes":0,
            "transport_flush":transport,
        })
    coordinates=("revision","discard","invocation",
                 "method_has_flusher","wrapper_status","body_bytes")
    sufficient=[]
    for k in range(len(coordinates)+1):
        for subset in combinations(coordinates,k):
            fibers={}
            for world in source_worlds:
                key=tuple(world[c] for c in subset)
                fibers.setdefault(key,set()).add(world["transport_flush"])
            if all(len(vals)==1 for vals in fibers.values()):
                sufficient.append(subset)
    minimal=[c for c in sufficient if not any(
        set(other)<set(c) for other in sufficient)]
    assert minimal==[("revision","discard")],minimal
    # Both dimensions are necessary on the observed complete 2x2x2 grid.
    assert ("revision",) not in sufficient and ("discard",) not in sufficient
    out={
      "verdict":"P10_P4Q_AUTHENTIC_SOURCE_EFFECT_NONFACTORING_WITNESS_PASS",
      "projector":"wrapper Go method set + tested HTTP status/body/counter + explicit Discard state + invocation form, EXCLUDING source-dependent transport effect",
      "counterexample":witness,
      "tested_worlds":len(source_worlds),
      "tested_candidate_coordinate_subsets":2**len(coordinates),
      "minimal_effect_predicting_feature_sets":[list(c) for c in minimal],
      "minimality_domain":"ONLY 8 tested real Go source-state-invocation combinations and listed candidate input features; no arbitrary program equivalence",
      "classical_proof":"Same projected input but different required event observation refutes existence of a deterministic projection-only event predictor for this pair. Adding revision/effect policy distinguishes them.",
      "code_provenance":"Original Chi baseline b1c9ab47626cc46b34393ad4d35779c4363c4e1e vs real merged contributed head 9b3e51c349f3fa6cf120ae786a2835e89e81da2e; exact Git blobs verified by workflow",
      "source_read_before_native":True,
      "blind_future_PR_forecast":False,
      "all_clients_certified":False,
      "source_owner_rights":"UNKNOWN_FOR_RESEARCHER",
      "equal_information_classical_effect_LTS":"EXPLAINS_WITNESS",
      "new_universal_law":"NOT_PROVEN"
    }
    dest=Path(args.out)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(out["verdict"])
    print("P10_P4Q_TWO_REAL_GO_TRACE_WITNESSES_AND_NONDISCARD_CONTROLS_PASS")

if __name__=="__main__":
    main()
