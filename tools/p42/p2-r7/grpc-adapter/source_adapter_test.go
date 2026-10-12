package r7adapter
import (
 "testing"
 "google.golang.org/grpc/mem"
)
type oldBytePool struct{ getCount,putCount int; lastReturned []byte }
func (p *oldBytePool) Get(size int) []byte {
 p.getCount++
 return make([]byte,size)
}
func (p *oldBytePool) Put(b []byte) {
 p.putCount++
 p.lastReturned=append([]byte(nil),b...)
}
type adaptedPool struct {legacy *oldBytePool}
func (p *adaptedPool) Get(size int) *[]byte {
 b:=p.legacy.Get(size)
 return &b
}
func (p *adaptedPool) Put(b *[]byte) {
 if b == nil {return}
 p.legacy.Put(*b)
}
var _ mem.BufferPool = (*adaptedPool)(nil)
func TestPostHistoricalGrpcPointerPoolAdapterPreservesSelectedRoundTrip(t *testing.T){
 old:=&oldBytePool{}
 actual:=mem.BufferPool(&adaptedPool{legacy:old})
 b:=actual.Get(4)
 if b==nil||len(*b)!=4 {t.Fatal("incompatible adapter output")}
 (*b)[0]=0x5e
 actual.Put(b)
 if old.getCount!=1||old.putCount!=1||len(old.lastReturned)!=4||old.lastReturned[0]!=0x5e{
  t.Fatalf("selected old round trip lost: %+v",old)
 }
 t.Log("P42_R7_POST_GRPC_LEGACY_POOL_ADAPTER_NATIVE_COMPILE_AND_SELECTED_ROUNDTRIP_PASS")
}
