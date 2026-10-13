#!/usr/bin/env python3
"""Make isolated Go test worlds from a byte-identical original Milvus source file.

Never modifies original grpc-go or Milvus bytes. Only root.go, guard.go and
checkpoint_test.go are authored. Prereg: tools/p42/p2-r11/frozen_p1...
"""
import json
from pathlib import Path
import sys
BASE=Path(__file__).resolve().parent
R=BASE.parent/"p2-r11"/"frozen_p1_independent_milvus_provider_typed_source_paths.json"
root_direct='''package resource
import "google.golang.org/grpc/mem"
func Encode(pool mem.BufferPool, payload []byte, size int) mem.Buffer {
    buf := pool.Get(size)
    copy((*buf)[:size],payload)
    return mem.NewBuffer(buf,pool)
}
'''
root_guard='''package resource
import "google.golang.org/grpc/mem"
func Encode(pool mem.BufferPool, payload []byte, size int) mem.Buffer {
    return writeZeroed(pool,payload,size)
}
'''
guard='''package resource
import "google.golang.org/grpc/mem"
func writeZeroed(pool mem.BufferPool, payload []byte, size int) mem.Buffer {
    buf := pool.Get(size)
    clear((*buf)[:size])
    copy((*buf)[:size],payload)
    return mem.NewBuffer(buf,pool)
}
'''
tests='''package resource
import ("bytes";"testing";"google.golang.org/grpc/mem")
type adversarialDirtyPool struct{}
func (adversarialDirtyPool) Get(n int) *[]byte { b:=bytes.Repeat([]byte{0x99},n); return &b }
func (adversarialDirtyPool) Put(b *[]byte){}
func TestOriginalExternalMilvusPoolWithHistoricalGrpc(t *testing.T) {
    var pool mem.BufferPool = &codecBufferPool{}
    a:=mem.Copy(bytes.Repeat([]byte{0x41},2048),pool)
    b:=mem.Copy(bytes.Repeat([]byte{0x42},2048),pool)
    if a.ReadOnlyData()[0]!=0x41 || b.ReadOnlyData()[0]!=0x42 {
        t.Fatal("unexpected original grpc isolation failure with independent Milvus provider")
    }
    b.Free();a.Free()
    t.Log("R11_P1_EXTERNAL_MILVUS_ORIGINAL_SOURCE_WITH_GRPC_2024_PASS")
}
func TestIndependentOldAndFutureConsumerDemands(t *testing.T) {
    old:=Encode(adversarialDirtyPool{},bytes.Repeat([]byte{0x41},2048),2048)
    if !bytes.Equal(old.ReadOnlyData(),bytes.Repeat([]byte{0x41},2048)) {t.Fatal("old full-overwrite client contract violated")}
    old.Free()
    future:=Encode(adversarialDirtyPool{},bytes.Repeat([]byte{0x41},1024),2048)
    dat:=future.ReadOnlyData()
    suffixZero:=bytes.Equal(dat[1024:],make([]byte,1024))
    suffixDirty:=bytes.Equal(dat[1024:],bytes.Repeat([]byte{0x99},1024))
    future.Free()
    if suffixZero!=__EXPECTED_NEW__ || (suffixZero==suffixDirty) {
        t.Fatalf("R11_P1 unexpected future observation gotZero=%v gotDirty=%v",suffixZero,suffixDirty)
    }
    t.Logf("R11_P1_STATE id=__NAME__ old=true future=%t genuine_external_source=true authored_adversarial_pool=true",suffixZero)
}
'''
def main():
    data=json.loads(R.read_text())
    assert data["protocol"]=="EVONOMOS_P42_R11_P1_INDEPENDENT_REAL_PROVIDER_AND_TYPED_EDIT_PATH_PRESPEC_V1"
    source=Path(sys.argv[1]).read_bytes()
    if b"type codecBufferPool struct" not in source or b"google.golang.org/grpc/mem" not in source:
        raise ValueError("wrong third-party external Go source")
    states={x["name"]:x for x in data["milestones"]}
    for x in data["milestones"]:
        dest=BASE/("invalid" if not x["build"] else "states")/x["name"]
        dest.mkdir(parents=True,exist_ok=True)
        (dest/"codec_buffer_pool.go").write_bytes(source)
        (dest/"root.go").write_text(root_guard if x["name"] in ("guard_selected","root_first") else root_direct)
        if x["name"] in ("guard_prepared","guard_selected"):
            (dest/"guard.go").write_text(guard)
        else:
            (dest/"guard.go").unlink(missing_ok=True)
        if x["build"]:
            test=tests.replace("__EXPECTED_NEW__","true" if x["new"] else "false").replace("__NAME__",x["name"])
            (dest/"checkpoint_test.go").write_text(test)
        print("R11_P1_EXTERNAL_SOURCE_WORLD="+x["name"]+" file_sha_matches="+str((dest/"codec_buffer_pool.go").read_bytes()==source).lower())
    print("R11_P1_THREE_REAL_EXTERNAL_SOURCE_STATES_AND_NEGATIVE_MATERIALIZED")
if __name__=="__main__":main()
