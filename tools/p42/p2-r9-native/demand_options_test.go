package r9

import (
 "testing"
 "google.golang.org/grpc/mem"
)
type backend struct{ puts int; value byte }
func (b *backend)Get(n int)[]byte{return make([]byte,n)}
func (b *backend)Put(v []byte){b.puts++;b.value=v[0]}
type adapter struct{ b *backend }
func (p *adapter)Get(n int)*[]byte {v:=p.b.Get(n);return &v}
func (p *adapter)Put(v *[]byte){if v!=nil{p.b.Put(*v)}}
type shared struct{ storage []byte }
func(p *shared)Get(n int)*[]byte {if len(p.storage)<n{p.storage=make([]byte,n)}; v:=p.storage[:n];return &v}
func(p *shared)Put(_ *[]byte){}
var _ mem.BufferPool=(*adapter)(nil)
var _ mem.BufferPool=(*shared)(nil)
var _ mem.BufferPool=mem.NopBufferPool{}
func TestDemandIndexedProviderAcceptance(t *testing.T){
 cases:=[]struct{name string; pool mem.BufferPool; b *backend; independent,accounted bool}{
  {"default-nop",mem.NopBufferPool{},nil,true,false},
  {"legacy-adapter",&adapter{b:&backend{}},nil,true,true},
  {"shared-provider",&shared{},nil,false,false},
 }
 for i:=range cases{
  c:=&cases[i]
  if a,ok:=c.pool.(*adapter);ok{c.b=a.b}
  t.Run(c.name,func(t *testing.T){
   a:=c.pool.Get(4);(*a)[0]=0x41
   b:=c.pool.Get(4);(*b)[0]=0x42
   independent:=(*a)[0]==0x41
   if independent!=c.independent{t.Fatalf("isolation wrong: %v",independent)}
   c.pool.Put(a);c.pool.Put(b)
   v:=c.pool.Get(4);(*v)[0]=0x5e;c.pool.Put(v)
   accounted:=c.b!=nil&&c.b.puts==3&&c.b.value==0x5e
   if accounted!=c.accounted{t.Fatalf("legacy accounting wrong: %v",accounted)}
   t.Logf("P42_R9_NATIVE_CASE name=%s type=true isolated=%t legacy_accounted=%t",c.name,independent,accounted)
  })
 }
}
