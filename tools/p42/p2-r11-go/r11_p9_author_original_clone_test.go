package chi_test

import (
 "net/http"
 "net/http/httptest"
 "runtime"
 "runtime/debug"
 "testing"

 "github.com/go-chi/chi/v5"
)
func TestR11P9OriginalUnmergedCloneStrategy(t *testing.T){
 oldP:=runtime.GOMAXPROCS(1);defer runtime.GOMAXPROCS(oldP)
 oldGC:=debug.SetGCPercent(-1);defer debug.SetGCPercent(oldGC)
 r:=chi.NewRouter()
 var first, original *chi.Context
 count:=0
 r.Get("/users/{id}",func(w http.ResponseWriter,req *http.Request){
  count++
  ctx:=chi.RouteContext(req.Context())
  if chi.URLParam(req,"id")=="Ada"{
   original=ctx
   first=ctx.Clone() // contributor original PR #1033; done BEFORE handler returns
  }
  w.WriteHeader(200)
  _,_=w.Write([]byte("OLD"))
 })
 for _,name:=range []string{"Ada","Bob"} {
  w:=httptest.NewRecorder()
  r.ServeHTTP(w,httptest.NewRequest("GET","/users/"+name,nil))
  if w.Code!=200||w.Body.String()!="OLD"{t.Fatalf("old source response broken %d %q",w.Code,w.Body.String())}
 }
 if count!=2||first==nil||original==nil {t.Fatal("lost original clone")}
 if first==original||first.URLParam("id")!="Ada"{t.Fatalf("clone future observer wrong %q",first.URLParam("id"))}
 t.Logf("R11_P9_ORIGINAL_CONTRIBUTOR_CLONED_CONTEXT_NATIVE_PASS old=200/OLD clone=%q original_after=%q",first.URLParam("id"),original.URLParam("id"))
}
var r11p9CloneSink *chi.Context
func BenchmarkR11P9OriginalContributorClonedRequest(b *testing.B){
 r:=chi.NewRouter()
 r.Get("/users/{id}",func(w http.ResponseWriter,req *http.Request){
  r11p9CloneSink=chi.RouteContext(req.Context()).Clone()
  w.WriteHeader(200); _,_=w.Write([]byte("OLD"))
 })
 request:=httptest.NewRequest("GET","/users/Ada",nil)
 b.ReportAllocs();b.ResetTimer()
 for n:=0;n<b.N;n++ {
  w:=httptest.NewRecorder()
  r.ServeHTTP(w,request.Clone(request.Context()))
  if w.Code!=200{b.Fatal(w.Code)}
 }
}
