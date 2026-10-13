package mux_test

import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "testing"
 "github.com/gorilla/mux"
)
type r11p7Observation struct { oldCode int; oldBody string; oldCalls int; pathCode int; sourceValue string; pathValue string; pattern string; err string }
func r11p7GorillaWorld(repair bool) (http.Handler,*r11p7Observation) {
 o:=new(r11p7Observation)
 r:=mux.NewRouter()
 r.HandleFunc("/health",func(w http.ResponseWriter,req *http.Request){
  o.oldCalls++
  w.WriteHeader(200)
  w.Write([]byte("OLD"))
 }).Methods("GET")
 r.HandleFunc("/users/{userID}",func(w http.ResponseWriter,req *http.Request){
  p:=mux.Vars(req)["userID"]
  if repair {
   req.SetPathValue("userID",p)
   rt:=mux.CurrentRoute(req)
   if rt==nil {o.err="missing CurrentRoute"} else {
    s,err:=rt.GetPathTemplate()
    if err!=nil {o.err=err.Error()} else {req.Pattern=s}
   }
  }
  o.sourceValue=p
  o.pathValue=req.PathValue("userID")
  o.pattern=req.Pattern
  w.WriteHeader(200)
  w.Write([]byte("USER"))
 }).Methods("GET")
 return r,o
}
func r11p7ObserveGorilla(repair bool) r11p7Observation {
 r,o:=r11p7GorillaWorld(repair)
 w:=httptest.NewRecorder()
 r.ServeHTTP(w,httptest.NewRequest("GET","/health",nil))
 o.oldCode=w.Code;o.oldBody=w.Body.String()
 w2:=httptest.NewRecorder()
 r.ServeHTTP(w2,httptest.NewRequest("GET","/users/Ada",nil))
 o.pathCode=w2.Code
 return *o
}
func TestR11P7RealGorillaTwoIndependentFutureMaintainerRequirements(t *testing.T){
 a:=r11p7ObserveGorilla(false)
 if a.oldCode!=200 || a.oldBody!="OLD" || a.oldCalls!=1 || a.pathCode!=200 || a.sourceValue!="Ada" || a.pathValue!="" || a.pattern!="" || a.err!="" {
  t.Fatalf("R11_P7_GORILLA_UNMODIFIED_SOURCE_PREDICTION_MISMATCH raw=%+v",a)
 }
 b:=r11p7ObserveGorilla(true)
 if b.oldCode!=200 || b.oldBody!="OLD" || b.oldCalls!=1 || b.pathCode!=200 || b.sourceValue!="Ada" || b.pathValue!="Ada" || b.pattern!="/users/{userID}" || b.err!="" {
  t.Fatalf("R11_P7_GORILLA_RESEARCH_ADAPTER_PREDICTION_MISMATCH repaired=%+v",b)
 }
 t.Logf("R11_P7_REAL_GORILLA_ORIGINAL_SOURCE_AND_CONTEXT_REPAIR_PASS raw=%+v repaired=%+v",a,b)
}
func BenchmarkR11P7GorillaMatchedFutureRequest(b *testing.B) {
 r,_:=r11p7GorillaWorld(true)
 req:=httptest.NewRequest("GET","/users/Ada",nil)
 b.ReportAllocs()
 b.ResetTimer()
 for i:=0;i<b.N;i++ {
  w:=httptest.NewRecorder()
  r.ServeHTTP(w,req.Clone(req.Context()))
  if w.Code!=200 {b.Fatal(fmt.Sprint("bad status",w.Code))}
 }
}
