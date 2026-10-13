#!/usr/bin/env python3
"""Finite post-evidence audit of HARC projection claims using ACTUAL native Ruby
origin logs produced by unchanged rack/rack source snapshots.

This is neither a proof of all programming languages nor a blind prediction.
It is a replayable bounded countermodel for observation-contract scope.
"""
from pathlib import Path
import json
import itertools

root = Path("out/p42-r11")
records={}
for phase in ("early","mid","late"):
    text=(root/f"{phase}-native.log").read_text()
    objects=[json.loads(line) for line in text.splitlines() if line.startswith("{") and line.endswith("}")]
    assert len(objects)==1,(phase,len(objects))
    x=objects[0]
    assert x["phase"]==phase
    assert x["initial_contract_status"]==200
    assert x["middleware_original_keyword_dispatch"] is True
    records[phase]=x

# Predicates extracted from original Ruby source observations; no hand-entered
# success matrix is used in the checker.
predicate={
    "legacy_void":lambda x:x["initial_contract_status"]==200,
    "future_keyword_api":lambda x:x["new_keyword_builder_options"],
    "historical_expression_return":lambda x:x["expressive_return_app_identity"],
    "command_nil_return":lambda x:x["command_style_return_nil"],
}
satisfaction={k:[phase for phase,x in records.items() if fn(x)] for k,fn in predicate.items()}
assert satisfaction=={
    "legacy_void":["early","mid","late"],
    "future_keyword_api":["mid","late"],
    "historical_expression_return":["early","mid"],
    "command_nil_return":["late"],
},satisfaction
assert "mid" in satisfaction["historical_expression_return"] and "late" not in satisfaction["historical_expression_return"]
assert "late" in satisfaction["command_nil_return"] and "mid" not in satisfaction["command_nil_return"]

# 'Return is nil' is already a client-observable fact; if promised as an
# EXACT normative contract, it cannot freely mutate to self. This is the
# countermodel to inferring flexibility merely from returning nil today.
all_designs=set(records)
valid={}
for size in range(len(predicate)+1):
    for required in itertools.combinations(sorted(predicate),size):
        valid["+".join(required) or "none"]=sorted(
            p for p in records if all(predicate[k](records[p]) for k in required))
        assert set(valid["+".join(required) or "none"]).issubset(all_designs)
for required_str,contained in valid.items():
    subset=set(required_str.split("+")) if required_str!="none" else set()
    for ext_str,ext in valid.items():
        sup=set(ext_str.split("+")) if ext_str!="none" else set()
        if subset.issubset(sup):
            assert set(ext).issubset(contained),(required_str,ext_str)

# A finite model-check of a language-independent separating-boundary lemma:
# if clients observe the environment only through I, then replacing plugin
# with the same I output cannot change them; but changing an observable port
# breaks some possible client and so cannot be universally guaranteed.
interface_vals=(0,1,2)
client_functions=tuple(itertools.product(interface_vals,repeat=len(interface_vals)))
for old_i in interface_vals:
    for new_i in interface_vals:
        for f in client_functions:
            old_obs=f[old_i]
            new_obs=f[new_i]
            if old_i==new_i:
                assert old_obs==new_obs
            if old_i!=new_i:
                # A distinguishing client exists; not ALL clients differ.
                assert any(g[old_i]!=g[new_i] for g in client_functions)
out={
    "status":"R11_P5_NATIVE_GROUNDED_CONTRACT_SCOPE_ANTITONICITY_AND_SEPARATOR_FINITE_PASS",
    "actual_native_rack_sources":records,
    "exact_demand_support":satisfaction,
    "valid_states_for_all_observer_sets":valid,
    "universal_claim_refuted":"nil does not by itself guarantee future return flexibility if clients are contractually entitled to observe nil",
    "theorem_1":"For rights/build-preserving edits, if all client observations factor through stable interface traces I and a permitted replacement preserves those traces, linked old clients remain safe. Proof: compose factorization and interface equality/refinement.",
    "theorem_2":"For old-client contract set C subset Cprime, valid repair paths satisfying Cprime are included in valid paths satisfying C. Proof: every Cprime constraint includes C. Exact strictness requires a witness.",
    "limits":"Finite source-driven Ruby observational checker and finite 3^3 client cut model; actual source evidence from run 38338031170. This is not a general compiler soundness proof, a uniqueness result or new TCS theory."
}
root.mkdir(parents=True,exist_ok=True)
(root/"p5-native-derived-contract-frontier.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
print("R11_P5_NATIVE_GROUNDED_CONTRACT_SCOPE_ANTITONICITY_AND_SEPARATOR_FINITE_PASS")
print({k:v for k,v in satisfaction.items()})
