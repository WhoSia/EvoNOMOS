package chi_test

import (
 "net/http"
 "net/http/httptest"
 "runtime"
 "runtime/debug"
 "testing"

 "github.com/go-chi/chi/v5"
)

func TestR11P9OriginalUnmergedPoisonStrategy(t *testing.T) {
 oldP:=runtime.GOMAXPROCS(1);defer runtime.GOMAXPROCS(oldP)
 oldGC:=debug.SetGCPercent(-1);defer debug.SetGCPercent(oldGC)
 r:=chi.NewRouter()
 var first,second *chi.Context
 count:=0
 r.Get("/users/{id}",func(w http.ResponseWriter,req *http.Request){
  count++
  ctx:=chi.RouteContext(req.Context())
  name:=chi.URLParam(req,"id")
  if name=="Ada" {
   first=ctx
   ctx.PreventReuse() // 2025 genuine contributor PR #1028 source, not admitted upstream
  }
  if name=="Bob" {second=ctx}
  w.WriteHeader(200)
  _,_=w.Write([]byte("OLD"))
 })
 for _,name:=range []string{"Ada","Bob"} {
  w:=httptest.NewRecorder()
  r.ServeHTTP(w,httptest.NewRequest("GET","/users/"+name,nil))
  if w.Code!=200||w.Body.String()!="OLD"{t.Fatalf("Old actual source contract failed %v %q",w.Code,w.Body.String())}
 }
 if count!=2||first==nil||second==nil {t.Fatal("Missing original route contexts")}
 if first==second {t.Fatal("Poisoned original contributor context returned to sync.Pool")}
 if first.URLParam("id")!="Ada"||second.URLParam("id")!="Bob" {
  t.Fatalf("Post-request retained first=%q second=%q",first.URLParam("id"),second.URLParam("id"))
 }
 t.Logf("R11_P9_ORIGINAL_CONTRIBUTOR_POISONED_CONTEXT_NATIVE_PASS old=200/OLD retained=%q independent=%t",first.URLParam("id"),first!=second)
}
var r11p9PoisonSink *chi.Context
func BenchmarkR11P9OriginalContributorPoisonedRequest(b *testing.B) {
 r:=chi.NewRouter()
 r.Get("/users/{id}",func(w http.ResponseWriter,req *http.Request){
  ctx:=chi.RouteContext(req.Context()); ctx.PreventReuse()
  r11p9PoisonSink=ctx
  w.WriteHeader(200); _,_=w.Write([]byte("OLD"))
 })
 request:=httptest.NewRequest("GET","/users/Ada",nil)
 b.ReportAllocs();b.ResetTimer()
 for n:=0;n<b.N;n++ {
  w:=httptest.NewRecorder()
  r.ServeHTTP(w,request.Clone(request.Context()))
  if w.Code!=200 {b.Fatal(w.Code)}
 }
}
