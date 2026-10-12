package r8

import (
 "testing"
 "google.golang.org/grpc/mem"
)
type legacyPool struct{ gets,puts int; returned []byte }
func (p *legacyPool) Get(n int) []byte {p.gets++; return make([]byte,n)}
func (p *legacyPool) Put(b []byte){p.puts++;p.returned=append([]byte(nil),b...)}
type adapter struct{old *legacyPool}
func (p *adapter) Get(n int)*[]byte{b:=p.old.Get(n);return &b}
func (p *adapter) Put(b *[]byte){if b!=nil{p.old.Put(*b)}}
type sharedPool struct {shared []byte}
func (p *sharedPool) Get(n int)*[]byte{
 if len(p.shared)<n{p.shared=make([]byte,n)}
 v:=p.shared[:n];return &v
}
func (p *sharedPool) Put(*[]byte){}
var _ mem.BufferPool=(*adapter)(nil)
var _ mem.BufferPool=(*sharedPool)(nil)
func TestTwoOutstandingBuffersTypeDoesNotEnforceIsolation(t *testing.T){
 providers:=[]struct{name string; pool mem.BufferPool; isolated bool}{
  {"normal-adapter",&adapter{old:&legacyPool{}},true},
  {"shared-alias-provider",&sharedPool{},false},
 }
 for _,provider:=range providers{
  t.Run(provider.name,func(t *testing.T){
   a:=provider.pool.Get(4)
   if a==nil||len(*a)!=4{t.Fatal("bad first buffer")}
   (*a)[0]=0x41
   b:=provider.pool.Get(4)
   if b==nil||len(*b)!=4{t.Fatal("bad second buffer")}
   (*b)[0]=0x42
   isolated:=(*a)[0]==0x41
   if isolated!=provider.isolated{t.Fatalf("unexpected alias classification: %s actual=%t",provider.name,isolated)}
   t.Logf("P42_R8_NATIVE_CASE name=%s typechecks=true outstanding_isolated=%t first_byte=%d",provider.name,isolated,(*a)[0])
   provider.pool.Put(a);provider.pool.Put(b)
  })
 }
}
func TestAdapterLegacyRoundtrip(t *testing.T){
 old:=&legacyPool{}
 var pool mem.BufferPool=&adapter{old:old}
 b:=pool.Get(4)
 if b==nil||len(*b)!=4{t.Fatal("adapter length contract")}
 (*b)[0]=0x5e
 pool.Put(b)
 if old.gets!=1||old.puts!=1||len(old.returned)!=4||old.returned[0]!=0x5e{t.Fatalf("legacy pool contract %+v",old)}
 t.Log("P42_R8_NATIVE_CASE name=identity-roundtrip typechecks=true put_mutation_preserved=true get=1 put=1")
}
