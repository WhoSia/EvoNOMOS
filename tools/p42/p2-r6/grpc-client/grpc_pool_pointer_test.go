//go:build grpc_pool_pointer

package r6grpc

import(
 "testing"
 "google.golang.org/grpc/mem"
)

type pointerPool struct{}
func (*pointerPool)Get(size int)*[]byte{b:=make([]byte,size);return &b}
func (*pointerPool)Put(*[]byte){}
func TestNewPointerPool(t *testing.T){
 var p mem.BufferPool = &pointerPool{}
 b:=p.Get(4)
 if len(*b)!=4 {t.Fatal("incorrect pool")}
 p.Put(b)
 t.Log("R6_GRPC_POINTER_POOL_INTERFACE_PASS")
}
