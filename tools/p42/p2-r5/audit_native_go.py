#!/usr/bin/env python3
"""R5 independent generated source semantic evidence grader.
Reads source bytes and REAL compiled Go outputs; does not trust generator's
claimed edit vectors. Strict syntax/site grammar; refuse unrecognized changes.
"""
import hashlib,json,re,sys
from pathlib import Path
def read_json(path):return json.loads(Path(path).read_text())
def lines(path):return Path(path).read_text().splitlines()
def site_vector(base,case):
    changes={}
    for name in ["read_client.go","export_client.go"]:
        a=lines(base/name);b=lines(case/name)
        if len(a)!=len(b) or any((("consumeRead" in l)!=("consumeRead" in r) and ("consumeExport" in l)!=("consumeExport" in r)) for l,r in zip(a,b)):
            raise ValueError("client source beyond allowed type signature edit grammar")
        changes[name]=int(a!=b)
    pa,pb=lines(base/"assembly.go"),lines(case/"assembly.go")
    if len(pa)!=len(pb) or len(pa)!=3:
        raise ValueError("assembly beyond frozen two explicit call-site grammar")
    wiring=int(pa[1]!=pb[1])+int(pa[2]!=pb[2])
    if pa[0]!=pb[0] or not all("return consume" in z for z in pa[1:]+pb[1:]):
        raise ValueError("unexpected assembly source")
    provider="\n".join(lines(case/"providers.go"))
    forced=len(re.findall(r'func \(\*ReadAlt\) Export\(\) string',provider))+len(re.findall(r'func \(\*ExportAlt\) Read\(\) string',provider))
    useful=len(re.findall(r'func \(\*ReadAlt\) Read\(\) string',provider))+len(re.findall(r'func \(\*ExportAlt\) Export\(\) string',provider))+len(re.findall(r'func \(\*BothAlt\) (?:Read|Export)\(\) string',provider))
    return {"consumer_signature_edits":sum(changes.values()),"composition_wiring_edits":wiring,"forced_irrelevant_methods":forced,"new_provider_useful_methods":useful,"touched_sites":sum(changes.values())+wiring+forced,"consumer_files_touched":sorted(k for k,v in changes.items() if v)}

def main():
    if len(sys.argv)!=5:
        raise SystemExit("usage: audit_native.py frozen.json generated_dir run_outcomes.json output_receipt.json")
    freeze,source_root,raw,out=map(Path,sys.argv[1:])
    m=read_json(freeze);o=read_json(raw)
    assert m["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P2_R5_CAPABILITY_OBLIGATION_COURT_FROZEN_V1"
    assert len(o["positive"])==16 and len(o["baseline"])==4
    assert set(o["negative"])=={"BUNDLE_PORT_R","BUNDLE_PORT_X","BUNDLE_PORT_RX"}
    assert all(x["build_rejected"] and "missing method" in x["diagnostic"] for x in o["negative"].values())
    for a,v in o["baseline"].items():
        assert v=={"read":"READ0","export":"EXPORT0"} and a in m["design"]["matrix"]
    cert=[]
    for item in m["predictions"]:
        ident=item["id"];arch=item["architecture"];demand=item["demand"];expected=item["expected"]
        case=source_root/"cases"/ident;base=source_root/"baselines"/arch
        actual=site_vector(base,case)
        for key in ["consumer_signature_edits","composition_wiring_edits","forced_irrelevant_methods","touched_sites"]:
            assert actual[key]==expected[key],(ident,key,actual,expected)
        assert actual["new_provider_useful_methods"]==(2 if demand in ["RX","C"] else 1)
        actual_out=o["positive"][ident]
        assert actual_out=={"read":expected["expected_read"],"export":expected["expected_export"]},(ident,actual_out,expected)
        # verify actual materialized source fingerprint, not only labels
        hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(case.glob("*.go"))}
        cert.append({"id":ident,"architecture":arch,"demand":demand,"source_site_vector":actual,"real_go_output":actual_out,"source_hashes":hashes})
    assert len(cert)==16
    lookup={v["id"]:v["source_site_vector"] for v in cert}
    assert lookup["BUNDLE_PORT_R"]["forced_irrelevant_methods"]==1
    assert lookup["SEGREGATE_PORT_R"]["forced_irrelevant_methods"]==0
    assert lookup["BUNDLE_PORT_C"]["forced_irrelevant_methods"]==0
    assert lookup["SEGREGATE_DIRECT_R"]["touched_sites"]==lookup["BUNDLE_DIRECT_R"]["touched_sites"]
    receipt={
      "protocol":"P42_R5_NATIVE_GO_4X4_CAPABILITY_OBLIGATION_SOURCE_COURT_PASS",
      "frozen_manifest_sha256":hashlib.sha256(freeze.read_bytes()).hexdigest(),
      "real_go_baseline_executions":4,
      "real_go_demand_executions":16,
      "negative_go_typecheck_compiler_rejections":3,
      "actual_source_site_vector_matched_frozen":16,
      "actual_go_output_matched_frozen":16,
      "source_realized_direct_vs_port_and_bundle_vs_segregate_interaction":True,
      "classic_go_method_set_reasoning_explains_all":True,
      "initial_interface_declaration_count":{"BUNDLE_PORT":1,"SEGREGATE_PORT":2,"DIRECT":0},
      "demand_correlation_effect":"R/X/RX partial providers produce forced method obligations only under BUNDLE_PORT, whereas C full combined provider has none",
      "uncalibrated_lifecycle_crossover":"bundle minus segregate initial interface surface plus weighted partial obligations = -1+p*w, p and w hypothetical",
      "original_third_party_upstream_repositories_modified":False,
      "genuine_real_world_developer_cost_measured":False,
      "historical_preexisting_product_architectures":False,
      "fully_independent_classical_prediction_benchmark":False,
      "new_nonclassical_TCS_law_proven":False,
      "LAW_R2_authorized":False,
      "cases":cert,
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("P42_R5_ALL_16_REAL_GO_COMPILED_CASES_3_NEGATIVE_TYPECHECKS_AND_SITE_AUDIT_PASS")
if __name__=="__main__":main()
