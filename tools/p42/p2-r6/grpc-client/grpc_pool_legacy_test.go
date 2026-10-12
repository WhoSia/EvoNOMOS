//go:build grpc_pool_legacy

package r6grpc

import(
 "testing"
 "google.golang.org/grpc/mem"
)

type legacyPool struct{}
func (*legacyPool)Get(size int)[]byte{return make([]byte,size)}
func (*legacyPool)Put([]byte){}
func TestOldByteSlicePool(t *testing.T){
 var p mem.BufferPool = &legacyPool{}
 b:=p.Get(4)
 if len(b)!=4 {t.Fatal("incorrect pool")}
 p.Put(b)
 t.Log("R6_GRPC_LEGACY_POOL_INTERFACE_PASS")
}
