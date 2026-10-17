package gin

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

type p10RepairOnlyWriter struct{ http.ResponseWriter }

// Research-owned handler replacement only; unmodified maintained Gin source.
func TestEvoNOMOSP10GinFailFastOneHandlerRepair(t *testing.T) {
 SetMode(TestMode)
 r:=New()
 r.GET("/old",func(c *Context){c.String(200,"old")})
 r.GET("/flush",func(c *Context){
  unwrap,ok:=interface{}(c.Writer).(interface{Unwrap() http.ResponseWriter})
  if !ok {t.Fatal("actual original Gin ResponseWriter lacks Unwrap")}
  if _,supported:=unwrap.Unwrap().(http.Flusher);!supported {
   panic("unsupported underlying Flusher for declared fail-fast client contract")
  }
  c.Writer.Flush()
  c.String(200,"after")
 })
 old:=httptest.NewRecorder()
 r.ServeHTTP(old,httptest.NewRequest("GET","/old",nil))
 if old.Code!=200||old.Body.String()!="old"{t.Fatalf("old contract %d %q",old.Code,old.Body.String())}
 input:=httptest.NewRecorder()
 var restricted http.ResponseWriter=&p10RepairOnlyWriter{ResponseWriter:input}
 panicSeen:=false
 func(){defer func(){if recover()!=nil{panicSeen=true}}();r.ServeHTTP(restricted,httptest.NewRequest("GET","/flush",nil))}()
 if !panicSeen{t.Fatal("research-owned Gin adapter failed fail-fast policy")}
 flushable:=httptest.NewRecorder()
 func(){defer func(){if v:=recover();v!=nil{t.Errorf("supported client panic %v",v)}}();r.ServeHTTP(flushable,httptest.NewRequest("GET","/flush",nil))}()
 if flushable.Code!=200||flushable.Body.String()!="after"{t.Fatal("supported output contract failure")}
 t.Log("P10_GIN_ONE_HANDLER_REPAIR oldGET200 failFastNoFlusher=true withFlusher=PASS")
}
