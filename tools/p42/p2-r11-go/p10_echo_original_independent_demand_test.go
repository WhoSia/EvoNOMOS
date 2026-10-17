package echo

import (
 "net/http"
 "net/http/httptest"
 "testing"
)

type evonomosP10BasicWriter struct{ http.ResponseWriter }

func TestEvoNOMOSP10EchoOptionalFlushClient(t *testing.T) {
 e := New()
 e.GET("/old", func(c *Context) error { return c.String(200,"old") })
 w:=httptest.NewRecorder()
 e.ServeHTTP(w, httptest.NewRequest("GET","/old",nil))
 if w.Code!=200 || w.Body.String()!="old" { t.Fatalf("old contract %d %q",w.Code,w.Body.String()) }
 e2:=New()
 e2.GET("/flush",func(c *Context) error {c.Response().Flush();return c.String(200,"after")})
 inner:=httptest.NewRecorder()
 var restricted http.ResponseWriter=&evonomosP10BasicWriter{ResponseWriter:inner}
 if _,ok:=restricted.(http.Flusher);ok {t.Fatal("unexpected input interface")}
 recovered:=false
 func(){defer func(){if recover()!=nil {recovered=true}}(); e2.ServeHTTP(restricted,httptest.NewRequest("GET","/flush",nil))}()
 if !recovered {t.Fatal("expected unsupported flush error by panic on original source")}
 supported:=httptest.NewRecorder()
 func(){defer func(){if x:=recover();x!=nil{t.Errorf("flush-capable recorder unexpected panic %v",x)}}();e2.ServeHTTP(supported,httptest.NewRequest("GET","/flush",nil))}()
 t.Log("ECHO_P10_NATIVE oldGET200 noFlusher=PANIC withFlusher=SUCCESS")
}
