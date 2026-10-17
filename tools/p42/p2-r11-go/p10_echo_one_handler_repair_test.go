package p10client

import (
 "net/http"
 "net/http/httptest"
 "testing"

 echo "github.com/labstack/echo/v5"
)

type p10RepairOnlyWriter struct{ http.ResponseWriter }

// Research-owned app handler, unchanged pinned Echo source.
func TestEvoNOMOSP10EchoGracefulOneHandlerRepair(t *testing.T) {
 e:=echo.New()
 e.GET("/old",func(c *echo.Context) error{return c.String(200,"old")})
 e.GET("/flush",func(c *echo.Context) error{
  u,ok:=c.Response().(interface{Unwrap() http.ResponseWriter})
  if !ok {t.Fatal("actual original Echo Response lacks Unwrap")}
  if _,supported:=u.Unwrap().(http.Flusher);supported{
   c.Response().(http.Flusher).Flush()
  }
  return c.String(200,"after")
 })
 old:=httptest.NewRecorder()
 e.ServeHTTP(old,httptest.NewRequest("GET","/old",nil))
 if old.Code!=200||old.Body.String()!="old"{t.Fatalf("old client %d %q",old.Code,old.Body.String())}
 inner:=httptest.NewRecorder()
 var basic http.ResponseWriter=&p10RepairOnlyWriter{ResponseWriter:inner}
 bad:=false
 func(){defer func(){if recover()!=nil{bad=true}}();e.ServeHTTP(basic,httptest.NewRequest("GET","/flush",nil))}()
 if bad||inner.Code!=200||inner.Body.String()!="after"{t.Fatalf("graceful demand failed bad=%t code=%d body=%q",bad,inner.Code,inner.Body.String())}
 capable:=httptest.NewRecorder()
 func(){defer func(){if x:=recover();x!=nil{t.Errorf("supported client error %v",x)}}();e.ServeHTTP(capable,httptest.NewRequest("GET","/flush",nil))}()
 if capable.Code!=200||capable.Body.String()!="after"{t.Fatal("supported contract mismatch")}
 t.Log("P10_ECHO_ONE_HANDLER_REPAIR oldGET200 gracefulNoFlusher=true withFlusher=PASS")
}
