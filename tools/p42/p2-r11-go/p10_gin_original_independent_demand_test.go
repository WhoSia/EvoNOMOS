package gin

import (
    "net/http"
    "net/http/httptest"
    "testing"
)

// A real *Recorder supports Flush, but an interface-only wrapper does not:
// construct a genuine capability-absent client without changing Gin source.
type evonomosP10BasicOnlyWriter struct{ http.ResponseWriter }

func TestEvoNOMOSP10OriginalGinIndependentDemand(t *testing.T) {
    SetMode(TestMode)
    r := New()
    r.GET("/fixed", func(c *Context) { c.String(http.StatusOK, "old") })
    w := httptest.NewRecorder()
    r.ServeHTTP(w, httptest.NewRequest(http.MethodGet, "/fixed", nil))
    if w.Code != 200 || w.Body.String() != "old" {
        t.Fatalf("old client mismatch: %d %q", w.Code, w.Body.String())
    }

    r2 := New()
    r2.GET("/flush", func(c *Context) {
        c.Writer.Flush()
        c.String(http.StatusOK, "after")
    })
    out := httptest.NewRecorder()
    var basic http.ResponseWriter = &evonomosP10BasicOnlyWriter{ResponseWriter: out}
    if _, ok := basic.(http.Flusher); ok {
        t.Fatal("basic input unexpectedly implements Flusher")
    }
    didPanic := false
    func() {
        defer func() { if recover() != nil { didPanic = true } }()
        r2.ServeHTTP(basic, httptest.NewRequest(http.MethodGet, "/flush", nil))
    }()
    if didPanic { t.Fatal("Gin baseline unexpectedly panicked without underlying Flusher") }
    if out.Code != 200 || out.Body.String() != "after" {
        t.Fatalf("Gin no-Flusher output diverged: %d %q", out.Code, out.Body.String())
    }

    withFlush := httptest.NewRecorder()
    func() {
        defer func() {
            if rec := recover(); rec != nil { t.Fatalf("Gin recorder Flush panic: %v", rec) }
        }()
        r2.ServeHTTP(withFlush, httptest.NewRequest(http.MethodGet, "/flush", nil))
    }()
    t.Log("GIN_P10_NATIVE: oldGET=200/old, noFlush=NO_PANIC, flushSupported=NO_PANIC")
}
