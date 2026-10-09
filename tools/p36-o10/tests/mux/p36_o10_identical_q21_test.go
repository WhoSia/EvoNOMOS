package mux

import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "sync"
 "testing"
)
func p36O10Build(policy,history string)(http.Handler,error) {
 p,err:=P36O10NewSelectableRouter(policy)
 if err!=nil{return nil,err}
 order:=[]string{"/members/{id}","/members/me"}
 if history=="SP"{order[0],order[1]=order[1],order[0]}
 for _,pattern:=range order {
  label:="PARAM";if pattern=="/members/me"{label="STATIC"}
  if err=p.Register(pattern,label);err!=nil{return nil,err}
 }
 return p.Handler(),nil
}
func p36O10Probe(handler http.Handler,path string)(int,string) {
 r:=httptest.NewRequest(http.MethodGet,path,nil)
 w:=httptest.NewRecorder()
 handler.ServeHTTP(w,r)
 return w.Code,w.Header().Get("X-P36-O10-Winner")
}
// Same Q21 code is inserted in both original Go packages; only 'package' differs.
func TestP36O10IdenticalQ21(t *testing.T) {
 for _,policy:=range []string{"specificity","chronology"} {
  for _,history:=range []string{"PS","SP"} {
   t.Run(policy+"/"+history,func(t *testing.T){
    handler,err:=p36O10Build(policy,history)
    if err!=nil{t.Fatal(err)}
    winner:="STATIC";if policy=="chronology"&&history=="PS"{winner="PARAM"}
    for i:=0;i<128;i++ {
     for _,tc:=range []struct{path string;code int;tag string}{
      {"/members/me",200,winner},{"/members/42",200,"PARAM"},{"/outside",404,""},
     }{
      gotCode,gotTag:=p36O10Probe(handler,tc.path)
      if gotCode!=tc.code||gotTag!=tc.tag {
       t.Fatalf("P36_O10_Q21_CONTRACT_FAIL policy=%s history=%s trial=%d path=%s code=%d tag=%q wantCode=%d wantTag=%q",
        policy,history,i,tc.path,gotCode,gotTag,tc.code,tc.tag)
      }
     }
    }
   })
  }
 }
}
func TestP36O10InvalidPolicyAndFrozenConfiguration(t *testing.T){
 for _,wrong:=range []string{"","both","STATIC","chronological"} {
  if _,err:=P36O10NewSelectableRouter(wrong);err==nil{t.Fatalf("unsupported policy accepted %q",wrong)}
 }
 p,err:=P36O10NewSelectableRouter("chronology");if err!=nil{t.Fatal(err)}
 for _,wrong:=range []struct{p,label string}{
  {"/outside","BAD"},{"/members/{who}","BAD"},{"/members/me",""},
 }{
  if err:=p.Register(wrong.p,wrong.label);err==nil{t.Fatalf("unsupported registration accepted %q %q",wrong.p,wrong.label)}
 }
 if err:=p.Register("/members/{id}","PARAM");err!=nil{t.Fatal(err)}
 if err:=p.Register("/members/{id}","DUPLICATE");err==nil{t.Fatal("duplicate accepted")}
 if err:=p.Register("/members/me","STATIC");err!=nil{t.Fatal(err)}
 h:=p.Handler()
 if err:=p.Register("/members/me","AFTER");err==nil{t.Fatal("post-publication register accepted")}
 code,tag:=p36O10Probe(h,"/members/me")
 if code!=200||tag!="PARAM"{t.Fatalf("published snapshot changed code=%d tag=%s",code,tag)}
}
func TestP36O10PublishedConcurrency(t *testing.T){
 handler,err:=p36O10Build("specificity","PS");if err!=nil{t.Fatal(err)}
 var group sync.WaitGroup
 mistakes:=make(chan error,8)
 for i:=0;i<8;i++ {
  group.Add(1)
  go func(){
   defer group.Done()
   for j:=0;j<32;j++{
    code,tag:=p36O10Probe(handler,"/members/me")
    if code!=200||tag!="STATIC"{mistakes<-fmt.Errorf("code=%d tag=%s",code,tag);return}
   }
  }()
 }
 group.Wait();close(mistakes)
 for e:=range mistakes{t.Error(e)}
}
func BenchmarkP36O10Dispatch(b *testing.B){
 for _,policy:=range []string{"specificity","chronology"} {
  for _,history:=range []string{"PS","SP"}{
   for _,pathcase:=range []struct{name,path string}{{"overlap","/members/me"},{"single","/members/42"}}{
    b.Run(policy+"/"+history+"/"+pathcase.name,func(b *testing.B){
     h,err:=p36O10Build(policy,history);if err!=nil{b.Fatal(err)}
     request:=httptest.NewRequest(http.MethodGet,pathcase.path,nil)
     b.ReportAllocs();b.ResetTimer()
     for i:=0;i<b.N;i++{w:=httptest.NewRecorder();h.ServeHTTP(w,request)}
    })
   }
  }
 }
}
func BenchmarkP36O10Build(b *testing.B){
 for _,policy:=range []string{"specificity","chronology"}{
  b.Run(policy,func(b *testing.B){
   b.ReportAllocs();b.ResetTimer()
   for i:=0;i<b.N;i++ {
    h,err:=p36O10Build(policy,"PS")
    if err!=nil{b.Fatal(err)}
    if h==nil{b.Fatal("nil handler")}
   }
  })
 }
}
