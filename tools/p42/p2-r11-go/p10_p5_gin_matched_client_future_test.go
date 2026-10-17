package gin

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

// A research-owned client writer deliberately hides the optional method set.
type evonomosP5BasicOnlyWriter struct{ http.ResponseWriter }

func TestEvoNOMOSP5GinMatchedFutureContract(t *testing.T) {
 SetMode(TestMode)
 r:=New()
 r.GET("/old",func(c *Context){c.String(http.StatusOK,"old")})
 old:=httptest.NewRecorder()
 r.ServeHTTP(old,httptest.NewRequest(http.MethodGet,"/old",nil))
 if old.Code!=200||old.Body.String()!="old"{t.Fatalf("old contract %d %q",old.Code,old.Body.String())}

 // An unmodified application has no /capability route.
 before:=httptest.NewRecorder()
 r.ServeHTTP(before,httptest.NewRequest(http.MethodGet,"/capability",nil))
 if before.Code!=404{t.Fatalf("zero-edit application already satisfies demand? status=%d",before.Code)}

 // ONE research-owned handler registration, no maintained Gin source changed.
 r.GET("/capability",func(c *Context){
  u,ok:=interface{}(c.Writer).(interface{Unwrap() http.ResponseWriter})
  if !ok{t.Fatal("pinned real Gin middleware exposes no Unwrap")}
  underlying:=u.Unwrap()
  has:=false
  if _,ok:=underlying.(http.Flusher);ok{has=true}
  observed:="absent"
  if has{observed="present"}
  c.Header("X-EvoNOMOS-Underlying-Flusher",observed)
  c.String(http.StatusOK,"probe")
 })
 for _,tc:=range []struct{name string;capable bool}{
  {"flusher-present",true},{"flusher-absent",false},
 }{
  t.Run(tc.name,func(t *testing.T){
   recorder:=httptest.NewRecorder()
   var incoming http.ResponseWriter=recorder
   if !tc.capable{incoming=&evonomosP5BasicOnlyWriter{ResponseWriter:recorder}}
   _,actual:=incoming.(http.Flusher)
   if actual!=tc.capable{t.Fatal("writer capability precondition failure")}
   r.ServeHTTP(incoming,httptest.NewRequest(http.MethodGet,"/capability",nil))
   expected:="absent"
   if tc.capable{expected="present"}
   if recorder.Code!=200||recorder.Body.String()!="probe"||
       recorder.Header().Get("X-EvoNOMOS-Underlying-Flusher")!=expected||recorder.Flushed{
    t.Fatalf("new contract sourceCapable=%t code=%d body=%q header=%q flushed=%t",
     tc.capable,recorder.Code,recorder.Body.String(),recorder.Header().Get("X-EvoNOMOS-Underlying-Flusher"),recorder.Flushed)
   }
   oldAfter:=httptest.NewRecorder()
   r.ServeHTTP(oldAfter,httptest.NewRequest(http.MethodGet,"/old",nil))
   if oldAfter.Code!=200||oldAfter.Body.String()!="old"{
    t.Fatalf("protected old contract changed under %s",tc.name)
   }
   t.Logf("P5_GIN_NEW_OWNED_HANDLER sourceCapable=%t header=%s code200 probe noTransportFlush=true oldGET=true",tc.capable,expected)
  })
 }
}
