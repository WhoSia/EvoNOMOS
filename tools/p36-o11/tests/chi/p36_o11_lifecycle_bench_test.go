package chi

import (
 "fmt"
 "net/http"
 "net/http/httptest"
 "testing"
)

// Retain the last published handler beyond the benchmark loop, so even
// N0000 measures real construction rather than a dead-code eliminated call.
var p36O11Retained http.Handler

// BenchmarkP36O11Lifecycle measures a WHOLE operation: create fresh Q21
// adapter, register two routes, publish Handler, then serve exactly N
// requests. Frozen Q21 test checks semantic correctness separately.
// Time/bytes/allocs are per WHOLE operation, not per HTTP request.
func BenchmarkP36O11Lifecycle(b *testing.B){
 for _,scenario:=range []struct{name,path string}{
  {"single","/members/42"},{"overlap","/members/me"},
 }{
  for _,n:=range []int{0,64,128,256,384,512,1024}{
   b.Run(scenario.name+"/"+fmt.Sprintf("N%04d",n),func(b *testing.B){
    req:=httptest.NewRequest(http.MethodGet,scenario.path,nil)
    var retained http.Handler
    b.ReportAllocs()
    b.ResetTimer()
    for i:=0;i<b.N;i++{
     h,err:=p36O10Build("specificity","PS")
     if err!=nil{b.Fatal(err)}
     for j:=0;j<n;j++{
      rec:=httptest.NewRecorder()
      h.ServeHTTP(rec,req)
     }
     retained=h
    }
    b.StopTimer()
    p36O11Retained=retained
   })
  }
 }
}
