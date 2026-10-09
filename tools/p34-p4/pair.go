package p34pair

import (
 "bytes"
 "context"
 "crypto/sha256"
 "errors"
 "hash"
 "io"
 "os"
 "sort"
 "sync"
 "sync/atomic"

 "github.com/restic/restic/internal/restic"
)

// Both new designs satisfy the exact pre-demand Restic 12-method contract.
// The shared vault deliberately isolates just the coordination difference.
type meta struct{}
func (meta) Location() string { return "p34-inmemory" }
func (meta) Connections() uint { return 1 }
func (meta) Hasher() hash.Hash { return sha256.New() }
func (meta) HasAtomicReplace() bool { return true }
func (meta) IsNotExist(err error) bool { return errors.Is(err,os.ErrNotExist) }
func (meta) Close() error { return nil }

type vault struct {
 mu sync.Mutex
 data map[restic.Handle][]byte
}
func newVault()*vault{return &vault{data:make(map[restic.Handle][]byte)}}
func (s *vault) save(ctx context.Context,h restic.Handle,rd restic.RewindReader)error{
 if err:=ctx.Err();err!=nil{return err}
 if err:=h.Valid();err!=nil{return err}
 b,err:=io.ReadAll(rd);if err!=nil{return err}
 s.mu.Lock();defer s.mu.Unlock();s.data[h]=append([]byte(nil),b...);return nil
}
func (s *vault) load(ctx context.Context,h restic.Handle,n int,off int64,cb func(io.Reader)error)error{
 if err:=ctx.Err();err!=nil{return err}
 s.mu.Lock();b,ok:=s.data[h];b=append([]byte(nil),b...);s.mu.Unlock()
 if !ok{return os.ErrNotExist}
 if off<0||off>int64(len(b))||n<0{return errors.New("invalid range")}
 b=b[off:]
 if n>0&&n<len(b){b=b[:n]}
 return cb(bytes.NewReader(b))
}
func (s *vault) stat(ctx context.Context,h restic.Handle)(restic.FileInfo,error){
 if err:=ctx.Err();err!=nil{return restic.FileInfo{},err}
 s.mu.Lock();defer s.mu.Unlock()
 b,ok:=s.data[h];if !ok{return restic.FileInfo{},os.ErrNotExist}
 return restic.FileInfo{Name:h.Name,Size:int64(len(b))},nil
}
func (s *vault) list(ctx context.Context,typ restic.FileType,cb func(restic.FileInfo)error)error{
 if err:=ctx.Err();err!=nil{return err}
 s.mu.Lock();names:=[]restic.FileInfo{}
 for h,b:=range s.data{if h.Type==typ{names=append(names,restic.FileInfo{Name:h.Name,Size:int64(len(b))})}}
 s.mu.Unlock()
 sort.Slice(names,func(i,j int)bool{return names[i].Name<names[j].Name})
 for _,n:=range names{if err:=ctx.Err();err!=nil{return err};if err:=cb(n);err!=nil{return err}}
 return nil
}
func (s *vault) remove(ctx context.Context,h restic.Handle)error{
 if err:=ctx.Err();err!=nil{return err}
 s.mu.Lock();defer s.mu.Unlock()
 if _,ok:=s.data[h];!ok{return os.ErrNotExist};delete(s.data,h);return nil
}
func (s *vault) delete(ctx context.Context)error{
 if err:=ctx.Err();err!=nil{return err}
 s.mu.Lock();defer s.mu.Unlock();s.data=make(map[restic.Handle][]byte);return nil
}

// DIRECT: each Restic public entry calls the common storage kernel directly.
type direct struct{meta; state *vault}
func newDirect()*direct{return &direct{state:newVault()}}
func (d *direct) Save(c context.Context,h restic.Handle,r restic.RewindReader)error{return d.state.save(c,h,r)}
func (d *direct) Load(c context.Context,h restic.Handle,n int,o int64,f func(io.Reader)error)error{return d.state.load(c,h,n,o,f)}
func (d *direct) Stat(c context.Context,h restic.Handle)(restic.FileInfo,error){return d.state.stat(c,h)}
func (d *direct) List(c context.Context,t restic.FileType,f func(restic.FileInfo)error)error{return d.state.list(c,t,f)}
func (d *direct) Remove(c context.Context,h restic.Handle)error{return d.state.remove(c,h)}
func (d *direct) Delete(c context.Context)error{return d.state.delete(c)}

// COMPOSED: adapter dispatches through four genuinely separate capability units.
// Instrumentation records adapter->unit boundary visits, not CPU time or effort.
type writeUnit struct{state *vault}
type readUnit struct{state *vault}
type indexUnit struct{state *vault}
type deleteUnit struct{state *vault}
func (x *writeUnit) save(c context.Context,h restic.Handle,r restic.RewindReader)error{return x.state.save(c,h,r)}
func (x *readUnit) load(c context.Context,h restic.Handle,n int,o int64,f func(io.Reader)error)error{return x.state.load(c,h,n,o,f)}
func (x *indexUnit) stat(c context.Context,h restic.Handle)(restic.FileInfo,error){return x.state.stat(c,h)}
func (x *indexUnit) list(c context.Context,t restic.FileType,f func(restic.FileInfo)error)error{return x.state.list(c,t,f)}
func (x *deleteUnit) remove(c context.Context,h restic.Handle)error{return x.state.remove(c,h)}
func (x *deleteUnit) delete(c context.Context)error{return x.state.delete(c)}
type composed struct{
 meta
 write *writeUnit
 read *readUnit
 index *indexUnit
 destroy *deleteUnit
 visits int64
}
func newComposed()*composed{
 s:=newVault()
 return &composed{write:&writeUnit{s},read:&readUnit{s},index:&indexUnit{s},destroy:&deleteUnit{s}}
}
func (d *composed) visit(){atomic.AddInt64(&d.visits,1)}
func (d *composed) Save(c context.Context,h restic.Handle,r restic.RewindReader)error{d.visit();return d.write.save(c,h,r)}
func (d *composed) Load(c context.Context,h restic.Handle,n int,o int64,f func(io.Reader)error)error{d.visit();return d.read.load(c,h,n,o,f)}
func (d *composed) Stat(c context.Context,h restic.Handle)(restic.FileInfo,error){d.visit();return d.index.stat(c,h)}
func (d *composed) List(c context.Context,t restic.FileType,f func(restic.FileInfo)error)error{d.visit();return d.index.list(c,t,f)}
func (d *composed) Remove(c context.Context,h restic.Handle)error{d.visit();return d.destroy.remove(c,h)}
func (d *composed) Delete(c context.Context)error{d.visit();return d.destroy.delete(c)}
func (d *composed) boundaryVisits()int64{return atomic.LoadInt64(&d.visits)}
var _ restic.Backend=(*direct)(nil)
var _ restic.Backend=(*composed)(nil)
