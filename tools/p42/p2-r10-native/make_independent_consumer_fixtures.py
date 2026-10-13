#!/usr/bin/env python3
"""R10-P4 fixture: byte-exact independent consumers, authored access shims only.

Never rewrite the pinned Thanos or OTEL sources. Check git blob SHA of the
downloaded originals in the workflow *before* generating access shims.
"""
from pathlib import Path
ROOT=Path(__file__).resolve().parent
THANOS=ROOT/"external"/"thanos"
OTEL=ROOT/"external"/"otelgrpc"
INTEGRATION=ROOT/"external"/"integration"
def write(d,n,s):
 d.mkdir(parents=True,exist_ok=True)
 (d/n).write_text(s,encoding="utf-8")
def main():
 for orig in ["codec_stringlabels.go","codec_slicelabels.go"]:
  if not (THANOS/orig).exists():raise SystemExit("missing byte-exact remote Thanos original: "+orig)
 if not (OTEL/"encoding.go").exists():raise SystemExit("missing byte-exact remote OTEL original")
 write(THANOS,"r10p4_shim.go",'''// Research-only public access to unchanged real Thanos function.
package extgrpc
import "google.golang.org/grpc/mem"
func R10P4Materialize(data mem.BufferSlice)([]byte,func()){
 return materializeForUnmarshal(data)
}
''')
 write(OTEL,"r10p4_shim.go",'''// Research-only payload/mock interface to execute unchanged OTEL CodecV2.Marshal.
package otelgrpc
import "google.golang.org/grpc/mem"
type r10p4Payload struct{ data []byte }
func (p r10p4Payload) SizeProto() int {return len(p.data)}
func (p r10p4Payload) MarshalProto(dst []byte) int {return copy(dst,p.data)}
func (p r10p4Payload) UnmarshalProto([]byte) error {return nil}
func R10P4Marshal(data []byte)(mem.BufferSlice,error){
 return (&codecV2{}).Marshal(r10p4Payload{data})
}
''')
 write(INTEGRATION,"integration_test.go",r'''package integration
import(
 "bytes"
 "os"
 "testing"
 tham "example.org/evonomos/p42p2r10/external/thanos"
 otel "example.org/evonomos/p42p2r10/external/otelgrpc"
 "google.golang.org/grpc/mem"
)
type trackingPool struct{ puts int }
func (*trackingPool) Get(n int)*[]byte{b:=make([]byte,n);return &b}
func (p *trackingPool) Put(*[]byte){p.puts++}

func TestRealIndependentThanosOtelConsumerOwnershipComposition(t *testing.T) {
 variant:=os.Getenv("R10_P4_TH_TAG")
 if variant!="default" && variant!="slicelabels" {t.Fatalf("unknown test build variant %q",variant)}
 pool:=&trackingPool{}
 first:=mem.Copy(bytes.Repeat([]byte{0x41},2048),pool)
 // Original Thanos materializeForUnmarshal gets this exact one-buffer input.
 b,release:=tham.R10P4Materialize(mem.BufferSlice{first})
 if len(b)!=2048||b[0]!=0x41{t.Fatal("Thanos original client bytes wrong")}
 expectedCleanup:=variant=="default"
 if (release!=nil)!=expectedCleanup{t.Fatalf("Thanos cleanup callback variant=%s nonnil=%t",variant,release!=nil)}
 // Execute two actual OpenTelemetry codec Marshal calls while holding Thanos bytes.
 one,err:=otel.R10P4Marshal(bytes.Repeat([]byte{0x43},2048))
 if err!=nil{t.Fatal(err)}
 two,err:=otel.R10P4Marshal(bytes.Repeat([]byte{0x44},2048))
 if err!=nil{t.Fatal(err)}
 if len(one)!=1||len(two)!=1{t.Fatal("OTEL returned wrong BufferSlice shape")}
 if one[0].Len()!=2048||two[0].Len()!=2048||one[0].ReadOnlyData()[0]!=0x43||two[0].ReadOnlyData()[0]!=0x44||b[0]!=0x41 {
   t.Fatal("cross-consumer outstanding-buffer interference")
 }
 // Only the ORIGINAL source input releases its ownership first.
 first.Free()
 if pool.puts!=0 {t.Fatalf("unexpected Put before consumer cleanup: %d",pool.puts)}
 if release!=nil{release()}
 expectedPut:=0
 if variant=="default"{expectedPut=1}
 if pool.puts!=expectedPut{t.Fatalf("returned to authored tracking backend %d expected %d",pool.puts,expectedPut)}
 // Independent OTEL-owned buffers were not passed through the Thanos pool.
 if one[0].ReadOnlyData()[0]!=0x43||two[0].ReadOnlyData()[0]!=0x44{t.Fatal("OTEL changed after Thanos release")}
 one.Free()
 two.Free()
 t.Logf("R10_P4_REAL_SOURCE_CROSS_MODULE variant=%s thanos_first=65 otel_first=67 otel_second=68 callback=%t thanos_put=%d",variant,expectedCleanup,pool.puts)
}
func TestRealThanosMultiFragmentMaterialization(t *testing.T){
 variant:=os.Getenv("R10_P4_TH_TAG")
 src:=mem.BufferSlice{
   mem.SliceBuffer(bytes.Repeat([]byte{0x41},1024)),
   mem.SliceBuffer(bytes.Repeat([]byte{0x41},1024)),
 }
 data,cleanup:=tham.R10P4Materialize(src)
 if len(data)!=2048||data[0]!=0x41||data[2047]!=0x41{t.Fatal("multi fragment materialization mismatch")}
 if (cleanup!=nil)!=(variant=="default"){t.Fatal("unexpected cleanup in real Thanos alternative")}
 if cleanup!=nil{cleanup()}
 src.Free()
 t.Logf("R10_P4_REAL_SOURCE_MULTIFRAGMENT variant=%s observed=65 length=2048 callback=%t",variant,cleanup!=nil)
}
''')
 print("R10_P4_FIXTURES_MATERIALIZED_WITH_ORIGINAL_SOURCES_UNCHANGED")
if __name__=="__main__":main()
