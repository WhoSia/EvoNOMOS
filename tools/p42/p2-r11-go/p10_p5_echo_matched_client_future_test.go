package p5client

import (
 "net/http"
 "net/http/httptest"
 "testing"

 echo "github.com/labstack/echo/v5"
)

type evonomosP5BasicOnlyWriter struct{ http.ResponseWriter }

func TestEvoNOMOSP5EchoMatchedFutureContract(t *testing.T){
 e:=echo.New()
 e.GET("/old",func(c *echo.Context)error{return c.String(200,"old")})
 old:=httptest.NewRecorder()
 e.ServeHTTP(old,httptest.NewRequest("GET","/old",nil))
 if old.Code!=200||old.Body.String()!="old"{t.Fatalf("old contract %d %q",old.Code,old.Body.String())}
 before:=httptest.NewRecorder()
 e.ServeHTTP(before,httptest.NewRequest("GET","/capability",nil))
 if before.Code!=404{t.Fatalf("baseline unexpected /capability code=%d",before.Code)}

 // Exactly one researcher-owned route handler in a client package.
 e.GET("/capability",func(c *echo.Context)error{
  u,ok:=c.Response().(interface{Unwrap()http.ResponseWriter})
  if !ok{t.Fatal("pinned Echo writer has no Unwrap")}
  _,capable:=u.Unwrap().(http.Flusher)
  v:="absent"
  if capable{v="present"}
  c.Response().Header().Set("X-EvoNOMOS-Underlying-Flusher",v)
  return c.String(200,"probe")
 })
 for _,tc:=range []struct{name string;capable bool}{
  {"flusher-present",true},{"flusher-absent",false},
 }{
  t.Run(tc.name,func(t *testing.T){
   recorder:=httptest.NewRecorder()
   var incoming http.ResponseWriter=recorder
   if !tc.capable{incoming=&evonomosP5BasicOnlyWriter{ResponseWriter:recorder}}
   _,actual:=incoming.(http.Flusher)
   if actual!=tc.capable{t.Fatal("input capability precondition failed")}
   e.ServeHTTP(incoming,httptest.NewRequest("GET","/capability",nil))
   expected:="absent"
   if tc.capable{expected="present"}
   if recorder.Code!=200||recorder.Body.String()!="probe"||
      recorder.Header().Get("X-EvoNOMOS-Underlying-Flusher")!=expected||recorder.Flushed{
    t.Fatalf("new contract cap=%t code=%d body=%q header=%q flushed=%t",
     tc.capable,recorder.Code,recorder.Body.String(),recorder.Header().Get("X-EvoNOMOS-Underlying-Flusher"),recorder.Flushed)
   }
   stillOld:=httptest.NewRecorder()
   e.ServeHTTP(stillOld,httptest.NewRequest("GET","/old",nil))
   if stillOld.Code!=200||stillOld.Body.String()!="old"{
    t.Fatalf("old contract drift")
   }
   t.Logf("P5_ECHO_NEW_OWNED_HANDLER sourceCapable=%t header=%s code200 probe noTransportFlush=true oldGET=true",tc.capable,expected)
  })
 }
}
