#!/usr/bin/env python3
"""P42 R10-P3: generate real Go source snapshots for each preregistered edit step.

All source changed relative to previous snapshot is research-authored. Actual
2024 grpc-go mem.Copy -> Buffer.Free remains unchanged as the imported client.
"""
from __future__ import annotations
import json
from pathlib import Path
from make_source_variants import PROVIDER_BASE,PROVIDER_FIXED,ROOT_BASE,ROOT_ADAPTER,ROOT_NOP,ADAPTER

ROOT=Path(__file__).resolve().parent
FROZEN=ROOT.parent/"p2-r10"/"frozen_p3_multistep_source_repair_paths.json"
STATES=ROOT/"paths"/"states"
INVALID=ROOT/"paths"/"invalid"

TEST=r'''package candidate
import ("bytes";"testing";"google.golang.org/grpc/mem")
func TestHistoricalGrpcAtStagedSourceCheckpoint(t *testing.T) {
 selectedSmall:=assemble()
 var _ mem.BufferPool=selectedSmall.pool
 a:=mem.Copy(bytes.Repeat([]byte{0x41},1024),selectedSmall.pool)
 b:=mem.Copy(bytes.Repeat([]byte{0x42},1024),selectedSmall.pool)
 small:=a.ReadOnlyData()[0]
 b.Free();a.Free()
 sc:=selectedSmall.returnCount()
 selectedLarge:=assemble()
 x:=mem.Copy(bytes.Repeat([]byte{0x41},2048),selectedLarge.pool)
 y:=mem.Copy(bytes.Repeat([]byte{0x42},2048),selectedLarge.pool)
 large:=x.ReadOnlyData()[0]
 y.Free();x.Free()
 lc:=selectedLarge.returnCount()
 if small!=byte(%d)||sc!=%d||large!=byte(%d)||lc!=%d {
   t.Fatalf("R10_P3 wrong checkpoint %s: small=%%d/%%d large=%%d/%%d",small,sc,large,lc)
 }
 t.Logf("R10_P3_STATE id=%s small=%%d small_puts=%%d large=%%d large_puts=%%d",small,sc,large,lc)
}
'''
def source(n:dict)->dict[str,str]:
    p={"shared":PROVIDER_BASE,"fresh":PROVIDER_FIXED}[n["provider"]]
    r={"shared":ROOT_BASE,"adapter":ROOT_ADAPTER,"nop":ROOT_NOP}[n["root"]]
    d={"provider.go":p,"root.go":r}
    if n["adapter"]:d["adapter.go"]=ADAPTER
    return d

def main()->None:
    manifest=json.loads(FROZEN.read_text())
    assert manifest["protocol"]=="EVONOMOS_P42_P2_R10_P3_SOURCE_LIFETIME_PATH_COMPOSITION_PRESEAL_V1"
    STATES.mkdir(parents=True,exist_ok=True);INVALID.mkdir(parents=True,exist_ok=True)
    generated=[]
    for n in manifest["nodes"]:
        if n["compile"]:
            dest=STATES/n["id"]
        else:
            dest=INVALID/n["id"]
        dest.mkdir(parents=True,exist_ok=True)
        content=source(n)
        if n["compile"]:
            small,large=n["expected"]["small"],n["expected"]["large"]
            content["checkpoint_test.go"]=TEST%(small[0],small[1],large[0],large[1],n["id"],n["id"])
        for existing in dest.glob("*.go"):
            if existing.name not in content:existing.unlink()
        for f,b in content.items():(dest/f).write_text(b)
        generated.append({"id":n["id"],"files":sorted(content),"compiles":n["compile"]})
        print("R10_P3_SOURCE_SNAPSHOT name="+n["id"]+" gofiles="+",".join(sorted(content)))
    (ROOT/"paths"/"snapshot_manifest.json").write_text(json.dumps(generated,indent=2)+"\n")
    print("R10_P3_REAL_GO_SOURCE_SNAPSHOTS_CREATED")

if __name__=="__main__": main()
