#!/usr/bin/env python3
"""R10: materialize explicit Go source edits, not just a provider-choice table.

Original grpc-go at 9ab8b625... is checked out read-only by the workflow.
All candidate source files are RESEARCH-AUTHORED; historical consumer
mem.Copy and Buffer.Free remain actual unmodified 2024 grpc source.
"""
from __future__ import annotations

import difflib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FROZEN = HERE.parent / "p2-r10" / "frozen_historical_grpc_consumer_and_repair_graph.json"
OUTPUT = HERE / "generated"

PROVIDER_BASE = """package candidate
type sharedPool struct {
    backing []byte
    puts int
    last byte
}
func (p *sharedPool) Get(n int) *[]byte {
    if len(p.backing)<n {p.backing=make([]byte,n)}
    v:=p.backing[:n]
    return &v
}
func (p *sharedPool) Put(b *[]byte) {
    p.puts++
    if b!=nil && len(*b)>0 {p.last=(*b)[0]}
}
"""

PROVIDER_FIXED = """package candidate
type sharedPool struct {
    backing []byte
    puts int
    last byte
}
func (p *sharedPool) Get(n int) *[]byte {
    v:=make([]byte,n) // P: provider-owner source edit; no outstanding alias
    return &v
}
func (p *sharedPool) Put(b *[]byte) {
    p.puts++
    if b!=nil && len(*b)>0 {p.last=(*b)[0]}
}
"""

ROOT_BASE = """package candidate
import "google.golang.org/grpc/mem"
type selection struct { pool mem.BufferPool; returnCount func()int }
func assemble() selection {
    p:=&sharedPool{}
    return selection{p,func()int{return p.puts}}
}
"""

ROOT_ADAPTER = """package candidate
import "google.golang.org/grpc/mem"
type selection struct { pool mem.BufferPool; returnCount func()int }
func assemble() selection {
    b:=&legacyPool{}
    return selection{&legacyAdapter{b},func()int{return b.puts}}
}
"""

ROOT_NOP = """package candidate
import "google.golang.org/grpc/mem"
type selection struct { pool mem.BufferPool; returnCount func()int }
func assemble() selection {
    return selection{mem.NopBufferPool{},func()int{return 0}}
}
"""

ADAPTER = """package candidate
// Research-authored legacy-backend adaptation, not a historical grpc patch.
type legacyPool struct { puts int; last byte }
func (p *legacyPool) Get(n int) []byte {return make([]byte,n)}
func (p *legacyPool) Put(b []byte) {p.puts++;if len(b)>0{p.last=b[0]}}
type legacyAdapter struct { backend *legacyPool }
func (p *legacyAdapter) Get(n int) *[]byte {
    v:=p.backend.Get(n)
    return &v
}
func (p *legacyAdapter) Put(v *[]byte) {
    if v!=nil {p.backend.Put(*v)}
}
"""

TEST = """package candidate
import (
  "bytes"
  "testing"
  "google.golang.org/grpc/mem"
)
const name = %s
const wantFirst = byte(%d)
const wantReturned = %d
// Original grpc-go mem.Copy -> mem.NewBuffer -> Buffer.Free -> pool.Put.
// The data in original mem.Buffer must remain observable while BOTH
// references are live. Pooling threshold at pinned revision is 1024.
func TestOriginal2024GrpcCopyAndReferenceLifetime(t *testing.T) {
    selected:=assemble()
    var _ mem.BufferPool=selected.pool
    first:=mem.Copy(bytes.Repeat([]byte{0x41},2048),selected.pool)
    second:=mem.Copy(bytes.Repeat([]byte{0x42},2048),selected.pool)
    if first.Len()!=2048||second.Len()!=2048 {t.Fatal("wrong buffer length")}
    observed:=first.ReadOnlyData()[0]
    if observed!=wantFirst {
        t.Fatalf("R10 native mem.Copy first byte got=%%d want=%%d",observed,wantFirst)
    }
    second.Free()
    first.Free()
    if got:=selected.returnCount(); got!=wantReturned {
        t.Fatalf("R10 native Free->Put got=%%d want=%%d",got,wantReturned)
    }
    t.Logf("R10_NATIVE name=%%s first=%%d isolated=%%t returned=%%d",name,observed,observed==0x41,selected.returnCount())
}
"""


# P42-P2-R10-P2 preregistered boundary experiment (sealed after first R10 native PASS).
# Original mem.Copy bypasses the pool when len(data) <= 1024; it uses pool.Get
# and reference-counted Buffer.Free for len(data) > 1024.
BOUNDARY_TEST = """package candidate
import (
  "bytes"
  "testing"
  "google.golang.org/grpc/mem"
)
func TestHistoricalPoolingThresholdBoundary(t *testing.T) {
  cases:=[]struct{size int; wantFirst byte; wantPuts int}{
    {1024,byte(%d),%d},
    {1025,byte(%d),%d},
  }
  for _,tc:=range cases {
    selected:=assemble()
    first:=mem.Copy(bytes.Repeat([]byte{0x41},tc.size),selected.pool)
    second:=mem.Copy(bytes.Repeat([]byte{0x42},tc.size),selected.pool)
    observed:=first.ReadOnlyData()[0]
    if observed!=tc.wantFirst {t.Fatalf("size=%%d first got=%%d want=%%d",tc.size,observed,tc.wantFirst)}
    second.Free()
    first.Free()
    if got:=selected.returnCount(); got!=tc.wantPuts {
       t.Fatalf("size=%%d puts got=%%d want=%%d",tc.size,got,tc.wantPuts)
    }
    t.Logf("R10_BOUNDARY name=%%s size=%%d first=%%d returned=%%d",name,tc.size,observed,selected.returnCount())
  }
}
"""

VARIANTS = {
    "base_shared": {"provider.go": PROVIDER_BASE, "root.go": ROOT_BASE},
    "provider_repair": {"provider.go": PROVIDER_FIXED, "root.go": ROOT_BASE},
    "adapter_repair": {"provider.go": PROVIDER_BASE, "root.go": ROOT_ADAPTER, "adapter.go": ADAPTER},
    "nop_repair": {"provider.go": PROVIDER_BASE, "root.go": ROOT_NOP},
}
EXPECTED_FILES = {"base_shared":[], "provider_repair":["provider.go"],
                  "adapter_repair":["adapter.go","root.go"], "nop_repair":["root.go"]}

def main() -> None:
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    if frozen["protocol"] != "EVONOMOS_P42_P2_R10_HISTORICAL_GRPC_CONSUMER_SOURCE_EDIT_FREEZE_V1":
        raise SystemExit("wrong freeze protocol")
    if sorted(VARIANTS)!=sorted(x["candidate"] for x in frozen["observer"]["expected"]):
        raise SystemExit("candidate set changed after freeze")
    boundary = json.loads((HERE.parent / "p2-r10" / "frozen_threshold_region_and_classical_rival.json").read_text(encoding="utf-8"))
    if boundary["protocol"] != "EVONOMOS_P42_P2_R10_P2_BOUNDARY_REGION_CLASSICAL_RIVAL_FREEZE_V1":
        raise SystemExit("wrong boundary freeze protocol")
    if [x["size"] for x in boundary["predictions"]] != [1024,1025,2048]:
        raise SystemExit("modified threshold contexts")
    OUTPUT.mkdir(parents=True,exist_ok=True)
    receipt=[]
    baseline=VARIANTS["base_shared"]
    for case in frozen["observer"]["expected"]:
        name=case["candidate"]
        target=OUTPUT/name
        target.mkdir(parents=True,exist_ok=True)
        expected_files=set(VARIANTS[name])|{"consumer_test.go","threshold_test.go"}
        for stale in target.glob("*.go"):
            if stale.name not in expected_files: stale.unlink()
        for file, body in VARIANTS[name].items():
            (target/file).write_text(body,encoding="utf-8")
        (target/"consumer_test.go").write_text(TEST%(json.dumps(name),case["first_byte"],2 if case["return_account"] else 0),encoding="utf-8")
        c0,c1=boundary["predictions"][:2]
        (target/"threshold_test.go").write_text(BOUNDARY_TEST%(c0["observed_first"][name],c0["returned_puts"][name],c1["observed_first"][name],c1["returned_puts"][name]),encoding="utf-8")
        actual_changed=sorted(k for k in set(VARIANTS[name])|set(baseline)
                              if VARIANTS[name].get(k)!=baseline.get(k))
        if actual_changed!=EXPECTED_FILES[name]:
            raise SystemExit("invalid source patch path "+name+":"+str(actual_changed))
        receipt.append({"candidate":name,"changed_source_paths":actual_changed,
                        "changed_path_count":len(actual_changed),
                        "predicted_isolation":case["isolation"],
                        "predicted_accounting":case["return_account"]})
        print("R10_SOURCE_REPAIR name=%s changed=%s"%(name,",".join(actual_changed) or "none"))
    (HERE/"r10_materialization_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print("R10_PREREG_AND_SOURCE_EDIT_GRAMMAR_PASS")

if __name__=="__main__":
    main()
