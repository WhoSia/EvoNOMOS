package p34pair

import (
 "bytes"
 "context"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "errors"
 "fmt"
 "io"
 "os"
 "reflect"
 "sort"
 "testing"

 "github.com/restic/restic/internal/restic"
)
type event struct {Step string `json:"step"`; Outcome string `json:"outcome"`; Content string `json:"content,omitempty"`}
type report struct {
 Schema string `json:"schema"`
 FrozenSource string `json:"frozen_source"`
 PublicMethodCount int `json:"public_method_count"`
 MandatoryMethods []string `json:"mandatory_methods"`
 CoreCalls int `json:"core_calls"`
 DirectBoundaryVisits int64 `json:"direct_boundary_visits"`
 ComposedBoundaryVisits int64 `json:"composed_boundary_visits"`
 ComposedInnerUnits int `json:"composed_inner_units"`
 TracesEquivalent bool `json:"traces_equivalent"`
 Trace []event `json:"trace"`
 Interpretation string `json:"interpretation"`
 Limitations []string `json:"limitations"`
 Verdict string `json:"verdict"`
}
func outcome(err error)string {
 if err==nil{return "OK"}
 if errors.Is(err,os.ErrNotExist){return "NOT_FOUND"}
 if errors.Is(err,context.Canceled){return "CANCELED"}
 if err.Error()=="STOP_LIST"{return "STOP_LIST"}
 if err.Error()=="STOP_LOAD"{return "STOP_LOAD"}
 return "OTHER:"+err.Error()
}
func checksum(b []byte)string{h:=sha256.Sum256(b);return hex.EncodeToString(h[:8])}
func scenario(t *testing.T,b restic.Backend)([]event,int) {
 t.Helper()
 ctx:=context.Background()
 h:=restic.Handle{Type:restic.PackFile,Name:"alpha"}
 h2:=restic.Handle{Type:restic.PackFile,Name:"beta"}
 h3:=restic.Handle{Type:restic.KeyFile,Name:"key-1"}
 var events []event
 calls:=0
 record:=func(name string,err error,contents []byte){
  row:=event{Step:name,Outcome:outcome(err)}
  if contents!=nil{row.Content=checksum(contents)}
  events=append(events,row)
 }
 save:=func(name string,handle restic.Handle,contents []byte){
  calls++
  err:=b.Save(ctx,handle,restic.NewByteReader(contents,b.Hasher()))
  record(name,err,nil);if err!=nil{t.Fatal(err)}
 }
 save("save_alpha",h,[]byte("abcd"))
 save("save_beta",h2,[]byte("bb"))
 save("save_key",h3,[]byte("secret"))
 calls++
 fi,err:=b.Stat(ctx,h);record("stat_alpha",err,[]byte(fmt.Sprint(fi.Name,":",fi.Size)))
 if err!=nil||fi.Size!=4{t.Fatalf("bad stat: %+v %v",fi,err)}
 full:=[]byte(nil);cbCalls:=0
 calls++
 err=b.Load(ctx,h,0,0,func(r io.Reader)error{
  cbCalls++;var e error;full,e=io.ReadAll(r);return e
 })
 record("load_full",err,full)
 if err!=nil||cbCalls!=1||!bytes.Equal(full,[]byte("abcd")){t.Fatalf("full load broken: calls=%d, err=%v",cbCalls,err)}
 partial:=[]byte(nil);calls++;cbCalls=0
 err=b.Load(ctx,h,2,1,func(r io.Reader)error{cbCalls++;var e error;partial,e=io.ReadAll(r);return e})
 record("load_partial",err,partial)
 if err!=nil||cbCalls!=1||!bytes.Equal(partial,[]byte("bc")){t.Fatalf("partial load: %s",partial)}
 var listed []string;calls++
 err=b.List(ctx,restic.PackFile,func(fi restic.FileInfo)error{
  listed=append(listed,fmt.Sprintf("%s:%d",fi.Name,fi.Size));return nil
 })
 record("list_pack",err,[]byte(fmt.Sprint(listed)))
 if err!=nil||!reflect.DeepEqual(listed,[]string{"alpha:4","beta:2"}){t.Fatalf("list mismatch: %v %v",listed,err)}
 called:=0;calls++
 err=b.List(ctx,restic.PackFile,func(fi restic.FileInfo)error{called++;return errors.New("STOP_LIST")})
 record("list_early_error",err,nil)
 if outcome(err)!="STOP_LIST"||called!=1{t.Fatalf("list error contract %v %d",err,called)}
 calls++;cbCalls=0
 err=b.Load(ctx,restic.Handle{Type:restic.PackFile,Name:"absent"},0,0,func(r io.Reader)error{cbCalls++;return nil})
 record("load_missing",err,nil)
 if !b.IsNotExist(err)||cbCalls!=0{t.Fatalf("missing load callback called")}
 calls++;cbCalls=0
 err=b.Load(ctx,h,0,0,func(r io.Reader)error{cbCalls++;return errors.New("STOP_LOAD")})
 record("load_callback_error",err,nil)
 if outcome(err)!="STOP_LOAD"||cbCalls!=1{t.Fatalf("load error: %v %d",err,cbCalls)}
 canceled,cancel:=context.WithCancel(ctx);cancel()
 calls++
 err=b.Save(canceled,h,restic.NewByteReader([]byte("SHOULD_NOT_WRITE"),b.Hasher()))
 record("save_cancelled",err,nil)
 if !errors.Is(err,context.Canceled){t.Fatal("cancellation ignored")}
 save("save_overwrite",h,[]byte("abcdef"))
 calls++;fi,err=b.Stat(ctx,h);record("stat_overwrite",err,[]byte(fmt.Sprint(fi.Name,":",fi.Size)))
 if err!=nil||fi.Size!=6{t.Fatal("overwrite not atomic")}
 calls++;err=b.Remove(ctx,h2);record("remove_beta",err,nil)
 if err!=nil{t.Fatal(err)}
 calls++;err=b.Remove(ctx,h2);record("remove_missing",err,nil)
 if !b.IsNotExist(err){t.Fatal("missing remove must fail")}
 calls++;err=b.Delete(ctx);record("delete_all",err,nil)
 if err!=nil{t.Fatal(err)}
 calls++;fi,err=b.Stat(ctx,h);record("stat_after_delete",err,nil)
 if !b.IsNotExist(err){t.Fatal("delete did not clear state")}
 listAfter:=0;calls++
 err=b.List(ctx,restic.PackFile,func(fi restic.FileInfo)error{listAfter++;return nil})
 record("list_after_delete",err,[]byte(fmt.Sprint(listAfter)))
 if err!=nil||listAfter!=0{t.Fatal("delete list incorrect")}
 if len(events)!=calls{t.Fatalf("event/call mismatch %d vs %d",len(events),calls)}
 return events,calls
}
func TestP34NewPairedRealResticInterface(t *testing.T){
 d:=newDirect();c:=newComposed()
 a,n0:=scenario(t,d)
 b,n1:=scenario(t,c)
 if n0!=n1||!reflect.DeepEqual(a,b){t.Fatalf("PUBLIC CONTRACT DIVERGENCE direct=%v composed=%v",a,b)}
 if c.boundaryVisits()!=int64(n1){t.Fatalf("internal adapter-unit visits expected %d got %d",n1,c.boundaryVisits())}
 if len(a)<15{t.Fatal("coverage too short")}
 methods:=[]string{"Save","Load","Stat","List","Remove","Delete"}
 sort.Strings(methods)
 out:=report{
  Schema:"P34_P4_NEW_RESTIC_COMPATIBLE_PAIRED_ADAPTERS_V1",
  FrozenSource:"restic/restic@495982232cf1af184eac0a97871ef8161e8708ee",
  PublicMethodCount:12,MandatoryMethods:methods,
  CoreCalls:n0,DirectBoundaryVisits:0,ComposedBoundaryVisits:c.boundaryVisits(),
  ComposedInnerUnits:4,TracesEquivalent:true,Trace:a,
  Interpretation:"Actual Go implementations compile against frozen restic.Backend, share storage core, and differ only in explicit capability dispatch topology. Internal visits are structural indirection, NOT observed developer time.",
  Limitations:[]string{"Independent P34 fixture, not original P12 OCI or OneDrive implementations","Shared vault intentionally matches algorithmic semantics; no maintenance cost or source-edit causal advantage measured","Not the entire upstream Restic backend conformance suite or production storage world","The deterministic per-step trace and callback checks are bounded; no unbounded concurrent temporal refinement"},
  Verdict:"P34_P4_PAIRED_RESTIC_SOURCE_IMPLEMENTATIONS_PASS__PUBLIC_TRACE_EQUAL__COMPOSITION_DISPATCH_MEASURED__MAINTENANCE_COST_HOLD",
 }
 if dst:=os.Getenv("P34_REPORT");dst!=""{
  raw,err:=json.MarshalIndent(out,"","  ");if err!=nil{t.Fatal(err)}
  if err:=os.WriteFile(dst,append(raw,10),0644);err!=nil{t.Fatal(err)}
 }
 t.Logf("P34_P4_RESTIC_PAIR_PASS calls=%d direct_visits=0 composed_visits=%d trace_equal=true",n0,c.boundaryVisits())
}

type wideningReport struct {
 Schema string `json:"schema"`
 Precommit string `json:"precommit"`
 InitialContract []string `json:"initial_contract"`
 WidenedContract []string `json:"widened_contract"`
 Phase0PublicCalls int `json:"phase0_public_calls"`
 Phase1PublicCalls int `json:"phase1_public_calls"`
 Phase0ComposedVisits int64 `json:"phase0_composed_visits"`
 Phase1ComposedVisits int64 `json:"phase1_composed_visits"`
 TracesIdentical bool `json:"traces_identical"`
 ContractWideningTested bool `json:"contract_widening_tested"`
 SourceChangeCostMeasured bool `json:"source_change_cost_measured"`
 Outcome string `json:"outcome"`
}
func wideningScenario(t *testing.T,b restic.Backend)(p0,p1 []string) {
 t.Helper()
 ctx:=context.Background()
 h:=restic.Handle{Type:restic.PackFile,Name:"evolving-item"}
 if err:=b.Save(ctx,h,restic.NewByteReader([]byte("value"),b.Hasher()));err!=nil{t.Fatal(err)}
 p0=append(p0,"Save:OK")
 var got []byte
 err:=b.Load(ctx,h,0,0,func(r io.Reader)error{var e error;got,e=io.ReadAll(r);return e})
 if err!=nil||!bytes.Equal(got,[]byte("value")){t.Fatal("D0 Load failed",err)}
 p0=append(p0,"Load:"+checksum(got))
 meta,err:=b.Stat(ctx,h)
 if err!=nil||meta.Size!=5{t.Fatal("D1 Stat failed")}
 p1=append(p1,fmt.Sprintf("Stat:%d",meta.Size))
 n:=0
 err=b.List(ctx,restic.PackFile,func(fi restic.FileInfo)error{n++;return nil})
 if err!=nil||n!=1{t.Fatal("D1 List failed")}
 p1=append(p1,"List:1")
 if err=b.Remove(ctx,h);err!=nil{t.Fatal("D1 Remove failed")}
 p1=append(p1,"Remove:OK")
 if err=b.Delete(ctx);err!=nil{t.Fatal("D1 Delete failed")}
 p1=append(p1,"Delete:OK")
 _,err=b.Stat(ctx,h)
 if !b.IsNotExist(err){t.Fatal("D1 final absence failed")}
 p1=append(p1,"StatAfterDelete:NOT_FOUND")
 return p0,p1
}
func TestP34DemandWideningAcrossSameAdapters(t *testing.T) {
 d:=newDirect();c:=newComposed()
 d0,d1:=wideningScenario(t,d)
 c0,c1:=wideningScenario(t,c)
 if !reflect.DeepEqual(d0,c0)||!reflect.DeepEqual(d1,c1){t.Fatal("demand-indexed traces diverged")}
 if len(d0)!=2||len(d1)!=5||c.boundaryVisits()!=7{t.Fatalf("incorrect temporal trace width: %d %d visits=%d",len(d0),len(d1),c.boundaryVisits())}
 r:=wideningReport{
  Schema:"P34_P4B_REAL_RESTIC_DEMAND_INDEXED_CLIENT_TRANSITION_V1",
  Precommit:"P34_P4_PAIRED_RESTIC_BACKEND_PRECOMMIT.md P4b registered before this test",
  InitialContract:[]string{"Save","Load"},
  WidenedContract:[]string{"Save","Load","Stat","List","Remove","Delete"},
  Phase0PublicCalls:2,Phase1PublicCalls:5,
  Phase0ComposedVisits:2,Phase1ComposedVisits:5,
  TracesIdentical:true,ContractWideningTested:true,SourceChangeCostMeasured:false,
  Outcome:"P34_P4B_DEMAND_WIDENING_TRACE_PASS__NO_SOURCE_CHANGE_COST_CLAIM",
 }
 if dst:=os.Getenv("P34_PHASE_REPORT");dst!=""{
  raw,e:=json.MarshalIndent(r,"","  ");if e!=nil{t.Fatal(e)}
  if e=os.WriteFile(dst,append(raw,10),0644);e!=nil{t.Fatal(e)}
 }
 t.Logf("P34_P4B_CLIENT_CONTRACT_WIDENING=PASS phase0=2 phase1=5 composed_visits=7")
}
