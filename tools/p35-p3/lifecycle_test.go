package p35pair

import (
 "bytes"
 "context"
 "io"
 "os"
 "sync"
 "testing"
 "github.com/restic/restic/internal/restic"
)

func TestP35P3LegacyLifecycle(t *testing.T) {
 c:=newComposed();ctx:=context.Background();h:=restic.Handle{Type:restic.PackFile,Name:"reuse"}
 legacy:=[]byte("P35:1:\x00\xfflegacy")
 injectLegacy(t,c,h,legacy)
 if got:=readAll(t,c,h);!bytes.Equal(got,legacy){t.Fatalf("prior bytes %q",got)}
 if err:=c.Save(ctx,h,restic.NewByteReader([]byte("fresh"),c.Hasher()));err!=nil{t.Fatal(err)}
 if !c.write.encoded[h]{t.Fatal("version metadata not written")}
 if got:=readAll(t,c,h);!bytes.Equal(got,[]byte("fresh")){t.Fatal("fresh decode")}
 if err:=c.Remove(ctx,h);err!=nil{t.Fatal(err)}
 if c.write.encoded[h]{t.Fatal("stale marker after Remove")}
 injectLegacy(t,c,h,legacy)
 if got:=readAll(t,c,h);!bytes.Equal(got,legacy){t.Fatal("legacy after Remove")}
 if err:=c.Save(ctx,h,restic.NewByteReader([]byte("new"),c.Hasher()));err!=nil{t.Fatal(err)}
 if err:=c.Delete(ctx);err!=nil{t.Fatal(err)}
 if len(c.write.encoded)!=0{t.Fatal("stale markers after Delete")}
 injectLegacy(t,c,h,legacy)
 if got:=readAll(t,c,h);!bytes.Equal(got,legacy){t.Fatal("legacy after Delete")}
 fi,err:=c.Stat(ctx,h);if err!=nil||fi.Size!=int64(len(legacy)){t.Fatal("metadata mismatch",fi,err)}
 t.Log("P35_P3_REMOVE_DELETE_REUSE_NO_STALE_VERSION=PASS")
}
func TestP35P3ConcurrentSnapshots(t *testing.T){
 c:=newComposed();ctx:=context.Background();h:=restic.Handle{Type:restic.PackFile,Name:"concurrent"}
 first:=[]byte("AAAA");second:=[]byte("BBBBBB")
 if err:=c.Save(ctx,h,restic.NewByteReader(first,c.Hasher()));err!=nil{t.Fatal(err)}
 var group sync.WaitGroup;errors:=make(chan error,100)
 for id:=0;id<4;id++{group.Add(1);go func(id int){defer group.Done();for i:=0;i<150;i++{
  if id<2{data:=first;if i%2==0{data=second};if err:=c.Save(ctx,h,restic.NewByteReader(data,c.Hasher()));err!=nil{errors<-err;return}}
  if id>=2{err:=c.Load(ctx,h,0,0,func(r io.Reader)error{data,e:=io.ReadAll(r);if e!=nil{return e};if !bytes.Equal(data,first)&&!bytes.Equal(data,second){return os.ErrInvalid};return nil});if err!=nil{errors<-err;return}}
 }}(id)}
 group.Wait();close(errors);for err:=range errors{t.Fatal(err)}
 t.Log("P35_P3_ATOMIC_SNAPSHOT_RACE=PASS")
}
