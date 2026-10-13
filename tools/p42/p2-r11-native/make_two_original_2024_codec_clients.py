#!/usr/bin/env python3
"""Extract two byte-for-byte contemporaneous 2024 external CodecV2 source files.

Tests alone are authored. Source files, their packages and methods are unchanged.
"""
import json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
FROZEN=HERE.parent/"p2-r11"/"frozen_p1b_two_real_2024_independent_grpc_consumers.json"
COMMON='''import ("bytes";"testing")
type r11MockVT struct {payload []byte}
func(m *r11MockVT) MarshalToSizedBufferVT(dst []byte)(int,error){return copy(dst,m.payload),nil}
func(m *r11MockVT) UnmarshalVT(src []byte)error{m.payload=append([]byte(nil),src...);return nil}
func(m *r11MockVT) SizeVT()int{return len(m.payload)}
func TestReal2024ExternalCodecSourceWithOriginalGrpc2024(t *testing.T){
 for _,size:=range []int{1024,2048}{
   want:=bytes.Repeat([]byte{0x41},size)
   encoder:=__CODEC__
   data,err:=encoder.Marshal(&r11MockVT{payload:want})
   if err!=nil{t.Fatalf("Marshal size=%d: %v",size,err)}
   if !bytes.Equal(data.Materialize(),want){t.Fatalf("Marshal bad bytes size=%d",size)}
   var out r11MockVT
   if err:=encoder.Unmarshal(data,&out);err!=nil{t.Fatalf("Unmarshal size=%d: %v",size,err)}
   if !bytes.Equal(out.payload,want){t.Fatalf("Decode bad bytes size=%d",size)}
   data.Free()
   t.Logf("R11_P1B_ORIGINAL_EXTERNAL_CODEC_CLIENT name=__NAME__ size=%d old_2024_grpc=true marshal=true unmarshal=true",size)
 }
}
'''
def main():
 if len(sys.argv)!=3:raise SystemExit("Usage: generator.py buildkit_original spicedb_original")
 frozen=json.loads(FROZEN.read_text())
 assert frozen["protocol"]=="EVONOMOS_P42_R11_P1B_TWO_GENUINE_CONTEMPORANEOUS_2024_GRC_GO_CLIENTS_PRESEAL_V1"
 for item,loc in zip(frozen["clients"],sys.argv[1:]):
   src=Path(loc).read_bytes()
   required=[b"google.golang.org/grpc/mem",b"mem.NewBuffer",b"mem.IsBelowBufferPoolingThreshold"]
   if any(x not in src for x in required):raise ValueError("mismatched original historical CodecV2 source")
   name="buildkit" if item["repo"]=="moby/buildkit" else "spicedb"
   target=HERE/"clients"/name
   target.mkdir(parents=True,exist_ok=True)
   (target/"original_codec.go").write_bytes(src)
   test="package "+item["package_name"]+"\n"+COMMON.replace("__CODEC__","codec{}" if name=="buildkit" else "&vtprotoCodec{}").replace("__NAME__",name)
   (target/"real_external_client_test.go").write_text(test)
   print("R11_P1B_EXACT_INDEPENDENT_2024_CODEC_SOURCE name="+name+" bytes="+str(len(src)))
 print("R11_P1B_TWO_HISTORICAL_ORIGINAL_CLIENT_TEST_SOURCES_MATERIALIZED")
if __name__=="__main__":main()
