#!/usr/bin/env python3
"""P42-R5 locally authored REAL Go compilation fixtures.
Four source architecture candidates, four frozen demand interventions.
This generates Go source files and real requested adaptations; outcome oracle
must separately inspect generated Go files and execute Go compiler.
Upstream repositories are NOT modified; this is a source-semantic pilot.
"""
import argparse,json
from pathlib import Path

def write(p,s):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(s)

def source_files(arch,demand,with_forced=True):
    kind,dispatch=arch.split("_")
    port=dispatch=="PORT"
    read=("R" in demand or demand=="C")
    export=("X" in demand or demand=="C")
    targets={}
    rt="Core";xt="Core"
    if demand=="C":
        rt=xt="BothAlt"
    else:
        if read:rt="ReadAlt"
        if export:xt="ExportAlt"
    contract=(
       ("type Bundle interface { Read() string; Export() string }\ntype ReadPort = Bundle\ntype ExportPort = Bundle\n"
         if kind=="BUNDLE" else
        "type ReadPort interface { Read() string }\ntype ExportPort interface { Export() string }\n")
       if port else "// DIRECT: no enforced interface boundaries for selected clients.\n"
    )
    targets["contracts.go"]="package main\n"+contract
    targets["core.go"]='''package main
type Core struct{}
func (*Core) Read() string { return "READ0" }
func (*Core) Export() string { return "EXPORT0" }
'''
    for func,typ,call,goal in [
        ("consumeRead","ReadPort" if port else rt,"Read","read"),
        ("consumeExport","ExportPort" if port else xt,"Export","export")]:
        if not port:typ="*"+typ
        targets[goal+"_client.go"]=f"package main\nfunc {func}(p {typ}) string {{ return p.{call}() }}\n"
    targets["assembly.go"]=f'''package main
func readResult() string {{ return consumeRead(&{rt}{{}}) }}
func exportResult() string {{ return consumeExport(&{xt}{{}}) }}
'''
    provider=["package main"]
    if demand=="C":
        provider+=["type BothAlt struct{}",'func (*BothAlt) Read() string { return "READ1" }','func (*BothAlt) Export() string { return "EXPORT1" }']
    else:
        if read:
            provider+=["type ReadAlt struct{}",'func (*ReadAlt) Read() string { return "READ1" }']
            if kind=="BUNDLE" and port and with_forced:provider+=['func (*ReadAlt) Export() string { return "UNUSED_ADAPTER_EXPORT" }']
        if export:
            provider+=["type ExportAlt struct{}",'func (*ExportAlt) Export() string { return "EXPORT1" }']
            if kind=="BUNDLE" and port and with_forced:provider+=['func (*ExportAlt) Read() string { return "UNUSED_ADAPTER_READ" }']
    targets["providers.go"]="\n".join(provider)+"\n"
    targets["main.go"]='''package main
import (
  "encoding/json"
  "fmt"
)
func main(){
  out:=map[string]string{"read":readResult(),"export":exportResult()}
  b,e:=json.Marshal(out)
  if e!=nil {panic(e)}
  fmt.Println(string(b))
}
'''
    targets["go.mod"]="module example.org/evonomos/p42r5case\n\ngo 1.25.0\n"
    return targets

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    m=json.loads(Path(args.manifest).read_text())
    assert m["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P2_R5_CAPABILITY_OBLIGATION_COURT_FROZEN_V1"
    dst=Path(args.out)
    for arch in m["design"]["matrix"]:
        for name,content in source_files(arch,"BASE").items():
            # Baseline is a separate copy compiled by native Go before source replacement.
            write(dst/"baselines"/arch/name,content)
    for c in m["predictions"]:
        case=dst/"cases"/c["id"]
        for name,content in source_files(c["architecture"],c["demand"]).items():
            write(case/name,content)
        if c["architecture"]=="BUNDLE_PORT" and c["demand"] in ("R","X","RX"):
            neg=dst/"negative"/c["id"]
            for name,content in source_files(c["architecture"],c["demand"],with_forced=False).items():
                write(neg/name,content)
    print("P42_R5_16_GO_SOURCES_4_BASELINES_3_NEGATIVE_COMPILER_CONTROLS_GENERATED")

if __name__=="__main__":main()
