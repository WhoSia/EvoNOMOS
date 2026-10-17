package p10client

import (
 "net/http"
 "net/http/httptest"
 "testing"

 echo "github.com/labstack/echo/v5"
)

// Research-authored external client; the original Echo production source
// is imported verbatim at the pinned commit, without compiling old upstream tests.
type basicOnlyWriter struct{ http.ResponseWriter }

func TestEvoNOMOSP10EchoExternalSourceClient(t *testing.T) {
 e := echo.New()
 e.GET("/old", func(c *echo.Context) error { return c.String(200, "old") })
 w := httptest.NewRecorder()
 e.ServeHTTP(w, httptest.NewRequest(http.MethodGet, "/old", nil))
 if w.Code != 200 || w.Body.String() != "old" {
  t.Fatalf("old GET contract mismatch %d %q", w.Code, w.Body.String())
 }
 streaming := echo.New()
 streaming.GET("/flush", func(c *echo.Context) error {
  c.Response().(http.Flusher).Flush()
  return c.String(200, "after")
 })
 out := httptest.NewRecorder()
 var noFlush http.ResponseWriter = &basicOnlyWriter{ResponseWriter: out}
 if _, ok := noFlush.(http.Flusher); ok { t.Fatal("noFlush input precondition failed") }
 didPanic := false
 func() {
  defer func() { if recover() != nil { didPanic = true } }()
  streaming.ServeHTTP(noFlush, httptest.NewRequest(http.MethodGet, "/flush", nil))
 }()
 if !didPanic { t.Fatal("Echo original source expected to signal unsupported Flush") }
 okOut := httptest.NewRecorder()
 func() {
  defer func() { if recovered := recover(); recovered != nil { t.Errorf("unexpected supported Flush error: %v", recovered) } }()
  streaming.ServeHTTP(okOut, httptest.NewRequest(http.MethodGet, "/flush", nil))
 }()
 t.Log("ECHO_P10_NATIVE: oldGET=200/old, noFlush=PANIC, flushSupported=NO_PANIC")
}
